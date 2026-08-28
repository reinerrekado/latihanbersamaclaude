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

- **Update terakhir:** 2026-08-29
- **Sedang di file:** `python-exercise-materials/collection-data-type/06_indexing_and_slicing.py`
- **Progress modul collection-data-type (1 dari 6 modul python):**
  - ✅ `01_python_list_basics.py` — selesai
  - ✅ `02_python_list_methods.py` — selesai
  - ✅ `03_list_comprehension.py` — selesai (termasuk latihan tambahan filter ganjil +100)
  - ✅ `04_python_tuple.py` — selesai (creation, indexing, immutability, tuple kosong, nested tuple, trik koma 1 item)
  - ✅ `05_tuple_methods.py` — selesai (`.count()`, `.index()`, `len()`, error saat value tidak ditemukan)
  - ⬜ `06_indexing_and_slicing.py` s.d. `12_dictionary_access_update.py` — belum dimulai (7 file lagi)
- **Modul python lain yang BELUM disentuh sama sekali:** `conditional-and-loop-statements` (11 file), `data-manipulation-pandas-numpy` (11 file, butuh pandas/numpy), `object-oriented-programming` (4 file), `python-function-and-file-handling` (5 file), `python-modular-programming` (9 bagian, proyek multi-file)
- **SQL (`sql-exercise-materials-`) belum disentuh sama sekali:** modul "9 - Introduction to Databases and SQL" (14 file demo + exercises) dan modul "10 - SQL Working with Multiple Tables" (6 file demo + exercises)
- **Deadline:** ujian materi dari **kedua repo** pada **2026-09-01** (H-3 dari tanggal update ini)
- **Assessment learning curve (jujur, per 2026-08-29):** Pemahaman konsep BAGUS dan makin cepat — sesi ini berhasil membereskan gap fondasi (assignment operator vs fungsi vs tipe data, method vs fungsi) yang sebelumnya bikin banyak hal terasa random. Begitu fondasi itu klik, soal-soal berikutnya (nested tuple, methods) langsung dijawab benar tanpa perlu diulang. **Tapi dari sisi kecepatan/volume: ini risiko serius untuk deadline 09-01.** 1 sesi belajar mendalam (dengan tanya-jawab step-by-step) baru menghasilkan ~3 file di 1 dari 6 modul python — sementara total sisa materi (~7 file collection-data-type + ~40 file di 5 modul python lain + ~20 file SQL) jauh lebih banyak dari yang realistis dikerjakan dengan kedalaman yang sama dalam 2 hari tersisa.
  - **Rekomendasi:** untuk sisa waktu, pertimbangkan pola belajar dua kecepatan — (a) topik yang terasa baru/asing → tetap pelan, predict-then-verify + breakdown fondasi kayak sesi ini; (b) topik yang pola-nya mirip yang sudah dikuasai (misal set/dictionary setelah paham list & tuple) → boleh dipercepat, cukup soal ringkas tanpa breakdown fondasi ulang. Juga pertimbangkan cek dulu **format ujian sebenarnya** (pilihan ganda konsep vs praktik nulis kode) supaya bisa prioritaskan materi yang paling relevan duluan, bukan urutan file secara berurutan.
- **Catatan gaya belajar:** lihat detail lengkap di memory Claude Code (`learning_style`, `user_background`) — ringkasnya: prefer coba jawab dulu (predict-then-verify) KECUALI mengaku belum paham suatu topik, baru dijelaskan dulu; user tidak punya background IT (SMA IPS, kuliah Ilmu Politik, kerja digital marketing & supply chain) jadi butuh analogi non-teknis dan penjelasan eksplisit untuk hal yang "obvious" bagi orang IT.

## Catatan Command Berguna

- `claude --continue` → lanjutkan sesi Claude Code terakhir **di PC yang sama** (tidak lintas perangkat)
- `claude --resume` → pilih dari sesi-sesi sebelumnya **di PC yang sama**
- `git status` → cek ada perubahan belum ter-commit atau tidak
- `git pull` → tarik update terbaru dari GitHub sebelum mulai kerja
- `git push` → kirim perubahan ke GitHub supaya bisa diambil dari perangkat lain
