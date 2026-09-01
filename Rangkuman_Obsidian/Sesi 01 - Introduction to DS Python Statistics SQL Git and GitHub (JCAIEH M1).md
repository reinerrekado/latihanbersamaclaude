---
tags: [jcaieh/module1, sesi-01, python, ai-fundamentals, algorithm, pseudocode, git, flowchart, jcaieh/module1/sesi01]
bootcamp: JCAIEH
module: 1
session: 1
aliases: ["Sesi 1", "Introduction to DS Python Statistics SQL Git and GitHub"]
---

# Session 1 — Introduction to DS, Python, Statistics, SQL, Git & GitHub

Catatan sesi pertama ini mencakup pengenalan konsep Artificial Intelligence (AI), dasar algoritma dan flowchart, studi kasus rekursi (Tower of Hanoi), pengenalan bahasa Python dan lingkungan kerjanya, konsep dasar pemrograman Python (variabel, tipe data, string, operator), pseudocode, hingga latihan praktik menulis kode pertama.

---

## Bab 1 — Pengenalan Artificial Intelligence (AI) & Applied AI Engineering

### 1.1 Definisi & Konseptual Dasar Artificial Intelligence (AI)

**[[Kamus & Cheatsheet (JCAIEH M1)#A|Artificial Intelligence (AI)]]** secara formal didefinisikan sebagai bidang dalam **Ilmu Komputer (Computer Science)** yang berfokus pada penciptaan sistem yang mampu melakukan tugas-tugas yang biasanya membutuhkan kecerdasan manusia.

#### Posisi AI dalam Ranah Ilmu Komputer

Dalam ekosistem _Computer Science_, AI menempati posisi yang setara dengan cabang ilmu lainnya seperti _web development_, _UI/UX design_, dan _cyber security_. Secara akademis, AI telah mengalami transisi signifikan; yang awalnya hanya merupakan sub-bidang atau konsentrasi di bawah Teknik Informatika, kini telah berkembang pesat menjadi jurusan mandiri di berbagai institusi pendidikan.

#### Kemampuan Utama yang Ditiru dari Manusia

Sistem AI dirancang untuk mereplikasi beberapa kemampuan kognitif utama manusia, antara lain:

- **Learning from data:** Kemampuan untuk belajar dari informasi yang ada.
- **Recognizing patterns:** Mengidentifikasi pola-pola tertentu dalam kumpulan data yang besar.
- **Understanding language:** Memahami bahasa manusia baik dalam bentuk teks maupun suara.
- **Making predictions or decisions:** Memberikan prediksi atau mengambil keputusan berdasarkan input.
- **Solving problems automatically:** Menyelesaikan masalah secara mandiri tanpa instruksi manual yang kaku.

#### Perbandingan Mendalam: AI vs. Software Tradisional

| Fitur | Software Tradisional | Artificial Intelligence (AI) |
| --- | --- | --- |
| **Metode Kerja** | Mengotomatisasi aturan (_rules_) yang sudah diketahui dan eksplisit. | Belajar dari pola data untuk masalah dengan aturan abstrak. |
| **Penulisan Aturan** | Ditulis secara manual oleh programmer. | Sistem merumuskan aturan sendiri melalui proses pembelajaran. |
| **Fleksibilitas** | Kaku, hanya bekerja sesuai instruksi tertulis. | Adaptif, mampu menangani input yang belum pernah dilihat sebelumnya. |

**Contoh Kasus: Membedakan Gambar Anjing dan Kucing.** Dalam software tradisional, menulis aturan untuk membedakan hewan sangat sulit (misal: menentukan nilai piksel tertentu, bentuk telinga, atau hidung secara manual). Dalam AI, kita menggunakan konsep **Supervised Machine Learning**. Proses ini dianalogikan seperti mendidik seorang anak kecil; kita memberikan banyak contoh gambar yang sudah diberi label ("Ini anjing", "Ini kucing"), sehingga sistem belajar mengenali ciri khas masing-masing secara otomatis.

### 1.2 Urgensi & Motivasi Mempelajari AI (Why Learn AI?)

Memahami AI bukan lagi sekadar pilihan, melainkan kebutuhan mendesak karena transformasi masif yang dibawanya ke berbagai sektor.

- **Career Growth:** Permintaan industri tinggi di lintas sektor — **Healthcare** (mendeteksi penyakit lewat X-ray dengan akurasi tinggi) dan **Finance** (analisis prediksi pasar dan manajemen risiko).
- **Productivity & Automation:** Otomasi konvensional memerlukan aturan yang sangat kaku, sedangkan otomasi berbasis AI mampu menangani tugas dinamis. Contoh Customer Service: manusia mungkin hanya memproses ~3 komplain/menit, sedangkan AI dapat memproses **1.000–10.000 komplain secara paralel dalam hitungan detik**.
- **Smarter Decision Making:** AI membantu meminimalkan bias persepsi manusia dan menyajikan _insight_ berbasis data sebelum keputusan penting diambil.
- **Future-Ready Skills:** Mempersiapkan keahlian AI adalah langkah strategis untuk tetap relevan di pasar kerja global.

> [!tip] Audio Insight — Analogi Listrik dari Andrew Ng
> **Andrew Ng**, profesor Stanford yang menjadi inspirasi banyak pengajar AI, memberikan kutipan terkenal: _"AI adalah listrik baru."_ Sama seperti listrik yang mentransformasi hampir setiap industri 100 tahun lalu, AI saat ini sedang melakukan transformasi masif yang serupa di segala lini kehidupan manusia.

### 1.3 Siklus Hidup Model AI yang Disederhanakan (AI Model Lifecycle)

Pengembangan model AI mengikuti alur kerja yang terstruktur dan berulang (iteratif):

1. **Problem Understanding** — mendefinisikan tujuan (_goal_) dan kriteria sukses; menganalisis apakah masalah memang membutuhkan solusi AI atau bisa diselesaikan dengan metode konvensional.
2. **Data Preparation** — pengumpulan (_collection_) dan pembersihan data (_clean the data_).
3. **Training** — mengajarkan model menggunakan data yang telah dipersiapkan agar model mengenali pola.
4. **Evaluation** — menguji performa model; jika kurang memuaskan, engineer dapat kembali ke tahap _Training_ atau bahkan _Data Preparation_.
5. **Deployment** — menyajikan model ke lingkungan produksi.
6. **Monitoring** — melacak performa model secara kontinu, karena lingkungan nyata sering berganti.

> [!tip] Audio Insight — Studi Kasus FYP TikTok (Model Drift)
> Model yang dilatih pada 5 Agustus untuk menyarankan konten FYP TikTok mungkin tidak lagi relevan pada bulan September karena pergeseran tren konten (_content shift_). Oleh karena itu, monitoring metrik performa sangat krusial untuk memutuskan kapan model perlu dilatih ulang.

### 1.4 Mitos-Mitos Umum tentang AI Engineer (Debunked)

- **Mitos 1: "Harus Jenius Matematika."** Faktanya, Anda hanya membutuhkan logika dasar dan statistik dasar. Kalkulus mendalam (_fancy calculus_) biasanya hanya dibutuhkan **AI Researcher**, bukan pengguna terapan.
- **Mitos 2: "Membutuhkan Compute Power / Perangkat High-End."** Faktanya, kita jarang melatih model raksasa dari nol — bisa menggunakan **pre-trained model** atau memanggil **API** dari penyedia layanan besar.
- **Mitos 3: "AI Diciptakan untuk Menggantikan Kita."** Faktanya, AI adalah alat bantu (_tool_). Yang akan menggantikan manusia bukan AI itu sendiri, melainkan orang lain yang mahir memanfaatkan AI untuk bekerja lebih efisien.

### 1.5 Kemampuan Utama AI dalam Aplikasi Modern (Core AI Capabilities)

- **Natural Language Processing (NLP):** kemampuan komputer memahami, menafsirkan, dan menghasilkan bahasa manusia. Contoh: ChatGPT, terjemahan mesin, analisis sentimen, _text summarization_, chatbot. Dulu satu model hanya bisa satu tugas; sekarang dengan **Generative AI**, satu model (ChatGPT) menggabungkan banyak keterampilan sekaligus.
- **Computer Vision (CV):** kemampuan komputer memahami input visual (gambar/video). Contoh: _face recognition_, _object detection_, klasifikasi gambar, OCR, kendaraan otonom (sensor kamera mendeteksi objek untuk mengambil keputusan seperti berhenti/menunggu).
- **Compound AI Solutions & Agentic AI:** solusi AI modern bersifat **gabungan (compound)** — kendaraan otonom menggabungkan CV (navigasi) dan NLP (asisten suara). **Agentic AI** mengintegrasikan NLP, CV, _reasoning_, dan _external tools_ untuk sistem cerdas yang mendekati kapabilitas manusia.

### 1.6 Fokus Pembelajaran: Applied AI Engineering

Industri memerlukan engineer yang memahami **full pipeline** — dari pembuatan model hingga penyajiannya (_delivery_) kepada pengguna akhir. Kurikulum mencakup: Programming Fundamental (Python), ML Fundamental, NLP/LLM, Computer Vision, dan Deployment.

**Analogi Chef:**

| Komponen AI | Analogi Chef | Penjelasan |
| --- | --- | --- |
| **AI** | **Chef Terlatih** | Seseorang yang telah mencicipi dan mempelajari ribuan hidangan. |
| **Data** | **Masakan/Hidangan** | Bahan pembelajaran yang dicicipi oleh Chef. |
| **Model** | **Keahlian & Penilaian** | Skill yang terbentuk dari proses mencicipi untuk membuat hidangan baru. |

**Tiga Pilar Utama Applied AI Engineer:** (1) NLP/LLM (_Language_), (2) Computer Vision (_Sight_), (3) Deployment (_Delivery_).

---

## Bab 2 — Dasar Pengembangan Perangkat Lunak & Algoritma

### 2.1 Definisi Pemrograman dan Bahasa Pemrograman

- **Pemrograman (Programming):** proses menciptakan serangkaian instruksi terperinci yang memberitahu komputer cara melakukan tugas tertentu secara efisien.
- **Bahasa Pemrograman (Programming Language):** kosakata dan aturan tata bahasa (sintaksis) yang digunakan untuk memberikan instruksi tersebut — jembatan komunikasi antara logika manusia dan eksekusi mesin.

**Contoh Bahasa Pemrograman Populer:** JavaScript, Java, Golang, PHP, keluarga bahasa C (C, C++, C#).

Untuk melakukan pemrograman dengan baik, seorang pengembang tidak bisa langsung menulis kode secara acak — dibutuhkan rencana langkah-demi-langkah yang jelas, yang disebut **Algoritma**.

### 2.2 Konsep dan Esensi Algoritma

Secara formal, algoritma adalah serangkaian instruksi langkah-demi-langkah untuk memecahkan masalah atau menyelesaikan tugas tertentu.

**Analogi Dunia Nyata: Pembuatan Kopi Hitam**

1. Rebus air hingga mendidih.
2. Masukkan kopi ke dalam cangkir.
3. Tuangkan air panas ke dalam cangkir.
4. Tambahkan gula atau susu sesuai selera.
5. Aduk dan sajikan.

> [!tip] Audio Insight — Pentingnya Detail Parameter dalam Algoritma
> Dalam konteks pemesanan atau instruksi, detail sangat menentukan hasil. Jika seseorang memesan _"kopi hitam jangan kemanisan"_, algoritma harus memiliki parameter yang jelas mengenai takaran gula agar hasil akhir sesuai dengan ekspektasi pengguna.

**4 Karakteristik Utama Algoritma:**

| Karakteristik | Penjelasan |
| --- | --- |
| **Clear & Unambiguous** | Setiap langkah harus jelas dan tidak bermakna ganda. |
| **Step-by-step** | Instruksi harus dijalankan secara berurutan. |
| **Definite Start and End** | Algoritma harus memiliki titik awal yang jelas dan berhenti setelah mencapai solusi. |
| **Effective** | Harus mampu memecahkan masalah dengan benar dan tepat sasaran. |

**Urgensi Algoritma:** menghemat waktu (menghindari _trial-and-error_), optimalisasi sumber daya (memori & daya komputasi), dan akurasi (hasil konsisten setiap kali dijalankan).

### 2.3 Studi Kasus Algoritma di Dunia Nyata

- **Optimalisasi Rute (Google Maps):** algoritma kompleks menganalisis data lalu lintas dan kondisi jalan secara _real-time_ untuk menentukan rute tercepat.
- **Rekomendasi Belanja Online:** algoritma menyaring jutaan pilihan barang untuk menampilkan produk paling relevan berdasarkan data perilaku pengguna.

### 2.4 Representasi Algoritma

**A. Plain Language (Step List)** — menggunakan bahasa manusia sehari-hari. Contoh: mencari angka terbesar dari tiga angka (7, -2, 11):

1. Bandingkan angka pertama (7) dengan angka kedua (-2).
2. Ambil angka yang lebih besar (7).
3. Bandingkan angka tersebut (7) dengan angka ketiga (11).
4. Angka terbesar yang ditemukan adalah hasilnya (11).

**B. Flowchart** — visualisasi proses menggunakan diagram dengan simbol-simbol standar, berguna untuk memvisualisasikan proses dengan banyak percabangan atau logika kompleks.

### 2.5 Simbol Flowchart Standar dan Implementasinya

| Simbol | Nama | Makna |
| --- | --- | --- |
| **Oval** | Terminator | Menandai titik awal (Start) atau akhir (End) dari sebuah sistem. |
| **Persegi Panjang** | Process | Menunjukkan operasi tertentu atau perhitungan internal. |
| **Kertas Robek** | Document | Merepresentasikan output berupa dokumen atau laporan fisik/cetakan. |
| **Belah Ketupat** | Decision | Titik percabangan logika; biasanya menghasilkan jalur "Ya" atau "Tidak". |
| **Jajar Genjang** | Data | Menunjukkan proses input data masuk atau output data keluar dari sistem. |

**Contoh 1 — Penjumlahan Dua Angka (529 + 256):** Start (Terminator) → Read A (Data: 529) → Read B (Data: 256) → Calculate Sum as A + B (Process) → Print Sum (Process/Data: 785) → End (Terminator).

**Contoh 2 — Penentuan Profit atau Loss:** Start → Read Income (1.000) → Read Cost (800) → Decision (Income >= Cost?): jika **Yes**, Profit = Income - Cost → Print Profit (200); jika **No**, Loss = Cost - Income → Print Loss → End.

### 2.6 Wawasan Diskusi — Perspektif Engineering terhadap Algoritma

> [!tip] Audio Insight — Algoritma sebagai Logika Proses Bisnis
> Dalam dunia _engineering_, algoritma dipandang sebagai pengejawantahan dari _business process logic_. Penting bagi seorang pengembang untuk melatih "flow berpikir" di dalam kepala. Menggambar flowchart memang membantu, namun kemampuan untuk menelusuri logika secara mental adalah keterampilan esensial.

> [!warning] Audio Insight — Prinsip Eksekusi Python (Serial, Bukan Paralel)
> Meskipun diagram flowchart bisa terlihat bercabang atau tampak paralel, Python sebagai bahasa yang diinterpretasikan mengeksekusi instruksi secara serial/sekuensial. Kode dijalankan baris demi baris (_line-by-line_) dari atas ke bawah. Cabang logika hanyalah pengalihan urutan eksekusi, bukan eksekusi bersamaan dalam satu waktu.

> [!tip] Audio Insight — Kompleksitas dan "Edge Cases"
> Dunia nyata jauh lebih rumit daripada sekadar alur sukses. Algoritma harus menangani _Edge Cases_ atau kondisi ekstrem, seperti pemesanan makanan saat saldo pelanggan tidak cukup, atau pemesanan barang saat stok tiba-tiba habis tepat sebelum pembayaran.

> [!tip] Audio Insight — Pemrograman Tradisional vs. AI dalam Menangani Aturan
> **Traditional Programming** memerlukan pendefinisian jutaan aturan secara manual (misal instruksi robot menyeberang jalan harus mencakup kondisi lampu hijau, ambulans, kegagalan sensor — sulit untuk skenario tak terbatas). **AI** jauh lebih unggul karena belajar dari data berpasangan (_input-output_), bukan menghafal aturan manual — misalnya menentukan pakaian berdasarkan cuaca yang kompleks (hujan tapi panas, mendidih tapi berangin).

> [!tip] Audio Insight — Abstraksi Perintah "Read"
> Dalam representasi algoritma, instruksi "Read" adalah sebuah abstraksi. Dalam praktik teknis, pembacaan data ini bisa berupa input manual dari keyboard, pembacaan data dari file di penyimpanan, atau pengambilan data secara berkala dari sensor fisik (misal sensor suhu/kelembapan).

---

## Bab 3 — Studi Kasus Logika Lanjutan: Tower of Hanoi

### 3.1 Pengenalan Tower of Hanoi & Aturan Main (Rules)

_[[Kamus & Cheatsheet (JCAIEH M1)#T|Tower of Hanoi]]_ adalah masalah klasik dalam matematika dan ilmu komputer yang sering digunakan untuk menguji kemampuan pemecahan masalah secara logis.

**Komponen Utama:** _N_ buah piringan (_disks_) dengan ukuran berbeda-beda dan 3 tiang (_pegs/rods_):

- **Source (Asal):** tiang tempat piringan pertama kali ditumpuk.
- **Target (Tujuan):** tiang tujuan akhir di mana semua piringan harus dipindahkan.
- **Auxiliary (Pembantu/Helper):** tiang perantara yang digunakan untuk membantu proses pemindahan.

Piringan-piringan awalnya ditumpuk di tiang _Source_ dengan urutan _decreasing size_ (piringan terbesar di dasar, terkecil di puncak).

**Tiga Aturan Mutlak:**

1. Hanya **satu piringan** yang boleh dipindahkan dalam satu waktu.
2. Hanya **piringan teratas** pada suatu tiang yang boleh diambil dan dipindahkan ke tiang lain.
3. Piringan yang **lebih besar tidak boleh** diletakkan di atas piringan yang lebih kecil.

> [!tip] Audio Insight — Analogi Kehidupan Nyata (Montessori)
> Secara filosofis dan praktis, _Tower of Hanoi_ bukan sekadar teori komputer. Dalam metode pendidikan Montessori, alat ini sering digunakan sebagai mainan edukasi untuk balita (_toddler_) — melatih kemampuan motorik halus serta cara berpikir analitis sejak dini melalui pemahaman pola dan batasan aturan.

### 3.2 Pendekatan Manual vs Pendekatan Rekursif (Recursive Logic)

**Keterbatasan Solusi Manual:** mendefinisikan langkah demi langkah secara kaku ("pindahkan disk 1 ke C, disk 2 ke B") **tidak scalable** — langkah yang berhasil untuk N=3 akan gagal/terlalu rumit untuk N=4 atau lebih, dan tidak memiliki pola umum yang bisa diadaptasi.

**Keunggulan Logika Rekursif:** fungsi yang memanggil dirinya sendiri di dalam tubuh fungsi tersebut untuk menyelesaikan parameter masalah yang lebih kecil. Masalah besar (N) dipecah menjadi masalah lebih kecil (N−1).

Fungsi utama biasanya didefinisikan sebagai `Hanoi(N, Source, Target, Helper)`. Keajaiban logika ini terletak pada _Role Shifting_ (Pertukaran Peran) tiang secara dinamis — pada satu langkah tiang B bertindak sebagai _Helper_, pada langkah berikutnya bisa bertukar peran menjadi _Target_ sementara.

### 3.3 Pembedahan Langkah-demi-Langkah (Step-by-Step Trace)

- **[[Kamus & Cheatsheet (JCAIEH M1)#B|Base Case]]:** terjadi ketika **N = 1** — pindahkan satu piringan tunggal langsung dari _Source_ ke _Target_ tanpa bantuan tiang lain.
- **[[Kamus & Cheatsheet (JCAIEH M1)#R|Recursive Case]]:** untuk setiap **N > 1**, algoritma mengikuti pola tiga langkah:
  1. Pindahkan **N-1** piringan dari _Source_ ke _Helper_ (menggunakan _Target_ sebagai bantuan sementara).
  2. Pindahkan piringan terbesar (ke-N) langsung dari _Source_ ke _Target_.
  3. Pindahkan **N-1** piringan yang tadi di _Helper_ ke _Target_ (menggunakan _Source_ sebagai bantuan sementara).

| Kasus | Deskripsi Logika | Total Langkah |
| --- | --- | --- |
| **N = 1** | `Hanoi(1, A, C, B)`: langsung pindahkan disk dari A ke C. | 1 |
| **N = 2** | `Hanoi(2, A, C, B)`: disk kecil (N-1) dipindah ke tiang pembantu (B) agar disk besar bebas berpindah ke tujuan (C), lalu disk kecil dipindah dari B ke C. | 3 |
| **N = 3** | `Hanoi(3, A, C, B)`: memanggil `Hanoi(2)` di dalamnya, menghasilkan alur optimal tanpa langkah terbuang. | 7 |
| **N = 4** | Mendemonstrasikan penumpukan 3 piringan di tiang pembantu untuk membebaskan piringan keempat (terbesar). | 15 |

**Kasus Ekstrem (N = 1000):** meskipun mustahil dilakukan manual, _Recursive Logic_ tetap bekerja sempurna — algoritma memandang 999 piringan teratas sebagai satu kesatuan yang harus dipindahkan ke _helper_ terlebih dahulu, menyisakan piringan ke-1000 (terbesar) untuk dipindahkan ke _target_, lalu mengembalikan 999 piringan di atasnya.

### 3.4 Implementasi Python dari Tower of Hanoi (Kode Tambahan)

Modul sumber membahas logika ini secara konseptual tanpa kode Python konkret. Berikut adalah implementasi kerja yang menerapkan persis pola Base Case & Recursive Case di atas:

```python
def hanoi(n, source, target, helper):
    if n == 1:
        # Base case: hanya 1 piringan, langsung pindah
        print(f"Pindahkan piringan 1 dari {source} ke {target}")
        return
    # Recursive case
    hanoi(n - 1, source, helper, target)   # 1. pindahkan N-1 ke helper
    print(f"Pindahkan piringan {n} dari {source} ke {target}")  # 2. pindahkan piringan terbesar
    hanoi(n - 1, helper, target, source)   # 3. pindahkan N-1 dari helper ke target

hanoi(3, "A", "C", "B")
# Output:
# Pindahkan piringan 1 dari A ke C
# Pindahkan piringan 2 dari A ke B
# Pindahkan piringan 1 dari C ke B
# Pindahkan piringan 3 dari A ke C
# Pindahkan piringan 1 dari B ke A
# Pindahkan piringan 2 dari B ke C
# Pindahkan piringan 1 dari A ke C
# (Total 7 langkah, sesuai tabel N=3 di atas)
```

> [!info] Lihat juga
> Konsep fungsi (`def`, parameter, `return`) dibahas lebih dalam di [[Sesi 05 - Python Function and File Handling (JCAIEH M1)|Sesi 05 - Python Function and File Handling]]. Rekursi juga dibandingkan langsung dengan _looping_ di [[Sesi 03 - Conditional and Loop Statement (JCAIEH M1)|Sesi 03 - Conditional and Loop Statement]] (Bab 5, perbandingan alokasi memori _stack_).

### 3.5 Insight Filosofi Algoritma

> [!tip] Audio Insight — Pentingnya Memulai dari "Solvable First"
> Dalam merancang algoritma, langkah pertama bukan mencoba mengoptimalkannya secara langsung, melainkan mencari penyelesaian yang paling mudah dan sederhana terlebih dahulu. Setelah masalah tersebut terpecahkan (_solvable_), barulah efisiensi ditingkatkan.

> [!tip] Audio Insight — Konsep Efisiensi Langkah (Optimal Moves)
> _Tower of Hanoi_ memberikan pola matematika pasti untuk jumlah langkah minimum, yaitu **2^N − 1**. Algoritma rekursif secara otomatis mengikuti pola ini, memastikan tidak ada pemborosan tenaga atau memori komputer.

> [!warning] Audio Insight — Logika N-1 sebagai Kunci Menuju Base Case
> Penggunaan `N-1` pada parameter fungsi rekursif bukan sekadar pengurangan angka, melainkan strategi untuk mencapai _Base Case_ (kondisi N=1). Tanpa pengurangan parameter ini, fungsi akan memanggil dirinya sendiri selamanya (_infinite loop_ / infinite recursion).

> [!tip] Audio Insight — Tujuan Utama Belajar Algoritma
> Belajar algoritma seperti _Tower of Hanoi_ bukan untuk menghafal sintaks bahasa pemrograman tertentu (Python atau Java). Tujuan sejatinya adalah melatih "jam terbang" pola pikir terstruktur — sehingga seorang _engineer_ dapat melakukan abstraksi masalah dunia nyata yang rumit menjadi logika komputer yang sistematis dan efisien.

---

## Bab 4 — Pengenalan Python & Lingkungan Kerja

### 4.1 Pengenalan Python sebagai High-Level Language

Python adalah bahasa pemrograman yang sangat fleksibel dan populer untuk berbagai domain: AI, _web development_, _backend development_, _data analysis_, hingga otomasi tugas repetitif.

- **[[Kamus & Cheatsheet (JCAIEH M1)#H|High-Level Language]] (Python):** sintaksisnya dirancang mendekati bahasa alami manusia (Inggris), sehingga relatif mudah dipelajari, dibaca, dan dipahami.
- **Low-Level Language:** seperti bahasa mesin (0 dan 1), sangat sulit dimengerti langsung oleh manusia, berinteraksi langsung dengan perangkat keras tanpa abstraksi luas.

### 4.2 Deep Dive: Interpreted vs Compiled Programming Language

- **[[Kamus & Cheatsheet (JCAIEH M1)#I|Interpreted Language]] (Python):** Python bekerja menggunakan _[[Kamus & Cheatsheet (JCAIEH M1)#I|Interpreter]]_, mengeksekusi kode secara langsung baris-demi-baris (_line-by-line_) secara sekuensial saat program dijalankan. Karena bekerja sekuensial, perancangan algoritma melalui flowchart harus logis dan berurutan agar selaras dengan cara kerja _interpreter_.
- **[[Kamus & Cheatsheet (JCAIEH M1)#C|Compiled Language]] (C/C++):** seluruh kode program harus diterjemahkan sekaligus oleh _[[Kamus & Cheatsheet (JCAIEH M1)#C|Compiler]]_ menjadi kode mesin mandiri (_standalone executable binary_) sebelum dijalankan.

| Karakteristik | Interpreted (Python) | Compiled (C/C++) |
| --- | --- | --- |
| **Proses Development** | Jauh lebih cepat (tulis dan langsung jalankan). | Lebih lambat karena butuh proses kompilasi ulang setiap perubahan. |
| **Debugging** | Lebih mudah; kesalahan terlacak tepat pada baris yang dieksekusi. | Lebih kompleks; kesalahan seringkali baru terdeteksi setelah kompilasi. |
| **Runtime Performance** | Relatif lebih lambat karena interpretasi terjadi saat aplikasi berjalan. | Sangat cepat karena kode sudah dalam bentuk biner mesin siap pakai. |

### 4.3 Setup Lingkungan Pengembangan (Development Environment)

**Alat Utama dan Ekstensi:**

- **IDE / Code Editor:** Visual Studio Code (VSCode).
- **Ekstensi VSCode Esensial:** **Python** (dukungan penuh bahasa Python), **Jupyter** (notebook interaktif), **Pylance** (_intellectual language support_ seperti auto-complete), **Gitlens** (opsional, visualisasi riwayat kode).

**Virtual Environment ([[Kamus & Cheatsheet (JCAIEH M1)#C|Venv]] & Conda)** — mengisolasi paket-paket yang dibutuhkan proyek tertentu agar tidak berbenturan dengan proyek lain.

- **Venv:** modul bawaan Python untuk membuat lingkungan virtual.
- **Conda/Miniconda:** pengelola lingkungan dan paket yang lebih luas.

> [!tip] Wawasan Penting — Venv Tidak Diperlukan Jika Sudah Ada Conda
> Jika pengguna telah menginstal Anaconda atau Conda, maka instalasi venv secara terpisah tidak lagi diperlukan. Hal ini dikarenakan Conda sudah memaketkan instalasi Python dan pengelola lingkungannya sendiri secara terintegrasi.

**Source Code Management ([[Kamus & Cheatsheet (JCAIEH M1)#G|Git]])** — alat wajib untuk manajemen riwayat kode: **Versioning** (melacak setiap perubahan kode dari waktu ke waktu) dan **Kolaborasi** (memungkinkan tim bekerja pada bagian kode berbeda secara paralel tanpa merusak pekerjaan satu sama lain). Lihat pembahasan lengkap di [[Sesi 02 - Intro to Git and GitHub (JCAIEH M1)|Sesi 02 - Intro to Git and GitHub]].

> [!tip] Tips Verifikasi — Cek Instalasi Git
> Untuk memastikan Git sudah terpasang, ketik perintah `git` di dalam terminal VSCode. Jika muncul daftar bantuan perintah, berarti Git telah dikenali oleh sistem.

**Troubleshooting Docker (Kasus Windows Home 11):** tantangan instalasi Docker Desktop pada Windows Home 11 diselesaikan dengan penyesuaian pengaturan Virtualisasi di tingkat BIOS perangkat, dan eksekusi perintah khusus melalui Command Prompt (CMD) untuk melepas batasan sistem edisi "Home".

### 4.4 Bedah Kode Pertama: Hello World!

Penulisan program 'Hello World' merupakan tradisi filosofis di dunia pemrograman sebagai langkah awal untuk memverifikasi bahwa lingkungan kerja telah siap.

```python
print('Hello world!')
# Output:
# Hello world!
```

**Bedah Elemen Kode:**

- **Fungsi Bawaan `print()`:** _built-in function_ dalam Python yang mengirimkan dan menampilkan keluaran (_output_) data ke layar monitor.
- **String Literal (`'Hello world!'`):** teks di dalam tanda kutip (tunggal atau ganda) — representasi data teks yang diproses oleh `print()`.

Pernyataan ini membuktikan bahwa Python adalah bahasa yang sangat ringkas — instruksi yang jelas dapat diberikan hanya dalam satu baris kode tanpa struktur _boilerplate_ rumit seperti pada bahasa lainnya.

---

## Bab 5 — Konsep Dasar Pemrograman Python

### 5.1 Konsep Variabel & Struktur Penyimpanan Memori

- **Definisi Formal:** variabel dianalogikan sebagai sebuah kotak (_box_) yang memiliki label. Label tersebut adalah nama variabel, dan isi di dalamnya adalah data atau nilai yang disimpan.
- **Mekanisme Memori (RAM):** saat variabel dibuat, Python menyimpan nilai/data di alamat memori RAM. Nama variabel berfungsi sebagai "label pengenal" agar pengembang dapat mengakses kembali nilai tersebut secara efisien dan berulang kali.
- **Operator Penugasan (`=`):** mengaitkan nilai di sisi kanan ke nama variabel di sisi kiri.

```python
message = "hello"  # "hello" disimpan di RAM dengan label 'message'
age = 20           # 20 disimpan di RAM dengan label 'age'
```

### 5.2 Aturan Mutlak Penamaan Variabel (Variable Naming)

- **Karakter yang Diperbolehkan:** huruf (A-Z, a-z), angka (0-9), dan _underscore_ `_`.
- **Larangan Angka di Depan:** karakter pertama tidak boleh berupa angka.
- **Case-Sensitive:** `Nama` berbeda dengan `nama`.
- **Larangan Python Keywords:** tidak boleh menggunakan _Reserved Words_ seperti `if`, `for`, `class`, `def`, `True`, `False`, `None`, dll.

| Nama Variabel | Status | Alasan Teknis |
| --- | --- | --- |
| `name` | Valid | Menggunakan huruf kecil standar. |
| `2name` | Invalid | Dimulai dengan angka (_Starts with a digit_). |
| `student_name` | Valid | Menggunakan _underscore_ sebagai pemisah. |
| `student-name` | Invalid | Tanda hubung/minus (`-`) tidak diperbolehkan. |
| `total2` | Valid | Angka diperbolehkan asal bukan di karakter pertama. |
| `total price` | Invalid | Spasi tidak diperbolehkan dalam nama variabel. |
| `_count` | Valid | _Underscore_ di awal diperbolehkan. |
| `class` | Invalid | `class` adalah kata kunci Python (_Python keyword_). |

```python
# Contoh yang VALID — akan berjalan tanpa error
name = "andi"
student_name = "budi"
total2 = 100
_count = 0

# Contoh INVALID di bawah ini akan memicu SyntaxError jika benar-benar dijalankan:
# 2name = "budi"        -> SyntaxError: invalid decimal literal
# student-name = "budi" -> SyntaxError (dibaca sebagai pengurangan: student - name)
# total price = 100     -> SyntaxError: invalid syntax
# class = "IPS"         -> SyntaxError: 'class' adalah keyword
```

> [!tip] Best Practice (PEP 8)
> Sangat disarankan menggunakan gaya penulisan `snake_case`, yaitu huruf kecil semua dan memisahkan antar kata dengan _underscore_ (contoh: `is_logged_in`, `total_price`).

### 5.3 Deep Dive Tipe Data Dasar (Basic Data Types)

- **Int (Integer):** bilangan bulat tanpa desimal (contoh: 10, -5).
- **Float:** nilai desimal/pecahan (contoh: 19.99, 3.14).
- **Bool (Boolean):** hanya memiliki dua nilai: `True` atau `False`.
- **Str (String):** teks/urutan karakter dibungkus tanda kutip tunggal (`'`) atau ganda (`"`).
- **[[Kamus & Cheatsheet (JCAIEH M1)#N|NoneType]]:** tipe data khusus untuk merepresentasikan ketiadaan nilai (`None`).

> [!warning] Audio Insight — Perbedaan 'None' vs '0'
> Terdapat perbedaan fundamental antara angka 0 dan `None`. Angka 0 tetap merupakan sebuah nilai numerik dengan tipe data Integer. Sedangkan `None` adalah representasi kosong atau tidak adanya nilai sama sekali (NoneType). Analoginya, 0 adalah laci yang berisi angka nol, sedangkan `None` adalah laci yang benar-benar kosong tanpa barang di dalamnya.

```python
angka_nol = 0
nilai_kosong = None

print(type(angka_nol))     # Output: <class 'int'>
print(type(nilai_kosong))  # Output: <class 'NoneType'>
print(angka_nol == nilai_kosong)  # Output: False -> nilainya beda secara konsep
```

### 5.4 Tipe Data Koleksi (Collection Data Types)

Wadah untuk struktur organisasi data, memungkinkan penyimpanan banyak nilai dalam satu variabel:

- **[[Kamus & Cheatsheet (JCAIEH M1)#L|List]]:** koleksi terurut yang bersifat _mutable_ (isinya dapat diubah, ditambah, atau dihapus setelah dibuat). Dideklarasikan dengan `[]`.
- **[[Kamus & Cheatsheet (JCAIEH M1)#T|Tuple]]:** koleksi terurut yang bersifat _immutable_ (isinya tidak dapat diubah setelah didefinisikan). Dideklarasikan dengan `()`.
- **[[Kamus & Cheatsheet (JCAIEH M1)#S|Set]]:** koleksi tidak terurut dari elemen yang unik — data duplikat otomatis dihapus. Dideklarasikan dengan `{}`.
- **[[Kamus & Cheatsheet (JCAIEH M1)#D|Dict (Dictionary)]]:** koleksi pasangan kunci-nilai (_key-value pairs_), sangat efisien untuk pencarian data berdasarkan kata kunci. Format: `{key: value}`.

```python
message = "Hello"
print(type(message))  # Output: <class 'str'>
```

> [!info] Lihat juga
> Keempat tipe data koleksi ini dibahas jauh lebih mendalam (metode, mutability, indexing/slicing) di [[Sesi 04 - Data Types Collection Notes (JCAIEH M1)|Sesi 04 - Data Types Collection Notes]] — termasuk mengapa List bersifat _mutable_ sedangkan Tuple _immutable_, dan perbandingan `id()` memori antar variabel.

### 5.5 Metode Manipulasi String (String Built-in Methods)

Python menyediakan berbagai metode bawaan untuk memproses teks secara otomatis:

| Metode | Fungsi |
| --- | --- |
| `.upper()` | Mengubah semua karakter menjadi huruf besar. |
| `.lower()` | Mengubah semua karakter menjadi huruf kecil. |
| `.strip()` | Menghapus spasi kosong di awal dan akhir string. |
| `.replace(lama, baru)` | Mengganti bagian teks tertentu dengan teks baru. |
| `.split()` | Memecah string menjadi list berdasarkan pemisah tertentu. |
| `.join()` | Menggabungkan elemen list menjadi satu string. |
| `.find()` | Mencari posisi indeks dari karakter atau kata tertentu. |
| `.startswith()` | Mengecek apakah string dimulai dengan karakter tertentu (True/False). |
| `.endswith()` | Mengecek apakah string diakhiri dengan karakter tertentu (True/False). |
| `.count()` | Menghitung jumlah kemunculan karakter tertentu dalam string. |
| `.format()` | Metode lama untuk menyisipkan variabel ke dalam string. |
| `.isalpha()` | Mengecek apakah seluruh isi string adalah huruf. |
| `.isdigit()` | Mengecek apakah seluruh isi string adalah angka. |
| `.isalnum()` | Mengecek apakah string hanya berisi huruf dan angka. |

Contoh kode demonstrasi tiap metode (ditambahkan sebagai pelengkap karena sumber asli hanya berupa daftar deskripsi):

```python
kalimat = "  Halo Dunia Python  "

print(kalimat.upper())          # Output: '  HALO DUNIA PYTHON  '
print(kalimat.lower())          # Output: '  halo dunia python  '
print(kalimat.strip())          # Output: 'Halo Dunia Python' (spasi awal/akhir hilang)
print(kalimat.replace("Dunia", "Python"))  # Output: '  Halo Python Python  '

kata = kalimat.strip().split()  # Memecah berdasarkan spasi
print(kata)                     # Output: ['Halo', 'Dunia', 'Python']

gabung = "-".join(kata)
print(gabung)                   # Output: 'Halo-Dunia-Python'

print(kalimat.find("Dunia"))    # Output: 7 (indeks awal kemunculan "Dunia")
print(kalimat.strip().startswith("Halo"))  # Output: True
print(kalimat.strip().endswith("Python"))  # Output: True
print(kalimat.count("a"))       # Output: 3 (jumlah huruf 'a' di kalimat)

nama = "Reiner"
umur = 31
print("Nama saya {} dan umur saya {}".format(nama, umur))
# Output: Nama saya Reiner dan umur saya 31

print("Python3".isalpha())   # Output: False (mengandung angka)
print("Python3".isdigit())   # Output: False (mengandung huruf)
print("Python3".isalnum())   # Output: True (huruf + angka saja, tanpa spasi/simbol)
```

### 5.6 Formatted String Literals (f-Strings)

[[Kamus & Cheatsheet (JCAIEH M1)#F|f-Strings]] adalah cara termudah dan paling efisien untuk menyisipkan variabel ke dalam teks.

- **Konsep:** tambahkan huruf `f` sebelum tanda kutip pembuka dan bungkus variabel/ekspresi dengan `{}`.
- **Kelebihan vs Concatenation:** dibandingkan penggabungan manual dengan `+` (yang memerlukan konversi tipe data manual seperti `str(age)`), f-String lebih bersih, ringkas, dan performanya lebih cepat.
- **Evaluasi Ekspresi:** f-String memungkinkan operasi matematika langsung di dalam `{}`.

```python
age = 25
# Manual Concatenation
message1 = "I am " + str(age) + " years old."

# f-String (Lebih Bersih)
message2 = f"Next year I will be {age + 1} years old."
print(message1)  # Output: I am 25 years old.
print(message2)  # Output: Next year I will be 26 years old.
```

### 5.7 User Input & Pengolahan Data

Fungsi `input()` digunakan untuk berinteraksi dengan pengguna.

- **Mekanisme:** saat dipanggil, program menjeda eksekusi, menunggu pengguna mengetik sesuatu di konsol, lalu menekan Enter.
- **Aturan Mutlak:** data yang diterima `input()` selalu bertipe String (`str`), meskipun pengguna memasukkan angka. Untuk operasi matematika, data harus dikonversi terlebih dahulu.

```python
umur_teks = input("Masukkan umur anda: ")   # umur_teks selalu str, walau diketik "20"
print(type(umur_teks))                       # Output: <class 'str'>

umur_angka = int(umur_teks)                  # konversi eksplisit ke int
print(umur_angka + 1)                        # baru bisa dihitung matematika
```

### 5.8 Operasi Angka & Modul Matematika (Math Module)

**Fungsi Bawaan (Tanpa Import):** `abs()` (nilai mutlak), `round()` (membulatkan), `pow()` (perpangkatan), `min()`/`max()` (nilai terkecil/terbesar), `sum()` (menjumlahkan koleksi angka), `int()`/`float()` (konversi tipe numerik).

**Modul Matematika (`import math`):** `math.sqrt()` (akar kuadrat), `math.ceil()` (pembulatan ke atas), `math.floor()` (pembulatan ke bawah), `math.factorial()` (faktorial), konstanta `math.pi` (3.14...), `math.e`, `math.inf` (tak hingga), `math.nan` (Not a Number).

```python
# Fungsi bawaan (tanpa import)
print(abs(-7))        # Output: 7
print(round(3.14159, 2))  # Output: 3.14
print(pow(2, 3))       # Output: 8 (2 pangkat 3)
print(min(4, 9, 1))    # Output: 1
print(max(4, 9, 1))    # Output: 9
print(sum([1, 2, 3]))  # Output: 6

# Modul math (butuh import)
import math
print(math.sqrt(16))       # Output: 4.0
print(math.ceil(4.1))      # Output: 5
print(math.floor(4.9))     # Output: 4
print(math.factorial(5))   # Output: 120  (5*4*3*2*1)
print(math.pi)              # Output: 3.141592653589793
print(math.e)                # Output: 2.718281828459045
print(math.inf)              # Output: inf
print(math.nan)              # Output: nan
```

### 5.9 Konversi Tipe Data (Type Conversion)

- **String Conversion:** `str()`.
- **Numeric Conversion:** `int()` atau `float()`. Perlu dicatat bahwa `int(3.99)` menghasilkan `3` karena fungsi ini memangkas (_truncation_) bagian desimal, **bukan** membulatkannya.
- **Boolean Conversion ([[Kamus & Cheatsheet (JCAIEH M1)#T|Truthy]] & [[Kamus & Cheatsheet (JCAIEH M1)#F|Falsy]]):**
  - **Falsy** (menghasilkan `False`): angka `0`, string kosong `""`, list kosong `[]`, tuple kosong `()`, set kosong `{}`, dan `None`.
  - **Truthy** (menghasilkan `True`): angka selain 0 (positif maupun negatif), string berisi (termasuk spasi atau teks `"False"`), dan koleksi dengan minimal satu elemen.

```python
print(int(3.99))    # Output: 3  (BUKAN 4 — ini truncation, bukan pembulatan)
print(int(-3.99))   # Output: -3 (dipangkas ke arah nol, bukan dibulatkan ke bawah)
print(round(3.99))  # Output: 4  (round() membulatkan sungguhan)

# Truthy & Falsy
print(bool(0))       # Output: False
print(bool(""))      # Output: False
print(bool([]))      # Output: False
print(bool("False")) # Output: True  -> string "False" TETAP truthy karena isinya tidak kosong!
print(bool([0]))     # Output: True  -> list berisi [0] tetap truthy karena ada 1 elemen
```

### 5.10 Operator Dasar Pemrograman

**Operator Aritmatika:** `+`, `-`, `*`, `/` (tambah, kurang, kali, bagi), `%` ([[Kamus & Cheatsheet (JCAIEH M1)#M|Modulo]] — sisa bagi), `**` (perpangkatan), `//` ([[Kamus & Cheatsheet (JCAIEH M1)#F|Floor Division]] — pembagian bulat, menghilangkan desimal).

**[[Kamus & Cheatsheet (JCAIEH M1)#A|Augmented Assignment Operators]]** — menyingkat penulisan operasi aritmatika sekaligus penugasan nilai kembali ke variabel:

```python
n = 8
n += 5   # sama dengan n = n + 5  -> n sekarang 13
print(n)  # Output: 13
n *= 2   # sama dengan n = n * 2  -> n sekarang 26
print(n)  # Output: 26
```

**Operator Perbandingan:** `==`, `!=`, `>`, `<`, `>=`, `<=` (selalu mengembalikan Boolean).

**Operator Logika:** `and` (True jika kedua kondisi benar), `or` (True jika salah satu kondisi benar), `not` (membalikkan nilai logika).

```python
x = 5
print(x > 3 and x < 10)  # Output: True
print(x < 3 or x == 5)   # Output: True
print(not (x > 10))       # Output: True
```

> [!info] Lihat juga
> Operator perbandingan dan logika ini dibahas jauh lebih mendalam — termasuk tabel _truth table_ lengkap dan konsep _short-circuit evaluation_ — di [[Sesi 03 - Conditional and Loop Statement (JCAIEH M1)|Sesi 03 - Conditional and Loop Statement]] Bab 2.

---

## Bab 6 — Pengantar Pseudocode & Latihan Mandiri Pemecahan Masalah

### 6.1 Konsep & Definisi Pseudocode

**Definisi Formal:** Pseudocode adalah versi bahasa pemrograman yang "lebih mudah dipahami" (_easier-to-understand_), disajikan dalam bentuk bahasa alami sederhana (_simple natural language_) yang menjembatani komunikasi antara logika manusia dan sintaks komputer yang kaku.

**Peran Utama dalam Algoritma:** memvisualisasikan detail proses pemecahan masalah secara bertahap (_step-by-step process_) sebelum menulis kode dalam sintaks pemrograman nyata (Python, JavaScript, dsb.), untuk memastikan alur logika sudah benar dan efisien.

**Analisis Kegunaan:** bagi pengembang pemula, pseudocode sangat krusial untuk menghindari hambatan berpikir akibat kendala teknis sintaks bahasa pemrograman (_syntax block_). Dengan memisahkan logika dari aturan penulisan kode yang rumit, pengembang dapat berfokus sepenuhnya pada penyelesaian masalah itu sendiri.

### 6.2 Bedah Contoh Desain Pseudocode: Area of Rectangle

**Contoh Kasus:** menghitung luas persegi panjang berdasarkan panjang (_length_) dan lebar (_width_). Rumus matematika formal: `Area = Length * Width`.

| Langkah | Aktivitas | Representasi Visual / Contoh |
| --- | --- | --- |
| **Langkah 1** | Mendefinisikan variabel awal dan menetapkan nilainya (_assignment_). | `const width = 10;` <br> `const length = 5;` |
| **Langkah 2** | Mendefinisikan variabel baru untuk menyimpan hasil dan mengimplementasikan formula perkalian. | `const areaOfRectangle = width * length;` |

### 6.3 Analisis Logika Lima Latihan Mandiri (Exercises)

**Latihan 1: Menghitung Luas Persegi Panjang** — Input `length = 5`, `width = 3`. Logika: perkalian sederhana. Output: `15`.

**Latihan 2: Menghitung Keliling Persegi Panjang** — Input `length = 5`, `width = 3`. Formula: `Perimeter = 2 * (length + width)`. Output: `16`.

**Latihan 3: Menghitung Properti Lingkaran** — Input `radius = 5`. Formula: `Diameter = 2 * radius`; `Circumference = 2 * pi * radius`; `Area = pi * radius^2`. Output: Diameter = 10, Circumference = 31.4159, Area = 78.539.

**Latihan 4: Mencari Sudut Ketiga Segitiga** — Input dua sudut, misal `a = 80`, `b = 65`. Formula: `Sudut ketiga = 180 - (a + b)`. Dasar teori: total sudut dalam segitiga selalu 180°. Output: `35`.

**Latihan 5: Mengonversi Hari ke Tahun, Bulan, dan Hari** — memerlukan pemetaan logika menggunakan pembagian bulat dan modulus. Catatan standar: 1 tahun = 365 hari, 1 bulan = 30 hari.

- **Langkah Logika:** (1) `years = days // 365`; (2) `remaining_days_1 = days % 365`; (3) `months = remaining_days_1 // 30`; (4) `final_days = remaining_days_1 % 30`.

| Input | Hasil Konversi |
| --- | --- |
| 400 Hari | 1 Tahun, 1 Bulan, 5 Hari |
| 366 Hari | 1 Tahun, 0 Bulan, 1 Hari |

### 6.4 Integrasi Diskusi Interaktif & Insight Dosen

> [!tip] Audio Insight — Media Penulisan Tugas: Notes Aplikasi Boleh, Tak Wajib Python
> Dalam diskusi antara mahasiswa (Reza & Adiba) dengan dosen, ditegaskan bahwa latihan mandiri ini dapat dikerjakan cukup di aplikasi catatan (_notes_) biasa. Mahasiswa diperbolehkan menggunakan bahasa alami atau pseudocode murni dan tidak diwajibkan langsung menulis dalam sintaks Python jika belum merasa terbiasa. Meski begitu, dosen tetap menganjurkan mahasiswa yang ingin bereksplorasi menggunakan VS Code untuk mencoba mengeksekusi script Python secara langsung, karena praktik langsung memberikan pengalaman belajar yang lebih mendalam.

> [!tip] Audio Insight — Filosofi "Pola Pikir Algoritma"
> Dosen menegaskan bahwa kefasihan menghafal sintaks Python pada pertemuan awal bukanlah hal terpenting. Hal yang paling mendasar adalah melatih pola pikir terstruktur dalam menyelesaikan masalah (_problem-solving mindset_). Poin utamanya: pahami alur berpikir algoritma di kepala terlebih dahulu; jika alur logika sudah benar, translasi ke baris kode pemrograman riil akan menjadi sangat mudah. Kekuatan seorang pengembang terletak pada logikanya, bukan hanya pada kemampuannya mengetik sintaks.

---

## Bab 7 — Latihan Code: Data Collection & Membuat Pesan

### 7.1 Kasus Membuat Keterangan Data Collection

> Lihat catatan tipe-tipe data koleksi di [[Sesi 01 - Introduction to DS Python Statistics SQL Git and GitHub (JCAIEH M1)#5.4 Tipe Data Koleksi (Collection Data Types)|Bab 5.4]] di atas, dan pembahasan lengkapnya di [[Sesi 04 - Data Types Collection Notes (JCAIEH M1)|Sesi 04 - Data Types Collection Notes]].

**7.1.1 Memberi keterangan kata** — jenis data string (str). Variabel: `binatang`. Data: `"anjing hitam besar"`, `"kucing berekor pendek"`.

```python
binatang = "anjing hitam besar"
print(binatang)
# Output: anjing hitam besar

binatang = "kucing berekor pendek"
print(binatang)
# Output: kucing berekor pendek
```

**7.1.2 Memberi keterangan angka** — jenis data integer (int). Variabel: `binatang`. Data: `20`.

```python
binatang = 20
print(binatang)
# Output: 20
```

**7.1.3 Mencampur variabel & tipe data** — mencampur variabel dalam sebuah wadah yakni _associative array_ dengan simbol `{}`. Kurung kurawal itu adalah dictionary.

Tugasnya: (1) masukkan _key_ ke dalam variabel; (2) masukkan data ke dalam _key_.

```python
daftar_binatang = {
    "pinguin_1": "hitam lucu",
    "jerapah_1": "berleher panjang",
    "armadilo_1": "berkulit keras"
}
print(daftar_binatang["armadilo_1"])
# Output: berkulit keras
```

Tujuan dari rancangan kode ini adalah untuk mengalokasikan ruang memori besar bernama `daftar_binatang`, lalu menyimpan tiga data keterangan binatang ke dalamnya secara terstruktur. Dengan format Dictionary, developer nantinya bisa dengan mudah memanggil keterangan spesifik secara akurat (misalnya mencari keterangan armadilo tanpa harus membaca data pinguin).

### 7.2 Membuat Pesan

**7.2.1 Mencetak Pesan — Cara Manual**

Setiap kode harus diperintah dulu agar bisa mengambil aksi. Untuk mencetak pesan, harus dibuat _message_ dulu yang isinya memanggil data collection kita.

```python
age = 32
message1 = "saya" + str(age) + "tahun"
print(message1)
# Output: saya32tahun
```

**7.2.2 f-string — Contoh Gampang**

Kasus: menambahkan umur dari data collection sekaligus membuat kalimat. Memanggil `age` dan menambahkan `+ 1`.

```python
age = 32
message2 = f"tahun depan saya akan berumur {age + 1} tahun"
print(message2)
# Output: tahun depan saya akan berumur 33 tahun
```

**7.2.3 Logika Percabangan (If-Else) & Boolean**

Menyiapkan Data Collection dan Kondisi (Boolean):

```python
umur = 31
sudah_tua = umur > 50
```

Mengatur percabangan keputusan dengan If-Else. Jika kondisi `sudah_tua` terbukti benar (`True`), maka `warna_rambut` diisi `"putih"`; selain itu (`False`) diisi `"hitam"`:

```python
if sudah_tua == True:
    warna_rambut = "putih"
else:
    warna_rambut = "hitam"
```

Mencetak logika murni (True/False) menggunakan f-String untuk melihat langsung wujud isi variabel Boolean `sudah_tua`:

```python
message3 = f"reiner sudah {umur} tahun. Apakah dia rambut dia putih? {sudah_tua}"
print(message3)
# Output: reiner sudah 31 tahun. Apakah dia rambut dia putih? False
# (karena 31 masih di bawah 50 tahun)
```

Mencetak variabel yang sudah diubah oleh If-Else — tujuannya adalah **menerjemahkan data yang diproses mesin agar menjadi informasi yang ramah dibaca oleh manusia**:

```python
message4 = f"reiner sudah {umur} tahun. Warna rambut dia adalah {warna_rambut}"
print(message4)
# Output: reiner sudah 31 tahun. Warna rambut dia adalah hitam
```

> [!info] Lihat juga
> Struktur `if-else` yang dipakai di atas dibahas secara sistematis (termasuk `if-elif-else`, _nested if_, dan aturan indentasi) di [[Sesi 03 - Conditional and Loop Statement (JCAIEH M1)|Sesi 03 - Conditional and Loop Statement]] Bab 3–4.

---

## Bab 8 — Review Fondasi Pemrograman Python

### 8.1 Logika Pemrograman Matematika & Geometri Dasar

Pemrograman dasar sering diawali dengan implementasi formula matematika untuk menyelesaikan persoalan geometri sederhana. Fokus utama: pendefinisian variabel yang tepat dan pemilihan tipe data yang sesuai dengan hasil kalkulasi.

**8.1.1 Perhitungan Persegi Panjang (Rectangle)**

Variabel yang terlibat: `length`, `width`, `area`, `perimeter`.

```python
length = 5
width = 3

area = length * width
perimeter = 2 * (length + width)

print(area)       # Output: 15
print(perimeter)  # Output: 16
```

> [!tip] Audio Insight — Tipe Data Hasil Perhitungan Geometri Persegi Panjang
> Dalam diskusi antara Brian dan instruktur, ditekankan bahwa variabel seperti `length`, `width`, dan `perimeter` umumnya menggunakan tipe data **Integer** (bilangan bulat) jika input awal tidak mengandung desimal. Hasil akhir dapat langsung ditampilkan sebagai angka tanpa perlu tambahan teks penjelasan jika tujuannya adalah _output_ langsung.

**8.1.2 Formulasi Lingkaran (Circle) dan Analisis Tipe Data**

Perhitungan lingkaran memiliki kompleksitas lebih tinggi karena melibatkan konstanta π (Pi), yang secara otomatis memengaruhi tipe data hasil kalkulasi.

- **Formula Dasar:** `diameter = 2 * r`; `circumference = 2 * pi * r` atau `pi * d`; `area = pi * r^2`.

| Karakteristik | Integer | Float |
| --- | --- | --- |
| **Definisi** | Bilangan bulat (tanpa koma). | Bilangan desimal/pecahan. |
| **Contoh Hasil** | 10, 15, 100. | 31.4, 78.5. |
| **Penggunaan** | Perhitungan jumlah barang, indeks. | Perhitungan sains, koordinat, luas lingkaran. |

> [!warning] Audio Insight — Steve Salah Mengasumsikan Hasil Perhitungan Lingkaran Selalu Integer
> Terjadi poin pembelajaran penting saat Steve mengasumsikan bahwa semua hasil perhitungan lingkaran adalah **Integer** karena input radiusnya bulat. Namun, setelah script dijalankan (`python test.py`), _output_ menunjukkan angka desimal (seperti 31.4). Hal ini membuktikan bahwa keterlibatan angka desimal (seperti `math.pi`) dalam operasi perkalian secara otomatis mengubah tipe data menjadi **Float** — walaupun input awalnya (radius) adalah integer bulat.

**8.1.3 Mencari Sudut Ketiga Segitiga**

Logika: `Sudut_3 = 180 - (Sudut_1 + Sudut_2)` (total sudut internal segitiga selalu 180°).

```python
angle1 = 60
angle2 = 70
angle3 = 180 - (angle1 + angle2)

print(angle3)  # Output: 50
```

### 8.2 Studi Kasus Konversi Hari

Kasus ini menguji pemahaman mengenai bagaimana memecah satu nilai besar (total hari) menjadi satuan waktu yang lebih terstruktur (tahun, bulan, hari) menggunakan operator aritmetika Python.

**8.2.1 Metode Perhitungan: Aritmetika Manual vs Operator Spesifik**

| Fitur | Metode Aritmetika Manual (Reza) | Metode Operator Ringkas (Anwar) |
| --- | --- | --- |
| **Operator Utama** | Pembagian tradisional (`/`) dan pengurangan. | _Floor Division_ (`//`) dan _Modulo_ (`%`). |
| **Efisiensi** | Membutuhkan lebih banyak langkah variabel sementara. | Jauh lebih ringkas dan langsung ke sisa bagi. |
| **Logika Tahun** | `hari / 365` (kemudian dibulatkan). | `hari // 365`. |
| **Logika Sisa Hari** | Pengurangan manual dari total. | `hari % 365`. |

**8.2.2 Implementasi Logika Floor Division dan Modulo** — pendekatan Anwar dianggap lebih efisien karena menggunakan operator yang memang didesain untuk pembagian bilangan bulat.

```python
total_days = 400

years = total_days // 365
remaining_days = total_days % 365
months = remaining_days // 30
days = remaining_days % 30

print(years, "Tahun", months, "Bulan", days, "Hari")
# Output: 1 Tahun 1 Bulan 5 Hari
```

> [!warning] Audio Insight — Modulo adalah Kunci Menghindari Kehilangan Sisa Hari
> Diskusi kelas mengidentifikasi bahwa konversi hari adalah salah satu latihan dengan tingkat kesulitan tertinggi bagi pemula. Pemahaman tentang sisa bagi (_modulo_) menjadi kunci agar sisa hari tidak hilang dalam perhitungan saat berpindah dari satuan tahun ke bulan.

### 8.3 Pengenalan Dasar Navigasi Terminal & IDE

Kemampuan menjalankan script Python memerlukan pemahaman navigasi direktori dalam sistem operasi melalui terminal atau _command prompt_.

**8.3.1 Perintah Navigasi Dasar**

- **`cd`** (_Change Directory_): masuk ke folder tertentu. Jika nama folder memiliki spasi (contoh: `Python Project`), gunakan bantuan _auto-complete_.
- **`ls`** (_List_): melihat daftar berkas dan folder di direktori aktif saat ini.
- **Tab Completion:** menekan tombol **Tab** saat mengetik nama direktori akan melengkapi nama folder secara otomatis untuk menghindari kesalahan tipografi.

**8.3.2 Eksekusi Script Python** — pastikan terminal berada di direktori yang sama dengan berkas Python.

- **Perintah eksekusi:** `python nama_file.py`
- **Penanganan Error Direktori:** jika terminal menunjukkan `C:\Users\Username` sementara file berada di `Desktop`, perintah `python` akan gagal kecuali melakukan `cd Desktop` terlebih dahulu.

**8.3.3 Penggunaan Komentar (Comment)** — digunakan untuk memberikan penjelasan pada kode atau menonaktifkan baris kode tertentu agar tidak dieksekusi.

- **Simbol:** tanda pagar `#`.
- **Pintasan Keyboard (VS Code):** Windows `Ctrl + /`, Mac `Cmd + /`.

```python
# Ini adalah komentar, baris ini tidak dieksekusi Python
print("Baris ini yang dieksekusi")  # komentar juga bisa di akhir baris
```

> [!tip] Audio Insight — Studi Kasus Navigasi Direktori Steve
> Dalam sesi praktik, Steve mengalami kendala saat mencoba menjalankan `python test.py` karena posisi terminalnya masih berada di direktori pengguna (`C:\Users\Steve`), sementara file tersebut tersimpan jauh di dalam sub-folder `OneDrive\Desktop\Python Project`. Penggunaan `cd` secara bertahap dan bantuan tombol **Tab** terbukti mempercepat proses navigasi menuju direktori yang tepat.

---

## Ringkasan Sesi

Sesi 1 membangun fondasi mengenai: (1) apa itu AI dan mengapa Applied AI Engineering relevan, (2) cara berpikir algoritmik lewat flowchart dan studi kasus Tower of Hanoi (rekursi), (3) instalasi lingkungan kerja Python + Git, (4) sintaks dasar Python (variabel, tipe data, string, f-string, operator), dan (5) pseudocode sebagai jembatan berpikir sebelum menulis kode. Materi ini menjadi fondasi langsung bagi [[Sesi 02 - Intro to Git and GitHub (JCAIEH M1)|Sesi 02 - Intro to Git and GitHub]] (Git mendalam), [[Sesi 03 - Conditional and Loop Statement (JCAIEH M1)|Sesi 03 - Conditional and Loop Statement]] (if-else & loop), dan [[Sesi 04 - Data Types Collection Notes (JCAIEH M1)|Sesi 04 - Data Types Collection Notes]] (list/tuple/set/dict mendalam).

---

## 🔗 Terkait

- [[Sesi 02 - Intro to Git and GitHub (JCAIEH M1)|Sesi 02 - Intro to Git and GitHub]] — Sesi 1 memperkenalkan Git/GitHub sekilas di Bab 4.3, lalu Sesi 2 membahasnya secara mendalam (empat istilah kunci, alur commit, branching).
- [[Sesi 03 - Conditional and Loop Statement (JCAIEH M1)|Sesi 03 - Conditional and Loop Statement]] — rekursi Tower of Hanoi (Bab 3) di sini menjadi pembanding langsung untuk perbedaan Recursion vs Looping yang dibahas di Sesi 3 Bab 5.
- [[Sesi 04 - Data Types Collection Notes (JCAIEH M1)|Sesi 04 - Data Types Collection Notes]] — pengenalan singkat List/Tuple/Set/Dict di Bab 5.4 di sini dibahas jauh lebih mendalam (metode, mutability, indexing/slicing) di Sesi 4.
