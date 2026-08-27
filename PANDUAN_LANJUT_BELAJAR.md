# Panduan Lanjut Belajar dengan Claude Code

Panduan end-to-end supaya sesi belajar bisa lanjut mulus dari perangkat mana pun (PC atau laptop), karena riwayat chat Claude Code **tidak** otomatis pindah antar perangkat — file ini yang menjaga kontinuitasnya.

---

## A. Setup Awal (sekali saja per perangkat baru, misal laptop besok)

1. Buka **VS Code**.
2. Buka terminal di dalamnya (`` Ctrl+` ``).
3. Kalau folder project **belum ada** di perangkat itu:
   ```
   git clone https://github.com/reinerrekado/latihanbersamaclaude.git
   ```
4. Kalau folder project **sudah ada** (misal ikut sync OneDrive): buka folder itu langsung via `File > Open Folder`.
5. Pastikan ekstensi **Claude Code** terpasang di VS Code, lalu login dengan akun Anda kalau diminta.

## B. Tiap Kali Mau Mulai Sesi Belajar

1. Buka VS Code, buka folder project ini.
2. Buka terminal, jalankan:
   ```
   git pull
   ```
   supaya file terbaru (termasuk panduan ini) ter-update.
3. Buka panel **Claude Code**, mulai chat baru.
4. Cukup bilang sesuatu seperti:
   > "Lanjutkan belajar, cek bagian Status Belajar Terakhir di PANDUAN_LANJUT_BELAJAR.md"
5. Kerjakan latihan seperti biasa — pola predict-then-verify: coba jawab dulu, baru dicocokkan dengan menjalankan kode.

## C. Sebelum Menutup Sesi

1. Kalau ada perubahan file (kode latihan baru, dll), commit & push:
   ```
   git add .
   git commit -m "progress belajar: <singkat, misal 'selesai file 03'>"
   git push
   ```
2. Minta Claude update bagian **Status Belajar Terakhir** di bawah ini supaya sesi berikutnya (di perangkat mana pun) tahu harus lanjut dari mana.
3. Tutup VS Code.

---

## Status Belajar Terakhir

*(diperbarui tiap akhir sesi — jangan dihapus, cukup ditimpa isinya)*

- **Update terakhir:** 2026-08-28
- **Sedang di file:** `python-exercise-materials/collection-data-type/03_list_comprehension.py`
- **Progress modul collection-data-type:**
  - ✅ `01_python_list_basics.py` — selesai (list creation, indexing 0-based, IndexError, nested list)
  - ✅ `02_python_list_methods.py` — selesai (append/insert/remove/pop/clear, copy vs reference, extend vs append)
  - 🟡 `03_list_comprehension.py` — hampir selesai, **tinggal Soal 4**: menulis sendiri list comprehension untuk filter angka genap dari `numbers = [3, 8, 15, 20, 7, 42]` lalu dikalikan 2 (percobaan terakhir masih salah nama variabel & operator)
  - ⬜ `04_python_tuple.py` s.d. `12_dictionary_access_update.py` — belum dimulai
- **Deadline:** ujian materi dari **kedua repo** (`python-exercise-materials` + `sql-exercise-materials`) pada **2026-09-01**
- **Catatan gaya belajar:** lebih suka coba jawab dulu sebelum dikasih penjelasan; kalau bilang "bingung"/"lost", minta breakdown lebih pelan (per langkah/tabel), bukan diulang penjelasan yang sama

## Catatan Command Berguna

- `claude --continue` → lanjutkan sesi Claude Code terakhir **di PC yang sama** (tidak lintas perangkat)
- `claude --resume` → pilih dari sesi-sesi sebelumnya **di PC yang sama**
- `git status` → cek ada perubahan belum ter-commit atau tidak
- `git pull` → tarik update terbaru dari GitHub sebelum mulai kerja
- `git push` → kirim perubahan ke GitHub supaya bisa diambil dari perangkat lain
