from models.inventory import Inventory
from models.queue import VillageQueue
from models.bst import ItemBST
from models.village import Village
from models.item import Item

class GameManager:
    def __init__(self):
        self.inventory = Inventory()
        self.village_queue = VillageQueue()
        self.bst = ItemBST()
        self.rescued_villages = []
        self.current_village = None
        self.used_items = []
        self.ui_root = None
        self.setup_villages()

    def setup_villages(self):
        villages = [
            Village("Inkilap", [Item("Kilic", 10), Item("Yiyecek", 5), Item("Harita", 3)]),
            Village("Kosu", [Item("Balta", 12), Item("İksir", 8), Item("Altin", 7)]),
            Village("Sirinyer", [Item("Bicak", 9), Item("Kalkan", 11), Item("Mizrak", 10)]),
            Village("Kemer", [Item("Tuzak", 6), Item("Fener", 4), Item("Yay", 9)]),
            Village("Hilal", [Item("Kalkan", 11), Item("İksir", 8), Item("BuyuKitabi", 15)]),
            Village("Alsancak", [Item("Merhem", 5), Item("Tuz", 2), Item("Tirpan", 11)]),
            Village("Halkapinar", [Item("İksir", 8), Item("Balta", 12), Item("Ok", 7)])
        ]
        for v in villages:
            self.village_queue.enqueue(v)

    def register_used_item(self, item_name):
        if item_name not in self.used_items:
            self.used_items.append(item_name)

    def rescue_next_village(self):
        from tkinter import simpledialog
        from ui.remove_item_popup import show_item_removal_popup

        village = self.village_queue.peek()
        if not village:
            print("Kurtarilacak koy kalmadi.")
            return None

        requirements = {
            "Hilal": ["BuyuKitabi", "Ok"],
            "Alsancak": ["İksir", "Yay"],
            "Halkapinar": ["Balta", "Kalkan"]
        }

        if village.name in requirements:
            cevap = simpledialog.askstring("Gereken Esyalar", f"{village.name} icin hangi esyalari kullaniyorsun? (virgul ile):")
            if not cevap:
                print(" Cevap girilmedi.")
                return None

            girilen = [x.strip().lower() for x in cevap.split(",")]
            gereken = [x.lower() for x in requirements[village.name]]

            if sorted(girilen) != sorted(gereken):
                print(f" {village.name} icin eksik veya yanlis esya girdin.")
                return None

        self.village_queue.dequeue()
        print(f" {village.name} basariyla kurtarildi!")
        self.rescued_villages.append(village.name)
        self.current_village = village.name

        for item in village.items:
            while self.inventory.is_full():
                item_names = [str(itm) for itm in self.inventory.list_items()]
                idx = show_item_removal_popup(self.ui_root, item_names)
                if idx is not None:
                    removed_item = self.inventory.remove_by_index(idx)
                    print(f" {removed_item.name} cikarildi.")
                else:
                    print(f" Yeni esya eklenmedi.")
                    break

            if not self.inventory.is_full():
                self.inventory.push(item)
                self.bst.insert(item)
                print(f" Canta eklendi: {item.name}")

        return village

    def show_progress(self):
        print(" Su anki koy:", self.current_village)
        print(" Kurtarilan koyler:", self.rescued_villages)
        print(" Kalan koyler:", [v.name for v in self.village_queue.list_villages()])

    def search_item(self, item_name):
        result = self.bst.search(item_name)
        found_in = None

        for name in self.rescued_villages:
            for v in self.inventory.list_items():
                if v.name.lower() == item_name.lower():
                    found_in = name
                    break

        if result:
            if found_in:
                print(f" {item_name} bulundu → Guc: {result.power} – Kazanilan koy: {found_in}")
            else:
                for v in self.village_queue.list_villages():
                    for it in v.items:
                        if it.name.lower() == item_name.lower():
                            print(f" {item_name} henuz kazanilmadi. {v.name} kurtarilirsa elde edilecek.")
                            return
                print(f" {item_name} bulundu → Guc: {result.power}")
        else:
            print(f" {item_name} bulunamadi.")
