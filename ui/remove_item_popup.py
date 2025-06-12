import tkinter as tk
from tkinter import simpledialog

def show_item_removal_popup(root, items):
    selected_index = []

    def on_select():
        try:
            selected_index.append(listbox.curselection()[0])
            top.destroy()
        except IndexError:
            pass  # hiçbir şey seçilmezse çıkma

    top = tk.Toplevel(root)
    top.title("Çanta Dolu – Bir Eşya Çıkar")

    label = tk.Label(top, text="Hangi öğeyi çıkarmak istersin?", font=("Arial", 10))
    label.pack(pady=5)

    listbox = tk.Listbox(top, selectmode=tk.SINGLE, width=30)
    for item in items:
        listbox.insert(tk.END, item)
    listbox.pack(pady=5)

    button = tk.Button(top, text="Seç ve Çıkar", command=on_select)
    button.pack(pady=5)

    top.grab_set()
    top.mainloop()

    return selected_index[0] if selected_index else None