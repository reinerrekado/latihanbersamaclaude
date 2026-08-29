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

### Checklist Materi Exam 1 (13 Sesi Module 1)

*(centang = konsep sesi sudah divalidasi quiz+retest solid, cukup buat exam pilihan ganda. Kode praktik itu bonus penguatan, bukan syarat centang — lihat sub-baris di sesi yang masih jalan.)*

**Progress: 5 / 13 sesi solid (~38%)**

- [x] Sesi 1 — Intro DS, Python, Statistics, SQL, Git & GitHub *(self-test web 90%)*
- [x] Sesi 2 — Intro to Git & GitHub *(quiz+retest Claude Code, solid)*
- [x] Sesi 3 — Conditional & Loop Statement *(konsep solid, self-test web 50%→ditambal→retest sukses; kode praktik `conditional-and-loop-statements/` masih 0/11 file — opsional buat penguatan, bukan syarat centang)*
- [x] Sesi 4 — Data Types Collection Notes *(konsep solid, self-test web 30%→ditambal→retest sukses; kode praktik `collection-data-type/` 5/12 file selesai — opsional buat penguatan, bukan syarat centang)*
- [ ] Sesi 5 — Python Function & File Handling
- [ ] Sesi 6 — Hackerrank Exercise
- [ ] Sesi 7 — Object Oriented Programming
- [ ] Sesi 8 — Python & Modular Programming
- [ ] Sesi 9 — Intro to Database & SQL
- [ ] Sesi 10 — SQL Working With Multiple Tables
- [x] Sesi 11 — Statistics Fundamental *(quiz+retest Claude Code, solid)*
- [ ] Sesi 12 — Python Data Manipulation With Pandas and Numpy
- [ ] Sesi 13 — Data Visualization

### Checklist Code Challenge 1 (terpisah, deadline 2026-09-03)

- [ ] Soal Easy #1 (LeetCode, Accepted)
- [ ] Soal Easy #2 (LeetCode, Accepted)
- [ ] Soal Easy #3 (LeetCode, Accepted)
- [ ] Soal Medium #1 (LeetCode, Accepted)
- [ ] Submit link akun LeetCode + screenshot Accepted via Google Form

