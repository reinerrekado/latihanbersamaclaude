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

*(centang = konsep sesi sudah divalidasi quiz+retest solid, cukup buat exam pilihan ganda. Kode praktik `.py`/`.sql` di repo itu **jalur latihan paralel** — cara dosen aslinya ngajar sesi ini live di kelas, ngukur skill nulis/jalanin kode beneran, bukan sekadar recall konsep. Nggak jadi syarat centang di sini karena Exam 1 sifatnya MCQ, tapi progressnya tetap dicatat di sub-baris karena relevan buat CC1 LeetCode & pemahaman yang lebih dalam.)*

**Progress: 13 / 13 sesi solid (100%) — TUNTAS di hari H Exam! 🎉**

**🏆 HASIL EXAM 1 ASLI: 17/20 (85%) — LULUS, jauh di atas nilai minimum (60%).** Dikerjakan Selasa 2026-09-01 malam, murni mandiri tanpa nyontek. Screenshot lengkap dianalisis & di-cross-check dengan catatan mandiri user — 100% cocok, skor terkonfirmasi akurat. Cuma 3 soal meleset (statistik Inferential vs "Predictive", `np.random.randn()` vs `randint()`, arah LEFT vs RIGHT JOIN) — 2 dari 3 itu PERSIS masuk "Pola #2: Konsep Berpasangan Ketuker" yang udah dipetakan di `CHEATSHEET.md` sebelum exam, validasi kuat bahwa analisis pola kognitif hari ini akurat.

- [x] Sesi 1 — Intro DS, Python, Statistics, SQL, Git & GitHub *(self-test web 90%)*
- [x] Sesi 2 — Intro to Git & GitHub *(quiz+retest Claude Code, solid)*
- [x] Sesi 3 — Conditional & Loop Statement *(konsep solid, self-test web 50%→ditambal→retest sukses. Jalur paralel — kode praktik `conditional-and-loop-statements/`: 0/11 file)*
- [x] Sesi 4 — Data Types Collection Notes *(konsep solid, self-test web 30%→ditambal→retest sukses. Jalur paralel — kode praktik `collection-data-type/`: 12/12 file SELESAI TOTAL)*
- [x] Sesi 5 — Python Function & File Handling *(quiz+retest Claude Code, solid, 2026-08-31, retest langsung 3/3 benar)*
- [x] Sesi 6 — Hackerrank Exercise *(quiz+retest Claude Code, solid, 2026-08-31)*
- [x] Sesi 7 — Object Oriented Programming *(quiz+retest Claude Code, solid, 2026-08-31, via iPad Remote Control)*
- [x] Sesi 8 — Python & Modular Programming *(quiz+retest Claude Code, solid, 2026-09-01)*
- [x] Sesi 9 — Intro to Database & SQL *(quiz+retest Claude Code, solid, 2026-08-31, termasuk subquery — verifikasi baca langsung RANGKUMAN_MODULE_1.md)*
- [x] Sesi 10 — SQL Working With Multiple Tables *(quiz+retest Claude Code, solid, 2026-08-31, termasuk JOIN — verifikasi baca langsung RANGKUMAN_MODULE_1.md)*
- [x] Sesi 11 — Statistics Fundamental *(quiz+retest Claude Code, solid)*
- [x] Sesi 12 — Python Data Manipulation With Pandas and Numpy *(quiz+retest Claude Code, solid, 2026-09-01 — sesi terakhir, semua 13 sesi tuntas)*
- [x] Sesi 13 — Data Visualization *(quiz+retest Claude Code, solid, 2026-08-30. Retest sudah pakai soal Bahasa Inggris sesuai keputusan.)*

### Checklist Code Challenge 1 (terpisah, deadline 2026-09-03)

