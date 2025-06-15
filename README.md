# 🛡️ Village Rescue Game with BST

Village Rescue Game, Python kullanılarak geliştirilmiş ve temel veri yapılarıyla desteklenen bir 2D macera oyunudur. Oyuncu, belirli eşyaları toplayarak köyleri sırayla kurtarır. Oyun; Binary Search Tree (BST), Queue (Kuyruk), Stack (Yığın) gibi yapılarla veri yapıları öğrenimini eğlenceli hâle getirir.

## 🎮 Oynanış
- Her köy belirli eşya gereksinimlerine sahiptir.
- Gerekli eşyalara sahipsen köy kurtarılır ve yeni eşyalar kazanırsın.
- Envanterin sınırlıdır, dikkatli yönet!
- Köy ilerlemesi kuyruk (Queue), envanter yığın (Stack), eşya arama ise BST ile yönetilir.

---

## 🧱 Kullanılan Veri Yapıları
- **Stack** → Envanter sistemi (`models/inventory.py`)
- **Queue** → Köy ilerleme sırası (`models/queue.py`)
- **Binary Search Tree (BST)** → Eşya sıralama ve arama (`models/bst.py`)

---

## 🧰 Teknolojiler
- Python 3.x
- Tkinter (UI için)
- Standart Python (harici kütüphane gerektirmez)

---

## 🚀 Kurulum ve Çalıştırma

### 1. Kurulum
Python 3 yüklü değilse: [https://python.org](https://python.org)  
Daha sonra terminalden şu adımları uygula:

```bash
git clone https://github.com/devberatzengin/VillageRescueGameWithBst.git
cd VillageRescueGameWithBst/village_rescue_game
```

---

### 2. UI ile Çalıştırma (Görsel Arayüz)
Oyunu grafik arayüzle oynamak için:

```bash
python -m ui.app_ui
```

Tkinter ile hazırlanmış arayüz açılır. Tıklanabilir köyler, eşya seçme ekranları ve envanter yönetimi görsel olarak sunulur.

---

### 3. Konsol Üzerinden Çalıştırma (Terminal Oynanışı)
Görsel arayüz yerine direkt terminal üzerinden oynamak için:

```bash
python main.py
```

Bu mod, UI olmadan oynanır ve tüm süreçler metin tabanlı olarak ilerler. Veri yapılarının nasıl çalıştığını görmek için faydalıdır.

---

## 📂 Klasör Yapısı
```
village_rescue_game/
├── main.py                  # (Varsa ekstra giriş noktası)
├── models/                  # Veri yapıları (BST, Queue, Stack)
├── services/                # Oyun mantığı (GameManager)
│   └── game_manager.py
├── ui/                      # Tkinter tabanlı kullanıcı arayüzü
│   └── app_ui.py
```

---

## 👤 Geliştirici
- Berat Zengin - [GitHub](https://github.com/devberatzengin)

---

## 📜 Lisans
MIT License