---

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
  - **UPDATE 2026-08-29 (sore) — sumber baru ditemukan, pertanyaan di atas terjawab:** ada file `RANGKUMAN_MODULE_1.md` di root repo ini (~658KB), rangkuman lengkap dari notes Obsidian milik tutor, isinya **13 sesi Module 1**:
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
    - **Relasi dengan repo kode:** menurut user, file `.py`/`.sql` di kedua repo exercise itu **bukan kurikulum terpisah** — itu adalah "papan tulis & kertas latihan" (demo + skeleton exercise) yang dipakai tutor pas ngajar sesi-sesi di atas. Jadi satu kesatuan: `RANGKUMAN_MODULE_1.md` = catatan konsep, file kode = praktik langsung, untuk sesi yang sama.
    - **Gap penting:** Sesi **2 (Git & GitHub)**, **11 (Statistics Fundamental)**, dan **13 (Data Visualization)** **tidak punya file kode sama sekali** di kedua repo — satu-satunya sumber belajar untuk 3 sesi ini adalah `RANGKUMAN_MODULE_1.md`. Sesi **1** & **6 (Hackerrank)** juga sebagian besar cuma ada di notes, bukan file kode terstruktur.
    - **Asal-usul `RANGKUMAN_MODULE_1.md`:** bukan modul mentah dari Purwadhika — hasil digest 3 tahap oleh user: (1) **NotebookLM** menggabungkan transcript rekaman kelas + PDF modul resmi → rangkuman yang juga menangkap insight lisan dosen yang tidak tertulis di PDF (muncul sebagai bagian **"[Wawasan Diskusi / Audio Insight]"**), (2) distrukturkan di **Obsidian** per sesi dengan internal linking, (3) dipakai di **Claude (web & Code)** untuk retrieval practice/quiz, bukan buat dibaca ulang pasif. **Implikasi penting:** bagian "[Wawasan Diskusi / Audio Insight]" di tiap Bab sering berisi nuansa/klarifikasi yang TIDAK ada di PDF modul asli — dosen biasanya menekankan itu lisan karena sering jadi kesalahpahaman siswa, jadi ini kandidat kuat soal jebakan Exam 1. **Prioritaskan bagian ini saat bikin soal quiz atau menjelaskan konsep dari notes.**
  - **Progress lintas platform — self-test via Claude Web (malam, 2026-08-29):** selain progress file kode di atas, sudah ada sesi retrieval practice (predict-then-verify via quiz) terpisah di Claude web (bukan Claude Code) untuk 3 dari 13 sesi:
    - **Sesi 1** (Intro Python/DS/Stats/SQL/Git) — self-test **90%** (setelah 2x percobaan) → **SOLID, tidak perlu diulang.**
    - **Sesi 3** (Conditional & Loop) — self-test awal 50%, gap sudah ditambal & retest sukses: `range(start,stop,step)` params, default dict iteration (keys only, bukan error), pola "dead code" di if-elif-else (bukan error meski kondisi overlap).
    - **Sesi 4** (Data Types Collection) — self-test awal 30%, gap sudah ditambal & retest sukses: indexing vs slicing out-of-range (IndexError vs return kosong), `.remove()` vs `.discard()` (error vs aman), `.setdefault()` vs `.update()` (defensif vs menimpa), `sorted(dict)` cuma sort keys, tuple tanpa koma `(5)` jadi int, `==` vs `is` setelah `.copy()`.
    - **Pola penting:** skor self-test awal rendah (30-50%) **bukan** tanda gagal paham konsep besar — begitu satu gap dijelaskan sekali, langsung retest sukses. Lanjutkan pola "coba dulu → salah → koreksi eksplisit" ini untuk sesi 5-13, jangan ganti ke "baca teori dulu sampai yakin".
    - **Sesi yang BELUM disentuh sama sekali (baik notes maupun quiz, di platform manapun):** 2 (Git), 5 (Function/File Handling), 6 (Hackerrank), 7 (OOP), 8 (Modular), 9-10 (SQL), 11 (Statistics), 12 (Pandas/Numpy), 13 (Data Viz).
    - **PENTING untuk sesi Claude Code manapun:** progress belajar bisa terjadi di Claude Web juga, dan **Claude Code tidak bisa membaca riwayat chat Claude Web secara otomatis**. Jangan asumsikan sesi yang "belum di-quiz di sini" berarti "belum ada progress apa-apa" — **tanya dulu ke user** apakah sudah ada sesi self-test di platform lain sebelum mulai dari nol.
  - **Prioritas belajar direvisi (per keputusan user, 2026-08-29 sore):** dahulukan sesi yang **sama sekali belum tersentuh di platform manapun** — Sesi 2, 11, 13 (baca dari `RANGKUMAN_MODULE_1.md`, breadth-first karena exam MCQ, prioritaskan bagian Audio Insight) — baru lanjut sesi yang punya pasangan notes+kode dan belum ada progress kode (mulai dari Sesi 4/`collection-data-type` yang sedang jalan, lalu 5, 7, 8, 9, 10, 12) sambil gabungkan baca notes + jalanin kode. Sesi 1 & 3 sudah solid/hampir solid dari self-test web, tidak perlu diulang dari nol — cukup spot-check kalau ragu.
  - **Ukuran tiap sesi (jumlah baris `RANGKUMAN_MODULE_1.md`, proxy kedalaman materi), untuk kalibrasi waktu:** Sesi 9=1666 (terbesar), Sesi 3=1202, Sesi 11=1035, Sesi 4=1015, Sesi 10=895, Sesi 7=808, Sesi 13=790, Sesi 12=799, Sesi 2=739, Sesi 8=735, Sesi 5=578, Sesi 6=421.
  - **Jadwal 3 hari disepakati (2026-08-29 malam), berbasis komitmen user minimal 4 jam/hari, metode quiz-first (bukan predict-then-verify per baris kode kayak sesi 4) untuk semua sesi baru:**
    - **Sabtu, 2026-08-30 (≥4 jam)** — sesi no-code dulu (satu-satunya sumbernya notes): Sesi 2 Git & GitHub (~1 jam) → Sesi 11 Statistics (~1,5 jam) → Sesi 13 Data Viz (~1 jam) → tuntasin kode Sesi 4 `collection-data-type` file 06-12 (konsep sudah tervalidasi web, harusnya cepat, ~1-1,5 jam).
    - **Minggu, 2026-08-31 (≥4 jam)** — hari terberat, dua modul SQL sekaligus (setup koneksi DB sekali jalan): Sesi 9 Intro DB & SQL (~2 jam, quiz-first + jalanin beberapa query kunci) → Sesi 10 SQL Multi-table/joins (~1 jam) → Sesi 7 OOP (~1 jam) → Sesi 8 Modular kalau waktu masih ada (kalau nggak, geser ke Senin).
    - **Senin, 2026-09-01, sebelum 19:30 WIB (ujian malam itu juga)** — nutup sisa + buffer review: Sesi 5 Function/File Handling (~1 jam) → Sesi 6 Hackerrank (~0,5 jam) → Sesi 12 Pandas/Numpy (~1,5 jam) → tuntasin kode Sesi 3 `conditional-and-loop-statements` (konsep sudah tervalidasi web, ~1 jam) → **sisa waktu jadi buffer:** skim ulang semua bagian "[Wawasan Diskusi/Audio Insight]" di 13 sesi + retest poin yang masih lemah.
    - **CC1 (4 soal LeetCode) sengaja TIDAK masuk hitungan jadwal di atas** — kerjain terpisah kapan saja sebelum 2026-09-03, termasuk boleh setelah Exam 1 selesai.
    - Jadwal ini fleksibel: kalau progress lebih cepat dari estimasi (user commit "bisa lebih" dari 4 jam), boleh tarik maju sesi hari berikutnya.
  - **Progress eksekusi jadwal (quiz-first di Claude Code, malam 2026-08-29 lanjut ke 2026-08-30):**
    - ✅ **Sesi 2 (Git & GitHub) — SELESAI, solid.** Quiz 10 soal cold (~40-50%), gap ditambal (commit=snapshot bukan eksekusi; staged≠masuk main; unmodified≠tidak bisa diubah; `--no-ff`=nambah commit bukan mempercepat; urutan `remote add origin`→`push -u origin main`), retest 5 soal kunci = 4/5 benar (1 typo kecil `-u` doang). Tidak perlu diulang, cukup spot-check kalau ragu nanti.
    - ✅ **Sesi 11 (Statistics Fundamental) — SELESAI, solid (2026-08-30).** Quiz 14 soal cold (skor rendah, wajar karena materi paling asing), gap ditambal, retest ULANG SEMUA sukses:
      - 2 cabang statistika (Descriptive vs Inferential) ✅, contoh ordinal (Easy/Medium/Hard) ✅, Median vs Mean (robust ke outlier) ✅, Stratified vs Cluster ✅ — langsung benar begitu ditambal.
      - Interval vs Ratio: konsep fisis (0°C tetap ada vs 0cm=nggak eksis) sebenarnya udah kena dari awal, cuma LABEL Ratio/Interval-nya kebalik — setelah diluruskan langsung paham.
      - IQR & outlier bound, Empirical Rule (68-95-99.7%), P-Value >< 0.05, Imbalanced Data (accuracy menyesatkan karena model asal-nebak kelas mayoritas tetap dapat skor tinggi, gantinya precision/recall) — semua di-retest pakai angka baru dan **berhasil dikerjakan mandiri**, termasuk nemuin sendiri insight tambahan bahwa batas bawah/atas outlier itu **tandanya (plus/minus) nggak tetap**, tergantung skala data (bukan aturan baku).
      - Chart numerik: Box Plot juga valid, Histogram default kalau cuma mau lihat 1 variabel.
      - **Kesimpulan:** sesi paling berat & paling banyak gap sejauh ini, tapi begitu ditambal SEMUA nempel di retest tanpa terkecuali — pola "quiz dulu, baru tambal" ini terbukti kuat bahkan buat materi yang sama sekali asing (bukan cuma coding).
    - **Kalibrasi waktu:** Sesi 2 + Sesi 11 kelar dalam ~2,5 jam wall-clock, tapi ~30 menit di antaranya distraksi (beresin komputer) — jadi **waktu efektif murni belajar sekitar ~2 jam** buat 2 sesi (1 ringan + 1 terberat). Ini lebih cepat dari estimasi awal, sinyal bagus buat proyeksi sisa waktu.
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
