import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tkinter as tk
from tkinter import messagebox, simpledialog
from services.game_manager import GameManager

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Koy Kurtarma Oyunu")
        self.game = GameManager()
        self.game.ui_root = self.root  # GUI ile item cikarma desteği

        self.label_status = tk.Label(root, text="🏞️ Hos geldin, Oyuna basla.", font=("Arial", 12))
        self.label_status.pack(pady=10)

        self.btn_rescue = tk.Button(root, text="1. Koyu Kurtar", width=25, command=self.rescue_village)
        self.btn_rescue.pack(pady=5)

        self.btn_inventory = tk.Button(root, text="2. Cantayi Goster", width=25, command=self.show_inventory)
        self.btn_inventory.pack(pady=5)

        self.btn_use_item = tk.Button(root, text="3. Esya Kullan", width=25, command=self.use_item)
        self.btn_use_item.pack(pady=5)

        self.btn_progress = tk.Button(root, text="4. İlerleme Durumu", width=25, command=self.show_progress)
        self.btn_progress.pack(pady=5)

        self.btn_search = tk.Button(root, text="5. BST ile Esya Ara", width=25, command=self.search_item)
        self.btn_search.pack(pady=5)

        self.btn_map = tk.Button(root, text="6. Harita / Gereksinimler", width=25, command=self.show_map_info)
        self.btn_map.pack(pady=5)

        self.btn_exit = tk.Button(root, text="0. Cik", width=25, command=root.quit)
        self.btn_exit.pack(pady=10)

    def rescue_village(self):
        village = self.game.rescue_next_village()
        if village:
            messagebox.showinfo("Basarili", f"{village.name} koyu basariyla kurtarildi")

    def show_inventory(self):
        items = self.game.inventory.list_items()
        if not items:
            messagebox.showinfo("canta", "canta bos.")
        else:
            item_list = "\n".join(str(item) for item in items)
            messagebox.showinfo("canta icerigi", item_list)

    def use_item(self):
        name = simpledialog.askstring("Esya Kullan", "Kullanmak istedigin esya:")
        if name:
            used = self.game.inventory.use_item(name)
            if used:
                self.game.register_used_item(name)

    def show_progress(self):
        current = self.game.current_village or "Henuz baslanmadi"
        rescued = ", ".join(self.game.rescued_villages) or "Yok"
        remaining = ", ".join([v.name for v in self.game.village_queue.list_villages()]) or "Kalmadi"
        message = f" su anki koy: {current}\n Kurtarilanlar: {rescued}\n Kalanlar: {remaining}"
        messagebox.showinfo("İlerleme", message)

    
    def search_item(self):
        name = simpledialog.askstring("Esya Ara", "Aramak istedigin esya:")
        if name:
            self.game.search_item(name)
        else:
                messagebox.showinfo("Sonuc", f"{name} bulunamadi")

    def show_map_info(self):
        map_window = tk.Toplevel(self.root)
        map_window.title("Harita ve Kurtarma Gereksinimleri")

        requirements = {
            "Hilal": ["Buyu Kitabi", "Ok"],
            "Alsancak": ["İksir", "Yay"],
            "Halkapinar": ["Balta", "Kalkan"]
        }

        all_villages = self.game.rescued_villages + [v.name for v in self.game.village_queue.list_villages()]
        for i, name in enumerate(all_villages):
            needs = requirements.get(name, [])
            need_text = "Yok" if not needs else ", ".join(needs)
            label = tk.Label(map_window, text=f"{i+1}. {name} – Gereken: {need_text}", font=("Arial", 10))
            label.pack(anchor="w", padx=10, pady=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()