# 🛡️ Village Rescue Game with BST

Village Rescue Game, Python kullanılarak geliştirilmiş ve temel veri yapılarıyla desteklenen bir 2D macera oyunudur. Oyuncu, belirli eşyaları toplayarak köyleri sırayla kurtarır. Oyun; Binary Search Tree (BST), Queue (Kuyruk), Stack (Yığın) gibi yapılarla veri yapıları öğrenimini eğlenceli hâle getirir.

## 🎮 Oynanış
- Her köy belirli eşya gereksinimlerine sahiptir.
- Gerekli eşyalara sahipsen köy kurtarılır ve yeni eşyalar kazanırsın.
- Envanterin sınırlıdır, dikkatli yönet!
- İlerleme sırası bir kuyrukla tutulur, eşyalar yığın yapısında saklanır.
- Eşyaların yönetimi ve sıralaması BST ile sağlanır.

## 🧱 Kullanılan Veri Yapıları
- **Stack** → Envanter sistemi (`inventory.py`)
- **Queue** → Köy ilerleme sırası (`queue.py`)
- **Binary Search Tree (BST)** → Eşya sıralama ve arama (`bst.py`)

## 🧰 Teknolojiler
- Python 3
- Tkinter (görsel arayüz)
- Custom veri yapısı sınıfları (kütüphane kullanılmadan sıfırdan yazıldı)

## 🚀 Kurulum
```bash
git clone https://github.com/devberatzengin/VillageRescueGameWithBst.git
cd VillageRescueGameWithBst
python main.py
```

## 📂 Klasör Yapısı
```
village_rescue_game/
├── main.py                 # Oyunun giriş noktası
├── models/                 # Veri yapıları (BST, Stack, Queue)
├── services/               # Oyun mantığı (GameManager)
├── ui/                     # Arayüz (Tkinter tabanlı)
```

## 📸 Ekran Görüntüsü
*(Buraya oyun ekranından bir görsel eklersen çok iyi olur)*

## 👤 Geliştirici
- Berat Zengin - [GitHub](https://github.com/devberatzengin)

## 📜 Lisans
MIT License
