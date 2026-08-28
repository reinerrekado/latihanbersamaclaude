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
- **Jadwal & scope resmi (dari dokumen briefing, update 2026-08-29):**
  - **Exam 1** — pilihan ganda, berbahasa Inggris, via purwadhika.com, materi python & SQL **modul 1**. **Selasa, 2026-09-01, 19:30-21:00 WIB.** Ini yang butuh materi matang (konsep, bukan hanya bisa jalanin kode).
  - **Code Challenge 1 (CC1)** — jauh lebih ringan dari perkiraan sebelumnya: cuma **4 soal LeetCode** (3 Easy @20 poin + 1 Medium @40 poin = 100 poin, soal dipilih bebas). Bukti: link akun LeetCode + screenshot status "Accepted" per soal, submit via Google Form. **Deadline: Kamis, 2026-09-03.** Independen dari progress modul di repo ini — boleh dikerjakan kapan saja, tidak perlu nunggu modul beres, dan bisa diselesaikan setelah Exam 1.
- **Assessment learning curve (revisi 2026-08-29, setelah scope CC diklarifikasi):** Pemahaman konsep BAGUS dan makin cepat — sesi pertama berhasil membereskan gap fondasi (assignment operator vs fungsi vs tipe data, method vs fungsi) yang sebelumnya bikin banyak hal terasa random. Begitu fondasi itu klik, soal berikutnya (nested tuple, tuple methods) langsung dijawab benar tanpa perlu diulang.
  - Risiko waktu **masih ada tapi lebih terkendali** dari penilaian sebelumnya, karena CC1 (4 soal LeetCode) ternyata beban ringan dan **terpisah** dari materi Exam 1 — jadi sisa waktu belajar (29-31 Agustus) bisa fokus **hampir sepenuhnya** ke penguatan materi Exam: lanjutan `collection-data-type`, `conditional-and-loop-statements`, `object-oriented-programming`, `python-function-and-file-handling`, `python-modular-programming`, plus dua modul SQL (`9 - Introduction to Databases and SQL`, `10 - SQL Working with Multiple Tables`). Modul `data-manipulation-pandas-numpy` prioritas lebih rendah kalau memang di luar cakupan "modul 1".
  - **UPDATE 2026-08-29 (sore) — sumber baru ditemukan, pertanyaan di atas terjawab:** ada file `CLAUDE.MD.md` di root repo ini (~658KB), rangkuman lengkap dari notes Obsidian milik tutor, isinya **13 sesi Module 1**:
    1. Introduction to DS, Python, Statistics, SQL, Git & GitHub
    2. Intro to Git & GitHub
    3. Conditional & Loop Statement
    4. Data Types Collection Notes
    5. Python Function & File Handling
    6. Hackerrank Exercise
    7. Object Oriented Programming
    8. Python & Modular Programming
    9. Intro to Database & SQL
    10. SQL Working With Multiple Tables
    11. Statistics Fundamental
    12. Python Data Manipulation With Pandas and Numpy
    13. Data Visualization
    - **Konfirmasi:** Sesi 9 & 10 di sini memang sama dengan folder `9 -...` dan `10 -...` di `sql-exercise-materials-`.
    - **Relasi dengan repo kode:** menurut user, file `.py`/`.sql` di kedua repo exercise itu **bukan kurikulum terpisah** — itu adalah "papan tulis & kertas latihan" (demo + skeleton exercise) yang dipakai tutor pas ngajar sesi-sesi di atas. Jadi satu kesatuan: `CLAUDE.MD.md` = catatan konsep, file kode = praktik langsung, untuk sesi yang sama.
    - **Gap penting:** Sesi **2 (Git & GitHub)**, **11 (Statistics Fundamental)**, dan **13 (Data Visualization)** **tidak punya file kode sama sekali** di kedua repo — satu-satunya sumber belajar untuk 3 sesi ini adalah `CLAUDE.MD.md`. Sesi **1** & **6 (Hackerrank)** juga sebagian besar cuma ada di notes, bukan file kode terstruktur.
  - **Prioritas belajar direvisi (per keputusan user, 2026-08-29 sore):** dahulukan sesi yang **sama sekali belum tersentuh** — Sesi 2, 11, 13 (baca dari `CLAUDE.MD.md`, breadth-first karena exam MCQ) — baru lanjut sesi yang punya pasangan notes+kode (mulai dari Sesi 4/`collection-data-type` yang sedang jalan, lalu 3, 5, 7, 8, 9, 10, 12) sambil gabungkan baca notes + jalanin kode.
  - **Rekomendasi pacing:**
    1. Karena Exam 1 **pilihan ganda** (bukan praktik nulis kode), prioritaskan **breadth dulu** — pastikan semua topik di scope kesentuh minimal di level konsep, baru dalami yang terasa lemah. Jangan lama-lama di satu file kalau polanya sudah familiar.
    2. Dua kecepatan belajar: topik baru/asing → tetap pelan (predict-then-verify + breakdown fondasi seperti sesi ini). Topik yang mirip yang sudah dikuasai (misal `set`/`dictionary` setelah paham `list`/`tuple`) → dipercepat, soal ringkas tanpa breakdown fondasi ulang.
    3. Karena Exam berbahasa Inggris, sambil belajar boleh sekalian biasakan istilah teknis dalam bahasa Inggris (nama konsep, pesan error) — materi di repo ini kebetulan sudah berbahasa Inggris.
    4. **CC1 (4 soal LeetCode) diselipkan terpisah**, kapan saja sebelum 2026-09-03, tidak perlu dikerjakan sebelum Exam 1 dan tidak mengurangi jatah waktu belajar materi Exam di 29-31 Agustus.
- **Catatan gaya belajar:** lihat detail lengkap di memory Claude Code (`learning_style`, `user_background`) — ringkasnya: prefer coba jawab dulu (predict-then-verify) KECUALI mengaku belum paham suatu topik, baru dijelaskan dulu; user tidak punya background IT (SMA IPS, kuliah Ilmu Politik, kerja digital marketing & supply chain) jadi butuh analogi non-teknis dan penjelasan eksplisit untuk hal yang "obvious" bagi orang IT.

## Catatan Command Berguna

- `claude --continue` → lanjutkan sesi Claude Code terakhir **di PC yang sama** (tidak lintas perangkat)
- `claude --resume` → pilih dari sesi-sesi sebelumnya **di PC yang sama**
- `git status` → cek ada perubahan belum ter-commit atau tidak
- `git pull` → tarik update terbaru dari GitHub sebelum mulai kerja
- `git push` → kirim perubahan ke GitHub supaya bisa diambil dari perangkat lain
