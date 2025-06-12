from services.game_manager import GameManager

def main():
    game = GameManager()

    while True:
        print("\n=== KOY KURTARMA OYUNU ===")
        print("1. Siradaki Koyu Kurtar")
        print("2. Cantayi Goster")
        print("3. Ogeyi Kullan")
        print("4. Ilerleme Durumunu Goster")
        print("5. Esya Ara (BST)")
        print("0. Cikis")

        secim = input("Seciminiz: ")

        if secim == "1":
            game.rescue_next_village()
        elif secim == "2":
            print("\n CANTA:")
            for item in game.inventory.list_items():
                print(f"- {item}")
        elif secim == "3":
            isim = input("Kullanilacak esya adi: ")
            kullanilan = game.inventory.use_item(isim)
            if kullanilan:
                game.register_used_item(isim)
        elif secim == "4":
            game.show_progress()
        elif secim == "5":
            aranan = input("Aranacak esya adi: ")
            game.search_item(aranan)
        elif secim == "0":
            print("Oyun kapatiliyor...")
            break
        else:
            print("Gexersiz secim.")

if __name__ == "__main__":
    main()
