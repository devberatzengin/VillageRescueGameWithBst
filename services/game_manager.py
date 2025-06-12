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
            Village("Inkilap", [Item("Lav", 10), Item("Kilic", 10), Item("OK", 7)]),
            Village("Kosu", [Item("Yay", 8), Item("Kalkan", 11), Item("Elmas", 10)]),
            Village("Sirinyer", [Item("Kazma", 9), Item("Cubuk", 4), Item("Altin", 7)]),
            Village("Kemer", [Item("Demir", 6), Item("Kurek", 5), Item("Harita", 3)]),
            Village("Hilal", [Item("Kalkan", 11), Item("Lav", 10), Item("TNT", 9)]),
            Village("Alsancak", [Item("Kazma", 9), Item("TNT", 8), Item("Elma", 6)]),
            Village("Halkapinar", [Item("CakmakTasi", 5), Item("Mesale", 4), Item("KizilTas", 3)])
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
            "Hilal": ["Lav", "Kalkan"],
            "Alsancak": ["Kazma", "TNT"],
            "Halkapinar": ["CakmakTasi", "KizilTas"]
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
