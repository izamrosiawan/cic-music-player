# CIC Music Player (Desktop Audio GUI Application)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet.svg)](https://customtkinter.tomschimansky.com/)
[![Pygame](https://img.shields.io/badge/Audio-Pygame%20Mixer-orange.svg)](https://www.pygame.org/)
[![Tests](https://img.shields.io/badge/Tests-Pytest%20Passing-brightgreen.svg)](#)

---

## 1. Deskripsi Proyek

Aplikasi pemutar musik desktop berbasis antarmuka grafis modern (**CustomTkinter**) dan backend audio (**Pygame Mixer**) yang mengimplementasikan struktur data *Doubly Linked List / Hierarchical Node Graph* untuk mengelola relasi artis, album, dan daftar putar lagu (*playlist*).

---

## 2. Struktur Repositori

```text
cic-music-player/
├── .gitignore          # Konfigurasi pengabaian cache Git
├── main/               # Kode sumber aplikasi desktop
│   ├── gui_main.py     # Entry point GUI aplikasi
│   ├── page_user.py    # Halaman interface pemutar musik pengguna
│   ├── page_admin.py   # Halaman manajemen lagu & album admin
│   ├── sistem.py       # Struktur data node & logika pemutar audio
│   └── data_dummy.py   # Inisialisasi database lagu lokal
├── tests/              # Automated unit tests (Pytest)
├── requirements.txt    # Pinned stable dependencies
└── README.md           # Laporan utama & panduan aplikasi
```

---

## 3. Pengujian Otomatis

Jalankan pengujian struktur data node musik:

```bash
pytest tests/
```

---

## 4. Cara Menjalankan

1. **Pasang Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Eksekusi Aplikasi**:
   ```bash
   python main/gui_main.py
   ```

---
*CIC Desktop Music Player Project.*