- [x] Soal Easy #1 (LeetCode, Accepted) — *Convert the Temperature, Accepted 2026-08-30, bukti sudah dikirim ke form*
- [ ] Soal Easy #2 (LeetCode, Accepted)
- [ ] Soal Easy #3 (LeetCode, Accepted)
- [ ] Soal Medium #1 (LeetCode, Accepted)
- [ ] Submit link akun LeetCode + screenshot Accepted via Google Form *(sebagian sudah — bukti Soal Easy #1 sudah terkirim; centang penuh setelah semua 4 soal beres)*

---

- **Update terakhir:** 2026-08-30
- **Sedang di file:** MODUL `collection-data-type` SELESAI TOTAL (12/12 file, 2026-08-30). Lanjutan berikutnya sesuai jadwal Minggu (2026-08-31): Sesi 9 Intro DB & SQL, Sesi 10 SQL Multi-table, Sesi 7 OOP, Sesi 8 Modular kalau waktu ada.
- **Progress modul collection-data-type (1 dari 6 modul python) — ✅ SELESAI SEMUA 12 FILE (2026-08-30):**
  - ✅ `01_python_list_basics.py` — selesai
  - ✅ `02_python_list_methods.py` — selesai
  - ✅ `03_list_comprehension.py` — selesai (termasuk latihan tambahan filter ganjil +100)
  - ✅ `04_python_tuple.py` — selesai (creation, indexing, immutability, tuple kosong, nested tuple, trik koma 1 item)
  - ✅ `05_tuple_methods.py` — selesai (`.count()`, `.index()`, `len()`, error saat value tidak ditemukan)
  - ✅ `06_indexing_and_slicing.py` — selesai. Gap sempat muncul: negative index dikira error (padahal valid), slicing multi-item step=1 sempat cuma ambil item awal+akhir doang (skip tengah) — ditambal pakai walkthrough index-by-index eksplisit, retest berkali-kali sampai konsisten benar (termasuk kasus step=2). Indexing vs slicing out-of-range (error vs `[]`) sudah solid dari sebelumnya, tetap benar.
  - ✅ `07_python_set.py` — selesai. Gap: `{}` kosong dikira set (padahal dict — jebakan utama file ini, sempat 2x salah sebelum nempel), alasan set nggak bisa di-index (bukan soal "bukan list", tapi karena unordered), arah sebab-akibat mutable/immutable vs hashable sempat kebalik (list dikira BISA jadi dict key karena "mutable" — harusnya sebaliknya, mutable=unhashable=tidak bisa). Konsep frozenset (kenapa perlu buat nested set) berhasil dijelaskan pakai jembatan ke tuple immutability (Sesi 4) yang sudah dikuasai.
  - ✅ `08_set_methods.py` — selesai. Cepat karena mirip list methods yang udah dikuasai. Cuma perlu penjelasan tambahan: `set.pop()` random (bukan by-index) karena set unordered, `.copy()` bikin objek independen (dikaitkan ke `==` vs `is` dari self-test web Sesi 4).
  - ✅ `09_set_operations.py` — selesai, LANGSUNG BENAR semua (union/intersection/difference/symmetric_difference/issubset/issuperset) tanpa koreksi — konsep Venn diagram ternyata sangat intuitif buat user. Cuma "proper subset" (`<` vs `<=`) yang perlu dijelaskan sekali (analogi: `issubset` boleh identik, `<` harus beneran lebih kecil/beda), langsung nempel di percobaan pertama.
  - ✅ `10_python_dictionary.py` — selesai. Gap: dikira duplicate key di dict literal bakal ERROR (padahal Python diam-diam overwrite pakai value terakhir, tanpa protes — beda karakter dari constraint SQL PRIMARY KEY).
  - ✅ `11_dictionary_methods.py` — selesai. Gap: `.get()` pada key yang nggak ada tanpa default sempat dikira balikin nilai dari pemanggilan `.get()` sebelumnya (bukan `None`) — ditambal, retest langsung benar termasuk paham `.get(key, default)` sebagai fallback value.
  - ✅ `12_dictionary_access_update.py` — selesai. 1 gap: awalnya nggak paham kenapa syntax `dict[key] = value` yang SAMA bisa jadi "update" atau "nambah key baru" tergantung situasi — ditambal pakai analogi "taruh buku di rak berlabel X" (efek beda tergantung status label sebelum aksi, bukan tergantung kode), langsung nempel di percobaan pertama.
  - **Pola keseluruhan modul ini:** kecepatan belajar meningkat drastis begitu masuk ke `set`/`dictionary` (setelah list/tuple dikuasai) — banyak file (09, sebagian besar 11-12) langsung benar di percobaan pertama atau kedua tanpa perlu banyak retest, sesuai prediksi "topik mirip yang sudah dikuasai bisa dipercepat".
- **Percobaan CC1 pertama (LeetCode "Two Sum") — 2026-08-30 malam, ~jam ke-7 belajar hari itu, BELUM selesai/submit:**
  - Dokumen resmi CC1 ditemukan di folder Downloads (bukan repo ini): `Briefing Code Challenge LeetCode AI-Engineer.docx` dan `Panduan Registrasi dan Soal LeetCode.docx`. Konfirmasi: 3 Easy (20 poin) + 1 Medium (40 poin), total 100 poin, **topik soal BEBAS/tidak wajib beda-beda** (filter Topics di LeetCode cuma opsional), submit via link profil + screenshot "Accepted" ke https://forms.gle/4ncAW2VPUueAkiJp8. Ada juga "Template Screenshot Code Challenge 1.docx" yang disebut di briefing tapi belum ditemukan filenya.
  - Sempat coba soal Math "2769. Find the Maximum Achievable Number" (formula `num + 2*t`) tapi user memilih kembali ke Two Sum karena maunya "success rate lebih tinggi" / lebih exact match ke skill yang baru dilatih (dict).
  - User paham konsep target vs index dengan benar (2 contoh manual benar), paham kenapa butuh 2 pasangan/pendekatan brute force perlu nested loop (setelah awalnya nebak 1 loop lalu 5x5=25, dikoreksi jadi n(n-1)/2), lalu di-switch ke pendekatan **1 loop + dict "complement"** (lebih sesuai basic yang baru dikuasai). Fatigue muncul pas diminta trace manual pelengkap di contoh baru (`nums=[4,6,9,1]`, target=15) — user bilang "saya fatigue", sesi dihentikan di titik ini SEBELUM sempat nulis kode Python beneran atau submit ke LeetCode.
  - **Insight penting buat sesi lanjutan:** user sempat bingung/frustrasi ("kenapa tidak plek dengan yang kita latih") karena psanggap 12 file collection-data-type tadi seharusnya bikin LeetCode terasa mudah. Perlu ditekankan lagi kalau perlu: **quiz-predict (baca kode orang, tebak output) itu skill "recognition", sedangkan LeetCode itu skill "sintesis dari nol"** — dua hal berbeda meski fondasinya (paham dict/set) sama. Jangan taruh soal LeetCode PERTAMA KALI di ekor sesi belajar yang udah panjang (7+ jam) — kalau lanjut CC1 lagi, mending di awal sesi saat masih fresh, bukan di ujung.
  - **Status lanjutan:** belum ada kode Python yang ditulis untuk Two Sum, belum submit ke LeetCode. CC1 deadline 2026-09-03, jadi tidak mendesak — aman dilanjutkan kapan saja, termasuk setelah Exam 1.
  - **3 soal Easy yang direkomendasikan buat CC1** (dipilih karena reuse skill yang baru dikuasai 2026-08-30): **Two Sum** (dict/complement, sudah dicoba sebagian), **Remove Duplicates from Sorted Array** (1 loop + index assignment, dikonfirmasi user "mampu"), **Contains Duplicate** (pakai `set`, paling simpel dari 3-nya). Alternatif super-gampang buat quick win: **Convert the Temperature** (Celsius→Kelvin/Fahrenheit, cuma 1 baris rumus, hampir pasti Accepted) — ternyata ISOMORFIK sama soal resmi Sesi 1 "TUGAS BESAR 2 no.1 Program Konversi Suhu" (Fahrenheit→Celsius, rumus `(F-32)*5/9`) di `RANGKUMAN_MODULE_1.md`.
- **TUGAS BESAR 2 Sesi 1 — 4/5 soal SELESAI (2026-08-30, predict-then-verify dari nol):**
  1. ✅ Konversi Suhu — selesai. Gap: sempat salah eja `celcius`/`celsius` beda-beda (NameError, mismatch nama fungsi/variabel/parameter) — konsep def/parameter/argument/return sempat butuh penjelasan analogi "resep masakan" (dapur=fungsi, bahan=parameter, piring dibawa keluar=return) sampai jelas.
  2. ✅ Konversi Jarak (cm→km) — selesai. Gap: penamaan variabel kebalik makna (parameter dikasih nama `km` padahal isinya cm, hasil dikasih nama `cm` padahal isinya km) — bukan bug fungsional tapi soal clean code. Juga nemuin sendiri kalau `/` selalu hasilkan float (`1.0 km` bukan `1 km`), dan f-string cuma bungkus nilai apa adanya (nggak otomatis buang `.0`).
  3. ✅ Cek Ganjil/Genap — selesai, LANGSUNG BENAR (pakai `n%2==1`/`n%2==0` + if-else). Sempat sesi tambahan ngebahas ulang konsep modulo (`%`) karena ketuker sama `//` (bingung "berapa kali muat" vs "sisa"-nya) — butuh 2-3 contoh angka baru sebelum konsisten benar (15%2 akhirnya benar mandiri).
  4. ✅ Manipulasi String (hapus first occurrence) — selesai setelah dikoreksi: `kata_dicari` sempat lupa didefinisikan, salah isi parameter kedua `.replace()` (isi teks "teks" padahal harusnya `""` buat menghapus), dan hasil `.replace()` sempat nggak ditampung ke variabel (lupa string itu immutable, harus di-assign ulang). Hasil akhir benar: `"Ho world"`.
  5. ⬜ Cek Palindrome — BELUM dikerjakan, di-skip sementara buat coba LeetCode duluan (Palindrome itu sendiri mirip soal LeetCode klasik, rencana digabung nanti).
  - **Sesi ini juga ada 2x momen jujur soal Copilot**: sempat aktifin Copilot buat liat hint pas macet di soal 3, lalu dimatiin lagi sendiri; dan sekali lagi pas soal LeetCode "cuma liat, nggak accept". Instruktur (via cheat sheet Sesi 3) tegas bilang jangan pakai AI autocomplete pas masih belajar dasar — user nunjukin insting yang tepat buat balik matiin sendiri.

- **CC1 (LeetCode) — mulai dikerjakan 2026-08-30 malam, progress 1/4 soal Accepted:**
  - ✅ **"Convert the Temperature" (Easy) — ACCEPTED di LeetCode.** Ditulis & ditest dulu di Jupyter (alur: draft lokal → pindah ke LeetCode → submit — ini SAH, nggak ada aturan wajib ngoding langsung di LeetCode, cuma submission akhir yang wajib terjadi di LeetCode). Sempat ada 2 bug transisi ke format `class Solution`: (1) case-mismatch `celsius` vs `Celsius` lagi (pola berulang!), (2) lupa cara test method di dalam class butuh instansiasi objek dulu (`sol = Solution()` baru `sol.method(...)`) — LeetCode ngelakuin ini otomatis pas submit, tapi di Jupyter harus manual.
  - ✅ **Bukti submission Soal 1 (Convert the Temperature) SUDAH dikirim ke form** (2026-08-30 malam). Format bukti sesuai `Template Screenshot Code Challenge.docx`: 2 screenshot terpisah per soal (CODE/SOLUSI + HASIL status "Accepted" dari tombol Submit, bukan dari "Run").
  - ⚠️ **Ketidakcocokan angka ditemukan** antara 2 dokumen resmi: Briefing bilang "3 Easy + 1 Medium = 100 poin", tapi Template Screenshot nulis teks "8 Easy + 2 Medium = 30 poin" untuk Modul 01 — TAPI template itu sendiri cuma nyediain 4 slot soal (Soal 1-3 Easy, Soal 4 Medium), yang justru cocok ke Briefing. User memutuskan itu typo/sisa teks dari template batch lain, pilih percaya ke Briefing + jumlah slot aktual (3 Easy+1 Medium), TIDAK dikonfirmasi ke pengajar (keputusan user sendiri, dicatat biar jelas bukan rekomendasi Claude).
  - **Sisa CC1:** 2 Easy lagi + 1 Medium. Kandidat: Remove Duplicates from Sorted Array, Contains Duplicate, atau Palindrome (gabung sama Soal 5 Tugas Besar 2 di atas). Medium belum dipilih.

- **Sesi 7 (OOP) & Sesi 9 (SQL) — mulai 2026-08-31, metode BERUBAH jadi "jelasin dulu baru quiz":**
  - **Perubahan metode penting:** setelah cold-quiz OOP & SQL awal hampir semua "lost", user nanya "apakah dilempar kuis sudah pasti saya tidak bisa jawab?" — dikonfirmasi BENAR untuk istilah teknis baru total (`self`, `__init__`, `GROUP BY`, dst) yang nggak bisa dinalar dari logika umum (beda dari statistik/viz yang masih bisa ditebak pakai analogi). Metode diganti: **jelasin ringkas dulu, baru quiz check** — khusus buat sesi vocabulary-heavy (SQL, OOP), BUKAN sesi reasoning-heavy (stats, viz) yang cold-quiz masih oke. Detail di memory `learning_style`.
  - ✅ **Sesi 7 (OOP) — SOLID, sudah di-retest (2026-08-31, lanjut dari iPad via Remote Control).** Dijelasin lengkap (class/object, `__init__`, `self`, inheritance, `super().__init__()`, `if __name__=="__main__"`, list sbg class bawaan). Retest pertama: 3/7 langsung benar (analogi cetakan kue, `__init__` auto-jalan, object independen), tapi 3 meleset — mekanisme `self` (dikira soal "urutan penulisan", bukan soal CARA MANGGIL via titik), efek hapus `super().__init__()` (dikira `Vehicle`/parent yang kehilangan atribut, padahal cuma OBJECT CHILD itu yang nggak dapet atribut → `AttributeError`, parent class tetap utuh), arah inheritance method (dikira `honk()` "milik child", padahal itu milik PARENT yang diwariskan). Retest ke-2 pakai kasus baru: 2/3 langsung benar (super()/AttributeError, kenapa child akses method parent), 1 masih kabur (`self` mechanism) — ditambal pakai perbandingan "1 kode dipakai gantian vs 2 salinan kode", retest ke-3 berhasil ("cuma 1 kode yang sama, dipakai gantian, `self` yang bedain"). **Kesimpulan: OOP solid, nggak perlu diulang dari nol lagi.**
  - ✅ **Sesi 9 (SQL) — SOLID SEMUA termasuk subquery.** DB vs DBMS, DDL vs DML, WHERE vs HAVING (sempat GROUP BY/HAVING KETUKER PERANNYA 2x — dikira HAVING yang "mengelompokkan", padahal itu tugas GROUP BY; ditambal pakai 3 contoh konkret berurutan — departemen/gaji, siswa/nilai, toko/penjualan — baru clean di percobaan ke-3), aggregate vs scalar function, dan **Subquery (WHERE/SELECT/FROM)** — sempat coba nulis subquery tanpa bungkus kurung/nesting yang benar (nyampur "AVG FROM karyawan" langsung ke WHERE tanpa nested SELECT terpisah), ditambal dengan breakdown 3-langkah (outer query dengan angka dummy → subquery mandiri → gabungkan) baru langsung benar. Alias wajib buat Derived Table di `FROM` juga sudah solid (paham konsekuensinya = SQL ERROR kalau lupa, bukan cuma "nggak ditampilkan").
  - **Verifikasi tambahan (2026-08-31):** atas permintaan user ("harusnya dipakai semua agar anda kaya"), Sesi 9 & 10 `RANGKUMAN_MODULE_1.md` dibaca PENUH langsung oleh Claude (bukan cuma lewat ringkasan subagent lagi) — dikonfirmasi cheat sheet SUDAH akurat, nggak ada koreksi. Bonus ditemukan: latihan konkret database `world` (9 soal) & `Sakila` (10 soal) dengan jawaban lengkap di source — bagus buat latihan pola soal real, belum dipakai.
  - ✅ **Sesi 10 (SQL JOIN) — SOLID (2026-08-31).** PK vs FK, Implicit vs Explicit JOIN, Cartesian Product bahaya, INNER/LEFT/RIGHT/FULL JOIN — retest 4/4 langsung benar KECUALI Self JOIN (dikira cuma "Inner Join biasa", dan dikira alias TIDAK dibutuhkan — padahal kebalik, alias itu MUTLAK di Self JOIN). Ditambal + retest ulang → benar (paham konsekuensi hapus alias = SQL ERROR "Not unique table/alias", bukan sekadar "database bingung" secara umum).
  - ✅ **Sesi 6 (Hackerrank) — SOLID (2026-08-31).** Runner-Up Score pattern, Company Logo (sort by count desc + tie-break abjad) — retest 3 soal, 1 miss: `map()` dikira LANGSUNG hasilkan list (lupa sifat *lazy*-nya, padahal baru diproses pas di-`list()`). Ditambal + 1 soal tambahan (Counter tie-break baru) → langsung benar.
  - ✅ **Sesi 5 (Function & File Handling) — SOLID, retest LANGSUNG 3/3 benar (2026-08-31).** Scope/`global` keyword (`UnboundLocalError` kalau assignment tanpa `global`), nested function (nggak bisa diakses dari luar), file mode `"w"` (timpa total). Konfirmasi prediksi: sesi ini emang cepat karena banyak overlap sama praktik Tugas Besar 2 hari ini (def/parameter/return udah dikuasai duluan).
  - **Perubahan metode TAMBAHAN (2026-08-31, dari user):** (1) setiap penjelasan HARUS ada contoh kode konkret per kasus/variant (bukan cuma tabel/prosa) — dikonfirmasi 2x oleh user, disimpan di memory `feedback_examples_when_teaching`. (2) Penjelasan harus **kronologis** (urutan proses beneran kejadian, bukan definisi/kesimpulan duluan) — user eksplisit minta di-challenge kalau kepermintaan ini berlebihan, tapi dikonfirmasi masuk akal karena udah kebukti works di 2 kali contoh (resep masakan buat function, GROUP BY/HAVING trace angka). Disimpan di memory `feedback_chronological_explanation`.
  - ✅ **Sesi 8 (Modular Programming) — SOLID (2026-09-01, dini hari/pagi).** Modular vs monolitik, import (seluruh modul vs spesifik), Project>Package>Module + `__init__.py` wajib, name guard `if __name__=="__main__"` (nggak nge-block definisi function/class, cuma eksekusi top-level), alias `as` (2 alasan beda: hindari bentrok nama vs murni konvensi ringkas — sempat ketuker, ditambal). Retest 3/3 benar setelah 1x koreksi (nama fungsi itu cuma LABEL, Python nggak "ngerti" arti kata "tambah"/"add" — user nanya duluan sebelum lanjut, bagus).
  - ✅ **Sesi 12 (Pandas/Numpy) — SOLID, SESI TERAKHIR, SEMUA 13 SESI TUNTAS (2026-09-01 pagi, hari H Exam).** NumPy vs List (homogen+cepat), `arange` (kasih step) vs `linspace` (kasih jumlah elemen), slicing array = VIEW bukan copy (beda dari List biasa — sempat salah hitung index tapi konsep VIEW-nya kejawab benar), `.loc` (inklusif) vs `.iloc` (eksklusif), `.groupby()` (setara `GROUP BY` SQL), `.argmax()` (posisi, BUKAN nilai — sempat ketuker sama `.max()`).
    - **Catatan penting soal fatigue:** di tengah sesi ini, pola lama "ambil ujung slice doang" (dari Sesi 4 pagi) SEMPAT MUNCUL LAGI di `.iloc` (jawab "0 dan 3" utk `iloc[0:3]`, lalu "1 dan 3" utk `iloc[1:4]`) — bukan gap konsep baru, tapi tanda kelelahan setelah maraton belajar panjang (dari OOP+SQL 2 jam kemarin malam, lanjut Sesi 8+12 dini hari/pagi tanpa jeda panjang). Ditambal pakai walkthrough tabel index eksplisit + user ngisi sendiri (bukan cuma dikasih tau), akhirnya solid lagi di 2 percobaan terakhir. **Pelajaran:** kalau pola error yang harusnya udah solid tiba-tiba muncul lagi, itu sinyal cek energi/fokus dulu, bukan langsung anggap gap baru.
  - **PROGRESS FINAL EXAM 1: 13/13 sesi solid (100%)** — tercapai tepat di hari H Exam (Selasa 2026-09-01, sebelum 19:30 WIB). Sisa waktu sebelum exam sebaiknya dipakai buat: (1) istirahat cukup (jangan begadang lanjut push lebih jauh), (2) skim ulang cheat sheet + bagian "⚠️ Trap" tiap sesi sebagai buffer review ringan, BUKAN sesi belajar berat baru.

- **Modul python lain yang BELUM disentuh sama sekali:** `conditional-and-loop-statements` (11 file), `data-manipulation-pandas-numpy` (11 file, butuh pandas/numpy), `object-oriented-programming` (4 file), `python-function-and-file-handling` (5 file)
- **`python-modular-programming` (9 bagian, proyek multi-file) — SEBAGIAN kesentuh (2026-09-01):** user sempat buka & tunjukin isi `02_first_module/main.py` dan `05_packages_demo/main.py` pas diskusi Sesi 8 (konsep import/package). Ini BUKAN pengerjaan sistematis (nggak predict-then-verify + run tiap file kayak `collection-data-type`), cuma referensi pas quiz konsep. Belum bisa dicentang selesai.
- **SQL (`sql-exercise-materials-`) belum disentuh sama sekali:** modul "9 - Introduction to Databases and SQL" (14 file demo + exercises) dan modul "10 - SQL Working with Multiple Tables" (6 file demo + exercises)
- **Jadwal & scope resmi (dari dokumen briefing, update 2026-08-29):**
  - **Exam 1** — pilihan ganda (**20 soal**), berbahasa Inggris, via **purwadhika.com** (online, TIDAK perlu masuk Zoom), materi python & SQL **modul 1**. **Selasa, 2026-09-01, 19:30-21:00 WIB.** Ini yang butuh materi matang (konsep, bukan hanya bisa jalanin kode).
    - **Aturan resmi (reminder dari pengajar, diterima 2026-09-01):** akses ujian CUMA bisa dibuka di jendela 19:30-21:00 WIB (nggak bisa lebih cepat/lebih lambat). **Begitu klik Start, WAJIB diselesaikan** apapun alasannya (nggak bisa pause/keluar-masuk). **Nilai minimum lulus: 60.**
    - **Kalau berhalangan:** ada Exam Susulan Selasa 2026-09-08 jam sama, tapi **berbayar Rp 350.000** — wajib chat pengajar duluan kasih alasan sebelum ikut susulan.
    - **Guideline teknis platform** (file lengkap: `GUIDELINE_PENGERJAAN_EXAM.pdf` di root repo ini) — poin PALING KRITIS:
      1. **TIDAK ADA tombol "kembali ke soal sebelumnya"** — begitu klik "Next", jawaban itu FINAL, nggak bisa direvisi lagi. Mikir matang-matang SEBELUM klik Next, bukan setelahnya.
      2. **Soal yang di-SKIP otomatis dianggap SALAH oleh sistem** — jangan skip kalau masih ada kemungkinan jawab, mending nebak daripada dikosongin.
      3. Kalau klik "Next" tapi soal belum diisi, muncul pop-up "Unanswered question" — klik **Cancel** buat balik isi (masih dalam soal yang sama, belum lewat), atau klik **Skip** cuma kalau BENERAN sengaja lewatin.
      4. **Timer tetap jalan** dari sejak halaman peraturan muncul (sebelum klik Start) — jangan lama-lama diam di situ.
      5. Kalau tombol Start belum aktif padahal udah jam ujian → refresh page / clear cache / logout-login ulang.
      6. Kalau ada soal harusnya ada gambar tapi nggak muncul → refresh/reload 1-2x.
      7. **Di soal TERAKHIR**, setelah klik "Submit Answer", WAJIB klik **"Proceed"** di pop-up berikutnya — kalau nggak, jawaban belum benar-benar ke-submit ke server. Baru selesai kalau muncul pop-up "Congratulations! You have completed the exam."
      8. **Disaranin screen record selama ujian** — kalau ada kendala teknis/kesalahan sistem, komplain CUMA diterima kalau ada bukti screen record. Kalau internet mendadak putus, boleh lanjut pakai browser & device YANG SAMA; kalau ganti device/browser, waktu ujian mulai dari sisa waktu terakhir (bukan reset penuh).
      9. Dilarang keras cheating/nyontek/cari jawaban dari luar (buku, internet, dll) — ada sanksi tegas kalau ketauan.
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
    - **WAJIB mulai Sesi 13 dan seterusnya (keputusan user 2026-08-30): selipkan soal retest dalam Bahasa Inggris**, bukan cuma terjemahan istilah tapi frasa soal utuh dalam Inggris. Alasan: semua quiz sejauh ini dalam Bahasa Indonesia, padahal Exam 1 aslinya berbahasa Inggris — paham konsep di Indonesia belum tentu langsung cepat kenali istilah yang sama di Inggris. Jangan cuma sekali-sekali, jadikan bagian rutin tiap sesi quiz baru.
  - **Prioritas belajar direvisi (per keputusan user, 2026-08-29 sore):** dahulukan sesi yang **sama sekali belum tersentuh di platform manapun** — Sesi 2, 11, 13 (baca dari `RANGKUMAN_MODULE_1.md`, breadth-first karena exam MCQ, prioritaskan bagian Audio Insight) — baru lanjut sesi yang punya pasangan notes+kode dan belum ada progress kode (mulai dari Sesi 4/`collection-data-type` yang sedang jalan, lalu 5, 7, 8, 9, 10, 12) sambil gabungkan baca notes + jalanin kode. Sesi 1 & 3 sudah solid/hampir solid dari self-test web, tidak perlu diulang dari nol — cukup spot-check kalau ragu.
  - **Ukuran tiap sesi (jumlah baris `RANGKUMAN_MODULE_1.md`, proxy kedalaman materi), untuk kalibrasi waktu:** Sesi 9=1666 (terbesar), Sesi 3=1202, Sesi 11=1035, Sesi 4=1015, Sesi 10=895, Sesi 7=808, Sesi 13=790, Sesi 12=799, Sesi 2=739, Sesi 8=735, Sesi 5=578, Sesi 6=421.
  - **Jadwal 3 hari disepakati (2026-08-29 malam), berbasis komitmen user minimal 4 jam/hari, metode quiz-first (bukan predict-then-verify per baris kode kayak sesi 4) untuk semua sesi baru:**
    - **[KOREKSI 2026-08-30: label hari di 3 baris jadwal ini salah ketik dari awal — Minggu/Senin/Selasa, bukan Sabtu/Minggu/Senin. Tanggal & urutan rencananya tetap sama, cuma nama harinya yang dibetulkan di sini.]**
    - **Minggu, 2026-08-30 (≥4 jam)** — sesi no-code dulu (satu-satunya sumbernya notes): Sesi 2 Git & GitHub (~1 jam) → Sesi 11 Statistics (~1,5 jam) → Sesi 13 Data Viz (~1 jam) → tuntasin kode Sesi 4 `collection-data-type` file 06-12 (konsep sudah tervalidasi web, harusnya cepat, ~1-1,5 jam). **[SELESAI SEMUA]**
    - **Senin, 2026-08-31 (≥4 jam)** — hari terberat, dua modul SQL sekaligus (setup koneksi DB sekali jalan): Sesi 9 Intro DB & SQL (~2 jam, quiz-first + jalanin beberapa query kunci) → Sesi 10 SQL Multi-table/joins (~1 jam) → Sesi 7 OOP (~1 jam) → Sesi 8 Modular kalau waktu masih ada (kalau nggak, geser ke Selasa).
    - **Selasa, 2026-09-01, sebelum 19:30 WIB (ujian malam itu juga)** — nutup sisa + buffer review: Sesi 5 Function/File Handling (~1 jam) → Sesi 6 Hackerrank (~0,5 jam) → Sesi 12 Pandas/Numpy (~1,5 jam) → tuntasin kode Sesi 3 `conditional-and-loop-statements` (konsep sudah tervalidasi web, ~1 jam) → **sisa waktu jadi buffer:** skim ulang semua bagian "[Wawasan Diskusi/Audio Insight]" di 13 sesi + retest poin yang masih lemah.
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
    - ✅ **Sesi 13 (Data Visualization) — SELESAI, solid (2026-08-30).** Chat Claude Code sebelumnya sempat "hilang" (bukan lintas perangkat, kemungkinan sesi baru/nggak ke-resume) — lanjut dari nol di sesi baru langsung baca `RANGKUMAN_MODULE_1.md` Bab 1-5 Sesi 13, quiz 12 soal cold dulu.
      - Quiz pertama skor rendah (~1,5/12) — banyak konsep KEBALIK arahnya, pola serupa Sesi 11 (interval/ratio): 4 kategori visualisasi (jawaban ngarang "observation/anomaly detection" padahal harusnya Comparison/Composition/**Relationship**/**Distribution**), arah skewness Box Plot (median deket Q1=right-skewed vs Q3=left-skewed, sempat kebalik beberapa kali sebelum nempel), formula IQR vs batas whisker (IQR = Q3-Q1 SAJA, pengali 1.5× baru dipakai di langkah batas whisker — sempat digabung jadi satu langkah), Stacked Bar (periode sedikit) vs Stacked Area (periode banyak) bukan soal "ada/tiada time series", 3 kondisi pie chart dilarang (waktu/fluktuasi, kategori >5, nilai berdekatan — cuma dapat 1/3), Histogram vs Bar Chart (batang nempel vs ada jeda, bukan soal "afinitas ke frekuensi"), alasan drop `PassengerId` sebelum correlation heatmap (karena cuma id/nomor urut tanpa makna kuantitatif, bukan soal "kebanyakan variabel"), solusi 2 variabel beda skala jauh (secondary Y-axis, BUKAN "jangan digabung di 1 grafik" — masalahnya skala, bukan soal ada/tiada korelasi).
      - **Analogi yang berhasil bikin klik soal arah skewness** (setelah analogi pertama "ekor ke kanan" gagal ngena imajinasi user): kasus gaji karyawan biasa (numpuk rendah) vs segelintir direktur (gaji ekstrem tinggi) → **"skew ikut arah si minoritas ekstrem yang nyempil, bukan arah kerumunan mayoritas."** Dikaitkan ke konsep Sesi 11 yang sudah solid (Mean gampang ketarik outlier, Median enggak) sebagai jembatan. Setelah itu retest soal skor pensiun & ujian langsung benar mandiri, termasuk nemuin sendiri kontradiksi kecil di jawaban sendiri (median deket Q1 vs Q3) begitu ditunjukkan.
      - Retest 7 soal (3 di antaranya full Bahasa Inggris, sesuai keputusan mulai Sesi 13) → 5/7 langsung solid, 2 sisanya (urutan Q1/Q3 selalu Q1=kecil/bawah terlepas dari skew arah manapun, dan IQR vs batas whisker jangan digabung) diluruskan sekali lagi dengan 2 soal angka baru → **langsung benar semua.**
      - **Kesimpulan:** pola "quiz dulu (skor rendah wajar) → tambal gap dengan analogi konkret yang dikaitkan ke konsep lama yang sudah solid → retest" tetap konsisten berhasil, bahkan untuk materi visual/abstrak yang beda karakter dari coding maupun statistik murni. Kalau satu analogi nggak "klik" (ekor ke kanan), ganti ke analogi yang lebih konkret & personal (gaji direktur) — jangan diulang analogi yang sama dengan kata-kata beda.
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
