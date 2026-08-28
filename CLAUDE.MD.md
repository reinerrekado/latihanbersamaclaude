# Purwadhika JCAI Engineering — Consolidated Study Notes

_Digabung dari seluruh notes Obsidian (13 sesi + High Level Study). Semua konten asli dipertahankan tanpa pengurangan, hanya disusun ulang urutannya._


---

## Table of Contents

- [High Level Study](#high-level-study)
- [Module 1 Session 1 Introduction to DS, Python, Statistics, SQL, Git & Github](#module-1-session-1-introduction-to-ds-python-statistics-sql-git--github)
- [Module 1 Session 2 Intro to GIt & Github](#module-1-session-2-intro-to-git--github)
- [Module 1 Session 3 Conditional & Loop Statement](#module-1-session-3-conditional--loop-statement)
- [Module 1 Session 4 Data Types Collection Notes](#module-1-session-4-data-types-collection-notes)
- [Module 1 Session 5 Python Function & File Handling](#module-1-session-5-python-function--file-handling)
- [Module 1 Session 6 Hackerrank Exercise](#module-1-session-6-hackerrank-exercise)
- [Module 1 Session 7 Object Oriented Programming](#module-1-session-7-object-oriented-programming)
- [Module 1 Session 8 Phyton & Modular Programming](#module-1-session-8-phyton--modular-programming)
- [Module 1 Session 9 Intro to Dabase & SQL](#module-1-session-9-intro-to-dabase--sql)
- [Module 1 Session 10 SQL Working With Multiple Tables](#module-1-session-10-sql-working-with-multiple-tables)
- [Module 1 Session 11 Statistics Fundamental](#module-1-session-11-statistics-fundamental)
- [Module 1 Session 12 Python Data Manipulation With Pandas and Numpy](#module-1-session-12-python-data-manipulation-with-pandas-and-numpy)
- [Module 1 Session 13 Data Visualization](#module-1-session-13-data-visualization)


---


# High Level Study


## Top Down Learning of Programming


**1. Pemrograman 
* [[Bab 2 Dasar Pengembangan Perangkat Lunak & Algoritma#1. Definisi Pemrograman dan Bahasa Pemrograman|Definisi Pemrograman]] adalah seni dan sains untuk memberikan instruksi kepada komputer agar menjalankan tugas tertentu. 
**2.  Algorithm
* [[Bab 2 Dasar Pengembangan Perangkat Lunak & Algoritma#2. Konsep dan Esensi Algoritma|Definisi Algoritma]] adalah serangkaian instruksi langkah demi langkah unutuk memecahkan masalah atau melakukan tugas tertentu. 
**3. Logic
* Komponen paling mikro yang membangun dari algoritma. Ini adalah aturan main, alur pengambil keputusan atau perulangan.
* Salah satu jenis yang sudah dipelajari adalah  logika [[Bab 3 Studi Kasus Logika Lanjutan - Tower of Hanoi#Langkah Rekursif Utama (Recursive Case)|rekulsif]]. Yakni sebuah fungsi untuk memanggil sebagai fungsi yang baru samapi bertemu titik henti (base case). 
**4.  Programming Language
* Definisi bahasa pemrograman adalah bahasa yang digunakan untuk berkomunikasi dan memberi instruksi kepada komputer. 
* [[Bab 4 Pengenalan Python & Lingkungan Kerja#Konsep Tingkatan Bahasa Pemrograman (Level)|Python]] adalah jenis bahasa pemrograman tingkat tinggi yang mendekati bahsa manusia. Sehingga gampang dibaca, dipejajrai dan dipahami oleh programmer.  
**5. Syntax
* Adalah tata bahasa atau aturan penulisan baku dalam pemrograman. Seperti grammar. 
* Elemen didalamnya ada keywords (if, for, return, print), tanda baca atau symbol khusus (krung kurawal, titik dua, tanda kutip), sensitifitas huruf (huruf besar/kecil merujuk hal berbeda) dan indentasi (spasi/tab).
**6. Variable 
* [[Bab 5 Konsep Dasar Pemrograman Python#1. Konsep Variabel & Struktur Penyimpanan Memori|Definisi Variable]] adalah elemen fundamental yang berfungsi sebagai wadah menimpan data.  Anggaplah variable adalah sebuah box dengan label. Labelnya adalah nama variabel, isi boxnya adalah data dan nilai yang disimpan. 
**7. Assignment Operator
* Adalah sebuah operator penugasan untuk menghubungkan label variable dengan nilai.
* Contoh: Age (label variable) = 20 (nilai).
**8. Basic Data Types
* Dalam python, setiap nilai memiliki [[Bab 5 Konsep Dasar Pemrograman Python#3. Deep Dive Tipe Data Dasar (Basic Data Types)|tipe data]] tertentu untuk menyatakan operasi apa yang bisa dikerjakannya. Contohnya integer, float, [[Bab 2 Review Boolean, Comparison, & Logical Operators|boolean]], string dan nonetypes. 
**9. Collection Data Types
* Adalah wadah [[Bab 5 Konsep Dasar Pemrograman Python#4. Tipe Data Koleksi (Collection Data Types|wadah khusus]] untuk menyimpan dan mengorganisasikan data. Jenisnya ada:
* Jenis didalamnya ada:
	* Dictionary: menampung key dan pasangan value {key : value} untuk pencarian data dengan keyword tertentu. 
	* Set: koleksi data unik yang tidak berurutan, jika ada data ganda python akan menghapus salah satunya. Dideklarasikan dengan {}
	* Tupple: Koleksi data berurutan yang sifatnya immutable (tidak bisaa dimodifikasi sejak bibuat). Dideklarasikan dengan ()
	* Set: Koleksi data berurutan yang sfatnya mutable atau bisa dimodifikasi, dihapus dan ditambah setelah dibuat. Dideklarasikan dengan [].
	











---


# Module 1 Session 1 Introduction to DS, Python, Statistics, SQL, Git & Github


## Bab 1 Pengenalan Artificial Intelligence (AI) & Applied AI Engineering

---
tags:
  - Ai
---
Panduan belajar ini disusun secara mendalam dan komprehensif untuk memberikan pemahaman menyeluruh mengenai fondasi **Artificial Intelligence (AI)** dan peran strategis seorang **AI Engineer** di industri modern. Seluruh materi didasarkan pada sumber rujukan teknis dan penjelasan instruksional yang tersedia.


---

## 1. DEFINISI & KONSEPTUAL DASAR ARTIFICIAL INTELLIGENCE (AI)

**Artificial Intelligence (AI)** secara formal didefinisikan sebagai bidang dalam **Ilmu Komputer (Computer Science)** yang berfokus pada penciptaan sistem yang mampu melakukan tugas-tugas yang biasanya membutuhkan kecerdasan manusia.

### Posisi AI dalam Ranah Ilmu Komputer

Dalam ekosistem _Computer Science_, AI menempati posisi yang setara dengan cabang ilmu lainnya seperti _web development_, _UI/UX design_, dan _cyber security_. Secara akademis, AI telah mengalami transisi signifikan; yang awalnya hanya merupakan sub-bidang atau konsentrasi di bawah Teknik Informatika, kini telah berkembang pesat menjadi jurusan mandiri di berbagai institusi pendidikan.

### Kemampuan Utama yang Ditiru dari Manusia

Sistem AI dirancang untuk mereplikasi beberapa kemampuan kognitif utama manusia, antara lain:

- **Learning from data:** Kemampuan untuk belajar dari informasi yang ada.
- **Recognizing patterns:** Mengidentifikasi pola-pola tertentu dalam kumpulan data yang besar.
- **Understanding language:** Memahami bahasa manusia baik dalam bentuk teks maupun suara.
- **Making predictions or decisions:** Memberikan prediksi atau mengambil keputusan berdasarkan input.
- **Solving problems automatically:** Menyelesaikan masalah secara mandiri tanpa instruksi manual yang kaku.

### Perbandingan Mendalam: AI vs. Software Tradisional

Perbedaan mendasar antara perangkat lunak tradisional dengan sistem AI terletak pada bagaimana instruksi diberikan kepada komputer:

| Fitur                | Software Tradisional                                                 | Artificial Intelligence (AI)                                         |
| -------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Metode Kerja**     | Mengotomatisasi aturan (_rules_) yang sudah diketahui dan eksplisit. | Belajar dari pola data untuk masalah dengan aturan abstrak.          |
| **Penulisan Aturan** | Ditulis secara manual oleh programmer.                               | Sistem merumuskan aturan sendiri melalui proses pembelajaran.        |
| **Fleksibilitas**    | Kaku, hanya bekerja sesuai instruksi tertulis.                       | Adaptif, mampu menangani input yang belum pernah dilihat sebelumnya. |
|                      |                                                                      |                                                                      |

**Contoh Kasus: Membedakan Gambar Anjing dan Kucing** Dalam software tradisional, menulis aturan untuk membedakan hewan sangat sulit (misal: menentukan nilai piksel tertentu, bentuk telinga, atau hidung secara manual). Dalam AI, kita menggunakan konsep **Supervised Machine Learning**. Proses ini dianalogikan seperti mendidik seorang anak kecil; kita memberikan banyak contoh gambar yang sudah diberi label ("Ini anjing", "Ini kucing"), sehingga sistem belajar mengenali ciri khas masing-masing secara otomatis.

---

## 2. URGENSI & MOTIVASI MEMPELAJARI AI (WHY LEARN AI?)

Memahami AI bukan lagi sekadar pilihan, melainkan kebutuhan mendesak karena transformasi masif yang dibawanya ke berbagai sektor.

### Pertumbuhan Karier (_Career Growth_)

Terdapat permintaan industri yang sangat tinggi di lintas sektor. Peran AI kini esensial di bidang:

- **Healthcare:** Contohnya dalam mendeteksi penyakit melalui analisis gambar X-ray dengan tingkat akurasi tinggi.
- **Finance:** Membantu melakukan analisis prediksi pasar dan manajemen risiko.

### Produktivitas & Otomasi (_Productivity & Automation_)

Otomasi konvensional memerlukan aturan yang sangat kaku. Sebaliknya, otomasi berbasis AI mampu menangani tugas-tugas yang lebih dinamis.

- **Contoh Kasus Customer Service (CS):** Dalam kategorisasi komplain, seorang manusia mungkin hanya mampu memproses sekitar 3 komplain per menit. Sistem AI dapat memproses **1.000 hingga 10.000 komplain secara paralel dalam hitungan detik**, menangani beban kerja besar tanpa kelelahan.

### Pengambilan Keputusan yang Lebih Cerdas (_Smarter Decision Making_)

AI membantu meminimalkan (meskipun tidak menghilangkan sepenuhnya) bias yang sering muncul akibat perbedaan persepsi manusia. Sistem AI mampu menyajikan wawasan (_insight_) berbasis data sebelum keputusan penting diambil.

### Keterampilan Siap Masa Depan (_Future-Ready Skills_)

Di era yang terus bertumbuh pesat, mempersiapkan keahlian AI adalah langkah strategis untuk tetap relevan dalam pasar kerja global.

### Analogi Listrik dari Andrew Ng

**Andrew Ng**, seorang profesor ternama dari Stanford yang menjadi inspirasi bagi banyak pengajar AI, memberikan kutipan terkenal: _"AI adalah listrik baru"_. Sama seperti listrik yang mentransformasi hampir setiap industri 100 tahun yang lalu, AI saat ini sedang melakukan transformasi masif yang serupa di segala lini kehidupan manusia.

---

## 3. SIKLUS HIDUP MODEL AI YANG DISEDERHANAKAN (AI MODEL LIFECYCLE)

Pengembangan model AI mengikuti alur kerja yang terstruktur dan berulang (iteratif):

1. **Problem Understanding:** Tahap awal untuk mendefinisikan tujuan (_goal_) dan kriteria sukses. Sangat penting untuk menganalisis apakah masalah tersebut memang membutuhkan solusi AI atau bisa diselesaikan dengan metode konvensional.
2. **Data Preparation:** Meliputi pengumpulan data (_collection_) dan pembersihan data (_clean the data_). Kualitas output AI sangat bergantung pada kualitas data ini.
3. **Training:** Proses mengajarkan model menggunakan data yang telah dipersiapkan agar model dapat mengenali pola.
4. **Evaluation:** Menguji performa model. Jika hasilnya kurang memuaskan, engineer dapat kembali ke tahap _Training_ atau bahkan ke _Data Preparation_ jika ditemukan bahwa datanya "kotor".
5. **Deployment:** Menyajikan model ke lingkungan produksi sehingga dapat diakses dan digunakan oleh pengguna nyata.
6. **Monitoring:** Melacak performa model secara kontinu. Karena lingkungan (_environment_) nyata sering berganti, model yang awalnya bagus bisa mengalami penurunan performa.

**Contoh Kasus: FYP TikTok** Model yang dilatih pada 5 Agustus untuk menyarankan konten FYP TikTok mungkin tidak lagi relevan pada bulan September. Hal ini disebabkan oleh pergeseran tren konten (_content shift_). Oleh karena itu, monitoring metrik performa sangat krusial untuk memutuskan kapan model perlu dilatih ulang.

---

## 4. MITOS-MITOS UMUM TENTANG AI ENGINEER (DEBUNKED)

Banyak hambatan psikologis yang menghalangi orang untuk mempelajari AI karena persepsi yang salah:

- **Mitos 1: "Harus Jenius Matematika"**
    - **Faktanya:** Anda hanya membutuhkan logika dasar dan statistik dasar. Kalkulus yang mendalam (_fancy calculus_) biasanya hanya dibutuhkan oleh **AI Researcher** yang bertugas merumuskan rumus-rumus baru untuk model AI, bukan pengguna terapan.
- **Mitos 2: "Membutuhkan Compute Power / Perangkat High-End"**
    - **Faktanya:** Saat ini kita jarang melatih model raksasa dari nol. Kita bisa menggunakan **pre-trained model** atau memanggil **API** dari model yang sudah dideploy oleh penyedia layanan besar.
- **Mitos 3: "AI Diciptakan untuk Menggantikan Kita"**
    - **Faktanya:** AI adalah alat bantu (_tool_). Yang akan menggantikan manusia bukanlah AI itu sendiri, melainkan orang lain yang mahir memanfaatkan AI untuk bekerja lebih efisien.

---

## 5. KEMAMPUAN UTAMA AI DALAM APLIKASI MODERN (CORE AI CAPABILITIES)

### Natural Language Processing (NLP)

Kemampuan komputer untuk memahami, menafsirkan, dan menghasilkan bahasa manusia.

- **Contoh:** ChatGPT, terjemahan mesin, analisis sentimen, perangkuman teks (_text summarization_), dan chatbot.
- **Evolusi:** Dahulu (5-7 tahun lalu), satu model hanya bisa melakukan satu tugas (misal: khusus untuk sentimen saja). Sekarang, dengan **Generative AI**, satu model tunggal (seperti ChatGPT) memiliki keterampilan gabungan: merangkum, menerjemahkan, dan menganalisis secara simultan.

### Computer Vision (CV)

Kemampuan komputer untuk memahami dan menganalisis input visual berupa gambar dan video.

- **Contoh:** _Face recognition_, _object detection_, klasifikasi gambar, OCR (_Optical Character Recognition_), dan kendaraan otonom.
- **Kasus Autonomous Vehicles:** Sensor kamera menerima gambar lingkungan, mendeteksi objek (mobil lain, lampu merah, pejalan kaki), dan membantu sistem mengambil keputusan (seperti berhenti atau menunggu).

### Compound AI Solutions & Agentic AI

Solusi AI modern saat ini bersifat **gabungan (compound)**. Kendaraan otonom, misalnya, menggabungkan CV untuk navigasi dan NLP untuk asisten suara. **Agentic AI** melangkah lebih jauh dengan mengintegrasikan NLP, CV, penalaran (_reasoning_), dan penggunaan peralatan eksternal (_external tools_) untuk membangun sistem cerdas yang mendekati kapabilitas kecerdasan manusia.

---

## 6. FOKUS PEMBELAJARAN: APPLIED AI ENGINEERING

### Mengapa Memilih Applied AI Engineering?

Produk AI masa depan tidak hanya berdiri sendiri. Industri memerlukan engineer yang memahami **full pipeline**—mulai dari pembuatan model hingga penyajiannya (_delivery_) kepada pengguna akhir. Keterampilan ini sangat praktis, ramah bagi pemula, dan sangat dicari oleh pasar kerja saat ini.

### Kurikulum Applied AI Engineering mencakup:

1. **Programming Fundamental:** Dasar-dasar logika menggunakan bahasa **Python**.
2. **ML Fundamental:** Alur kerja dasar Machine Learning.
3. **NLP/LLM:** Pemahaman bahasa manusia oleh mesin.
4. **Computer Vision:** Bagaimana mesin "melihat".
5. **Deployment:** Cara menyajikan model AI agar bermanfaat bagi pengguna nyata.

### Analogi Chef untuk Konsep AI

Untuk memudahkan pemahaman, konsep pengembangan AI dapat dianalogikan dengan dunia kuliner:

|Komponen AI|Analogi Chef|Penjelasan|
|---|---|---|
|**AI**|**Chef Terlatih**|Seseorang yang telah mencicipi dan mempelajari ribuan hidangan.|
|**Data**|**Masakan/Hidangan**|Bahan pembelajaran yang dicicipi oleh Chef.|
|**Model**|**Keahlian & Penilaian**|Skill yang terbentuk dari proses mencicipi tersebut untuk membuat hidangan baru yang luar biasa.|

### **Tiga Pilar Utama Applied AI Engineer:**

1. **NLP/LLM (Language):** Kemampuan mesin untuk membaca dan menulis.
2. **Computer Vision (Sight):** Kemampuan mesin untuk melihat dan mengenali.
3. **Deployment (Delivery):** Kemampuan mesin untuk menyajikan layanan kepada pengguna nyata.



## Bab 2 Dasar Pengembangan Perangkat Lunak & Algoritma

---
tags:
  - algorithm
  - programming
  - flowchart
  - plain_language
aliases:
  - Dasar-Dasar Pemrograman
---
Panduan belajar ini menyajikan analisis mendalam mengenai fondasi pengembangan perangkat lunak, dengan fokus utama pada logika algoritma sebagai tulang punggung pemrograman modern. Materi ini mengintegrasikan konsep teoritis dari modul fundamental dengan wawasan praktis dari diskusi instruksional.

---
## 1. Definisi Pemrograman dan Bahasa Pemrograman

Pemrograman pada dasarnya adalah seni dan sains untuk memberikan instruksi kepada komputer agar menjalankan tugas tertentu. Tanpa instruksi ini, perangkat keras komputer tidak memiliki kemampuan untuk melakukan operasi apa pun.

- **Pemrograman (Programming):** Proses menciptakan serangkaian instruksi terperinci yang memberitahu komputer cara melakukan tugas tertentu secara efisien.
- **Bahasa Pemrograman (Programming Language):** Merupakan kosakata dan serangkaian aturan tata bahasa (sintaksis) yang digunakan untuk memberikan instruksi tersebut. Bahasa ini bertindak sebagai jembatan komunikasi antara logika manusia dan eksekusi mesin.


**Contoh Bahasa Pemrograman Populer:**

- JavaScript
    
- Java
    
- Golang
    
- PHP
    
- Keluarga Bahasa C: C, C++, dan C#
    

### Hubungan Pemrograman dengan Algoritma

Untuk melakukan pemrograman dengan baik, seorang pengembang tidak bisa langsung menulis kode secara acak. Dibutuhkan rencana langkah-demi-langkah yang jelas sebelum implementasi teknis dimulai. Rencana sistematis inilah yang disebut sebagai **Algoritma**.

## 2. Konsep dan Esensi Algoritma

Secara formal, algoritma didefinisikan sebagai serangkaian instruksi langkah-demi-langkah untuk memecahkan masalah atau menyelesaikan tugas tertentu. ^400a3e

### Analogi Dunia Nyata: Pembuatan Kopi Hitam

Algoritma sering kali dianalogikan dengan resep masakan atau prosedur harian. Contoh klasiknya adalah prosedur membuat secangkir kopi hitam:

1. Rebus air hingga mendidih.
    
2. Masukkan kopi ke dalam cangkir.
    
3. Tuangkan air panas ke dalam cangkir.
    
4. Tambahkan gula atau susu sesuai selera.
    
5. Aduk dan sajikan.
    

> **Wawasan Interaktif (Audio Insight):**
> 
> Dalam konteks pemesanan atau instruksi, detail sangat menentukan hasil. Jika seseorang memesan _"kopi hitam jangan kemanisan"_, algoritma harus memiliki parameter yang jelas mengenai takaran gula agar hasil akhir sesuai dengan ekspektasi pengguna.

### 4 Karakteristik Utama Algoritma

Sebuah algoritma yang efektif harus memenuhi standar berikut:

|**Karakteristik**|**Penjelasan**|
|---|---|
|**Clear & Unambiguous**|Setiap langkah harus jelas dan tidak bermakna ganda.|
|**Step-by-step**|Instruksi harus dijalankan secara berurutan.|
|**Definite Start and End**|Algoritma harus memiliki titik awal yang jelas dan pada akhirnya harus berhenti setelah mencapai solusi.|
|**Effective**|Harus mampu memecahkan masalah dengan benar dan tepat sasaran.|

### Urgensi Algoritma

Penggunaan algoritma yang tepat sangat krusial karena:

- **Menghemat Waktu:** Menghindari _trial-and-error_ yang tidak perlu.
    
- **Optimalisasi Sumber Daya:** Menggunakan memori dan daya komputasi secara efisien.
    
- **Akurasi:** Memastikan hasil yang konsisten setiap kali dijalankan.
    

## 3. Studi Kasus Algoritma di Dunia Nyata

Algoritma bukan sekadar konsep akademik, melainkan mesin penggerak teknologi yang digunakan sehari-hari:

- **Optimalisasi Rute (Google Maps):** Menggunakan algoritma kompleks untuk menganalisis berbagai data lalu lintas dan kondisi jalan secara _real-time_ guna menentukan rute tercepat dari titik A ke titik B.
    
- **Rekomendasi Belanja Online:** Platform _e-commerce_ menggunakan algoritma untuk menyaring jutaan pilihan barang dan menampilkan produk yang paling relevan dengan minat pengguna berdasarkan data perilaku sebelumnya.
    

## 4. Representasi Algoritma

Ada dua cara umum yang digunakan untuk memodelkan algoritma sebelum diubah menjadi kode program:

### A. Plain Language (Step List)

Menggunakan bahasa manusia sehari-hari untuk mendeskripsikan langkah.

**Contoh Kasus:** Mencari angka terbesar dari tiga angka (7, -2, 11).

1. Bandingkan angka pertama (7) dengan angka kedua (-2).
    
2. Ambil angka yang lebih besar (7).
    
3. Bandingkan angka tersebut (7) dengan angka ketiga (11).
    
4. Angka terbesar yang ditemukan adalah hasilnya (11).
    

### B. Flowchart

Visualisasi proses menggunakan diagram dengan simbol-simbol standar untuk menunjukkan alur kerja. Flowchart sangat berguna untuk memvisualisasikan proses yang memiliki banyak percabangan atau logika kompleks.

## 5. Simbol Flowchart Standar dan Implementasinya

Setiap bentuk dalam flowchart memiliki makna teknis yang spesifik:

|**Simbol**|**Nama**|**Makna**|
|---|---|---|
|**Oval**|Terminator|Menandai titik awal (Start) atau akhir (End) dari sebuah sistem.|
|**Persegi Panjang**|Process|Menunjukkan operasi tertentu atau perhitungan internal.|
|**Kertas Robek**|Document|Merepresentasikan output berupa dokumen atau laporan fisik/cetakan.|
|**Belah Ketupat**|Decision|Titik percabangan logika; biasanya menghasilkan jalur "Ya" atau "Tidak".|
|**Jajar Genjang**|Data|Menunjukkan proses input data masuk atau output data keluar dari sistem.|

### Detail Kasus Implementasi Flowchart

**1. Penjumlahan Dua Angka (529 + 256)**

1. Start (Terminator)
    
2. Read A (Data: 529)
    
3. Read B (Data: 256)
    
4. Calculate Sum as A + B (Process: 529 + 256)
    
5. Print Sum (Process/Data: 785)
    
6. End (Terminator)
    

**2. Penentuan Profit atau Loss**

1. Start
    
2. Read Income (Contoh: 1.000)
    
3. Read Cost (Contoh: 800)
    
4. Decision (Income >= Cost?):
    
    - Jika **Yes**: Hitung Profit = Income - Cost ➔ Print Profit (200).
        
    - Jika **No**: Hitung Loss = Cost - Income ➔ Print Loss.
        
5. End
    

## 6. Wawasan Diskusi (Audio Insights)

Bagian ini merangkum pemikiran mendalam dari perspektif _engineering_ dalam memandang algoritma dan pemrograman:

### Algoritma sebagai Logika Proses Bisnis

Dalam dunia _engineering_, algoritma dipandang sebagai pengejawantahan dari _business process logic_. Penting bagi seorang pengembang untuk melatih "flow berpikir" di dalam kepala. Menggambar flowchart memang membantu, namun kemampuan untuk menelusuri logika secara mental adalah keterampilan esensial.

### Prinsip Eksekusi Python

Meskipun diagram flowchart bisa terlihat bercabang atau tampak paralel, Python sebagai bahasa yang diinterpretasikan mengeksekusi instruksi secara serial/sekuensial. Kode dijalankan baris demi baris (_line-by-line_) dari atas ke bawah. Cabang logika hanyalah pengalihan urutan eksekusi, bukan eksekusi bersamaan dalam satu waktu.

### Kompleksitas dan "Edge Cases"

Dunia nyata jauh lebih rumit daripada sekadar alur sukses. Algoritma harus menangani _Edge Cases_ atau kondisi ekstrem, seperti:

- Pemesanan makanan saat saldo pelanggan tidak cukup.
    
- Pemesanan barang saat stok tiba-tiba habis tepat sebelum pembayaran.
    

### Pemrograman Tradisional vs. AI

Perbedaan mendasar dalam menangani aturan (_rules_) yang kompleks:

- **Traditional Programming:** Memerlukan pendefinisian jutaan aturan secara manual. Contoh: Instruksi robot menyeberang jalan harus mencakup kondisi lampu hijau, keberadaan ambulans, atau kegagalan sensor. Ini sulit dilakukan secara manual untuk skenario yang tak terbatas.
    
- **Artificial Intelligence (AI):** AI jauh lebih unggul karena ia belajar dari data berpasangan (_input-output_), bukan menghafal aturan manual. Dalam penentuan pakaian berdasarkan cuaca (misal: hujan tapi panas, atau mendidih tapi berangin), AI mempelajari pola dari data historis untuk memberikan keputusan yang lebih adaptif.
    

### Abstraksi Perintah "Read"

Dalam representasi algoritma, instruksi "Read" adalah sebuah abstraksi. Dalam praktik teknis, pembacaan data ini bisa berupa:

- Input manual dari _keyboard_ oleh pengguna.
    
- Pembacaan data dari sebuah file di penyimpanan.
    
- Pengambilan data secara berkala dari sensor fisik (misal: sensor suhu atau kelembapan).



## Bab 3 Studi Kasus Logika Lanjutan - Tower of Hanoi


Dokumen ini merupakan panduan belajar komprehensif yang menyintesis materi mengenai _Tower of Hanoi_, sebuah studi kasus krusial dalam pemahaman logika rekursif tingkat lanjut bagi seorang _AI Engineer_. Materi ini mencakup teori dasar, aturan main, hingga abstraksi logika yang menjadi landasan penyelesaian masalah kompleks.

---

## 1. PENGENALAN TOWER OF HANOI & ATURAN MAIN (RULES)

_Tower of Hanoi_ diakui sebagai masalah klasik dalam bidang matematika dan ilmu komputer yang sering digunakan untuk menguji kemampuan pemecahan masalah secara logis. Secara struktural, masalah ini melibatkan tiga komponen utama dan aturan pemindahan yang sangat ketat.

### Komponen Utama

Permainan ini melibatkan _N_ buah piringan (_disks_) dengan ukuran yang berbeda-beda dan 3 tiang (_pegs/rods_) yang memiliki peran spesifik:

- **Source (Asal):** Tiang tempat piringan pertama kali ditumpuk.
    
- **Target (Tujuan):** Tiang tujuan akhir di mana semua piringan harus dipindahkan.
    
- **Auxiliary (Pembantu/Helper):** Tiang perantara yang digunakan untuk membantu proses pemindahan.
    

Piringan-piringan tersebut awalnya ditumpuk di tiang _Source_ dengan urutan _decreasing size_ (ukuran piringan terbesar berada di dasar dan piringan terkecil berada di puncak).

### Tiga Aturan Mutlak (Rules of Tower of Hanoi)

Dalam memindahkan seluruh tumpukan dari _Source_ ke _Target_, terdapat tiga aturan yang tidak boleh dilanggar:

1. Hanya **satu piringan** yang boleh dipindahkan dalam satu waktu.
    
2. Hanya **piringan teratas** pada suatu tiang yang boleh diambil dan dipindahkan ke tiang lain.
    
3. Piringan yang **lebih besar tidak boleh** diletakkan di atas piringan yang lebih kecil.
    

### Analogi Kehidupan Nyata

Secara filosofis dan praktis, _Tower of Hanoi_ bukan sekadar teori komputer. Dalam metode pendidikan Montessori, alat ini sering digunakan sebagai mainan edukasi untuk balita (_toddler_). Tujuannya adalah untuk melatih kemampuan motorik halus serta melatih cara berpikir analitis sejak dini melalui pemahaman pola dan batasan aturan.

## 2. PENDEKATAN MANUAL VS PENDEKATAN REKURSIF (RECURSIVE LOGIC)

Memahami perbedaan antara solusi manual dan rekursif adalah kunci untuk menguasai algoritma ini.

### Keterbatasan Solusi Manual

Pendekatan manual sering kali dilakukan dengan mendefinisikan langkah demi langkah secara kaku (misalnya: "pindahkan disk 1 ke C, disk 2 ke B"). Pendekatan ini memiliki kelemahan fatal:

- **Tidak Scalable:** Langkah-langkah manual yang berhasil untuk 3 piringan (N=3) akan langsung gagal atau menjadi terlalu rumit untuk diikuti manusia saat jumlah piringan bertambah menjadi 4 atau lebih.
    
- **Kekakuan Logika:** Solusi manual tidak memiliki pola umum yang dapat diadaptasi untuk variabel yang berubah.
    

### Keunggulan Logika Rekursif (Recursive Logic)

Logika Rekursif menawarkan solusi yang jauh lebih elegan. Konsep dasarnya adalah fungsi yang memanggil dirinya sendiri di dalam tubuh fungsi tersebut untuk menyelesaikan parameter masalah yang lebih kecil. Dalam hal ini, masalah besar (N) dipecah menjadi masalah yang lebih kecil (N−1).

### Struktur Fungsi Rekursif Hanoi

Fungsi utama biasanya didefinisikan sebagai `Hanoi(N, Source, Target, Helper)`. Keajaiban dari logika ini terletak pada _Role Shifting_ (Pertukaran Peran) tiang secara dinamis:

- Pada satu langkah, tiang B bertindak sebagai _Helper_.
    
- Pada langkah berikutnya, tiang B bisa bertukar peran menjadi _Target_ sementara untuk memindahkan sub-masalah piringan yang lebih kecil.
    

## 3. PEMBEDAHAN LANGKAH-DEMI-LANGKAH (STEP-BY-STEP TRACE)

Logika rekursif _Tower of Hanoi_ bekerja berdasarkan dua kondisi utama: _Base Case_ dan _Recursive Case_.

### Kondisi Dasar (Base Case)

Terjadi ketika **N = 1**. Ini adalah kondisi paling sederhana di mana kita hanya perlu memindahkan satu piringan tunggal langsung dari tiang _Source_ ke tiang _Target_ tanpa memerlukan bantuan tiang lain.

### Langkah Rekursif Utama (Recursive Case)

Untuk setiap **N > 1**, algoritma mengikuti pola tiga langkah besar:

1. Pindahkan **N-1** piringan dari _Source_ ke _Helper_ (menggunakan _Target_ sebagai bantuan sementara).
    
2. Pindahkan piringan terbesar (piringan ke-N) langsung dari _Source_ ke _Target_.
    
3. Pindahkan **N-1** piringan yang tadi berada di _Helper_ ke _Target_ (menggunakan _Source_ sebagai bantuan sementara).
    

### Contoh Detail Berdasarkan Jumlah Piringan

|**Kasus**|**Deskripsi Logika**|**Total Langkah**|
|---|---|---|
|**N = 1**|`Hanoi(1, A, C, B)`: Langsung pindahkan disk dari A ke C.|1|
|**N = 2**|`Hanoi(2, A, C, B)`: Disk kecil (N-1) harus dipindah ke tiang pembantu (B) agar disk besar bebas berpindah ke tujuan (C). Kemudian pindahkan disk kecil dari B ke C.|3|
|**N = 3**|`Hanoi(3, A, C, B)`: Memanggil fungsi `Hanoi(2)` di dalamnya. Proses ini menghasilkan alur yang sangat optimal tanpa ada langkah yang terbuang.|7|
|**N = 4**|Mendemonstrasikan penumpukan 3 piringan di tiang pembantu (_Helper_) untuk membebaskan piringan keempat (terbesar) agar bisa mendarat di tiang tujuan.|15|

### Analisis Kasus Ekstrem (N = 1000)

Meskipun secara visual mustahil dilakukan secara manual, _Recursive Logic_ tetap bekerja sempurna. Algoritma akan tetap konsisten: memandang 999 piringan teratas sebagai satu kesatuan yang harus dipindahkan ke tiang _helper_ terlebih dahulu, menyisakan piringan ke-1000 (terbesar) di dasar untuk dipindahkan ke _target_, lalu mengembalikan 999 piringan di atasnya.

## 4. INSIGHT FILOSOFI ALGORITMA (AUDIO DISCUSSION INTEGRATION)

Berdasarkan diskusi mendalam mengenai perancangan algoritma, terdapat beberapa poin kunci yang harus dipahami oleh setiap pengembang:

- **Pentingnya Memulai dari "Solvable First":** Dalam merancang algoritma, langkah pertama bukan mencoba mengoptimalkannya secara langsung, melainkan mencari penyelesaian yang paling mudah dan sederhana terlebih dahulu. Setelah masalah tersebut terpecahkan (_solvable_), barulah efisiensi ditingkatkan.
    
- **Konsep Efisiensi Langkah (Optimal Moves):** _Tower of Hanoi_ memberikan pola matematika pasti untuk jumlah langkah minimum, yaitu **$2^N - 1$**. Algoritma rekursif secara otomatis mengikuti pola ini, memastikan tidak ada pemborosan tenaga atau memori komputer.
    
- **Logika N-1:** Diskusi interaktif menekankan bahwa penggunaan `N-1` pada parameter fungsi rekursif bukan sekadar pengurangan angka, melainkan strategi untuk mencapai _Base Case_ (kondisi N=1). Tanpa pengurangan parameter ini, fungsi akan memanggil dirinya sendiri selamanya (_infinite loop_).
    
- **Tujuan Utama Belajar Algoritma:** Belajar algoritma seperti _Tower of Hanoi_ bukan untuk menghafal sintaks bahasa pemrograman tertentu (seperti Python atau Java). Tujuan sejatinya adalah melatih "jam terbang" pola pikir terstruktur. Dengan menguasai logika ini, seorang _engineer_ dapat melakukan abstraksi masalah dunia nyata yang rumit menjadi logika komputer yang sistematis dan efisien.



## Bab 4 Pengenalan Python & Lingkungan Kerja

---
tags:
  - Phyton
---

Panduan belajar ini disusun secara sistematis untuk memberikan pemahaman mendalam mengenai fondasi bahasa pemrograman Python, perbedaan mekanisme eksekusi kode, persiapan alat kerja, hingga bedah sintaksis pertama. Seluruh materi didasarkan pada dokumentasi teknis dan wawasan instruksional yang tersedia dalam konteks sumber.

---

## 1. Pengenalan Python sebagai High-Level Language

Python didefinisikan sebagai bahasa pemrograman yang sangat fleksibel dan populer digunakan untuk berbagai domain teknologi modern, termasuk _Artificial Intelligence_ (AI), _web development_, _backend development_, _data analysis_, hingga otomasi tugas-tugas repetitif.

### Konsep Tingkatan Bahasa Pemrograman (Level)

Dalam dunia pemrograman, istilah 'level' merujuk pada seberapa dekat bahasa tersebut dengan bahasa manusia atau bahasa mesin:

- **High-Level Language (Python):** Python dikategorikan sebagai bahasa tingkat tinggi karena sintaksisnya dirancang mendekati bahasa alami manusia (Inggris). Hal ini membuat Python relatif mudah dipelajari, dibaca, dan dipahami oleh pemula maupun profesional.
    
- **Low-Level Language:** Sebaliknya, bahasa tingkat rendah seperti bahasa mesin (terdiri dari deretan angka 0 dan 1) sangat sulit dimengerti langsung oleh manusia. Bahasa ini berinteraksi secara langsung dengan perangkat keras tanpa abstraksi yang luas.
    

## 2. Deep Dive: Interpreted vs Compiled Programming Language

Terdapat perbedaan mendasar dalam cara komputer memproses instruksi dari bahasa pemrograman. Python menggunakan mekanisme interpretasi, yang berbeda dengan bahasa seperti C atau C++.

### Mekanisme Interpreted Language (Python)

Python bekerja menggunakan _Interpreter_. Cara kerjanya adalah mengeksekusi kode secara langsung baris-demi-baris (_line-by-line_) secara sekuensial dari atas ke bawah pada saat program dijalankan.

- **Kaitan dengan Flowchart:** Karena Python bekerja secara sekuensial, perancangan algoritma melalui flowchart harus dilakukan secara logis dan berurutan agar selaras dengan cara kerja _interpreter_ dalam membaca kode.
    

### Mekanisme Compiled Language (C/C++)

Bahasa yang terkompilasi membutuhkan langkah tambahan sebelum program dapat dijalankan. Seluruh kode program harus diterjemahkan sekaligus oleh _Compiler_ menjadi kode mesin mandiri (_standalone executable binary_).

### Analisis Trade-off (Perbandingan)

|**Karakteristik**|**Interpreted (Python)**|**Compiled (C/C++)**|
|---|---|---|
|**Proses Development**|Jauh lebih cepat (tulis dan langsung jalankan).|Lebih lambat karena butuh proses kompilasi ulang setiap perubahan.|
|**Debugging**|Lebih mudah; kesalahan terlacak tepat pada baris yang dieksekusi.|Lebih kompleks; kesalahan seringkali baru terdeteksi setelah proses kompilasi.|
|**Runtime Performance**|Relatif lebih lambat karena proses interpretasi terjadi saat aplikasi berjalan.|Sangat cepat karena kode sudah dalam bentuk biner mesin yang siap pakai.|

## 3. Setup Lingkungan Pengembangan (Development Environment)

Untuk mulai membangun aplikasi berbasis AI dan Python, diperlukan instalasi alat dan konfigurasi lingkungan yang tepat agar proses pengembangan berjalan efisien.

### Alat Utama dan Ekstensi

- **IDE / Code Editor:** Visual Studio Code (VSCode) digunakan sebagai editor teks utama untuk menulis kode.
    
- **Ekstensi VSCode Esensial:**
    
    - **Python:** Memberikan dukungan penuh untuk bahasa Python di VSCode.
        
    - **Jupyter:** Untuk menjalankan notebook interaktif.
        
    - **Pylance:** Memberikan fitur _intellectual language support_ seperti pelengkapan otomatis kode (_auto-complete_).
        
    - **Gitlens (Opsional):** Membantu visualisasi riwayat perubahan kode.
        

### Virtual Environment (Venv & Conda)

Virtual Environment berfungsi untuk mengisolasi paket-paket yang dibutuhkan oleh proyek tertentu agar tidak berbenturan dengan proyek lain.

- **Venv:** Modul bawaan Python untuk membuat lingkungan virtual.
    
- **Conda/Miniconda:** Pengelola lingkungan dan paket yang lebih luas.
    

> **Wawasan Penting:** Jika pengguna telah menginstal Anaconda atau Conda, maka instalasi venv secara terpisah tidak lagi diperlukan. Hal ini dikarenakan Conda sudah memaketkan instalasi Python dan pengelola lingkungannya sendiri secara terintegrasi.

### Source Code Management (Git)

Git adalah alat wajib dalam dunia kerja nyata untuk manajemen riwayat kode.

- **Versioning:** Melacak setiap perubahan yang terjadi pada kode dari waktu ke waktu.
    
- **Kolaborasi:** Memungkinkan tim untuk bekerja pada bagian kode yang berbeda secara paralel tanpa merusak pekerjaan satu sama lain.
    

> **Tips Verifikasi:** Untuk memastikan Git sudah terpasang, ketik perintah `git` di dalam terminal VSCode. Jika muncul daftar bantuan perintah, berarti Git telah dikenali oleh sistem.

### Troubleshooting Docker (Kasus Windows Home 11)

Dalam diskusi kelas, diidentifikasi adanya tantangan instalasi Docker Desktop pada pengguna Windows Home 11. Solusinya melibatkan:

- Penyesuaian pengaturan Virtualisasi di tingkat BIOS perangkat.
    
- Eksekusi perintah khusus melalui _Command Prompt_ (CMD) untuk melepas batasan sistem yang menghalangi instalasi pada edisi "Home".
    

## 4. Bedah Kode Pertama: Hello World!

Penulisan program 'Hello World' merupakan tradisi filosofis di dunia pemrograman sebagai langkah awal untuk memverifikasi bahwa lingkungan kerja telah siap sebelum masuk ke logika yang lebih kompleks.

### Demonstrasi Kode

Python

```
print('Hello world!')
```

### Bedah Elemen Kode

- **Fungsi Bawaan `print()`:** Merupakan _built-in function_ dalam Python yang memiliki tugas khusus untuk mengirimkan dan menampilkan keluaran (_output_) data ke layar monitor.
    
- **String Literal (`'Hello world!'`):** Teks yang berada di dalam tanda kutip (bisa kutip tunggal atau ganda). Ini adalah representasi data teks yang akan diproses oleh fungsi `print()`.
    

Pernyataan ini membuktikan bahwa Python adalah bahasa yang sangat ringkas, di mana instruksi yang jelas dapat diberikan hanya dalam satu baris kode tanpa memerlukan struktur _boilerplate_ yang rumit seperti pada bahasa lainnya.



## Bab 5 Konsep Dasar Pemrograman Python

Dokumen ini merupakan panduan belajar komprehensif mengenai dasar-dasar pemrograman Python, mencakup variabel, tipe data, manipulasi string, hingga operasi logika dan matematika. Materi ini disusun berdasarkan integrasi materi presentasi teknis dan penjelasan mendalam dari instruktur.

---
## 1. Konsep Variabel & Struktur Penyimpanan Memori

Dalam pemrograman Python, variabel adalah elemen fundamental yang berfungsi sebagai wadah untuk menyimpan data.

- **Definisi Formal:** Variabel dianalogikan sebagai sebuah kotak (_box_) yang memiliki label. Label tersebut adalah nama variabel, dan isi di dalamnya adalah data atau nilai yang disimpan.
    
- **Mekanisme Memori (RAM):** Berdasarkan penjelasan teknis, saat sebuah variabel dibuat, Python menyimpan nilai/data tersebut di dalam alamat memori RAM. Nama variabel berfungsi sebagai "label pengenal" agar pengembang dapat mengakses kembali nilai tersebut di alamat RAM yang sama secara efisien dan berulang kali di sepanjang program.
    
- **Operator Penugasan (Assignment Operator):** Tanda sama dengan (`=`) digunakan sebagai operator penugasan. Perannya adalah mengaitkan nilai yang berada di sisi kanan ke nama variabel yang berada di sisi kiri.
    

**Contoh Sederhana:**

Python

```
message = "hello"  # "hello" disimpan di RAM dengan label 'message'
age = 20           # 20 disimpan di RAM dengan label 'age'
```

## 2. Aturan Mutlak Penamaan Variabel (Variable Naming)

Penamaan variabel dalam Python harus mengikuti aturan sintaksis yang ketat agar tidak terjadi _error_ saat _runtime_.

- **Karakter yang Diperbolehkan:** Hanya huruf (A-Z, a-z), angka (0-9), dan garis bawah (_underscore_ `_`).
    
- **Larangan Angka di Depan:** Karakter pertama dari nama variabel tidak boleh berupa angka.
    
- **Sifat Case-Sensitive:** Python membedakan huruf besar dan kecil secara mutlak. Variabel `Nama` berbeda dengan `nama`.
    
- **Larangan Python Keywords:** Tidak boleh menggunakan kata kunci cadangan Python (_Reserved Words_) seperti `if`, `for`, `class`, `def`, `True`, `False`, `None`, dan lainnya.
    

### Tabel Analisis Validitas Penamaan Variabel

|Nama Variabel|Status|Alasan Teknis|
|---|---|---|
|`name`|Valid|Menggunakan huruf kecil standar.|
|`2name`|Invalid|Dimulai dengan angka (_Starts with a digit_).|
|`student_name`|Valid|Menggunakan _underscore_ sebagai pemisah.|
|`student-name`|Invalid|Tanda hubung/minus (`-`) tidak diperbolehkan.|
|`total2`|Valid|Angka diperbolehkan asal bukan di karakter pertama.|
|`total price`|Invalid|Spasi tidak diperbolehkan dalam nama variabel.|
|`_count`|Valid|_Underscore_ di awal diperbolehkan.|
|`class`|Invalid|`class` adalah kata kunci Python (_Python keyword_).|

> **Best Practice (PEP 8):** Sangat disarankan menggunakan gaya penulisan `snake_case`, yaitu menggunakan huruf kecil semua dan memisahkan antar kata dengan _underscore_ (contoh: `is_logged_in`, `total_price`).

## 3. Deep Dive Tipe Data Dasar (Basic Data Types)

Setiap nilai dalam Python memiliki tipe data tertentu yang menentukan operasi apa yang bisa dilakukan terhadapnya.

- **Int (Integer):** Merepresentasikan bilangan bulat tanpa desimal (contoh: 10, -5).
    
- **Float:** Merepresentasikan nilai desimal atau pecahan (contoh: 19.99, 3.14).
    
- **Bool (Boolean):** Entitas logika yang hanya memiliki dua nilai: `True` atau `False`.
    
- **Str (String):** Teks atau urutan karakter yang dibungkus oleh tanda kutip tunggal (`'`) atau ganda (`"`).
    
- **NoneType:** Tipe data khusus untuk merepresentasikan ketiadaan nilai (`None`).
    

> **Wawasan Khusus: Perbedaan 'None' vs '0'** Terdapat perbedaan fundamental antara angka 0 dan `None`. Angka 0 tetap merupakan sebuah nilai numerik dengan tipe data Integer. Sedangkan `None` adalah representasi kosong atau tidak adanya nilai sama sekali (NoneType). Analoginya, 0 adalah laci yang berisi angka nol, sedangkan `None` adalah laci yang benar-benar kosong tanpa barang di dalamnya.

## 4. Tipe Data Koleksi (Collection Data Types)

Adalah wadah untuk struktur organisasi data. Tipe data koleksi memungkinkan penyimpanan banyak nilai dalam satu variabel.

- **List:** Koleksi terurut yang bersifat _mutable_ (isinya dapat diubah, ditambah, atau dihapus setelah dibuat). Dideklarasikan dengan kurung siku `[]`.
    
- **Tuple:** Koleksi terurut yang bersifat _immutable_ (isinya tidak dapat diubah setelah didefinisikan). Dideklarasikan dengan kurung biasa `()`.
    
- **Set:** Koleksi tidak terurut dari elemen yang unik. Jika ada data duplikat, Python akan menghapusnya secara otomatis. Dideklarasikan dengan kurung kurawal `{}`.
    
- **Dict (Dictionary):** Koleksi pasangan kunci-nilai (_key-value pairs_). Sangat efisien untuk pencarian data berdasarkan kata kunci tertentu. Format penulisan: `{key: value}`.
    

**Pembuktian Tipe Data:** Gunakan fungsi bawaan `type()` untuk mengetahui tipe data dari sebuah variabel.

Python

```
message = "Hello"
print(type(message)) # Output: <class 'str'>
```

## 5. Metode Manipulasi String (String Built-in Methods)

Python menyediakan berbagai metode bawaan untuk memproses teks secara otomatis:

- `.upper()`: Mengubah semua karakter menjadi huruf besar.
    
- `.lower()`: Mengubah semua karakter menjadi huruf kecil.
    
- `.strip()`: Menghapus spasi kosong di awal dan akhir string.
    
- `.replace(lama, baru)`: Mengganti bagian teks tertentu dengan teks baru.
    
- `.split()`: Memecah string menjadi list berdasarkan pemisah tertentu.
    
- `.join()`: Menggabungkan elemen list menjadi satu string.
    
- `.find()`: Mencari posisi indeks dari karakter atau kata tertentu.
    
- `.startswith()`: Mengecek apakah string dimulai dengan karakter tertentu (True/False).
    
- `.endswith()`: Mengecek apakah string diakhiri dengan karakter tertentu (True/False).
    
- `.count()`: Menghitung jumlah kemunculan karakter tertentu dalam string.
    
- `.format()`: Metode lama untuk menyisipkan variabel ke dalam string.
    
- `.isalpha()`: Mengecek apakah seluruh isi string adalah huruf.
    
- `.isdigit()`: Mengecek apakah seluruh isi string adalah angka.
    
- `.isalnum()`: Mengecek apakah string hanya berisi huruf dan angka.
    

## 6. Formatted String Literals (f-Strings)

f-Strings adalah cara termudah dan paling efisien untuk menyisipkan variabel ke dalam teks.

- **Konsep:** Cukup tambahkan huruf `f` sebelum tanda kutip pembuka dan bungkus variabel atau ekspresi dengan kurung kurawal `{}`.
    
- **Kelebihan vs Concatenation:** Dibandingkan dengan penggabungan manual menggunakan tanda tambah (`+`) yang memerlukan konversi tipe data manual (seperti `str(age)`), f-String jauh lebih bersih, ringkas, dan memiliki performa runtime yang lebih cepat.
    
- **Evaluasi Ekspresi:** f-String memungkinkan operasi matematika langsung di dalam kurung kurawal.
    

**Contoh Perbandingan:**

Python

```
age = 25
# Manual Concatenation
message1 = "I am " + str(age) + " years old."

# f-String (Lebih Bersih)
message2 = f"Next year I will be {age + 1} years old."
```

## 7. User Input & Pengolahan Data

Fungsi `input()` digunakan untuk berinteraksi dengan pengguna.

- **Mekanisme:** Saat fungsi ini dipanggil, program akan menjeda eksekusi, menunggu pengguna mengetikkan sesuatu di konsol, dan menekan tombol Enter.
    
- **Aturan Mutlak:** Data yang diterima oleh fungsi `input()` selalu bertipe String (`str`), meskipun pengguna memasukkan angka. Jika ingin melakukan operasi matematika, data tersebut harus dikonversi terlebih dahulu.
    

## 8. Operasi Angka & Modul Matematika (Math Module)

Python memiliki fungsi bawaan untuk angka dan modul tambahan untuk perhitungan kompleks.

### Fungsi Bawaan (Tanpa Import)

- `abs()`: Nilai mutlak.
    
- `round()`: Membulatkan angka.
    
- `pow()`: Perpangkatan.
    
- `min()` / `max()`: Mencari nilai terkecil/terbesar.
    
- `sum()`: Menjumlahkan koleksi angka.
    
- `int()` / `float()`: Konversi tipe numerik.
    

### Modul Matematika (`import math`)

- `math.sqrt()`: Akar kuadrat.
    
- `math.ceil()`: Pembulatan ke atas.
    
- `math.floor()`: Pembulatan ke bawah.
    
- `math.factorial()`: Faktorial angka.
    
- **Konstanta:** `math.pi` (3.14...), `math.e`, `math.inf` (tak hingga), `math.nan` (Not a Number).
    

## 9. Konversi Tipe Data (Type Conversion)

Proses mengubah satu tipe data ke tipe data lainnya sering dibutuhkan dalam pengolahan data.

- **String Conversion:** Menggunakan `str()`.
    
- **Numeric Conversion:** Menggunakan `int()` atau `float()`. Perlu dicatat bahwa `int(3.99)` akan menghasilkan `3` karena fungsi ini memangkas (_truncation_) bagian desimal, bukan membulatkannya.
    
- **Boolean Conversion (Truthy & Falsy):**
    
    - **Nilai Falsy (Menghasilkan False):** Angka `0`, string kosong `""`, list kosong `[]`, tuple kosong `()`, set kosong `{}`, dan `None`.
        
    - **Nilai Truthy (Menghasilkan True):** Angka selain 0 (positif maupun negatif), string yang memiliki isi (termasuk spasi atau teks "False"), dan koleksi yang memiliki setidaknya satu elemen.
        

## 10. Operator Dasar Pemrograman

### Operator Aritmatika

- `+`, `-`, `*`, `/` : Tambah, kurang, kali, bagi.
    
- `%` (Modulo): Sisa bagi hasil pembagian.
    
- `**`: Perpangkatan.
    
- `//` (Floor Division): Pembagian bulat (menghilangkan desimal).
    

### Augmented Assignment Operators

Digunakan untuk menyingkat penulisan operasi aritmatika sekaligus penugasan nilai kembali ke variabel tersebut. **Penelusuran (Tracing) Contoh:**

Plaintext

```
n = 8
n += 5  (Sama dengan n = 8 + 5) -> n sekarang 13.
n *= 2  (Sama dengan n = 13 * 2) -> n sekarang 26.
```

### Operator Perbandingan & Logika

- **Perbandingan:** `==` (sama dengan), `!=` (tidak sama dengan), `>`, `<`, `>=`, `<=` (selalu mengembalikan nilai Boolean).
    
- **Logika:**
    
    - `and`: Bernilai True jika kedua kondisi benar.
        
    - `or`: Bernilai True jika salah satu kondisi benar.
        
    - `not`: Membalikkan nilai logika (True menjadi False, dan sebaliknya).



## Bab 6 Pengantar Pseudocode & Latihan Mandiri Pemecahan Masalah

Panduan belajar ini disusun secara komprehensif untuk memberikan pemahaman mendalam mengenai peran pseudocode dalam pengembangan algoritma dan strategi pemecahan masalah (_problem-solving_). Materi ini mencakup definisi teoretis, implementasi praktis dalam perhitungan matematis, hingga filosofi pembelajaran yang ditekankan dalam diskusi kelas.

---
## 1. Konsep & Definisi Pseudocode

### Definisi Formal

Pseudocode pada dasarnya adalah versi bahasa pemrograman yang "lebih mudah dipahami" (_easier-to-understand_). Hal ini disajikan dalam bentuk bahasa alami sederhana (_simple natural language_) yang menjembatani komunikasi antara logika manusia dan sintaks komputer yang kaku.

### Peran Utama dalam Algoritma

Fungsi fundamental dari pseudocode adalah untuk memvisualisasikan detail proses pemecahan masalah secara bertahap (_step-by-step process_). Sebelum seorang pengembang menulis kode dalam sintaks pemrograman nyata seperti Python atau JavaScript, pseudocode digunakan untuk memastikan alur logika telah benar dan efisien.

### Analisis Kegunaan

Bagi pengembang pemula, pseudocode merupakan alat yang sangat krusial untuk menghindari hambatan berpikir akibat kendala teknis sintaks bahasa pemrograman (_syntax block_). Dengan memisahkan logika dari aturan penulisan kode yang rumit, pengembang dapat berfokus sepenuhnya pada penyelesaian masalah itu sendiri.

## 2. Bedah Contoh Desain Pseudocode: Area of Rectangle

Sebagai pengenalan praktis, berikut adalah bedah kasus desain pseudocode untuk menghitung luas persegi panjang:

- **Contoh Kasus:** Menghitung luas persegi panjang berdasarkan nilai panjang (_length_) dan lebar (_width_) yang diberikan.
    
- **Petunjuk Penyelesaian (Hint):**
    
    - Identifikasi mekanisme penghitungan luas.
        
    - Petakan rumus matematika formal: `Area = Length * Width`.
        

**Langkah Pemecahan Masalah dalam Pseudocode:**

| **Langkah**   | **Aktivitas**                                                                                 | **Representasi Visual / Contoh**                         |
| ------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Langkah 1** | Mendefinisikan variabel awal dan menetapkan nilainya (_assignment_).                          | `const width = 10;`<br><br>  <br><br>`const length = 5;` |
| **Langkah 2** | Mendefinisikan variabel baru untuk menyimpan hasil dan mengimplementasikan formula perkalian. | `const areaOfRectangle = width * length;`                |

## 3. Analisis Logika Lima Latihan Mandiri (Exercises)

Berikut adalah uraian langkah-langkah berpikir logis, formula matematis, serta variabel input-output yang diperlukan untuk menyelesaikan latihan mandiri:

**Latihan 1: Menghitung Luas Persegi Panjang (Area of Rectangle)**

- **Spesifikasi:** Input `length = 5`, `width = 3`.
    
- **Logika:** Melakukan perkalian sederhana antara dua variabel input.
    
- **Output:** `15`.
    

**Latihan 2: Menghitung Keliling Persegi Panjang (Perimeter of Rectangle)**

- **Spesifikasi:** Input `length = 5`, `width = 3`.
    
- **Formula Logis:** `Perimeter = 2 * (length + width)`.
    
- **Output:** `16`.
    

**Latihan 3: Menghitung Properti Lingkaran (Circle Properties)**

- **Spesifikasi:** Input `radius = 5`.
    
- **Formula Logis:**
    
    - `Diameter = 2 * radius`.
        
    - `Circumference = 2 * pi * radius`.
        
    - `Area = pi * radius^2`.
        
- **Output:** Diameter = 10, Circumference = 31.4159, Area = 78.539.
    

**Latihan 4: Mencari Sudut Ketiga Segitiga (Angles of Triangle)**

- **Spesifikasi:** Input dua sudut, misal `a = 80`, `b = 65`.
    
- **Formula Logis:** `Sudut ketiga = 180 - (a + b)`.
    
- **Dasar Teori:** Aturan geometris menetapkan bahwa total sudut dalam segitiga selalu berjumlah 180 derajat.
    
- **Output:** `35`.
    

**Latihan 5: Mengonversi Hari ke Tahun, Bulan, dan Hari (Days Conversion)**

Tugas ini memerlukan pemetaan logika menggunakan pembagian bulat dan operasi sisa bagi (_modulus_).

- **Catatan Standar:** 1 tahun = 365 hari, 1 bulan = 30 hari.
    
- **Langkah Logika:**
    
    1. **Menghitung tahun:** Membagi bulat jumlah hari dengan 365 (`years = days // 365`).
        
    2. **Sisa hari pertama:** Mencari sisa bagi jumlah hari dengan 365 (`remaining_days_1 = days % 365`).
        
    3. **Menghitung bulan:** Membagi bulat sisa hari pertama dengan 30 (`months = remaining_days_1 // 30`).
        
    4. **Sisa hari akhir:** Mencari sisa bagi sisa hari pertama dengan 30 (`final_days = remaining_days_1 % 30`).
        

**Hasil Kasus Uji:**

| **Input** | **Hasil Konversi**       |
| --------- | ------------------------ |
| 400 Hari  | 1 Tahun, 1 Bulan, 5 Hari |
| 366 Hari  | 1 Tahun, 0 Bulan, 1 Hari |

## 4. Integrasi Diskusi Interaktif & Insight Dosen

Berdasarkan interaksi kelas, terdapat beberapa poin penting yang perlu diperhatikan oleh mahasiswa dalam mengerjakan latihan mandiri ini:

### Media Penulisan Tugas

Dalam diskusi antara mahasiswa (Reza & Adiba) dengan dosen, ditegaskan bahwa latihan mandiri ini dapat dikerjakan cukup di aplikasi catatan (_notes_) biasa. Mahasiswa diperbolehkan menggunakan bahasa alami atau pseudocode murni dan tidak diwajibkan langsung menulis dalam sintaks Python jika belum merasa terbiasa.

### Fleksibilitas Eksplorasi

Meskipun pseudocode diperbolehkan, dosen tetap menganjurkan mahasiswa yang ingin bereksplorasi menggunakan Visual Studio Code untuk mencoba mengeksekusi script Python secara langsung. Praktik langsung ini dianggap akan memberikan pengalaman belajar yang lebih mendalam.

### Filosofi "Pola Pikir Algoritma"

Dosen memberikan penegasan fundamental bahwa kefasihan menghafal sintaks Python pada pertemuan awal bukanlah hal terpenting. Hal yang paling mendasar adalah melatih pola pikir terstruktur dalam menyelesaikan masalah (_problem-solving mindset_).

**Poin utama pembelajaran ini adalah:**

- Pahami alur berpikir algoritma di kepala terlebih dahulu.
    
- Jika alur logika sudah benar, translasi ke baris kode pemrograman riil akan menjadi sangat mudah.
    
- Kekuatan seorang pengembang terletak pada logikanya, bukan hanya pada kemampuannya mengetik sintaks.



## Latihan Code

## 1. Kasus membuat keterangan Data Collection

> Lihat catatan tipe-tipe data koleksi disi [[Bab 5 Konsep Dasar Pemrograman Python#4. Tipe Data Koleksi (Collection Data Types)]]

### 1.1. Memberi keterangan kata

[Cek kamus string](https://docs.python.org/3/library/stdtypes.html#string-methods)

Jenis data disini adalah string (str)
Variabel: binatang
Data: "anjing hitam besar", "kucing berekor pendek"

```bash
binatang: "anjing hitam besar"
```


```bash
binatang: "kucing berekor pendek"
```


### 1.2. Memberi keterangan angka
Jenis data: integer (int)
Variabel: binatang
Data: 20

```bash
binatang: 20
```

### 1.3. Mencampur variabel & tipe data

Mencampur variabel dalam dalam sebuah wadah yakni associative array dengan simbol {}. Kurung kurawal itu adalah dictionary. 

Jenis data: string, integer
Variabel: "daftar_binatang"
Key value (label pengenal): 
```bash
"pinguin_1"
"jerapah_1"
"armadilo_1"
```

Tugasnya:
1. Masukan key kedalam variable. 
2. Masukan data kedalam key. 
```bash
daftar_binatang = {
		"pinguin_1": "hitam lucu",
		"jerapah_1": "berleher panjang",
		"armadilo_1": "berkulit keras"
}

```

Tujuan dari rancangan kode ini adalah untuk mengalokasikan ruang memori besar bernama `daftar_binatang`, lalu menyimpan tiga data keterangan binatang ke dalamnya secara terstruktur. Dengan menggunakan format Dictionary, tujuannya agar Anda sebagai pengembang (developer) nantinya bisa dengan mudah memanggil keterangan spesifik secara akurat (misalnya mencari keterangan armadilo tanpa harus membaca data pinguin).



## 2. Membuat Pesan

### 2.1 Mencetak pesan: 
Setiap code harus diperintah dulu akgar bisa mengambil aksi. 
Dalam case melakuakn pencetakan pesan, harus dibuat message dulu yang isinya memanggil data collection anda. 

### 2.1.1 Cara Manual

1. Buat data collection dengan isi:
```bash
age = 32
```

2. Kemudian perintah cetak dengan 
```bash
message1 = "saya" + str(age) + "tahun"

print (message1)
```

3.  Kemudian cetak pesan dengan memencet tombol play di file py anda. Nati akan muncul di terminal:
```bash
saya32tahun
```

### 2.1.2  f-string

#### 2.1.2.1 Contoh Gampang

Disini saya punya kasus ingin menambahkan umur dari data collection, sekaligus membuat kalimat. Maka saya memanggil umur atau **age** dan menambahkan penambahan sederhana + 1.

1. Buat data collection dengan isi:
```bash
age = 32
```

2. Kemudian perintah cetak dengan
```bash
message2 = f"tahun depan saya akan berumur {age + 1} tahun"

print (message2)
```

3. Kemudian cetak pesan dengan memencet tombol play di file py anda. Nanti akan muncul di terminal:
```bash
tahun depan saya akan berumur 33 tahun
```

#### 2.1.2.2 Logika Percabangan (If-Else) & boolean

Disini saya mau melakukan penambahan sederhana dan mengecek perhitungan, benar atau salah:

1. Menyiapkan Data Collection dan Kondisi (Boolean):
```bash
umur = 31
sudah_tua = umur > 50
```

2. Mengatur percabangnan keputusan dengan (If-Else):
Jika kondisi sudah_tua terbuki benar (True), maka variabel warna_rambut akan diisi keterangan data "putih". Selain kondisi itu, akan dikenal sebagai (False) dan diisi "hitam"
```bash
if sudah_tua == True:

    warna_rambut = "putih"
else:

    warna_rambut = "hitam"
```

3. Mencetak logika murni (True/False)
Menggunakan f-String untuk melihat langsung wujud isi dari variabel Boolean "sudah_tua".
```bash
message3 = f"reiner sudah {umur} tahun. Apakah dia rambut dia putih? {sudah_tua}"

print (message3)
```
 terminal akan menjawab bahwa keterangan false. Karena dia masih dibawha 50 tahun. 
```bash
reiner sudah 31 tahun. Apakah dia rambut dia putih? False
```

4. Mencetak Variabel yang Sudah Diubah oleh If-Else

Kegunaan utama langkah 4 adalah **menerjemahkan data yang diproses mesin agar menjadi informasi yang ramah dibaca oleh manusia.**

```bash
message4 = f"reiner sudah {umur} tahun. Warna rambut dia adalah {warna_rambut}"

print (message4)
```
terminal akan menjawab bahwa warna rambut dia adalah hitam. 
```bash
reiner sudah 31 tahun. Warna rambut dia adalah hitam
```




## Review Fondasi Pemrograman Python

---
tags:
  - Phyton
---
Dokumen ini menyajikan review dari sesi 1 dalam modul 1, sintesis komprehensif mengenai dasar-dasar pemrograman Python, mencakup logika matematika dasar, manipulasi tipe data angka, hingga pengoperasian dasar melalui terminal dan _Integrated Development Environment_ (IDE).

## 1. Logika Pemrograman Matematika & Geometri Dasar

Pemrograman dasar sering kali diawali dengan implementasi formula matematika ke dalam kode untuk menyelesaikan persoalan geometri sederhana. Fokus utama pada bagian ini adalah pendefinisian variabel yang tepat dan pemilihan tipe data yang sesuai dengan hasil kalkulasi.

### 1.1. Perhitungan Persegi Panjang (_Rectangle_)

Dalam menghitung karakteristik persegi panjang, diperlukan pendefinisian input yang jelas untuk variabel panjang (_length_) dan lebar (_width_). Berdasarkan variabel tersebut, operasi aritmetika dilakukan untuk mencari luas (_area_) dan keliling (_perimeter_).

- **Variabel yang Terlibat:** `length`, `width`, `area`, `perimeter`.
- **Logika Kode:**

```python
length = 5
width = 3

area = length * width
perimeter = 2 * (length + width)

print(area)
print(perimeter)
```

**[Wawasan Diskusi / Audio Insight]** Dalam diskusi antara Brian dan instruktur, ditekankan bahwa variabel seperti `length`, `width`, dan `perimeter` umumnya menggunakan tipe data **Integer** (bilangan bulat) jika input awal tidak mengandung desimal. Hasil akhir dapat langsung ditampilkan sebagai angka tanpa perlu tambahan teks penjelasan jika tujuannya adalah _output_ langsung.

### 1.2. Formulasi Lingkaran (_Circle_) dan Analisis Tipe Data

Perhitungan lingkaran memiliki kompleksitas lebih tinggi karena melibatkan konstanta \pi (Pi). Penggunaan konstanta ini secara otomatis akan memengaruhi tipe data dari hasil kalkulasi.

- **Formula Dasar:**
    - `diameter` = 2 \times r
    - `circumference` (Keliling) = 2 \times \pi \times r atau \pi \times d
    - `area` (Luas) = \pi \times r^2
- **Perbandingan Karakteristik Tipe Data Angka:**

|   |   |   |
|---|---|---|
|Karakteristik|Integer|Float|
|**Definisi**|Bilangan bulat (tanpa koma).|Bilangan desimal/pecahan.|
|**Contoh Hasil**|10, 15, 100.|31.4, 78.5.|
|**Penggunaan**|Perhitungan jumlah barang, indeks.|Perhitungan sains, koordinat, luas lingkaran.|

**[Wawasan Diskusi / Audio Insight]** Terjadi poin pembelajaran penting saat Steve mengasumsikan bahwa semua hasil perhitungan lingkaran adalah **Integer** karena input radiusnya bulat. Namun, setelah script dijalankan (`python test.py`), _output_ menunjukkan angka desimal (seperti 31.4). Hal ini membuktikan bahwa keterlibatan angka desimal dalam operasi perkalian secara otomatis mengubah tipe data menjadi **Float**.

### 1.3. Mencari Sudut Ketiga Segitiga

Logika pemrograman untuk mencari sudut ketiga dari sebuah segitiga didasarkan pada aturan geometri bahwa total sudut internal segitiga selalu 180^\circ.

- **Logika:** Sudut_3 = 180 - (Sudut_1 + Sudut_2).
- **Implementasi Kode:**

```python
angle1 = 60
angle2 = 70
angle3 = 180 - (angle1 + angle2)

print(angle3)
```

## 2. Studi Kasus Konversi Hari

Kasus ini menguji pemahaman mengenai bagaimana memecah satu nilai besar (total hari) menjadi satuan waktu yang lebih terstruktur (tahun, bulan, dan hari) menggunakan operator aritmetika Python.

### 2.1. Metode Perhitungan: Aritmetika Manual vs Operator Spesifik

Terdapat dua pendekatan utama dalam menyelesaikan masalah konversi ini, sebagaimana didiskusikan dalam sesi studi kasus.

|   |   |   |
|---|---|---|
|Fitur|Metode Aritmetika Manual (Reza)|Metode Operator Ringkas (Anwar)|
|**Operator Utama**|Pembagian tradisional (`/`) dan pengurangan.|_Floor Division_ (`//`) dan _Modulo_ (`%`).|
|**Efisiensi**|Membutuhkan lebih banyak langkah variabel sementara.|Jauh lebih ringkas dan langsung ke sisa bagi.|
|**Logika Tahun**|`hari / 365` (kemudian dibulatkan).|`hari // 365`.|
|**Logika Sisa Hari**|Pengurangan manual dari total.|`hari % 365`.|

### 2.2. Implementasi Logika _Floor Division_ dan _Modulo_

Pendekatan Anwar dianggap lebih efisien dalam Python karena menggunakan operator yang memang didesain untuk pembagian bilangan bulat.

```python
total_days = 400

years = total_days // 365
remaining_days = total_days % 365
months = remaining_days // 30
days = remaining_days % 30

print(years, "Tahun", months, "Bulan", days, "Hari")
```

**[Wawasan Diskusi / Audio Insight]** Diskusi kelas mengidentifikasi bahwa konversi hari adalah salah satu latihan dengan tingkat kesulitan tertinggi bagi pemula. Pemahaman tentang sisa bagi (_modulo_) menjadi kunci agar sisa hari tidak hilang dalam perhitungan saat berpindah dari satuan tahun ke bulan.

## 3. Pengenalan Dasar Navigasi Terminal & IDE

Kemampuan menjalankan script Python memerlukan pemahaman tentang navigasi direktori dalam sistem operasi melalui terminal atau _command prompt_.

### 3.1. Perintah Navigasi Dasar

Terminal menggunakan perintah berbasis teks untuk berpindah antar folder (_directory_).

- `**cd**` **(**_**Change Directory**_**):** Digunakan untuk masuk ke folder tertentu.
    - Jika nama folder memiliki spasi (contoh: `Python Project`), gunakan bantuan _auto-complete_.
- `**ls**` **(**_**List**_**):** Digunakan untuk melihat daftar berkas dan folder di direktori aktif saat ini.
- `**Tab Completion**`**:** Menekan tombol **Tab** saat mengetik nama direktori akan melengkapi nama folder secara otomatis untuk menghindari kesalahan tipografi.

### 3.2. Eksekusi Script Python

Untuk menjalankan berkas Python yang telah dibuat di IDE (seperti VS Code), pengguna harus memastikan terminal berada di direktori yang sama dengan berkas tersebut.

- **Perintah eksekusi:** `python nama_file.py`
- **Penanganan Error Direktori:** Jika terminal menunjukkan `C:\Users\Username` sementara file berada di `Desktop`, maka perintah `python` akan gagal kecuali pengguna melakukan `cd Desktop` terlebih dahulu.

### 3.3. Penggunaan Komentar (_Comment_)

Komentar digunakan untuk memberikan penjelasan pada kode atau menonaktifkan baris kode tertentu agar tidak dieksekusi oleh Python.

- **Simbol:** Menggunakan tanda pagar `#`.
- **Pintasan Keyboard (VS Code):**
    - Windows: `Ctrl + /`
    - Mac: `Cmd + /`

**[Wawasan Diskusi / Audio Insight]** Dalam sesi praktik, Steve mengalami kendala saat mencoba menjalankan `python test.py` karena posisi terminalnya masih berada di direktori pengguna (`C:\Users\Steve`), sementara file tersebut tersimpan jauh di dalam sub-folder `OneDrive\Desktop\Python Project`. Penggunaan `cd` secara bertahap dan bantuan tombol **Tab** terbukti mempercepat proses navigasi menuju direktori yang tepat.



---


# Module 1 Session 2 Intro to GIt & Github


## Bab 1 Pengenalan Git dan GitHub (Introduction to Git & GitHub)

---
tags:
  - GIT
  - GITHUB
---
# Pengenalan Git dan GitHub

Dokumen ini memberikan tinjauan tingkat tinggi mengenai Git dan GitHub, yang mencakup definisi, sejarah singkat, karakteristik utama, serta signifikansi penggunaannya dalam pengembangan perangkat lunak modern.

## Definisi Git

Git adalah sebuah _distributed version control system_ (VCS) yang memungkinkan pengembang untuk melacak perubahan pada kode mereka dari waktu ke waktu. Sistem ini dirancang untuk menangani segala jenis proyek, mulai dari proyek kecil hingga proyek yang sangat besar, dengan tingkat kecepatan dan efisiensi yang tinggi.

Salah satu fungsi utama Git adalah memfasilitasi kolaborasi. Dengan Git, beberapa orang dapat bekerja pada proyek yang sama secara bersamaan tanpa risiko saling menimpa (_overwriting_) perubahan yang dilakukan oleh pengembang lain.

## Sejarah Singkat dan Tokoh Kunci

Git diciptakan oleh **Linus Torvalds**, yang juga dikenal sebagai pencipta sistem operasi Linux. Pengembangan Git didorong oleh kebutuhan akan sistem kontrol versi yang handal dan terdistribusi untuk mengelola pengembangan _kernel_ Linux yang sangat kompleks dan masif.

## Karakteristik Utama Git

Berikut adalah tabel yang merangkum fitur dan karakteristik fundamental dari Git:

|   |   |
|---|---|
|Karakteristik|Deskripsi|
|**Tipe Sistem**|_Distributed version control system_ (VCS).|
|**Fungsi Utama**|Melacak setiap perubahan pada kode sumber secara kronologis.|
|**Keamanan Kolaborasi**|Memungkinkan banyak pengembang bekerja bersama tanpa risiko _overwriting_.|
|**Efisiensi Proyek**|Mampu menangani proyek berskala kecil hingga sangat besar dengan cepat.|
|**Arsitektur Terdistribusi**|Setiap pengembang memiliki salinan lengkap dari riwayat proyek di mesin lokal mereka.|

## Definisi GitHub

Berbeda dengan Git yang merupakan alat (_tool_) teknis, GitHub adalah sebuah platform layanan _hosting_ berbasis web untuk repositori Git. GitHub menyediakan tempat bagi pengembang untuk menyimpan proyek mereka secara daring (_online_), sehingga memudahkan proses kolaborasi dengan pihak luar atau anggota tim lainnya.

GitHub bukan sekadar tempat penyimpanan, melainkan berfungsi sebagai jejaring sosial bagi para pengembang. Di sini, pengembang dapat saling berbagi kode, memberikan kontribusi pada proyek sumber terbuka (_open-source_), dan mengelola proyek secara profesional.

### Fitur Kerja Tim di GitHub

GitHub menyediakan berbagai alat untuk mendukung manajemen proyek dan kerja sama tim, antara lain:

- **Pull Request:** Mekanisme untuk mengajukan perubahan kode ke proyek utama.
- **Issue Tracking:** Fitur untuk mencatat dan melacak bug, tugas, atau permintaan fitur baru.
- **Project Management:** Perangkat lunak terintegrasi untuk mengelola alur kerja dan progres proyek.

## Perbedaan Peran Git vs GitHub

Sering kali dianggap sama, Git dan GitHub memiliki peran yang berbeda namun saling melengkapi dalam ekosistem pengembangan perangkat lunak:

|   |   |   |
|---|---|---|
|Aspek Perbedaan|Git|GitHub|
|**Sifat Dasar**|Perangkat lunak _version control_ (lokal).|Layanan _hosting_ berbasis web (cloud).|
|**Instalasi**|Diinstal dan dijalankan secara lokal pada komputer.|Diakses melalui peramban web atau aplikasi pihak ketiga.|
|**Fokus Utama**|Pelacakan perubahan kode dan manajemen revisi.|Penyimpanan daring, kolaborasi tim, dan jejaring sosial pengembang.|
|**Ketergantungan**|Dapat berjalan sendiri tanpa internet.|Memerlukan koneksi internet untuk sinkronisasi dan fitur kolaboratif.|

## Signifikansi Penggunaan Git & GitHub

Penggunaan kombinasi Git dan GitHub sangat penting bagi pengembang modern karena alasan berikut:

1. **Peningkatan Produktivitas:** Memudahkan pengelolaan versi kode sehingga pengembang dapat fokus pada penulisan fitur.
2. **Kolaborasi yang Lebih Baik:** Menyediakan infrastruktur yang rapi agar tim dapat bekerja secara simultan tanpa konflik yang merusak.
3. **Code Management:** Memberikan kontrol penuh terhadap riwayat kode, memudahkan pelacakan bug, dan memastikan keamanan integritas kode sumber.

**[Wawasan Diskusi / Audio Insight]** Dalam sesi interaktif, ditekankan betapa masifnya kontribusi Linus Torvalds terhadap dunia teknologi informasi. Torvalds tidak hanya menciptakan sistem operasi Linux—yang kini bersifat gratis dan menjadi tulang punggung bagi mayoritas server di seluruh dunia—tetapi ia juga menciptakan Git sebagai solusi atas kebutuhan manajemen kode yang kompleks. Penjelasan ini menggarisbawahi bahwa tanpa inovasi Torvalds dalam menciptakan Git, kolaborasi pengembang skala global seperti yang terlihat di GitHub saat ini tidak akan mungkin terjadi secara efisien.



## Bab 2 Konsep Dasar Sistem Git



Sistem Git merupakan _distributed version control system_ (VCS) yang memungkinkan pengembang untuk melacak perubahan kode dari waktu ke waktu. Git dirancang untuk menangani proyek dari skala kecil hingga sangat besar dengan efisien, memungkinkan kolaborasi antar pengembang tanpa risiko menimpa pekerjaan satu sama lain.

## 1. Metode Analogi Struktur Git

Untuk memahami cara kerja Git, struktur sistem ini dapat divisualisasikan menggunakan analogi sebuah pohon. Analogi ini membantu pengembang memahami hirarki dan hubungan antar elemen di dalam Git:

- **Pohon (Tree):** Merepresentasikan keseluruhan proyek atau aplikasi yang sedang dikembangkan.
- **Cabang (Branch):** Merepresentasikan jalur pengembangan yang independen. Dalam satu pohon (proyek), bisa terdapat banyak cabang yang tumbuh secara bersamaan.
- **Daun (Leaves):** Merepresentasikan **commit**. Setiap daun adalah titik penanda perubahan yang spesifik pada jalur pengembangan tersebut.

## 2. Empat Istilah Kunci Utama Git

Memahami Git memerlukan penguasaan atas empat istilah fundamental yang menjadi fondasi pengoperasiannya:

### Repository (Repo)

_Repository_ adalah tempat penyimpanan utama di mana sebuah proyek disimpan. Secara teknis, ini berfungsi seperti folder besar di komputer yang memiliki kemampuan khusus untuk melacak semua file dan setiap perubahan yang terjadi pada file-file tersebut sepanjang waktu.

### Commit

_Commit_ adalah sebuah _snapshot_ atau potret dari proyek pada titik waktu tertentu. Ketika pengembang melakukan perubahan dan menyimpannya sebagai _commit_, Git mencatat keadaan persis dari seluruh proyek saat itu.

- Setiap _commit_ diidentifikasi secara unik menggunakan **SHA-1 hash** (untaian 40 karakter heksadesimal).
- Hash ini memungkinkan pengembang untuk merujuk kembali ke versi lama dan melihat sejarah perubahan dengan presisi tinggi.

### Branch

_Branch_ adalah salinan jalur pengembangan proyek yang memungkinkan pengembang bekerja tanpa memengaruhi jalur utama (_main project_). Fitur ini sangat penting untuk eksperimen atau pengembangan fitur baru secara terisolasi.

### Merge

_Merge_ adalah proses pengambilan perubahan dari sebuah _branch_ dan menggabungkannya kembali ke proyek utama.

- Git akan mencoba menggabungkan perubahan secara otomatis.
- Jika terdapat perubahan pada baris kode yang sama di dua jalur berbeda, akan terjadi _conflict_. Dalam situasi ini, pengembang harus melakukan **conflict resolution** secara manual untuk menentukan kode mana yang akan digunakan.

**[Wawasan Diskusi / Audio Insight]**

- **Repository vs. Cloud Storage:** _Repository_ dapat dibayangkan seperti layanan drive bersama (seperti Google Drive atau OneDrive), namun dengan kecerdasan tambahan untuk melacak riwayat perubahan secara mendalam, bukan sekadar menyimpan file versi terbaru.
- **Kolaborasi Git vs. Google Docs:** Berbeda dengan Google Docs yang menggunakan _live update_ (perubahan tersimpan otomatis secara _real-time_), Git menggunakan mekanisme _merge_ dan _conflict resolution_ manual. Hal ini memberikan kendali penuh kepada pengembang untuk meninjau kode sebelum digabungkan ke sistem utama.

## 3. Tabel Rangkuman 4 Istilah Kunci

|   |   |   |
|---|---|---|
|Istilah Kunci|Definisi Teknis|Analogi Dunia Nyata|
|**Repository**|Lokasi penyimpanan digital untuk melacak seluruh file dan riwayat perubahan.|Folder besar atau gudang arsip proyek.|
|**Commit**|_Snapshot_ proyek pada titik waktu tertentu dengan identitas SHA-1 hash.|Foto keadaan proyek sebagai titik simpan (_checkpoint_).|
|**Branch**|Jalur pengembangan independen yang terpisah dari kode utama.|Cabang pohon yang tumbuh ke arah berbeda dari batang utama.|
|**Merge**|Proses penggabungan perubahan dari satu jalur ke jalur lainnya.|Menyatukan kembali cabang ke batang pohon utama.|

## 4. Signifikansi dan Konsep Branching System

Sistem _branching_ memiliki peran krusial dalam menjaga stabilitas proyek. Tujuan utamanya adalah memisahkan jalur fitur baru atau eksperimen agar tidak merusak kode produksi utama (_main branch_) yang sedang berjalan.

Visualisasi _branching_ dapat dilihat pada skema pengembangan aplikasi besar, misalnya Instagram:

- **Main Branch (Warna Abu-abu):** Merupakan jalur kode yang stabil dan sedang digunakan oleh pengguna (kode produksi).
- **Feature Branches (Warna Biru/Kuning):** Jalur pengembangan untuk fitur baru, misalnya fitur "Explore" atau "Account". Pengembang bekerja di sini untuk memastikan fitur selesai dan bebas _bug_ sebelum akhirnya melakukan _merge_ ke jalur abu-abu.

Dengan sistem ini, jika terjadi kesalahan pada fitur baru yang sedang dikembangkan (jalur biru), aplikasi utama (jalur abu-abu) tetap aman dan tidak mengalami gangguan atau _crash_.

## 5. Lelucon Keselamatan Software Engineer

Dalam komunitas _software engineer_, terdapat sebuah anekdot atau lelucon mengenai prosedur darurat jika terjadi kebakaran di gedung kantor. Lelucon ini menggambarkan prioritas seorang pengembang terhadap keamanan kode yang mereka tulis:

**"In Case of Fire:"**

1. `git commit`
2. `git push`
3. `git out!`

**[Wawasan Diskusi / Audio Insight]** Dosen menjelaskan logika di balik lelucon ini sebagai protokol keselamatan digital:

- **git commit:** Mengamankan perubahan terakhir di _checkpoint_ lokal laptop.
- **git push:** Mengunggah kode tersebut ke _cloud remote repository_. Hal ini dilakukan agar jika laptop hancur atau meleleh akibat api, hasil kerja keras pengembang tetap selamat di server _cloud_.
- **git out!:** Setelah kode aman di server, barulah pengembang menyelamatkan diri keluar dari gedung. Ini menekankan bahwa bagi seorang pengembang, keselamatan kode (aset digital) sering kali diposisikan sangat penting sebelum mereka benar-benar meninggalkan area berbahaya.



## Bab 3 Bekerja dengan Commits Lokal secara Terstruktur dan Mendalam



Dokumen ini menyajikan panduan mendalam mengenai pengelolaan _commits_ pada Git lokal berdasarkan materi teknis dan diskusi interaktif dalam sesi pembelajaran. Fokus utama bab ini adalah memahami bagaimana Git melacak perubahan berkas dan prosedur standar dalam menciptakan _snapshot_ kode yang stabil.

## 1. Siklus Status Berkas (Status Lifecycle)

Dalam Git, setiap berkas di dalam _working directory_ (direktori kerja) memiliki siklus status yang menentukan bagaimana Git memperlakukan berkas tersebut. Secara garis besar, berkas dikategorikan menjadi dua kelompok utama: _tracked files_ dan _untracked files_.

- **Tracked files:** Berkas yang sudah dikenal oleh Git. Berkas ini adalah bagian dari _snapshot_ terakhir atau telah masuk ke dalam _staging area_. Statusnya dapat berupa _unmodified_, _modified_, atau _staged_.
- **Untracked files:** Berkas apa pun di dalam direktori kerja yang tidak ada dalam _snapshot_ terakhir dan belum dimasukkan ke dalam _staging area_. Git melihat berkas ini tetapi tidak memantau perubahannya secara otomatis.

### Tabel Karakteristik dan Indikator Status Berkas

|   |   |   |
|---|---|---|
|Status|Arti|Karakteristik / Indikator|
|**Untracked**|Berkas Baru|Berkas yang belum pernah direkam oleh Git. Tidak termasuk dalam riwayat versi.|
|**Unmodified**|Belum Dimodifikasi|Berkas _tracked_ yang isinya identik dengan versi yang ada pada _commit_ terakhir.|
|**Modified**|Telah Dimodifikasi|Berkas _tracked_ yang telah mengalami perubahan pada direktori kerja, namun perubahannya belum ditandai untuk _commit_.|
|**Staged**|Siap di-Commit|Berkas yang telah ditandai (melalui perintah `git add`) untuk disertakan dalam _snapshot_ berikutnya.|

**[Wawasan Diskusi / Audio Insight]** Dalam praktik menggunakan VS Code, indikator status berkas dapat dilihat secara visual di samping nama berkas pada panel penjelajah. Diskusi kelas menyoroti bahwa berkas yang berstatus **Untracked** sering kali ditandai dengan indikator huruf **'U'** berwarna hijau. Hal ini menandakan bahwa berkas tersebut baru dibuat dan Git memerlukan instruksi eksplisit (seperti `git add`) untuk mulai melacaknya.

## 2. Alur Kerja Perintah Dasar Commit Lokal

Proses melakukan _commit_ memerlukan urutan perintah yang disiplin untuk memastikan riwayat perubahan tersimpan dengan rapi.

### 2.1 Inisialisasi Repository (`git init`)

Langkah pertama dalam menggunakan Git adalah mengubah direktori biasa menjadi Git _repository_ lokal. Perintah `git init` akan membuat sub-direktori `.git` tersembunyi yang menyimpan semua metadata dan riwayat versi.

**[Wawasan Diskusi / Audio Insight]** Diskusi teknis menunjukkan adanya kesulitan navigasi terminal sebelum menjalankan `git init`. Pengguna sering kali berada di direktori pengguna default (seperti `C:\Users\NamaUser`) dan harus berpindah ke folder proyek yang tepat.

- **Navigasi Terminal:** Gunakan perintah `cd` (_change directory_) untuk mencapai folder tujuan. Contoh alur navigasi yang didiskusikan meliputi pemindahan dari `OneDrive` ke `Desktop`, lalu ke `Python Project`.
- **Auto-complete:** Gunakan tombol **Tab** saat mengetik nama folder untuk menghindari kesalahan penulisan (seperti spasi pada nama folder).
- **Verifikasi Lokasi:** Jalankan perintah `ls` (atau `dir` pada Windows) untuk melihat isi direktori dan memastikan berkas proyek ada di sana sebelum menjalankan perintah Git.

### 2.2 Mengatur Identitas (`git config`)

Sebelum melakukan _commit_, pengguna wajib mengatur identitas global. Hal ini penting karena setiap _commit_ Git menyertakan informasi penulis sebagai bagian dari _snapshot_ yang tidak dapat diubah.

```python
git config --global user.name "Nama Pengguna"
git config --global user.email "email@contoh.com"
```

### 2.3 Memeriksa Status Real-Time (`git status`)

Perintah `git status` digunakan untuk melihat perbedaan antara berkas di direktori kerja, _staging area_ (index), dan _commit_ terakhir (HEAD). Perintah ini memberikan panduan mengenai langkah apa yang harus diambil selanjutnya (misalnya: apakah ada berkas yang perlu di-`add`).

### 2.4 Memindahkan Berkas ke Tahap Staged (`git add`)

Berkas yang telah dimodifikasi atau berkas baru harus dipindahkan ke _staging area_ sebelum bisa disimpan secara permanen.

- `git add <nama_berkas>`: Menambahkan berkas spesifik.
- `git add .`: Menambahkan semua perubahan dan berkas baru di direktori saat ini ke tahap _staged_.

### 2.5 Membuat Snapshot (`git commit`)

_Commit_ adalah proses mengambil _snapshot_ dari proyek pada titik waktu tertentu. Setiap _commit_ diidentifikasi oleh _hash_ SHA-1 unik sepanjang 40 karakter.

```bash
git commit -m "feat: pesan commit yang deskriptif"
```

**Kriteria Commit yang Sempurna:**

1. Menyertakan perubahan yang tepat (tidak kurang, tidak lebih).
2. Memiliki pesan _commit_ yang menjelaskan maksud dari perubahan tersebut secara jelas.

**[Wawasan Diskusi / Audio Insight]** Dosen memberikan panduan khusus saat mahasiswa menghadapi kondisi "no commits yet" meskipun berkas sudah ada. Melalui kasus Reainer, dijelaskan bahwa urutan yang benar adalah memastikan berkas dipindahkan ke "changes to be committed" terlebih dahulu menggunakan `git add`, baru kemudian menjalankan `git commit`. Tanpa tahap _add_, Git tidak akan memiliki data untuk disimpan ke dalam riwayat.

### 2.6 Memeriksa Perubahan (`git diff`)

Sebelum melakukan _commit_, disarankan menjalankan `git diff` untuk memeriksa detail perubahan baris per baris pada berkas. Hal ini memastikan bahwa hanya perubahan yang diinginkan yang masuk ke dalam _snapshot_.

## 3. Catatan Tambahan Terkait Lingkungan Kerja

Dalam mengerjakan proyek berbasis Python dan Git di terminal VS Code, sangat penting untuk memperhatikan lingkungan eksekusi (environment).

**[Wawasan Diskusi / Audio Insight]** Sebelum menjalankan script Python atau perintah Git tertentu, dosen menekankan pentingnya aktivasi _virtual environment_. Di terminal VS Code, sering kali pengguna perlu memastikan bahwa environment **base** pada MiniConda atau Anaconda sudah aktif. Hal ini ditandai dengan munculnya nama environment dalam kurung di awal baris perintah terminal. Aktivasi lingkungan yang tepat memastikan semua _dependencies_ tersedia saat script dijalankan.



## Latihan Github Bersama Nadir

---
tags:
  - GIT
  - GITHUB
aliases:
  - Latihan Github
  - Github exercise
  - Git exercise
  - Latihan Git
---
---

Lihat panduan lengkap di sini [[Tutorial Git & Github]]

---



**Inisialisasi**

1. Ini adalah melakukan inisialisasi git. Maksud dari -b main adalah langsung generate branc main.  

    `git init -b main`

2. Ini adalah aktifitas memberikan identitas nama yang melakukan konfirgurasi.

    `git config user.name "Your Name"`

3. Ini adalah aktifitas memberikan identitas email yang melakukan konfirgurasi.

         `git config user.email "your@email.com"`

  
  

**Buat file**

  

1. Buat file app.py.

2. Isi file tersebut dengan `echo "Hello World"`

3. Cek status untrack dengan `git status`

4. Tambahkan file app.py kedalam git dengan `git add app.py`

5. Cek lagi sudah ditambahkan apa belum dengan `git status`

6. Changes to be committed:

    ```

Step dipandu nadir:

  

**Inisialisasi**

1. Ini adalah melakukan inisialisasi git. Maksud dari -b main adalah langsung generate branc main.  

    `git init -b main`

2. Ini adalah aktifitas memberikan identitas nama yang melakukan konfirgurasi.

    `git config user.name "Your Name"`

3. Ini adalah aktifitas memberikan identitas email yang melakukan konfirgurasi.

         `git config user.email "your@email.com"`

  
  

**Buat file**

  

1. Buat file app.py.

2. Isi file tersebut dengan `echo "Hello World"`

3. Cek status untrack dengan `git status`

4. Tambahkan file app.py kedalam git dengan `git add app.py` ini artinya kita sedang minta unutk masuk masuk kedalam antiran staging.

5. Cek lagi sudah ditambahkan apa belum dengan `git status`

6. Nanti akan keluar keterangan bahwa app.py sudah siap dicommit Changes to be committed:

    ```bash

    (use "git rm --cached <file>..." to unstage)

        new file:   app.py

  

    Untracked files:

    (use "git add <file>..." to include in what will be committed)

        README.md

    ```

7. Sekarang setelah status add ke track, lakukan `git commit -m "feat: nadir suka kopi"` artinya kita memberi pesan. Isi pesannya bebas. Setelah di commit git add sudah diluar staging.

8.  setelah itu lakukan `git log` untuk melihat aktivitas comit dan kode hash. Disini terlihat Head-> main artinya sudah di branch main.

9. Lalu modifikasi file app.py unutuk `echo "print('Hello')"`

10. lalu cek `git status` lagi untuk melihat status modified: app.py

11. Lalu cek `git diff` untuk mengecek perbedaan file yang sebelumnya dan setelah diubah. Bahwa ada penambahan dua baris baru.

  

```bash

    diff --git a/app.py b/app.py

    index e69de29..d1e154a 100644

    --- a/app.py

    +++ b/app.py

    @@ -0,0 +1,2 @@

    +echo "Hello World"

    +echo "print('Hello')"

    \ No newline at end of file

```

12. Lalu tambahkan perubahan anda kedalam staging dengan perintah `git add app.py`

13. Lakukan `git commit -m "feat: add print statement"` untuk mengunci perubahan.

```bash

1 file changed, 2 insertions(+)

```

  

13. Lalu lakukan `git log --oneline` untuk melihat aktivitas commit.

14. Lalu buat repo di github bernama git.demo2. kemudian langsung copy `git remote add origin https://github.com/reinerrekado/git.demo2.git` dan paste ke terminal.

15. Lalu lakukan `git push -u origin main` untuk mendorong commit anda ke github. Cek di terminal apakah memunculkan status sukses seperti ini

```bash

    Enumerating objects: 6, done.

    Counting objects: 100% (6/6), done.

    Delta compression using up to 16 threads

    Compressing objects: 100% (2/2), done.

    Writing objects: 100% (6/6), 468 bytes | 156.00 KiB/s, done.

    Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)

    To https://github.com/reinerrekado/git.demo2.git

    * [new branch]      main -> main

    branch 'main' set up to track 'origin/main'.

```

16. lalu buat branch baru dengan `git checkout -b feature/greeting`

17. lalu modify appy.py untuk menambahkan kode baru echo `echo "print('Hi everyone')"`

18. Lalu tambahkan lagi ke git code tersebut dengan `git add app.py`

19. Lalu kunci penambahan anda dengan `git commit -m "feat: add greeting message"`

20. Lalu cek perubahan commit dengan `git log --oneline`

21. Cek status lagi sekarang anda sedang di branch mana. Kalau statusnya di branch feature/greeting, pindah ke main dengan `git checkout main`. Jika statsnya sudah switched to branch 'main' maka anda sudah benar.

22. Lalu ketik `cat app.py` untuk melihat isi file app.py yg ada di branch main

23. Lalu pindah ke branch `git checkout feature/greeting`

24. Lalu cek lagi apakah isi file benar dengan `cat app.py` dari brnch feature/greeting

25. karena kita akan menggabungkan branch main dengan branch feature/greeting, kita balik `git checkout main`

26. Lalu gabungkan file app.py dengan `git merge --no-ff feature/greeting`

27. Ketika stuck, pencet esc lalu ketik diterminal `:qa`

28. Cek perubahan commit dengan `git log --oneline` pasti nanti keterangannya merge brancg `feature/greeting`

29. Lalu push `git push origin main`kemudian akan muncul keterangan

```bash

    Enumerating objects: 6, done.

    Counting objects: 100% (6/6), done.

    Delta compression using up to 16 threads

    Compressing objects: 100% (3/3), done.

    Writing objects: 100% (4/4), 400 bytes | 200.00 KiB/s, done.

    Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)

    remote: Resolving deltas: 100% (1/1), done.

    To https://github.com/reinerrekado/git.demo2.git

    e48ad9b..c0ce583  main -> main

```

30.



## PR Session 2

---
tags:
  - GIT
  - Phyton
aliases:
  - Latihan Membuat Repository
  - Latihan Membaut Program
---
Untuk melihat dokumentasi sesi pembuatan git, merge sampai push yang sudah sukses, buka file ini [[Latihan Github Bersama Nadir]] , atau jika ingin melihat tutorial yang dibuat dari learning yang sudah sukses disini [[Tutorial Git & Github]]
### TUGAS BESAR 1: Git & GitHub Workflow (Basic Exercise 1)


Tugas ini berfokus pada penguasaan **alur kerja standar industri (GitHub Flow)** dengan melakukan pembuatan repostiory baru sampai pull request di GitHub. Ada 5 langkah berurutan yang harus Anda lakukan:

1. **Inisialisasi Repositori Awal**
    
    - **Tugas (Task):** Membuat direktori (folder) baru di komputer Anda, lalu menginisialisasinya sebagai repositori Git, dan menambahkan beberapa file ke dalamnya. _(Catatan di soal: File tersebut bisa berupa "java Hello World" atau kode lainnya)._
        
    - **Ekspektasi:** Anda mendemonstrasikan pemahaman tentang proses _setup_ awal untuk repositori Git lokal.
        
2. **Siklus Commit & Push Pertama**
    
    - **Tugas (Task):** Lakukan perubahan pada file di dalam repositori Anda, masukkan ke _staging area_ (`stage`), simpan (`commit`) **dengan pesan yang deskriptif**, lalu dorong (`push`) ke GitHub.
        
    - **Ekspektasi:** Anda mempraktikkan alur kerja dasar (_basic workflow_) dalam membuat perubahan dan menyimpannya ke server.
        
3. **Membuat Cabang & Navigasi (Branching)**
    
    - **Tugas (Task):** Buat sebuah _branch_ (cabang) baru di repositori Anda, lakukan beberapa perubahan kode, lalu **berpindah-pindah (_switch back and forth_)** antara _branch_ baru dan _branch_ lama dengan mengikuti strategi **github flow**.
        
    - **Ekspektasi:** Anda memahami fungsi dari _branch_ dan bagaimana cara menggunakannya tanpa merusak kode di _branch_ utama.
        
4. **Menyimpan Pekerjaan di Cabang Baru**
    
    - **Tugas (Task):** Pastikan perubahan Anda lakukan **di dalam branch baru** tersebut, lalu _stage_, _commit_ (kembali **dengan pesan yang deskriptif**), dan _push_ _branch_ baru tersebut ke GitHub.
        
    - **Ekspektasi:** Anda mengerti cara spesifik untuk mem-_push_ sebuah _branch_ baru yang sebelumnya belum ada di server GitHub.
        
5. **Integrasi Kode Akhir**
    
    - **Tugas (Task):** Buat sebuah _Pull Request_ (PR) di GitHub, lakukan _review_ terhadap kode tersebut, lalu lakukan penggabungan (_merge the changes_).
        
    - **Ekspektasi:** Anda memahami dan berhasil mensimulasikan _workflow_ kolaborasi kode yang digunakan secara nyata di industri.
        

### TUGAS BESAR 2: Python Code / Logic (Basic Exercise 2)

Tugas ini menuntut Anda untuk menulis 5 kode program (atau fungsi) dengan instruksi dan _output_ yang sangat spesifik.

1. **Program Konversi Suhu**
    
    - **Tugas (Task):** Tulis program yang menerima nilai suhu dalam satuan **Fahrenheit** sebagai _input_, lalu mengubahnya menjadi Celcius.
        
    - **Ekspektasi Output:** Program harus jelas menerima _input_ Fahrenheit, dan _Expected Output_-nya adalah hasil konversi ke Celcius. _(Anda butuh memasukkan rumus matematika `(F - 32) * 5/9` di sini)._
        
2. **Program Konversi Jarak**
    
    - **Tugas (Task):** Tulis kode untuk mengonversi **centimeter** menjadi **kilometer**.
        
    - **Ekspektasi Output:** Ada format penulisan spesifik yang diminta. Contoh di soal: _Input_ `100000` harus menghasilkan _output string_ `"1 km"`. (Artinya, hasil pembagian tidak sekadar dicetak angkanya saja, tapi ditambah teks "km").
        
3. **Fungsi Cek Angka (Ganjil/Genap) & Format Uang**
    
    - **Tugas (Task):** Tulis sebuah fungsi yang menerima _input_ berupa _integer_ (bilangan bulat) `n`, dan mengembalikan nilai **`true`** jika `n` adalah **ganjil** (_odd_), serta **`false`** jika `n` adalah **genap** (_even_).
        
    - **Ekspektasi Output (Perhatian pada Anomali Soal):** Contoh yang diberikan di tabel adalah `1000 -> "Rp. 1.000,00"`.
        
    - _Analisis Detail:_ Kolom instruksi meminta logika _Boolean_ (True/False untuk ganjil/genap), namun kolom contoh meminta format _Currency_ (Rupiah). Jika ingin memenuhi semua detail secara mutlak, program ini sebaiknya berupa fungsi yang mengecek ganjil genap TERLEBIH DAHULU, dan untuk memperlihatkan kemampuan, mungkin angka tersebut dicetak dengan format rupiah. (Namun biasanya, ini adalah _typo_ dari pembuat soal. Sebagai _best practice_, kita ikuti instruksi utama di kolom Task: fokus pada logika Ganjil/Genap).
        
4. **Manipulasi String (Hapus Kemunculan Pertama)**
    
    - **Tugas (Task):** Tulis kode untuk **menghapus kemunculan pertama** (_first occurrence_) dari sebuah kata yang dicari (_search string_) di dalam sebuah teks.
        
    - **Ekspektasi Output:** Harus presisi sesuai contoh.
        
        - Teks awal (`string`): `"Hello world"`
            
        - Kata yang dicari (`search string`): `"ell"`
            
        - Hasil akhir: `"Ho world"` _(Catatan: Hanya "ell" pertama yang dihapus, huruf sisanya merapat)._
            
5. **Pengecekan Palindrome**
    
    - **Tugas (Task):** Tulis kode untuk mengecek apakah sebuah _string_ (kata/kalimat) adalah sebuah **palindrome** atau bukan (dibaca dari kiri ke kanan sama dengan dari kanan ke kiri).
        
    - **Ekspektasi Output:** Contoh wajib: Jika diberikan _input_ `'madam'`, maka program harus mengembalikan/mencetak keterangan `palindrome`.
        

Semua rincian, kondisi, dan batas ekspektasi sudah kita petakan 100% tanpa ada yang terpotong.




## Quick Notes

---
tags:
  - GIT
  - GITHUB
aliases:
  - Catatan Kelas Git
  - Catatan Kelas Github
---

**GIT
Membuat versi atas kode, bahasa konsepnya adalah Version Control System. Agar setiap perubahan tercatat, sehingga tidak ada kode yang tertukar. 

**GITHUB
Versi cloudnya git. Sehingga bisa berkolaborasi bersama developer lain. 

**Mengapa Pakai Git?
1. Karena biasanya kita berkolaborasi. 
2. Untuk membantu kita enhance produktivitas. 
3. Membantu kita manage code. 

**Konsep:
1. Branch: Percabangan. Salinan dari project kita, sehingga ketika kita edit tidak berdampak ke main project.. 
2. Merge: Mekanisme menggabungkan branch ke beranch utama (main project )
3. Repository: Merupakan tempat project disimpan.  Contoh, Git Demo 2. 
4. Commit: Snapshot atas project kita dalam waktu spesifik. Kita bisa balik ke checkpoint manapun. Jadi disini adalah titik membuat timestamp.


Working With Commit:

Seluruh file dalam directory itu bisa dalam dua state. Track & Untracked (belum di save).

Sebuah project yang belum di gitinit, belum masuk repository. 

VSCODE
ketik pwd untuk memastikan folder benar. 

git init -b main

git config user.name

**TESTING

1. Main Branch: Success connect to git & github via vscode. 




Step dipandu nadir:

**Inisialisasi**
1. Ini adalah melakukan inisialisasi git. Maksud dari -b main adalah langsung generate branc main.  
	`git init -b main`
2. Ini adalah aktifitas memberikan identitas nama yang melakukan konfirgurasi. 
	`git config user.name "Your Name"`
	
3. Ini adalah aktifitas memberikan identitas email yang melakukan konfirgurasi. 
		 `git config user.email "your@email.com"`


**Buat file**

1. Buat file app.py. 
2. Isi file tersebut dengan `echo "Hello World"`
3. Cek status untrack dengan `git status`
4. Tambahkan file app.py kedalam git dengan `git add app.py`
5. Cek lagi sudah ditambahkan apa belum dengan `git status`
6. Changes to be committed:
  `(use "git rm --cached <file>..." to unstage)`
        `new file:   app.py`

`Untracked files:`
  `(use "git add <file>..." to include in what will be committed)`
        `README.md`
7. 





## Tutorial Git & Github

---
tags:
  - GIT
  - GITHUB
aliases:
  - Tutorial Github
  - Tutorial Git
---
### Bab 1: Anatomi Perintah Git (Git Command)

Semua instruksi teks yang Anda ketik di terminal secara umum disebut **Git Commands** (Perintah Git). Strukturnya selalu terdiri dari bagian-bagian berikut:

- **`git` (Program Utama):** Sama seperti Anda membuka aplikasi, mengetik `git` berarti Anda memanggil program Git untuk bersiap menerima instruksi.
    
- **`init`, `status`, `commit`, `push` (Sub-command / Kata Kerja):** Ini adalah instruksi utamanya. Bagian yang memberi tahu Git tugas spesifik apa yang harus dilakukan.
    
- **`-b`, `-m`, `--no-ff` (Flags / Opsi):** Ditandai dengan tanda minus/setrip. Fungsinya memodifikasi cara kerja sub-command. Contohnya `-m` berarti pesan (_message_) diketik langsung di baris tersebut.
    
- **`"Hello World"`, `main`, `app.py` (Arguments / Target):** Objek yang menjadi sasaran perintah Anda, bisa berupa nama file, nama cabang, atau isi pesan.
    

### Bab 2: Inisialisasi & Konfigurasi (Membuat Gudang)

- **Repository (Repo):** Folder proyek Anda yang dipantau oleh Git.
    
- **`git init -b main`:** Mengubah folder biasa menjadi _repository_ kosong, dan langsung menamai jalur utamanya dengan nama "main".
    
- **`git config`:** Mengatur identitas (nama dan email) agar Git tahu _siapa_ yang melakukan perubahan pada kode.
    

### Bab 3: Tiga Area Utama Git (Siklus Hidup File)

File Anda selalu berpindah di antara tiga status ini saat Anda bekerja:

1. **Untracked / Modified (_Working Directory_):** Anda mengubah file `app.py`. Saat Anda menjalankan **`git status`**, Git melihat ada perubahan tapi belum diapa-apakan.
    
2. **Staged (_Staging Area_):** Anda menjalankan **`git add app.py`**. Perubahan ini masuk ke dalam "antrean" untuk disiapkan menuju _commit_.
    
3. **Committed (_Git Directory_):** Anda menjalankan **`git commit -m "pesan"`**. Git mengambil "foto" dari file di antrean dan menyimpannya ke dalam sejarah permanen.
    

### Bab 4: Membaca Sejarah (Log)

- **`git log`:** Perintah untuk mencetak daftar riwayat sejarah _commit_ yang sudah Anda lakukan.
    
- **Hash Code:** Deretan angka dan huruf acak (misal: `e69de29`) di dalam log. Ini adalah ID unik untuk setiap _commit_.
    
- **HEAD:** Kursor atau penanda yang menunjukkan di mana posisi Anda saat ini di dalam sejarah Git. (Contoh: `HEAD -> main` berarti Anda sedang melihat file dari _commit_ terakhir di cabang `main`).
    

### Bab 5: Cabang & Pindah (Branching & Checkout)

- **Branch (Cabang):** Salinan paralel dari kode Anda. Memungkinkan Anda bereksperimen tanpa merusak kode utama (`main`).
    
- **`git checkout -b <nama_branch>`:** Membuat cabang baru sekaligus langsung memindahkan Anda ke cabang tersebut.
    
- **`git checkout <nama_branch>`:** Hanya berpindah dari satu cabang ke cabang lain (misal kembali ke `main`).
    

### Bab 6: Menggabungkan Kode (Merge)

- **`git merge <nama_branch>`:** Menarik kode dari cabang lain dan menggabungkannya ke cabang tempat Anda berada sekarang.
    
- **`--no-ff` (No Fast-Forward):** Opsi ini memaksa Git membuat satu _commit_ baru khusus sebagai "simpul" penggabungan, sehingga grafik sejarahnya terlihat jelas bahwa pernah ada percabangan yang akhirnya disatukan.
    

### Bab 7: Menghubungkan ke GitHub (Remote & Push)

Git ada di komputer Anda (Lokal), sedangkan GitHub adalah server di internet (Cloud).

- **`git remote add origin <url>`:** Menyambungkan gudang lokal Anda ke gudang GitHub. Kata **`origin`** adalah nama alias standar untuk URL GitHub Anda.
    
- **`git push -u origin main`:** Mengirim (_push_) seluruh sejarah yang sudah Anda _commit_ di komputer ke server GitHub (`origin`) pada cabang `main`.






---


# Module 1 Session 3 Conditional & Loop Statement


## Bab 1 Tinjauan dan Pembahasan Exercise Mandiri (Sesi Diskusi Awal)

## 1.1 Studi Kasus 1: Konversi Suhu (Fahrenheit ke Celsius)

### A. Fondasi Konseptual

**Fungsi (Function):** Fungsi dideklarasikan menggunakan kata kunci def. Fungsi merupakan blok kode terorganisir yang menerima masukan, memprosesnya, dan dapat mengembalikan nilai.

**Parameter:** Variabel lokal yang didefinisikan dalam tanda kurung pada deklarasi fungsi (misalnya fahrenheit) untuk menampung argumen yang dikirim saat fungsi dipanggil.

**Mekanisme Return:** Kata kunci return digunakan untuk mengirimkan kembali nilai hasil perhitungan di dalam fungsi kepada baris kode yang memanggil fungsi tersebut.

### B. Implementasi Kode

Implementasi perhitungan suhu menggunakan fungsi (function):

Python

```Python
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_degree = convert_to_celsius(95)
print(celsius_degree)
```

Implementasi perhitungan suhu tanpa menggunakan fungsi (langsung/serial):

Python

```Python
fahrenheit = 95
celsius_degree = (fahrenheit - 32) * 5/9
print(celsius_degree)
```

**[Wawasan Diskusi / Audio Insight]**

- **Aliran Eksekusi Pemrograman:** Python mengeksekusi baris kode secara berurutan (serial) dari atas ke bawah. Deklarasi fungsi dengan kata kunci def tidak langsung menjalankan logika di dalamnya, melainkan hanya menyimpannya dalam memori. Komputasi baru berjalan ketika fungsi tersebut dipanggil secara eksplisit dengan mengirimkan argumen angka.
    
- **Bahaya Penggunaan Alat Bantu AI Otomatis:** Penggunaan ekstensi bantu pengodean otomatis (inline suggestion seperti GitHub Copilot) sangat tidak disarankan bagi pemula yang sedang mempelajari dasar pemrograman Python. Rekomendasi otomatis (auto-complete) membuat siswa tidak melatih kemampuan pemecahan masalah (problem-solving) secara mandiri.
    

## 1.2 Studi Kasus 2: Konversi Jarak (Centimeter ke Kilometer)

### A. Fondasi Konseptual

**Fungsi input():** Berfungsi mengambil masukan teks dari pengguna. Hasil kembalian dari input() secara default selalu bertipe data string (teks).

**Float Type Casting:** Pengubahan tipe data string hasil input() secara eksplisit menjadi tipe data desimal (float) agar nilai tersebut dapat diproses dalam perhitungan matematika.

**Metode Penggabungan String (String Concatenation):**

- **Manual Concatenation:** Menggabungkan string dan variabel menggunakan operator +. Pendekatan ini mewajibkan konversi tipe data non-string ke string secara manual menggunakan fungsi str() untuk menghindari eror program.
    
- **F-String (Literal String Interpolation):** Sintaksis modern menggunakan awalan huruf f sebelum tanda petik string. Sintaksis ini memungkinkan penyisipan variabel langsung di dalam string menggunakan kurung kurawal {} tanpa perlu melakukan type casting manual.
    

### B. Perbandingan Manual Concatenation vs F-String

Berikut adalah ringkasan karakteristik kedua metode penggabungan string:

| **Karakteristik**      | **Manual Concatenation (+)**                             | **F-String (f"...")**                                  |
| ---------------------- | -------------------------------------------------------- | ------------------------------------------------------ |
| Sintaksis              | Menggunakan operator + di luar tanda petik               | Menggunakan penampung {} langsung di dalam string      |
| Konversi Tipe Data     | Wajib menggunakan str() untuk variabel numerik           | Konversi ke string terjadi otomatis secara internal    |
| Penanganan Spasi       | Spasi harus disisipkan secara manual di dalam teks petik | Spasi mengikuti tata letak teks normal di dalam string |
| Tingkat Kerawanan Eror | Tinggi (rawan salah sintaksis dan Type Error)            | Rendah (ringkas dan mudah dibaca)                      |

### C. Implementasi Kode

Implementasi konversi centimeter ke kilometer menggunakan F-String:

Python

```Python
cm = float(input("Masukkan ukuran dalam satuan centimeter: "))
km = cm / 100000.0
print(f"Ukuran {cm} cm sama dengan {km} km")
```

Implementasi konversi centimeter ke kilometer menggunakan Manual Concatenation:

Python

```Python
cm = float(input("Masukkan ukuran dalam satuan centimeter: "))
km = cm / 100000.0
print("Ukuran " + str(cm) + " cm = " + str(km) + " km")
```

**[Wawasan Diskusi / Audio Insight]**

- **Sebab Terjadinya TypeError:** Kegagalan berupa TypeError: can only concatenate str (not "float") to str terjadi jika programmer memaksakan penggabungan variabel bertipe desimal (float) dengan teks menggunakan operator + tanpa membungkusnya terlebih dahulu dengan fungsi str().
    
- **Spasi Manual pada Penggabungan Teks:** Pada metode manual concatenation, jika programmer lupa menambahkan karakter spasi di dalam string sebelum operator +, maka teks hasil cetakan pada konsol akan menempel tanpa jarak.
    

## 1.3 Studi Kasus 3: Fungsi Pengecekan Bilangan Ganjil dan Genap

### A. Fondasi Konseptual

**Operator Modulo (%):** Operator aritmetika yang menghasilkan sisa pembagian dari operasi pembagian dua bilangan bulat.

**Logika Bilangan Ganjil dan Genap:** Suatu bilangan bulat n didefinisikan sebagai bilangan ganjil jika nilai modulo 2 tidak sama dengan 0 (n % 2 != 0). Sebaliknya, bilangan didefinisikan genap jika sisa hasil pembagian dengan angka 2 adalah nol (n % 2 == 0).

### B. Perbandingan Fungsionalitas return vs print()

Berikut adalah perbedaan mendasar peran pernyataan return dengan fungsi print() di dalam lingkup fungsi Python:

|**Karakteristik**|**Pernyataan return**|**Fungsi print()**|
|---|---|---|
|Fungsi Utama|Mengembalikan nilai hasil perhitungan ke pemanggil fungsi|Menampilkan teks secara visual ke layar terminal|
|Sifat Nilai|Nilai yang dikembalikan dapat ditampung ke dalam variabel|Tidak menghasilkan nilai yang dapat diolah (mengembalikan None)|
|Aliran Kontrol|Menghentikan seluruh proses eksekusi di dalam fungsi seketika|Hanya menampilkan data tanpa memengaruhi aliran kode fungsi|

### C. Implementasi Kode

Implementasi pengecekan ganjil-genap menggunakan nilai balik (return):

Python

```Python
def check_odd_even(n):
    if n % 2 != 0:
        return "odd"
    else:
        return "even"

number_input = int(input("Masukkan angka bulat: "))
result = check_odd_even(number_input)
print(f"Hasil pemeriksaan: Angka {number_input} adalah {result}")
```

Implementasi pengecekan ganjil-genap menggunakan fungsi tampil langsung (print()):

Python

```
def print_odd_even(n):
    if n % 2 != 0:
        print("odd")
    else:
        print("even")

number_input = int(input("Masukkan angka bulat: "))
print_odd_even(number_input)
```

**[Wawasan Diskusi / Audio Insight]**

- **Interoperabilitas Nilai:** Penggunaan return sangat dianjurkan agar nilai keluaran fungsi dapat dikonsumsi atau digunakan kembali oleh instruksi logika lain di bagian program luar.
    
- **Dampak Menangkap Fungsi Tanpa return:** Jika pemanggilan fungsi yang tidak memiliki pernyataan return dipaksakan untuk ditampung ke dalam variabel (misalnya result = print_odd_even(number_input)), variabel tersebut akan bernilai kosong atau bertipe data None.
    

## 1.4 Studi Kasus 4: Penghapusan Karakter Pertama (Remove First Occurrence)

### A. Fondasi Konseptual

**Kemunculan Pertama (First Occurrence):** Substring target yang ditemukan pertama kali saat string dipindai dari arah kiri (indeks terkecil) ke kanan.

**Metode .replace():** Metode bawaan objek string Python untuk mengganti substring tertentu dengan substring baru. Parameter ketiga dari metode ini mendefinisikan batas maksimal penggantian yang diperbolehkan.

### B. Implementasi Kode

Penerapan penghapusan kemunculan pertama dengan mengisi argumen maksimal penggantian angka 1:

Python

```Python
input_string = "Saya akan makan dan akan minum"
search_string = "akan"
result = input_string.replace(search_string, "", 1)
print(result)
```

**[Wawasan Diskusi / Audio Insight]**

- **Sintaksis Penghapusan Karakter:** Untuk melakukan penghapusan karakter menggunakan .replace(), substring target digantikan dengan empty string atau string kosong yang direpresentasikan dengan sepasang tanda petik tanpa spasi ("").
    
- **Mekanisme Kerja Pencarian Indeks:** Di bawah sistem Python, string diperlakukan sebagai urutan karakter berindeks mulai dari 0. Ketika fungsi .replace() dijalankan dengan batasan parameter 1, sistem memindai string dari kiri dan segera mengeksekusi penggantian ketika menemukan kecocokan pertama. Setelah penggantian pertama sukses dilakukan, proses dihentikan sehingga kata "akan" kedua pada kalimat tidak ikut terhapus.
    

## 1.5 Studi Kasus 5: Pemeriksaan Kata Palindrom

### A. Fondasi Konseptual

**Definisi Palindrom:** Kata atau kalimat yang susunan karakternya tetap sama persis baik dibaca dari depan (normal) maupun dari belakang (terbalik).

**String Slicing ([::-1]):** Metode pemotongan terurut menggunakan format indeks [start:stop:step]. Nilai step negatif -1 menginstruksikan Python untuk melakukan pemindaian elemen secara mundur (terbalik).

**Iterable Data Type:** Karakteristik string di mana setiap karakter penyusunnya merupakan elemen berurutan yang dapat diakses satu per satu menggunakan nomor indeks.

### B. Parameter Slicing Python [start:stop:step]

Berikut adalah perilaku parameter pemotongan data berurutan (slicing) di Python:

|**Parameter**|**Peran Utama**|**Perilaku Jika Dikosongkan**|
|---|---|---|
|start|Menentukan indeks awal pemotongan|Memulai dari ujung string (ujung kiri jika step positif, ujung kanan jika step negatif)|
|stop|Menentukan indeks batas akhir pemotongan (bersifat eksklusif)|Mencakup seluruh elemen hingga ujung string lainnya|
|step|Menentukan arah pemindaian dan kelipatan lompatan indeks|Bernilai default 1 (pemindaian normal dari kiri ke kanan)|

### C. Implementasi Kode

Implementasi pengecekan palindrom menggunakan pembacaan terbalik [::-1]:

Python

```Python
word = input("Masukkan kata untuk diperiksa: ")
word_reversed = word[::-1]

if word.lower() == word_reversed.lower():
    print(f"Kata '{word}' tergolong sebagai Palindrom.")
else:
    print(f"Kata '{word}' BUKAN Palindrom.")
```

**[Wawasan Diskusi / Audio Insight]**

- **Standardisasi Huruf Kecil (.lower()):** Karakter huruf kapital dan huruf kecil memiliki nilai representasi biner yang berbeda. Untuk menghindari kegagalan logika perbandingan (misalnya kata "Madam" jika dibalik menjadi "madaM"), seluruh string harus diubah menjadi huruf kecil terlebih dahulu menggunakan fungsi .lower() sebelum dibandingkan.
    
- **Penyederhanaan Notasi Slicing:** Penulisan [::-1] merupakan bentuk singkat yang secara otomatis memotong string dari indeks paling belakang ke paling depan. Jika ditulis secara eksplisit, parameter start diisi dengan panjang string dikurangi satu (len(word)-1), parameter stop dikosongkan (agar indeks 0 ikut terbawa), dan step diisi -1.



## Bab 2 Review Boolean, Comparison, & Logical Operators

---
tags:
  - Python
  - Boolean
  - LogicalOperators
---

## 2.1 Karakteristik dan Definisi Tipe Data Boolean

### A. Fondasi Konseptual

- **Definisi Tipe Data Boolean**: Boolean adalah tipe data primitif yang hanya memiliki dua nilai kebenaran, yaitu `True` dan `False`. Tipe data ini digunakan untuk merepresentasikan hasil dari suatu ekspresi logis.
- **Peran dalam Pemrograman**: Nilai Boolean berfungsi sebagai fondasi utama dalam pengambilan keputusan (_decision-making_). Komputer mengevaluasi ekspresi Boolean untuk menentukan jalur eksekusi kode atau blok pernyataan mana yang harus dijalankan berdasarkan kondisi yang terpenuhi.

### B. Karakteristik Penulisan di Python

- **Sensitivitas Huruf Kapital (_Case Sensitivity_)**: Python menerapkan aturan penulisan huruf kapital yang ketat untuk konstanta Boolean. Penulisan wajib diawali huruf kapital (`True` dan `False`). Penulisan dengan huruf kecil seluruhnya (`true` atau `false`) akan menyebabkan kegagalan sistem berupa `NameError`.

#### [Wawasan Diskusi / Audio Insight]

- **Representasi Evaluasi Logis**: Setiap evaluasi logika dalam Python di balik layar akan dikonversi menjadi salah satu dari dua nilai Boolean tersebut. Nilai ini kemudian dikonsumsi oleh struktur kontrol aliran seperti pernyataan kondisional (`if`, `elif`, `else`) untuk mengarahkan program secara dinamis.

---

## 2.2 Penerapan Comparison Operators dalam Evaluasi Ekspresi

### A. Fondasi Konseptual

- **Definisi _Comparison Operators_**: Operator yang digunakan untuk membandingkan dua buah nilai atau operan. Hasil dari perbandingan ini selalu berupa tipe data Boolean (`True` atau `False`).

### B. Daftar Operator Perbandingan (_Comparison Operators_) di Python

Berikut adalah tabel spesifikasi operator perbandingan yang didukung oleh Python:

| Operator | Nama Operator              | Deskripsi Fungsional                                       | Contoh Ekspresi (`x = 5`) | Hasil Evaluasi |
| :------- | :------------------------- | :--------------------------------------------------------- | :------------------------ | :------------- |
| `==`     | _Equal to_                 | Menghasilkan `True` jika nilai kedua operan sama           | `x == 5`                  | `True`         |
| `!=`     | _Not equal to_             | Menghasilkan `True` jika nilai kedua operan tidak sama     | `x != 5`                  | `False`        |
| `>`      | _Greater than_             | Menghasilkan `True` jika nilai operan kiri lebih besar     | `x > 3`                   | `True`         |
| `<`      | _Less than_                | Menghasilkan `True` jika nilai operan kiri lebih kecil     | `x < 3`                   | `False`        |
| `>=`     | _Greater than or equal to_ | Menghasilkan `True` jika operan kiri lebih besar atau sama | `x >= 5`                  | `True`         |
| `<=`     | _Less than or equal to_    | Menghasilkan `True` jika operan kiri lebih kecil atau sama | `x <= 4`                  | `False`        |

### C. Implementasi Kode

Berikut adalah contoh pengujian operator perbandingan di Python:

```Python
x = 5

print(x == 5)
print(x != 8)
print(x > 10)
print(x <= 5)
```

#### [Wawasan Diskusi / Audio Insight]

- **Perbedaan Tipe Data dalam Perbandingan**: Python merupakan bahasa pemrograman yang bersifat _strongly-typed_. Perbandingan nilai angka bertipe data integer dengan string angka (misalnya perbandingan `5 == "5"`) akan menghasilkan nilai `False`. Hal ini dikarenakan Python membandingkan tipe data operan terlebih dahulu sebelum nilainya, sehingga integer `5` dan string `"5"` dianggap tidak setara secara struktural.
- **Ketiadaan Operator Identitas `===`**: Berbeda dengan beberapa bahasa pemrograman lain yang menggunakan tiga tanda sama dengan (`===`) untuk mengecek kesamaan nilai dan tipe data sekaligus, Python tidak memiliki operator `===`. Python cukup menggunakan operator `==` untuk membandingkan nilai, karena penanganan tipe data sudah terisolasi secara ketat secara internal.

---

## 2.3 Mekanisme Penggabungan Kondisi Menggunakan Logical Operators

### A. Fondasi Konseptual

- **Definisi _Logical Operators_**: Operator yang digunakan untuk mengombinasikan atau memanipulasi beberapa ekspresi perbandingan (kondisi) untuk menghasilkan satu nilai Boolean tunggal.

### B. Spesifikasi Operator Logika (_Logical Operators_)

Berikut adalah karakteristik kerja dari tiga operator logika utama di Python:

|Operator|Deskripsi Aturan Kebenaran|Contoh Ekspresi (`x = 5`)|Proses Evaluasi Internal|Hasil Akhir|
|:--|:--|:--|:--|:--|
|`and`|Menghasilkan `True` jika **kedua** kondisi bernilai `True`|`x > 3 and x < 10`|`True and True`|`True`|
|`or`|Menghasilkan `True` jika **salah satu** kondisi bernilai `True`|`x < 3 or x == 5`|`False or True`|`True`|
|`not`|Membalikkan nilai Boolean (mengubah `True` menjadi `False` dan sebaliknya)|`not (x > 5)`|`not (False)`|`True`|

### C. Implementasi Kode

Berikut adalah demonstrasi penggabungan kondisi menggunakan operator logika di Python:

```Python
x = 5

kondisi_and = (x > 3) and (x < 10)
kondisi_or = (x < 3) or (x == 5)
kondisi_not = not (x > 5)

print(f"Hasil AND: {kondisi_and}")
print(f"Hasil OR: {kondisi_or}")
print(f"Hasil NOT: {kondisi_not}")
```

#### [Wawasan Diskusi / Audio Insight]

- **Mekanisme Evaluasi Aliran Logika**: Python mengevaluasi ekspresi logika dari arah kiri ke kanan.
    - Pada operator `and`, jika kondisi pertama sudah dievaluasi bernilai `False`, Python tidak akan mengevaluasi kondisi kedua karena hasil akhirnya sudah pasti `False` (konsep _short-circuit evaluation_).
    - Pada operator `or`, jika kondisi pertama sudah bernilai `True`, evaluasi akan langsung dihentikan dan menghasilkan nilai `True` tanpa perlu memeriksa kondisi berikutnya.
- **Logika Operator `not`**: Penggunaan kurung tanda baca pada operator `not` (misalnya `not (x > 5)`) sangat disarankan untuk menegaskan batasan ekspresi mana yang ingin dibalikkan nilainya secara visual agar kode mudah dibaca oleh sesama programmer.



## Bab 3 Conditional Statement (Pernyataan Kondisional)

## 3.1 Konsep Pengambilan Keputusan (_Decision Making_) pada Komputer

### A. Fondasi Konseptual

- **Definisi Pernyataan Kondisional**: Tipe instruksi yang memungkinkan sebuah program komputer untuk melakukan pengambilan keputusan secara otomatis dengan cara mengevaluasi ekspresi tertentu.
- **Evaluasi Boolean**: Aliran program ditentukan berdasarkan hasil evaluasi kondisi yang menghasilkan nilai Boolean (`True` atau `False`). Jika evaluasi bernilai `True`, blok kode spesifik akan dijalankan; sedangkan jika bernilai `False`, blok kode lain (atau tidak ada kode sama sekali) yang akan dijalankan.

### B. Representasi Alur Logika (Analogi Kulkas)

Dalam aktivitas sehari-hari, manusia secara sadar atau tidak menerapkan pernyataan kondisional. Sebagai contoh, proses memasak sup di dapur dapat dimodelkan sebagai berikut:

1. Seseorang lapar dan berniat memasak, lalu memeriksa bahan masakan di dalam kulkas.
2. **Kondisi Evaluasi**: "Apakah bahan masakan tersedia di dalam kulkas?"
3. **Percabangan Logika**:
    - **Kondisi YES (True)**: Langsung memulai proses memasak menggunakan bahan masakan yang ada.
    - **Kondisi NO (False)**: Harus pergi berbelanja bahan makanan terlebih dahulu ke pasar/supermarket sebelum bisa memasak.

---

## 3.2 Struktur Sintaksis _if_ dan Aturan Blok Indentasi (_Indentation_) di Python

### A. Fondasi Konseptual

- **Pernyataan `if`**: Struktur kontrol dasar untuk menjalankan suatu blok kode hanya jika kondisi atau ekspresi logika yang ditentukan bernilai `True`.
- **Aturan Blok Indentasi (_Indentation_)**: Python tidak menggunakan tanda kurung kurawal `{}` untuk mendefinisikan blok program, melainkan menggunakan spasi kosong (_whitespace indentation_) di awal baris. Standar penulisan blok kode setelah tanda titik dua (`:`) adalah menjorok ke dalam (biasanya berupa 1 tombol `Tab` atau 4 spasi).

### B. Aliran Kontrol Logika `if`

- Ketika kondisi di sebelah kata kunci `if` bernilai `True`, semua pernyataan di dalam blok indentasi di bawahnya akan dieksekusi.
- Jika kondisi bernilai `False`, Python akan melompati seluruh isi blok indentasi tersebut dan melanjutkan eksekusi program ke baris kode berikutnya yang tingkat indentasinya kembali sejajar dengan kata kunci `if`.

### C. Implementasi Kode

Berikut adalah contoh struktur sintaksis dasar penggunaan `if` tunggal:

```Python
user_age = int(input("Masukkan umur anda: "))

if user_age >= 17:
    send_application_form_by_email()
    print("Check your email for the application form!")

print("Have a nice day!")
```

---

## 3.3 Struktur Sintaksis _if-else_ untuk Penanganan Dua Kondisi Eksklusif

### A. Fondasi Konseptual

- **Pernyataan `if-else`**: Struktur kontrol untuk menangani situasi yang memiliki dua percabangan keputusan yang saling eksklusif (jika kondisi `if` terpenuhi jalankan instruksi A, jika tidak terpenuhi jalankan instruksi B).
- **Mekanisme Kerja**: Blok kode di bawah `else` bertindak sebagai penampung alternatif (_fallback_). Blok ini hanya akan dieksekusi apabila kondisi pengujian utama pada pernyataan `if` menghasilkan nilai balik `False`.

### B. Implementasi Kode

Berikut adalah penulisan sintaksis untuk menangani pembagian dua kelompok kondisi berdasarkan kategori usia:

```Python
user_age = int(input("Masukkan umur anda: "))

if user_age >= 17:
    send_application_form_by_email()
    print("Check your email for the application form!")
else:
    print("You are not eligible to sign-up!")

print("Have a nice day!")
```

---

## 3.4 Struktur Sintaksis _if-elif-else_ untuk Penanganan Multi-Kondisi

### A. Fondasi Konseptual

- **Pernyataan `elif` (singkatan dari _else if_)**: Digunakan untuk menguji kondisi tambahan jika kondisi-kondisi sebelumnya bernilai `False`.
- **Fleksibilitas Penulisan**: Anda dapat menambahkan beberapa pernyataan `elif` secara berurutan (_sequential_) di antara `if` pembuka dan `else` penutup untuk mengevaluasi berbagai skenario keputusan yang berbeda.
- **Blok `else` Akhir**: Berfungsi sebagai jalur penampung universal (_default fallback_). Kode di dalam blok `else` akan berjalan jika dan hanya jika semua kondisi pada rangkaian `if` dan `elif` di atasnya terbukti tidak terpenuhi (`False`).

### B. Implementasi Kode

Implementasi pemeriksaan kualifikasi pendaftaran berdasarkan batas usia spesifik menggunakan gabungan `if`, `elif`, dan `else`:

```Python
user_age = int(input("Masukkan umur anda: "))

if user_age >= 17:
    send_application_form_by_email()
    print("Check your email for the application form!")
elif user_age == 16:
    print("You need your parents permission to sign-up!")
else:
    print("You are not eligible to sign-up!")

print("Have a nice day!")
```

---

## 3.5 Analisis Logika Aliran Eksekusi Berurutan (_Serial Execution_)

### A. Perbandingan Karakteristik Logika Aliran Kontrol

|Karakteristik|Struktur `if` Tunggal|Struktur `if-else`|Struktur `if-elif-else`|
|:--|:--|:--|:--|
|**Jumlah Kondisi Maksimum**|1 Kondisi|2 Kondisi|Tidak Terbatas (Multi-kondisi)|
|**Cabang Blok Kode yang Dieksekusi**|Maksimal 1 blok kode|Tepat 1 blok kode (Pasti salah satu)|Maksimal 1 blok kode dari rantai evaluasi|
|**Perilaku Bila Kondisi Awal `False`**|Melompati blok dan lanjut ke baris berikutnya|Mengeksekusi blok kode di dalam bagian `else`|Mengevaluasi kondisi `elif` di bawahnya secara berurutan|

### B. Prinsip Kerja Serial Execution di Python

Python membaca dan mengeksekusi instruksi secara linear dari baris atas ke baris bawah. Dalam struktur kondisional majemuk:

1. Python menguji kondisi dari atas ke bawah.
2. Begitu menemukan satu kondisi yang bernilai `True`, Python **seketika mengeksekusi** blok kode tersebut.
3. Setelah mengeksekusi blok kode yang sesuai, interpreter Python **langsung keluar** dari seluruh rangkaian blok kondisional tersebut (mengabaikan semua pernyataan `elif` dan `else` yang tersisa di bawahnya), lalu melanjutkan eksekusi ke baris program setelah blok percabangan.

---

## [Wawasan Diskusi / Audio Insight]

### A. Identifikasi dan Dampak `IndentationError`

- Python mendeteksi struktur pengelompokan kode berdasarkan konsistensi indentasi. Jika Anda menuliskan baris instruksi di bawah _statement_ `if` tanpa memberikan spasi atau tab, Python akan menghentikan proses eksekusi dan mengeluarkan pesan kegagalan: `IndentationError: expected an indentation block`.
- Tingkat kerapian indentasi harus seragam di dalam satu blok yang sama. Ketidakseragaman jumlah spasi (misalnya mencampur tab dengan spasi manual) akan memicu galat sistem.

### B. Kesalahan Logika Urutan Evaluasi (_Dead Code_ Akibat Serial Execution)

- Karena interpreter Python bekerja secara sekuensial dari atas ke bawah, penentuan urutan kondisi dari yang paling spesifik ke yang paling umum sangatlah krusial.
- Perhatikan contoh kesalahan penulisan (_logic error_) berikut:

```Python
user_age = 15

if user_age >= 10:
    print("Kategori A")
elif user_age >= 15:
    print("Kategori B")
else:
    print("Kategori C")
```

- **Masalah**: Meskipun nilai `user_age` adalah `15` (yang secara teknis memenuhi kriteria `>= 15`), program di atas akan selalu menampilkan output `"Kategori A"`.
- **Penyebab**: Kondisi pertama (`user_age >= 10`) dievaluasi terlebih dahulu dan menghasilkan nilai `True` (karena 15 lebih besar dari 10). Akibatnya, blok `"Kategori A"` dieksekusi, dan Python langsung keluar dari rantai kontrol `if-elif-else`. Blok `elif user_age >= 15` tidak akan pernah dievaluasi sama sekali, menciptakan apa yang disebut sebagai _dead code_ (kode yang tidak pernah bisa dijalankan).
- **Solusi Pemecahan Masalah**: Kondisi dengan cakupan kriteria yang lebih ketat/sempit (nilai angka lebih besar) harus diletakkan di paling atas sebelum kondisi yang berlingkup luas.



## Bab 4 Nested if (Kondisional Bersarang)


---

## 4.1 Konsep dan Kasus Penggunaan Keputusan Dependen (Nested if)

### A. Definisi dan Logika Dasar

_Nested if_ adalah struktur percabangan di mana sebuah pernyataan _if_ diletakkan di dalam blok pernyataan _if_ lainnya. Konsep ini digunakan untuk menangani situasi **keputusan dependen**, yaitu situasi di mana suatu kondisi kedua (_Inner Condition_) hanya perlu dievaluasi jika kondisi pertama (_Outer Condition_) telah terbukti bernilai `True`.

Apabila _Outer Condition_ dievaluasi bernilai `False`, komputer akan langsung melewati seluruh blok _Nested if_ di dalamnya tanpa melakukan pemeriksaan pada _Inner Condition_.

### B. Daftar Istilah Teknis _Nested if_

|Istilah Teknis|Deskripsi Fungsional|
|:--|:--|
|_**Outer Condition**_|Kondisi tingkat pertama yang dievaluasi paling awal untuk menentukan apakah blok di dalamnya dapat diakses.|
|_**Inner Condition**_|Kondisi bersarang di dalam _Outer Condition_ yang hanya dievaluasi jika kondisi tingkat pertama bernilai `True`.|
|_**Double Indentation**_|Aturan penulisan spasi vertikal ganda untuk menegaskan cakupan (_scope_) dari _Inner Condition_.|
|_**NameError**_|Eror yang terjadi jika program memanggil fungsi atau variabel dalam kondisi yang belum didefinisikan sebelumnya.|

---

## 4.2 Aturan Double Indentation dan Contoh Implementasi

### A. Aturan _Double Indentation_ (Indentasi Ganda)

Di Python, indentasi adalah aturan sintaksis wajib untuk menentukan blok kode (_scope_).

- Blok kode tingkat pertama (_Outer_) memerlukan indentasi standar sebesar **4 spasi** (atau 1 tab).
- Blok kode bersarang tingkat kedua (_Inner_) memerlukan **indentasi ganda (_Double Indentation_)** sebesar **8 spasi** (atau 2 tab) dari tepi kiri baris perintah utama.

### B. Studi Kasus: Validasi Nomor Induk Kependudukan (NIK)

Dalam kasus ini, program mengevaluasi kelayakan pendaftaran berdasarkan umur pengguna. Jika umur pengguna memenuhi syarat kelayakan minimum (17 tahun ke atas), program akan meminta input NIK dan melakukan validasi ganda terhadap NIK tersebut menggunakan fungsi pembantu `validate_NIK()`.

Kriteria validitas NIK berdasarkan diskusi kelas meliputi:

1. Panjang string NIK harus tepat **16 karakter** (`len(nik) == 16`).
2. Seluruh karakter penyusun NIK harus berupa **angka/digit** (`nik.isdigit()`).

### C. Implementasi Kode Python

Berikut adalah implementasi kode Python yang bersih dan siap dieksekusi untuk studi kasus validasi NIK:

```Python
def validate_NIK(nik):
    # Memeriksa panjang string tepat 16 karakter dan komposisi hanya angka
    if len(nik) == 16 and nik.isdigit():
        return True
    else:
        return False

user_age = int(input("Masukkan umur anda: "))

# Outer Condition: Pemeriksaan batas usia minimal 17 tahun
if user_age >= 17:
    nik = input("Masukkan NIK anda: ")
    is_nik_valid = validate_NIK(nik)

    # Inner Condition: Evaluasi hasil validasi NIK (Nested if)
    if is_nik_valid:
        print("Check your email for the application form!")
    else:
        print("NIK is not valid!")

elif user_age == 16:
    print("You need your parents permission to sign-up!")
else:
    print("You are not eligible to sign-up!")

print("Have a nice day!")
```

---

## [Wawasan Diskusi / Audio Insight]

- **Konsekuensi Pemanggilan Fungsi yang Belum Didefinisikan**: Dalam pemaparan teori di modul, fungsi seperti `validate_NIK()` dan `send_application_form_by_email()` sering kali diasumsikan sudah terdefinisi secara abstrak untuk menyederhanakan alur logika. Namun, pada praktiknya di Python, fungsi-fungsi tersebut harus didefinisikan secara eksplisit terlebih dahulu di bagian atas kode sebelum dipanggil. Jika langsung dipanggil tanpa definisi, interpreter Python akan menghentikan program dan memicu eror `NameError: name 'validate_NIK' is not defined`.
- **Logika Penyederhanaan Evaluasi Boolean**: Pada penulisan kondisi bersarang `if is_nik_valid:`, penulisan tersebut secara fungsional identik dengan `if is_nik_valid == True:`. Namun, penggunaan `if is_nik_valid:` sangat direkomendasikan karena lebih bersih (_pythonic_) dan efisien. Hal ini dikarenakan variabel `is_nik_valid` sudah menyimpan nilai tipe data Boolean (`True` atau `False`) hasil dari nilai pengembalian (_return value_) fungsi `validate_NIK()`.
- **Mekanisme Kerja Fungsi `len()` dan Metode `.isdigit()`**: Berdasarkan hasil diskusi kelas, proses validasi NIK menggabungkan fungsi bawaan Python `len()` untuk mendapatkan panjang string dan metode objek string `.isdigit()` untuk memastikan tidak ada karakter huruf atau simbol di dalam NIK. Kedua kondisi ini digabungkan secara ketat dengan operator logika `and`, yang mewajibkan kedua evaluasi bernilai `True` agar hasil akhir validasi bernilai `True`.
- **Alur Penyelamatan Sumber Daya Eksekusi**: Melalui teknik _Nested if_, komputer menghemat sumber daya komputasi dengan tidak menjalankan perintah input NIK atau memanggil fungsi validasi jika usia pengguna di bawah 17 tahun. Blok kode bagian dalam (_inner_) benar-benar terisolasi dan dilindungi oleh _Outer Condition_.



## Bab 5 Looping and Iteration (Perulangan)



---

## 5.1 Konsep Dasar Perulangan dan Stopping Condition

### A. Definisi Looping dan Iteration

- **Looping** atau **Iteration** adalah proses eksekusi sekumpulan instruksi secara berulang-ulang hingga suatu kondisi berhenti yang ditentukan terpenuhi.
- Metode ini digunakan sebagai mekanisme otomatisasi untuk menangani tugas-tugas yang bersifat repetitif secara efisien tanpa harus menulis ulang instruksi yang sama berkali-kali.

### B. Karakteristik Stopping Condition

- **Stopping Condition** merupakan syarat batas evaluasi yang wajib dipenuhi agar aliran eksekusi program dapat keluar dari siklus perulangan.
- Jika _Stopping Condition_ tidak didefinisikan dengan benar atau tidak pernah tercapai selama program berjalan, sistem akan terjebak dalam situasi **Infinite Loop** (perulangan tanpa akhir). Keadaan ini akan terus-menerus mengonsumsi memori dan daya komputasi perangkat secara berlebihan hingga program dihentikan secara paksa.

---

## 5.2 Perbandingan Efisiensi Penulisan Kode

Pendekatan otomatisasi perulangan memberikan efisiensi yang signifikan dibandingkan dengan penulisan baris instruksi secara manual. Berikut adalah tabel komparasi karakteristik dari kedua pendekatan tersebut:

|Kriteria Perbandingan|Tanpa Perulangan (_Without Looping_)|Menggunakan Perulangan (_Using a Loop_)|
|:--|:--|:--|
|**Volume Penulisan Kode**|Tinggi (instruksi berulang harus disalin secara manual sebanyak jumlah eksekusi)|Rendah (hanya memerlukan deklarasi struktur perulangan sekali)|
|**Tingkat Keterbacaan**|Buruk dan redundan, menyulitkan proses penelusuran kesalahan|Bersih, ringkas, dan profesional|
|**Kemudahan Pemeliharaan**|Rendah (perubahan satu logika mengharuskan pengeditan di setiap baris duplikat)|Tinggi (perubahan logika cukup dilakukan pada satu blok perulangan)|
|**Fleksibilitas Jumlah Repetisi**|Kaku (jumlah eksekusi sudah terkunci secara statis sejak kode ditulis)|Dinamis (jumlah repetisi dapat berubah mengikuti variabel atau input sistem)|

### Perbandingan Skenario Kode (Studi Kasus: Mengaduk Sup)

1. **Pendekatan Tanpa Perulangan (_Without Looping_)**:
    
    ```
    stir_the_soup()
    stir_the_soup()
    stir_the_soup()
    stir_the_soup()
    stir_the_soup()
    ```
    
2. **Pendekatan Menggunakan Perulangan (_Using a Loop_)**:
    
    ```
    while not soup_cooked:
        stir_the_soup()
    ```
    

---

## 5.3 Cabang Sintaksis Perulangan Utama di Python

Python menyediakan dua macam struktur sintaksis untuk menangani operasi perulangan:

1. **for Loop**:
    - Sintaksis perulangan yang bekerja dengan cara mengiterasi atau menelusuri setiap elemen di dalam objek yang bersifat _Iterable_ (seperti tipe data String, List, Tuple, Dictionary, Set, atau objek Range).
    - Umumnya digunakan ketika jumlah putaran perulangan sudah dapat diketahui atau didefinisikan secara pasti sejak awal.
2. **while Loop**:
    - Sintaksis perulangan yang beroperasi berdasarkan evaluasi berkala terhadap suatu kondisi Boolean.
    - Blok instruksi di bawah struktur _while_ akan terus dijalankan secara berulang selama kondisi pengujian menghasilkan nilai `True`. Ketika kondisi berubah menjadi `False`, siklus perulangan langsung berhenti.

---

## [Wawasan Diskusi / Audio Insight]

- **Pembeda Fundamental antara Looping dengan Rekursi (_Recursion_)**:
    - Dalam interaksi kelas, dibahas pertanyaan kritis mengenai korelasi perulangan dengan konsep pemrograman rekursif. Dosen menegaskan bahwa meskipun keduanya menghasilkan eksekusi berulang, prinsip kerjanya di dalam memori sangat berbeda.
    - _Recursion_ adalah sebuah fungsi yang memanggil dirinya sendiri dari dalam badan fungsinya sendiri, sehingga membutuhkan alokasi tumpukan memori (_stack_) baru untuk setiap pemanggilan fungsi berantai tersebut hingga batas berhenti (_base case_) dicapai.
    - Sebaliknya, _Looping_ bekerja secara linier di dalam satu cakupan eksekusi yang sama. Program mengevaluasi kondisi secara langsung untuk mengulang instruksi yang didefinisikan (misalnya menjalankan fungsi luar secara berulang seperti `stir_the_soup()`), sehingga jauh lebih hemat dalam penggunaan sumber daya memori komputer.



## Bab 6 Perulangan dengan Sintaksis for


---

## 6.1 Fungsi range() dan Konfigurasi Parameternya

### A. Fondasi Konseptual

Fungsi `range()` adalah fungsi bawaan Python yang digunakan untuk menghasilkan urutan (_sequence_) angka numerik secara berurutan. Secara default, urutan ini selalu dimulai dari angka `0` dengan kelipatan penambahan (_increment_) sebesar `1`. Aliran angka yang dihasilkan oleh fungsi ini akan selalu berhenti tepat **satu angka sebelum** angka batas akhir (_stop value_) yang ditentukan.

### B. Konfigurasi Parameter range()

Fungsi `range()` menerima tiga parameter konfigurasi dengan aturan penulisan: `range(start, stop, step)`.

|Parameter|Sifat|Deskripsi|Nilai Default|
|:--|:--|:--|:--|
|**`start`**|Opsional|Menentukan angka awal dimulainya urutan.|`0`|
|**`stop`**|Wajib|Menentukan batas akhir urutan. Angka pada posisi ini bersifat eksklusif (tidak dimasukkan ke dalam hasil).|Tidak ada|
|**`step`**|Opsional|Menentukan besarnya nilai lompatan atau kelipatan penambahan (_increment_).|`1`|

### C. Contoh Implementasi Komparatif

Berikut adalah beberapa skenario penulisan fungsi `range()` beserta urutan angka yang dihasilkan:

- **Skenario 1: Satu Parameter `range(stop)`**
    
    ```Python
    # Menghasilkan angka dari 0 sampai sebelum 10 dengan langkah 1
    for number in range(10):
        print(number, end=" ")
    # Output: 0 1 2 3 4 5 6 7 8 9
    ```
    
- **Skenario 2: Dua Parameter `range(start, stop)`**
    
    ```Python
    # Menghasilkan angka dari 1 sampai sebelum 10 dengan langkah 1
    for number in range(1, 10):
        print(number, end=" ")
    # Output: 1 2 3 4 5 6 7 8 9
    ```
    
- **Skenario 3: Tiga Parameter `range(start, stop, step)`**
    
    ```Python
    # Menghasilkan angka dari 1 sampai sebelum 10 dengan lompatan 2
    for number in range(1, 10, 2):
        print(number, end=" ")
    # Output: 1 3 5 7 9
    ```
    

### [Wawasan Diskusi / Audio Insight]

- **Sifat Eksklusif Parameter `stop`**: Sangat penting untuk mengingat bahwa nilai pada parameter `stop` tidak akan pernah diikutsertakan dalam hasil akhir. Sebagai contoh, `range(10)` atau `range(1, 10)` hanya akan menghasilkan angka maksimal sampai `9`.
- **Aturan Default Parameter**: Di dalam Python, jika sebuah parameter fungsi dideklarasikan menggunakan tanda sama dengan (seperti `start=0`), parameter tersebut bersifat opsional karena sudah memiliki nilai default. Sebaliknya, parameter `stop` tidak memiliki nilai default sehingga wajib didefinisikan secara eksplisit oleh programmer ketika memanggil fungsi `range()`.

---

## 6.2 Karakteristik Iterable Data Types

### A. Fondasi Konseptual

Objek _Iterable_ adalah tipe data atau objek apa pun dalam Python yang elemen-elemen penyusunnya dapat diakses, dijelajahi, atau dilalui satu per satu secara berurutan (_traversed_). Objek ini berfungsi sebagai wadah penampung nilai yang nantinya akan dikonsumsi oleh struktur perulangan seperti `for loop`.

### B. Karakteristik Tipe Data Iterable di Python

|Tipe Data|Contoh Deklarasi|Deskripsi Karakteristik Iterasi|
|:--|:--|:--|
|**String**|`"Python"`|Mengiterasi setiap karakter huruf penyusun string secara berurutan (`'P'`, `'y'`, `'t'`, `'h'`, `'o'`, `'n'`).|
|**List**|`["Apple", "Banana", "Orange"]`|Mengiterasi setiap elemen objek di dalam kurung siku secara berurutan.|
|**Tuple**|`(10, 20, 30)`|Mengiterasi objek berurutan yang bersifat tidak dapat diubah (_immutable_).|
|**Dictionary**|`{"name": "John", "age": 20}`|Mengiterasi pasangan kunci (_keys_) dan nilai (_values_). Secara default hanya mengembalikan kunci.|
|**Set**|`{1, 2, 3}`|Mengiterasi sekumpulan nilai unik yang tidak terurut secara berurutan.|
|**Range**|`range(5)`|Mengiterasi urutan numerik dinamis yang dihasilkan dari fungsi pembatas.|

---

## 6.3 Sintaksis Dasar for loop

### A. Fondasi Konseptual

Sintaksis `for loop` di Python dirancang khusus untuk melakukan iterasi langsung pada elemen-elemen dari objek _iterable_ tanpa memerlukan evaluasi kondisi Boolean eksplisit seperti pada perulangan `while`. Jumlah pengulangan dalam `for loop` ditentukan secara otomatis berdasarkan jumlah elemen yang tersedia di dalam objek wadah tersebut.

### B. Struktur Sintaksis Dasar

```Python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Pada contoh di atas, variabel `fruit` dideklarasikan langsung di baris deklarasi perulangan sebagai variabel penampung sementara. Pada iterasi pertama, `fruit` akan menyimpan nilai `"apple"`, iterasi kedua `"banana"`, dan iterasi ketiga `"cherry"`. Perulangan otomatis berakhir ketika sistem mendeteksi tidak ada lagi elemen yang tersisa di dalam list `fruits`.

### [Wawasan Diskusi / Audio Insight]

- **Persistensi Variabel Perulangan**: Variabel penampung sementara yang digunakan di baris deklarasi `for loop` (misalnya variabel `number` pada `for number in range(10)`) tidak akan dihapus dari memori komputer setelah perulangan selesai berjalan. Variabel tersebut tetap menyimpan nilai terakhir yang diproses dalam iterasi (dalam contoh ini, nilai terakhir yang tersimpan adalah `9`).
- **Fleksibilitas Penamaan Variabel**: Nama variabel penampung setelah kata kunci `for` bebas dinamai apa saja oleh programmer (misalnya `for x in range(5)` atau `for buah in fruits`). Aturan utamanya adalah nama variabel tersebut harus dipanggil dengan ejaan yang persis sama di dalam blok kode pengolahan data di bawahnya.

---

## 6.4 Fungsi enumerate() untuk Pelacakan Pasangan Indeks dan Nilai

### A. Fondasi Konseptual

Fungsi `enumerate()` adalah fungsi penolong bawaan Python yang digunakan untuk mengiterasi suatu objek _iterable_ sekaligus melacak posisi indeks dari masing-masing elemen yang sedang diproses. Fungsi ini menghilangkan kebutuhan programmer untuk membuat dan menambahkan nilai variabel pencatat indeks (_counter_) secara manual di dalam blok perulangan.

### B. Mekanisme Kerja dan Struktur Pengembalian

Fungsi `enumerate()` bekerja dengan mengemas indeks dan elemen terkait ke dalam format pasangan data _tuple_ dengan pola: `(index, element)`.

```Python
kata = "hai"
for indeks, huruf in enumerate(kata):
    print(f"Huruf ke-{indeks} dari '{kata}' adalah {huruf}")
```

### C. Pengaturan Parameter `start` pada Fungsi enumerate()

Secara default, penomoran indeks yang dihasilkan oleh `enumerate()` selalu dimulai dari angka `0`. Namun, kita dapat mengatur parameter `start` untuk mengubah angka awal dimulainya penghitungan indeks tersebut.

```Python
fruits = ["apple", "banana", "cherry"]
# Mengatur penghitungan indeks dimulai dari angka 1
for indeks, buah in enumerate(fruits, start=1):
    print(f"Peringkat {indeks}: {buah}")
```

### [Wawasan Diskusi / Audio Insight]

- **Dampak Parameter `start`**: Menentukan nilai `start=1` (atau angka lainnya) pada `enumerate()` hanya mengubah representasi angka pencatat indeks yang ditampilkan ke terminal, tetapi **tidak melakukan operasi pemotongan (_skipping_)** pada data. Elemen pertama (indeks ke-0 pada list asli) akan tetap diproses penuh sebagai elemen pertama dalam iterasi, namun nomor pencatatnya saja yang digeser menjadi angka 1.
- **Komparasi Efisiensi**: Melakukan pelacakan indeks menggunakan `enumerate()` dinilai jauh lebih bersih, aman, dan efisien (_pythonic_) dibandingkan metode konvensional yang mengombinasikan fungsi `range()` dan fungsi panjang data `len()` secara manual seperti pada baris kode di bawah ini:
    
    ```Python
    # Metode Manual (Kurang Efisien)
    for i in range(len(fruits)):
        print(f"Indeks {i}: {fruits[i]}")
    ```
    

---

## 6.5 Iterasi Spesifik pada Tipe Data Dictionary

### A. Fondasi Konseptual

Tipe data Dictionary di Python menyimpan data dalam format pasangan kunci dan nilai (_key-value pairs_). Ketika kita melakukan perulangan `for` langsung pada objek dictionary, Python secara default hanya akan mengembalikan elemen kuncinya (_keys_) saja. Untuk melakukan iterasi secara spesifik pada bagian tertentu dari dictionary, Python menyediakan tiga buah metode bawaan (_built-in methods_).

### B. Karakteristik Metode Iterasi Dictionary

|Metode|Deskripsi Fungsional|Contoh Implementasi|
|:--|:--|:--|
|**Default (Tanpa Metode)**|Hanya mengiterasi bagian kunci (_keys_) saja.|`for key in person:`|
|**`.keys()`**|Menegaskan iterasi khusus pada kumpulan kunci saja.|`for key in person.keys():`|
|**`.values()`**|Mengiterasi khusus pada kumpulan nilai (_values_) saja.|`for val in person.values():`|
|**`.items()`**|Mengiterasi pasangan kunci dan nilai sekaligus secara bersamaan.|`for key, val in person.items():`|

### C. Implementasi Kode

Berikut adalah contoh penerapan metode `.items()` untuk mengekstrak pasangan kunci dan nilai secara bersamaan:

```Python
person = {"name": "John", "age": 20, "weight": 73}

for key, value in person.items():
    print(f"{key}: {value}")
```

### [Wawasan Diskusi / Audio Insight]

- **Format Penulisan Dictionary**: Penulisan dictionary dideklarasikan menggunakan kurung kurawal `{}`. Karakter yang ditulis sebelum tanda titik dua (`:`) bertindak sebagai Kunci (_Key_), sedangkan karakter setelah titik dua bertindak sebagai Nilai (_Value_).
- **Urutan Penangkapan Variabel**: Saat menggunakan metode `.items()`, kita wajib menyediakan dua variabel penampung pada baris deklarasi `for` (misalnya `for key, value in person.items()`). Python akan selalu mengirimkan data kunci ke variabel pertama dan data nilai ke variabel kedua secara berurutan. Jangan membalik urutan variabel jika ingin menjaga kejelasan logika kode.

---

## 6.6 Implementasi Pernyataan pass sebagai Placeholder

### A. Fondasi Konseptual

Pernyataan `pass` adalah pernyataan kosong (_null statement_) di Python yang tidak melakukan operasi atau tindakan apa pun saat dieksekusi oleh komputer. Di Python, blok struktur kontrol seperti `if` atau `for loop` tidak diperbolehkan memiliki blok instruksi yang kosong secara sintaksis. Jika hal tersebut terjadi, Python Interpreter akan menghentikan program dan memicu kesalahan eror sintaks.

### B. Contoh Kasus Penggunaan pass

Pernyataan `pass` digunakan sebagai penampung sementara (_placeholder_) untuk menjaga struktur sintaksis program tetap valid ketika programmer sedang merancang kerangka perulangan namun belum menuliskan logika pemrosesan data di dalamnya.

```Python
# Kerangka perulangan yang belum selesai ditulis logikanya
for number in range(100):
    pass  # Menjaga agar kode tidak mengalami eror saat dijalankan
```

### [Wawasan Diskusi / Audio Insight]

- **Solusi Anti-Eror**: Tanpa adanya instruksi `pass` di dalam badan perulangan kosong, program Python akan langsung memicu kesalahan fatal berupa `IndentationError` atau `SyntaxError`.
- **Perbedaan `pass` vs `continue`**: Pernyataan `pass` sama sekali tidak memengaruhi alur perulangan—komputer tetap menjalankan semua tahapan iterasi secara normal tanpa melakukan aksi apa pun. Sementara pernyataan `continue` akan melompati sisa instruksi yang ada di bawahnya dalam iterasi saat ini dan langsung berpindah ke langkah iterasi berikutnya.



## Bab 7 Perulangan dengan Sintaksis while


## 7.1 Aliran Kontrol Perulangan Berbasis Evaluasi Kondisi Boolean

### A. Fondasi Konseptual

- **Definisi _while Loop_**: _while loop_ di Python adalah salah satu dari dua cabang sintaksis perulangan utama yang mengandalkan evaluasi kondisi logika untuk mengontrol perulangan. Program akan mengeksekusi blok kode di dalamnya secara berulang-ulang selama kondisi yang didefinisikan tersebut terus bernilai `True`.
- **Mekanisme Aliran Kontrol**: Komputer akan melakukan pemeriksaan kondisi terlebih dahulu sebelum mengeksekusi blok perulangan:
    1. Jika kondisi bernilai `True`, blok instruksi di dalam perulangan akan dijalankan.
    2. Setelah satu putaran eksekusi selesai, kondisi akan diperiksa kembali di bagian atas.
    3. Jika kondisi berubah bernilai `False`, perulangan akan langsung terhenti, dan eksekusi dilanjutkan ke baris instruksi setelah blok perulangan.

### B. Istilah Teknis dalam Perulangan _while_

|Istilah Teknis|Deskripsi Fungsional|
|:--|:--|
|_Initial Condition_|Nilai awal variabel kontrol sebelum masuk ke dalam perulangan.|
|_Condition Evaluation_|Proses di mana komputer mengevaluasi ekspresi logika untuk memeriksa status _True_ atau _False_.|
|_Stopping Condition_|Keadaan atau nilai tertentu di mana kondisi _while_ menjadi _False_, yang memaksa perulangan untuk berhenti secara normal.|
|_Loop Increment / Decrement_|Pembaruan nilai variabel kontrol di dalam perulangan untuk mencegah terjadinya perulangan tanpa akhir (_Infinite Loop_).|

### C. Implementasi Kode

Berikut adalah implementasi _while loop_ sederhana untuk mencetak deret hitung bertambah (increment):

```
count = 1
while count <= 3:
    print(count)
    count += 1
```

Berikut adalah implementasi untuk deret hitung berkurang (decrement) menggunakan skenario pembelian cokelat:

```
money = 10
while money > 0:
    print("Buying $1 Chocolate...")
    money = money - 1
```

#### [Wawasan Diskusi / Audio Insight]

- **Sifat Dinamis Perulangan _while_**: Berbeda dengan _for loop_ yang iterasi elemennya sudah pasti berdasarkan panjang objek iterable, _while loop_ digunakan ketika jumlah perulangan tidak diketahui secara pasti di awal dan sepenuhnya bergantung pada perubahan kondisi logika yang dinamis selama runtime.
- **Perilaku Memori**: Setiap kali variabel kontrol (seperti `count` atau `money`) diperbarui di dalam blok perulangan, nilai barunya akan langsung diperbarui di dalam memori. Proses evaluasi logika pada baris _while_ selalu menggunakan nilai terbaru dari variabel kontrol tersebut pada iterasi berikutnya.

---

## 7.2 Identifikasi Bahaya dan Dampak Infinite Loop pada Sumber Daya Komputasi

### A. Fondasi Konseptual

- **Definisi _Infinite Loop_**: Situasi di mana perulangan berjalan secara terus-menerus tanpa pernah berhenti karena kondisi evaluasi logika _while_ selalu bernilai `True`.
- **Penyebab Utama**: Terjadi karena programmer lupa menuliskan instruksi pembaruan nilai variabel kontrol (seperti pengurangan/penambahan variabel kontrol) atau kondisi berhenti (_stopping condition_) yang dikonfigurasi tidak akan pernah bisa tercapai.

### B. Karakteristik dan Dampak Teknis _Infinite Loop_

|Karakteristik|Deskripsi Dampak|
|:--|:--|
|**Konsumsi CPU**|Menggunakan sumber daya pemrosesan CPU perangkat secara penuh, yang dapat menyebabkan sistem hang atau melambat.|
|**Penggunaan Memori**|Dapat menyebabkan kebocoran memori jika ada alokasi data baru secara terus-menerus di dalam perulangan.|
|**Pencegahan**|Selalu pastikan adanya pembaruan nilai variabel kontrol (_increment_ / _decrement_) di dalam blok perulangan sebelum menjalankan program.|

### C. Contoh Kasus _Infinite Loop_

Berikut adalah bentuk penulisan kode yang tidak memperbarui variabel kontrol `money` sehingga mengakibatkan perulangan tanpa henti:

```
# PERINGATAN: Kode ini memicu Infinite Loop jika dijalankan
money = 10
while money > 0:
    print("Buying $1 Chocolate...")
    # Nilai money tidak pernah dikurangi, sehingga kondisi money > 0 selalu True
```

#### [Wawasan Diskusi / Audio Insight]

- **Cara Menghentikan Paksa di VS Code**: Jika programmer tidak sengaja menjalankan _Infinite Loop_ di terminal, eksekusi program dapat dihentikan secara paksa dengan menekan tombol kombinasi tombol pintas `Ctrl + C` di dalam terminal Python.
- **Penggunaan Fungsi Penunda (_Time Delay_)**: Dalam sesi latihan pengujian _Infinite Loop_, fungsi `time.sleep(0.3)` dari pustaka `time` Python dapat dimanfaatkan untuk memberi jeda komputasi sebesar 0.3 detik per iterasi. Hal ini bertujuan agar eksekusi perulangan berjalan cukup lambat sehingga proses _infinite loop_ dapat diamati secara visual pada layar terminal tanpa langsung membebani CPU komputer secara ekstrem.

---

## 7.3 Pernyataan Aliran Perulangan: break dan continue

### A. Fondasi Konseptual

Python menyediakan kata kunci kontrol aliran khusus untuk memodifikasi jalannya eksekusi perulangan dari dalam blok kode:

- **Pernyataan _break_**: Berfungsi untuk menghentikan perulangan secara paksa pada saat itu juga, tanpa memedulikan apakah kondisi _while_ masih bernilai `True` atau tidak. Setelah pernyataan `break` dipicu, komputer langsung melompat keluar dari perulangan.
- **Pernyataan _continue_**: Berfungsi untuk langsung melompati sisa instruksi di bawahnya pada iterasi yang sedang berjalan, lalu memaksa program untuk segera melompat ke bagian awal perulangan untuk melakukan evaluasi kondisi atau iterasi berikutnya.

### B. Perbandingan Mekanisme Kerja _break_ vs _continue_

|Karakteristik|Pernyataan _break_|Pernyataan _continue_|
|:--|:--|:--|
|**Dampak Terhadap Perulangan**|Menghentikan dan keluar dari seluruh perulangan seketika|Hanya melompati iterasi berjalan dan melanjutkan ke iterasi berikutnya|
|**Titik Keluar (_Exit Point_)**|Langsung menuju baris kode pertama di luar blok perulangan|Kembali ke baris evaluasi kondisi _while_ di bagian atas|
|**Tujuan Umum**|Menangani kondisi darurat atau batas maksimum (seperti stok habis)|Melompati eksekusi instruksi tertentu untuk kasus-kasus spesifik|

### C. Implementasi Kode dengan _break_

Contoh kasus di mana perulangan terhenti paksa menggunakan `break` saat stok cokelat habis (`chocolate_stock == 0`), meskipun pembeli masih memiliki uang (`money > 0`):

```
money = 10
chocolate_stock = 5

while money > 0:
    print("Buying $1 Chocolate...")
    if chocolate_stock == 0:
        print("Chocolate out of stock!")
        break
    money = money - 1
    chocolate_stock = chocolate_stock - 1
```

### D. Implementasi Kode dengan _continue_

Contoh kasus menggunakan `continue` pada hari ke-7 di mana cokelat dibagikan gratis. Eksekusi pemotongan uang pembeli diloncati, namun perulangan tetap berlanjut ke hari berikutnya:

```
money = 10
day = 1

while money > 0:
    print("Buying $1 Chocolate...")
    if day == 7:
        print("Free chocolate today!")
        day = day + 1
        continue
    money = money - 1
    day = day + 1
```

#### [Wawasan Diskusi / Audio Insight]

- **Bahaya _Infinite Loop_ pada _continue_**: Ketika menggunakan pernyataan `continue`, urutan penulisan kode pembaruan variabel kontrol harus diletakkan dengan cermat. Pada contoh kasus "hari gratis", instruksi `day = day + 1` diletakkan tepat **sebelum** kata kunci `continue` agar nilai hari tetap bertambah. Jika pembaruan nilai variabel kontrol hanya diletakkan di akhir blok _while_ (di bawah pernyataan `continue`), program akan terjebak dalam _Infinite Loop_ karena variabel hari akan bernilai 7 selamanya tanpa pernah diperbarui.

---

## 7.4 Sintaksis else dalam Loop

### A. Fondasi Konseptual

- **Definisi _else_ pada Loop**: Di Python, blok pernyataan `else` dapat dikaitkan dengan perulangan `while` atau `for`. Blok `else` ini memiliki karakteristik unik di mana instruksi di dalamnya **hanya akan dijalankan apabila perulangan berakhir secara normal** (kondisi perulangan bernilai `False`).
- **Kondisi Eksklusi**: Jika perulangan dihentikan di tengah jalan secara paksa menggunakan kata kunci `break`, maka blok pernyataan `else` di bawah perulangan tersebut **tidak akan pernah dieksekusi** oleh komputer.

### B. Karakteristik Aliran Eksekusi _else in Loop_

|Status Akhir Perulangan|Apakah Blok _else_ Dieksekusi?|Alasan Aliran Sistem|
|:--|:--|:--|
|Perulangan selesai secara normal (_while_ menjadi _False_)|**Ya**|Sistem mendeteksi perulangan selesai tanpa adanya interupsi eksternal.|
|Perulangan berhenti akibat pernyataan _break_|**Tidak**|Sistem mendeteksi adanya interupsi paksa yang melompati bagian penutup perulangan.|

### C. Implementasi Kode (Studi Kasus Validasi Password / Login Attempt)

Berikut adalah implementasi sistem percobaan autentikasi maksimal 3 kali menggunakan perulangan _while_ dan _else_. Jika pengguna berhasil login sebelum percobaan habis, program memicu `break` sehingga blok `else` diabaikan. Jika percobaan habis tanpa jawaban benar, perulangan selesai normal dan blok `else` dikunci dijalankan:

```
attempt = 1
while attempt <= 3:
    password = input("Password: ")
    if password == "python":
        print("Authenticated!")
        break
    else:
        print("Wrong password!")
        attempt += 1
else:
    print("Maximum attempt reached! Account locked!")
```

#### [Wawasan Diskusi / Audio Insight]

- **Penyederhanaan Logika Pemrograman**: Fitur _else in loop_ sangat berguna untuk menyederhanakan kode yang membutuhkan penanda status (_flag_). Tanpa menggunakan blok `else` ini, programmer harus membuat variabel penanda tambahan (seperti `is_locked = True`) dan melakukan pengecekan kondisi logika bersyarat di luar blok perulangan secara manual, yang membuat kode menjadi lebih panjang dan kurang efisien.



## Bab 8 Studi Komparasi & Pembahasan Soal Latihan Akhir Sesi


## 8.1 Tabel Komparasi Karakteristik Utama Antara for Loop vs while Loop

Python menyediakan dua mekanisme utama untuk melakukan perulangan (_looping_), yaitu `for loop` dan `while loop`. Pemilihan antara keduanya bergantung pada karakteristik data dan kebutuhan kontrol aliran program.

Berikut adalah tabel komparasi fungsional antara `for loop` dan `while loop`:

|Fitur|_for Loop_|_while Loop_|
|:--|:--|:--|
|**Kondisi Penggunaan Terbaik**|Jumlah iterasi sudah diketahui secara pasti sebelum perulangan dimulai.|Jumlah iterasi tidak diketahui secara pasti dan bergantung pada pemenuhan suatu kondisi tertentu.|
|**Mekanisme Berhenti (_Stopping Condition_)**|Berhenti otomatis setelah seluruh elemen dalam objek _iterable_ selesai diproses atau rentang _range_ berakhir.|Berhenti ketika evaluasi kondisi logika (_loop condition_) berubah bernilai `False`.|
|**Kasus Penggunaan Umum (_Common Use Cases_)**|Mengiterasi elemen pada tipe data koleksi (_list_, _string_, _dictionary_, _tuple_, _set_) atau hasil fungsi `range()`.|Menunggu suatu aksi/kondisi (_waiting for a condition_), siklus permainan (_game loops_), membaca _user input_, dan logika mencoba kembali (_retry logic_).|
|**Dukungan Pernyataan `break`**|Ya, dapat digunakan untuk menghentikan perulangan secara paksa di tengah jalan.|Ya, dapat digunakan untuk menghentikan perulangan secara paksa di tengah jalan.|
|**Dukungan Pernyataan `continue`**|Ya, dapat digunakan untuk melompati iterasi berjalan dan langsung berpindah ke iterasi berikutnya.|Ya, dapat digunakan untuk melompati iterasi berjalan dan langsung mengevaluasi kembali kondisi utama.|
|**Dukungan Blok `else`**|Ya, blok `else` akan dieksekusi jika perulangan selesai berjalan normal tanpa interupsi `break`.|Ya, blok `else` akan dieksekusi jika perulangan selesai berjalan normal (kondisi menjadi `False`) tanpa interupsi `break`.|

---

## 8.2 Analisis Algoritma dan Pembahasan Solusi Soal Latihan Akhir

Bagian ini membedah solusi pemrograman dari empat soal latihan penutup kelas untuk melatih pemahaman logika kondisional dan perulangan.

### A. Soal 1: Pengecekan Kategori Angka (Ganjil, Genap, atau Nol)

Program diminta menerima input sebuah bilangan bulat, lalu mengategorikan apakah angka tersebut merupakan bilangan genap (_even_), ganjil (_odd_), atau nol (_zero_).

#### Solusi Kode Python

```Python
def check_number_type(number):
    if number == 0:
        print("zero")
    elif number % 2 == 0:
        print("even")
    else:
        print("odd")

check_number_type(10)
check_number_type(1)
check_number_type(0)
```

#### [Wawasan Diskusi / Audio Insight]

- **Logika Evaluasi Nol Pertama**: Pemeriksaan kondisi `number == 0` harus diletakkan pada percabangan pertama (`if`). Jika tidak, angka `0` akan lolos ke pemeriksaan modulo `0 % 2 == 0` dan teridentifikasi secara salah sebagai bilangan genap (_even_), karena secara aritmetika sisa hasil bagi 0 dengan 2 adalah 0.
- **Pembersihan Kata Kunci `pass`**: Pada saat menggunakan kerangka kode (_skeleton code_), kata kunci `pass` diletakkan sebagai penampung sementara agar program tidak eror saat dibaca oleh Python interpreter. Setelah fungsi atau logika selesai didefinisikan secara konkret, kata kunci `pass` harus dihapus karena tidak lagi diperlukan.

---

### B. Soal 2: Perhitungan Rata-Rata Angka Dinamis (Hingga Input Berhenti pada Angka 0)

Program diminta untuk terus-menerus meminta input bilangan bulat dari pengguna (_repeatedly ask the user_) sampai pengguna memasukkan angka `0`. Setelah angka `0` dimasukkan, program harus menghitung dan menampilkan nilai rata-rata dari seluruh bilangan bulat yang dimasukkan sebelumnya (angka `0` sebagai penanda berhenti tidak ikut dihitung).

#### Solusi Kode Python

```Python
total = 0
count = 0

while True:
    number = int(input("Masukkan angka bulat (0 untuk berhenti): "))
    if number == 0:
        if total == 0:
            print(0)
        else:
            average = total / count
            print(average)
        break
    total += number
    count += 1
```

#### [Wawasan Diskusi / Audio Insight]

- **Penanganan Eror Pembagian Nol (_ZeroDivisionError_)**: Jika pengguna langsung memasukkan angka `0` pada kesempatan pertama tanpa memasukkan angka lain terlebih dahulu, variabel `count` akan bernilai `0`. Pembagian `total / count` (yaitu `0 / 0`) akan memicu kegagalan sistem berupa `ZeroDivisionError`. Oleh karena itu, diperlukan validasi tambahan `if total == 0` atau `if count == 0` untuk langsung mencetak hasil `0` tanpa melakukan komputasi pembagian.
- **Aturan Desain Fungsi (`return` vs `print()`)**: Dalam perancangan fungsi Python yang baik, hindari penulisan `return print(...)`. Pernyataan `return` digunakan untuk mengirimkan kembali nilai murni hasil komputasi kepada pemanggil fungsi agar nilai tersebut dapat diolah kembali. Jika hanya ingin menampilkan teks hasil ke layar terminal tanpa mengembalikan nilai apa pun, gunakan instruksi `print()` secara langsung tanpa menyertakan `return`.
- **Peletakan Pernyataan `break`**: Pastikan pernyataan `break` diletakkan dengan indentasi yang tepat setelah proses pelaporan rata-rata selesai dilakukan pada saat input `0` terdeteksi. Hal ini bertujuan agar perulangan `while True` langsung dihentikan secara permanen dalam satu kali proses eksekusi.

---

### C. Soal 3: Pencarian Nilai Terbesar dari 3 Input Bilangan Bulat (Tanpa max())

Program diminta menerima 3 input bilangan bulat dari pengguna, kemudian menentukan dan mencetak bilangan dengan nilai terbesar di antara ketiganya tanpa menggunakan fungsi bawaan Python seperti `max()`.

#### Solusi Kode Python

```Python
num1 = int(input("Masukkan angka pertama: "))
num2 = int(input("Masukkan angka kedua: "))
num3 = int(input("Masukkan angka ketiga: "))

if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

print(f"largest = {largest}")
```

#### [Wawasan Diskusi / Audio Insight]

- **Definisi Nilai Terbesar**: Sebuah bilangan bulat didefinisikan sebagai bilangan terbesar dari kelompok tiga angka apabila bilangan tersebut secara bersamaan memiliki nilai yang lebih besar dibandingkan bilangan kedua DAN bilangan ketiga.
- **Penggunaan Operator Logika `and`**: Logika ini diimplementasikan menggunakan operator logika `and` untuk menggabungkan dua kondisi perbandingan terpisah (`num1 > num2 and num1 > num3`). Kedua perbandingan tersebut wajib bernilai `True` agar variabel penampung `largest` dapat diisi dengan angka bersangkutan.
- **Efisiensi Cabang Akhir (`else`)**: Cabang `else` paling akhir tidak memerlukan kondisi logika eksplisit tambahan. Jika angka pertama bukan yang terbesar (`if` bernilai `False`) dan angka kedua juga bukan yang terbesar (`elif` bernilai `False`), maka secara otomatis angka ketiga merupakan nilai terbesar yang tersisa.

---

### D. Soal 4: Perhitungan Jumlah Bilangan Prima dalam Batas Rentang Tertentu (Lower & Upper Bound)

Program diminta meminta input batas bawah (_lower bound_) dan batas atas (_upper bound_) dari pengguna. Program kemudian menghitung total jumlah (penjumlahan/sum) dari seluruh bilangan prima yang berada di dalam rentang tersebut (inklusif). Jika batas bawah lebih besar dari batas atas atau jika batas bawah bernilai negatif (kurang dari 0), program harus menampilkan pesan eror `"range not valid"`.

#### Solusi Kode Python

```Python
lower = int(input("Masukkan batas bawah: "))
upper = int(input("Masukkan batas atas: "))

if lower > upper or lower < 0 or upper < 0:
    print("range not valid")
else:
    prime_sum = 0
    for num in range(lower, upper + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_sum += num
    print(prime_sum)
```

#### [Wawasan Diskusi / Audio Insight]

- **Validasi Awal Rentang Data**: Logika kondisional diletakkan di bagian teratas untuk menyaring input abnormal. Skenario seperti `lower > upper` (misal, batas bawah 10 dan batas atas 0) atau input bernilai negatif (seperti -1) harus langsung menghentikan aliran komputasi utama dan mencetak `"range not valid"`.
- **Karakteristik Bilangan Prima**: Bilangan prima adalah bilangan bulat positif yang hanya memiliki dua pembagi positif, yaitu angka 1 dan dirinya sendiri. Bilangan prima terkecil dimulai dari angka 2, sehingga kondisi pemeriksaan `num > 1` wajib disertakan sebelum menguji pembagi potensial lainnya.
- **Perhitungan Matematika Rentang Inklusif**: Saat melakukan iterasi pada perulangan `for` menggunakan fungsi `range()`, batas atas harus ditambahkan dengan angka 1 (`upper + 1`). Hal ini disebabkan karena parameter `stop` pada fungsi `range()` bersifat eksklusif (tidak diikutsertakan dalam iterasi).



## Conditional and Loop Statements

## Boolean ##

Hasil dari logical expression. Isinya hanya True & False. 

Ini akan membantu python mengammbil keptusan.  Pakai if, elif dan else statements. 

### If Syntax
Mirip dengan latihan


### Looping and Iteration###

Buat loop, dimana proses berulang terus sampai kondisinya terpenuhi. Artinya melakukan eksekusi berulang, dan tidak akan berhenti sampai kondisinya berhenti. 

### for syntax ###

#### Range Function ####


 #### while Syntax ####





---


# Module 1 Session 4 Data Types Collection Notes


## Bab 1 Review Sesi Sebelumnya #U2013 Sesi Tanya Jawab & Latihan Bilangan Prima

## 1.1 Aturan Validasi Input Range

Sebelum melakukan perhitungan, program harus memvalidasi input _range_ yang dimasukkan oleh pengguna. Input tersebut terdiri dari batas bawah (_lower limit_) dan batas atas (_upper limit_).

### 1.1.1 Syarat Kelayakan Input

Input batas bawah dan batas atas harus memenuhi beberapa kriteria agar dapat diproses lebih lanjut:

- Harus berupa bilangan bulat positif (_positive integer_).
- Batas bawah tidak boleh bernilai lebih besar dari batas atas.
- Kedua nilai batas tidak boleh bernilai negatif (di bawah 0).

### 1.1.2 Tabel Validasi Range Input

Berikut adalah rangkuman logika validasi input _range_:

|Kondisi Input|Status Kelayakan|Tindakan Program|
|:--|:--|:--|
|`lower` > `upper`|Tidak Valid|Menghentikan eksekusi / Memberikan pesan error|
|`lower` < 0 atau `upper` < 0|Tidak Valid|Menghentikan eksekusi / Memberikan pesan error|
|`lower` >= 0 dan `lower` <= `upper`|Valid|Melanjutkan ke proses perhitungan bilangan prima|

**[Wawasan Diskusi / Audio Insight]** Berdasarkan penjelasan dosen di kelas, penanganan validasi range ini diletakkan di bagian paling awal program menggunakan blok percabangan `if`. Hal ini bertujuan untuk memastikan program tidak melakukan _computation_ yang sia-sia apabila data input dari pengguna terdeteksi tidak valid.

---

## 1.2 Algoritma Pencarian dan Perhitungan Bilangan Prima

Setelah input dipastikan valid, program akan mengevaluasi setiap angka di dalam rentang (_range_) tersebut untuk mendeteksi apakah angka tersebut merupakan bilangan prima, kemudian mengakumulasikannya.

### 1.2.1 Struktur Perulangan Utama (_Outer Loop_)

Perulangan utama digunakan untuk melakukan iterasi terhadap setiap angka dalam rentang yang telah ditentukan.

- **Inklusivitas Batas Atas**: Rentang iterasi diatur menggunakan parameter `range(lower, upper + 1)`. Penambahan nilai `1` pada batas atas diperlukan karena fungsi `range()` bawaan Python bersifat eksklusif di batas akhir (hanya memproses hingga `upper - 1`). Dengan menggunakan `upper + 1`, batas akhir tetap diikutsertakan dalam pemeriksaan.
- **Penyaringan Angka <= 1**: Bilangan prima didefinisikan sebagai bilangan bulat positif yang nilainya harus lebih besar dari 1. Oleh karena itu, angka 1 dan angka di bawahnya langsung diabaikan dalam pemeriksaan dan dilewati (_skip_).

### 1.2.2 Logika Pembuktian Bilangan Prima

Untuk mendeteksi bilangan prima, program menggunakan metode pembuktian terbalik:

1. **Asumsi Awal**: Setiap angka yang lolos penyaringan awal diasumsikan sebagai bilangan prima terlebih dahulu dengan mengeset variabel flag `is_prime = True`.
2. **Pencarian Pembagi (_Divisor_)**: Program melakukan perulangan kedua (_inner loop_) untuk menguji pembagi (_divisor_ atau variabel `i`) dari rentang `2` hingga `number - 1` (`range(2, number)`). Angka 1 dan angka itu sendiri dikecualikan dari rentang ini.
3. **Pembuktian Negatif**: Di dalam _inner loop_, dilakukan operasi modulus (`number % divisor`). Jika ditemukan nilai pembagi yang menghasilkan sisa bagi sama dengan nol (habis dibagi), maka:
    - Status kelayakan diubah menjadi bukan prima (`is_prime = False`).
    - Perulangan dalam segera dihentikan menggunakan pernyataan `break`, karena satu bukti pembagi sudah cukup untuk menggugurkan kelayakan bilangan prima.
4. **Akumulasi Penjumlahan**: Jika setelah perulangan dalam selesai nilai `is_prime` tetap bernilai `True`, angka tersebut dipastikan bilangan prima dan nilainya ditambahkan ke variabel akumulator total (misalnya `total_prima`).

---

## 1.3 Penanganan Kasus Khusus: Angka 2 sebagai Bilangan Prima

Angka 2 merupakan satu-satunya bilangan prima genap. Algoritma ini mampu menangani angka 2 secara otomatis dan akurat tanpa memerlukan percabangan kondisi tambahan.

### 1.3.1 Alur Eksekusi Angka 2

Ketika variabel angka (`number`) mencapai nilai 2, langkah eksekusi berjalan sebagai berikut:

1. Angka 2 lolos dari penyaringan awal karena nilai `2 > 1`.
2. Asumsi awal diatur: `is_prime = True`.
3. Program masuk ke _inner loop_ pembagi dengan parameter rentang `range(2, 2)`.
4. Dalam Python, objek `range(2, 2)` tidak menghasilkan elemen angka apa pun (kosong), sehingga perulangan pembagi langsung dilewati (_skip_).
5. Karena perulangan pembagi dilewati, status `is_prime` tidak pernah berubah menjadi `False`.
6. Nilai `is_prime` tetap `True` dan angka 2 didefinisikan sebagai bilangan prima, kemudian diakumulasikan ke dalam variabel total.

### 1.3.2 Tabel Tracing Logika Pemeriksaan Angka

Berikut adalah tracing alur eksekusi pemeriksaan beberapa angka contoh:

|Angka (`number`)|Asumsi Awal|Rentang Pembagi (`range(2, number)`)|Evaluasi Modulus|Status Akhir (`is_prime`)|Akumulasi|
|:--|:--|:--|:--|:--|:--|
|2|`True`|`range(2, 2)` (Kosong)|Tidak dievaluasi (loop dilewati)|`True`|Ditambahkan ke total|
|3|`True`|`range(2, 3)` (Isi: 2)|`3 % 2 != 0`|`True`|Ditambahkan ke total|
|4|`True`|`range(2, 4)` (Isi: 2, 3)|`4 % 2 == 0` (Habis dibagi)|`False` (Mengalami `break`)|Diabaikan|

**[Wawasan Diskusi / Audio Insight]** Dalam rekaman sesi tanya jawab kelas, sempat muncul kebingungan mengenai mengapa angka 2 dapat terdeteksi sebagai prima padahal program tidak melakukan proses pembagian divisor. Dosen memberikan klarifikasi penting bahwa hal ini dikarenakan objek `range(2, 2)` menghasilkan rentang kosong pada interpreter Python. Akibatnya, perulangan pembagi otomatis terlewati, dan program langsung mempertahankan status default `is_prime = True`.

---

## 1.4 Contoh Implementasi Kode Python

Berikut adalah contoh implementasi lengkap dari algoritma di atas yang bebas dari error sintaks:

```Python
lower = int(input("Masukkan batas bawah: "))
upper = int(input("Masukkan batas atas: "))

if lower > upper or lower < 0 or upper < 0:
    print("Range tidak valid")
else:
    total_prima = 0
    for number in range(lower, upper + 1):
        if number > 1:
            is_prime = True
            for divisor in range(2, number):
                if number % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                total_prima += number
    print("Total bilangan prima dalam range:", total_prima)
```





## Bab 2 Pengantar Tipe Data Koleksi (Collection Data Types) di Python


## 2.1 Definisi dan Kategori Collection Data Types

Collection Data Types adalah objek yang menampung nol atau lebih objek anggota yang disebut sebagai elemen. Python menyediakan berbagai macam tipe koleksi bawaan (_built-in_) maupun pembantu (_auxiliary_) untuk efisiensi penyimpanan data.

Secara garis besar, Collection Data Types di Python dibagi ke dalam 3 kategori utama:

1. **Sequences** (Urutan)
2. **Mappings** (Pemetaan)
3. **Sets** (Himpunan)

Tabel di bawah ini merangkum karakteristik teknis dari masing-masing tipe data koleksi di Python berdasarkan kelas (_class_), kategori (_category_), klasifikasi (_kind_), serta sifat keterubahan (_mutability_):

|Type|Class|Category|Kind|Mutable|
|:--|:--|:--|:--|:--|
|`ranges`|`range`|_sequences_|_Non-primitive_|No|
|`tuples`|`tuple`|_sequences_|_Non-primitive_|No|
|`lists`|`list`|_sequences_|_Non-primitive_|Yes|
|`dictionaries`|`dict`|_mappings_|_Non-primitive_|Yes|
|`sets`|`set`|_sets_|_Non-primitive_|Yes|
|`frozen sets`|`frozenset`|_sets_|_Non-primitive_|No|

## 2.2 Karakteristik Mutability

Sifat _mutability_ mengacu pada kemampuan suatu tipe data untuk diubah nilainya setelah objek dideklarasikan di dalam memori komputer:

- **Mutable (Bisa Diubah)**: Elemen-elemen di dalam objek tipe data koleksi ini dapat dimodifikasi, ditambah, dihapus, atau diganti setelah objek tersebut berhasil dibuat. Contoh tipe data koleksi yang bersifat _mutable_ adalah `list`, `dict` (dictionary), dan `set`.
- **Immutable (Tidak Bisa Diubah / Read-Only)**: Elemen-elemen di dalam objek tipe data koleksi ini bersifat statis dan sama sekali tidak dapat diubah, diganti, atau dimodifikasi setelah proses deklarasi awal. Contoh tipe data koleksi yang bersifat _immutable_ adalah `range`, `tuple`, dan `frozenset`.

---

## **[Wawasan Diskusi / Audio Insight]**

### A. Implementasi Alur Kerja Git dalam Pembelajaran Praktis

Di dalam pelaksanaan kelas AI Engineering Purwadhika, dosen mengintegrasikan sistem pengontrol versi (_version control system_) menggunakan platform GitHub untuk mengelola materi latihan praktis secara efisien. Alur kerja Git yang wajib diikuti oleh siswa adalah sebagai berikut:

1. **Kloning Repositori Awal (`git clone`)**: Siswa melakukan pengunduhan atau penyalinan repositori pusat GitHub di awal kelas agar semua materi latihan tersimpan secara lokal di komputer masing-masing.
2. **Pembaruan Berkas Materi (`git pull`)**: Ketika ada folder latihan baru atau pembaruan materi yang diunggah oleh dosen (seperti materi folder `collection data type`), siswa tidak perlu melakukan kloning ulang. Siswa cukup menjalankan perintah pembaruan berikut pada terminal mereka:

```
git pull
```

Perintah di atas akan secara otomatis menarik (_pull_) seluruh berkas materi terbaru dari repositori pusat ke komputer lokal siswa. Penerapan metode ini bertujuan melatih kemampuan praktis siswa dalam berinteraksi dengan Git agar siap menghadapi standar industri pekerjaan sebagai AI Engineer.



## Bab 3 Tipe Data Python List

## 3.1 Konsep Dasar List

List adalah salah satu tipe data koleksi bawaan di Python yang digunakan untuk menyimpan beberapa nilai (elemen) dalam satu variabel tunggal. Penggunaan list bertujuan untuk menghindari pembuatan banyak variabel individual secara tidak praktis (misalnya menghindari deklarasi `student_1`, `student_2`, hingga `student_100` secara manual).

Karakteristik teknis tipe data List:

- Ditulis menggunakan kurung siku `[...]`.
- Setiap elemen di dalamnya memiliki indeks (_ordered_) yang dimulai dari angka 0 (_zero-based indexing_).
- Bersifat _mutable_, artinya nilai elemen di dalamnya dapat diubah, ditambah, atau dihapus setelah objek dideklarasikan di dalam memori.
- Mendukung penyimpanan data campuran (_mixed types_) di mana satu list dapat menampung tipe data integer, string, float, boolean, hingga objek list lain (_nested list_).

### 3.1.1 Deklarasi List

Berikut adalah tabel metode deklarasi List di Python:

|Jenis List|Sintaks Deklarasi|Karakteristik / Hasil|
|:--|:--|:--|
|List Kosong|`empty_list = []` atau `empty_list = list()`|Menghasilkan objek list dengan jumlah elemen nol. Kedua metode ini bernilai setara (_equal_).|
|List Homogen|`students = ["andi", "budi", "cinta"]`|Menyimpan beberapa nilai dengan tipe data yang sama (string).|
|List Campuran (_Mixed List_)|`mixed_list = [1, "andi", [2.5, range(10)]]`|Menyimpan elemen dengan tipe campuran (integer, string, dan list bersarang yang berisi float serta objek range).|

Untuk mengakses elemen di dalam _nested list_ (list di dalam list), digunakan pengindeksan ganda. Contoh akses elemen pada `mixed_list`:

- Elemen indeks ke-1: `mixed_list[1]` menghasilkan `"andi"`.
- Elemen indeks ke-2 (berupa list): `mixed_list[2]` menghasilkan `[2.5, range(10)]`.
- Akses spesifik ke angka `2.5` di dalam list bersarang: `mixed_list[2][0]`.

---

## 3.2 Metode dan Fungsi Bawaan List

### 3.2.1 Metode untuk Menambahkan Elemen

Terdapat tiga metode utama untuk menambahkan elemen ke dalam objek list:

- `.append(item)`: Menambahkan satu elemen baru di bagian paling akhir list.
- `.insert(index, item)`: Menyisipkan satu elemen baru pada posisi indeks spesifik yang ditentukan. Elemen di posisi indeks tersebut dan setelahnya akan bergeser ke kanan.
- `.extend(iterable)`: Menggabungkan seluruh elemen dari objek iterable lain (seperti list lain) secara sejajar ke dalam list utama.

### 3.2.2 Metode untuk Menghapus Elemen

Terdapat tiga metode utama untuk menghapus elemen dari list:

- `.pop(index)`: Menghapus elemen berdasarkan posisi indeks yang ditentukan dan mengembalikan (_return_) nilai elemen tersebut. Jika parameter indeks dikosongkan, secara default metode ini akan menghapus dan mengembalikan elemen paling terakhir.
- `.remove(value)`: Menghapus elemen pertama yang memiliki nilai cocok dengan parameter yang dimasukkan. Jika nilai tidak ditemukan di dalam list, Python akan memicu `ValueError`.
- `.clear()`: Mengosongkan seluruh isi list, menghasilkan list kosong tanpa menghapus objek list itu sendiri dari memori.

### 3.2.3 Metode untuk Menggandakan List (`.copy()` vs Referensi)

Dalam Python, melakukan penugasan langsung variabel list baru ke variabel list lama (`new_list = old_list`) tidak melakukan penggandaan objek secara fisik di memori. Kedua variabel tersebut akan merujuk (_point_) ke alamat memori (_memory address_) yang sama.

Untuk menduplikasi list secara aman ke alamat memori yang berbeda, wajib menggunakan metode `.copy()` untuk menghasilkan salinan dangkal (_shallow copy_).

|Metode Pendekatan|Sintaks Kode|Karakteristik Perubahan Data|Dampak pada Objek Memori|
|:--|:--|:--|:--|
|Referensi Langsung (Tanpa Copy)|`list_b = list_a`|Perubahan elemen pada `list_b` akan otomatis memengaruhi `list_a` (dan sebaliknya).|Kedua variabel memiliki ID memori yang sama (`id(list_a) == id(list_b)`).|
|Shallow Copy (Dengan `.copy()`)|`list_b = list_a.copy()`|Perubahan elemen pada `list_b` tidak akan memengaruhi `list_a`.|Kedua variabel merujuk pada objek memori yang berbeda (`id(list_a) != id(list_b)`).|

### 3.2.4 Fungsi Bawaan (_Built-in Functions_) pada List

Fungsi independen yang dapat menerima objek list sebagai argumen:

- `len(list_obj)`: Mengembalikan jumlah total elemen yang ada di dalam list.
- `sorted(list_obj)`: Mengembalikan list baru yang elemennya telah terurut secara menaik (_ascending_ secara default) tanpa memodifikasi urutan elemen pada objek list asli.

---

## 3.3 Konsep List Comprehension

_List comprehension_ adalah fitur Python yang menawarkan sintaksis lebih ringkas untuk membuat list baru berdasarkan elemen-elemen dari list atau objek iterable yang sudah ada.

Sintaksis dasar penulisan:

```
newlist = [expression for item in iterable if condition]
```

Keterangan komponen:

1. `expression`: Hasil akhir atau manipulasi elemen yang akan dimasukkan ke dalam list baru (misalnya mengubah teks menjadi uppercase, menghitung kuadrat, dll.).
2. `for item in iterable`: Proses perulangan dasar untuk mengambil tiap elemen dari objek asal.
3. `if condition`: Operasi penyaringan (_filtering_) opsional. Elemen hanya akan diproses oleh `expression` jika kondisi ini terpenuhi (_True_).

### 3.3.1 Perbandingan Implementasi Kode

Kasus: Menyaring daftar buah yang memiliki huruf `"a"` di dalam namanya, kemudian mengubah nama buah tersebut menjadi huruf besar (_uppercase_).

#### Pendekatan Konvensional (Tanpa List Comprehension):

```
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruit_with_a = []

for fruit in fruits:
    if "a" in fruit:
        fruit_with_a.append(fruit.upper())

print(fruit_with_a)
# Output: ['APPLE', 'BANANA', 'DATE']
```

#### Pendekatan Modern (Dengan List Comprehension):

```
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruit_with_a = [fruit.upper() for fruit in fruits if "a" in fruit]

print(fruit_with_a)
# Output: ['APPLE', 'BANANA', 'DATE']
```

---

## **[Wawasan Diskusi / Audio Insight]**

### A. Perbedaan Signifikan Antara `.extend()` dan `.append()`

Berdasarkan penjelasan interaktif di kelas, terdapat perbedaan mendasar ketika menambahkan elemen berupa list ke dalam list lain:

- Jika menggunakan `.append(list_lain)`, maka seluruh objek `list_lain` dimasukkan utuh sebagai **satu elemen tunggal bersarang (nested list)** di bagian akhir list utama.
- Jika menggunakan `.extend(list_lain)`, Python akan **membongkar (_unpack_)** seluruh elemen dari `list_lain` terlebih dahulu, lalu menggabungkannya satu per satu secara sejajar dengan elemen di list utama.

Berikut adalah ilustrasi perbedaan kodenya:

```
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# Menggunakan .append()
list_b_append = list_b.copy()
list_b_append.append(list_a)
# Hasil: [4, 5, 6, [1, 2, 3]]

# Menggunakan .extend()
list_b_extend = list_b.copy()
list_b_extend.extend(list_a)
# Hasil: [4, 5, 6, 1, 2, 3]
```

### B. Analisis Memori: Operator `is` vs Operator `==`

Dalam sesi tanya jawab, dijelaskan perbedaan mendasar antara membandingkan nilai variabel dan membandingkan lokasi fisik memori:

- Operator `==` digunakan untuk mengevaluasi **kesamaan nilai (_value equality_)** antar variabel.
- Operator `is` digunakan untuk mengevaluasi **kesamaan identitas memori (_reference equality_)** untuk memastikan apakah kedua variabel merujuk pada alamat memori yang persis sama.
- Setiap objek variabel di memori memiliki alamat unik yang dapat dilacak menggunakan fungsi bawaan `id(nama_variabel)`.

```
# Contoh Tracing Identitas Memori
list_x = [1, 2, 3]
list_y = list_x.copy()

print(list_x == list_y)  # True (Nilai elemen di dalamnya sama)
print(list_x is list_y)  # False (Disimpan di alamat memori yang berbeda karena hasil .copy())
print(id(list_x) == id(list_y))  # False
```

### C. Rekonstruksi Pola Pikir Membaca List Comprehension

Bagi programmer pemula, sintaksis list comprehension seringkali membingungkan karena urutan penulisannya yang terbalik dibandingkan perulangan `for` biasa. Dosen memberikan metode praktis untuk membaca dan merancang list comprehension secara bertahap:

1. **Tentukan Sumber Data (Looping)**: Fokus terlebih dahulu pada blok perulangan tengah, yaitu `for item in iterable`.
2. **Tentukan Penyaringan (Filtering)**: Baca blok kondisi di bagian paling kanan, yaitu `if condition`. Tentukan elemen mana saja yang memenuhi syarat untuk lolos seleksi.
3. **Tentukan Aksi Akhir (Expression)**: Baca blok ekspresi di bagian paling kiri, yaitu manipulasi apa yang ingin diterapkan pada elemen yang lolos seleksi sebelum dimasukkan ke list baru (seperti `.upper()`, `.capitalize()`, atau operasi aritmatika).

Metode ini terbukti mempermudah siswa kelas AI Engineering dalam menyelesaikan tugas penyaringan karakter teks dan operasi matematika secara cepat tanpa mengalami kegagalan logika pemrograman.



## Bab 4 Tipe Data Python Tuple

## 4.1 Konsep Dasar dan Karakteristik Tuple

Tuple adalah tipe data koleksi di Python yang digunakan untuk menyimpan beberapa nilai di dalam satu variabel tunggal, mirip dengan List. Perbedaan mendasar antara List dan Tuple terletak pada sifat keterubahannya (_mutability_). Tuple bersifat _immutable_, yang berarti nilai atau elemen di dalamnya bersifat _read-only_ dan tidak dapat diubah, ditambah, atau dihapus setelah objek Tuple dideklarasikan di dalam memori komputer.

### 4.1.1 Kasus Penggunaan Utama

Tuple sangat ideal digunakan untuk menampung kumpulan data yang nilainya bersifat konstan atau tidak boleh mengalami modifikasi sepanjang program berjalan. Contoh kasus penggunaan:

- **Geolokasi**: Menyimpan koordinat wilayah dalam format (latitude, longitude), misalnya `jakarta_geolocation = (-6.200000, 106.816666)`.
- **Representasi Warna**: Menyimpan format warna RGB (Red, Green, Blue), misalnya `white = (255, 255, 255)`.

### 4.1.2 Karakteristik dan Sintaksis Penulisan

- **Kurung Biasa**: Tuple ditulis menggunakan tanda kurung biasa atau tanda paranthesis `(...)`.
- **Akses Indeks**: Setiap elemen di dalam Tuple memiliki indeks berurutan berbasis nol (_zero-based indexing_), dimulai dari `0` untuk elemen pertama.
- **Tipe Data Campuran**: Sebuah Tuple dapat menyimpan elemen dengan tipe data berbeda (_mixed types_) maupun Tuple bersarang (_nested tuple_).
- **Deklarasi Tuple Kosong**: Tuple kosong dapat dideklarasikan menggunakan fungsi pembantu `tuple()` atau menggunakan kurung biasa kosong `()`.

|Karakteristik|Deskripsi Teknis|
|:--|:--|
|**Sifat Memori**|_Immutable_ (Read-Only)|
|**Sintaksis**|Kurung biasa `(...)`|
|**Pengindeksan**|Berbasis Nol (_Zero-based indexing_)|
|**Kompatibilitas**|Mendukung _mixed types_, elemen kosong, dan _nested tuple_|

---

## 4.2 Deklarasi Khusus Single Item Tuple

Dalam menulis Tuple yang hanya memiliki satu elemen (_single item tuple_), terdapat aturan penulisan sintaksis khusus yang wajib dipenuhi agar interpreter Python dapat mengenali objek tersebut sebagai Tuple, bukan sebagai tipe data primitif biasa.

- **Aturan Tanda Koma Akhir**: Anda wajib menambahkan tanda koma `,` langsung setelah elemen pertama di dalam tanda kurung.
- **Contoh Sintaksis Valid**: `my_tuple = (5,)`.
- **Konsekuensi Kegagalan Sintaksis**: Jika dideklarasikan tanpa tanda koma (misalnya `my_tuple = (5)`), Python akan mendeteksinya sebagai pengelompokan operasi matematika biasa (_parenthesis grouping_) dan variabel tersebut akan dideklarasikan sebagai tipe data `int` dengan nilai `5`.

---

## 4.3 Metode dan Fungsi Bawaan Tuple

Karena sifatnya yang _immutable_, Tuple tidak memiliki metode manipulasi elemen seperti `.append()` atau `.pop()`. Metode bawaan Tuple dirancang khusus hanya untuk mengakses nilai atau melakukan pelacakan informasi elemen.

Berikut adalah daftar metode dan fungsi bawaan yang dapat digunakan pada tipe data Tuple:

|Metode / Fungsi|Jenis|Deskripsi|
|:--|:--|:--|
|`.index(value)`|_Method_|Mengembalikan indeks posisi pertama dari nilai yang dicari. Menghasilkan error jika nilai tidak ditemukan.|
|`.count(value)`|_Method_|Menghitung dan mengembalikan frekuensi kemunculan nilai tertentu di dalam Tuple.|
|`len(tuple_obj)`|_Function_|Mengembalikan jumlah total elemen yang ada di dalam objek Tuple.|

---

## 4.4 Contoh Implementasi Kode Python

Di bawah ini adalah contoh penggunaan tipe data Tuple secara praktis yang bebas dari error sintaksis:

```bash
# Deklarasi Tuple Geolocation dan RGB
jakarta_geolocation = (-6.200000, 106.816666)
rgb_color = (255, 128, 0)

# Deklarasi Tuple Kosong
empty_tup_1 = tuple()
empty_tup_2 = ()

# Deklarasi Single Item Tuple (Wajib tanda koma)
single_item = (5,)

# Deklarasi Nested Tuple
nested_tuple = (1, (2, 3, 4), ("a", "b"))

# Mengakses elemen tunggal menggunakan indeks berbasis nol
latitude = jakarta_geolocation[0]
longitude = jakarta_geolocation[1]

# Penggunaan metode count, index, dan fungsi len
fibonacci_numbers = (1, 1, 2, 3, 5, 8, 13)

freq_of_one = fibonacci_numbers.count(1)     # Hasil: 2
index_of_five = fibonacci_numbers.index(5)   # Hasil: 4
total_elements = len(fibonacci_numbers)      # Hasil: 7

# Menampilkan hasil output
print("Latitude:", latitude)
print("Single Item Type:", type(single_item))
print("Jumlah elemen Fibonacci:", total_elements)
```

---

## **[Wawasan Diskusi / Audio Insight]**

### A. Penanganan Kegagalan Pencarian dengan Metode `.index()`

Berdasarkan penjelasan dosen dalam rekaman audio kelas, penggunaan metode `.index()` untuk mencari posisi elemen di dalam Tuple harus dilakukan secara hati-hati. Jika Anda memanggil metode `.index()` untuk nilai yang sama sekali tidak terdaftar di dalam Tuple, interpreter Python akan segera memicu kegagalan runtime berupa `ValueError: tuple.index(x): x not in tuple`.

Untuk mengatasi crash ini pada program nyata, praktisi AI Engineering disarankan melakukan pengecekan keanggotaan menggunakan operator `in` sebelum menjalankan pencarian indeks, atau menggunakan blok penanganan pengecualian `try-except`.

### B. Alasan Interpreter Python Mewajibkan Tanda Koma pada Single Item Tuple

Dalam sesi tanya jawab interaktif, dijelaskan secara mendalam mengapa Python mewajibkan penulisan koma pada Tuple beranggota tunggal seperti `(5,)`. Tanda kurung biasa `(...)` di Python memiliki peran ganda:

1. Sebagai pendefinisi objek Tuple.
2. Sebagai operator pengelompokan prioritas matematika (_parenthesis grouping_), seperti dalam rumus `(2 + 3) * 5`.

Apabila Anda menuliskan `my_tuple = (5)` tanpa koma, Python memprioritaskannya sebagai ekspresi matematika biasa, sehingga objek Tuple tidak pernah dibuat. Penambahan koma `,` di dalam kurung memberikan petunjuk mutlak kepada interpreter Python bahwa ekspresi tersebut harus dievaluasi sebagai sebuah objek Tuple.



## Bab 5 Indexing dan Slicing pada List dan Tuple

## 5.1 Indexing (Pengindeksan) Elemen Tunggal

Setiap elemen di dalam tipe data `list` dan `tuple` memiliki posisi spesifik yang disebut sebagai indeks. Indeks ini digunakan untuk menunjuk dan mengakses elemen tunggal secara langsung.

### 5.1.1 Aturan Pengindeksan Python

Python menggunakan sistem pengindeksan berbasis nol (_zero-based indexing_), yang berarti elemen pertama selalu dimulai dari indeks `0`. Python juga mendukung pengindeksan negatif untuk mempermudah akses elemen dari arah belakang.

- **Indeks Positif**: Dimulai dari `0` untuk elemen pertama di sebelah kiri, bergerak maju ke kanan (`1`, `2`, `3`, dst.).
- **Indeks Negatif**: Dimulai dari `-1` untuk elemen terakhir di sebelah kanan, bergerak mundur ke kiri (`-2`, `-3`, `-4`, dst.).

### 5.1.2 Tabel Skema Indeks Positif dan Negatif

Sebagai visualisasi, berikut adalah skema indeks untuk variabel list `students = ["andi", "budi", "cinta", "doni"]`:

|Elemen|"andi"|"budi"|"cinta"|"doni"|
|:--|:-:|:-:|:-:|:-:|
|**Indeks Positif**|`0`|`1`|`2`|`3`|
|**Indeks Negatif**|`-4`|`-3`|`-2`|`-1`|

### 5.1.3 Contoh Implementasi Kode Indexing

Sintaks dasar akses elemen tunggal adalah `list_or_tuple[index]`.

```Python
# Deklarasi List dan Tuple
students = ["andi", "budi", "cinta", "doni"]
coordinate = (-6.2, 106.8)

# Mengakses elemen pertama menggunakan indeks positif
nama_pertama = students[0]
print(nama_pertama)  # Output: "andi"

# Mengakses koordinat longitude menggunakan indeks positif
longitude = coordinate[1]
print(longitude)  # Output: 106.8

# Mengakses elemen terakhir menggunakan indeks negatif
nama_terakhir = students[-1]
print(nama_terakhir)  # Output: "doni"
```

---

## 5.2 Slicing (Pemotongan Bagian) Data

Slicing digunakan apabila program memerlukan sebagian porsi data (_portion_) atau sub-koleksi dari `list` atau `tuple`, bukan hanya satu elemen tunggal.

### 5.2.1 Format Sintaksis Slicing

Operasi slicing ditulis menggunakan kurung siku dengan format parameter sebagai berikut:

```Python
list_or_tuple[start:stop:step]
```

Berikut adalah rincian fungsional dari ketiga parameter di atas:

- **`start`**: Indeks awal pemotongan (inklusif). Jika dikosongkan, Python akan memulai dari indeks paling awal (`0`).
- **`stop`**: Indeks batas akhir pemotongan (eksklusif). Pemotongan hanya akan dilakukan hingga indeks `stop - 1`. Jika dikosongkan, pemotongan akan berjalan hingga elemen terakhir.
- **`step`**: Jarak lompatan antar elemen yang diambil selama proses pemotongan. Nilai default parameter ini adalah `1`.

### 5.2.2 Contoh Kasus Slicing

Berikut adalah contoh penerapan slicing pada list dan tuple:

```Python
students = ["andi", "budi", "cinta", "doni"]
coordinate = (-6.2, 106.8)

# 1. Mengambil elemen dari indeks 2 hingga akhir
some_students_1 = students[2:]
print(some_students_1)  # Output: ["cinta", "doni"]

# 2. Mengambil elemen dari awal hingga sebelum indeks 2 (indeks 0 dan 1)
some_students_2 = students[:2]
print(some_students_2)  # Output: ["andi", "budi"]

# 3. Mengambil elemen dengan melompati elemen (step = 2) dari indeks 0 hingga sebelum 3
some_students_3 = students[0:3:2]
print(some_students_3)  # Output: ["andi", "cinta"]

# 4. Menduplikasi atau mengambil seluruh elemen list/tuple
location = coordinate[:]
print(location)  # Output: (-6.2, 106.8)
```

---

## 5.3 Penanganan Kasus Out-of-Range (Batas Indeks)

Python memiliki karakteristik unik yang sangat berbeda dalam menangani kondisi batas indeks yang melampaui kapasitas elemen (_out-of-range_) antara operasi indexing langsung dan slicing.

### 5.3.1 Perbedaan Karakteristik Penanganan Batas Indeks

- **Akses Indexing Langsung**: Jika program mencoba mengakses satu indeks tertentu yang nilainya melebihi kapasitas elemen yang ada (misalnya mengakses indeks ke-10 pada list yang hanya memiliki 4 elemen), Python akan segera menghentikan program dan memicu error `IndexError: list index out of range`.
- **Akses Slicing**: Jika operasi slicing dideklarasikan melewati batas indeks elemen yang tersedia (misalnya melakukan slicing mulai dari indeks ke-10), Python tidak akan memicu error apa pun. Interpreter Python secara aman akan mengembalikan koleksi kosong (`[]` untuk list atau `()` untuk tuple).

### 5.3.2 Tabel Perbandingan Perilaku Batas Indeks

|Fitur / Operasi|Sintaksis Contoh|Kondisi Indeks|Perilaku Interpreter Python|
|:--|:--|:--|:--|
|**Indexing**|`students[10]`|Melebihi kapasitas (_out-of-range_)|Crash dengan memicu `IndexError`|
|**Slicing**|`students[10:]`|Melebihi kapasitas (_out-of-range_)|Lolos tanpa error, mengembalikan koleksi kosong (`[]` atau `()`)|

```Python
students = ["andi", "budi", "cinta", "doni"]

# Contoh penanganan out-of-range pada Slicing (Aman dari error)
slicing_kosong = students[10:]
print(slicing_kosong)  # Output: []
```

---

## **[Wawasan Diskusi / Audio Insight]**

### A. Efisiensi Penggunaan Indeks Negatif `-1`

Di dalam rekaman kelas, dosen menekankan pentingnya pembiasaan penggunaan indeks negatif `-1` untuk mengambil data terakhir dari sebuah list atau tuple. Pendekatan ini dinilai jauh lebih efisien dan intuitif secara industri karena pengembang tidak perlu memanggil fungsi `len(list_or_tuple) - 1` untuk menghitung total elemen terlebih dahulu hanya untuk menjangkau elemen paling akhir.

### B. Mekanisme Keamanan Slicing Terhadap Crash Aplikasi

Dalam sesi diskusi praktis, dijelaskan alasan mengapa Python membiarkan operasi slicing yang di luar rentang (_out-of-range_) tetap berjalan tanpa memicu crash. Slicing dirancang untuk mengambil "porsi segmen data yang tersedia". Apabila segmen yang diminta berada di luar batas elemen aktual, Python mengasumsikan bahwa tidak ada elemen yang dapat diiris pada rentang tersebut, sehingga mengembalikan kontainer kosong (`[]` atau `()`) dianggap sebagai output logis yang aman untuk kelancaran jalannya aplikasi (_fail-safe mechanism_).



## Bab 6 Tipe Data Python Set

## 6.1 Konsep Dasar Set

Set adalah tipe data koleksi di Python yang digunakan untuk menyimpan elemen-elemen unik secara otomatis dengan menghapus seluruh nilai duplikat. Sifat ini sangat berguna dalam menyaring data yang terdaftar lebih dari satu kali secara tidak sengaja.

### 6.1.1 Karakteristik Utama Set

Set memiliki karakteristik teknis yang membedakannya secara signifikan dari List dan Tuple:

- **Unordered (Tidak Terurut)**: Elemen di dalam Set tidak memiliki posisi atau urutan yang konsisten.
- **Unindexed (Tidak Memiliki Indeks)**: Karena tidak terurut, elemen Set tidak dapat diakses menggunakan indeks seperti `my_set[0]`. Upaya melakukan indexing langsung pada Set akan menghasilkan kesalahan `TypeError: 'set' object is not subscriptable`.
- **Unique Elements Only**: Set secara otomatis mengabaikan dan menghapus nilai duplikat saat inisialisasi maupun saat manipulasi data.

### 6.1.2 Tabel Karakteristik Deklarasi Set

Berikut adalah rangkuman aturan penulisan dan deklarasi Set di Python:

| Kasus Deklarasi              | Sintaksis           | Keterangan Teknis                                                                                                                                                               |
| :--------------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Set dengan elemen            | `{val1, val2, ...}` | Ditulis menggunakan kurung kurawal `{...}` dengan pemisah koma antar elemen.                                                                                                    |
| Set kosong                   | `set()`             | Wajib dideklarasikan menggunakan fungsi `set()`.                                                                                                                                |
| Kurung kurawal kosong        | `{}`                | **DILARANG** untuk Set kosong karena Python otomatis mendeteksinya sebagai Dictionary kosong.                                                                                   |
| Set Bersarang (_Nested Set_) | `frozenset()`       | Set tidak dapat langsung menampung Set lain sebagai elemennya karena elemen Set harus bersifat _hashable_ (_immutable_). Set bagian dalam wajib dibungkus dengan `frozenset()`. |

---

## 6.2 Metode dan Fungsi Bawaan Set

Sebagai objek _mutable_, elemen di dalam Set dapat ditambah atau dihapus setelah dideklarasikan. Berikut adalah metode-metode manipulasi Set yang disediakan oleh Python:

### 6.2.1 Penambahan Elemen

- `.add(item)`: Menambahkan satu elemen tunggal ke dalam Set.
- `.update(iterable)`: Menambahkan banyak elemen sekaligus dari objek lain yang bersifat _iterable_ (seperti List, Tuple, atau Set lain).

### 6.2.2 Penghapusan Elemen

- `.remove(value)`: Menghapus elemen tertentu berdasarkan nilainya. Jika nilai yang dicari tidak ditemukan di dalam Set, Python akan memicu kesalahan `KeyError`.
- `.discard(value)`: Menghapus elemen tertentu berdasarkan nilainya secara aman. Jika nilai yang dicari tidak ditemukan, metode ini tidak akan memicu kesalahan dan eksekusi program tetap berjalan normal.
- `.pop()`: Menghapus dan mengembalikan satu elemen acak dari Set. Karena Set bersifat tidak terurut, elemen yang dihapus tidak dapat diprediksi secara konsisten.
- `.clear()`: Mengosongkan seluruh isi Set, menghasilkan Set kosong yang setara dengan `set()`.

### 6.2.3 Fungsi Umum & Duplikasi

- `len(set_name)`: Mengembalikan jumlah elemen unik yang tersimpan di dalam Set.
- `.copy()`: Membuat salinan dangkal (_shallow copy_) dari Set pada alamat memori yang berbeda untuk mencegah terjadinya bug referensi memori yang sama.

---

## 6.3 Operasi Matematika Set (_Set Operations_)

Set di Python mendukung operasi aljabar himpunan matematika. Operasi ini dapat dilakukan baik menggunakan metode bawaan (_built-in methods_) maupun operator simbolis khusus.

### 6.3.1 Tabel Ringkasan Operasi Himpunan

| Operasi                  | Deskripsi Himpunan                                                             | Metode Bawaan               | Operator | Contoh Hasil (`A` dan `B`)                           |
| :----------------------- | :----------------------------------------------------------------------------- | :-------------------------- | :------- | :--------------------------------------------------- |
| **Union**                | Menggabungkan seluruh elemen unik dari kedua himpunan.                         | `A.union(B)`                | `A \|B`  |                                                      |
| **Intersection**         | Mengambil elemen yang ada di kedua himpunan secara bersamaan.                  | `A.intersection(B)`         | `A & B`  | `A = {'a', 'b'}, B = {'b', 'c'}` Hasil: `{'b'}`      |
| **Difference**           | Mengambil elemen himpunan pertama yang tidak ada di himpunan kedua.            | `A.difference(B)`           | `A - B`  | `A = {'a', 'b'}, B = {'b', 'c'}` Hasil: `{'a'}`      |
| **Symmetric Difference** | Mengambil elemen unik dari masing-masing himpunan yang tidak saling beririsan. | `A.symmetric_difference(B)` | `A ^ B`  | `A = {'a', 'b'}, B = {'b', 'c'}` Hasil: `{'a', 'c'}` |

### 6.3.2 Hubungan dan Perbandingan Antar Himpunan

Python juga menyediakan operator pembanding untuk menganalisis hubungan relasional antara dua himpunan:

- **Subset (`.issubset()` atau `<=`)**: Mengembalikan nilai `True` jika seluruh elemen himpunan `A` terkandung di dalam himpunan `B`.
- **Superset (`.issuperset()` atau `>=`)**: Mengembalikan nilai `True` jika seluruh elemen himpunan `B` terkandung di dalam himpunan `A`.
- **Proper Subset (`<`)**: Mengembalikan nilai `True` jika `A` adalah subset dari `B` dan himpunan `A` tidak sama dengan `B` (ada elemen di `B` yang tidak dimiliki `A`).
- **Proper Superset (`>`)**: Mengembalikan nilai `True` jika `A` adalah superset dari `B` dan himpunan `A` tidak sama dengan `B`.

---

## **[Wawasan Diskusi / Audio Insight]**

### A. Interoperabilitas Tipe Data: Konversi Timbal Balik List dan Set

Berdasarkan diskusi interaktif di kelas, terdapat penjelasan penting mengenai konversi tipe data:

- List dapat dikonversi ke Set menggunakan fungsi `set(my_list)` untuk menyaring nilai duplikat secara instan.
- Set yang telah bersih dari duplikat dapat dikonversi kembali menjadi List menggunakan fungsi `list(my_set)` sehingga datanya dapat dimanipulasi menggunakan indeks.
- **Konsekuensi Memori**: Proses konversi ini bersifat destruktif terhadap elemen duplikat asal. Elemen duplikat yang telah dibuang saat diubah menjadi Set tidak akan bisa dikembalikan lagi saat dikonversi ulang menjadi List.

### B. Studi Kasus Latihan Kelas: Analisis Pembagian Kelas Siswa

Dalam sesi latihan mandiri kelas, siswa memecahkan studi kasus pembagian siswa berdasarkan dua kelas minat, yaitu `Python Class` dan `SQL Class`. Implementasi logisnya menggunakan metode aljabar himpunan sebagai berikut:

1. **Mencari Siswa yang Mengambil Kedua Kelas (Irisan/Intersection)**: Digunakan untuk mendeteksi siswa yang terdaftar di kelas Python sekaligus kelas SQL. Contohnya, siswa bernama Citra dan Doni yang aktif di kedua kelas tersebut.
2. **Mencari Siswa yang Hanya Mengambil Satu Kelas (Beda Setara/Symmetric Difference)**: Digunakan untuk memisahkan siswa yang hanya mengambil salah satu kelas saja (tidak terdaftar di kedua kelas sekaligus), seperti Andi, Budi, Efraim, dan Fajar.
3. **Mencari Siswa yang Hanya Mengambil Kelas Python (Selisih/Difference)**: Digunakan untuk memisahkan siswa kelas Python murni dengan mengeluarkan nama siswa yang juga mengambil kelas SQL, menghasilkan nama Andi dan Budi.

---

## 6.4 Contoh Implementasi Kode Python

Berikut adalah contoh kode implementasi manipulasi Set dan penyelesaian studi kasus pembagian kelas yang bebas dari kesalahan sintaks:

```Python
# 1. Deklarasi Set dan penyaringan duplikat dari List
student_list = ["andi", "budi", "citra", "andi", "doni", "efraim", "citra"]
attendance_set = set(student_list)
print("Hasil Set unik:", attendance_set)

# 2. Deklarasi Set kosong dan manipulasi elemen
movie_set = set()
movie_set.add("Inception")
movie_set.update(["The Matrix", "Searching"])
movie_set.discard("La La Land")  # Menghapus secara aman tanpa error
print("Daftar film:", movie_set)

# 3. Studi Kasus Pembagian Kelas Minat Siswa
python_class = {"andi", "budi", "citra", "doni"}
sql_class = {"citra", "doni", "efraim", "fajar"}

# Menghitung siswa yang mengambil kedua kelas (Intersection)
both_classes = python_class & sql_class
print("Siswa di kedua kelas:", both_classes)

# Menghitung siswa yang hanya mengambil salah satu kelas (Symmetric Difference)
one_class_only = python_class ^ sql_class
print("Siswa di satu kelas saja:", one_class_only)

# Menghitung siswa yang hanya mengambil kelas Python saja (Difference)
pure_python = python_class - sql_class
print("Siswa kelas Python saja:", pure_python)
```



## Bab 7 Tipe Data Python Dictionary

## 7.1 Konsep Dasar dan Karakteristik Dictionary

Python Dictionary adalah tipe data koleksi yang menyimpan data dalam bentuk pasangan _key-value_ (kunci-nilai). Struktur ini dirancang untuk mempermudah pencarian dan pengambilan data secara cepat menggunakan sebuah _key_ sebagai pencari, berbeda dengan List atau Tuple yang mengandalkan posisi indeks angka.

### 7.1.1 Aturan Penulisan dan Karakteristik Key-Value

- **Sintaksis**: Ditulis menggunakan kurung kurawal `{...}` dengan pasangan _key_ dan _value_ yang dipisahkan oleh tanda titik dua (`key: value`). Masing-masing item (pasangan _key-value_) dipisahkan dengan tanda koma.
- **Keunikan Key**: _Key_ bertindak sebagai pengindeks unik di dalam dictionary sehingga tidak boleh ada _key_ yang duplikat. Jika terdapat _key_ yang sama saat deklarasi, nilai terakhir akan menimpa nilai sebelumnya.
- **Sifat Value**: _Value_ di dalam dictionary bebas, diperbolehkan memiliki nilai yang sama (duplikat), dan dapat berupa tipe data apa pun (string, integer, float, boolean, list, tuple, set, atau dictionary lain).
- **Mutability**: Dictionary termasuk dalam kategori tipe data yang _mutable_ (dapat diubah). Pengguna dapat menambah, menghapus, atau memperbarui pasangan _key-value_ setelah objek dideklarasikan di memori.

### 7.1.2 Tabel Karakteristik Komponen Dictionary

|Komponen|Karakteristik Utama|Keunikan|Sifat Mutability|Tipe Data yang Diperbolehkan|
|:--|:--|:--|:--|:--|
|**Key**|Bertindak sebagai alamat/indeks|Harus Unik|Immutable|Tipe data dasar yang bersifat hashable (string, number, tuple)|
|**Value**|Data yang disimpan|Boleh Duplikat|Mutable / Immutable|Semua jenis tipe data (termasuk list dan dictionary lain)|
|**Item**|Representasi satu pasang _key-value_|Ditentukan oleh _Key_|Mutable|Gabungan pasangan _key_ dan _value_|

---

## 7.2 Deklarasi Dictionary

Deklarasi dictionary dapat dilakukan untuk membuat objek baru, baik objek kosong maupun objek yang sudah memiliki data awal.

### 7.2.1 Cara Deklarasi Dictionary Kosong

Terdapat dua cara untuk membuat dictionary kosong di Python:

1. Menggunakan kurung kurawal kosong `{}`.
2. Menggunakan fungsi bawaan `dict()`.

_Catatan penting: Pendeklarasian menggunakan kurung kurawal kosong `{}` otomatis diidentifikasi sebagai dictionary kosong oleh Python, bukan set kosong._

### 7.2.2 Cara Deklarasi Dictionary dengan Data Awal

Penulisan data awal dilakukan dengan format pasangan langsung di dalam kurung kurawal. Dictionary juga mendukung struktur bersarang (_nested dictionary_) di mana sebuah _value_ di dalamnya berupa dictionary lain.

```python
# Deklarasi dictionary kosong
empty_dict_1 = {}
empty_dict_2 = dict()

# Deklarasi dictionary standar
student_data = {
    "name": "andi",
    "grade": 12,
    "is_graduate": False
}

# Deklarasi nested dictionary (dictionary bersarang)
sample_nested = {
    "text": "hello",
    "num": 3.14,
    "flag": True,
    "list_data": [1, 2],
    "nested_dict": {"x": 10}
}
```

---

## 7.3 Akses dan Pembaruan Nilai Dictionary

### 7.3.1 Mengakses Nilai (_Accessing Value_)

Untuk mengambil nilai (_value_) dari dictionary, terdapat dua metode utama:

1. **Menggunakan Kurung Siku (`dictionary["key"]`)**: Metode ini mengakses nilai secara langsung lewat kata kunci. Jika _key_ yang dicari tidak terdaftar, Python akan langsung memicu error berupa `KeyError` dan menghentikan jalannya program.
2. **Menggunakan Metode `.get(key, default_value)`**: Metode ini jauh lebih aman untuk menghindari crash. Jika _key_ ditemukan, metode ini mengembalikan nilainya. Jika tidak ditemukan, metode ini akan mengembalikan nilai default yang ditentukan (atau `None` jika nilai default dikosongkan) tanpa memicu error.

### 7.3.2 Memperbarui atau Menambah Nilai (_Updating or Adding Value_)

Pembaruan data atau penambahan pasangan baru dapat dilakukan secara langsung dengan sintaksis penugasan nilai:

```python
dictionary["key"] = value
```

- Jika _key_ **sudah ada**, nilai lama akan langsung ditimpa (_overwrite_) dengan nilai baru.
- Jika _key_ **belum ada**, Python otomatis akan membuat pasangan _key-value_ baru di dalam dictionary tersebut.

```python
student_data = {
    "name": "andi",
    "age": 20,
    "major": "physics",
    "gpa": 3.2,
    "is_graduated": False
}

# Mengakses nilai dengan kurung siku
print(student_data["name"])  # Output: andi

# Mengakses nilai dengan .get() secara aman
# Key "is_active" tidak ada di dictionary, sehingga mengembalikan nilai default (False)
status_aktif = student_data.get("is_active", False)
print(status_aktif)  # Output: False

# Memperbarui nilai yang sudah ada
student_data["is_graduated"] = True

# Menambahkan pasangan key-value baru karena key "scholarship" belum ada
student_data["scholarship"] = True
```

---

## 7.4 Metode dan Fungsi Bawaan Dictionary

Python menyediakan berbagai metode bawaan (_built-in methods_) dan fungsi untuk memanipulasi serta mengelola data di dalam dictionary.

### 7.4.1 Tabel Metode Manipulasi dan Informasi Dictionary

|Metode|Deskripsi Kerja|Contoh Sintaksis|Hasil Tindakan|
|:--|:--|:--|:--|
|`.update()`|Menambah atau memperbarui satu atau lebih pasangan _key-value_ sekaligus.|`dict.update({"gpa": 3.5})`|Mengubah nilai "gpa" menjadi 3.5|
|`.setdefault()`|Mengambil nilai dari _key_; jika _key_ belum ada, otomatis menambahkannya dengan nilai default.|`dict.setdefault("minor", "math")`|Menambah "minor": "math" jika belum ada|
|`.get()`|Mengambil nilai berdasarkan _key_ secara aman tanpa memicu crash program.|`dict.get("age", 0)`|Mengembalikan nilai "age" atau 0 jika tidak ada|
|`.keys()`|Mengembalikan seluruh _keys_ di dalam objek koleksi khusus.|`dict.keys()`|Berupa `dict_keys([...])`|
|`.values()`|Mengembalikan seluruh _values_ di dalam objek koleksi khusus.|`dict.values()`|Berupa `dict_values([...])`|
|`.items()`|Mengembalikan seluruh pasangan _key-value_ dalam bentuk tuple.|`dict.items()`|Berupa `dict_items([(*key*, *value*), ...])`|
|`.pop()`|Menghapus item berdasarkan _key_ yang ditentukan dan mengembalikan nilainya.|`dict.pop("is_graduated")`|Menghapus item dan mengembalikan status boolean-nya|
|`.popitem()`|Menghapus dan mengembalikan pasangan _key-value_ yang terakhir kali dimasukkan.|`dict.popitem()`|Mengembalikan tuple pasangan terakhir yang dihapus|
|`.clear()`|Menghapus seluruh pasangan _key-value_ hingga dictionary menjadi kosong.|`dict.clear()`|Objek dictionary menjadi kosong `{}`|
|`.copy()`|Membuat salinan baru di alamat memori berbeda (_shallow copy_).|`new_dict = dict.copy()`|Mencegah perubahan data pada objek asli|

### 7.4.2 Fungsi Umum Bawaan Python

- **`len(dictionary)`**: Digunakan untuk menghitung jumlah total elemen (pasangan _key-value_) yang tersimpan di dalam dictionary.
- **`sorted(dictionary)`**: Digunakan untuk mengurutkan kata kunci (_keys_) di dalam dictionary secara naik (_ascending_/alfabetis) dan mengembalikan hasilnya dalam bentuk sebuah List baru. Fungsi ini tidak mengubah susunan dictionary asli.

```python
student_data = {
    "name": "andi",
    "age": 20,
    "major": "physics",
    "gpa": 3.2,
    "is_graduated": False
}

# 1. Menggunakan .update()
student_data.update({"gpa": 3.5, "is_active": True})

# 2. Menggunakan .setdefault()
student_data.setdefault("minor", "mathematics")

# 3. Mengambil informasi Keys, Values, dan Items
semua_kunci = student_data.keys()
semua_nilai = student_data.values()
semua_pasangan = student_data.items()

# 4. Menghapus data dengan .pop()
nilai_terhapus = student_data.pop("is_graduated")

# 5. Mengurutkan keys menggunakan sorted()
kunci_terurut = sorted(student_data)
```

---

## **[Wawasan Diskusi / Audio Insight]**

### A. Penyederhanaan Logika Lookup ID Siswa (Studi Kasus Latihan Kelas)

Pada sesi latihan kelas, terdapat tugas pemrograman di mana siswa diminta membuat fungsi untuk mencari nama siswa berdasarkan kode ID yang diinputkan pengguna. Ketentuannya: jika ID tidak ditemukan, sistem harus menampilkan tulisan `"not found"`.

Dalam diskusi kelas, salah satu siswa (Anwar) menggunakan pendekatan kondisional klasik `if-else` untuk mengevaluasi apakah hasil pencarian bernilai kosong atau tidak. Kerangka berpikir kondisional tersebut adalah sebagai berikut:

```python
# Pendekatan kondisional if-else (kurang efisien)
hasil_cari = student_dict.get(input_id)
if hasil_cari == None:
    print("not found")
else:
    print(hasil_cari)
```

Dosen memberikan koreksi penting untuk memotong redundansi kode tersebut. Metode `.get()` bawaan Python memiliki parameter opsional kedua yang dirancang khusus sebagai nilai pengembalian default (_default value_). Dengan memanfaatkan fitur ini, logika di atas dapat diringkas menjadi satu baris kode yang jauh lebih efisien, bersih, dan mudah dibaca:

```
# Solusi satu baris yang disarankan dosen
print(student_dict.get(input_id, "not found"))
```

Penerapan ini menghilangkan kebutuhan pemeriksaan manual `if-else` karena interpreter Python akan langsung menangani penyaringan tersebut di tingkat internal.

### B. Perbedaan Perilaku Kerja: `.update()` vs `.setdefault()`

Berdasarkan penjelasan dosen di kelas, terdapat perbedaan mendasar pada cara kerja manipulasi data antara metode `.update()` dan `.setdefault()`:

- Metode `.update()` bertindak secara agresif. Jika _key_ yang dimasukkan sudah ada di dalam dictionary, maka nilai lama akan langsung ditimpa (_overwritten_). Jika _key_ belum ada, baru pasangan tersebut ditambahkan.
- Metode `.setdefault()` bertindak secara pasif/defensif. Metode ini **hanya akan menambahkan data jika key yang dimaksud belum ada** di dalam dictionary. Jika _key_ tersebut sudah terdaftar, metode ini tidak akan mengubah nilai asli yang tersimpan dan hanya mengembalikan nilai lama yang ada.

### C. Karakteristik Pengurutan Dictionary Menggunakan `sorted()`

Sering terjadi kesalahpahaman bahwa fungsi `sorted()` akan mengurutkan seluruh struktur dictionary beserta nilainya. Dosen menegaskan bahwa fungsi `sorted(student_data)` hanya akan mengekstrak kata kunci (_keys_) saja, mengurutkannya secara alfabetis atau menaik, lalu mengembalikannya sebagai tipe data List baru. Nilai (_values_) di dalam dictionary sama sekali tidak diikutkan dalam proses pengurutan ataupun diubah posisinya.



## Bab 8 Praktik Logika Pemecahan Masalah (Problem Solving) Mandiri

## 8.1 Pengenalan Platform HackerRank

HackerRank adalah platform evaluasi kode daring (_online code evaluation platform_) yang digunakan oleh pengembang (_developer_) untuk melatih logika pemrograman secara interaktif, serta digunakan oleh industri sebagai instrumen penyaringan kandidat teknis.

### 8.1.1 Prosedur Pendaftaran Akun (_Sign Up_)

Siswa wajib melakukan pendaftaran akun mandiri untuk mulai mengerjakan tantangan pemrograman dengan ketentuan:

- Mengakses portal resmi di alamat `hackerrank.com`.
- Memilih opsi registrasi khusus untuk pengembang, yaitu **"For Developers"**. Opsi ini menyediakan akses gratis (_free_) tanpa batasan waktu untuk modul-modul dasar latihan.
- Mengisi data kredensial atau menghubungkannya dengan akun GitHub atau email personal untuk verifikasi identitas.

### 8.1.2 Navigasi Jalur Persiapan (_Prepare Path_)

Setelah proses autentikasi berhasil, siswa mengarahkan navigasi dasbor ke bagian persiapan:

- Memilih menu **Prepare** di dalam dasbor utama.
- Memilih spesialisasi bahasa pemrograman: **Python**.
- Mengonfigurasi parameter penyaringan agar materi yang muncul sesuai dengan cakupan kelas dasar.

---

## 8.2 Struktur Latihan dan Kurikulum Rekomendasi

Untuk melatih pola pikir yang terstruktur serta menguji pemahaman sintaksis, HackerRank menyediakan kurikulum terfragmentasi berdasarkan tingkat kesulitan dan materi pembelajaran.

### 8.2.1 Parameter Penyaringan Kategori Latihan

Siswa diinstruksikan untuk menggunakan konfigurasi filter berikut guna membatasi cakupan pencarian tantangan pemrograman:

|Parameter Filter|Pengaturan Rekomendasi|Deskripsi|
|:--|:--|:--|
|**Difficulty**|_Easy_ (Mudah)|Menyediakan tantangan tingkat dasar untuk memperkuat sintaksis bahasa pemrograman.|
|**Subdomain**|_Python Basic_|Fokus pada fitur bawaan bahasa Python tanpa melibatkan pustaka (_library_) eksternal yang kompleks.|

### 8.2.2 Daftar Tantangan Pemecahan Masalah yang Direkomendasikan

Tantangan pemrograman di dalam subdomain Python dianjurkan untuk dikerjakan dari tingkat paling dasar dengan rincian topik sebagai berikut:

- **Pernyataan Kondisional & Operator Aritmatika**:
    - _Python If-Else_
    - _Arithmetic Operators_
    - _Python: Division_
- **Algoritma Perulangan & Fungsi Cetak**:
    - _Loops_
    - _Write a function_
    - _Print Function_
- **Manipulasi Struktur & Koleksi Data**:
    - _List Comprehensions_
    - _Find the Runner-Up Score!_
    - _Nested Lists_
    - _Finding the percentage_
    - _Lists_
    - _Tuples_
    - _sWAP cASE_

---

## 8.3 Signifikansi Problem Solving dalam Karier AI Engineer

Kemampuan menyelesaikan masalah pemrograman (_problem solving_) merupakan kualifikasi teknis yang krusial bagi calon profesional kecerdasan buatan (_AI_).

### 8.3.1 Peran dalam Tahapan Seleksi Kerja

- **Ujian Teknis (_Technical Test_)**: Rekrutmen posisi AI Engineer di industri modern hampir selalu menempatkan tes logika pemrograman daring sebagai gerbang penyaringan awal.
- **Dampak Kritis**: Kegagalan dalam menyelesaikan tantangan pemrograman dasar pada tahap seleksi awal ini akan langsung membatalkan kelanjutan kandidat ke babak wawancara teknis berikutnya, terlepas dari keahlian mereka dalam pemodelan kecerdasan buatan (_AI modeling_).

### 8.3.2 Pembentukan Pola Pikir Terstruktur

Latihan memecahkan masalah pemrograman secara berulang bertujuan untuk:

- Melatih logika berpikir logis dan berurutan saat menyusun kode.
- Meningkatkan efisiensi pemilihan tipe data koleksi (seperti kapan harus menggunakan List vs Set atau Dictionary) berdasarkan kebutuhan kompleksitas algoritma.
- Membiasakan pengembang dengan pengujian kode secara otomatis melalui berbagai skenario kasus uji (_test cases_).

---

## **[Wawasan Diskusi / Audio Insight]**

### A. Strategi Pemilihan Soal Berdasarkan Metrik Success Rate

Dalam diskusi interaktif di kelas, dosen memberikan panduan taktis bagi siswa dalam menavigasi tumpukan tantangan di platform HackerRank:

- **Memahami Metrik Success Rate**: Setiap soal latihan menyertakan indikator tingkat keberhasilan, seperti `89%`. Persentase ini mengindikasikan tingkat kemudahan soal secara statistik—semakin mendekati 100%, semakin banyak pengembang yang berhasil menyelesaikan seluruh kasus uji dengan benar.
- **Rekomendasi Alur Belajar**: Siswa yang baru memulai disarankan untuk mengurutkan atau memilih soal yang memiliki _success rate_ tinggi terlebih dahulu untuk membiasakan diri dengan format pengumpulan kode, sebelum beralih secara bertahap ke soal dengan _success rate_ lebih rendah atau tingkat kesulitan _Medium_ dan _Hard_.

### B. Solusi Masalah Pendaftaran Akun

Selama pelaksanaan praktikum di kelas, terdapat laporan siswa yang mengalami kegagalan pendaftaran akibat kesalahan pemilihan jenis akun. Dosen meluruskan bahwa portal HackerRank membagi registrasi menjadi dua kategori besar:

- Portal untuk industri/perekrut (_For Employers_).
- Portal untuk pengembang/siswa (_For Developers_).

Pendaftaran mandiri untuk latihan harus diselesaikan melalui opsi **"For Developers"** agar mendapatkan akses kurikulum belajar gratis tanpa batasan waktu trial.



## Notes Module 1 Session 4 Data Types Collection Notes

Dictionary bisa didaftarkan dengan contoh
```bash
dictionary["key"]
```



---


# Module 1 Session 5 Python Function & File Handling


## Bab 1 Python Function (Fungsi Python)



Study Guide ini disusun secara terstruktur untuk membahas konsep dasar, implementasi, serta praktik terbaik dalam pembuatan _function_ di Python berdasarkan modul materi resmi dan wawasan lisan yang disampaikan selama diskusi kelas.

---

## 1.1 Definisi dan Konsep Dasar Fungsi (Function Definition)

### A. Fondasi Konseptual

- **Analogi Resep Masakan**: Sebuah _function_ dianalogikan seperti sebuah resep masakan. Resep tersebut menentukan bahan-bahan yang dibutuhkan (_inputs_), langkah-langkah pembuatan yang harus diikuti (_logic_), serta hidangan hasil akhir yang akan didapatkan (_output_).
- **Prinsip Sekali Tulis**: Mendefinisikan sebuah _function_ setara dengan menuliskan resep masakan lalu menyerahkannya kepada Python. Setelah resep tersebut dipahami oleh Python, kita hanya perlu memanggil namanya kapan pun membutuhkan hasil yang sama, tanpa harus menulis ulang langkah-langkah logika tersebut dari awal.

### B. Karakteristik Utama

- **Blok Kode Terorganisir**: _Function_ adalah blok kode terpisah yang dirancang khusus untuk mengeksekusi satu tugas spesifik secara berulang (_specific task_).
- **Keyword Pendefinisian**: Di dalam Python, pembuatan _function_ dapat dilakukan menggunakan dua kata kunci utama, yaitu kata kunci `def` atau kata kunci `lambda`.

#### [Wawasan Diskusi / Audio Insight]

- **Kapan Harus Membuat Function**: Dosen menekankan bahwa _function_ dibuat untuk membungkus kode yang akan dijalankan berulang kali. Apabila suatu proses hanya akan dijalankan satu kali saja di dalam seluruh rangkaian program, maka pembuatan _function_ sebenarnya tidak terlalu krusial atau tidak dibutuhkan. Tujuan utamanya adalah melakukan generalisasi langkah-langkah logis agar program menjadi lebih efisien.

---

## 1.2 Fungsi Bawaan (Built-In Function)

### A. Karakteristik Built-In Function

- **Langsung Tersedia**: Python menyediakan sejumlah fungsi yang siap digunakan secara langsung sejak interpreter Python dijalankan.
- **Tanpa Konfigurasi Tambahan**: Pengguna tidak perlu mendefinisikan logika fungsi tersebut secara manual atau mengimpor (_import_) modul eksternal apa pun sebelum memanggilnya.

### B. Daftar Istilah Built-In Function

Karakteristik beberapa _built-in function_ yang sering digunakan di dalam Python dirangkum dalam tabel berikut:

|Nama Built-In Function|Karakteristik / Deskripsi Singkat|
|:--|:--|
|`print()`|Menampilkan data atau teks hasil komputasi ke layar atau konsol.|
|`len()`|Menghitung panjang atau jumlah elemen di dalam suatu objek koleksi data.|
|`input()`|Menerima baris input teks langsung dari pengguna melalui keyboard.|
|`range()`|Menghasilkan urutan angka numerik berdasarkan interval tertentu.|

---

## 1.3 Fungsi dengan Kata Kunci def (Function with def)

### A. Sintaksis dan Pembuatan Objek

- **Sintaks Standar**: Pendefinisian standar menggunakan kata kunci `def` diikuti dengan nama fungsi, tanda kurung `()`, titik dua `:`, dan blok kode logika yang menjorok ke dalam (_indented block_).
- **Alokasi Memori**: Saat kita mendefinisikan fungsi menggunakan `def`, Python akan membuat sebuah objek fungsi (_function object_) di memori komputer yang menyimpan seluruh instruksi logika di dalam tubuh fungsi tersebut, kemudian mengaitkan nama fungsi sebagai referensi penunjuk (_pointer_) ke objek tersebut.

### B. Proses Pemanggilan Fungsi (Calling a Function)

- **Eksekusi Logika**: Untuk mengeksekusi objek fungsi tersebut, kita memanggil namanya diikuti dengan tanda kurung `()`.
- **Transfer Kendali**: Saat fungsi dipanggil, kendali program secara otomatis berpindah (_transfer_) ke blok definisi fungsi untuk mengeksekusi semua baris kode di dalamnya. Setelah seluruh kode selesai dieksekusi, kendali program akan melompat kembali ke pernyataan setelah baris pemanggilan fungsi tersebut.

#### [Wawasan Diskusi / Audio Insight]

- **Perbedaan Pemanggilan dengan Kurung vs Tanpa Kurung**: Dalam sesi demo, diperlihatkan bahwa jika kita menuliskan nama fungsi tanpa menggunakan tanda kurung (misalnya `print(greet)`), Python hanya akan mengembalikan representasi objek fungsi tersebut beserta alamat memorinya (seperti `<function greet at 0x...>` ). Namun, jika dipanggil menggunakan kurung (seperti `greet()`), program akan beralih mengeksekusi logika internalnya.
- **Fleksibilitas Input-Output**: Fungsi dapat dirancang tanpa memiliki input maupun output sama sekali. Struktur fungsi fleksibel dan dapat dikategorikan menjadi empat jenis: memiliki input dan output, hanya memiliki input, hanya memiliki output, atau tidak memiliki keduanya.

---

## 1.4 Fungsi dengan Input (Function with Input)

### A. Parameter dan Argumen

Untuk meningkatkan fleksibilitas sehingga fungsi dapat menghasilkan keluaran yang dinamis sesuai dengan kondisi penggunaan, kita dapat mendefinisikannya dengan input menggunakan variabel khusus.

|Istilah Teknis|Definisi dan Karakteristik|
|:--|:--|
|_Parameter_|Variabel penampung (_placeholder_) yang dideklarasikan di dalam tanda kurung pada bagian definisi fungsi.|
|_Argument_|Nilai nyata (_actual value_) yang dikirimkan ke fungsi saat fungsi tersebut dipanggil.|

### B. Nilai Bawaan (Default Value)

- **Fungsi Default**: Kita dapat menentukan nilai bawaan (_default value_) pada parameter fungsi. Jika kita tidak mengirimkan argumen apa pun saat memanggil fungsi tersebut, Python secara otomatis akan menggunakan nilai bawaan yang telah didefinisikan.
- **Sintaks Default Value**: Ditulis dengan format `parameter = value` di dalam kurung definisi fungsi.

#### [Wawasan Diskusi / Audio Insight]

- **Studi Kasus Parameter `time=None`**: Pada contoh fungsi `greet(name="Bob", time=None)`, parameter `time` diberi nilai default `None`. Logika internal menggunakan pengkondisian `if time:` untuk mendeteksi apakah argumen `time` dikirimkan oleh pengguna atau tidak. Jika bernilai `None` (yang dievaluasi sebagai _False_), program akan melompat ke blok `else:` dan hanya menyapa nama saja.

---

## 1.5 Pernyataan Kembalian (return Statement)

### A. Peran return versus print()

- **Batas Tampilan `print()`**: Fungsi `print()` hanya bertugas menampilkan hasil langsung ke layar monitor, sehingga nilai tersebut tidak dapat disimpan atau dimanfaatkan kembali dalam komputasi program.
- **Penyimpanan Hasil dengan `return`**: Pernyataan `return` digunakan untuk mengirimkan nilai kembali (_send a value back_) ke baris tempat fungsi tersebut dipanggil. Nilai ini kemudian dapat disimpan ke dalam variabel, digunakan kembali untuk kalkulasi berikutnya, atau dikirimkan ke fungsi lain.

### B. Karakteristik Fungsi Berdasarkan Keberadaan return

|Jenis Fungsi|Karakteristik Aliran Data|Hasil jika Ditangkap Variabel|
|:--|:--|:--|
|**Tanpa `return`**|Logika fungsi dieksekusi, nilai hasil komputasi hanya berada di dalam lingkup lokal fungsi tersebut atau dicetak ke layar.|Menghasilkan nilai `None`.|
|**Dengan `return`**|Mengirimkan secara eksplisit nilai hasil perhitungan keluar dari lingkup fungsi menuju pemanggilnya.|Variabel penangkap berhasil menyimpan nilai riil hasil komputasi.|

---

## 1.6 Fungsi dengan Kata Kunci lambda (Function with lambda)

### A. Karakteristik Anonymous Function

- **Fungsi Anonim**: Fungsi yang dibuat menggunakan kata kunci `lambda` adalah fungsi khusus yang tidak memiliki nama (_anonymous function_).
- **Batasan Satu Baris**: Fungsi ini hanya dapat digunakan jika logika di dalamnya sangat sederhana dan dapat dituliskan secara lengkap dalam satu baris ekspresi saja (_single-line expression_).
- **Sintaksis Penulisan**:

```
lambda parameter(s): expression
```

- **Konversi Otomatis**: Semua fungsi standar (`def`) yang hanya memiliki satu baris ekspresi logika di dalamnya dapat dikonversi menjadi fungsi `lambda`.

#### [Wawasan Diskusi / Audio Insight]

- **Penyimpanan Logika ke Variabel**: Meskipun `lambda` pada dasarnya adalah fungsi tanpa nama, dalam praktiknya logika tersebut sering disimpan ke dalam sebuah variabel (misalnya `lambda_function = lambda num1, num2:...`) agar variabel tersebut dapat dipanggil seperti fungsi biasa.
- **Alternatif Iterasi Manual**: Dalam diskusi kelas, dosen mengajukan pertanyaan bagaimana melakukan operasi perkalian setiap elemen list dengan `-2` apabila kita belum memahami fungsi `lambda`. Solusi alternatif yang disepakati adalah menggunakan perulangan (_looping_ / _iterator_) dengan membuat list kosong terlebih dahulu, mengalikan setiap elemen satu per satu, dan memasukkannya menggunakan metode `.append()`.

---

## 1.7 Praktik Penulisan Fungsi yang Bersih (Writing Clean Functions)

### A. Aturan Emas Clean Function

Untuk menghasilkan kode program yang mudah dibaca (_readable_), mudah diuji (_testable_), mudah dipelihara (_maintainable_), serta mudah dipahami oleh orang lain, kita harus menerapkan aturan berikut:

1. Menggunakan nama fungsi yang deskriptif (_descriptive function name_).
2. Menggunakan nama parameter yang bermakna (_meaningful parameter name_).
3. Menentukan petunjuk tipe data (_type hint_) untuk parameter input dan nilai kembalian (_return value_).
4. Menyediakan dokumentasi deskriptif yang jelas (_docstring_) untuk menerangkan fungsionalitas blok kode tersebut.

### B. Studi Kasus Perbandingan Keterbacaan

Perbandingan visual dilakukan antara fungsi `calc()` yang ditulis buruk dan fungsi `get_median()` yang ditulis dengan kaidah _clean function_ untuk menghitung nilai tengah (_median_) dari sebuah list.

- **Fungsi calc() (Buruk/Membingungkan)**:
    
- Menggunakan nama fungsi `calc()` yang terlalu umum dan tidak deskriptif.
    
- Nama parameter menggunakan singkatan `lst` tanpa petunjuk tipe data.
    
- Variabel penampung di dalamnya disingkat menjadi `mid1` dan `mid2` tanpa penjelasan.
    
- Tidak memiliki dokumentasi (_docstring_) sehingga sulit dipahami maksudnya secara instan.
    
- **Fungsi get_median() (Sangat Baik/Bersih)**:
    
- Menggunakan nama fungsi `get_median()` yang sangat jelas.
    
- Menetapkan _type hint_ pada parameter input (`data: list`) dan tipe data hasil kembalian (`-> float`).
    
- Dilengkapi _docstring_ tiga tanda petik `"""` yang menjelaskan tugas fungsi, deskripsi argumen yang dibutuhkan, serta apa yang dikembalikan.
    

#### [Wawasan Diskusi / Audio Insight]

- **Sifat Type Hint di Python**: Berdasarkan pertanyaan mahasiswa di kelas mengenai batasan tipe data pada _type hint_, dosen menegaskan bahwa _type hint_ di Python **tidak memicu error secara otomatis saat runtime** jika tipe data yang dimasukkan berbeda (misalnya kita memasukkan string pada fungsi yang ditandai dengan tipe data list). _Type hint_ murni bersifat sebagai panduan dokumentasi (_documentation aid_) untuk membantu programmer, rekan kerja, maupun agen AI memahami struktur input-output yang diharapkan tanpa harus menelusuri isi logika di dalam fungsi tersebut.
- **Penanganan Error pada Input Non-List**: Ketika mendiskusikan pembatasan input tipe data pada fungsi `process_data(data: list) -> list`, seorang mahasiswa bertanya mengenai perilaku program apabila diinputkan data selain `list` dan bagaimana cara menangani error tersebut. Dosen menjelaskan bahwa di luar pemeriksaan petunjuk tipe data, penanganan error (_error handling_) dapat diimplementasikan menggunakan blok konstruksi `try` dan `except`. Ketika proses pemanggilan fungsi diletakkan di dalam blok `try` dan terjadi kesalahan tipe data (_type error_ atau kesalahan komputasi lainnya), kesalahan tersebut akan ditangkap (_catch_) oleh blok `except` sehingga program tidak langsung terhenti secara tidak normal.



## Bab 2 Python Namespace and Scope (Namespace dan Ruang Lingkup)



Study Guide ini disusun secara terstruktur untuk membahas mekanisme Python dalam melacak variabel di memori, pembatasan akses variabel berdasarkan lokasi pembuatannya, serta penggunaan kata kunci khusus untuk memodifikasi variabel di luar ruang lingkup normal.

---

## 2.1 Konsep Namespace (Ruang Nama)

### A. Fondasi Konseptual Namespace

- **Definisi**: _Namespace_ adalah sebuah area penyimpanan berlabel yang bertugas melacak nama-nama (_names_) yang kita buat di dalam program beserta objek (_objects_) yang dirujuk oleh nama-nama tersebut.
- **Analogi Loker Penyimpanan**: _Namespace_ dapat dianalogikan seperti area penyimpanan berlabel di mana Python menyimpan nama variabel atau nama fungsi sebagai label penunjuk (_pointer_) ke nilai atau objek data yang sesungguhnya di memori komputer.

### B. Tiga Tingkatan Namespace

Python mengelola nama menggunakan hirarki bertingkat yang otomatis dibuat pada kondisi tertentu:

- **Built-in Namespace**: Berisi nama bawaan yang disediakan langsung oleh Python. _Namespace_ ini otomatis dibuat saat interpreter Python dijalankan dan langsung tersedia di seluruh bagian program tanpa memerlukan konfigurasi atau impor modul eksternal (contoh: `print()`, `range()`, `input()`, `len()`).
- **Global Namespace**: Berisi nama-nama variabel, fungsi, atau kelas yang didefinisikan secara umum di tingkat program utama (tingkat modul atau file aktif).
- **Local Namespace**: Berisi nama-nama yang didefinisikan secara khusus di dalam tubuh suatu fungsi. _Namespace_ ini bersifat sementara; hanya dibuat saat fungsi dieksekusi dan akan dihapus dari memori begitu fungsi selesai dijalankan.

---

## 2.2 Konsep Scope (Ruang Lingkup)

### A. Definisi Scope

- **Definisi**: _Scope_ adalah aturan yang menentukan di bagian mana saja suatu nama atau variabel yang telah dibuat dapat diakses secara langsung di dalam kode program.
- **Aturan Akses**: Keberadaan sebuah variabel di dalam _Namespace_ tertentu tidak menjamin variabel tersebut dapat dibaca dari mana saja. Aturan _Scope_ membatasi visibilitas variabel untuk menjaga integritas data dalam program.

### B. Perbandingan Variabel Global dan Lokal

Karakteristik perbedaan antara _global variable_ dan _local variable_ dirangkum dalam tabel berikut:

|Karakteristik Perbandingan|Global Variable|Local Variable|
|:--|:--|:--|
|**Lokasi Pendefinisian**|Dibuat di luar tubuh fungsi (tingkat modul/file utama).|Dibuat di dalam tubuh fungsi tertentu.|
|**Aksesibilitas Langsung**|Dapat diakses dari bagian mana pun di dalam file yang sama (baik di dalam maupun di luar fungsi).|Hanya dapat diakses dari dalam tubuh fungsi tempat variabel tersebut didefinisikan.|
|**Siklus Hidup (_Lifetime_)**|Bertahan selama seluruh rangkaian program utama berjalan.|Hanya bertahan selama fungsi tempat ia didefinisikan sedang dieksekusi.|

#### [Wawasan Diskusi / Audio Insight]

- **Variabel dengan Nama Sama di Scope Berbeda**: Dalam sesi diskusi tanya jawab, muncul pertanyaan mengenai apakah penamaan variabel boleh sama di tingkatan _scope_ yang berbeda. Berdasarkan demonstrasi langsung di kelas, diperlihatkan bahwa penamaan variabel yang sama diperbolehkan. Jika ada variabel bernama `message` di lingkup global dan variabel bernama `message` di lingkup lokal fungsi, Python memperlakukannya sebagai dua variabel yang sepenuhnya berbeda. Saat fungsi dieksekusi, Python memprioritaskan variabel lokal terlebih dahulu. Setelah fungsi selesai berjalan, program akan kembali merujuk pada nilai variabel global di luar fungsi tanpa terjadi tumpang tindih.

---

## 2.3 Kata Kunci global (global Keyword)

### A. Fungsi global Keyword

- **Tujuan Penggunaan**: Di dalam Python, _global keyword_ digunakan untuk memberikan instruksi eksplisit kepada interpreter agar menggunakan dan memodifikasi variabel yang berada di lingkup global (_global scope_) dari dalam konteks lokal fungsi.
- **Sintaksis Deklarasi**:
    
    ```
    global variable_name
    ```
    

### B. Konsekuensi UnboundLocalError

- **Pemicu Error**: Apabila kita mencoba mengubah nilai (_reassign/modify_) sebuah variabel global secara langsung di dalam fungsi tanpa mendeklarasikan kata kunci `global`, Python secara otomatis akan menganggap variabel tersebut sebagai variabel lokal baru.
- **Mekanisme Kegagalan**: Saat program mencoba melakukan operasi perubahan nilai (misalnya `position += 1`), Python akan mencari definisi awal variabel lokal tersebut di dalam fungsi. Karena nilai awalnya tidak ditemukan di lingkup lokal, interpreter akan menghentikan eksekusi program dan melempar kesalahan berupa `UnboundLocalError`.

#### [Wawasan Diskusi / Audio Insight]

- **Studi Kasus Kesalahan Kode `position`**: Dalam sesi demo pemrograman, dosen memperlihatkan contoh variabel global koordinat `position = 0`. Ketika dibuat fungsi `move_forward()` yang di dalamnya langsung berisi kode `position += 1`, program mengalami kegagalan _runtime_ dengan pesan `UnboundLocalError`. Masalah ini dipecahkan dengan menambahkan baris deklarasi `global position` di bagian paling atas di dalam tubuh fungsi sebelum melakukan operasi penambahan nilai. Dengan demikian, nilai variabel `position` di tingkat global berhasil diperbarui menjadi `1` ketika fungsi tersebut dipanggil.

---

## 2.4 Kata Kunci nonlocal (nonlocal Keyword)

### A. Definisi dan Fungsi nonlocal Keyword

- **Tujuan Penggunaan**: Kata kunci `nonlocal` digunakan khusus di dalam fungsi bersarang (_nested function_) untuk memberitahu Python secara eksplisit agar mengakses dan mengubah variabel yang didefinisikan pada fungsi pembungkus terdekat (_nearest enclosing function scope_).
- **Penjembatan Scope**: Keyword ini berfungsi menjembatani perbedaan antara lingkup lokal terdalam dengan lingkup lokal satu tingkat di atasnya, tanpa harus menaikkan variabel tersebut ke tingkat modul global yang terlalu tinggi.

### B. Karakteristik Penggunaan nonlocal

- **Khusus Nested Function**: Kata kunci `nonlocal` hanya valid dan hanya dapat bekerja di dalam struktur fungsi bersarang (_nested function_). Penggunaannya di luar struktur ini akan menyebabkan kesalahan sintaksis.
- **Menghindari Duplikasi Memori**: Deklarasi keyword ini memastikan bahwa Python tidak menginisialisasi variabel lokal baru di dalam fungsi terdalam, melainkan langsung memanipulasi variabel milik fungsi pembungkusnya di memori komputer.

#### [Wawasan Diskusi / Audio Insight]

- **Asal-Usul nonlocal dalam Diskusi Kelas**: Pembahasan mengenai keyword `nonlocal` berawal dari pertanyaan mahasiswa yang menanyakan keberadaan alternatif kata kunci selain `global` untuk fungsi bersarang. Dosen bersama mahasiswa kemudian mengeksplorasi dokumentasi mengenai skenario fungsi bersarang `fun()` yang di dalamnya mendefinisikan fungsi `gun()`. Diperlihatkan bahwa apabila kita ingin agar perubahan variabel di dalam fungsi terdalam `gun()` ikut mengubah nilai variabel di fungsi pembungkus `fun()`, kita harus menggunakan keyword `nonlocal`. Jika kita menggunakan keyword `global`, Python justru akan mencari variabel tersebut di tingkat teratas modul file (luar fungsi `fun()`), yang dapat menyebabkan error jika variabel global tersebut memang tidak pernah dibuat sejak awal.



## Bab 3 Nested, Callback, and Recursive Function (Fungsi Bersarang, Callback, dan Rekursif)


Study Guide ini menyajikan pembahasan mendalam mengenai konsep fungsi tingkat lanjut di Python, mencakup fungsi bersarang (_Nested Function_), pengiriman fungsi sebagai argumen (_Callback Function_), fungsi yang memanggil dirinya sendiri (_Recursive Function_), serta panduan logika dan solusi untuk latihan-latihan mandiri (_Exercises_) yang diulas dalam sesi kuliah.

---

## 3.1 Nested Function (Fungsi Bersarang)

### A. Konsep Dasar dan Lingkup Akses

- **Definisi**: _Nested Function_ adalah praktik mendefinisikan suatu fungsi pembantu (_helper function_) di dalam tubuh fungsi utama (_enclosing function_).
- **Alokasi dan Lingkup**: Fungsi bagian dalam (_inner function_) hanya akan diciptakan dan dialokasikan di memori saat fungsi utama sedang dieksekusi. Begitu fungsi utama selesai dijalankan, fungsi bagian dalam tersebut akan dihapus dari memori.
- **Batasan Akses**: Karena didefinisikan di dalam lingkup lokal fungsi utama, _nested function_ murni bersifat lokal dan tidak dapat diakses atau dipanggil secara langsung dari lingkup global (di luar fungsi utama).
- **Studi Kasus Perhitungan Pajak**: Implementasi fungsi pembantu `add_tax` yang didefinisikan di dalam fungsi utama `calculate_total` untuk menambahkan komponen pajak sebesar 11% pada setiap harga barang.

```
def calculate_total(prices):
    tax_rate = 0.11

    def add_tax(price):
        return price * (1 + tax_rate)

    total = 0
    for price in prices:
        total += add_tax(price)
    return total
```

### B. Karakteristik Utama Nested Function

- **Enclosing Scope Access**: Fungsi bagian dalam memiliki hak akses langsung untuk membaca variabel-variabel yang dideklarasikan pada lingkup fungsi luar (seperti variabel `tax_rate`).
- **Encapsulation (Enkapsulasi)**: Menyembunyikan fungsionalitas spesifik yang hanya relevan bagi fungsi utama, mencegah polusi nama fungsi pada lingkup global.

#### [Wawasan Diskusi / Audio Insight]

- **Proteksi Logika Internal**: Berdasarkan hasil demo di kelas, apabila kita mencoba memanggil fungsi `add_tax()` secara langsung dari lingkup luar program, Python akan memicu kesalahan (_error_) karena nama fungsi tersebut tidak terdaftar di lingkup global (_NameError_). Logika internal ini sepenuhnya terproteksi di dalam fungsi pembungkusnya.

---

## 3.2 Callback Function (Fungsi Callback)

### A. Konsep Dasar dan Fleksibilitas Kode

- **Definisi**: _Callback Function_ adalah sebuah fungsi yang dilewatkan sebagai argumen atau nilai input ke dalam fungsi lain.
- **Mekanisme Kerja**: Fungsi penerima bertindak sebagai pengontrol aliran utama, sementara logika operasi spesifik didelegasikan kepada fungsi callback yang dikirimkan. Fungsi penerima dapat mengeksekusi fungsi callback tersebut kapan saja di dalam tubuh logikanya saat diperlukan.
- **Studi Kasus Kalkulator Multi-Operasi**: Fungsi `kalkulator` dirancang sebagai pengendali utama yang menerima parameter `operasi` berupa fungsi callback, serta dua operand `a` dan `b`.

```
def tambah(a, b):
    return a + b

def kurang(a, b):
    if a >= b:
        return a - b
    else:
        return b - a

def kalkulator(operasi, a, b):
    return operasi(a, b)
```

### B. Karakteristik Penggunaan Callback

- **Modularitas Tinggi**: Kita dapat dengan mudah menambahkan fungsi operasi baru (seperti perkalian atau pembagian) tanpa perlu mengubah struktur logika internal pada fungsi `kalkulator`.
- **Dinamis**: Eksekusi logika di dalam fungsi utama sepenuhnya bergantung pada fungsi callback mana yang dikirimkan saat pemanggilan dilakukan.

#### [Wawasan Diskusi / Audio Insight]

- **Aturan Pemanggilan Tanpa Kurung**: Dosen memberikan penekanan penting mengenai sintaksis pemanggilan. Saat melemparkan fungsi sebagai argumen (misalnya `kalkulator(tambah, 1, 3)`), nama fungsi `tambah` harus dituliskan **tanpa tanda kurung `()`**. Jika dituliskan dengan kurung, Python akan mengeksekusi fungsi tersebut terlebih dahulu dan mengirimkan nilai hasilnya, bukan referensi objek fungsinya. Tanda kurung baru diaplikasikan di dalam tubuh fungsi penerima (`operasi(a, b)`).

---

## 3.3 Recursive Function (Fungsi Rekursif)

### A. Konsep Dasar dan Cara Kerja

- **Definisi**: _Recursive Function_ adalah fungsi yang memecahkan masalah komputasi dengan cara memanggil dirinya sendiri secara berulang-ulang.
- **Strategi Penyelesaian**: Pendekatan rekursif membagi satu masalah besar menjadi serangkaian sub-masalah sejenis yang berukuran lebih kecil, menyelesaikannya secara bertahap, lalu menggabungkan kembali hasilnya.
- **Komponen Mutlak**: Setiap fungsi rekursif wajib memiliki dua komponen utama:
    1. _Base Case_ (_Stopping Condition_): Kondisi batas dasar yang dievaluasi menggunakan percabangan `if` untuk menghentikan pemanggilan diri sendiri.
    2. _Recursive Case_: Bagian logika di mana fungsi memanggil dirinya sendiri dengan argumen yang nilainya semakin mendekati _Base Case_.
- **Studi Kasus Hitung Mundur (Countdown)**: Fungsi `countdown` menerima sebuah bilangan, mencetaknya, lalu memanggil dirinya sendiri dengan nilai bilangan yang dikurangi 1 hingga menyentuh angka 1.

```
def countdown(num):
    print(num)
    if num > 1:
        countdown(num - 1)
```

### B. Perbandingan Karakteristik Rekursif dan Iterasi

Perbedaan fundamental antara pendekatan fungsi rekursif dengan perulangan iteratif biasa dirangkum dalam tabel berikut:

|Karakteristik Perbandingan|Fungsi Rekursif|Iterasi Biasa (Looping)|
|:--|:--|:--|
|**Mekanisme Pengulangan**|Pemanggilan fungsi ke dirinya sendiri secara berulang.|Menggunakan instruksi `for` atau `while`.|
|**Kondisi Berhenti**|Ditentukan secara eksplisit pada pernyataan _Base Case_.|Ditentukan oleh kondisi terminasi loop yang bernilai `False`.|
|**Efisiensi Memori**|Lebih boros memori (membutuhkan ruang untuk _Call Stack_).|Sangat efisien (variabel kontrol diperbarui pada alamat memori yang sama).|
|**Risiko Kegagalan**|Menyebabkan crash sistem akibat kehabisan memori _stack_.|Mengakibatkan program berjalan tanpa henti (_infinite loop_).|

#### [Wawasan Diskusi / Audio Insight]

- **Bahaya Konsumsi Memori (Stack Overflow)**: Dalam sesi pemaparan, dosen mengingatkan dampak fatal apabila fungsi rekursif ditulis tanpa memiliki _stopping condition_ yang valid. Setiap kali fungsi memanggil dirinya sendiri, Python akan membuka bingkai memori baru di dalam _call stack_. Jika pemanggilan terjadi tanpa batas (_infinite call_), memori RAM komputer akan terkuras habis dengan sangat cepat, yang mengakibatkan program langsung mengalami crash atau hang.
- **Studi Kasus Klasik Tower of Hanoi**: Masalah pemindahan cakram klasik seperti _Tower of Hanoi_ yang sempat dibahas merupakan contoh nyata di mana pendekatan rekursif memberikan solusi penulisan kode yang jauh lebih sederhana, elegan, dan mudah dipahami dibandingkan dengan perulangan iteratif yang membutuhkan logika pelacakan posisi sangat rumit.

---

## 3.4 Panduan dan Implementasi Latihan Mandiri (Exercises)

Sesi latihan mandiri di kelas berfokus pada penerapan fungsi dinamis, penanganan parameter default, serta optimasi logika matematika. Berikut adalah rincian solusi dan analisis kasus dari latihan tersebut:

### A. Latihan 1: Luas Lingkaran Fleksibel (get_circle_area)

- **Deskripsi Tugas**: Buatlah fungsi `get_circle_area` yang menerima parameter `radius` dan `diameter` yang masing-masing bernilai default `None`. Fungsi harus menghitung luas lingkaran berdasarkan input yang dikirimkan. Jika kedua input diberikan sekaligus, prioritaskan penggunaan `radius`. Hasil akhir wajib dibulatkan ke dalam 3 angka desimal.

```
import math

def get_circle_area(radius=None, diameter=None):
    if radius is not None:
        r = radius
    elif diameter is not None:
        r = diameter / 2
    else:
        return 0
    area = math.pi * r * r
    return round(area, 3)
```

#### [Wawasan Diskusi / Audio Insight]

- **Penyusunan Aliran Kondisi (Prioritas)**: Logika prioritas diselesaikan dengan menaruh pengecekan `radius is not None` pada blok `if` paling atas. Sifat pengeksekusian percabangan di Python memastikan bahwa jika kondisi pertama bernilai `True`, blok di bawahnya (`elif` diameter) akan dilewati sepenuhnya. Hal ini menjamin parameter radius selalu diutamakan secara otomatis.

---

### B. Latihan 2: Konverter Suhu (convert_temperature)

- **Deskripsi Tugas**: Buatlah fungsi `convert_temperature` yang menerima input nilai temperatur (`temp`) dan unit skalanya (`unit` berupa string `"C"` atau `"F"`). Kembalikan nilai hasil konversi suhu yang sesuai.

```
def convert_temperature(temp, unit):
    if unit == "C":
        return (temp * 9/5) + 32
    elif unit == "F":
        return (temp - 32) * 5/9
    else:
        raise ValueError("Unit skala tidak valid. Gunakan 'C' atau 'F'.")
```

#### [Wawasan Diskusi / Audio Insight]

- **Penerapan Error Handling**: Untuk mengantisipasi input unit yang tidak valid (misalnya pengguna memasukkan selain huruf "C" atau "F"), sangat disarankan untuk mengimplementasikan pelemparan pengecualian (_raising exception_) berupa `ValueError` agar sistem tidak menghasilkan kalkulasi yang salah saat eksekusi runtime.

---

### C. Latihan 3: Analisis Bilangan Bulat Komprehensif (analyze_number)

- **Deskripsi Tugas**: Buatlah fungsi `analyze_number` yang menganalisis sebuah bilangan bulat untuk:
    1. Menentukan apakah angka tersebut bernilai positif, negatif, atau nol.
    2. Menentukan apakah angka tersebut ganjil (_odd_) atau genap (_even_).
    3. Khusus untuk bilangan positif, periksa apakah angka tersebut termasuk bilangan prima (_prime_) atau bukan.
    4. Gabungkan seluruh hasil analisis ke dalam satu pesan teks terformat.

```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def analyze_number(num):
    if num == 0:
        return "Zero"

    # Menentukan Parity (Ganjil/Genap)
    if num % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    # Menentukan Sign (Positif/Negatif) dan Status Prima
    if num > 0:
        if is_prime(num):
            return f"Prime and {parity}"
        else:
            return f"Positive and {parity}"
    else:
        return f"Negative and {parity}"
```

#### [Wawasan Diskusi / Audio Insight]

- **Optimasi Matematika Pengecekan Prima**: Pada sesi pembahasan live coding, diperlihatkan teknik optimasi pencarian bilangan prima menggunakan batas nilai akar kuadrat (`int(n**0.5) + 1`). Penggunaan metode ini menghemat siklus perulangan secara drastis dibandingkan melakukan iterasi penuh hingga `n-1`, terutama untuk nilai angka pengujian yang sangat besar.
- **Kaidah Modularitas (Separation of Concerns)**: Memisahkan pengecekan prima ke dalam fungsi pembantu eksternal `is_prime()` merupakan praktik penulisan kode bersih yang sangat direkomendasikan. Kode menjadi lebih mudah dibaca dan diuji secara terisolasi.
- **Penyelesaian Bug Perulangan (Adiba Live Coding Case)**: Dalam sesi analisis kegagalan kode siswa, diidentifikasi bug di mana bilangan prima salah dideteksi karena peletakan pernyataan `return True` yang salah ditaruh di dalam blok perulangan `for` loop secara tidak sengaja. Kesalahan ini menyebabkan loop langsung berhenti pada iterasi pertama tanpa menguji angka pembagi lainnya. Solusinya adalah memindahkan pernyataan `return True` ke luar blok perulangan `for` untuk memastikan seluruh rentang angka pembagi selesai diuji secara menyeluruh.



## Bab 4 Working with External Files in Python (Bekerja dengan File Eksternal)


Study Guide ini dirancang khusus untuk membahas dasar-dasar manipulasi berkas eksternal di Python, meliputi konsep penyimpanan permanen, berbagai mode pembukaan file, operasi baca-tulis, hingga implementasi manajemen memori otomatis menggunakan `with statement`. Seluruh materi diselaraskan antara teori modul dan studi kasus diskusi praktis di kelas.

---

## 4.1 Fondasi Konseptual File Eksternal

### A. Penyimpanan Sementara versus Permanen

- **Batas Variabel**: Selama program dijalankan, data disimpan secara sementara (_temporary_) di dalam memori RAM menggunakan variabel. Begitu interpreter Python dimatikan atau program selesai dieksekusi, seluruh data tersebut akan terhapus sepenuhnya.
- **Peran File Eksternal**: Berkas eksternal memungkinkan program untuk menyimpan data secara permanen (_persistently_) ke dalam media penyimpanan fisik (seperti Hard Disk atau SSD). Program dapat membaca kembali data tersebut kapan saja bahkan setelah komputer dimatikan.

### B. Alur Interaksi File di Python

- **Membuka (Open)**: Menghubungkan program Python dengan sistem penyimpanan sistem operasi menggunakan fungsi bawaan `open()`. Langkah ini menghasilkan objek file (_file object_) atau penunjuk (_file handler_) di memori.
- **Memproses (Read/Write)**: Melakukan manipulasi isi file seperti mengambil data (_reading_) atau memasukkan data baru (_writing_).
- **Menutup (Close)**: Memutuskan koneksi berkas eksternal menggunakan metode `.close()` untuk membebaskan sumber daya memori dan mengunci kembali berkas agar tidak terjadi korupsi data (_data corruption_).

---

## 4.2 Membuka File (Opening a File)

### A. Sintaksis Dasar Fungsi open()

Untuk membuka file, Python menyediakan fungsi bawaan dengan parameter masukan berupa lokasi file (_filepath_) dan mode akses (_mode_):

```
file_object = open(filepath, mode)
```

### B. Karakteristik Mode Akses File

Akses manipulasi file ditentukan oleh tipe string mode yang dimasukkan. Karakteristik dari tiga mode utama dirangkum dalam tabel berikut:

|Mode|Nama Operasi|Deskripsi Karakteristik|Perilaku terhadap Berkas|
|:--|:--|:--|:--|
|`"r"`|_Read_|Membuka file khusus untuk dibaca.|Berkas yang dituju wajib sudah ada sebelumnya di direktori. Jika tidak ada, Python akan memicu kesalahan _FileNotFoundError_.|
|`"w"`|_Write_|Membuka file khusus untuk ditulis.|Jika berkas sudah ada, seluruh isi lamanya akan dihapus total (_truncated_ / ditimpa). Jika berkas belum ada, berkas baru akan otomatis dibuat.|
|`"a"`|_Append_|Membuka file untuk ditambahkan datanya di bagian paling akhir.|Nilai baru akan ditulis mulai dari baris akhir tanpa merusak atau menghapus data lama. Jika berkas belum ada, berkas baru otomatis dibuat.|

---

## 4.3 Membaca dan Menulis File (Reading and Writing a File)

### A. Operasi Tulis (write)

Fungsi `.write()` digunakan untuk memasukkan satu string data ke dalam file yang telah dibuka dengan mode `"w"` atau `"a"`.

```
file = open("data.txt", "w")
file.write("Hello, Python!")
file.close()
```

### B. Operasi Baca (read)

Fungsi `.read()` digunakan untuk mengambil seluruh teks dari berkas eksternal sebagai satu kesatuan objek string di Python.

```
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```

#### [Wawasan Diskusi / Audio Insight]

- **Karakter Newline `\n`**: Dalam sesi demonstrasi kelas, mahasiswa menanyakan perihal penggunaan karakter garis miring terbalik (_backslash_) diikuti huruf n (`\n`) yang disisipkan di dalam kode string. Dosen menjelaskan bahwa itu adalah karakter khusus (_escape character_) untuk merepresentasikan instruksi pindah baris (_enter / newline_). Jika karakter ini tidak disertakan, teks yang ditulis berikutnya akan menempel pada baris yang sama.

---

## 4.4 Pernyataan with (with Statement)

### A. Risiko Lupa Menutup File

Saat membuka file secara manual menggunakan `open()`, berkas tersebut akan tetap berada dalam status terkunci oleh proses sistem operasi sebelum metode `.close()` dipanggil. Jika program mengalami eror sebelum baris `.close()` dieksekusi, atau jika programmer lupa menuliskan metode `.close()`, berkas tersebut berisiko mengalami kebocoran memori (_memory leak_) atau kerusakan data.

### B. Manajemen Otomatis dengan with Statement

Di Python, pendekatan terbaik (_best practice_) untuk menangani manipulasi file adalah menggunakan pernyataan `with`. Pernyataan ini menjamin bahwa berkas akan ditutup secara otomatis oleh sistem begitu aliran eksekusi keluar dari blok indentasi `with`, bahkan jika terjadi kesalahan (_exception_) di tengah jalan. Programmer tidak perlu lagi memanggil metode `.close()` secara manual.

```
# Sintaks standar pembacaan file dengan with statement
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# Di luar blok indentasi ini, file sudah otomatis tertutup dengan aman
```

---

## 4.5 Latihan Mandiri Manipulasi File (Exercises)

Di akhir sesi kuliah, mahasiswa ditantang untuk menyelesaikan skenario dunia nyata yang mengintegrasikan pembuatan fungsi bersih dengan penulisan berkas eksternal.

### Latihan 4: Program Menyimpan Faktur Belanja (Invoice Saver)

Mahasiswa diminta membuat program interaktif yang menanyakan jumlah buah yang dibeli, meminta nama buah, harga, serta kuantitasnya, lalu menyimpan kalkulasi tersebut secara terstruktur ke dalam file bernama `invoice.txt`.

#### [Wawasan Diskusi / Audio Insight]

- **Strategi Penyimpanan dengan List of Dictionary**: Dalam sesi demo pengerjaan oleh mahasiswa (Ivo), data input dibungkus terlebih dahulu ke dalam tipe data terstruktur berupa list yang berisi kamus (_list of dictionary_). Struktur ini mempermudah pelacakan data sebelum ditulis ke media fisik.
- **Kustomisasi Layout Penulisan**: Untuk memisahkan visualisasi antar item buah di dalam berkas teks, mahasiswa menggunakan logika pemeriksaan pengkondisian. Jika item yang sedang diproses dalam perulangan bukan merupakan item terakhir (`item != items[-1]`), maka program akan menyisipkan karakter enter ganda (`\n\n`) untuk menciptakan jarak pemisah yang rapi. Penulisan ke file dieksekusi secara efisien menggunakan blok `with open("invoice.txt", "w")`.

### Latihan 5: Menghitung Total Belanja dan Diskon (Invoice Reader and Discount)

Mahasiswa diminta membuat fungsi `get_total(list_of_price, discount)` yang bertugas mengambil atau membaca daftar harga total belanja dari berkas `invoice.txt` yang sudah dibuat pada Latihan 4, menjumlahkannya, lalu mengembalikan nilai akhir belanja setelah dikurangi persentase diskon yang ditentukan.

#### [Wawasan Diskusi / Audio Insight]

- **Pola Integrasi Aliran Data (Data Flow)**: Proses pemecahan masalah dilakukan dengan membagi tugas ke dalam fungsi khusus. Fungsi utama (seperti `read_prices_and_get_total()`) bertugas melakukan pembacaan file `invoice.txt` menggunakan `with open` dalam mode `"r"`, mengekstrak nilai angka total belanja dari string teks, menyimpannya ke dalam list, lalu mengirimkan list tersebut ke dalam fungsi kalkulator `get_total(list_of_price, discount)` untuk mendapatkan harga bersih setelah diskon.



---


# Module 1 Session 6 Hackerrank Exercise


## Bab 1 & 2 Membuat infoice & Membuat Runner-Up Score

## 1. Membaca dan Memproses File Invoice (Topik 1A)

Tujuan utama dari topik ini adalah mengekstrak data numerik dari sebuah file teks (`invoice.txt`) yang memiliki struktur data berulang dan menghitung total harga setelah diskon.

A. Alur Logika Penyelesaian

1. **Membuka File:** Menggunakan fungsi `open()` untuk membaca file `invoice.txt`.
2. **Membaca Line per Line:** Menggunakan `.readlines()` untuk mengambil seluruh baris dalam file.
3. **Iterasi dengan Langkah (Step Looping):** Karena struktur file terdiri dari Nama, Quantity, dan Total, maka Looping dilakukan dengan melompat setiap 3 baris untuk menargetkan baris "Total".
4. **Ekstraksi Nilai (Parsing):**
    - **Metode Karakter:** Memeriksa setiap karakter apakah merupakan digit menggunakan `.isdigit()`.
    - **Metode Split (Direkomendasikan):** Memecah string baris "Total" menggunakan `.split()`. Nilai angka biasanya berada di indeks terakhir `[-1]`.
5. **Perhitungan:** Mengumpulkan semua angka ke dalam List, menjumlahkannya dengan `sum()`, dan mengalikan dengan faktor diskon (misalnya 10%).

B. Kode Python (Manipulasi File)

```
# Inisialisasi list untuk menyimpan harga
total_prices = []

# Membaca file
with open('invoice.txt', 'r') as file:
    lines = file.readlines()
    # Looping melompat 3 baris untuk mengambil baris 'Total'
    for i in range(2, len(lines), 3):
        line_content = lines[i]
        # Memecah string dan mengambil angka di posisi terakhir
        parts = line_content.split()
        price = int(parts[-1])
        total_prices.append(price)

# Menghitung subtotal dan diskon
subtotal = sum(total_prices)
discount = 10
final_total = subtotal * (1 - discount/100)

print(f"Total sebelum diskon: {subtotal}")
print(f"Total setelah diskon {discount}%: {final_total}")
```

---

## 2. Menemukan Runner-Up Score (Topik 1B)

Masalah ini melatih kemampuan dalam mengolah Array/List untuk menemukan nilai tertinggi kedua dari sekumpulan skor yang diberikan.

A. Alur Logika dan Constraints

- **Constraints:**
    - Jumlah skor (N): 2≤N≤10.
    - Rentang skor: −100 hingga 100.
- **Logika Penyelesaian:**
    1. Menerima input N sebagai jumlah data.
    2. Menerima baris skor dan mengubahnya menjadi List of Integer menggunakan `map(int, input().split())`.
    3. **Menghapus Duplikat:** Mengubah List menjadi `set` agar nilai yang sama (seperti dua skor juara pertama) hanya terhitung satu kali.
    4. **Sorting:** Mengurutkan skor secara Ascending.
    5. **Akses Indeks:** Mengambil nilai pada indeks `[-2]` (elemen kedua dari belakang) yang merupakan Runner-Up.

B. Kode Python (Runner-Up Score)

```
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Menghapus duplikat dengan set dan mengurutkan
    unique_scores = sorted(list(set(arr)))
    
    # Mencetak nilai tertinggi kedua
    print(unique_scores[-2])
```

---

3. Manipulasi List dan Dictionary Kompleks

Selain dua topik utama, terdapat latihan tambahan mengenai Nested List dan pemrosesan string menggunakan Dictionary.

A. Nested List (Mencari Skor Terendah Kedua)

- Data disimpan dalam format List di dalam List: `[[Nama, Skor], [Nama, Skor]]`.
- Menggunakan List Comprehension untuk mengekstrak skor saja, mencari skor terendah kedua melalui `set()` dan `sorted()`.
- Melakukan filter untuk mengambil nama-nama yang memiliki skor tersebut, lalu diurutkan secara Alphabetical.

B. Command Parsing (List Operations)

- Program menerima sejumlah N perintah (seperti `insert`, `append`, `remove`, `pop`, `reverse`).
- Logika menggunakan `if-elif` untuk mengecek jenis perintah pada indeks `[0]` setelah string di-split.

---

4. Daftar Fungsi dan Metode Python Penting

|Fungsi / Metode|Kegunaan|Contoh Penggunaan|
|---|---|---|
|`split()`|Memecah string menjadi List berdasarkan separator (default: spasi).|`line.split()`|
|`map()`|Menerapkan fungsi ke setiap item dalam iterable (Lazy Operation).|`map(int, input().split())`|
|`set()`|Mengubah iterable menjadi himpunan unik (menghapus duplikat).|`set(list_skor)`|
|`sorted()`|Mengurutkan elemen secara Ascending dan mengembalikan List baru.|`sorted(set_data)`|
|`append()`|Menambahkan elemen baru ke posisi terakhir dalam List.|`list.append(nilai)`|
|`insert(i, e)`|Menyisipkan nilai `e` pada indeks ke-`i`.|`list.insert(0, 5)`|
|`items()`|Mengambil pasangan Key dan Value dari sebuah Dictionary.|`dict.items()`|

---

[Wawasan Dosen / Audio Insight]

- **Lazy Operation pada Map:** Fungsi `map()` di Python bersifat "lazy". Artinya, proses konversi (misalnya menjadi integer) tidak langsung dilakukan sampai hasilnya dibutuhkan (seperti saat dikonversi menjadi `list` atau `set`).
- **Keuntungan Menggunakan Set:** Dalam kasus mencari Runner-Up, penggunaan `set()` sangat krusial jika terdapat nilai tertinggi yang ganda. Tanpa `set()`, juara kedua mungkin tidak akan ditemukan jika juara pertama memiliki skor yang sama di beberapa entri.
- **Efisiensi Split:** Menggunakan `.split()` jauh lebih efisien dan bersih daripada melakukan iterasi karakter per karakter untuk mencari angka di dalam sebuah kalimat string.
- **Constraint di HackerRank:** Batasan (Constraints) yang tertulis di soal merupakan acuan bagi pemrogram bahwa input data tidak akan keluar dari rentang tersebut. Pemrogram tidak wajib membuat validasi manual menggunakan `if` untuk mengecek constraint tersebut kecuali diminta secara eksplisit.
- **Lambda dalam Sorting:** Untuk sorting yang kompleks (misalnya mengurutkan berdasarkan kemunculan terbanyak sekaligus urutan alfabet), Python dapat menggunakan parameter `key` dengan `lambda` untuk menentukan prioritas pengurutan pada Dictionary.



## Bab 2 Nested List Hackerrank


## 1. Deskripsi Tantangan (Problem Description)

Tantangan **Nested Lists** pada HackerRank dirancang untuk menguji pemahaman Anda dalam mengelola struktur data list di dalam list (sub-list). Tujuan utama dari latihan ini adalah:

- Menerima input berupa nama mahasiswa (string) dan nilai (float/integer) untuk sejumlah N mahasiswa.
- Menyimpan data tersebut ke dalam struktur data yang terorganisir.
- Mencari dan menampilkan nama mahasiswa yang memiliki **nilai terendah kedua** (_second lowest grade_).

**Visualisasi Struktur Data (Nested List):** Data akan disimpan dalam format seperti berikut: `students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]`

**Aturan Penulisan Output:** Jika terdapat lebih dari satu mahasiswa yang memiliki nilai terendah kedua tersebut, nama-nama mereka harus diurutkan secara alfabetis sebelum dicetak ke layar.

## 2. Batasan Masalah (Constraints)

Dalam platform kompetitif seperti HackerRank, batasan masalah adalah **Test Case Guarantees**. Anda tidak perlu melakukan validasi manual (seperti blok `if-condition` tambahan) karena input dipastikan memenuhi kriteria berikut:

- **Jumlah mahasiswa (**N**):** Berkisar antara 2 hingga 5 mahasiswa.
- **Tipe Data:** Nama berupa string dan nilai berupa float atau integer.
- **Kepastian Solusi:** Dipastikan akan selalu ada satu atau lebih mahasiswa yang memiliki nilai terendah kedua (tidak semua mahasiswa memiliki nilai yang sama persis).

## 3. Daftar Fungsi dan Metode Python

Berikut adalah instrumen pemrograman yang krusial untuk menyelesaikan tantangan ini:

|Fungsi/Metode|Deskripsi Singkat|
|---|---|
|`input()`|Meminta input dari pengguna melalui keyboard sebagai string.|
|`int()` / `float()`|Melakukan casting tipe data string ke angka bulat atau desimal.|
|`split()`|Memecah string menjadi list berdasarkan separator (default: spasi).|
|`append()`|Menambahkan elemen baru (termasuk sub-list) ke dalam list utama.|
|`set()`|Digunakan untuk mengisolasi nilai unik (menghapus duplikasi skor) agar nilai terendah kedua dapat diindeks dengan akurat.|
|`sorted()`|Mengurutkan elemen. Mengembalikan list baru dalam urutan menaik (_ascending_).|
|`items()`|Mengambil pasangan _key_ (skor) dan _value_ (list nama) dari dictionary untuk iterasi.|
|`lambda`|Fungsi anonim untuk kustomisasi logika pengurutan kompleks pada `sorted()`.|

## 4. Logika Penyelesaian Masalah (Problem Solving Logic)

4.1 Pendekatan Nested List

1. **Inisialisasi:** Buat list kosong `students = []`.
2. **Input Loop:** Gunakan perulangan untuk memasukkan sub-list `[nama, nilai]` ke dalam list utama menggunakan `append()`.
3. **Ekstraksi Nilai:** Ambil semua skor saja dari list utama (bisa menggunakan _list comprehension_).
4. **Unique & Sort:** Gunakan `set()` pada list skor untuk membuang duplikasi, lalu urutkan dengan `sorted()`.
5. **Identifikasi Target:** Ambil skor pada indeks ke-1 dari list skor unik. Ini adalah nilai terendah kedua.
6. **Filtering:** Filter list `students` untuk mengambil nama mahasiswa yang memiliki skor sama dengan nilai terendah kedua.
7. **Output:** Urutkan nama-nama hasil filter secara alfabetis dan cetak satu per satu.

4.2 Pendekatan Dictionary (**Highly Recommended**)

Pendekatan ini sangat disarankan untuk skenario data yang lebih besar karena memetakan satu skor ke banyak nama secara efisien.

1. **Struktur Data:** Gunakan dictionary dengan **Skor** sebagai _Key_ dan **List Nama** sebagai _Value_.
2. **Pemetaan:** Saat iterasi input, cek apakah skor sudah ada di dictionary. Jika belum, buat entri baru; jika sudah ada, tambahkan nama ke dalam list value-nya.
3. **Sorting Keys:** Ambil semua _keys_ (skor) dari dictionary, kemudian urutkan.
4. **Identifikasi Skor:** Pilih skor pada posisi indeks ke-1 (terendah kedua).
5. **Tie-breaker & Output:** Ambil list nama yang berasosiasi dengan skor tersebut. Urutkan list nama tersebut secara alfabetis (sebagai penangan jika ada lebih dari satu nama), lalu cetak.

6. Implementasi Kode Python

Berikut adalah implementasi menggunakan logika pengurutan dan pembersihan duplikasi yang optimal:

```
if __name__ == '__main__':
    students = []
    # Loop input berdasarkan jumlah N mahasiswa
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Mengisolasi skor unik dan mengurutkannya
    # unique_grades[1] secara spesifik menargetkan nilai terendah kedua
    unique_grades = sorted(set([s[1] for s in students]))
    second_lowest_grade = unique_grades[1]

    # Mencari nama mahasiswa yang memiliki skor tersebut
    # Melakukan sorting alfabetis secara langsung pada hasil filter
    result_names = sorted([s[0] for s in students if s[1] == second_lowest_grade])

    # Mencetak nama satu per satu
    for name in result_names:
        print(name)
```

6. Wawasan Instruktur (Audio Insight)

Sebagai pemahaman mendalam bagi mahasiswa tingkat lanjut, perhatikan poin-poin berikut:

- **Lazy Operator:** Fungsi `map()` adalah _lazy operator_. Artinya, Python tidak langsung memproses pemetaan di memori sampai data tersebut benar-benar diminta (misalnya saat dikonversi menjadi `set` atau `list`). Ini sangat efisien untuk menangani dataset besar.
- **Efisiensi Dictionary:** Dictionary jauh lebih intuitif untuk memetakan hubungan _one-to-many_ (satu skor milik banyak mahasiswa). Hal ini mencerminkan cara kerja pengindeksan data di dunia nyata.
- **Kustomisasi Sorting (The Tuple Trick):** Dalam kasus lebih kompleks seperti soal "Company Logo", kita sering menggunakan `lambda` untuk multi-kriteria sorting. Contoh: `sorted(data, key=lambda x: (-x[1], x[0]))`.
    - `-x[1]` (negatif) memaksa angka diurutkan secara **descending** (terbesar ke terkecil).
    - `x[0]` memastikan string diurutkan secara **ascending** (A ke Z).
    - Ini adalah teknik "Senior Instructor" untuk menangani dua aturan pengurutan dalam satu baris kode.
- **Pentingnya Constraints:** Ingatlah bahwa batasan di HackerRank adalah janji sistem. Anda tidak perlu membuang waktu menulis kode defensif (seperti `if N < 2`) jika sistem sudah menjamin bahwa N minimal bernilai 2. Fokuslah pada efisiensi logika inti.

Gemini Notebook can be inaccurate; please double check its responses.



## Bab 3 Latihan HackerRank List Commands

Panduan Studi: Topik 3 Latihan HackerRank List Commands

Dokumen ini menyajikan panduan komprehensif untuk menyelesaikan tantangan pemrograman Python pada platform HackerRank, khususnya Topik 3 mengenai **List Commands**. Panduan ini disusun berdasarkan diskusi teknis, alur logika penyelesaian masalah, dan wawasan instruksional guna memastikan pemahaman mendalam terhadap manipulasi objek list di Python.

## 1. Deskripsi Latihan

Tantangan ini mengharuskan pengembang untuk menginisialisasi sebuah list kosong dan melakukan serangkaian perintah manipulasi berdasarkan input yang diberikan. Terdapat N buah perintah yang harus diproses satu per satu, di mana setiap perintah merujuk pada metode bawaan (_built-in methods_) dari tipe data list di Python.

## 2. Daftar Fungsi dan Metode List

Berdasarkan persyaratan latihan, berikut adalah metode-metode list yang perlu diimplementasikan:

|Perintah|Deskripsi Fungsi|Contoh Input|
|---|---|---|
|`insert`|Memasukkan integer e pada indeks ke-i|`insert 0 5`|
|`print`|Mencetak seluruh isi list ke layar|`print`|
|`remove`|Menghapus kemunculan pertama dari elemen e|`remove 6`|
|`append`|Menambahkan elemen e ke akhir list|`append 10`|
|`sort`|Mengurutkan elemen di dalam list secara ascending|`sort`|
|`pop`|Menghapus elemen terakhir dari list|`pop`|
|`reverse`|Membalik urutan elemen di dalam list|`reverse`|

## 3. Constraints dan Format Input

- **Format Input:** Baris pertama berisi integer N yang menyatakan jumlah perintah. N baris berikutnya berisi perintah-perintah yang disebutkan dalam tabel di atas.
- **Batasan:** Perintah harus diproses secara berurutan sesuai urutan input.
- **Tipe Data:** Input yang diterima dari keyboard awalnya berupa string, sehingga diperlukan konversi tipe data (_casting_) untuk parameter angka.

## 4. Alur Logika Penyelesaian

Berdasarkan diskusi teknis, alur logika untuk menyelesaikan masalah ini adalah sebagai berikut:

1. **Inisialisasi:** Buat sebuah variabel list kosong (misalnya `numbers = []`).
2. **Input Jumlah Perintah:** Baca nilai N dan konversi menjadi integer menggunakan `int(input())`.
3. **Iterasi Perintah:** Lakukan perulangan (_loop_) sebanyak N kali.
4. **Parsing Input:**
    - Gunakan metode `.split()` pada input string untuk memecah perintah.
    - Secara default, `.split()` akan membagi string berdasarkan spasi.
    - Elemen pertama (indeks 0) dari hasil split adalah tipe perintah (`command type`).
5. **Logika Kondisional:**
    - Gunakan struktur `if-elif-else` untuk menentukan aksi berdasarkan `command type`.
    - Jika perintah membutuhkan parameter (seperti `insert`, `append`, atau `remove`), ambil elemen berikutnya dari hasil split dan lakukan _casting_ ke integer.
6. **Eksekusi:** Panggil metode list yang sesuai pada variabel list yang telah diinisialisasi.

7. Implementasi Kode Python

Berikut adalah implementasi kode Python murni berdasarkan logika yang didiskusikan:

```
if __name__ == '__main__':
    N = int(input())
    numbers = []

    for _ in range(N):
        # Membaca perintah dan memecahnya berdasarkan spasi
        parts = input().split()
        command = parts[0]

        if command == "insert":
            index = int(parts[1])
            element = int(parts[2])
            numbers.insert(index, element)
        elif command == "print":
            print(numbers)
        elif command == "remove":
            element = int(parts[1])
            numbers.remove(element)
        elif command == "append":
            element = int(parts[1])
            numbers.append(element)
        elif command == "sort":
            numbers.sort()
        elif command == "pop":
            numbers.pop()
        elif command == "reverse":
            numbers.reverse()
```

## 6. [Wawasan Dosen / Audio Insight]

Berikut adalah poin-poin penting dan tips tambahan yang ditekankan selama sesi diskusi untuk meningkatkan kualitas kode dan pemahaman logika:

- **Fleksibilitas** **.split()****:** Metode `.split()` tanpa parameter secara otomatis mendeteksi _white space_ (spasi, tab, enter) sebagai pemisah. Hal ini sangat berguna untuk menangani input seperti `insert 0 5` yang memiliki panjang elemen berbeda dengan perintah `print`.
- **Pentingnya Casting:** Semua input yang diambil melalui fungsi `input()` di Python secara default bertipe string. Kegagalan melakukan _casting_ ke `int()` saat menjalankan perintah `insert` atau `append` akan menyebabkan error atau perilaku program yang tidak diinginkan karena list akan menyimpan string, bukan angka.
- **Penanganan Error Indeks:** Saat melakukan parsing perintah seperti `parts[1]` atau `parts[2]`, pengembang harus memastikan bahwa elemen tersebut memang ada dalam hasil split untuk menghindari `IndexError: list index out of range`. Namun, dalam konteks HackerRank, input biasanya dijamin sesuai dengan format yang dijanjikan.
- **Lazy Operation:** Memahami konsep operasional di Python sangat penting. Contohnya, fungsi `map()` bersifat _lazy operation_, artinya fungsi tersebut tidak akan dieksekusi sampai hasilnya benar-benar dibutuhkan oleh fungsi lain (seperti saat dikonversi menjadi `list` atau `set`).
- **Manipulasi Dictionaries:** Meskipun Topik 3 fokus pada List, penggunaan Dictionary juga dibahas sebagai alternatif efektif jika masalah melibatkan pemetaan kunci dan nilai (misalnya skor dan nama mahasiswa), di mana kunci dapat diurutkan secara independen dari nilainya.



## Bab 4  Latihan HackerRank Company Logo

Study Guide: Topik 4 - Latihan HackerRank Company Logo

Study Guide ini disusun untuk membantu memahami logika penyelesaian masalah pemrograman Python melalui platform HackerRank, khususnya pada tantangan _Company Logo_. Dokumen ini merangkum diskusi teknis mengenai penggunaan tipe data Dictionary, fungsi Lambda untuk sorting kustom, serta penanganan batasan (constraints) dalam kode.

## 1. Logika Penyelesaian Masalah: Company Logo

Masalah utama dalam _Company Logo_ adalah menghitung frekuensi kemunculan setiap karakter dalam sebuah String dan menampilkan tiga karakter yang paling sering muncul. Jika jumlah kemunculan sama, maka karakter diurutkan berdasarkan urutan alfabet (alphabetical order).

1.1. Pendekatan Dictionary

Dictionary digunakan sebagai instrumen penghitung (_counter_) karena efisiensinya dalam memetakan kunci (Key) ke nilai (Value).

- **Key:** Menyimpan karakter unik dari String (huruf).
- **Value:** Menyimpan jumlah kemunculan karakter tersebut (integer).
- **Proses:** Lakukan Loop pada setiap karakter dalam String. Jika karakter belum ada dalam Dictionary, inisialisasi dengan nilai 1. Jika sudah ada, lakukan increment pada Value-nya.

1.2. Pendekatan Fungsi Lambda untuk Sorting

Fungsi Lambda sangat krusial dalam metode `sorted()` untuk menangani dua kriteria pengurutan sekaligus:

1. **Prioritas 1 (Occurrence Count):** Diurutkan secara Descending (besar ke kecil). Dalam kode, ini diwakili dengan tanda negatif (`-`) pada Value.
2. **Prioritas 2 (Alphabetical):** Jika frekuensi sama, diurutkan secara Ascending (A-Z). Dalam kode, ini diwakili dengan nilai positif pada Key.

 ## 2. Constraints (Batasan Masalah)

Berdasarkan spesifikasi teknis, solusi harus mematuhi batasan berikut:

- **Panjang String S:** Minimal 3 karakter dan maksimal 104 karakter (3≤len(S)≤104).
- **Karakter Unik:** String dijamin memiliki setidaknya 3 karakter yang berbeda.
- **Format Huruf:** String biasanya berisi _lowercase letters_ (huruf kecil).
- **Output:** Hanya menampilkan **top three** (tiga besar) karakter yang paling sering muncul beserta jumlah kemunculannya.

## 3. Daftar Fungsi dan Metode Python

Berikut adalah fungsi dan metode yang digunakan dalam latihan Topik 4:

|Fungsi / Metode|Kegunaan|
|---|---|
|`.split()`|Memecah String menjadi List berdasarkan separator (default-nya adalah _white space_).|
|`set()`|Mengubah List menjadi Set untuk menghapus nilai duplikat (menghasilkan nilai unik).|
|`sorted()`|Mengurutkan elemen dalam _iterable_ (seperti List atau Dictionary Items).|
|`.items()`|Mengembalikan pasangan Key dan Value dari Dictionary untuk keperluan iterasi atau sorting.|
|`lambda`|Fungsi anonim untuk mendefinisikan logika sorting kustom dalam satu baris.|
|`.append()`|Menambahkan elemen baru ke posisi terakhir dalam sebuah List.|
|`int()`|Melakukan casting atau konversi tipe data String/Float menjadi Integer.|
|`input()`|Mengambil input dari pengguna melalui keyboard.|

## 4. Implementasi Kode Python

Berikut adalah kumpulan kode murni berdasarkan diskusi teknis untuk menyelesaikan masalah _Company Logo_ dan logika terkait:

4.1. Solusi Company Logo (Dictionary & Lambda)

```
if __name__ == '__main__':
    s = input()
    
    # Inisialisasi Dictionary untuk menghitung huruf
    letter_counter = {}
    
    for letter in s:
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
            
    # Sorting menggunakan Lambda
    # Item 1 (Value) di-sort descending (-), Item 0 (Key) di-sort ascending
    result = sorted(letter_counter.items(), key=lambda x: (-x[1], x[0]))
    
    # Menampilkan 3 karakter teratas
    for i in range(3):
        print(result[i][0], result[i][1])
```

4.2. Logika Runner-Up Score (Set & Sorted)

```
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Menghapus duplikat dengan set, lalu di-sort
    unique_scores = sorted(set(arr))
    
    # Mengambil skor tertinggi kedua (index -2)
    print(unique_scores[-2])
```

## 5. [Wawasan Dosen / Audio Insight]

Bagian ini merangkum poin-poin penting dari diskusi instruktur mengenai logika pemrograman Python:

- **Pentingnya HackerRank:** Platform ini sering digunakan untuk _Technical Test_ pada peran IT seperti Software Engineer, AI Engineer, dan Data Scientist. Memahami logika di sini membantu mempersiapkan diri untuk tes masuk kerja.
- **Lazy Operator pada fungsi** **map()****:** Fungsi `map()` bersifat _lazy_. Artinya, proses konversi (seperti mengubah String ke Integer) tidak langsung dijalankan sampai hasilnya benar-benar dibutuhkan (misalnya saat diubah menjadi List atau Set).
- **Dictionary vs List:** Untuk kasus pencarian frekuensi karakter, Dictionary jauh lebih intuitif dan efisien dibandingkan Nested List karena kita bisa langsung mengakses Key (karakter) untuk melakukan _update_ nilai kemunculannya.
- **Handling Constraints:** Di HackerRank, batasan (constraints) adalah acuan untuk test case. Programmer tidak perlu membuat pengecekan `if` manual untuk memvalidasi apakah input sudah sesuai batasan, karena sistem dijamin memberikan input yang masuk dalam rentang batasan tersebut.
- **Logika Slicing dan Sorting:** Penggunaan indeks negatif (seperti `[-2]`) adalah cara cepat di Python untuk mengakses elemen dari urutan paling belakang tanpa perlu menghitung panjang List secara manual.



---


# Module 1 Session 7 Object Oriented Programming


## Bab 1 Pendahuluan Object Oriented Programming (OOP)

## 1.1 Definition dan Characteristics dari OOP

### A. Conceptual Foundation

- Object-Oriented Programming (OOP) merupakan sebuah _software design paradigm_ yang mengorganisasi _code_ di sekitar _objects_ (_data_) dibandingkan di sekitar _functions_ dan _logic_.
- _Paradigm_ ini memodelkan _real-world entities_ dengan mengelompokkan _data_ (_attributes_) dan _behaviors_ (_methods_) ke dalam satu kesatuan _unit_ yang kohesif (_single cohesive unit_).
- Di dunia nyata, segala sesuatu yang ada di sekitar kita dapat diposisikan sebagai kumpulan dari _objects_ (seperti _laptop_, _handphone_, _tumblr_, atau _user_).

### B. Attributes dan Methods dalam OOP

- Setiap _object_ didefinisikan oleh dua karakteristik utama, yaitu:
    - _Attributes_: _Data_ yang merepresentasikan _state_ atau identitas dari sebuah _object_ (misalnya: _name_, _age_, _email_ pada _object_ _user_).
    - _Methods_: _Function_ yang menggambarkan kemampuan atau _behavior_ dari _object_ tersebut, yang menempel pada _object_ yang bersangkutan (misalnya: _update_info_, _get_info_, _greet_).

#### [Wawasan Diskusi / Audio Insight]

- Dalam program _AI engineering_, materi terkait OOP sering kali dilewati karena pembelajaran Python dilakukan secara sekilas. Padahal, pemahaman konsep dasar OOP sangat krusial agar tidak membingungkan saat masuk ke dalam implementasi praktis yang banyak menggunakan _paradigm_ ini.
- Untuk kebutuhan _AI engineering_, fokus utama ditekankan pada penguasaan dasar-dasar OOP seperti _class_ (sebagai _blueprint_), _object_ (sebagai _instance_), _attributes_, dan _methods_. Konsep tingkat lanjut yang sangat mendalam seperti _encapsulation_, _abstraction_, dan _polymorphism_ jarang digunakan secara intensif dalam pekerjaan sehari-hari di bidang ini.

---

## 1.2 Perbandingan Procedural Programming dan Object-Oriented Programming (OOP)

### A. Paradigm Organisasi Code

- Perbedaan struktural utama antara _procedural programming_ dan _object-oriented programming_ terletak pada pemisahan dan pengelompokan _data_ serta _functions_:

|Karakteristik|Procedural Programming|Object-Oriented Programming (OOP)|
|:--|:--|:--|
|**Organisasi Utama**|Berfokus pada _functions_ dan _logic_.|Berfokus pada _objects_ dan _data_.|
|**Relasi Data & Function**|_Function_ (_behavior_) dan _data_ terkait berada dalam _unit_ atau _logic_ yang terpisah (_separate unit/logic_).|_Function_ (_behavior_) dan _data_ terkait disatukan dalam satu grup _code_ (_class unit_).|
|**Aksesibilitas Function**|_Function_ dibuat secara mandiri dan dapat digunakan oleh _object_ atau _data type_ apa saja secara bebas.|_Methods_ (_functions_) menempel secara eksklusif pada _object_ tertentu dan hanya milik _object_ tersebut.|

### B. Perbandingan melalui Implementasi Code Python

- Berikut adalah perbandingan sintaksis konkret antara _procedural approach_ dan _OOP approach_ pada Python:

#### 1. Procedural Programming Approach

- Pada _procedural approach_, _data_ didefinisikan secara independen sebagai variabel-variabel terpisah, dan _functions_ eksternal menerima _data_ tersebut untuk melakukan operasi:

```
name = "Alex"
email = "alex@ex.com"
age = 20

def update_email(new_email):
    global email
    email = new_email

def get_user_info():
    return {
        "name" : name,
        "email" : email,
        "age" : age,
    }

def send_email():
    return f"email send to {email}"
```

#### 2. Object-Oriented Programming (OOP) Approach

- Pada _object-oriented approach_, seluruh _data_ (_attributes_) dan _functions_ (_methods_) dibungkus bersama di dalam sebuah deklarasi _class_:

```
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def change_email(self, new_email):
        self.email = new_email

    def get_user_info(self):
        return self.__dict__

    def send_email(self):
        return f"email send to {self.email}"
```

#### [Wawasan Diskusi / Audio Insight]

- Tanpa disadari, ketika memprogram menggunakan Python, kita sudah sering menggunakan _built-in data types_ berbasis _OOP paradigm_. Contohnya adalah _data type_ _list_ atau _dictionary_, di mana setiap kali kita melakukan _instantiation_ (seperti membuat _list_ kosong), kita sebenarnya sedang memanggil _constructor_ dari _class_ _list_.
- _Built-in data types_ tersebut memiliki _methods_ eksklusif yang menempel padanya (seperti `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, dan `.clear()`) yang tidak dapat digunakan oleh _data type_ lain yang berbeda _class_ _blueprint_-nya.

---

## 1.3 Alasan Penggunaan dan Complexity Management

### A. Mengelola Complexity Perangkat Lunak

- Seiring dengan perkembangan skala perangkat lunak, mengorganisasi _code_ murni hanya berdasarkan _functions_ dan _logic_ prosedural akan membuat hubungan (_relationship_) antara _data_ dan _behavior_ menjadi semakin sulit dikelola (_harder to manage_).
- OOP menyediakan mekanisme alternatif untuk mengorganisasi _complexity_ tersebut agar lebih terstruktur dan rapi.

### B. Efisiensi Passing Data (_Self-Tracking Data_)

- Perbandingan efisiensi pengelolaan variabel _state_ tanpa OOP dan dengan OOP adalah sebagai berikut:

|Parameter Perbandingan|Tanpa OOP (Procedural)|Dengan OOP|
|:--|:--|:--|
|**Pengelolaan State**|Pengembang harus secara berulang kali mengirimkan (_repeatedly pass_) _data_ _state_ (seperti _account balance_) ke setiap _function_ yang membutuhkannya.|_Object_ melacak _data_-nya sendiri secara internal (_keeps track of its own balance_), menghilangkan kebutuhan _passing parameter_ berulang kali.|
|**Ketergantungan Function**|_Function_ sangat bergantung pada _parameter_ luar yang dipasok secara eksplisit pada setiap pemanggilan.|_Methods_ dapat mengakses _data_ _object_ kapan saja melalui referensi internal (`self`).|

- Ilustrasi perbandingan manajemen _account balance_ pada _bank account_:

#### 1. Non-OOP Approach (Repeatedly passing data)

- Pada pendekatan ini, _data_ saldo harus terus disuplai secara manual ke _function_ `deposit` atau `withdraw`:

```
def deposit(account_balance, amount):
    return account_balance + amount

def withdraw(account_balance, amount):
    if amount <= account_balance:
        return account_balance - amount
    return account_balance

account_balance_1 = 100
account_balance_2 = 200

account_balance_1 = deposit(account_balance_1, 100)
account_balance_2 = deposit(account_balance_2, 200)

account_balance_1 = withdraw(account_balance_1, 10)
account_balance_2 = withdraw(account_balance_2, 30)
```

#### 2. OOP Approach (Object mengelola datanya sendiri)

- Dengan menggunakan _class_ dan _object_, setiap _instance_ melacak _balance_-nya sendiri:

```
class Account:
    def __init__(self, amount):
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

account_1 = Account(100)
account_2 = Account(200)

account_1.deposit(100)
account_2.deposit(200)

account_1.withdraw(10)
account_2.withdraw(30)
```

#### [Wawasan Diskusi / Audio Insight]

- Implementasi OOP memisahkan alamat memori (_memory address_) untuk setiap _object_ secara terpisah. Ketika kita membuat `account_1` and `account_2` dari _class_ `Account` yang sama, kedua _objects_ tersebut tetap merupakan entitas yang terpisah secara independen di memori. Segala perubahan keadaan (_state change_) seperti penambahan _balance_ pada satu akun tidak akan memengaruhi _balance_ akun lainnya.



## Bab 2  Konsep Dasar Class dan Object

## 2.1 Definition dan Characteristics dari Class

### A. Conceptual Foundation

- _Class_ merupakan sebuah _blueprint_ (cetak biru) yang menetapkan _data_ (_attributes_) dan _behaviors_ (_methods_) yang dapat dimiliki oleh suatu tipe _object_.
- Saat membuat sebuah _class_, kita tidak sedang mendefinisikan suatu entitas secara spesifik, melainkan membuat sebuah representasi umum (_general representation_) mengenai apa saja yang dapat dimiliki dan dilakukan oleh tipe _object_ tersebut.

### B. Analogy dari Class

- Analogi nyata dari sebuah _class_ adalah ketika kita mengamati mobil (_cars_):
    - _Attributes_ (Karakteristik/Data): Setiap mobil secara umum memiliki kapasitas bahan bakar (_fuel_capacity_), tipe mobil (_type_of_car_), dan jenis mesin (_engine_type_).
    - _Behaviors_ (Kemampuan/Perilaku): Setiap mobil secara umum dapat membunyikan klakson (_honk()_), melaju ke depan (_move_forward()_), melakukan akselerasi (_accelerate()_), bergerak mundur (_move_backward()_), dan mengerem (_brake()_).
- Representasi umum dari karakteristik dan perilaku mobil inilah yang didefinisikan di dalam sebuah _Class_.

### C. Python Implementation dari Class

- Berikut adalah sintaks dasar untuk mendefinisikan sebuah _Class_ di Python menggunakan kata kunci `class`:

```
class Car:
    type_name = "suv"
    fuel_capacity = 45
    engine_type = "petrol"

    def honk(self):
        pass

    def move_forward(self):
        pass

    def brake(self):
        pass
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa mendefinisikan sebuah _class_ mirip seperti membuat sebuah formulir (_form_). Formulir tersebut menetapkan kolom-kolom kosong apa saja yang harus diisi, seperti _fuel_capacity_, _type_of_car_, dan _engine_type_.
- Selain atribut standar di atas, mahasiswa mengusulkan beberapa _attributes_ tambahan yang dapat mendefinisikan mobil, seperti jumlah ban/roda (_bannya/roda_), warna (_color_), merek (_brand_), dan tahun pembuatan (_year of manufacture_).
- Untuk bagian _behaviors_, mahasiswa juga mengusulkan perilaku tambahan seperti belok kanan (_turn right_), belok kiri (_turn left_), dan posisi gigi netral (_gear neutral_).
- Analogi industri nyata yang diberikan oleh dosen adalah platform _e-commerce_ Shopee:
    - _Class_ _User_ di Shopee didefinisikan dengan _attributes_ berupa _name_, _ID_, _password_, tanggal lahir, dan _gender_.
    - _Behaviors_ (_methods_) yang melekat pada _Class_ _User_ tersebut meliputi tindakan seperti tambah ke keranjang (_add to cart_), melakukan _check out_, masuk log (_sign in_), dan keluar log (_sign out_).

---

## 2.2 Definition dan Characteristics dari Object

### A. Instance dari Class

- _Object_ merupakan instansiasi spesifik (_specific instance_) dari sebuah _class_.
- Ketika kita telah memiliki _blueprint_ (_class_), kita memerlukan objek nyata yang dibangun berdasarkan cetak biru tersebut untuk dapat digunakan di dalam program.
- _Object_ yang dibuat dari _class_ yang sama akan berbagi _attributes_ dan _behaviors_ yang didefinisikan oleh _class_ tersebut, namun masing-masing _object_ memiliki data keadaan (_state_) sendiri.

### B. State dan Memory Allocation

- Setiap _object_ yang dibuat bersifat independen satu sama lain dan disimpan pada alamat memori (_memory address_) yang berbeda.
- Perubahan keadaan (_state change_) pada satu _object_ tidak akan memengaruhi keadaan _object_ lainnya. Sebagai contoh, jika kita membuat dua objek mobil dari _class_ yang sama, ketika mobil pertama bergerak maju (_move_forward()_), posisinya akan berubah tanpa memengaruhi posisi mobil kedua.

### C. Python Implementation dari Object Creation

- Berikut adalah cara melakukan _instantiation_ (pembuatan _object_) dari sebuah _class_ dan bagaimana _object_ tersebut beroperasi secara independen di memori:

```
class Car:
    type_name = "suv"
    fuel_capacity = 45
    engine_type = "petrol"
    color = "red"
    position = 0

    def honk(self):
        print("Tin! Tin!")

    def move_forward(self):
        self.position += 1

    def brake(self):
        print("brake!")

# Instantiation (pembuatan object)
car_john = Car()
car_emily = Car()

# Mengakses attributes
print(car_john.color)      # Output: red
print(car_emily.color)     # Output: red

# Memanggil methods
car_john.honk()            # Output: Tin! Tin!
car_john.move_forward()

# Memeriksa perbedaan state masing-masing object
print(car_john.position)   # Output: 1
print(car_emily.position)  # Output: 0
```

#### [Wawasan Diskusi / Audio Insight]

- Di dunia nyata, segala sesuatu di sekeliling kita pada dasarnya adalah kumpulan dari _objects_, seperti _laptop_, _handphone_, _tumblr_, atau _user_.
- Proses pembuatan _object_ dilakukan dengan memanggil _constructor_, yaitu menuliskan nama _class_ diikuti dengan tanda kurung buka dan tutup (seperti `Car()`), lalu menyimpannya ke dalam suatu variabel (misalnya `car_john = Car()`).
- Pengecekan identitas menggunakan operator `is` (misalnya `car_john is car_emily`) akan mengembalikan nilai `False`. Hal ini membuktikan bahwa meskipun dibuat dari _class_ yang sama, keduanya merupakan dua _objects_ terpisah dengan alamat memori (_memory address_) yang berbeda secara independen.
- Hubungan _Class_ dan _Object_ dengan _Built-in Data Types_ di Python:
    - Tanpa disadari, tipe data bawaan Python seperti _list_ dan _dictionary_ merupakan sebuah _Class_ yang dibuat oleh pengembang Python.
    - Saat kita menuliskan kode untuk membuat _list_ kosong seperti `my_list = []` atau `my_list = list()`, kita sebenarnya sedang memanggil _constructor_ dari _Class_ _list_ untuk menciptakan sebuah _Object_ (_instance_) baru.
    - Setiap _Object_ dari kelas _list_ tersebut memiliki akses ke _methods_ eksklusif yang didefinisikan di dalam cetak birunya, seperti `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, dan `.clear()`.
    - _Methods_ tersebut hanya dapat digunakan oleh objek yang bertipe kelas _list_ dan tidak dapat dipanggil secara sembarangan oleh tipe objek lain dari kelas yang berbeda.



## Bab 3 Konstruktor __init__ dan Atribut self

## 3.1 Konstruktor **init** dalam Class

### A. Conceptual Foundation dari **init**

- _**init**_ merupakan sebuah _special method_ di Python yang bertindak sebagai _constructor_ untuk membangun _object_ dari suatu _class_.
- _Constructor_ ini dijalankan secara otomatis (_automatically runs_) pada saat sebuah _object_ diinisialisasi atau diciptakan.
- Fungsi utama dari _**init**_ adalah untuk memberikan nilai awal (_initial values_) bagi konfigurasi, _attributes_, atau _state_ dari _object_ tersebut pada saat pertama kali dibuat.

### B. Perbedaan Pengisian State Tanpa dan Dengan **init**

- Tanpa menggunakan _**init**_, setiap _object_ yang diinstansiasi dari _class_ yang sama akan memiliki _state_ awal yang identik (misalnya semua objek mobil otomatis bertipe SUV, berwarna merah, posisi 0, dll.).
- Dengan menggunakan _**init**_, kita dapat membedakan konfigurasi setiap _object_ sejak awal proses inisialisasi (_initialization_).

|Pendekatan|Karakteristik Inisialisasi|Dampak pada Object|
|:--|:--|:--|
|**Without **init****|Atribut di-_hardcode_ secara langsung di dalam badan _class_.|Semua _objects_ yang dibuat memiliki nilai _attributes_ yang identik pada awal pembuatan.|
|**With **init****|Atribut diinisialisasi secara dinamis melalui argumen yang dikirim ke _constructor_.|Setiap _object_ dapat memiliki _configuration_ dan _state_ awal yang unik sejak pembuatan.|

### C. Python Implementation dari **init**

- Berikut adalah implementasi pendefinisian _class_ dengan dan tanpa menggunakan _**init**_:

#### 1. Class Tanpa **init** (Attributes Identik)

```
class Car:
    type_name = "SUV"
    fuel_capacity = 45
    engine_type = "petrol"
    color = "red"
    position = 0

# Setiap objek akan selalu memiliki state awal yang sama
car_john = Car()
car_emily = Car()
```

#### 2. Class Dengan **init** (Attributes Dinamis)

```
class Car:
    def __init__(self, type_name, fuel_capacity, engine_type, color):
        self.type_name = type_name
        self.fuel_capacity = fuel_capacity
        self.engine_type = engine_type
        self.color = color
        self.position = 0

# Objek dikonstruksi dengan nilai awal berbeda
car_john = Car("sedan", 45, "petrol", "red")
car_emily = Car("SUV", 50, "petrol", "yellow")
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa kata "_construct_" secara harfiah berarti membangun. Jadi, _constructor_ adalah metode khusus yang digunakan untuk membangun atau mendirikan sebuah _object_ dari cetak birunya (_class_).
- Untuk memanggil _constructor_ di Python, pengguna cukup menuliskan nama _class_ diikuti dengan tanda kurung dan argumen yang diperlukan, misalnya `Car("sedan", 45, "petrol", "red")`. Tindakan ini secara otomatis memicu eksekusi metode `__init__` di latar belakang.
- Mahasiswa mengamati bahwa _special method_ ini selalu diawali dan diakhiri dengan dua karakter _underscore_ (`__init__`), yang menandakan metode tersebut merupakan _magic method_ bawaan Python yang memiliki perilaku khusus.

---

## 3.2 Atribut self dan Referensi Current Object

### A. Conceptual Foundation dari self

- _self_ adalah variabel referensi bawaan di Python yang merujuk secara eksklusif kepada _current object_ (objek saat ini yang sedang diproses atau diakses oleh program).
- Di dalam definisi _class_, _self_ digunakan untuk mengakses _attributes_ dan _methods_ milik objek tersebut secara internal.
- Setiap kali kita mendefinisikan _method_ di dalam _class_, parameter pertama dari _method_ tersebut secara mutlak harus diisi oleh _self_.

### B. Mekanisme Kerja self di Memori

- Ketika sebuah _method_ dipanggil melalui objek tertentu, Python secara otomatis melewatkan objek tersebut sebagai argumen pertama untuk parameter _self_.
- Melalui referensi _self_, Python mengetahui objek mana di memori yang data _attributes_-nya harus dibaca atau diubah, sehingga tidak terjadi tumpang tindih data antar-objek.

|Sintaks Pemanggilan|Interpretasi Internal Python|Keterangan|
|:--|:--|:--|
|`car_john.move_forward(10)`|`Car.move_forward(car_john, 10)`|Objek `car_john` dikirim sebagai parameter `self` secara otomatis.|
|`self.color`|Mengakses _attribute_ `color` dari objek pemanggil|Merujuk langsung ke alamat memori spesifik objek saat ini.|

### C. Python Implementation dari self

- Berikut adalah contoh untuk mengamati bagaimana _self_ menghubungkan pemanggilan _method_ ke objek yang bersangkutan:

```
class Car:
    def __init__(self, type_name, color):
        self.type_name = type_name
        self.color = color

    def print_current_object_info(self):
        # Mengakses attributes milik objek saat ini menggunakan self
        print(f"Type: {self.type_name}")
        print(f"Color: {self.color}")

car_john = Car("sedan", "red")

# Pemanggilan method
car_john.print_current_object_info()
```

#### [Wawasan Diskusi / Audio Insight]

- Berdasarkan penjelasan dosen, _self_ dapat dibayangkan sebagai cara objek merujuk ke "dirinya sendiri".
- Ketika kita membuat `car_john = Car("sedan", "red")`, maka di dalam memori, _self_ akan merujuk ke objek `car_john`. Jadi, pernyataan `self.type_name = type_name` diartikan oleh Python sebagai `car_john.type_name = "sedan"`.
- Demikian juga jika kita membuat `car_emily = Car("SUV", "yellow")`, maka _self_ untuk objek tersebut akan mengarah ke `car_emily`, sehingga `self.color = color` diterjemahkan sebagai `car_emily.color = "yellow"`. Hal inilah yang menjamin bahwa perubahan _state_ pada satu objek disimpan secara terisolasi di alamat memori masing-masing dan tidak saling memengaruhi.

---

## 3.3 Attributes vs Parameters dalam Inisialisasi

### A. Definisi dan Batasan Peran

- _Attributes_ adalah variabel yang menempel langsung pada _class_ atau objek (ditandai dengan awalan `self.`), dan bertindak sebagai penyimpan data keadaan (_state_) dari objek tersebut.
- _Parameters_ adalah variabel lokal yang didefinisikan di dalam tanda kurung metode _**init**_ yang bertugas menerima pasokan nilai (_inputs_) dari luar pada saat objek dibuat.

### B. Aturan Hubungan dan Kustomisasi Atribut

- Atribut tidak harus selalu diisi langsung dari nilai parameter. Kita dapat menentukan apakah suatu atribut dapat dikustomisasi oleh pengguna saat pembuatan objek, atau dikunci dengan nilai default tertentu.
- Jika sebuah atribut ingin dikunci dengan nilai default (misalnya saldo rekening baru selalu dimulai dari `0`, atau posisi awal mobil selalu `0`), maka kita tidak perlu menyediakan parameter untuk atribut tersebut di dalam tanda kurung metode `__init__`.

|Tipe Data|Deklarasi Sintaks|Sifat Nilai|Kustomisasi Pengguna|
|:--|:--|:--|:--|
|**Attributes**|Diawali dengan `self.` (misal: `self.balance`)|Bertahan selama objek hidup di memori (_state_).|Tergantung pada keberadaan parameter di _constructor_.|
|**Parameters**|Ditulis dalam parameter list `__init__` (misal: `balance`)|Bersifat sementara dan hancur setelah metode selesai dijalankan.|Ditentukan oleh nilai argumen yang dikirim saat instansiasi.|

### C. Python Implementation dari Attributes dan Parameters

- Berikut adalah contoh implementasi di mana kita membedakan atribut yang dapat dikustomisasi dengan atribut yang dikunci dengan nilai default:

```
class BankAccount:
    # owner_name dapat dikustomisasi, balance dikunci ke nilai default 0
    def __init__(self, owner_name):
        self.owner_name = owner_name  # Diisi dari parameter
        self.balance = 0             # Nilai default internal, tanpa parameter

# Instansiasi hanya mengirimkan satu argumen untuk owner_name
account_john = BankAccount("John")

print(account_john.owner_name)  # Output: John
print(account_john.balance)     # Output: 0
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menegaskan bahwa penamaan parameter di dalam tanda kurung `__init__` dan nama atribut yang diawali `self.` tidak harus sama. Sebagai contoh, kita bisa menulis `def __init__(self, A): self.owner_name = A`. Penamaan yang sama (seperti `self.owner_name = owner_name`) hanyalah sebuah kesepakatan (_convention_) yang umum digunakan oleh para pemrogram untuk mempermudah pembacaan kode.
- Untuk mengilustrasikan ini secara praktis, dalam latihan pembuatan _class_ `BankAccount`:
    - Atribut `owner_name` dan `balance` didefinisikan di bawah referensi `self` di dalam metode `__init__` (menjadi `self.owner_name` dan `self.balance`).
    - Jika pengguna ingin agar nilai awal `balance` dapat disesuaikan pada saat pembuatan akun, maka variabel `balance` harus dimasukkan sebagai parameter dalam `__init__` (misalnya `def __init__(self, owner_name, balance)`).
    - Namun, jika kita ingin saldo awal rekening selalu bernilai `0` tanpa bisa diubah saat inisialisasi, kita dapat menghapus parameter `balance` dari tanda kurung `__init__` dan menetapkan `self.balance = 0` secara langsung di dalam badan metode tersebut.



## Bab 4 Penambahan Behavior melalui Method

## 4.1 Definition dan Characteristics dari Methods

### A. Conceptual Foundation dari Methods

- _Method_ merupakan sebuah _function_ yang didefinisikan di dalam sebuah _class_ yang menggambarkan _behavior_ (perilaku atau kemampuan) yang dapat dilakukan oleh sebuah _object_.
- Perbedaan mendasar antara _attributes_ dan _methods_ di dalam _class_ adalah:

|Karakteristik|Attributes|Methods|
|:--|:--|:--|
|**Definisi**|Variabel yang menempel pada _class_ untuk menyimpan data atau keadaan (_state_) dari _object_.|_Function_ yang didefinisikan di dalam _class_ untuk menggambarkan tindakan (_behavior_) yang dapat dilakukan oleh _object_.|
|**Sintaksis**|Dideklarasikan seperti variabel biasa (misalnya: `self.fuel = 40`).|Dideklarasikan menggunakan kata kunci `def` di dalam _class_ (misalnya: `def move_forward(self)`).|
|**Penggunaan**|Digunakan untuk merepresentasikan identitas atau kondisi _object_.|Digunakan untuk memproses data, mengubah _state_, atau melakukan aksi tertentu.|

### B. Perbedaan antara Methods dan Regular Functions

- _Regular Function_ (fungsi biasa) didefinisikan secara mandiri di luar _class_. Fungsi ini bersifat global dan dapat menerima parameter berupa data apa saja secara bebas untuk diproses.
- _Method_ didefinisikan secara eksklusif di dalam sebuah _class_. _Method_ ini menempel pada _object_ tertentu hasil instansiasi _class_ tersebut dan tidak dapat dipanggil secara independen tanpa adanya _object_ penerima.

### C. Python Implementation dari Methods

- Berikut adalah implementasi penulisan _methods_ di dalam _class_ `Car` yang menunjukkan _behavior_ `get_info()` dan `move_forward()`:

```
class Car:
    def __init__(self, type_name, fuel=0):
        self.type_name = type_name
        self.fuel = fuel

    def get_info(self):
        print(self.__dict__)

    def move_forward(self, distance):
        if self.fuel > 0:
            print(f"Move {distance} km")
            self.fuel -= 1
        else:
            print("No fuel!")
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa tanpa disadari, kita sudah sangat sering menggunakan _methods_ bawaan dari _built-in data types_ Python.
- Contoh paling nyata adalah pada kelas _list_. Ketika kita memiliki _object_ berupa _list_ dan memanggil fungsi seperti `.pop()`, `.sort()`, `.append()`, `.extend()`, `.insert()`, `.remove()`, atau `.clear()`, fungsi-fungsi tersebut merupakan _methods_ yang menempel secara eksklusif pada cetak biru kelas _list_.
- _Methods_ ini tidak dapat digunakan secara sembarangan oleh tipe data lain yang tidak memiliki definisi _behavior_ tersebut di dalam cetak birunya.

---

## 4.2 Mekanisme Pemanggilan dan Aliran Eksekusi Methods

### A. Aliran Eksekusi Internal Python

- Ketika sebuah program memanggil sebuah _method_ pada suatu _object_ (misalnya: `car_john.move_forward(10)`), terdapat serangkaian langkah eksekusi internal yang dijalankan oleh interpreter Python:

|Tahap|Aktivitas Eksekusi Internal|
|:--|:--|
|**Langkah 1**|Program memicu pemanggilan _method_ pada instansi _object_ tertentu: `car_john.move_forward(10)`.|
|**Langkah 2**|Python mencari definisi dari _method_ bernama `move_forward` di dalam deklarasi _class_ `Car`.|
|**Langkah 3**|Jika _method_ ditemukan, Python secara otomatis melewatkan instansi _object_ itu sendiri (`car_john`) sebagai argumen pertama untuk parameter `self`, diikuti dengan argumen berikutnya (`10`) untuk parameter `distance`.|
|**Langkah 4**|Di dalam blok kode _method_, referensi `self` merujuk ke variabel keadaan milik `car_john` (`self.fuel` merujuk ke `car_john.fuel`).|
|**Langkah 5**|Blok logika di dalam _method_ dieksekusi. Jika `fuel > 0`, teks gerakan dicetak dan nilai `self.fuel` dikurangi.|
|**Langkah 6**|Setelah seluruh instruksi di dalam _method_ selesai diproses, kendali program dikembalikan ke baris instruksi berikutnya di luar _class_.|

### B. Python Implementation dari Method Call

- Berikut adalah contoh konkret bagaimana dua objek yang berbeda memanggil _methods_ yang sama namun menghasilkan output yang berbeda karena perbedaan _state_ internal masing-masing:

```
# Instantiation objek dengan data state awal berbeda
car_john = Car("sedan", 40)
car_emily = Car("suv")  # Default fuel = 0

# Objek car_john memanggil move_forward
car_john.move_forward(10)   # Output: Move 10 km

# Objek car_emily memanggil move_forward
car_emily.move_forward(10)  # Output: No fuel!
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen dan mahasiswa mendiskusikan kelemahan pada logika pengurangan bahan bakar (_fuel_) di dalam materi dasar. Jika kode hanya ditulis `self.fuel -= 1` setiap kali melaju tanpa memedulikan seberapa jauh jaraknya (_distance_), maka mobil yang melaju sejauh 1 km maupun 100.000 km hanya akan mengurangi kapasitas bahan bakar sebesar 1 unit. Hal ini secara matematis tidak masuk akal (_not making sense_).
- Untuk menyelesaikan masalah tersebut, dalam sesi diskusi kelas diusulkan penambahan atribut tingkat konsumsi bahan bakar (_fuel_consumption_) pada objek, misalnya rasio jarak tempuh per liter (seperti 1 liter untuk 7 km pada sedan, atau 1 liter untuk 10 km pada SUV).
- Dengan penyesuaian logika tersebut, pengurangan bahan bakar dapat dihitung secara dinamis dan proporsional berdasarkan parameter jarak tempuh yang dimasukkan saat memanggil _method_:

```
# Ilustrasi logika dinamis yang didiskusikan di kelas lisan
def move_forward_dynamic(self, distance):
    required_fuel = distance / self.fuel_consumption
    if self.fuel >= required_fuel:
        self.fuel -= required_fuel
        print(f"Move {distance} km successfully")
    else:
        print("No fuel!")
```



## Bab 5 Pewarisan Sifat (Basic Inheritance)

## 5.1 Definition dan Konsep Dasar dari Inheritance

### A. Conceptual Foundation

- _Inheritance_ merupakan sebuah mekanisme di mana suatu _class_ baru yang lebih spesifik (_child class_ atau _derived class_) dibangun berdasarkan _class_ umum yang sudah ada (_parent class_ atau _base class_).
- _Child class_ akan mewarisi semua properti, _attributes_, dan _behaviors_ (_methods_) yang didefinisikan oleh _parent class_, sehingga tidak perlu mendefinisikan ulang elemen-elemen dasar tersebut dari awal.
- Konsep ini merepresentasikan hubungan "is-a" (misalnya: _RegressionModel_ "is-a" _MachineLearningModel_, atau _Sedan_ "is-a" _Car_).

### B. Alasan Penggunaan dan Reusability

- **Code Organization**: Membantu mengelola struktur kode agar lebih terorganisasi dengan memisahkan fungsi yang bersifat umum (_generic_) ke dalam _parent class_, sementara fitur yang terspesialisasi disimpan di _child class_.
- **Code Reusability**: Menghindari penulisan ulang kode yang sama (_code duplication_) secara berulang pada beberapa _classes_ yang memiliki karakteristik dasar serupa.
- **Extensibility**: Mempermudah pengembangan dengan memperluas fungsionalitas (_extending functionality_) _parent class_ tanpa mengganggu atau memodifikasi kode dasar yang sudah berjalan stabil.

|Parameter Perbandingan|Tanpa Inheritance|Dengan Inheritance|
|:--|:--|:--|
|**Penulisan Kode**|Setiap tipe _class_ harus menuliskan seluruh _attributes_ dan _methods_ dasar secara berulang dari awal.|_Child class_ langsung mewarisi struktur umum dari _parent class_ secara otomatis.|
|**Spesialisasi Fitur**|Sulit membedakan fungsionalitas khusus karena semua logika digabung dalam satu atau beberapa berkas terpisah.|Fitur spesifik didefinisikan secara eksklusif hanya di dalam _child class_ yang membutuhkannya.|
|**Kemudahan Maintenance**|Perubahan pada logika dasar mengharuskan pembaruan kode di setiap _class_ secara individual.|Cukup memperbarui logika dasar di _parent class_, dan seluruh _child classes_ akan terupdate.|

#### [Wawasan Diskusi / Audio Insight]

- Dosen memberikan analogi industri otomotif untuk mempermudah pemahaman konsep _Inheritance_:
    - Daripada pengembang harus membuat _class_ `Sedan`, `SUV`, dan `PickUp` secara terpisah dari awal (yang akan mengakibatkan penulisan ulang atribut roda, mesin, tangki bahan bakar, serta metode rem dan gas di setiap kelas), pendekatan terbaik adalah membuat sebuah _parent class_ bernama `Car`.
    - _Class_ `Car` menetapkan seluruh atribut dan perilaku umum yang pasti dimiliki oleh semua jenis mobil.
    - Selanjutnya, _class_ `Sedan`, `SUV`, dan `PickUp` dideklarasikan sebagai _child classes_ yang mewarisi (_inherit_) fungsionalitas dari kelas `Car`, lalu menambahkan fungsionalitas spesifik mereka sendiri (misalnya, _PickUp_ menambahkan atribut kapasitas bak muatan).
- Terkait kedalaman pemahaman OOP untuk kebutuhan praktis, mahasiswa (Ibnu) menanyakan apakah kurikulum bootcamp juga akan membahas pilar OOP lanjutan seperti _Encapsulation_, _Abstraction_, atau _Polymorphism_:
    - Dosen menjelaskan bahwa fokus utama dalam program _AI Engineering_ sengaja dibatasi pada fondasi utama (seperti _Class_, _Object_, _Attributes_, _Methods_, dan _Basic Inheritance_) tanpa mendalami pilar rekayasa perangkat lunak lanjutan tersebut secara rumit.
    - Berdasarkan pengalaman profesional dosen selama 5 tahun bekerja sebagai _AI Engineer_, pilar-pilar lanjutan seperti _Polymorphism_ dan _Abstraction_ sangat jarang digunakan secara intensif dalam pekerjaan sehari-hari di bidang kecerdasan buatan. Oleh karena itu, pengembang disarankan untuk memperdalam konsep dasar yang relevan terlebih dahulu daripada kebingungan dengan teori rekayasa perangkat lunak yang terlalu mendalam.

---

## 5.2 Implementasi dan Struktur Sintaksis Inheritance

### A. Deklarasi Child Class dan Pemanggilan Constructor Parent

- Untuk mendefinisikan _child class_ yang mewarisi _parent class_, nama _parent class_ dituliskan di dalam tanda kurung langsung setelah penulisan nama _child class_.
- Di dalam _constructor_ (`__init__`) milik _child class_, pemanggilan metode `super().__init__()` wajib dilakukan untuk menginisialisasi atribut-atribut dasar yang dikelola oleh _parent class_.

### B. Sintaksis Dasar super()

- `super()` merujuk secara langsung ke _parent class_ (kelas di atasnya).
- Pemanggilan `super().__init__()` bertindak sebagai instruksi untuk menjalankan konstruktor _parent class_, yang memungkinkan _child class_ mendapatkan konfigurasi awal atribut dasar secara otomatis.

### C. Python Implementation dari Basic Inheritance

- Berikut adalah implementasi konkret pembuatan _parent class_ `MachineLearningModel` yang diwariskan kepada _child class_ `RegressionModel`:

```
class MachineLearningModel:
    def __init__(self, task, train_data, test_data):
        self.task = task
        self.train_data = train_data
        self.test_data = test_data

    def train(self):
        pass

    def test(self):
        pass

class RegressionModel(MachineLearningModel):
    def __init__(self, train_data, test_data):
        # Memanggil dan menginisialisasi atribut dasar dari parent class
        super().__init__(task="regression",
                         train_data=train_data,
                         test_data=test_data)

        # Mendefinisikan atribut spesifik milik RegressionModel
        self.error_function = "r2"

    # Mendefinisikan method spesifik milik RegressionModel
    def multicolinearity_test(self):
        pass
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan urutan pemanggilan di dalam blok kode `RegressionModel`:
    - Parameter `train_data` dan `test_data` yang diterima oleh _constructor_ `RegressionModel` langsung dioper ke atas (_parent_) menggunakan `super().__init__()` dengan argumen tambahan berupa nilai konstan `task="regression"`. Hal ini menjamin setiap kali sebuah objek `RegressionModel` dibuat, atribut `task` miliknya akan otomatis bernilai "regression" tanpa perlu diinput secara manual oleh pengguna.
    - Setelah `super().__init__()` selesai dijalankan untuk membuat fondasi dasar dari _parent class_, barulah pengembang menambahkan atribut spesifik di bawahnya seperti `self.error_function = "r2"` (yang merujuk pada metrik evaluasi _R-Squared_).
- Ketika sebuah objek dideklarasikan dari _child class_, objek tersebut memegang kendali penuh atas seluruh aset milik _parent class_ sekaligus aset spesifik miliknya sendiri:
    - Objek tersebut dapat memanggil atribut dan metode dari _parent class_ (seperti `.task`, `.train()`, dan `.test()`).
    - Objek tersebut juga dapat memanggil atribut dan metode spesifik miliknya sendiri (seperti `.error_function` dan `.multicolinearity_test()`).

---

## 5.3 Perbandingan Model Spesifik dalam Machine Learning

### A. Perluasan Fungsionalitas ke Model Klasifikasi

- Selain `RegressionModel`, _parent class_ `MachineLearningModel` yang sama juga dapat diwariskan ke model spesifik lain seperti `ClassificationModel`.
- Pendekatan ini menunjukkan bagaimana satu _parent class_ dapat memiliki beberapa _child classes_ yang berbeda dengan spesialisasi masing-masing, namun tetap berbagi basis fungsionalitas yang identik.

### B. Perbedaan Spesifikasi RegressionModel dan ClassificationModel

- Kedua _child classes_ tersebut memiliki perbedaan kebutuhan evaluasi (_error evaluation_) dan analisis diagnostik model yang disesuaikan dengan jenis tugasnya:

|Karakteristik|RegressionModel|ClassificationModel|
|:--|:--|:--|
|**Parent Class**|`MachineLearningModel`|`MachineLearningModel`|
|**Task Attribute Value**|`"regression"`|`"classification"`|
|**Specific Attribute**|`error_function = "r2"` (R-Squared)|`error_function = "accuracy"`|
|**Specific Method**|`multicolinearity_test()`|`confusion_matrix()`|
|**Shared Methods (Inherited)**|`train()`, `test()`|`train()`, `test()`|

### C. Python Implementation untuk Multiple Child Classes

- Di bawah ini adalah contoh perbandingan bagaimana kedua _child classes_ diturunkan dari satu basis kelas induk yang sama dan diinstansiasi menjadi objek-objek independen:

```
# Membuat objek dari RegressionModel
model_reg = RegressionModel(train_data="dataset_latih_reg", test_data="dataset_uji_reg")

# Mengakses inherited attribute dan method
print(model_reg.task)               # Output: regression
model_reg.train()

# Mengakses specific attribute dan method regression
print(model_reg.error_function)     # Output: r2
model_reg.multicolinearity_test()


# Membuat objek dari ClassificationModel (analogi implementasi)
class ClassificationModel(MachineLearningModel):
    def __init__(self, train_data, test_data):
        super().__init__(task="classification",
                         train_data=train_data,
                         test_data=test_data)
        self.error_function = "accuracy"

    def confusion_matrix(self):
        pass

model_clf = ClassificationModel(train_data="dataset_latih_clf", test_data="dataset_uji_clf")

# Mengakses inherited attribute dan method
print(model_clf.task)               # Output: classification
model_clf.train()

# Mengakses specific attribute dan method classification
print(model_clf.error_function)     # Output: accuracy
model_clf.confusion_matrix()
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen memberikan penjelasan mengapa pembagian _attributes_ dan _methods_ spesifik ini sangat krusial:
    - Atribut metrik evaluasi seperti `"r2"` (R-Squared) atau metode diagnostik seperti `multicolinearity_test()` hanya relevan dan bekerja pada domain analisis regresi numerik, sehingga tidak boleh ada pada kelas klasifikasi.
    - Sebaliknya, evaluasi menggunakan metrik akurasi (_accuracy_) dan representasi visual _confusion matrix_ via metode `confusion_matrix()` hanya relevan untuk domain klasifikasi data kategorikal, sehingga tidak boleh ada pada kelas regresi.
    - Dengan menggunakan paradigma _Inheritance_, pengembang berhasil mencegah terjadinya kesalahan struktural dan menjamin bahwa fungsionalitas yang tidak relevan tidak akan pernah bisa diakses atau dipanggil oleh objek yang salah, sekaligus tetap menjaga efisiensi penulisan kode dasar latihan (`train` dan `test`) yang seragam di memori.



## Bab 6 Latihan Praktis dan Pembahasan Teknis Python

## 6.1 Studi Kasus Class BankAccount

### A. Persyaratan Fungsionalitas Class BankAccount

- _Class_ bernama `BankAccount` dirancang untuk merepresentasikan rekening bank secara umum dengan fungsionalitas pengelolaan saldo dasar.
- Karakteristik dan elemen fungsionalitas dari _Class_ `BankAccount` dirinci pada tabel berikut:

|Elemen Class|Nama Elemen|Deskripsi Fungsional|
|:--|:--|:--|
|**Attributes**|`owner_name`|Menyimpan nama pemilik rekening (_data type_: _string_).|
||`balance`|Menyimpan nilai saldo saat ini (_data type_: _numeric_).|
|**Methods**|`__init__`|_Constructor_ untuk menginisialisasi nama pemilik dan saldo awal saat objek pertama kali dibangun.|
||`deposit(amount)`|Menambahkan nilai sejumlah `amount` ke dalam atribut saldo (`balance`).|
||`withdraw(amount)`|Mengurangi saldo sebesar `amount` jika saldo mencukupi. Jika saldo tidak cukup, proses penarikan digagalkan dan menampilkan pesan error.|

### B. Implementasi Code Python

- Berikut adalah implementasi lengkap untuk _Class_ `BankAccount` beserta skenario pengujian untuk dua objek secara independen di memori:

```
class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")

# Skenario Pengujian Unit
if __name__ == "__main__":
    # Inisialisasi Objek Rekening John
    john_account = BankAccount("John", 1000000)
    john_account.deposit(500000)
    john_account.withdraw(300000)
    print(f"Account: {john_account.owner_name}")
    print(f"Final balance: {john_account.balance}")

    print("-" * 40)

    # Inisialisasi Objek Rekening Emily
    emily_account = BankAccount("Emily", 200000)
    emily_account.deposit(100000)
    emily_account.withdraw(500000)
    print(f"Account: {emily_account.owner_name}")
    print(f"Final balance: {emily_account.balance}")
```

#### [Wawasan Diskusi / Audio Insight]

- Diskusi antara dosen dan mahasiswa (Stepen) menyoroti perbedaan mendasar antara _parameter_ dan _attribute_ di dalam metode _constructor_ `__init__`:
    - _Attributes_ didefinisikan secara internal dengan awalan kata kunci `self.` (seperti `self.owner_name` dan `self.balance`), yang menandakan bahwa variabel tersebut menempel secara eksklusif pada objek yang bersangkutan.
    - _Parameters_ (seperti `owner_name` dan `balance` pada baris deklarasi `def __init__(self, owner_name, balance)`) hanyalah variabel penampung sementara untuk menangkap argumen nilai yang dikirimkan oleh pengguna saat instansiasi dilakukan.
    - Untuk memudahkan penulisan, terdapat konvensi standar (_naming convention_) untuk menyamakan nama variabel _parameter_ dengan nama _attribute_, meskipun secara fungsional keduanya sangat berbeda.
- Dosen juga memberikan simulasi skenario desain _state lock_:
    - Jika suatu nilai _attribute_ ingin dikunci sebagai nilai bawaan (_default value_) yang tidak dapat disesuaikan saat pertama kali objek dibuat (misalnya, saldo awal/`balance` selalu bernilai 0), maka parameter `balance` tidak perlu dicantumkan dalam deklarasi _constructor_.
    - Implementasinya dapat ditulis secara langsung di dalam ruang lingkup _constructor_: `self.balance = 0`.
- Melalui studi kasus ini, dosen kembali menegaskan definisi formal: variabel yang menempel pada kelas disebut sebagai _attribute_, sementara fungsi yang didefinisikan di dalam kelas disebut sebagai _method_.
- Dari sisi pengujian eksekusi:
    - Objek pertama (`john_account`) diinisialisasi dengan saldo awal 1.000.000, ditambah setoran (`deposit`) 500.000 (menjadi 1.500.000), dan dikurangi penarikan (`withdraw`) 300.000, sehingga menghasilkan saldo akhir (_final balance_) sebesar 1.200.000.
    - Objek kedua (`emily_account`) diinisialisasi dengan saldo awal 200.000, ditambah setoran 100.000 (menjadi 300.000), namun gagal melakukan penarikan sebesar 500.000 karena saldo tidak mencukupi. Sistem menampilkan pesan `"Insufficient balance."` dan mempertahankan saldo akhir Emily tetap sebesar 300.000.
    - Mahasiswa lainnya (Rainer) membagikan pengalaman praktis tentang penambahan fungsi cetak (`print`) kustom di dalam logika internal `deposit` dan `withdraw` untuk mempermudah pelacakan kronologis (_state tracking_) aliran dana secara langsung dari dalam objek.

---

## 6.2 Mekanisme if **name** == '**main**'

### A. Fondasi Konseptual

- Struktur pemeriksaan `if __name__ == '__main__'` merupakan suatu konstruksi kontrol di Python untuk mendeteksi konteks pengeksekusian file _script_.
- Mekanisme ini mengevaluasi apakah file dijalankan secara langsung (_run directly_) oleh pengguna atau diimpor (_imported_) sebagai sebuah _module_ ke dalam berkas Python lain.
- Perilaku variabel internal `__name__` dirangkum dalam tabel di bawah ini:

|Kondisi Eksekusi File|Nilai Variabel `__name__`|Dampak terhadap Blok Kode Utama|
|:--|:--|:--|
|File dijalankan secara langsung (_run directly_) oleh pengguna di terminal.|`"__main__"`|Evaluasi bernilai `True`. Seluruh blok kode di bawah struktur `if` akan dieksekusi.|
|File diimpor (_imported_) sebagai _module_ oleh file _script_ lain.|Nama dari file _script_ itu sendiri (nama modul).|Evaluasi bernilai `False`. Blok kode di bawah struktur `if` akan dilewati (_skipped_).|

### B. Implementasi Code Python

- Berikut adalah visualisasi implementasi pendeteksian variabel internal `__name__` untuk menunjukkan perilakunya ketika dijalankan secara langsung:

```
# Berkas: exercise.py

class BankAccount:
    pass

# Melakukan pengecekan nilai dari variabel internal __name__
print(f"Isi dari variabel internal __name__ adalah: {__name__}")

if __name__ == "__main__":
    print("Kode eksekusi utama berjalan di sini.")
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan cara kerja di balik layar variabel internal `__name__` yang diatur secara otomatis oleh mesin _interpreter_ Python.
- Ketika pengguna menjalankan program secara langsung dari terminal dengan mengetikkan perintah `python3 exercise.py`, variabel `__name__` akan diisi secara otomatis dengan nilai string `"__main__"`. Kondisi pengecekan menjadi terpenuhi sehingga bagian pengujian program dijalankan.
- Apabila kita membuat file _script_ baru (misalnya `another_file.py`) dan menuliskan baris kode `import exercise`, proses impor tersebut akan memicu pemuatan isi modul. Namun, karena file `exercise.py` tidak dijalankan secara langsung, nilai variabel `__name__` di dalamnya akan otomatis berubah menjadi string `"exercise"`. Walhasil, seluruh blok kode pengujian di bawah pemeriksaan `if __name__ == '__main__'` tidak akan ikut terpanggil di file baru tersebut.
- Melalui teknik ini, _developer_ dapat dengan aman menyatukan pendefinisian cetak biru (_blueprint_) kelas, metode, atau fungsi di dalam satu file bersama dengan skenario kode pengujian mandiri (_unit testing_) tanpa khawatir kode pengujian tersebut mengganggu proses pemuatan berkas saat dijadikan modul eksternal.



## Untitled





---


# Module 1 Session 8 Phyton & Modular Programming


## Bab 1 Pengenalan Pemrograman Modular (Introduction to Modular Programming)


### A. Fondasi Konseptual

- **Definisi Pemrograman Modular**: Pendekatan pemrograman yang memecah atau membagi program besar menjadi komponen-komponen atau modul-modul kecil yang dapat digunakan kembali (_reusable components_). Setiap file Python (`.py`) dalam paradigma ini diidentifikasi sebagai satu modul terpisah.
- **Definisi Kode Monolitik**: Pendekatan pemrograman tradisional di mana seluruh fungsi, variabel, dan logika program digabungkan ke dalam satu file tunggal (_single file_).
- **Prinsip Dasar**: Pemrograman modular bertujuan untuk mengelola kompleksitas sistem (_complexity_) seiring bertambahnya skala proyek dan volume kode (_line of code_) yang ditulis.

#### [Wawasan Diskusi / Audio Insight]

- Pada proyek riil, file monolitik sering kali bertumbuh secara organik. Ketika sebuah fitur baru dikembangkan, developer cenderung langsung menambahkan fungsi baru ke dalam file utama yang sama. Pada titik tertentu, sistem ini akan mengalami masalah skalabilitas (_scale up_) yang signifikan. Meskipun secara fungsional kode tersebut tetap berjalan (_works_), kode tersebut akan menjadi terlalu kompleks dan tidak terstruktur.

---

### B. Tantangan Kode Monolitik (Monolithic Code Challenges)

Ketika program bertumbuh menjadi lebih besar (misalnya mencapai 500 baris kode atau lebih), terdapat lima tantangan utama yang muncul akibat penggunaan kode monolitik:

1. **Sulit Dibaca (_Difficult to Read_)**: Penumpukan seluruh fungsi dan logika di dalam satu file menyebabkan bagian kode tertentu tertimbun, sehingga sulit untuk dicari dan dipahami alurnya.
2. **Sulit Dipelihara (_Difficult to Maintain_)**: Kode monolitik menjadi sangat rapuh seiring waktu. Satu perubahan kecil atau kesalahan ketik (_typo_) pada satu bagian dapat merusak bagian lain yang tidak berhubungan (_break unrelated features_).
3. **Sulit Didebug (_Difficult to Debug_)**: Proses pelacakan sumber kesalahan (_error_) menjadi sangat rumit karena seluruh jalannya program berada di dalam satu ruang lingkup file yang sama.
4. **Sulit Digunakan Kembali (_Difficult to Reuse_)**: Fungsi yang didefinisikan dalam kode monolitik tidak dapat dipanggil oleh file lain secara langsung. Untuk menggunakannya kembali, developer terpaksa melakukan salin-tempel (_copy-paste_) kode secara manual.
5. **Sulit Berkolaborasi (_Difficult to Collaborate_)**: Ketika beberapa developer bekerja pada file monolitik yang sama, proses integrasi kode akan sering mengalami konflik penggabungan (_merge conflict_) di repositori Git/GitHub.

|Karakteristik|Kode Monolitik (_Monolithic Code_)|Pemrograman Modular (_Modular Programming_)|
|:--|:--|:--|
|**Struktur Berkas**|Terpusat dalam satu file tunggal (_single file_)|Terbagi ke dalam beberapa file modul kecil|
|**Keterbacaan**|Rendah, logika penting tertimbun dalam ratusan baris|Tinggi, kode bersih (_clean_) dan ringkas (_concise_)|
|**Dampak Kesalahan**|Tinggi, satu kesalahan dapat merusak seluruh sistem (_break_)|Terisolasi pada modul yang bersangkutan saja|
|**Kemudahan Pengujian**|Sulit karena ketergantungan antar-fungsi sangat erat|Mudah karena pengujian unit (_unit testing_) dapat dilakukan secara terisolasi|
|**Kolaborasi Tim**|Sering memicu _merge conflict_ yang sulit diresolusi|Lebih lancar melalui pembagian tanggung jawab modul (_clear responsibility_)|

#### [Wawasan Diskusi / Audio Insight]

- **Masalah Pencarian Kode**: Dosen mencontohkan bahwa pada kode monolitik, logika pembersihan teks (_text cleaning logic_) dapat dengan mudah "terkubur" di antara ratusan baris kode lainnya, membuat developer kesulitan menemukannya kembali saat dibutuhkan.
- **Kerentanan Berantai**: Satu _typo_ kecil pada fungsi di file monolitik dapat menghentikan jalannya seluruh program (_break the whole file_) secara total.
- **Mekanisme Kolaborasi Tim**: Jika proyek dikelola secara modular, pembagian tugas menjadi lebih jelas. Sebagai contoh, developer A dapat fokus mengerjakan tahap _preprocessing_, developer B pada _model training_, dan developer C pada pemuatan data (_load results_). Setiap developer bekerja pada file modul terpisah dan membuat cabang (_branch_) Git masing-masing. Saat dilakukan penggabungan (_merge_), sistem Git akan mengenalinya sebagai file baru atau perubahan terpisah, sehingga dapat melakukan penggabungan otomatis (_auto-merge_) tanpa memicu konflik terus-menerus. Sebaliknya, jika bekerja pada satu file yang sama, baris-baris kode akan saling tumpang tindih dan memicu _conflict_ yang harus diresolusi manual (_resolve conflict_) secara berulang.

---

### C. Batasan dan Evaluasi Kebutuhan Modularisasi

Meskipun pemrograman modular menawarkan banyak keuntungan, penerapannya harus disesuaikan dengan kebutuhan proyek nyata.

- **Efek Samping Kompleksitas**: Modularisasi pada dasarnya menambahkan sedikit kompleksitas (_complexity_) pada struktur proyek (misalnya dalam mengelola jalur file, impor, dan hubungan antar-modul) demi mendapatkan keteraturan.
- **Prinsip Evaluasi**: Jika program yang dibangun sangat sederhana, berukuran kecil, dan hanya berupa skrip sekali pakai, pemrograman modular tidak perlu dipaksakan. Memaksakan modularisasi pada kasus yang tidak tepat justru akan menambah kompleksitas yang tidak perlu (_unnecessary complexity_).

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan pentingnya melihat kondisi nyata sebelum memutuskan melakukan modularisasi. Modularisasi adalah investasi struktural. Jika hanya membuat satu file kecil sederhana, pendekatan satu file (monolitik) justru lebih efisien karena menghindari kompleksitas berlebih yang tidak mendatangkan manfaat nyata.



## Bab 2 Modul dalam Python (Module in Python)


### A. Fondasi Konseptual

- **Definisi Modul**: Sebuah file Python tunggal berekstensi `.py` yang berisi sekumpulan kode terorganisasi dan dapat digunakan kembali (_reusable code_). Modul dapat berisi definisi fungsi (_functions_), kelas (_classes_), maupun variabel.
- **Tujuan Pembuatan Modul**: Memisahkan logika program yang sejenis ke dalam file terpisah guna meningkatkan kerapian, memudahkan proses pemeliharaan (_maintenance_), mempermudah proses pencarian kesalahan (_debugging_), serta meningkatkan reusabilitas kode (_code reusability_).
- **Struktur Berkas Sederhana**:
    - `calculator.py`: Berkas modul yang menyimpan fungsi-fungsi utilitas kalkulasi.
    - `main.py`: Berkas skrip utama yang mengimpor dan memanfaatkan utilitas dari `calculator.py`.

#### [Wawasan Diskusi / Audio Insight]

- **Fleksibilitas Isi Modul**: Berdasarkan diskusi kelas, dosen mengonfirmasi bahwa isi dari sebuah modul Python tidak terbatas pada fungsi (_functions_) saja. Modul juga dapat diisi dengan pendefinisian kelas (_classes_) atau variabel sesuai kebutuhan rancangan program.
- **Kemudahan Pelacakan Masalah**: Dosen menjelaskan bahwa pengorganisasian kode ke dalam modul sangat membantu proses pemecahan masalah (_debugging_). Jika terjadi kesalahan kalkulasi, developer dapat langsung menuju ke file `calculator.py` tanpa perlu memeriksa ratusan baris kode lainnya di berkas utama.

---

### B. Metode Pengimporan Modul (Importing Module)

Ada dua metode utama yang digunakan untuk mengimpor modul di Python, masing-masing memiliki karakteristik penulisan (_syntax_) dan pengelolaan ruang nama (_namespace_) yang berbeda:

1. **Metode Mengimpor Seluruh Modul (`import module_name`)**
    
    - **Karakteristik**: Mengimpor keseluruhan modul ke dalam berkas aktif.
    - **Cara Pemanggilan**: Setiap pemanggilan fungsi atau komponen di dalam modul wajib diawali dengan nama modul sebagai _namespace_ (contoh: `module_name.function_name()`).
    - **Dampak Kelalaian Namespace**: Jika nama modul tidak disertakan saat pemanggilan fungsi, Python tidak akan mengenali fungsi tersebut dan akan memicu kesalahan sistem (_NameError_).
2. **Metode Mengimpor Komponen Spesifik (`from module_name import function_name`)**
    
    - **Karakteristik**: Hanya mengimpor komponen atau fungsi tertentu yang dideklarasikan secara eksplisit ke dalam berkas aktif. Komponen lain yang tidak disebutkan di baris impor tidak akan dapat diakses.
    - **Cara Pemanggilan**: Fungsi dapat dipanggil secara langsung menggunakan namanya tanpa perlu menambahkan prefiks nama modul di depannya (contoh: `function_name()`).
    - **Kelebihan**: Membuat penulisan kode pada berkas utama terasa lebih bersih, ringkas, dan efisien (_clean and concise_).

|Metode Impor|Sintaksis Impor|Contoh Pemanggilan Fungsi|Pengaruh terhadap Namespace|Reusabilitas|
|:--|:--|:--|:--|:--|
|**Mengimpor Seluruh Modul**|`import calculator`|`calculator.add(2, 3)`|Melindungi _namespace_ agar tidak terjadi bentrokan nama variabel atau fungsi|Tinggi, mengimpor seluruh fungsionalitas modul sekaligus|
|**Mengimpor Komponen Spesifik**|`from calculator import add`|`add(2, 3)`|Memasukkan komponen langsung ke _namespace_ lokal berkas aktif|Terbatas, hanya mengimpor komponen yang dideklarasikan saja|

#### [Wawasan Diskusi / Audio Insight]

- **Dampak Kesalahan Tanpa Namespace**: Dosen mendemonstrasikan secara langsung di kelas kesalahan yang terjadi ketika developer menggunakan `import calculator` tetapi memanggil fungsi secara langsung seperti `add(2, 3)`. Python akan mengeluarkan pesan _error_ "NameError: name 'add' is not defined" karena Python kehilangan rujukan lokasi definisi fungsi tersebut. Hal ini membuktikan pentingnya pemahaman _namespace_ dalam modul.
- **Alur Pengimporan dalam Proyek**: Dosen memberikan simulasi penulisan modul matematika alternatif bernama `math_utils.py` yang berisi fungsi `add(a, b)` dan `multiply(a, b)`. Dengan menggunakan `from math_utils import add, multiply`, kode di berkas utama menjadi jauh lebih terbaca karena fungsi-fungsi tersebut langsung dikenali oleh berkas pengeksekusi tanpa embel-embel nama file di depannya.

---

### C. Demonstrasi dan Implementasi Kode

Berikut adalah contoh struktur kode bersih untuk implementasi modul pertama sesuai dengan standar latihan di kelas:

1. **Pembuatan Berkas Modul (`calculator.py`)**

```
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

2. **Implementasi pada Berkas Utama dengan Metode Impor Utuh (`main.py`)**

```
import calculator

result_add = calculator.add(2, 3)
result_sub = calculator.subtract(5, 2)

print(result_add)
print(result_sub)
```

3. **Implementasi pada Berkas Utama dengan Metode Impor Spesifik (`main.py`)**

```
from calculator import add, subtract

result_add = add(2, 3)
result_sub = subtract(5, 2)

print(result_add)
print(result_sub)
```

#### [Wawasan Diskusi / Audio Insight]

- **Pilihan Pendekatan Impor**: Kedua pendekatan di atas sepenuhnya valid dan bekerja dengan baik (_works_). Keputusan pemilihan metode impor sangat bergantung pada preferensi kerapian penulisan kode serta kebutuhan perlindungan ruang nama (_namespace_) dari variabel lain yang ada pada proyek Anda.



## Bab 3 Mengorganisasi Proyek (Organizing a Project)



### A. Fondasi Konseptual

- **Hierarki Proyek Python**: Pengorganisasian kode dalam Python mengikuti struktur hierarki tiga tingkat guna memisahkan ruang lingkup kerja dan tanggung jawab kode secara terstruktur.
- **Tiga Komponen Utama**:
    - **Project**: Keseluruhan aplikasi atau pustaka (_library_) secara utuh dan lengkap yang sedang bangun.
    - **Package**: Direktori atau folder fisik yang digunakan untuk mengelompokkan beberapa modul Python yang memiliki keterkaitan fungsional.
    - **Module**: Satu berkas Python tunggal (berkas berekstensi `.py`) yang berisi kode program berupa kelas (_class_), fungsi (_function_), atau variabel yang dapat digunakan kembali.

|Istilah|Karakteristik Utama|Representasi Fisik|
|:--|:--|:--|
|**Project**|Aplikasi lengkap atau pustaka (_library_) secara menyeluruh|Folder utama proyek (_root directory_)|
|**Package**|Folder pengelompok modul-modul yang saling berhubungan|Folder khusus berisi file `__init__.py`|
|**Module**|Berkas kode tunggal berisi fungsi atau kelas siap pakai|Berkas berekstensi `.py`|

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa pemahaman hierarki ini sangat penting ketika proyek bertumbuh dari skrip tunggal menjadi aplikasi skala besar. Secara sederhana, modul adalah berkas individu, package adalah folder yang membungkus berkas-berkas tersebut, dan project adalah seluruh ekosistem aplikasi tersebut. Modul tidak hanya terbatas pada pendefinisian fungsi (_functions_), melainkan dapat berisi kelas (_classes_) dan variabel global.

---

### B. Studi Kasus Penerapan: Customer Churn Prediction

- **Prinsip Pembagian Tanggung Jawab (_Separation of Responsibility_)**: Dalam merancang proyek pemrograman modular, setiap modul wajib didefinisikan untuk memegang satu tanggung jawab spesifik yang jelas (_clear responsibility_). Pembuatan modul tidak boleh dilakukan secara acak (_random_).
    
- **Alur Kerja Logis Proyek**:
    
    1. **Load Data**: Memuat dataset mentah dari sumber penyimpanan.
    2. **Preprocessing Data**: Melakukan pembersihan data (_cleaning_) dan transformasi.
    3. **Model Training**: Melatih model kecerdasan buatan (_AI model_) menggunakan data hasil pemrosesan.
    4. **Model Evaluation**: Mengevaluasi performa model menggunakan metrik pengujian.
    5. **Orchestration**: Mengatur jalannya seluruh proses dari awal hingga akhir melalui berkas utama.
- **Pembagian Tugas dan Berkas Modul**:
    

|Nama Berkas Modul|Tanggung Jawab Spesifik (_Responsibility_)|Fitur / Fungsionalitas Utama|
|:--|:--|:--|
|**`data.py`**|Memuat data (_load the data_)|Fungsi untuk membaca dataset mentah dari penyimpanan lokal atau _cloud_|
|**`preprocessing.py`**|Pra-pemrosesan data (_preprocessing data_)|Menangani nilai kosong (_missing values_), menghapus data duplikat (_duplicate removal_), dan penyandian fitur (_encoding features_)|
|**`model.py`**|Pelatihan model (_training the model_)|Mendefinisikan algoritma AI dan melatih model di atas data bersih|
|**`evaluate.py`**|Evaluasi model (_evaluate the model_)|Menghitung performa model menggunakan metrik evaluasi|
|**`main.py`**|Mengorkestrasi sistem (_orchestrate_)|Mengimpor seluruh modul fungsional dan menjalankan alur kerja proyek secara teratur|

#### [Wawasan Diskusi / Audio Insight]

- **Masalah Pembuatan Modul Secara Acak**: Dosen mengingatkan agar pengembang tidak membagi modul secara sembarangan (seperti membuat `modul_A.py` atau `modul_B.py` tanpa pembagian fungsi yang jelas). Setiap modul harus memiliki nama yang mendeskripsikan tanggung jawabnya agar kode mudah dipelihara (_maintainable_).
- **Efisiensi Kolaborasi dan Pemeliharaan**: Jika terjadi _error_ pada tahap pembersihan data duplikat, pengembang dapat langsung menuju berkas `preprocessing.py` tanpa mengganggu berkas `model.py` atau `main.py`. Pola modular ini juga memfasilitasi kerja paralel dalam tim. Misalnya, Developer A bekerja pada `preprocessing.py`, Developer B pada `model.py`, dan Developer C pada `evaluate.py`. Karena bekerja pada file terpisah, mereka dapat membuat cabang (_branch_) Git masing-masing, meminimalkan terjadinya konflik penggabungan (_merge conflict_), dan memungkinkan Git melakukan penggabungan otomatis (_auto-merge_).
- **Kondisi Berkas Utama**: Setelah modularisasi diterapkan, berkas `main.py` menjadi sangat bersih, ringkas (_concise_), dan mudah dibaca karena hanya berisi panggilan tingkat tinggi (_high-level calls_) terhadap fungsi-fungsi yang diimpor dari modul lain.

---

### C. Teknik Penggunaan Alias dalam Impor

- **Definisi Alias**: Mekanisme mempersingkat nama modul yang diimpor menggunakan kata kunci `as`.
- **Manfaat Utama**:
    - Mempersingkat penulisan kode saat memanggil fungsi dari modul dengan nama yang panjang.
    - Menghindari konflik ruang nama (_namespace conflict_) di dalam berkas aktif.
- **Konstruksi Konflik Ruang Nama (_Namespace Conflict_)**: Konflik ini terjadi apabila sebuah nama variabel yang dideklarasikan di dalam file utama memiliki nama yang persis sama dengan nama modul yang diimpor. Python akan mengalami tumpang tindih nama sehingga menyebabkan kesalahan eksekusi program (_NameError_ atau kegagalan pemanggilan fungsi).

Berikut adalah contoh implementasi pengorganisasian proyek dan penggunaan alias secara aman dalam Python:

```
# data.py
def load_data():
    print("Loading dataset from source...")

# preprocessing.py
def clean_data():
    print("Handling missing values and removing duplicates...")

# model.py
def train_model():
    print("Training the AI model...")

# main.py
import data as dt
import preprocessing as pp
import model as model_modul  # Menggunakan alias untuk menghindari namespace conflict

# Deklarasi variabel lokal yang memiliki nama sama dengan nama modul asli
model = "Random Forest Classifier"  # Variabel ini tidak akan bentrok karena modul 'model' diimpor sebagai 'model_modul'

# Eksekusi fungsi menggunakan alias
dt.load_data()
pp.clean_data()
model_modul.train_model()

print(f"Active local variable 'model': {model}")
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen mencontohkan bahwa pada berkas `main.py` di atas, variabel `model` dideklarasikan untuk menampung teks `"Random Forest Classifier"`. Jika modul `model.py` diimpor secara biasa dengan perintah `import model`, maka pemanggilan fungsi di bawahnya seperti `model.train()` akan memicu _error_ karena interpreter Python menganggap `model` sebagai variabel bertipe string, bukan sebagai modul. Dengan menggunakan alias `import model as model_modul`, ruang nama modul dialihkan ke `model_modul`, sehingga variabel lokal `model` dapat digunakan secara bersamaan tanpa memicu konflik ruang nama (_namespace conflict_).



## Bab 4 Penggunaan Kondisional

# Penggunaan Kondisional `__name__ == "__main__"`

### A. Fondasi Konseptual

- **Masalah Eksekusi Otomatis**: Saat sebuah file Python diimpor sebagai modul oleh file lain, interpreter Python akan mengeksekusi seluruh baris kode di dalam modul tersebut dari atas ke bawah. Jika di dalam file modul tersebut terdapat kode pengujian, deklarasi variabel uji coba, atau fungsi cetak (_print statement_), baris-baris tersebut akan ikut dijalankan secara otomatis saat proses impor dilakukan. Hal ini menghasilkan eksekusi yang tidak diinginkan pada berkas utama (_main program_).
- **Definisi `__name__ == "__main__"`**: Konstruksi kondisional ini bertindak sebagai pelindung eksekusi (_name guard_) yang mengontrol aliran eksekusi berkas Python. Kondisional ini memberikan instruksi kepada Python untuk hanya mengeksekusi blok kode di bawahnya apabila berkas tersebut dijalankan secara langsung sebagai proses utama (_main process_ atau _main execution_) melalui terminal.
- **Karakteristik Perilaku**: Jika berkas tersebut hanya diimpor ke berkas lain sebagai modul pustaka, pemeriksaan kondisional ini akan bernilai salah (_False_) dan blok kode di dalamnya akan diabaikan sehingga tidak ikut dieksekusi.

---

### B. Cara Kerja dan Mekanisme Variabel `__name__`

- **Mekanisme Variabel Bawaan**: Python memiliki variabel khusus bawaan bernama `__name__` yang secara otomatis didefinisikan untuk setiap berkas script yang dijalankan.
- **Nilai Variabel Berdasarkan Konteks Eksekusi**:
    - **Eksekusi Langsung**: Saat sebuah file Python dijalankan secara langsung dari terminal, variabel `__name__` di dalam file tersebut akan diisi dengan string `"__main__"`. Nilai ini bersifat mutlak untuk berkas yang bertindak sebagai titik masuk eksekusi (_entry point_).
    - **Proses Impor Modul**: Saat file tersebut diimpor sebagai modul ke dalam file lain, variabel `__name__` di dalam file modul tersebut tidak akan bernilai `"__main__"`, melainkan berubah nilai secara otomatis menjadi nama asli dari modul itu sendiri (misalnya `"calculator"`).

|Skenario Eksekusi|Nilai Variabel `__name__` di Berkas Aktif|Status Evaluasi `__name__ == "__main__"`|Dampak terhadap Blok Kode Pelindung|
|:--|:--|:--|:--|
|**Berkas Utama dijalankan langsung**|`"__main__"`|Benar (_True_)|Blok kode di dalam kondisional dieksekusi|
|**Berkas Modul diimpor ke berkas lain**|Nama modul tersebut (misalnya `"calculator"`)|Salah (_False_)|Blok kode di dalam kondisional dilewati/diabaikan|

#### [Wawasan Diskusi / Audio Insight]

- **Pembuktian Nilai Variabel**: Melalui sesi interaksi tanya jawab antara mahasiswa (Anwar) dan dosen, dibuktikan secara langsung isi dari variabel `__name__` menggunakan perintah cetak (_print statement_). Saat berkas utama dijalankan langsung, hasil cetak menunjukkan variabel `__name__` di file utama bernilai `"__main__"`. Namun, ketika modul pendukung diimpor, variabel `__name__` di dalam file modul pendukung tersebut tercetak sebagai nama modul itu sendiri, bukan `"__main__"`. Perbedaan nilai inilah yang membuat evaluasi logika kondisional berhasil memisahkan proses impor dan eksekusi langsung secara akurat.
- **Independensi Nama Berkas Utama**: Dalam diskusi kelas dengan mahasiswa (Stepen), dosen menguji coba mengganti nama berkas utama dari `main.py` menjadi `main_code.py` lalu menjalankannya langsung. Hasilnya menunjukkan bahwa variabel `__name__` pada berkas utama yang dieksekusi tetap bernilai `"__main__"`. Nilai `"__main__"` bersifat konseptual untuk menandai proses utama dan sama sekali tidak bergantung pada nama fisik file script di dalam sistem penyimpanan komputer Anda.

---

### C. Manfaat Menggunakan Name Guard

- **Mencegah Eksekusi yang Tidak Diinginkan (_Prevent Unwanted Execution_)**: Menghentikan jalannya kode eksekusi utama, kode demonstrasi, pengujian, atau fungsi cetak secara otomatis ketika file tersebut diimpor oleh file program lain.
- **Meningkatkan Penggunaan Kembali Kode (_Boost Code Reusability_)**: Memungkinkan satu file Python tunggal berfungsi ganda secara fleksibel, yaitu sebagai pustaka modul yang menyediakan fungsi-fungsi untuk diimpor berkas lain, sekaligus sebagai script mandiri (_independent script_) yang memiliki fungsi eksekusi mandiri ketika dijalankan langsung.
- **Pengujian Cepat dan Terisolasi (_Easy Quick Testing / Isolated Unit Test_)**: Memudahkan developer dalam menuliskan dan menjalankan kode pengujian unit khusus secara langsung di bagian bawah file modul guna memastikan fungsi-fungsi di dalamnya bekerja dengan benar, tanpa khawatir kode tes tersebut akan mengganggu atau mengotori output dari berkas lain yang mengimpor modul tersebut.

---

### D. Demonstrasi Kasus dan Implementasi Kode

Berikut adalah contoh perbandingan penulisan modul kalkulator tanpa pelindung (_no guard_) dengan modul kalkulator yang dilengkapi pelindung (_name guard_) beserta cara kerjanya saat diimpor oleh file utama:

```
# calculator_no_guard.py
# File modul tanpa pelindung eksekusi

def add(a, b):
    return a + b

# Baris eksekusi uji coba langsung di bawah ini akan selalu jalan otomatis saat diimpor
result = add(1, 2)
print(f"Hasil penjumlahan di calculator_no_guard: {result}")


# calculator_with_guard.py
# File modul dengan pelindung eksekusi (name guard)

def add(a, b):
    return a + b

# Blok kode ini diproteksi menggunakan kondisional __name__ == "__main__"
if __name__ == "__main__":
    result = add(1, 2)
    print(f"Eksekusi uji coba mandiri di calculator_with_guard: {result}")


# main.py
# File utama yang mengimpor kedua modul di atas

print("--- Memulai Proses Impor Modul Tanpa Pelindung ---")
import calculator_no_guard  # Output dari baris uji coba di calculator_no_guard akan langsung tercetak otomatis di terminal

print("--- Memulai Proses Impor Modul Dengan Pelindung ---")
import calculator_with_guard  # Output uji coba di calculator_with_guard tidak akan tercetak karena diproteksi guard

# Panggilan fungsi dari modul terproteksi tetap berjalan dengan normal
hasil_aman = calculator_with_guard.add(5, 7)
print(f"Hasil panggilan fungsi add secara aman: {hasil_aman}")
```

#### [Wawasan Diskusi / Audio Insight]

- **Masalah Kesalahpahaman Impor**: Dalam diskusi kelas, mahasiswa (Stepen) sempat mengalami kebingungan karena berasumsi bahwa penggunaan blok kondisional `if __name__ == "__main__":` akan menghalangi fungsi-fungsi penting di dalam modul untuk diimpor. Dosen menegaskan bahwa pemahaman tersebut keliru. Blok pelindung eksekusi hanya menyaring dan menghentikan baris perintah eksekusi langsung (seperti pembuatan variabel hasil dan fungsi cetak demonstrasi di baris terbawah modul). Sementara itu, definisi fungsi utama (seperti `def add(a, b)`) tetap terdaftar dengan sempurna di dalam memori dan dapat diimpor serta digunakan oleh berkas eksternal kapan saja tanpa hambatan.
- **Readability vs Penyusunan Baris Kode**: Saat membedah tugas kelompok, dosen menyarankan agar penulisan variabel-variabel penampung hasil fungsi di dalam fungsi pelaporan (_report function_) dideklarasikan secara runtut dan terpisah daripada menyatukannya ke dalam satu baris panjang (_single line assignment_). Mengisolasi variabel penampung di baris-baris terpisah sebelum mencetaknya sangat meningkatkan keterbacaan kode (_readability_) dan mempermudah pelacakan alur data (_data tracing_) saat terjadi kesalahan.



## Bab 5 Package dalam Python (Packages in Python)


### A. Fondasi Konseptual

- **Definisi Package**: Folder atau direktori terorganisasi di dalam Python yang membungkus beberapa modul yang saling berkaitan agar mudah dikelola ketika skala proyek bertumbuh besar.
- **Pembeda Utama (Folder Biasa vs Package)**: Folder biasa hanya bertindak sebagai tempat penyimpanan fisik berkas di dalam sistem operasi. Sementara itu, Package adalah direktori khusus yang dikenali oleh interpreter Python sebagai pustaka (_library_) karena di dalamnya terdapat berkas inisialisasi bernama `__init__.py`.
- **File Inisialisasi `__init__.py`**: Berkas khusus (dapat berupa berkas kosong) yang wajib diletakkan di dalam direktori folder untuk memberi tahu Python bahwa folder tersebut merupakan sebuah package dan harus diperlakukan sebagai package. Jika folder tidak memiliki berkas `__init__.py`, maka folder tersebut hanya akan dianggap sebagai folder biasa dan proses impor fungsionalitas di tingkat folder akan gagal.

|Aspek Karakteristik|Folder Biasa|Package dalam Python|
|:--|:--|:--|
|**Keberadaan `__init__.py`**|Tidak memiliki berkas `__init__.py`|Wajib memiliki berkas `__init__.py`|
|**Pengenalan oleh Python**|Hanya dianggap sebagai direktori penyimpanan fisik biasa|Dikenali sebagai satu kesatuan package atau pustaka (_library_)|
|**Kemudahan Impor**|Memerlukan rute impor panjang (_Deep Import_)|Mendukung penyederhanaan impor (_Shallow Import_)|
|**Ekspos Fungsi**|Modul di dalamnya harus diakses secara manual dan individual|Fungsi terpilih dapat diekspos langsung di level folder utama|

#### [Wawasan Diskusi / Audio Insight]

- Di dalam kelas, dosen berdiskusi dengan Brian mengenai komponen penyusun direktori `preprocessing/`. Direktori tersebut membungkus modul-modul seperti `clean.py`, `encoder.py`, dan `standardizer.py`. Dosen memperjelas bahwa berkas `__init__.py` bukanlah modul biasa, melainkan file konfigurasi inisialisasi khusus yang mengendalikan perilaku pengimporan package tersebut.
- Stepen menanyakan kemungkinan pembuatan package bertingkat atau di dalam package terdapat package lain (_nested packages_). Dosen memverifikasi bahwa struktur bertingkat (_nested_) sangat mungkin dibuat di Python. Namun, pada implementasi proyek riil (_real world cases_), pembuatan folder yang terlalu bertingkat-tingkat umumnya dihindari demi menjaga kesederhanaan dan mencegah kompleksitas navigasi struktur proyek yang berlebihan.

---

### B. Perbedaan Metode Impor pada Package (_Deep Import_ vs _Shallow Import_)

- **Deep Import**: Metode pengimporan di mana pengembang harus merujuk nama modul dan rute jalurnya secara lengkap hingga ke tingkat berkas modul paling dalam untuk memanggil fungsi tertentu.
    - _Sintaksis_: `from package.module import function`
    - _Karakteristik_: Mengharuskan pengguna package memahami detail internal struktur folder dan nama berkas modul yang spesifik.
- **Shallow Import**: Metode pengimporan praktis langsung di tingkat folder package utama tanpa perlu merujuk nama berkas modul secara mendalam.
    - _Sintaksis_: `from package import function`
    - _Karakteristik_: Struktur internal didelegasikan ke berkas `__init__.py` yang bertugas memetakan dan mengekspos (_expose_) fungsi-fungsi terpilih ke permukaan package agar langsung dapat digunakan oleh berkas utama.

|Karakteristik Perbandingan|Deep Import|Shallow Import|
|:--|:--|:--|
|**Konstruksi Impor**|Rute impor panjang hingga ke file `.py` spesifik|Rute impor pendek langsung ke folder package utama|
|**Pengetahuan Struktur**|Pengembang wajib tahu nama berkas modul internal secara detail|Pengembang cukup memanggil langsung dari nama package utama|
|**Kerapian Kode**|Lebih panjang dan kompleks jika struktur folder sangat dalam|Lebih bersih, ringkas (_concise_), dan mudah dibaca|
|**Ketergantungan `__init__.py`**|Tetap berjalan meskipun berkas `__init__.py` kosong|Wajib mengonfigurasi ekspos fungsi di dalam `__init__.py`|

#### [Wawasan Diskusi / Audio Insight]

- **Konsekuensi Tanpa Inisialisasi (_Without Init Exposing_)**: Dosen mendemonstrasikan bahwa jika baris ekspor di dalam berkas `__init__.py` dimatikan (misalnya dikomentari), maka perintah impor ringkas (_Shallow Import_) akan memicu kesalahan sistem berupa `NameError` atau `cannot import name 'clean_text' from 'utils'`. Tanpa deklarasi eksplisit di dalam `__init__.py`, Python akan selalu memaksa pengembang menggunakan jalur impor panjang (_longer form_) yang berbelit-belit.
- **Efisiensi Kerja Tim Kolaboratif**: Pembagian modul di dalam package (seperti memisahkan fungsi ke dalam `clean.py`, `encoder.py`, dan `standardizer.py`) sangat mempermudah kolaborasi paralel dalam tim. Dosen mencontohkan bahwa Developer A (Brian) dapat fokus mengerjakan modul pembersihan teks (`clean.py`), Developer B (Evo) pada modul penyandian (`encoder.py`), dan Developer C (Anwar) pada modul penskalaan data (`standardizer.py`). Meskipun dikerjakan terpisah oleh orang yang berbeda, pengguna akhir (_end-user_) dari package tersebut tidak akan terganggu karena mereka cukup memanggil satu jalur impor ringkas yang sama yang telah disatukan di dalam `__init__.py`.

---

### C. Demonstrasi dan Implementasi Kode

Berikut adalah contoh struktur direktori proyek modular menggunakan konsep package beserta konfigurasi berkas inisialisasi dan pengimporannya pada berkas utama secara aman:

1. **Struktur Direktori Proyek**:

```
ai_project/
├── main.py
└── preprocessing/
    ├── __init__.py
    ├── clean_text.py
    └── encoder.py
```

2. **Isi Berkas Modul `clean_text.py`**:

```
def standardize_text(text):
    # Melakukan pembersihan teks dasar dengan menghapus spasi di awal/akhir dan mengubah ke huruf kecil
    return text.strip().lower()
```

3. **Isi Berkas Modul `encoder.py`**:

```
def categorical_encoder():
    print("Encoding categorical features...")
```

4. **Isi Berkas Inisialisasi `__init__.py`**:

```
# Menentukan fungsi dari modul internal mana saja yang ingin diekspos ke tingkat package
from .clean_text import standardize_text
from .encoder import categorical_encoder
```

5. **Isi Berkas Utama `main.py` (Menggunakan Shallow Import)**:

```
# Mengimpor fungsi secara ringkas langsung dari tingkat package utama
from preprocessing import standardize_text, categorical_encoder

raw_text = "   Hello World   "
cleaned = standardize_text(raw_text)

print(f"Hasil Clean Text: '{cleaned}'")
categorical_encoder()
```



## Bab 6 Tips Pemrograman Modular (Modular Programming Tips)


### A. Prinsip Desain dan Pengorganisasian (_Design Principles_)

- **Patuhi Prinsip Single Responsibility (_Single Responsibility Principle_)**: Setiap file modul atau fungsi hanya boleh bertanggung jawab atas satu tugas atau pekerjaan spesifik. Jangan menggabungkan logika yang tidak berkaitan (seperti pembersihan data dan pelatihan model) ke dalam satu modul tunggal.
- **Atur dengan Struktur Folder yang Jelas (_Clear Folder Structure_)**: Kelompokkan berkas-berkas modul secara logis di dalam direktori proyek agar alur navigasi proyek mudah dipahami oleh anggota tim pengembang lainnya.
- **Gunakan Pelindung `if __name__ == "__main__"`**: Selalu bungkus kode eksekusi utama atau kode pengujian unit di dalam file modul utilitas menggunakan blok pelindung ini. Hal ini memastikan kode uji coba tersebut tidak berjalan secara otomatis saat modul diimpor oleh berkas lain.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa penerapan _Single Responsibility Principle_ sangat krusial dalam proyek tim berskala besar. Ketika terjadi kegagalan sistem pada proses pembersihan data, pengembang dapat langsung melacak dan memperbaiki kesalahan tersebut hanya pada berkas `preprocessing.py`. Proses pemeliharaan ini menjadi sangat efisien karena tidak ada risiko kode pelatihan model di berkas `model.py` atau berkas orkestrasi di `main.py` ikut terganggu.

---

### B. Praktik Terbaik Menghindari Masalah Teknis (_Technical Best Practices_)

- **Hindari Impor Melingkar (_Avoid Circular Imports_)**: Impor melingkar terjadi ketika `file_A.py` mengimpor `file_B.py`, sementara pada saat yang sama `file_B.py` juga mengimpor `file_A.py`. Hal ini harus dihindari karena akan membingungkan interpreter Python dan memicu kesalahan urutan eksekusi (_execution order errors_).
- **Gunakan Parameter dan Hindari Hardcoding (_Pass Parameters & Avoid Hardcoding_)**: Jangan menuliskan nilai, nama berkas, atau konfigurasi secara statis (_hardcoding_) di dalam modul fungsional. Sebaliknya, gunakan argumen atau parameter dinamis agar modul dapat digunakan kembali secara fleksibel untuk berbagai kumpulan data yang berbeda.
- **Tambahkan Berkas `__init__.py` untuk Packages**: Selalu sertakan berkas inisialisasi `__init__.py` di dalam folder modul Anda. Hal ini dilakukan untuk mendeklarasikan folder tersebut secara eksplisit sebagai sebuah _Package_ resmi dan mengaktifkan metode pengimporan yang rapi (_cleaner import_).

|Aturan Praktis|Tujuan Utama|Contoh Penerapan / Solusi|
|:--|:--|:--|
|**Single Responsibility**|Menjaga fokus satu tugas per file|Memisahkan file `data.py` dari `preprocessing.py`|
|**Avoid Circular Imports**|Mencegah error eksekusi melingkar|Mendesain jalur impor searah (file A mengimpor file B, tetapi tidak sebaliknya)|
|**Avoid Hardcoding**|Menjaga modularitas tetap fleksibel|Menggunakan fungsi `load_data(file_path)` alih-alih mengunci nama file di dalam fungsi|
|**Use **init**.py**|Mendeklarasikan folder sebagai package|Membuat berkas kosong `__init__.py` di dalam direktori modul|

#### [Wawasan Diskusi / Audio Insight]

- **Bahaya Hardcoding**: Dosen mencontohkan bahwa jika kita menuliskan langsung nama berkas secara statis di dalam modul fungsional (misalnya langsung mengunci nama berkas `sales_2024.csv` di dalam fungsi pembaca data), fungsi tersebut akan menjadi kaku. Ketika data berganti menjadi `sales_2025.csv` pada tahun berikutnya, pengembang terpaksa harus membongkar dan mengubah kode di dalam modul tersebut. Solusi terbaik adalah melewatkan nama berkas sebagai parameter dinamis ke dalam fungsi (seperti `load_data(file_name)`), sehingga modul tetap fleksibel dan tidak perlu diubah kembali di masa mendatang.
- **Penyelesaian Masalah Impor Melingkar**: Untuk menghindari kegagalan eksekusi akibat impor melingkar, pengembang harus menyusun ketergantungan antar-modul secara linear atau searah. Jika dua modul membutuhkan fungsi satu sama lain, fungsi-fungsi tersebut sebaiknya dipecah kembali ke dalam modul utilitas ketiga yang netral untuk diimpor oleh kedua modul tersebut.

---

### C. Batasan dan Evaluasi Kebutuhan Modularisasi

- **Pertimbangan Kompleksitas**: Modularisasi pada dasarnya memperkenalkan sedikit kompleksitas tambahan pada struktur proyek (seperti pengelolaan direktori, file inisialisasi, penentuan jalur impor, dan hubungan antar-modul).
- **Prinsip Evaluasi**: Jika program yang sedang dibangun sangat sederhana, berukuran kecil, dan hanya berupa skrip sekali pakai (_one-off script_), pemrograman modular tidak perlu dipaksakan. Pendekatan satu file tunggal (_monolithic_) justru lebih efisien untuk kasus-kasus sederhana guna menghindari kompleksitas yang tidak mendatangkan manfaat nyata (_unnecessary complexity_).

#### [Wawasan Diskusi / Audio Insight]

- Dosen mengingatkan mahasiswa untuk tidak terlalu ekstrem dalam melakukan modularisasi (_over-engineering_). Sebelum memecah program menjadi banyak modul, selalu lakukan evaluasi terlebih dahulu mengenai skala proyek yang dikerjakan. Modularisasi adalah sebuah investasi jangka panjang untuk keteraturan struktur kode; jika keuntungan keteraturan tersebut tidak melebihi beban kompleksitas pengelolaan berkas yang baru, maka pertahankan struktur file tunggal yang sederhana.



## Bab 7 Latihan Praktis (Practice Exercises)


### A. Latihan 1: Basic (Create Your First Module)

- **Tujuan Skenario**: Mahasiswa diarahkan untuk memecah logika pemrograman tunggal menjadi struktur modular sederhana dengan memisahkan fungsi utilitas perhitungan nilai siswa ke dalam modul terpisah dan memanggilnya melalui berkas eksekusi utama.
- **Spesifikasi Modul (`grades_utils.py`)**:
    - `calc_average(scores)`: Menerima masukan berupa daftar nilai (_list of numbers_) dan mengembalikan nilai rata-rata yang dibulatkan hingga dua angka di belakang desimal.
    - `get_grade(average)`: Menentukan huruf mutu berdasarkan nilai rata-rata dengan ketentuan klasifikasi standar.
- **Skema Klasifikasi Nilai**:

|Batas Nilai Rata-Rata|Huruf Mutu (_Grade_)|
|:--|:--|
|Lebih besar atau sama dengan 90|A|
|Lebih besar atau sama dengan 80|B|
|Lebih besar atau sama dengan 70|C|
|Lebih besar atau sama dengan 60|D|
|Di bawah 60|E|

- **Implementasi Kode Sumber**:

```
# grades_utils.py
def calc_average(scores):
    return round(sum(scores) / len(scores), 2)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "E"
```

```
# main.py
from grades_utils import calc_average, get_grade

# Representasi Data Input
scores = [80, 90, 75]

# Penghitungan Rata-rata dan Penentuan Huruf Mutu
avg_score = calc_average(scores)
grade = get_grade(avg_score)

# Menampilkan Hasil Output Pengujian
print(f"Average: {avg_score}, Grade: '{grade}'")
# Expected Output: Average: 81.67, Grade: 'B'
```

#### [Wawasan Diskusi / Audio Insight]

- **Demonstrasi Mahasiswa**: Brian mempresentasikan kode miliknya di depan kelas, menggunakan fungsi bawaan `round(..., 2)` untuk membatasi presisi nilai desimal rata-rata tepat dua angka di belakang koma guna memenuhi spesifikasi tugas.
- **Dukungan Tipe Objek Modul**: Atas pertanyaan Stepen, dosen mengonfirmasi secara eksplisit bahwa modul Python bersifat fleksibel. Modul tidak hanya terbatas untuk membungkus fungsi (_functions_), melainkan dapat menampung definisi kelas (_classes_) maupun variabel di dalamnya.

---

### B. Latihan 2: Intermediate (Control Execution with `__name__`)

- **Tujuan Skenario**: Mengontrol eksekusi kode pada modul utilitas menggunakan pelindung eksekusi (_name guard_) untuk memisahkan logika pengujian internal dari logika aplikasi utama.
- **Spesifikasi Tugas**: Menambahkan baris cetak uji coba (_test print_ atau _self test_) secara langsung di dalam berkas `grades_utils.py` menggunakan kondisional `if __name__ == "__main__":`.
- **Perbandingan Ekspektasi Eksekusi**:

|Konteks Eksekusi Berkas|Hasil Output yang Diharapkan|Status Blok Guard|
|:--|:--|:--|
|Berkas `grades_utils.py` dijalankan secara langsung|Menampilkan pesan _self test_ dan hasil pengujian lokal|Dieksekusi (_True_)|
|Berkas `grades_utils.py` diimpor ke berkas `main.py`|Berkas utama berjalan normal tanpa menampilkan pesan pengujian lokal|Dilewati (_False_)|

- **Implementasi Kode Sumber**:

```
# grades_utils.py
def calc_average(scores):
    return round(sum(scores) / len(scores), 2)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "E"

# Pelindung Blok Pengujian Lokal (Name Guard)
if __name__ == "__main__":
    test_scores = [100, 90, 95]
    test_avg = calc_average(test_scores)
    print(f"[Self Test] Run directly. Average: {test_avg}, Grade: {get_grade(test_avg)}")
```

#### [Wawasan Diskusi / Audio Insight]

- **Demonstrasi Mahasiswa**: Mbak Adiba membagikan layar pengujiannya yang menunjukkan bahwa kode pengujian lokal yang dibungkus di dalam kondisional `if __name__ == "__main__":` berhasil disembunyikan secara otomatis saat berkas utama `main.py` dijalankan, sehingga mencegah polusi konsol akibat tereksekusinya pengujian yang tidak diinginkan (_unwanted execution_).

---

### C. Latihan 3: Advanced (Build a Package)

- **Tujuan Skenario**: Mereorganisasi kode penilai siswa ke dalam satu struktur folder paket (_Package_) bernama `grades` untuk mengaktifkan pengimporan praktis tingkat permukaan (_Shallow Import_) menggunakan bantuan file inisialisasi `__init__.py`.
- **Struktur Direktori Proyek**:

```
project/
│
├── main.py
└── grades/
    ├── __init__.py
    ├── loader.py
    ├── calculator.py
    └── report.py
```

- **Spesifikasi Modul di Dalam Package**:
    - `loader.py`: Menyediakan fungsi `get_scores()` untuk mengambil data nilai siswa (dalam skenario ini mengembalikan data list statis).
    - `calculator.py`: Menyediakan fungsi `calculate_average(scores)` dan `get_grade(average)`.
    - `report.py`: Menyediakan fungsi `print_report()` yang bertugas mengoordinasikan seluruh alur pemuatan data, kalkulasi, hingga pencetakan laporan ke konsol.
- **Implementasi Kode Sumber**:

```
# grades/loader.py
def get_scores():
    return [80, 90, 75]
```

```
# grades/calculator.py
def calculate_average(scores):
    return round(sum(scores) / len(scores), 2)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "E"
```

```
# grades/report.py
from grades.loader import get_scores
from grades.calculator import calculate_average, get_grade

def print_report():
    scores = get_scores()
    avg_score = calculate_average(scores)
    grade = get_grade(avg_score)
    print("----- STUDENT GRADE REPORT -----")
    print(f"Raw Scores    : {scores}")
    print(f"Average Score : {avg_score}")
    print(f"Final Grade   : {grade}")
```

```
# grades/__init__.py
# Mengekspos fungsi spesifik ke tingkat package (Shallow Import)
from grades.calculator import get_grade
from grades.report import print_report
```

```
# main.py
# Melakukan Shallow Import langsung dari tingkat package 'grades'
from grades import get_grade, print_report

# Menguji fungsionalitas laporan yang terkoordinasi
print_report()
```

#### [Wawasan Diskusi / Audio Insight]

- **Optimalisasi Overhead & Desain Variabel**: Dosen memberikan koreksi penting pada berkas `report.py`. Disarankan untuk menampung pemanggilan fungsi `get_scores()` ke dalam sebuah variabel lokal (misalnya `scores = get_scores()`) alih-alih memanggil fungsinya secara berulang di baris kode berikutnya. Memanggil fungsi yang sama berkali-kali akan menimbulkan beban komputasi tambahan (_overhead_) yang tidak efisien. Menampung nilai ke dalam variabel lokal membantu program berjalan lebih cepat dan menjaga kerapian penulisan kode (_readability_).
- **Pertanyaan Desain Bersarang (_Nested Packages_)**: Menjawab keingintahuan Stepen mengenai apakah package bisa dibuat bertingkat (_nested packages_), dosen menjelaskan bahwa dalam praktik industri nyata, struktur paket yang terlalu dalam (_deeply nested_) sangat jarang digunakan karena memperumit manajemen jalur impor (_path management_). Struktur datar yang rapi dan terukur jauh lebih direkomendasikan.

---

### D. Materi Tambahan & Catatan Diskusi Kuliah

#### 1. Manajemen Pembaruan Repositori Git

- **Kasus Kendala**: Mahasiswa sering melakukan kloning ulang seluruh repositori secara penuh (_git clone_) saat pengajar memperbarui bahan ajar atau latihan baru di GitHub, yang mana tindakan ini tidak praktis.
- **Solusi Perintah**: Mahasiswa cukup membuka terminal, mengarahkan direktori aktif ke dalam folder repositori lokal yang lama, lalu menjalankan perintah git pull:

```
git pull
```

Perintah ini akan secara otomatis mendeteksi perubahan terbaru di repositori GitHub pengajar dan mengunduh berkas atau folder baru secara cepat tanpa merusak pekerjaan lokal yang telah dimodifikasi.

#### 2. Persiapan Pertemuan Berikutnya: Pengenalan Perkakas SQL

Pada sesi berikutnya, materi perkuliahan akan beralih ke pembahasan SQL (_Structured Query Language_). Dosen menyarankan mahasiswa untuk menyiapkan perkakas manajemen basis data.

- **Rekomendasi Perkakas Evaluasi**:

|Nama Perkakas (_Tools_)|Ruang Lingkup Dukungan|Karakteristik Penggunaan|
|:--|:--|:--|
|**MySQL Workbench**|Khusus untuk MySQL saja|Antarmuka grafis (UI) resmi untuk berinteraksi dengan server basis data MySQL.|
|**DBeaver**|Mendukung multi-basis data (_Database agnostic_)|Sangat direkomendasikan karena mendukung berbagai jenis basis data (MySQL, PostgreSQL, Google BigQuery, dll.). Perkakas ini sangat populer di industri karena fleksibilitasnya dalam mengelola berbagai ekosistem basis data yang berbeda secara bersamaan dalam satu aplikasi.|



## Test

**1. Algoritma Fungsi** **calc_average(scores)**

	Fungsi ini bertujuan untuk menghitung nilai rata-rata dari daftar nilai yang diberikan dan membulatkannya.

1. **Menerima Input**: Sebuah daftar (list) berisi angka-angka nilai, kita sebut sebagai `scores`.
2. **Validasi Data Kosong**:
    - Periksa apakah list `scores` tersebut kosong atau tidak.
    - **Jika kosong**, langsung kembalikan nilai **0.0** (langkah ini penting untuk menghindari error pembagian dengan nol/_ZeroDivisionError_).
3. **Proses Perhitungan**:
    - **Langkah A**: Hitung jumlah total seluruh nilai di dalam list (`sum`).
    - **Langkah B**: Hitung banyaknya data atau jumlah elemen di dalam list (`length`).
    - **Langkah C**: Bagi hasil **Langkah A** dengan **Langkah B** untuk mendapatkan nilai rata-rata kasar.
4. **Pembulatan**: Bulatkan hasil nilai rata-rata tersebut hingga **2 angka di belakang koma**.
5. **Kembalikan Hasil (Output)**: Kirimkan nilai rata-rata yang sudah dibulatkan tersebut kembali ke program utama (`main.py`).

---

**2. Algoritma Fungsi** **get_grade(average)**

Fungsi ini menentukan huruf mutu (grade) berdasarkan nilai rata-rata menggunakan logika percabangan (_conditional statement_).

1. **Menerima Input**: Sebuah angka desimal/integer yang merupakan nilai rata-rata, kita sebut sebagai `average`.
2. **Evaluasi Kondisi (dari nilai tertinggi ke terendah)**:
    - **Kondisi 1**: Apakah `average` **lebih besar dari atau sama dengan 90**?
        - Jika **Ya**, tentukan grade = **"A"**. Selesai.
    - **Kondisi 2**: Jika tidak, apakah `average` **lebih besar dari atau sama dengan 80**?
        - Jika **Ya**, tentukan grade = **"B"**. Selesai.
    - **Kondisi 3**: Jika tidak, apakah `average` **lebih besar dari atau sama dengan 70**?
        - Jika **Ya**, tentukan grade = **"C"**. Selesai.
    - **Kondisi 4**: Jika tidak, apakah `average` **lebih besar dari atau sama dengan 60**?
        - Jika **Ya**, tentukan grade = **"D"**. Selesai.
    - **Kondisi 5 (Pilihan Terakhir)**: Jika semua kondisi di atas tidak terpenuhi (nilai di bawah 60):
        - Tentukan grade = **"E"**. Selesai.
3. **Kembalikan Hasil (Output)**: Kirimkan huruf grade yang terpilih kembali ke program utama.



---


# Module 1 Session 9 Intro to Dabase & SQL


## Bab 1 Pengenalan Database & Database Management System (DBMS)

## 1.1 Definisi dan Karakteristik Database

### A. Fondasi Konseptual Database

- Database didefinisikan sebagai koleksi data yang terorganisasi, yang secara umum disimpan dan diakses secara elektronik dari sistem komputer.
- Istilah electronic database merujuk pada kumpulan data atau informasi apa pun yang dirancang secara khusus untuk kebutuhan rapid search dan retrieval menggunakan bantuan komputer.
- Pada tingkat kompleksitas yang lebih tinggi, database dikembangkan dengan menerapkan teknik formal design dan modeling.

| Istilah             | Karakteristik Utama                                                           |
| :------------------ | :---------------------------------------------------------------------------- |
| Database            | Organized collection of data yang disimpan secara elektronik.                 |
| Electronic Database | Kumpulan data atau informasi yang dirancang untuk rapid search dan retrieval. |
| Complex Database    | Memerlukan teknik formal design dan modeling dalam pengembangannya.           |

### B. Mekanisme Penyimpanan Elektronik

- Penyimpanan data dalam sistem komputer ditujukan untuk efisiensi pengolahan informasi digital.
- Pengorganisasian data yang sistematis memungkinkan pencarian informasi yang cepat dan akurat.

#### [Wawasan Diskusi / Audio Insight]

- Database bukan sekadar tempat penyimpanan pasif untuk menaruh data.
- Tujuan utama penyimpanan data adalah untuk memfasilitasi penggunaan kembali data tersebut di masa mendatang, baik untuk proses retrieve maupun search.
- Data yang disimpan harus diorganisasikan agar proses pencarian kembali dapat dilakukan secara cepat oleh sistem komputer.

## 1.2 Terminologi Formal dan Peran DBMS

### A. Komponen Utama Arsitektur Informasi

- Secara formal, istilah "database" merujuk pada satu set related data beserta metode pengorganisasian data tersebut.
- Akses terhadap data yang terorganisasi ini disediakan melalui perantara yang disebut Database Management System (DBMS).
- DBMS terdiri dari integrated set of computer software yang mengizinkan user untuk berinteraksi dengan satu atau lebih database.
- DBMS menyediakan akses terhadap seluruh data yang tersimpan di dalam database, meskipun pembatasan akses dapat diberlakukan untuk melindungi data tertentu.

|Komponen|Deskripsi Fungsional|
|:--|:--|
|Related Data|Kumpulan data yang saling berhubungan secara logis dan terstruktur.|
|DBMS|Integrated set of computer software untuk interaksi user dengan database.|
|Access Restriction|Mekanisme pembatasan akses untuk melindungi integritas dan kerahasiaan data tertentu.|

### B. Interaksi Pengguna dan Pengaturan Akses

- Pengguna tidak langsung memanipulasi file data fisik, melainkan berinteraksi melalui lapisan software DBMS.
- Pengaturan hak akses diatur oleh DBMS untuk membatasi query atau pembacaan data yang tidak diizinkan.

#### [Wawasan Diskusi / Audio Insight]

- Database didefinisikan sebagai kumpulan data-data yang saling berhubungan (related data) dan cara penyimpanan data tersebut secara terstruktur.
- DBMS bertindak sebagai software perantara yang memungkinkan user mengakses, mengelola, dan berinteraksi dengan satu atau lebih database secara efisien.
- Tanpa adanya DBMS, pengguna akan mengalami kesulitan besar dalam mengontrol dan mengamankan data yang tersebar dalam sistem.

## 1.3 Fungsi Utama dan Efisiensi Kerja DBMS

### A. Fungsionalitas Teknis DBMS

- DBMS berfungsi membantu proses correlate, query, dan report terhadap informasi yang telah dikumpulkan.
- Sistem ini dirancang untuk menjawab berbagai macam pertanyaan (questions) terkait data dengan sangat cepat.
- DBMS membantu pengguna memahami data yang rumit (complicated data) melalui pemrosesan yang sistematis.
- Penggunaan DBMS mampu meningkatkan efisiensi kerja serta mengurangi excessive work hours dalam mencapai target operasional tertentu.

|Fungsi Utama DBMS|Kontribusi Operasional|
|:--|:--|
|Correlate|Menghubungkan berbagai kumpulan data yang terpisah.|
|Query|Melakukan pencarian data secara spesifik menggunakan kueri.|
|Report|Menyusun laporan dari collected information.|
|Efficiency|Mengurangi excessive work hours dalam pengelolaan data.|

### B. Peningkatan Produktivitas Kerja

- DBMS mengotomatisasi pencarian data yang jika dilakukan secara manual akan memakan waktu sangat lama.
- Pemrosesan data yang terpusat meminimalkan duplikasi pekerjaan dan kesalahan manusia.

#### [Wawasan Diskusi / Audio Insight]

- DBMS mempermudah analisis data bisnis secara cepat tanpa perlu membaca data tabular satu per satu secara manual.
- **Contoh Kasus Pelanggan:** Jika perusahaan ingin mengetahui pelanggan mana yang paling loyal (sering membeli) atau pelanggan mana yang paling jarang melakukan pembelian, DBMS dapat langsung menjawab pertanyaan tersebut dengan cepat, asalkan data transaksi tersedia di database dan query ditulis dengan benar.
- **Analogi Efisiensi (Excel vs SQL):** Di Microsoft Excel, pencarian pelanggan loyal dari data tabular yang besar dapat dilakukan menggunakan fitur Pivot. Di dalam DBMS, terdapat bahasa pemrograman khusus (SQL) yang memungkinkan pengguna melakukan pengelompokan dan analisis serupa secara jauh lebih cepat dan efisien dengan menuliskan sintaks kueri yang tepat.
- DBMS sangat membantu pengguna dalam memahami data yang rumit, namun apabila tingkat kompleksitas data terlalu tinggi, DBMS memerlukan dukungan teknik lain seperti visualisasi data.

## 1.4 Database dalam Manajemen Bisnis dan Pengambilan Keputusan

### A. Pemanfaatan Strategis Informasi dalam Bisnis

- Dunia usaha atau bisnis memanfaatkan database untuk melakukan pelacakan terhadap basic transaction.
- Database menyediakan informasi penting yang membantu perusahaan menjalankan bisnis secara lebih efisien.
- Database berfungsi membantu manager dan employee dalam membuat keputusan yang lebih baik.

|Tujuan Bisnis|Manfaat Database|
|:--|:--|
|Tracking|Memantau jalannya transaksi dasar (basic transaction) perusahaan.|
|Efficiency|Menyediakan data operasional untuk efisiensi bisnis.|
|Decision-Making|Menyediakan landasan informasi bagi manajer dan karyawan untuk mengambil keputusan.|

### B. Pengambilan Keputusan Berbasis Data

- Penggunaan database memastikan setiap kebijakan operasional didasarkan pada fakta keras yang terekam dalam sistem, bukan asumsi subjektif.
- Akurasi pengambilan keputusan meningkat seiring dengan ketersediaan data historis transaksi yang lengkap.

#### [Wawasan Diskusi / Audio Insight]

- Konsep pengambilan keputusan berbasis data (data-driven decision making) hanya dapat diwujudkan apabila seluruh data bisnis tersimpan dengan baik di dalam database.
- Para manajer, karyawan, dan seluruh stakeholder yang terkait membutuhkan akses data real-time untuk menghasilkan better decision.
- DBMS merupakan satu-satunya alat penunjang utama yang memungkinkan para pengambil keputusan tersebut mengakses dan menyaring informasi yang relevan dari database.



## Bab 10 Subquery dan Kueri Bersarang (Sub Queries and Nested SELECT)


## 10.1 Definisi dan Penempatan Subquery

### A. Konsep Dasar Subquery

- Subquery atau kueri bersarang didefinisikan sebagai sebuah kueri SQL yang berada di dalam kueri SQL lainnya.
- Kueri yang berada di bagian dalam (inner query) dieksekusi terlebih dahulu, kemudian hasilnya digunakan oleh kueri yang berada di bagian luar (outer query) untuk menyelesaikan operasi utamanya.
- Subquery dapat disisipkan atau bersarang di dalam berbagai jenis pernyataan SQL utama, termasuk SELECT, INSERT, UPDATE, atau DELETE, serta dapat disisipkan di dalam subquery lainnya.

|Konsep|Deskripsi Fungsional|
|:--|:--|
|Subquery|SQL query yang ditulis di dalam kueri SQL lain yang lebih besar.|
|Outer Query|Kueri utama di tingkat luar yang memanfaatkan hasil dari subquery.|
|Inner Query|Sebutan lain dari subquery yang dieksekusi terlebih dahulu oleh mesin database.|

### B. Aturan Penulisan dan Sintaksis Umum

- Subquery umumnya diletakkan di dalam tanda kurung `()` untuk memisahkannya secara jelas dari kueri luar.
- Hasil dari subquery dapat berupa nilai tunggal (skalar), satu kolom dengan beberapa baris (list), atau sebuah tabel virtual (dataset).

#### [Wawasan Diskusi / Audio Insight]

- Subquery digunakan ketika data kueri luar bergantung pada hasil perhitungan dinamis yang tidak dapat diperoleh secara langsung dengan kueri satu tingkat biasa.
- Penggunaan indentasi saat menulis subquery sangat disarankan untuk memudahkan pembacaan struktur logika kueri bersarang, meskipun secara teknis penulisan indentasi ini tidak wajib bagi mesin MySQL (berbeda dengan bahasa pemrograman Python yang mewajibkan indentasi).

## 10.2 Subquery dalam Klausa WHERE

### A. Evaluasi Kondisi Menggunakan Fungsi Agregasi

- Salah satu batasan utama SQL adalah ketidakmampuan untuk mengevaluasi atau menaruh fungsi agregat seperti `AVG()`, `MIN()`, atau `MAX()` secara langsung di dalam klausa penyaringan `WHERE` biasa.
- Sebagai solusinya, subquery digunakan di dalam klausa `WHERE` untuk menghitung nilai agregat tersebut terlebih dahulu, sebelum hasilnya dievaluasi oleh klausa `WHERE` pada kueri utama.

|Jenis Operasi|Sintaksis Standar yang Salah|Solusi Sintaksis Menggunakan Subquery|
|:--|:--|:--|
|Filter Rata-rata|`WHERE Salary < AVG(Salary)`|`WHERE Salary < (SELECT AVG(Salary) FROM Employees)`|

### B. Studi Kasus dan Penerapan Praktis

- **Kasus 1 (Data Gaji Karyawan):** Untuk menampilkan data karyawan yang gajinya di bawah rata-rata gaji seluruh karyawan:
    
    ```
    SELECT ID, NAME, SALARY
    FROM EMPLOYEE
    WHERE SALARY < (SELECT AVG(SALARY) FROM employees);
    ```
    
- **Kasus 2 (Data Usia Karyawan):** Menampilkan nama depan, nama belakang, dan usia karyawan dari tabel `new_employees` yang memiliki usia di atas rata-rata usia seluruh karyawan:
    
    ```
    SELECT First_Name, Last_Name, Age
    FROM new_employees
    WHERE Age > (SELECT AVG(Age) FROM new_employees);
    ```
    

#### [Wawasan Diskusi / Audio Insight]

- Pada Kasus 2, subquery `(SELECT AVG(Age) FROM new_employees)` akan mengembalikan satu nilai numerik tunggal (yaitu nilai rata-rata usia). Nilai tersebut kemudian bertindak sebagai parameter pembanding dinamis untuk klausa `WHERE Age >` pada kueri utama.

## 10.3 Subquery dalam Daftar Kolom (Scalar Subquery)

### A. Substitusi Nama Kolom dengan Nilai Tunggal

- Subquery dapat digunakan di dalam daftar pilihan kolom pada klausa `SELECT` untuk mensubstitusi atau menambahkan kolom ekspresi baru (_column expressions_).
- Setiap subquery yang ditempatkan pada daftar kolom harus mengembalikan satu nilai tunggal (_scalar_) per baris kueri utama.

|Istilah|Karakteristik Utama|
|:--|:--|
|Column Expressions|Penggantian atau penambahan nama kolom dengan subquery untuk menghasilkan kolom dinamis baru.|
|Scalar Output|Syarat wajib subquery di klausa `SELECT` yang hanya boleh menghasilkan satu sel data (satu kolom dan satu baris) untuk setiap baris kueri utama.|

### B. Contoh Kasus Kolom Dinamis

- **Kasus Analisis Rentang Usia:** Menampilkan nama depan karyawan, nama belakang, usia saat ini, serta kolom tambahan berisi usia termuda dan usia tertua dari seluruh data di tabel `new_employees`:
    
    ```
    SELECT First_Name, Last_Name, Age,
           (SELECT MIN(Age) FROM new_employees) AS Youngest,
           (SELECT MAX(Age) FROM new_employees) AS Oldest
    FROM new_employees;
    ```
    

#### [Wawasan Diskusi / Audio Insight]

- Subquery yang digunakan pada daftar kolom ini sangat membantu saat pengguna ingin membandingkan nilai individual setiap baris dengan nilai ekstrem (seperti nilai minimum atau maksimum) dari keseluruhan tabel secara berdampingan tanpa perlu melakukan operasi pengelompokan `GROUP BY` yang mereduksi baris data asli.

## 10.4 Subquery dalam Klausa FROM (Derived Tables)

### A. Pembuatan Tabel Virtual Sementara

- Subquery yang diletakkan di dalam klausa `FROM` berfungsi menggantikan posisi nama tabel fisik. Konsep ini dikenal sebagai _Derived Tables_ atau _Table Expressions_.
- Subquery ini menghasilkan sekumpulan baris dan kolom yang bertindak sebagai tabel virtual sementara untuk diproses lebih lanjut oleh kueri utama.

|Terminologi|Karakteristik Utama|
|:--|:--|
|Derived Tables|Tabel sementara yang dihasilkan dari eksekusi subquery di dalam klausa `FROM`.|
|Table Expressions|Istilah lain untuk kueri bersarang yang menghasilkan struktur dataset tabular sementara di dalam klausa kueri utama.|

### B. Aturan Wajib Alias (AS) di MySQL

- Dalam sistem DBMS MySQL, setiap _Derived Table_ yang dihasilkan dari subquery pada klausa `FROM` **wajib** diberikan nama alias menggunakan kata kunci `AS` (atau ditulis langsung setelah tanda kurung tutup subquery).
    
- Jika alias ini dilewatkan, mesin MySQL akan memunculkan pesan error teknis dan kueri gagal dieksekusi.
    
- **Sintaksis Standar dengan Alias:**
    
    ```
    SELECT * FROM
    (SELECT ID, NAME, DEPARTMENT_ID FROM employees) AS ALL_EMPLOYEES;
    ```
    
- **Contoh Studi Kasus Biodata:** Menampilkan seluruh data dari tabel sementara biodata karyawan yang disaring dari tabel asli `employees`:
    
    ```
    SELECT * FROM
    (SELECT First_name, Last_name, Gender, Birth_date FROM employees) AS Employee_Biodata;
    ```
    

#### [Wawasan Diskusi / Audio Insight]

- Penamaan alias pada _Derived Table_ sangat penting bagi manajemen memori database MySQL agar kueri utama dapat merujuk kembali ke tabel hasil filter sementara tersebut dengan nama yang jelas.
- Meskipun penulisan alias ini diwajibkan oleh sintaksis MySQL, alias tersebut tidak harus selalu dipanggil secara aktif di bagian kueri utama jika memang tidak diperlukan. Pengguna dapat menuliskan alias yang singkat dan cepat (misalnya `AS SA` atau `AS ST` seperti dicontohkan dosen) agar kueri dapat dieksekusi tanpa error.



## Bab 11 Latihan Praktis (Exercise)


## 11.1 Pengenalan Database Latihan "world"

### A. Deskripsi Skema dan Struktur Tabel

- Database latihan yang digunakan adalah database bawaan MySQL yang bernama **"world"**.
- Database ini terdiri dari tiga tabel utama yang saling berelasi:
    - **`city`**: Menyimpan informasi data kota-kota di dunia (memiliki kolom `ID`, `Name`, `CountryCode`, `District`, dan `Population`).
    - **`country`**: Menyimpan informasi data negara-world (memiliki kolom `Code`, `Name`, `Continent`, `Region`, `SurfaceArea`, `IndepYear`, `Population`, `LifeExpectancy`, `GNP`, `GNPOld`, dll).
    - **`countrylanguage`**: Menyimpan informasi bahasa yang digunakan di setiap negara.

|Nama Tabel|Kolom Kunci (Key Columns)|Deskripsi Singkat|
|:--|:--|:--|
|`city`|`ID` (Primary Key), `CountryCode` (Foreign Key)|Informasi data administrasi kota tingkat dunia.|
|`country`|`Code` (Primary Key)|Data demografi, ekonomi, dan geografis negara.|
|`countrylanguage`|`CountryCode` (Primary Key), `Language`|Distribusi bahasa resmi dan non-resmi negara.|

### B. Prosedur Penyusunan Lingkungan Kerja (Injest Database)

- Proses import database dapat dilakukan melalui Command Line Interface (CLI) menggunakan utilitas `mysql` bawaan sistem operasi.
- Sebelum melakukan injest, pengguna harus mengunduh file biner beralamat `world.sql` dari laman resmi dokumentasi MySQL, kemudian mengekstraknya jika dalam format terkompresi (`.zip`).
- Perintah eksekusi impor biner database pada terminal adalah sebagai berikut:

```
mysql -u root -p world < "C:\path\to\world.sql"
```

#### [Wawasan Diskusi / Audio Insight]

- Dalam praktek instalasi langsung saat kuliah luring, beberapa mahasiswa Windows mengalami kendala perintah `mysql` tidak dikenali (_not recognized_). Solusinya adalah mendaftarkan alamat biner MySQL (contoh: `C:\Program Files\MySQL\MySQL Server 8.0\bin`) ke dalam variabel lingkungan sistem (**Environment Path**) terlebih dahulu.
- Pada terminal PowerShell Windows, simbol pengarah input `<` dicadangkan (_reserved_) untuk penggunaan masa depan sehingga akan menghasilkan error. Solusinya adalah menjalankan proses impor melalui **Command Prompt (CMD)** standar Windows agar berjalan mulus.
- Jika koneksi sukses dibuat pada perkakas antarmuka seperti **DBeaver** tetapi database `world` yang baru di-injest belum muncul pada panel navigasi, lakukan operasi **Refresh (F5)** pada folder lokal agar struktur tabel ter-render secara real-time.

---

## 11.2 Bedah Soal dan Solusi Query SQL (Database world)

### A. Soal 1: Aktivasi Database world

- **Pertanyaan:** Aktifkan database `world` agar seluruh query berikutnya mengeksekusi tabel di dalam database tersebut.
- **Sintaks SQL:**

```
USE world;
```

### B. Soal 2: Menghitung Jumlah Region Unik

- **Pertanyaan:** Ada berapa banyak region yang tercatat di dalam database `world`? Ubah nama header kolom output-nya menjadi `Jumlah_Region`.
- **Sintaks SQL:**

```
SELECT COUNT(DISTINCT region) AS Jumlah_Region
FROM country;
```

- **Hasil Eksekusi:** Teridentifikasi sebanyak **25** region unik di dunia.

### C. Soal 3: Menghitung Jumlah Negara di Benua Afrika

- **Pertanyaan:** Berapakah jumlah negara yang berada di benua Afrika (`Africa`)? Ubah nama header kolom output-nya menjadi `Jumlah_Negara`.
- **Sintaks SQL:**

```
SELECT COUNT(Name) AS Jumlah_Negara
FROM country
WHERE Continent = 'Africa';
```

- **Hasil Eksekusi:** Teridentifikasi sebanyak **58** negara di benua Afrika.

### D. Soal 4: Menampilkan 5 Negara dengan Populasi Terbesar

- **Pertanyaan:** Tampilkan 5 negara dengan jumlah populasi terbesar di dunia. Ubah nama header kolom output-nya masing-masing menjadi `Nama_Negara` dan `Populasi`.
- **Sintaks SQL:**

```
SELECT Name AS Nama_Negara, Population AS Populasi
FROM country
ORDER BY Population DESC
LIMIT 5;
```

- **Hasil Eksekusi:**
    1. China
    2. India
    3. United States (Amerika Serikat)
    4. Indonesia
    5. Brazil

### E. Soal 5: Menampilkan Rata-Rata Harapan Hidup tiap Benua

- **Pertanyaan:** Tampilkan rata-rata angka harapan hidup (`LifeExpectancy`) untuk setiap benua, diurutkan dari nilai rata-rata yang paling rendah. Ubah nama header kolom output-nya masing-masing menjadi `Nama_Benua` dan `Rata_Rata_Harapan_Hidup`.
- **Sintaks SQL:**

```
SELECT Continent AS Nama_Benua, AVG(LifeExpectancy) AS Rata_Rata_Harapan_Hidup
FROM country
GROUP BY Continent
ORDER BY Rata_Rata_Harapan_Hidup ASC;
```

#### [Wawasan Diskusi / Audio Insight]

- Saat query ini dijalankan oleh mahasiswa, benua **Antarctica** menghasilkan nilai rata-rata harapan hidup berupa `NULL` atau tidak memiliki data harapan hidup sama sekali karena tidak memiliki populasi penduduk tetap.

### F. Soal 6: Menampilkan Benua dengan Jumlah Region Lebih dari 3

- **Pertanyaan:** Tampilkan jumlah region untuk setiap benua yang memiliki jumlah region unik lebih dari 3. Ubah nama header kolom output-nya masing-masing menjadi `Nama_Benua` dan `Jumlah_Region`.
- **Sintaks SQL:**

```
SELECT Continent AS Nama_Benua, COUNT(DISTINCT Region) AS Jumlah_Region
FROM country
GROUP BY Continent
HAVING Jumlah_Region > 3;
```

- **Hasil Eksekusi:** Menampilkan daftar benua seperti Asia, Europe, dan Africa yang memenuhi kriteria penyaringan agregat.

### G. Soal 7: Menampilkan Rata-Rata GNP di Afrika Berdasarkan Region

- **Pertanyaan:** Tampilkan nilai rata-rata GNP di benua Afrika berdasarkan pembagian regionnya, lalu urutkan dari nilai rata-rata GNP yang paling besar ke yang paling kecil. Ubah nama header kolom output-nya masing-masing menjadi `Nama_Region` dan `Rata_Rata_GNP`.
- **Sintaks SQL:**

```
SELECT Region AS Nama_Region, AVG(GNP) AS Rata_Rata_GNP
FROM country
WHERE Continent = 'Africa'
GROUP BY Region
ORDER BY Rata_Rata_GNP DESC;
```

- **Hasil Eksekusi:** Peringkat rata-rata GNP terbesar dipimpin oleh Northern Africa, diikuti Southern Africa, Western Africa, Central Africa, dan Eastern Africa.

### H. Soal 8: Menampilkan Negara Berisi Tepat 6 Huruf dan Berakhiran 'O'

- **Pertanyaan:** Tampilkan nama negara yang memiliki panjang karakter nama tepat 6 huruf dan diakhiri dengan huruf 'O'.
- **Sintaks SQL:**

```
SELECT Name
FROM country
WHERE LENGTH(Name) = 6 AND Name LIKE '%o';
```

- **Hasil Eksekusi:** Menghasilkan negara-negara spesifik yang memenuhi kondisi string matching tersebut, contohnya **Monaco** dan **Mexico**.

#### [Wawasan Diskusi / Audio Insight]

- Pada diskusi luring kelas, mahasiswa sempat mencoba menyelesaikan kasus ini menggunakan manipulasi klausa `GROUP BY Name HAVING` panjang karakter tertentu. Dosen memberikan koreksi penting bahwa fungsi `LENGTH()` bukanlah fungsi agregat (melainkan fungsi skalar), sehingga penyaringan karakter string individu wajib diletakkan langsung di dalam klausa filter utama **`WHERE`** dan tidak memerlukan pengelompokan grup.

### I. Soal 9: Menampilkan Region dengan Kenaikan Rata-Rata GNP Terbesar

- **Pertanyaan:** Region mana saja yang nilai rata-rata GNP terbarunya mengalami kenaikan dibandingkan rata-rata GNP masa lalu (`GNPOld`)? Urutkan hasilnya dari nilai selisih kenaikan yang paling tinggi ke yang paling rendah.
- **Sintaks SQL:**

```
SELECT Region,
       AVG(GNP) AS Avg_GNP,
       AVG(GNPOld) AS Avg_GNPOld,
       (AVG(GNP) - AVG(GNPOld)) AS Selisih
FROM country
GROUP BY Region
HAVING AVG(GNP) > AVG(GNPOld)
ORDER BY Selisih DESC;
```

#### [Wawasan Diskusi / Audio Insight]

- Di akhir diskusi luring, terjadi perbandingan output kueri antara mahasiswa di mana region **British Islands** seharusnya berada di peringkat teratas sebagai region dengan selisih kenaikan rata-rata GNP terbesar. Perbedaan urutan sempat terjadi karena kesalahan sepele penulisan tanda petik pada klausa pengurutan `ORDER BY`.
- Dosen mengingatkan aturan mutlak penulisan SQL bahwa nama kolom alias pada klausa `ORDER BY` **dilarang keras dibungkus dengan tanda petik tunggal (`'Selisih'`)**. Pembungkusan dengan tanda petik tunggal akan dibaca oleh sistem komputer sebagai string statis konstan dan bukan representasi nilai kolom dinamis, yang mengakibatkan logika pengurutan database menjadi kacau atau tidak berjalan semestinya.



## Bab 2 interface-koneksi

## 2.1 Parameter Koneksi Database

### A. Parameter Utama Koneksi

- Untuk menghubungkan (_connect_) sistem antarmuka ke database server, diperlukan beberapa parameter utama yang harus didefinisikan secara tepat.
- Kegagalan pengisian atau ketidakcocokan salah satu parameter akan menyebabkan koneksi ditolak oleh database server.

| Parameter | Deskripsi Teknis                                                        | Nilai Standar / Default                           |
| :-------- | :---------------------------------------------------------------------- | :------------------------------------------------ |
| DBMS      | Tipe Database Management System yang ditargetkan untuk koneksi.         | MySQL, PostgreSQL, SQLite                         |
| Host      | Alamat jaringan server tempat database fisik dideploy dan dijalankan.   | `localhost` atau `127.0.0.1` (untuk server lokal) |
| Port      | Pintu masuk komunikasi data digital spesifik untuk layanan DBMS.        | `3306` (MySQL), `5432` (PostgreSQL)               |
| Username  | Nama identitas akun pengguna yang memiliki hak akses di database.       | `root` (Super Admin bawaan MySQL)                 |
| Password  | Kunci keamanan autentikasi untuk memverifikasi akses dari user terkait. | Ditentukan saat instalasi awal                    |

### B. Mekanisme Keamanan Koneksi

- Database server mengamankan data dengan membatasi koneksi hanya dari pengguna terverifikasi melalui pencocokan kombinasi Host, Username, dan Password.
- Hak akses (privilege) dapat diatur per user untuk membatasi query yang diizinkan pada objek database tertentu.

#### [Wawasan Diskusi / Audio Insight]

- Ketika ingin terhubung ke database dalam lingkungan kerja profesional, Anda wajib meminta informasi lengkap mengenai tipe DBMS yang digunakan, alamat Host, nomor Port yang terbuka, serta kredensial Username dan Password kepada tim administrator database. Tanpa parameter ini, koneksi tidak akan pernah bisa terjalin.

## 2.2 Perkakas (Tools) Mengakses Database

### A. Perbandingan GUI (Graphical User Interface) vs CLI (Command Line Interface)

- Akses ke database dapat dilakukan menggunakan dua pendekatan utama berdasarkan jenis antarmukanya.

|Jenis Perkakas|Nama Perkakas|Karakteristik Utama|
|:--|:--|:--|
|GUI (Graphical User Interface)|MySQL Workbench|Perkakas visual resmi (_official_) yang dikembangkan khusus untuk mengelola database MySQL secara eksklusif.|
|GUI (Graphical User Interface)|DBeaver|Perkakas visual multi-database yang mendukung banyak tipe DBMS seperti MySQL, PostgreSQL, SQLite, DB2, Greenplum, dan MariaDB.|
|CLI (Command Line Interface)|MySQL 8.0 Command Line Client|Antarmuka berbasis teks murni (terminal/command prompt) untuk mengeksekusi perintah database dengan mengetik baris perintah langsung.|

### B. Konfigurasi Koneksi pada GUI (DBeaver & MySQL Workbench)

- Langkah praktis pembuatan koneksi baru pada perkakas GUI:
    - **MySQL Workbench:**
        1. Klik ikon tambah (`+`) pada halaman utama (_Add Connection_).
        2. Tentukan _Connection Name_ (misalnya: "Purwadika MySQL").
        3. Masukkan parameter koneksi (Host: `127.0.0.1` atau `localhost`, Port: `3306`, Username: `root`).
        4. Saat membuka koneksi (_Open Connection_), masukkan password MySQL Anda ketika diminta.
    - **DBeaver:**
        1. Klik kanan pada panel _Database Navigator_, pilih **Create** -> **Connection**.
        2. Pilih ikon **MySQL**, lalu klik _Next_.
        3. Isi parameter koneksi (Server Host: `localhost`, Port: `3306`, Username: `root`, Password sesuai konfigurasi lokal Anda).
        4. Klik **Test Connection** untuk memverifikasi fungsionalitas koneksi sebelum menyimpannya dengan menekan tombol _Finish_.

#### [Wawasan Diskusi / Audio Insight]

- **Kelebihan GUI dibanding CLI:** Penggunaan CLI/terminal untuk melihat database dan tabel yang jumlahnya banyak dinilai sangat menyulitkan bagi pemula karena output ditampilkan dalam format teks murni yang padat dan kaku. Perkakas GUI menawarkan visualisasi yang jauh lebih terstruktur dan mudah dinavigasi.
- **Konsep Arsitektur Interface:** Perkakas GUI (DBeaver/MySQL Workbench) pada dasarnya hanyalah lapisan antarmuka (_interface/client_) yang bertindak sebagai jembatan untuk menulis (_write_) dan membaca (_retrieve_) data dari database server fisik. Jika Anda mengedit data menggunakan MySQL Workbench, data di server fisik akan langsung berubah. Sehingga ketika keesokan harinya Anda membuka DBeaver untuk membaca database yang sama, data hasil pembaruan tersebut akan langsung terbaca secara konsisten.
- **Tujuan Penggunaan Perkakas:** Perkakas database GUI dirancang untuk kebutuhan pengerjaan teknis pengembang (_developer_) atau analis data (_data analyst_) untuk mempermudah eksekusi query. Di dunia kerja nyata, tabel tabular mentah dari database GUI ini tidak disajikan langsung ke level eksekutif/direktur karena sulit dipahami secara instan. Data tersebut harus diekstraksi terlebih dahulu lalu divisualisasikan menggunakan alat visualisasi data eksternal.
- **Karakteristik Aturan Penulisan Sintaks SQL:** Penulisan query SQL bersifat fleksibel terhadap spasi, baris baru, dan indentasi (_indentation insensitive_). Hal ini berbeda dengan bahasa pemrograman Python yang mewajibkan indentasi (_indentation sensitive_). Pengaturan spasi dan baris baru pada SQL semata-mata dilakukan untuk mempermudah pemeliharaan kode dan keterbacaan (_readability_) oleh manusia.

## 2.3 Otentikasi dan Navigasi Dasar Melalui CLI

### A. Alur Kerja Otentikasi CLI

- CLI menggunakan utilitas baris perintah sistem operasi untuk masuk dan memverifikasi identitas pengguna langsung ke mesin server database.

### B. Perintah Navigasi Awal Database

- Setelah otentikasi berhasil, terminal akan menampilkan prompt `mysql>` yang menandakan sistem siap menerima query.
- Eksekusi query navigasi awal wajib diakhiri dengan tanda titik koma (semicolon `;`):
    - Menampilkan seluruh database pada server:
        
        ```
        SHOW DATABASES;
        ```
        
    - Mengaktifkan dan menggunakan database target (contoh: database `world`):
        
        ```
        USE world;
        ```
        
    - Menampilkan seluruh tabel yang berada di dalam database aktif:
        
        ```
        SHOW TABLES;
        ```
        

#### [Wawasan Diskusi / Audio Insight]

- **Pendaftaran Environment Path (Windows):** Jika saat mengetikkan perintah `mysql` pada Command Prompt (CMD) Windows muncul pesan error _'mysql' is not recognized_, hal tersebut menandakan lokasi folder instalasi biner MySQL belum terdaftar pada sistem. Langkah penyelesaiannya adalah:
    1. Cari dan buka pengaturan **Edit the system environment variables** melalui Windows Search.
    2. Buka variabel bernama **Path** pada bagian variabel lingkungan, lalu klik _Edit_ atau klik dua kali.
    3. Klik **New** dan masukkan alamat absolut folder instalasi `bin` MySQL Anda (contoh: `C:\Program Files\MySQL\MySQL Server 8.0\bin`).
    4. Klik **OK** untuk menyimpan seluruh konfigurasi.
    5. **Sangat Penting:** Tutup terminal/Command Prompt yang sedang aktif, lalu buka kembali agar perubahan variabel lingkungan tersebut dapat dimuat ulang (_reload_) oleh sistem operasi. Perintah `mysql` kini siap digunakan.
- **Penanganan Error Koneksi DBeaver (allowPublicKeyRetrieval):** Jika saat melakukan pengujian koneksi di DBeaver muncul error terkait autentikasi publik, arahkan kursor ke tab **Driver Properties** di pengaturan koneksi DBeaver Anda. Cari properti bernama `allowPublicKeyRetrieval`, lalu ubah nilainya dari `false` menjadi `true`. Simpan konfigurasi dan lakukan tes koneksi ulang.
- **Penanganan Lupa Password Database Server:** Lupa kata sandi MySQL server lokal tidak dapat diatasi dengan fitur pemulihan sederhana seperti "forgot password". Prosedur reset manualnya sangat kompleks dan memakan waktu. Metode pemecahan masalah tercepat untuk lingkungan belajar lokal adalah melakukan _uninstall_ aplikasi MySQL Server secara total, lalu menginstal ulang server database tersebut untuk mengonfigurasi kata sandi administratif yang baru. Proses instalasi ulang ini tidak perlu dilakukan pada aplikasi antarmuka seperti DBeaver.
- **Unduh Driver Database Otomatis:** Saat pertama kali mengonfigurasi koneksi database jenis baru pada DBeaver, aplikasi akan mendeteksi kebutuhan berkas driver pendukung dan memicu unduhan otomatis dari repositori online. Pengguna cukup mengonfirmasi persetujuan unduhan (_download_) agar koneksi dapat diaktifkan.



## Bab 3 Operasi Dasar Database & Pembuatan Tabel (DDL - Data Definition Language)

## 3.1 Operasi Dasar Database

### A. Pendefinisian dan Manajemen Database

- Database baru didefinisikan dan dibuat pada server database menggunakan perintah Data Definition Language (DDL).
- Pembuatan database menghasilkan ruang penyimpanan kosong di server yang siap diisi dengan berbagai objek database, seperti tabel.
- Operasi manajemen database dasar meliputi pembuatan, melihat daftar database yang aktif, memilih database untuk digunakan, dan menghapus database dari server.

|Perintah SQL|Deskripsi Fungsional|Kode Contoh|
|:--|:--|:--|
|CREATE DATABASE|Membuat database baru di server database.|`CREATE DATABASE Seller;`|
|SHOW DATABASES|Menampilkan daftar seluruh database yang tersedia di server.|`SHOW DATABASES;`|
|USE|Mengaktifkan database tertentu agar query selanjutnya dieksekusi di database tersebut.|`USE Seller;`|
|DROP DATABASE|Menghapus database beserta seluruh tabel dan data di dalamnya secara permanen.|`DROP DATABASE Seller;`|

### B. Sintaksis dan Eksekusi Perintah SQL

- Setiap perintah DDL diakhiri dengan tanda titik koma (`;`) sebagai pembatas (delimiter) standar dalam SQL, terutama ketika mengeksekusi beberapa perintah sekaligus.
- Penghapusan database menggunakan perintah `DROP DATABASE` harus dilakukan secara hati-hati karena tindakan ini bersifat destruktif dan tidak dapat dibatalkan (undo).

#### [Wawasan Diskusi / Audio Insight]

- **Proses Refresh UI:** Saat membuat database baru (misalnya `demo_scratch`) melalui SQL script editor di perangkat lunak GUI seperti DBeaver, database baru tersebut tidak akan langsung muncul di panel navigasi kiri secara otomatis. Pengguna harus melakukan operasi _refresh_ (menekan tombol F5 atau klik kanan -> _Refresh_) untuk memperbarui tampilan antarmuka pengguna.
- **Urutan Operasi:** Setelah database dibuat menggunakan `CREATE DATABASE`, pengguna wajib mengaktifkan database tersebut dengan perintah `USE` sebelum dapat membuat tabel atau memasukkan data ke dalamnya.
- **Sistem Bawaan:** Saat pertama kali mengoneksikan database server yang baru diinstal, sistem secara bawaan sudah memiliki database sistem default bernama `sys` yang digunakan untuk keperluan internal sistem DBMS.

---

## 3.2 Pembuatan Tabel Baru (CREATE TABLE)

### A. Struktur dan Definisi Kolom Tabel

- Tabel adalah objek database utama yang menyimpan data dalam bentuk baris (rows) dan kolom (columns).
- Perintah `CREATE TABLE` digunakan untuk mendefinisikan tabel baru dengan menentukan nama tabel, nama kolom, serta tipe data untuk masing-masing kolom.
- Tipe data (Data Type) menentukan jenis nilai yang dapat disimpan oleh suatu kolom, seperti angka bulat (integer) atau karakter teks (character string).

|Karakteristik Struktur|Deskripsi Teknis|
|:--|:--|
|Table Name|Nama pengidentifikasi unik untuk tabel di dalam database yang aktif.|
|Column Name|Nama pengidentifikasi unik untuk setiap kolom dalam tabel.|
|Data Type|Jenis data yang dialokasikan untuk kolom (seperti `int` atau `varchar`).|
|Character Limit|Batas panjang karakter maksimum yang dapat ditampung oleh tipe data string/character.|

### B. Sintaksis Dasar Pembuatan Tabel

- Struktur penulisan query `CREATE TABLE` menggunakan tanda kurung untuk membungkus definisi kolom-kolomnya, dengan koma sebagai pemisah antar-definisi kolom.

```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    column4 datatype
);
```

### C. Contoh Praktis Pembuatan Tabel Persons

- Tabel contoh bernama `Persons` dibuat dengan mendefinisikan lima kolom spesifik: `PersonID`, `LastName`, `FirstName`, `Address`, dan `City`.

```
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
```

- Penjelasan detail alokasi kolom pada tabel `Persons`:
    - Kolom `PersonID` menggunakan tipe data `int` yang dialokasikan untuk menyimpan bilangan bulat (integer).
    - Kolom `LastName`, `FirstName`, `Address`, dan `City` menggunakan tipe data `varchar(255)`, yang berarti kolom-kolom tersebut menampung data karakter alfanumerik variabel dengan batas panjang maksimum 255 karakter.

### D. Deskripsi dan Verifikasi Struktur Tabel

- Setelah tabel berhasil dibuat, struktur tabel tersebut dapat diverifikasi untuk memastikan tipe data dan batasan kolom telah terkonfigurasi dengan benar.
- Perintah verifikasi struktur di terminal adalah:

```
DESCRIBE table_name;
```

#### [Wawasan Diskusi / Audio Insight]

- **Verifikasi Struktur via GUI dan CLI:** Pada aplikasi GUI seperti DBeaver, detail kolom dapat dilihat dengan mengklik ganda nama tabel lalu membuka tab _Data_ atau _Properties_. Di sisi lain, pada CLI, perintah `DESCRIBE` (contoh: `DESCRIBE person;`) akan menampilkan informasi kolom berupa nama kolom (_Field_), tipe data (_Type_), apakah kolom diperbolehkan kosong (_Null_), dan penunjuk kunci (_Key_).
- **Pengaturan Nullability:** Kolom-kolom pada tabel `Persons` yang baru dibuat secara default akan bernilai `YES` pada kolom _Null_. Ini berarti kolom tersebut bersifat opsional dan diperbolehkan untuk tidak memiliki nilai (bernilai null) saat pengisian data.
- **Ketiadaan Constraint Key:** Pada contoh dasar ini, belum ada kolom yang didefinisikan sebagai _Primary Key_ atau kunci unik lainnya, sehingga kolom _Key_ pada deskripsi struktur tabel masih kosong.

---

## 3.3 Pembuatan Tabel Berdasarkan Tabel yang Sudah Ada (CREATE TABLE Using Another Table)

### A. Konsep Duplikasi Struktur dan Data

- Sistem database mengizinkan pembuatan tabel baru dengan menyalin definisi kolom dari tabel yang sudah ada.
- Metode ini dikenal dengan istilah _CREATE TABLE Using Another Table_.
- Tabel baru yang dihasilkan akan mewarisi definisi kolom yang sama persis dengan tabel sumber, dan secara otomatis terisi oleh data dari tabel sumber berdasarkan query pemilihan yang didefinisikan.

### B. Sintaksis Duplikasi Tabel

- Duplikasi tabel memanfaatkan kombinasi klausa `CREATE TABLE` dan perintah pemilihan `SELECT` dengan kata kunci `AS`.

```
CREATE TABLE new_table_name AS
SELECT column1, column2
FROM existing_table_name
WHERE condition;
```

- Pengguna dapat menyalin seluruh kolom menggunakan simbol asterisk (`*`) atau hanya memilih beberapa kolom spesifik yang dibutuhkan dari tabel sumber.

### C. Contoh Praktis Duplikasi Tabel TestTable

- Duplikasi tabel dilakukan untuk membuat tabel baru bernama `TestTable` yang merupakan salinan kolom `customername` dan `contactname` dari tabel sumber bernama `customers`.

```
CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers;
```

#### [Wawasan Diskusi / Audio Insight]

- **Penundaan Latihan Praktis:** Dalam sesi kuliah luring, dosen memutuskan untuk menunda praktik langsung pembuatan tabel menggunakan metode _CREATE TABLE Using Another Table_ ini. Penundaan ini bertujuan agar mahasiswa memahami terlebih dahulu dasar-dasar query pencarian dan manipulasi data dasar menggunakan klausa `SELECT`, `FROM`, dan `WHERE` (DML) secara menyeluruh sebelum melakukan operasi penyalinan struktur database yang lebih kompleks.



## Bab 4 Manipulasi Data Dasar & Pemilihan Data (DML - Data Manipulation Language)

## 4.1 Memasukkan Data Baru ke Tabel (INSERT INTO)

### A. Definisi dan Fungsi Perintah INSERT INTO

- Perintah `INSERT INTO` digunakan untuk menambahkan baris data baru (records) ke dalam suatu tabel di database.
- Data yang dimasukkan harus mematuhi tipe data dan aturan kolom yang didefinisikan saat tabel dibuat pada tahap DDL.

|Metode INSERT|Karakteristik Sintaksis|Keuntungan Utama|
|:--|:--|:--|
|Metode Pertama|Menspesifikasikan nama kolom sebelum klausa VALUES.|Aman jika struktur urutan kolom tabel berubah di masa depan.|
|Metode Kedua|Langsung memasukkan nilai setelah klausa VALUES tanpa nama kolom.|Query lebih pendek dan cepat ditulis, namun nilai wajib sesuai urutan skema kolom.|

### B. Metode Pertama INSERT INTO (Spesifikasi Nama Kolom)

- Metode ini mendefinisikan kolom-kolom target secara eksplisit sebelum memasukkan nilainya.
- Sintaksis:

```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

- Contoh Kasus:

```
INSERT INTO persons (PersonID, LastName, FirstName, Address, City)
VALUES (1, 'Andrew', 'Michael', 'Jln. Mawar', 'BSD');
```

### C. Metode Kedua INSERT INTO (Tanpa Spesifikasi Nama Kolom)

- Jika nilai ditambahkan untuk seluruh kolom tabel, penulisan nama kolom dapat dilewati dengan syarat urutan nilai wajib sama persis dengan urutan kolom dalam skema tabel asli.
- Sintaksis:

```
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

- Contoh Kasus:

```
INSERT INTO persons
VALUES (2, 'Zidane', 'Zinedine', 'Jln. Anggret', 'DKI');
```

#### [Wawasan Diskusi / Audio Insight]

- **Aturan Penggunaan Titik Koma (Semicolon):** Dalam perangkat lunak DBMS seperti DBeaver atau MySQL Workbench, penggunaan titik koma di akhir baris query bersifat opsional jika Anda mengeksekusi query satu per satu. Namun, jika Anda menjalankan beberapa perintah sekaligus (multiple commands) secara berurutan, titik koma wajib diletakkan di akhir setiap query sebagai pemisah agar tidak memicu error sistem.
- **Penyisipan Data Ganda (Multiple Rows Insert):** DBMS mendukung penyisipan banyak baris data sekaligus dalam satu kali eksekusi perintah `INSERT INTO` untuk meningkatkan efisiensi operasional. Caranya adalah dengan memisahkan setiap kelompok nilai menggunakan tanda koma di dalam klausa `VALUES`.
- Contoh Sintaksis Penyisipan Ganda:

```
INSERT INTO persons (PersonID, LastName, FirstName, Address, City)
VALUES
(3, 'Gandi', 'G', 'Jalan Caka', 'Jakarta'),
(4, 'Arif', 'A', 'Jalan Caka', 'Jakarta');
```

## 4.2 Pemilihan dan Menampilkan Data Tabel (SELECT)

### A. Kegunaan Perintah SELECT

- Perintah `SELECT` digunakan untuk mengekstrak dan menampilkan data dari tabel database.
- Hasil pencarian data tersebut disimpan dalam tabel hasil sementara yang disebut sebagai result-set.

|Jenis Perintah SELECT|Bentuk Sintaksis|Efek Terhadap Kolom Hasil|
|:--|:--|:--|
|SELECT Bintang (`*`)|`SELECT * FROM table_name;`|Menampilkan seluruh kolom yang terdaftar di tabel secara lengkap.|
|SELECT Kolom Spesifik|`SELECT col1, col2 FROM table_name;`|Hanya menampilkan kolom-kolom yang didefinisikan secara eksplisit.|

### B. Menampilkan Seluruh Kolom (*)

- Karakter bintang (`*`) bertindak sebagai wildcard yang memerintahkan DBMS untuk mengambil seluruh kolom yang ada pada skema tabel target.
- Sintaksis:

```
SELECT * FROM table_name;
```

- Contoh Kasus (Menampilkan seluruh data kota dari tabel `City` yang memiliki kolom ID, Name, CountryCode, District, dan Population):

```
SELECT * FROM CITY;
```

### C. Menampilkan Kolom Tertentu

- Untuk menghemat memori dan meningkatkan keterbacaan data, Anda dapat memilih beberapa kolom spesifik saja dengan memisahkan nama kolom menggunakan tanda koma.
- Sintaksis:

```
SELECT column1, column2, ...
FROM table_name;
```

- Contoh Kasus (Mengambil kolom nama kota, distrik, dan populasi dari tabel `City`):

```
SELECT Name, District, Population
FROM City;
```

#### [Wawasan Diskusi / Audio Insight]

- Penggunaan `SELECT *` sangat praktis saat melakukan eksplorasi data awal guna memahami skema dan isi tabel. Namun, pada database produksi skala besar, menyeleksi kolom spesifik jauh lebih direkomendasikan untuk menghindari overhead transfer data yang tidak diperlukan.

## 4.3 Menampilkan Nilai Unik (SELECT DISTINCT)

### A. Konsep Penghapusan Duplikasi

- Di dalam tabel database, sebuah kolom sering kali berisi nilai-nilai yang sama (duplikat).
- Klausa `DISTINCT` digunakan di dalam pernyataan `SELECT` untuk menyaring hasil query sehingga hanya menampilkan nilai-nilai yang unik dan berbeda saja.

|Sintaksis DISTINCT|Target Pengolahan|Output Hasil Query|
|:--|:--|:--|
|`SELECT DISTINCT column_name`|Mengidentifikasi nilai-nilai unik dalam kolom terpilih.|Menghilangkan seluruh nilai duplikat yang redundan dari result-set.|

### B. Sintaksis SELECT DISTINCT

- Sintaksis:

```
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

- Contoh Kasus 1 (Mendapatkan daftar nama kota unik dari tabel `City` tanpa pengulangan nama yang sama):

```
SELECT DISTINCT Name
FROM City;
```

- Contoh Kasus 2 (Mendapatkan daftar distrik unik dari tabel `City`):

```
SELECT DISTINCT District
FROM City;
```

#### [Wawasan Diskusi / Audio Insight]

- Penggunaan `SELECT DISTINCT` sangat penting dalam analisis data bisnis, misalnya untuk mengetahui sebaran kota asal pelanggan atau daftar wilayah pengiriman yang aktif tanpa perlu dibingungkan oleh ribuan baris transaksi duplikat yang berulang.

## 4.4 Membatasi Jumlah Baris Query (LIMIT)

### A. Pengendalian Volume Output Query

- Klausa `LIMIT` digunakan untuk menentukan jumlah baris data maksimal yang ingin ditampilkan oleh result-set.
- Aturan ini sangat berguna untuk membatasi tampilan record sehingga pengolahan data menjadi lebih cepat dan efisien.

|Kata Kunci|Kegunaan Utama|Implikasi Kinerja DBMS|
|:--|:--|:--|
|`LIMIT n`|Membatasi baris yang ditampilkan maksimal sebanyak n baris teratas.|Menghemat memori dan mempercepat waktu tunggu retrieval data skala besar.|

### B. Sintaksis Klausa LIMIT

- Klausa `LIMIT` diletakkan di bagian paling akhir dari suatu pernyataan SQL.
- Sintaksis:

```
SELECT column1, column2, ...
FROM table_name
LIMIT number;
```

- Contoh Kasus 1 (Menampilkan 3 baris data teratas dari tabel `City`):

```
SELECT * FROM City
LIMIT 3;
```

- Contoh Kasus 2 (Menampilkan 5 baris data teratas dari tabel `City`):

```
SELECT * FROM City
LIMIT 5;
```

#### [Wawasan Diskusi / Audio Insight]

- **Kombinasi Strategis:** Klausa `LIMIT` akan bekerja secara maksimal ketika dikombinasikan dengan perintah pengurutan data (`ORDER BY`). Sebagai contoh, kombinasi ini dapat mempermudah pencarian record ekstrem seperti "3 kota dengan populasi tertinggi" atau "5 pelanggan dengan transaksi paling sedikit" (_Top-N_ dan _Bottom-N_ analysis).
- **Optimasi Kueri:** Menjalankan kueri `SELECT * FROM table_name` pada tabel berisi jutaan baris tanpa menyertakan klausa `LIMIT` dapat membebani server database secara signifikan karena sistem dipaksa memproses dan mencetak seluruh data sekaligus. Membiasakan diri menggunakan `LIMIT` saat eksplorasi data adalah praktik terbaik dalam pengembangan aplikasi database.



## Bab 5 Penyaringan Data Tingkat Lanjut (Filtering Data)


## 5.1 Klausa Penyaringan WHERE

- Klausa `WHERE` adalah perintah dasar yang digunakan untuk menyaring baris data (_records_) dari tabel.
- Fungsi utama klausa ini adalah mengekstrak hanya baris data yang memenuhi kriteria atau kondisi spesifik yang ditentukan.
- Klausa `WHERE` diletakkan setelah klausa `FROM` dalam struktur query SQL.

### A. Sintaksis Dasar dan Penyaringan Nilai Numerik

- SQL menggunakan operator perbandingan standar seperti `=`, `>`, `<`, `>=`, `<=`, dan `<>` (tidak sama dengan) dalam kondisi `WHERE`.
- Kriteria penyaringan numerik tidak membutuhkan tanda kutip di sekitar nilai angka yang dicari.

```
SELECT column1, column2, ... FROM table_name WHERE condition;
```

- Contoh query untuk menyaring seluruh kolom dari tabel `City` yang memiliki jumlah populasi lebih dari satu juta jiwa (1.000.000):

```
SELECT * FROM City WHERE Population > 1000000;
```

### B. Penyaringan Data Teks dan String

- Penyaringan data teks atau string membutuhkan penggunaan tanda kutip tunggal (`'`) di sekitar nilai teks yang menjadi kriteria penyaringan.
    
- Contoh query untuk menyaring seluruh kolom dari tabel `City` yang berada di negara Indonesia (menggunakan kode negara `'IDN'`):
    

```
SELECT * FROM City WHERE CountryCode = 'IDN';
```

### C. Penggabungan Beberapa Kondisi (AND dan OR Operator)

- Beberapa kriteria penyaringan dapat digabungkan secara logis menggunakan operator `AND` atau `OR`.
    
- Operator `AND` mengharuskan seluruh kondisi penyaringan terpenuhi agar baris data ditampilkan.
    
- Operator `OR` mengizinkan baris data ditampilkan apabila salah satu kondisi penyaringan terpenuhi.
    
- Contoh query menggunakan operator `AND` untuk menampilkan kota di Indonesia yang memiliki populasi di atas 500.000 jiwa:
    

```
SELECT * FROM City WHERE CountryCode = 'IDN' AND Population > 500000;
```

- Contoh query menggunakan operator `OR` untuk menampilkan kota yang berada di Indonesia (`'IDN'`) atau Malaysia (`'MYS'`):

```
SELECT * FROM City WHERE CountryCode = 'IDN' OR CountryCode = 'MYS';
```

#### [Wawasan Diskusi / Audio Insight]

- Klausa `WHERE` bertindak sebagai penyaring pertama sebelum data diolah lebih lanjut oleh sistem.
- Di dalam diskusi kuliah dicontohkan bahwa operator `AND` memaksa pemenuhan kondisi secara kaku (misalnya, kota tersebut harus berada di negara Indonesia sekaligus memiliki populasi padat). Sebaliknya, operator `OR` memberikan kelonggaran di mana baris data akan lolos penyaringan apabila salah satu dari kondisi terpenuhi.

---

## 5.2 Pencocokan Pola Teks (String Patterns menggunakan LIKE Operator)

- Operator `LIKE` digunakan bersama klausa `WHERE` untuk mencari pola teks tertentu (_specified pattern_) pada kolom string.
- Pencocokan pola ini sangat berguna ketika pengguna tidak mengetahui nilai teks secara persis tetapi mengetahui sebagian polanya.

### A. Penggunaan Wildcard dalam SQL

- SQL menyediakan dua karakter khusus (_wildcards_) yang digunakan bersama operator `LIKE`:
    - `%` (Tanda Persen): Merepresentasikan nol, satu, atau beberapa karakter (_zero, one, or multiple characters_).
    - `_` (Tanda Garis Bawah / Underscore): Merepresentasikan satu karakter tunggal saja secara eksis (_exactly a single character_).
- Kedua wildcard ini dapat digunakan secara terpisah maupun digabungkan dalam satu pola pencarian teks.

|Pola Operator LIKE|Deskripsi Pola Pencarian|
|:--|:--|
|`WHERE SellerName LIKE 'a%'`|Menemukan nilai teks yang diawali dengan huruf "a".|
|`WHERE SellerName LIKE '%a'`|Menemukan nilai teks yang diakhiri dengan huruf "a".|
|`WHERE SellerName LIKE '%or%'`|Menemukan nilai teks yang mengandung suku kata "or" di posisi mana pun.|
|`WHERE SellerName LIKE '_r%'`|Menemukan nilai teks yang memiliki huruf "r" di posisi kedua.|
|`WHERE SellerName LIKE 'a_%'`|Menemukan nilai teks yang diawali dengan huruf "a" dengan panjang minimal 2 karakter.|
|`WHERE SellerName LIKE 'a__%'`|Menemukan nilai teks yang diawali dengan huruf "a" dengan panjang minimal 3 karakter.|
|`WHERE SellerName LIKE 'a%o'`|Menemukan nilai teks yang diawali dengan huruf "a" dan diakhiri dengan huruf "o".|

### B. Implementasi Query dengan Wildcard Persen (%)

- Wildcard `%` diletakkan di posisi tertentu dalam string kriteria untuk menentukan arah pencarian pola teks.
    
- Contoh query menampilkan seluruh kolom dari tabel `City` yang nama distriknya diawali dengan huruf 'Y':
    

```
SELECT * FROM CITY WHERE DISTRICT LIKE 'Y%';
```

- Contoh query menampilkan seluruh kolom dari tabel `City` yang nama distriknya diakhiri dengan huruf 'x':

```
SELECT * FROM CITY WHERE DISTRICT LIKE '%x';
```

- Contoh query menampilkan seluruh kolom dari tabel `City` yang nama kotanya diawali dengan huruf 'Y' dan diakhiri dengan huruf 'a':

```
SELECT * FROM CITY WHERE NAME LIKE 'Y%a';
```

#### [Wawasan Diskusi / Audio Insight]

- Dalam rekaman audio kuliah, dosen memberikan contoh praktis pencarian kota yang diawali dengan huruf tertentu, seperti kota yang diawali dengan huruf 'X'. Saat kueri dijalankan, database langsung mengekstrak kota-kota seperti Xushan, Xinghua, Xiangcheng, dan sejenisnya dari tabel.
- Karakter persen (`%`) bekerja secara dinamis karena mampu menampung karakter apa pun dengan panjang berapa pun setelah huruf awal ditentukan.

---

## 5.3 Penyaringan Rentang Nilai (BETWEEN & NOT BETWEEN)

- Operator `BETWEEN` digunakan untuk menyaring baris data yang nilainya berada dalam batas rentang tertentu.
- Jenis data yang dapat difilter menggunakan operator ini meliputi tipe data numerik (_numbers_), teks (_text_), maupun tanggal (_dates_).

### A. Sifat Inklusif Operator BETWEEN

- Operator `BETWEEN` bersifat **inklusif** (_inclusive_), yang berarti nilai batas awal (_begin value_) dan nilai batas akhir (_end value_) dimasukkan sebagai bagian dari hasil penyaringan.

```
SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2;
```

- Contoh query untuk menampilkan nama kota beserta populasi dari tabel `City` yang memiliki rentang populasi antara satu juta (1.000.000) sampai dua juta (2.000.000) jiwa:

```
SELECT Name, Population FROM City WHERE Population BETWEEN 1000000 AND 2000000;
```

- Contoh query untuk menampilkan nama negara, wilayah (_region_), dan angka harapan hidup (_life expectancy_) dari tabel `Country` yang memiliki angka harapan hidup antara 80 sampai 90 tahun:

```
SELECT Name, Region, LifeExpectancy FROM Country WHERE LifeExpectancy BETWEEN 80 AND 90;
```

### B. Operator NOT BETWEEN

- Operator `NOT BETWEEN` bekerja sebaliknya, yaitu mengecualikan rentang nilai yang ditentukan dan hanya menampilkan data yang berada di luar rentang tersebut.
    
- Contoh query menampilkan nama negara, wilayah, dan angka harapan hidup dari tabel `Country` yang angka harapan hidupnya berada di luar rentang 45 sampai 90 tahun:
    

```
SELECT Name, Region, LifeExpectancy FROM Country WHERE LifeExpectancy NOT BETWEEN 45 AND 90;
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa secara konseptual, penulisan operator `BETWEEN` merupakan bentuk penyederhanaan sintaksis yang setara dengan penulisan operator perbandingan matematika manual menggunakan logika `AND`.
- Sebagai contoh, kondisi `WHERE Population BETWEEN 1000000 AND 2000000` secara fungsional identik dengan penulisan kondisi `WHERE Population >= 1000000 AND Population <= 2000000`. Database akan menghasilkan kumpulan data (_result set_) yang sama persis.

---

## 5.4 Sensitivitas Karakter (Case Sensitivity) pada Penyaringan SQL

- Penanganan sensitivitas huruf dalam eksekusi query dipengaruhi oleh letak komponen dan sistem operasi yang digunakan.

### A. Aturan Standar Case Sensitivity dalam Database

- Kata kunci dasar atau perintah utama SQL (_SQL keywords_) seperti `SELECT`, `WHERE`, `LIKE`, `AND`, dan `OR` bersifat **case-insensitive** (tidak sensitif huruf). Perintah dapat ditulis dalam huruf besar maupun huruf kecil tanpa memengaruhi fungsionalitas.
- Nama kolom (_column names_) secara umum bersifat **case-insensitive**.
- Nama database dan nama tabel (_database and table names_) sangat bergantung pada sistem operasi yang menjalankan database server:
    - Pada sistem operasi **Linux**, nama database dan tabel bersifat **case-sensitive** (sensitif huruf).
    - Pada sistem operasi **Windows** dan **macOS**, nama database dan tabel bersifat **case-insensitive** (tidak sensitif huruf).

### B. Sensitivitas Perbandingan String

- Perbandingan string (_text data and string comparison_) yang dieksekusi di dalam klausa `WHERE` (termasuk operator `LIKE`) sangat bergantung pada kolasi dari kolom tabel (_columns collation_).

#### [Wawasan Diskusi / Audio Insight]

- Mahasiswa mengonfirmasi bahwa ketika mereka menuliskan nama kolom seperti `district`, `city`, atau `countrycode` menggunakan huruf kecil semua (tanpa kapital), database tetap berhasil mengekstrak data tanpa memicu pesan kesalahan (_error_).
- Namun, dosen mengingatkan bahwa sensitivitas huruf menjadi sangat krusial saat melakukan pencarian teks spesifik. Misalnya, mencari data teks tertentu di dalam kolom harus ditulis secara hati-hati karena dapat dipengaruhi oleh konfigurasi kolasi bawaan dari kolom bersangkutan di database server.



## Bab 6 Pembaruan dan Penghapusan Data (Updating & Deleting)


## 6.1 Perintah Pembaruan Data (UPDATE)

### A. Konseptual dan Sintaksis Dasar UPDATE

- Perintah `UPDATE` digunakan untuk memodifikasi atau mengubah baris data yang sudah ada (existing records) di dalam suatu tabel database.
- Sintaksis dasar dari perintah `UPDATE` adalah sebagai berikut:

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- Klausa `SET` digunakan untuk menentukan kolom yang akan diubah beserta nilai barunya, sedangkan klausa `WHERE` berfungsi menentukan kondisi atau kriteria baris data mana saja yang akan diperbarui nilainya.

### B. Demonstrasi Kasus dan Penerapan Praktis

- Pembaruan data dapat disimulasikan menggunakan tabel `person` yang telah dibuat pada bab sebelumnya.
- **Kasus 1 (Pembaruan ID Tunggal):** Mengubah data alamat (`Address`) menjadi `'Jln. Melati'` dan kota (`City`) menjadi `'DKI'` untuk record dengan `PersonID` bernilai 1 (Andrew).

```
UPDATE person
SET Address = 'Jln. Melati', City = 'DKI'
WHERE PersonID = 1;
```

- Sebelum query dijalankan, alamat Andrew adalah `'Jln. Mawar'` dengan kota `'BSD'`. Setelah query dieksekusi, kolom alamat berubah menjadi `'Jln. Melati'` dan kota menjadi `'DKI'`.
- **Kasus 2 (Pembaruan Multi-Kolom):** Mengubah nama belakang (`LastName`) menjadi `'Andrea'` dan nama depan (`FirstName`) menjadi `'Robert'` untuk baris dengan `PersonID` bernilai 2.

```
UPDATE person
SET LastName = 'Andrea', FirstName = 'Robert'
WHERE PersonID = 2;
```

#### [Wawasan Diskusi / Audio Insight]

- Melalui alat antarmuka seperti DBeaver atau MySQL Workbench, setelah melakukan perubahan data (`UPDATE`), pengguna dapat menjalankan kueri seleksi untuk memverifikasi perubahan secara instan.

```
SELECT * FROM person;
```

- Data yang telah diperbarui akan langsung tercermin secara real-time pada tabel hasil kueri seleksi.

---

## 6.2 Perintah Penghapusan Data (DELETE)

### A. Konseptual dan Sintaksis Dasar DELETE

- Perintah `DELETE` digunakan untuk menghapus baris data yang sudah ada (existing records) dari suatu tabel di database.
- Sintaksis dasar dari perintah `DELETE` adalah sebagai berikut:

```
DELETE FROM table_name
WHERE condition;
```

- Klausa `WHERE` pada kueri `DELETE` sangat vital karena menentukan kriteria spesifik baris mana yang akan dihapus secara permanen dari tabel.

### B. Demonstrasi Kasus dan Penerapan Praktis

- **Kasus 1 (Penghapusan Berdasarkan ID):** Menghapus record tertentu di dalam tabel `person` yang memiliki `PersonID` bernilai 4.

```
DELETE FROM person
WHERE PersonID = 4;
```

- Setelah kueri dieksekusi, baris data dengan ID bernilai 4 akan terhapus sepenuhnya dari tabel `person`.
- **Kasus 2 (Penghapusan Berdasarkan Usia):** Penghapusan record pada tabel `pelanggan` untuk pelanggan yang memiliki kriteria usia (`Usia`) bernilai 28 tahun.

```
DELETE FROM pelanggan
WHERE Usia = 28;
```

- Sebelum kueri dieksekusi, terdapat record pelanggan bernama Joni Saputra dengan usia 28 tahun. Setelah kueri dijalankan, record tersebut terhapus secara permanen.

#### [Wawasan Diskusi / Audio Insight]

- Setiap operasi `DELETE` yang berhasil dieksekusi di DBMS local host akan langsung menghapus data dari penyimpanan fisik.
- Pengguna disarankan untuk selalu menjalankan perintah kueri seleksi `SELECT * FROM table_name;` pasca eksekusi `DELETE` untuk mengonfirmasi bahwa baris data yang terhapus sudah tepat dan tidak ada kesalahan penghapusan.

---

## 6.3 Bahaya Operasi Tanpa Klausa WHERE

### A. Konsekuensi Kelalaian Klausa WHERE

- Mengabaikan penggunaan klausa `WHERE` pada perintah `UPDATE` atau `DELETE` merupakan kesalahan fatal yang dapat merusak integritas data tabel.
- Jika klausa `WHERE` tidak disertakan pada perintah `UPDATE`, maka **seluruh baris** data yang ada di tabel tersebut akan diperbarui secara massal menggunakan nilai baru yang didefinisikan pada klausa `SET`.
- Jika klausa `WHERE` tidak disertakan pada perintah `DELETE`, maka **seluruh baris data** yang ada di dalam tabel tersebut akan dihapus sekaligus, menyisakan tabel dalam keadaan kosong tanpa isi.

|Perintah|Dampak Tanpa Klausa WHERE|Konsekuensi Operasional|
|:--|:--|:--|
|UPDATE|Mengubah nilai kolom yang ditentukan untuk seluruh baris data di tabel.|Kehilangan data historis atau data asli secara permanen pada baris yang seharusnya tidak diubah.|
|DELETE|Menghapus seluruh baris data yang tersimpan di dalam tabel sekaligus.|Mengosongkan isi tabel secara total, meskipun struktur kolom tabel tetap utuh.|

### B. Mitigasi dan Best Practice Keamanan Data

- Sebagai praktik terbaik (_best practice_), pengguna disarankan untuk selalu menuliskan klausa `WHERE` terlebih dahulu sebelum mengeksekusi perintah manipulasi data (`UPDATE` dan `DELETE`).
- Melakukan verifikasi data dengan menjalankan kueri `SELECT` menggunakan klausa `WHERE` yang sama sebelum mengubahnya menjadi kueri `UPDATE` atau `DELETE` sangat disarankan guna menghindari kesalahan target data.

#### [Wawasan Diskusi / Audio Insight]

- Dosen memberikan peringatan keras (_what not to do_) dengan sengaja memberikan tanda komentar (_commented out_) pada klausa `WHERE` di skrip demonstrasi, sebagai peringatan visual bagi mahasiswa mengenai bahaya kelalaian kueri tanpa `WHERE`.
- Beberapa DBMS modern (seperti MySQL Workbench) secara default mengaktifkan fitur pengaman bernama _Safe Updates Mode_. Fitur ini secara otomatis memblokir eksekusi perintah `UPDATE` atau `DELETE` jika tidak menyertakan klausa `WHERE` yang merujuk pada kolom indeks atau kolom kunci (_Key_), untuk mencegah ketidaksengajaan modifikasi data berskala massal.



## Bab 7 Pengurutan Hasil Query (Sorting Result Sets)


## 7.1 Konsep Dasar Pengurutan Data dengan `ORDER BY`

### A. Pengenalan Klausa `ORDER BY`

- Klausa `ORDER BY` digunakan untuk mengurutkan kumpulan hasil (_result-set_) dari kueri data berdasarkan satu atau lebih kolom.
- Secara default, klausa `ORDER BY` akan mengurutkan data dari nilai terkecil ke terbesar (_ascending_).
- Untuk mengubah urutan dari terbesar ke terkecil (_descending_), kata kunci `DESC` ditambahkan secara eksplisit setelah nama kolom yang bersangkutan.

|Kata Kunci|Arah Pengurutan|Karakteristik Default|
|:--|:--|:--|
|`ASC`|Terkecil ke terbesar (_ascending_)|Merupakan arah pengurutan bawaan (_default_) jika tidak ditentukan secara eksplisit.|
|`DESC`|Terbesar ke terkecil (_descending_)|Harus dituliskan secara eksplisit setelah nama kolom.|

### B. Sintaksis Dasar `ORDER BY`

- Sintaksis penulisan query dasar untuk melakukan pengurutan adalah sebagai berikut:

```
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

#### [Wawasan Diskusi / Audio Insight]

- Secara lisan dijelaskan bahwa pengurutan data berbasis teks (string atau karakter) akan diurutkan secara alfabetis dari huruf A hingga Z secara otomatis.
- Penggunaan tanda petik (quotes) pada nama kolom dalam klausa `ORDER BY` sangat dilarang karena dapat mengacaukan logika pengurutan database (sistem memperlakukannya sebagai literal string biasa, bukan nama kolom fisik). Pastikan menulis nama kolom secara langsung tanpa tanda petik seperti `ORDER BY gnp DESC` agar query berjalan dengan benar.

## 7.2 Teknik Pengurutan Tingkat Lanjut (Multiple Columns)

### A. Pengurutan Berdasarkan Lebih dari Satu Kolom

- Database mendukung pengurutan baris data menggunakan kombinasi beberapa kolom sekaligus.
- Kolom pertama yang didefinisikan akan menjadi prioritas utama pengurutan. Kolom kedua dan berikutnya hanya akan dievaluasi jika terdapat nilai yang sama (_duplicate values_) pada kolom prioritas sebelumnya.

### B. Implementasi Query Multiple Columns

- Contoh kueri berikut mengurutkan baris data berdasarkan kode negara (`CountryCode`) secara _ascending_, dan jika terdapat kode negara yang sama, baris akan diurutkan kembali berdasarkan jumlah populasi (`Population`) dari yang terbesar ke terkecil (_descending_):

```
SELECT ID, Name, CountryCode, District, Population
FROM City
ORDER BY CountryCode ASC, Population DESC;
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen mengilustrasikan kasus pengurutan multi-kolom ini pada data kota dengan kode negara Afghanistan (`AFG`). Karena beberapa kota memiliki kode negara `AFG` yang identik, kolom populasi kemudian digunakan sebagai penentu urutan sekunder agar data populasi kota-kota di Afghanistan tersebut tersusun rapi dari populasi terbesar ke terkecil.

## 7.3 Kombinasi `ORDER BY` dan `LIMIT` (Analisis Top-N dan Bottom-N)

### A. Pengambilan Data Teratas (_Top-N_)

- Analisis _Top-N_ digunakan untuk menyaring sejumlah baris tertentu yang memiliki nilai tertinggi di dalam database.
- Hal ini dicapai dengan mengurutkan kolom target secara menurun (`DESC`), kemudian membatasi jumlah baris yang ditampilkan menggunakan klausa `LIMIT`.

```
SELECT Name, Population AS populasi
FROM country
ORDER BY Population DESC
LIMIT 5;
```

### B. Pengambilan Data Terbawah (_Bottom-N_)

- Sebaliknya, analisis _Bottom-N_ ditujukan untuk menyaring sejumlah baris dengan nilai terendah.
- Pengambilan data dilakukan dengan mengurutkan kolom secara menaik (`ASC` atau default), lalu memotong baris keluaran menggunakan klausa `LIMIT`.

```
SELECT Name, Population
FROM country
ORDER BY Population ASC
LIMIT 5;
```

#### [Wawasan Diskusi / Audio Insight]

- Di dalam sesi tanya jawab latihan praktis, mahasiswa mendemonstrasikan penyelesaian kueri untuk menampilkan 5 negara dengan populasi terbesar di dunia menggunakan database latihan `world`.
- Kueri tersebut disusun secara efisien dalam satu baris maupun terpisah demi keterbacaan: mengurutkan kolom `Population` secara descending, lalu menempatkan klausa `LIMIT 5` di baris paling akhir dari kueri. Hasil eksekusi kueri ini menampilkan lima negara teratas secara berurutan: Cina, India, Amerika Serikat, Indonesia, dan Brasil.



## Bab 8 Fungsi Bawaan Database (Built-in Database Functions)


## 8.1 Klasifikasi Fungsi Bawaan Database

### A. Definisi dan Peran Fungsi Bawaan

- Database secara umum dilengkapi dengan built-in function (fungsi bawaan) yang dapat dimasukkan secara langsung ke dalam pernyataan SQL.
- Penggunaan fungsi ini secara signifikan mengurangi jumlah data yang perlu diekstraksi dari server, sehingga mempercepat proses pengolahan data.
- Fungsi bawaan SQL dikelompokkan menjadi dua kategori utama berdasarkan cakupan kerjanya:
    - **Aggregate Functions (Fungsi Agregat):** Beroperasi pada sekumpulan nilai (_collection of values_) atau satu kolom secara keseluruhan untuk menghasilkan nilai tunggal (_single value_).
    - **Scalar Functions (Fungsi Skalar):** Beroperasi pada setiap nilai individual (_every individual value_) di baris data secara mandiri.

|Jenis Fungsi|Karakteristik Utama|Contoh Fungsi|
|:--|:--|:--|
|Aggregate Function|Beroperasi pada sekumpulan nilai/kolom, menghasilkan satu nilai tunggal.|SUM, COUNT, AVG, MIN, MAX|
|Scalar Function|Beroperasi secara independen pada setiap nilai baris data individual.|ROUND, LENGTH, UCASE, LCASE|

#### [Wawasan Diskusi / Audio Insight]

- Penggunaan fungsi agregat sangat krusial dalam analisis data bisnis skala besar karena kalkulasi dilakukan langsung di sisi server database, bukan di sisi aplikasi klien, sehingga menghemat konsumsi memori dan bandwidth jaringan.

---

## 8.2 Fungsi Agregat Utama (Aggregate Functions)

### A. Fungsi SUM() dan COUNT()

- **SUM():** Menghitung total jumlah nilai numerik pada suatu kolom spesifik.
    - Sintaksis:
        
        ```
        SELECT SUM(column_name) FROM table_name WHERE condition;
        ```
        
    - Contoh praktis (menghitung total populasi di India):
        
        ```
        SELECT SUM(Population) AS Total_Population FROM City WHERE CountryCode = 'IND';
        ```
        
- **COUNT():** Mengembalikan jumlah baris data yang cocok dengan kriteria filter yang ditentukan.
    - Sintaksis:
        
        ```
        SELECT COUNT(column_name) FROM table_name WHERE condition;
        ```
        
    - Contoh praktis (menghitung jumlah kota di Indonesia):
        
        ```
        SELECT COUNT(Name) AS Total_City FROM City WHERE CountryCode = 'IDN';
        ```
        

### B. Fungsi AVG(), MIN(), dan MAX()

- **AVG():** Menghitung nilai rata-rata dari kolom bertipe numerik.
    - Sintaksis:
        
        ```
        SELECT AVG(column_name) FROM table_name WHERE condition;
        ```
        
    - Contoh praktis (menghitung rata-rata populasi kota di Indonesia):
        
        ```
        SELECT AVG(Population) AS Avg_Population FROM City WHERE CountryCode = 'IDN';
        ```
        
- **MIN():** Mengambil nilai terkecil/minimum dari kolom yang dipilih.
    - Sintaksis:
        
        ```
        SELECT MIN(column_name) FROM table_name WHERE condition;
        ```
        
    - Contoh praktis (mencari populasi kota terkecil di Indonesia):
        
        ```
        SELECT MIN(Population) AS Min_Population FROM City WHERE CountryCode = 'IDN';
        ```
        
- **MAX():** Mengambil nilai terbesar/maksimum dari kolom yang dipilih.
    - Sintaksis:
        
        ```
        SELECT MAX(column_name) FROM table_name WHERE condition;
        ```
        
    - Contoh praktis (mencari populasi kota terbesar di Indonesia):
        
        ```
        SELECT MAX(Population) AS Max_Population FROM City WHERE CountryCode = 'IDN';
        ```
        

|Fungsi Agregat|Deskripsi Teknis|Output|
|:--|:--|:--|
|SUM()|Menghitung akumulasi total nilai numerik dalam satu kolom.|Angka total|
|COUNT()|Menghitung jumlah baris yang memenuhi kondisi spesifik.|Angka bulat (jumlah baris)|
|AVG()|Menghitung rata-rata aritmatika dari nilai numerik kolom.|Angka desimal (rata-rata)|
|MIN()|Menemukan nilai paling rendah/kecil dalam kolom.|Nilai minimum|
|MAX()|Menemukan nilai paling tinggi/besar dalam kolom.|Nilai maksimum|

#### [Wawasan Diskusi / Audio Insight]

- Fungsi agregat mengabaikan nilai NULL dalam kalkulasinya (kecuali COUNT(*) yang menghitung seluruh baris termasuk baris kosong).
- Sesuai data lisan pada rekaman kuliah, rata-rata populasi kota di wilayah Indonesia (dengan filter CountryCode = 'IDN') adalah sekitar 441.008, dengan populasi kota terkecil bernilai 89.900 dan kota terbesar mencapai 9.604.900.

---

## 8.3 Fungsi Skalar Utama (Scalar Functions)

### A. Fungsi ROUND() dan LENGTH()

- **ROUND():** Membulatkan nilai numerik ke jumlah desimal tertentu.
    - Sintaksis:
        
        ```
        ROUND(number, decimals)
        ```
        
    - Parameter `number` wajib diisi (angka yang ingin dibulatkan), sedangkan parameter `decimals` bersifat opsional (jumlah angka di belakang koma. Jika diabaikan, maka nilai akan dibulatkan ke bilangan bulat terdekat tanpa desimal).
    - Contoh praktis (menghitung kepadatan populasi di Asia Tenggara dengan pembulatan 2 desimal):
        
        ```
        SELECT Name, Region, ROUND(Population/SurfaceArea, 2) AS Population_Density FROM Country WHERE Region = 'Southeast Asia';
        ```
        
- **LENGTH():** Mengembalikan panjang karakter dari suatu string/teks (dihitung dalam satuan bytes).
    - Sintaksis:
        
        ```
        LENGTH(string)
        ```
        
    - Contoh praktis (menghitung jumlah panjang karakter nama negara di Asia Tenggara dan diurutkan menurun):
        
        ```
        SELECT Name, LENGTH(Name) AS Length_Name FROM Country WHERE Region = 'Southeast Asia' ORDER BY Length_Name DESC;
        ```
        

### B. Fungsi Manipulasi Huruf (UCASE/UPPER dan LCASE/LOWER)

- **UCASE() / UPPER():** Mengonversi seluruh string teks menjadi huruf besar/kapital secara penuh.
    - Sintaksis:
        
        ```
        UCASE(text)
        ```
        
    - Contoh praktis:
        
        ```
        SELECT UCASE(Name), Population FROM Country WHERE Region = 'Southeast Asia';
        ```
        
- **LCASE() / LOWER():** Mengonversi seluruh string teks menjadi huruf kecil secara penuh.
    - Sintaksis:
        
        ```
        LCASE(text)
        ```
        
    - Contoh praktis:
        
        ```
        SELECT LCASE(Name), Population FROM Country WHERE Region = 'Southeast Asia';
        ```
        

|Fungsi Skalar|Parameter Wajib|Hasil Operasi|
|:--|:--|:--|
|ROUND()|Angka, [Jumlah Desimal]|Nilai angka yang sudah dibulatkan.|
|LENGTH()|Teks/String|Panjang string dalam satuan byte.|
|UCASE() / UPPER()|Teks/String|Teks dalam bentuk huruf kapital penuh.|
|LCASE() / LOWER()|Teks/String|Teks dalam bentuk huruf kecil penuh.|

#### [Wawasan Diskusi / Audio Insight]

- Fungsi skalar dapat dijalankan langsung di klausa `SELECT` untuk memformat tampilan data, atau di dalam klausa `WHERE` untuk melakukan penyaringan dinamis.
- Dari sesi tanya jawab kuliah, mahasiswa sempat mencoba menggunakan fungsi `LENGTH` dikombinasikan dengan `GROUP BY` dan `HAVING` secara keliru. Dosen menegaskan bahwa fungsi `LENGTH` adalah fungsi skalar, bukan fungsi agregat, sehingga penyaringan berdasarkan panjang karakter nama (contoh: mencari negara yang panjang namanya sama dengan 6) harus ditulis menggunakan klausa `WHERE` secara langsung, bukan klausa `HAVING`.
    - Contoh penulisan penyaringan yang benar untuk mencari nama negara dengan panjang 6 karakter dan berakhiran 'o':
        
        ```
        SELECT Name FROM Country WHERE LENGTH(Name) = 6 AND Name LIKE '%o';
        ```
        

---

## 8.4 Pengelompokan Data (GROUP BY)

### A. Konsep dan Mekanisme GROUP BY

- Klausa `GROUP BY` digunakan untuk mengelompokkan baris data yang memiliki nilai yang sama ke dalam baris rangkuman (_summary rows_), seperti "menghitung jumlah kota di setiap negara".
- Klausa ini sering kali digunakan bersama dengan fungsi agregat (`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`) untuk mengagregasi hasil set berdasarkan satu atau beberapa kolom.
- Urutan sintaksis standar SQL:
    
    ```
    SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) ORDER BY column_name(s);
    ```
    

### B. Demonstrasi Kasus GROUP BY

- **Kasus 1 (Menghitung jumlah kota untuk setiap kode negara):**
    
    ```
    SELECT COUNT(ID), CountryCode FROM City GROUP BY CountryCode;
    ```
    
- **Kasus 2 (Menghitung rata-rata populasi kota di setiap distrik di Indonesia):**
    
    ```
    SELECT AVG(Population), District FROM City WHERE CountryCode = 'IDN' GROUP BY District;
    ```
    
- **Kasus 3 (Menggabungkan GROUP BY dengan Alias `AS`):** Menggunakan `AS` untuk memberikan nama kolom baru yang lebih representatif pada hasil query agregasi.
    
    ```
    SELECT AVG(Population) AS Rata_rata, District AS Provinsi FROM City WHERE CountryCode = 'IDN' GROUP BY District;
    ```
    

#### [Wawasan Diskusi / Audio Insight]

- Klausa `GROUP BY` memecah data menjadi kelompok-kelompok kecil secara logis sebelum fungsi agregat dijalankan. Kolom yang ditulis di dalam klausa `SELECT` (non-agregat) harus dicantumkan pula secara konsisten pada klausa `GROUP BY` untuk mencegah terjadinya galat pembacaan skema data pada sistem DBMS.

---

## 8.5 Penyaringan Grup Data (HAVING)

### A. Definisi dan Sintaksis Klausa HAVING

- Klausa `HAVING` memiliki fungsi yang serupa dengan klausa `WHERE`, yaitu menyaring hasil set data. Namun, perbedaan mendasarnya adalah **`HAVING` digunakan khusus untuk menyaring hasil setelah proses pengelompokan (`GROUP BY`) dilakukan**.
- Urutan sintaksis lengkap yang menggabungkan seluruh klausa utama:
    
    ```
    SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) HAVING group_condition ORDER BY column_name(s);
    ```
    

### B. Contoh Implementasi HAVING

- **Kasus 1 (Menampilkan rata-rata populasi distrik di Indonesia yang nilainya di atas 500.000):** Kueri ini tidak dapat menggunakan `WHERE` untuk memfilter rata-rata karena nilai rata-rata baru dihitung setelah baris data dikelompokkan per distrik.
    
    ```
    SELECT AVG(Population) AS Rata_rata, District AS Provinsi
    FROM CITY
    WHERE CountryCode = 'IDN'
    GROUP BY District
    HAVING Rata_rata > 500000;
    ```
    
- **Kasus 2 (Menyaring kolom grup itu sendiri menggunakan HAVING):** Meskipun penyaringan nama provinsi sebaiknya diletakkan di `WHERE` demi efisiensi, `HAVING` juga mampu melakukan filter langsung pada kolom grup, misalnya mencari provinsi yang diawali dengan huruf 'K'.
    
    ```
    SELECT AVG(Population) AS Rata_rata, District AS Provinsi
    FROM CITY
    WHERE CountryCode = 'IDN'
    GROUP BY District
    HAVING Provinsi LIKE 'K%';
    ```
    

### C. Tabel Perbedaan Antara WHERE dan HAVING

Berikut adalah perbedaan mendasar dari kedua klausa filter tersebut secara terstruktur:

|Karakteristik|Klausa WHERE|Klausa HAVING|
|:--|:--|:--|
|**Tahap Eksekusi**|Dieksekusi sebelum baris data dikelompokkan (_before grouping_).|Dieksekusi setelah baris data dikelompokkan (_after grouping_).|
|**Fungsi Agregat**|Tidak dapat digunakan bersama fungsi agregat (misal: dilarang menulis `WHERE AVG(Population) > 100`).|Sangat kompatibel dan digunakan untuk menyaring fungsi agregat (misal: `HAVING Rata_rata > 500000`).|
|**Objek Penyaringan**|Menyaring baris data individual secara langsung dari tabel fisik.|Menyaring kelompok/grup data hasil ringkasan agregasi.|

#### [Wawasan Diskusi / Audio Insight]

- Dari tanya jawab kuliah, ketika mahasiswa menanyakan perbedaan mendasar antara `HAVING` dan `WHERE`, dosen memberikan penjelasan sebagai berikut:
    - `WHERE` diletakkan **sebelum** `GROUP BY` untuk menyaring baris-baris data dari tabel asal terlebih dahulu. Hanya baris yang lolos penyaringan `WHERE` yang akan masuk ke tahap pengelompokan.
    - `HAVING` diletakkan **setelah** `GROUP BY` untuk menyaring kelompok-kelompok data yang sudah terbentuk berdasarkan hasil perhitungan agregasi.
    - Penggunaan `WHERE` jauh lebih efisien untuk kolom non-agregat karena membatasi jumlah data yang diproses sejak awal, sementara `HAVING` ideal digunakan ketika kriteria filter melibatkan hasil perhitungan fungsi agregat seperti `SUM()`, `AVG()`, atau `COUNT()`.



## Bab 9 Fungsi Terkait Tanggal dan Waktu (Date and Time Functions)


## 9.1 Format Penyimpanan Tanggal dan Waktu Standar

### A. Tipe Data dan Format Standar

- Sistem database memiliki tipe data khusus yang dirancang untuk menyimpan informasi tanggal (date) dan waktu (time) secara presisi.
- Format standar penyimpanan data tanggal dan waktu meliputi:
    - **DATE**: Disimpan menggunakan format `YYYYMMDD` (Tahun-Bulan-Hari).
    - **TIME**: Disimpan menggunakan format `HHMMSS` (Jam-Menit-Detik).
    - **TIMESTAMP**: Disimpan menggunakan format `YYYYXXDDHHMMSSZZZZZZ` yang mencakup komponen tanggal, waktu, hingga mikrodetik atau zona waktu.

|Tipe Data|Format Standar|Deskripsi|
|:--|:--|:--|
|DATE|YYYYMMDD|Menyimpan data tanggal tanpa komponen waktu.|
|TIME|HHMMSS|Menyimpan data waktu (jam, menit, detik) secara mandiri.|
|TIMESTAMP|YYYYXXDDHHMMSSZZZZZZ|Menyimpan data kombinasi tanggal dan waktu yang sangat detail.|

#### [Wawasan Diskusi / Audio Insight]

- Database menggunakan tipe data khusus ini agar operasi penyaringan, pengurutan, dan manipulasi waktu dapat dilakukan secara efisien.
- Representasi data waktu dalam format standar memudahkan integrasi data lintas platform tanpa risiko salah interpretasi zona waktu atau penulisan tanggal.

## 9.2 Fungsi Ekstraksi Komponen Tanggal dan Waktu

### A. Ekstraksi Nilai Numerik

- Fungsi bawaan ekstraksi digunakan untuk mengambil satu komponen numerik spesifik dari suatu kolom tanggal atau waktu.
    
- Daftar fungsi ekstraksi numerik yang didukung:
    
    - `YEAR()`: Mengekstrak komponen tahun dalam bentuk angka integer.
    - `MONTH()`: Mengekstrak komponen bulan (1 hingga 12).
    - `DAY()` atau `DAYOFMONTH()`: Mengekstrak komponen hari dalam bulan (1 hingga 31).
    - `DAYOFWEEK()`: Mengekstrak indeks hari dalam seminggu.
    - `DAYOFYEAR()`: Mengekstrak urutan hari dalam setahun (1 hingga 366).
    - `WEEK()`: Mengekstrak urutan minggu dalam setahun.
    - `HOUR()`: Mengekstrak komponen jam (0 hingga 23).
    - `MINUTE()`: Mengekstrak komponen menit (0 hingga 59).
    - `SECOND()`: Mengekstrak komponen detik (0 hingga 59).
- **Contoh Kasus Penggunaan `YEAR()`:** Menghitung rata-rata nilai transaksi harian per tahun dari tabel pembayaran (`payment`):
    
    ```
    SELECT YEAR(payment_date) AS Year_Sales, AVG(amount) AS Total_Amount_Yearly
    FROM PAYMENT
    GROUP BY Year_Sales;
    ```
    
- **Contoh Kasus Penggunaan `DAY()`:** Menampilkan ID pelanggan dan komponen hari pembayaran dari tabel `payment` untuk transaksi dengan nilai di atas US$ 11:
    
    ```
    SELECT Customer_id, DAY(payment_date)
    FROM PAYMENT
    WHERE amount > 11;
    ```
    

|Fungsi|Tipe Output|Deskripsi Kegunaan|
|:--|:--|:--|
|YEAR(date)|Integer|Mengambil angka tahun dari tanggal.|
|MONTH(date)|Integer|Mengambil angka bulan (1-12) dari tanggal.|
|DAY(date)|Integer|Mengambil angka hari (1-31) dari tanggal.|
|HOUR(time)|Integer|Mengambil angka jam dari kolom waktu/timestamp.|

#### [Wawasan Diskusi / Audio Insight]

- Komponen tanggal yang diekstrak menggunakan fungsi seperti `YEAR()` akan menghasilkan nilai bertipe integer (angka bulat). Hal ini memungkinkan data hasil ekstraksi langsung dikelompokkan menggunakan klausa `GROUP BY` untuk kepentingan analisis tren tahunan atau bulanan.
- Indentasi dalam kueri SQL bersifat opsional (tidak wajib seperti Python), namun sangat dianjurkan untuk mempermudah pembacaan baris instruksi `SELECT`, `FROM`, `WHERE`, dan `GROUP BY`.

## 9.3 Fungsi Representasi Teks (Nama Hari dan Bulan)

### A. Konversi Tanggal ke Nama

- Database menyediakan fungsi khusus untuk memformat komponen tanggal menjadi nama tekstual dalam bahasa Inggris:
    
    - `DAYNAME()`: Mengonversi nilai tanggal menjadi nama hari dalam seminggu (seperti _Monday_, _Tuesday_, _Wednesday_, _Thursday_, _Friday_, _Saturday_, _Sunday_).
    - `MONTHNAME()`: Mengonversi nilai tanggal menjadi nama bulan dalam setahun (seperti _January_, _February_, _March_, _April_, _May_, _June_, _July_, _August_, _September_, _October_, _November_, _December_).
- **Contoh Kasus Penggunaan `DAYNAME()`:** Menghitung rata-rata nilai transaksi berdasarkan nama hari pembayaran dan mengurutkannya dari yang terkecil:
    
    ```
    SELECT AVG(amount) AS Average_Amount, DAYNAME(payment_date) AS Day
    FROM PAYMENT
    GROUP BY DAYNAME(payment_date)
    ORDER BY Average_Amount;
    ```
    
- **Contoh Kasus Penggunaan `MONTHNAME()`:** Menghitung rata-rata nilai transaksi berdasarkan nama bulan pembayaran dari tabel `payment`:
    
    ```
    SELECT AVG(amount) AS Average_Amount, MONTHNAME(payment_date) AS Month_Name
    FROM PAYMENT
    GROUP BY Month_Name
    ORDER BY Average_Amount;
    ```
    

|Fungsi|Contoh Output|Deskripsi Kegunaan|
|:--|:--|:--|
|DAYNAME(date)|'Saturday', 'Monday'|Mengonversi tanggal ke representasi teks nama hari.|
|MONTHNAME(date)|'August', 'February'|Mengonversi tanggal ke representasi teks nama bulan.|

#### [Wawasan Diskusi / Audio Insight]

- Fungsi representasi teks sangat bermanfaat ketika menyajikan data kepada pihak manajerial atau direktur, karena format nama hari (seperti _Saturday_) jauh lebih mudah dipahami secara visual dibandingkan representasi angka indeks hari.

## 9.4 Aritmatika Tanggal (Date Arithmetic)

### A. Operasi Penjumlahan dan Pengurangan Tanggal

- Aritmatika tanggal (_Date Arithmetic_) merupakan proses melakukan operasi matematika langsung (penambahan atau pengurangan) terhadap nilai tanggal untuk menghasilkan tanggal baru.
    
- Penambahan nilai integer pada objek tanggal secara otomatis akan menggeser tanggal tersebut ke beberapa hari ke depan.
    
- **Contoh Kasus Penjumlahan Tanggal:** Menampilkan nama hari satu hari setelah tanggal pembayaran asli (`One_Day_After_Payment`) pada tabel `payment` untuk transaksi yang diproses oleh staf dengan ID 1 dan nilai transaksi di atas US$ 11:

    ```
    SELECT Customer_id, Amount, DAYNAME(DATE(payment_date) + 1) AS One_Day_After_Payment
    FROM PAYMENT
    WHERE staff_id = 1 AND amount > 11;
    ```
    

|Operasi|Contoh Sintaksis|Hasil Fungsional|
|:--|:--|:--|
|Penambahan Tanggal|`DATE(payment_date) + 1`|Menghasilkan tanggal baru yang bergeser 1 hari ke depan.|

#### [Wawasan Diskusi / Audio Insight]

- Operasi aritmatika tanggal dapat dilakukan dengan mengonversi kolom waktu/timestamp ke tipe data tanggal murni terlebih dahulu menggunakan fungsi `DATE(payment_date)`, baru kemudian ditambahkan nilai numerik integer (misalnya `+ 1` untuk bergeser ke hari berikutnya).
- Perlu diperhatikan batasan dalam operasi aritmatika sederhana ini agar tidak terjadi _overflow_ jika nilai penambah hari terlalu besar di luar batasan penanganan memori tipe datanya.



## Lecture Notes session 9 Module 1

1. Create Database. 
	1. Pertama, buka klik kanan di localhost pada panel kiri layar, kemudian SQL Editor, New SQL Script. 
	2. Rename script menjadi Database_and_SQL_intro.sql.
	3. Paste `SHOW DATABASES;` kemudian play untuk melihah database apa saja yang sudah ada. 
	4. Tiban dengan `CREATE DATABASE demo_scratch;` untuk buat database bau.
	5. Kemudian refresh, locachost di panel kiri layar, nanti akan muncul demo_scratch.
	6. Kemudian belajar untuk menghapus database dengan `DROP DATABASE demo_scratch;` kemudian, play dan refresh panel localhost. Databahse tsb akan hilang. 
	7. Sekarang bikin lagi database baru, namanya `CREATE DATABASE seller;`
	8. 

Having:
1. Mengolah data agregat atau hasil olahan

Where:
1. Menyaring data
LIKE:
2. mencocokan. 



---


# Module 1 Session 10 SQL Working With Multiple Tables


## Bab 1 Relational Model Constraints (Batasan Model Relasional)


## 1.1 Pengantar Batasan Data dalam Bisnis dan Konsep Referencing

### A. Fondasi Konseptual Batasan Data

- Dalam sistem bisnis, setiap data yang disimpan di dalam database relasional harus mematuhi batasan (_restrictions_) atau aturan (_rules_) tertentu yang berlaku di dunia nyata.
- Batasan ini berfungsi untuk menjaga integritas, akurasi, dan konsistensi data yang dikelola oleh sistem informasi perusahaan.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menerangkan bahwa batasan model relasional (_Relational Model Constraints_) merupakan aturan mutlak yang menjamin keandalan data. Ketika sistem beralih dari satu tabel ke skenario multi-tabel (_multiple tables_), batasan relasi ini menjadi fondasi utama agar tidak terjadi ketidaksinkronan data antar-tabel.

### B. Konsep Referencing

- _Referencing_ adalah konsep di mana suatu entitas dalam tabel relasional merujuk atau mengacu pada entitas di tabel lain untuk melengkapi informasi yang dibutuhkan.
- Contoh hubungan dunia nyata antara _Actress_ (Aktris) dan _Movie_ (Film):
    - Aturan bisnis menyatakan minimal satu aktris bermain dalam satu film (hubungan _One-to-One_).
    - Untuk mencari rincian informasi aktris, entitas _Movie_ akan merujuk (_refer_) ke entitas _Actress_.
    - Sebaliknya, untuk melacak film yang dibintangi aktris tersebut, entitas _Actress_ merujuk ke entitas _Movie_.

#### [Wawasan Diskusi / Audio Insight]

- Dosen mencontohkan secara konkret menggunakan film "Odyssey" dengan aktor utama "Matt Damon". Informasi film tersebut tercatat dalam tabel `movie`, namun rincian data diri Matt Damon seperti kewarganegaraan atau nilai aset bersih (_network_) disimpan di tabel aktor (`actress`/`actor`).
- Jika pengguna ingin mengetahui "berapa network value dari aktor utama film Odyssey", informasi tersebut tidak dapat diperoleh hanya dari satu tabel. Sistem harus melakukan pencarian silang melalui hubungan rujukan (_referencing_) dengan menghubungkan tabel `movie` dan tabel `actress`.

---

## 1.2 Primary Key dan Foreign Key

### A. Karakteristik Primary Key dan Foreign Key

- Untuk menghubungkan beberapa tabel, setiap tabel harus memiliki kunci pengidentifikasi yang jelas dan terstandarisasi.

Berikut adalah tabel karakteristik perbandingan antara _Primary Key_ dan _Foreign Key_ berdasarkan aturan model relasional:

|Karakteristik|Primary Key|Foreign Key|
|:--|:--|:--|
|**Definisi**|Kolom atau sekumpulan kolom yang secara unik mengidentifikasi setiap rekor/baris dalam sebuah tabel.|Kolom atau kumpulan kolom dalam suatu tabel yang merujuk pada _Primary Key_ di tabel lain.|
|**Keunikan Nilai**|Harus bernilai unik (_UNIQUE_); dilarang keras ada duplikasi nilai dalam satu tabel.|Nilainya tidak harus unik di tabel tempatnya berada; dapat menerima nilai yang berulang.|
|**Nilai Kosong**|Tidak boleh mengandung nilai kosong (_cannot contain NULL values_).|Secara umum dapat menerima nilai NULL jika aturan bisnis memperbolehkannya.|
|**Tujuan/Fungsi**|Mengidentifikasi baris data secara unik di tabel asal.|Menghubungkan atau mengaitkan (_link_) dua tabel secara logis.|

#### [Wawasan Diskusi / Audio Insight]

- Dosen memaparkan beberapa contoh pengidentifikasi unik (_identifier_) di dunia nyata yang bertindak sebagai _Primary Key_:
    - **Nomor Induk Kependudukan (NIK)**: Dalam database kependudukan Indonesia, NIK wajib bersifat unik dan tidak boleh kosong (_cannot contain NULL values_) karena mengidentifikasi setiap individu secara tunggal. Seseorang tidak boleh memiliki dua NIK, dan dua orang tidak boleh memiliki NIK yang sama.
    - **Nomor Polisi (Plat Kendaraan)**: Dalam database kepolisian atau Samsat, nomor polisi berfungsi sebagai _Primary Key_ yang mengidentifikasi setiap unit kendaraan secara unik.
- Untuk menjelaskan konsep _Foreign Key_, dosen menggunakan studi kasus relasi antara Penduduk dan Kendaraan:
    - Tabel `penduduk` memiliki _Primary Key_ berupa `NIK`.
    - Tabel `kendaraan` memiliki _Primary Key_ berupa `plat_nomor`.
    - Karena setiap kendaraan dimiliki oleh seorang penduduk, kolom `NIK` dimasukkan ke dalam tabel `kendaraan` sebagai kolom pemilik kendaraan. Di dalam tabel `kendaraan`, kolom `NIK` ini bertindak sebagai _Foreign Key_ yang merujuk ke _Primary Key_ `NIK` di tabel `penduduk`. Hubungan ini mendefinisikan relasi kata kerja kepemilikan (_memiliki_ atau _dimiliki_).

---

## 1.3 Representasi ERD (Entity Relationship Diagram) dalam Model Data Relasional

### A. Komponen Utama ERD

- _Entity Relationship Diagram_ (ERD) digunakan untuk menggambarkan skema database relasional secara visual.
- Dua komponen mendasar dari ERD adalah:
    - **Entity (Entitas)**: Representasi dari objek atau benda di dunia nyata yang ingin disimpan datanya (contoh: `departments`, `employees`). Entitas yang valid harus memiliki _Primary Key_ sendiri agar setiap baris datanya dapat diidentifikasi secara unik.
    - **Relation (Relasi)**: Hubungan antar-entitas yang divisualisasikan dengan garis penghubung, atau didefinisikan melalui tabel relasi perantara (_bridge/composite tables_).

### B. Jenis-Jenis Hubungan (Relationship)

Dalam model data relasional, hubungan antar-tabel dikelompokkan ke dalam beberapa jenis berikut:

- **One-to-One (Satu-ke-Satu)**: Hubungan di mana satu baris pada tabel pertama berpasangan dengan tepat satu baris pada tabel kedua (misalnya hubungan minimal aktris dan film).
- **One-to-Many (Satu-ke-Banyak)**: Hubungan di mana satu rekor di tabel induk berhubungan dengan banyak rekor di tabel dependen (contoh: satu karyawan dapat memiliki beberapa catatan riwayat gaji pada tabel `salaries`).
- **Many-to-Many (Banyak-ke-Banyak)**: Hubungan di mana banyak rekor di tabel pertama berhubungan dengan banyak rekor di tabel kedua (contoh: departemen memiliki banyak karyawan, dan karyawan dapat bekerja di beberapa departemen). Hubungan ini wajib dipecah menjadi tabel perantara (_bridge table_).

### C. Composite Primary Key (Kunci Utama Komposit)

- _Composite Primary Key_ merupakan _Primary Key_ yang dibentuk dari kombinasi dua atau lebih kolom di dalam satu tabel demi menjamin keunikan rekor. Hal ini umum diterapkan pada tabel transaksi atau tabel riwayat (_history_).

#### [Wawasan Diskusi / Audio Insight]

- Dosen mengoreksi ketidakakuratan konseptual dalam diagram ERD contoh yang ada pada slide modul:
    - Pada diagram slide, tabel `salaries` dan `titles` digambarkan hanya menggunakan `employee_number` as _Primary Key_.
    - Dosen menjelaskan bahwa rancangan ini salah secara konseptual karena dalam tabel riwayat, `employee_number` pasti akan berulang (duplikat) seiring bertambahnya riwayat gaji bulanan atau perubahan jabatan karyawan bersangkutan.
    - Solusi yang tepat adalah menerapkan _Composite Primary Key_. Untuk tabel `salaries`, keunikan baris harus dijamin dengan menggabungkan kolom `employee_number` dan kolom tanggal mulai `from_date`. Dengan kombinasi ini, database dapat melacak perubahan riwayat tanpa melanggar batasan keunikan kunci.

---

## 1.4 Terminologi Tabel Relasional: Parent Table dan Dependent Table

### A. Peran Tabel dalam Relasi

Dalam struktur database relasional, tabel yang saling terhubung dikategorikan menjadi dua jenis berdasarkan kepemilikan kunci relasionalnya:

- **Parent Table (Tabel Induk)**: Tabel yang menampung _Primary Key_ yang dirujuk oleh tabel lain. Tabel ini bersifat independen dan menyediakan data acuan.
- **Dependent Table (Tabel Dependen)**: Tabel yang menampung satu atau beberapa _Foreign Key_ yang merujuk pada tabel induk. Tabel ini bergantung pada eksistensi data yang ada di tabel induk.

Tabel perbandingan di bawah ini memperjelas perbedaan peran kedua jenis tabel tersebut:

|Karakteristik|Parent Table|Dependent Table|
|:--|:--|:--|
|**Kepemilikan Kunci**|Menyimpan _Primary Key_ utama yang menjadi target rujukan.|Menyimpan _Foreign Key_ yang merujuk ke tabel lain.|
|**Ketergantungan Data**|Independen; data dapat dimasukkan tanpa bergantung pada tabel lain.|Dependen; data _Foreign Key_ yang dimasukkan wajib eksis di tabel induk.|
|**Contoh Kasus**|`employees` (tabel karyawan) dan `departments` (tabel departemen).|`dept_emp` atau `dept_manager` (tabel relasi penugasan departemen yang menampung referensi ID karyawan dan ID departemen).|



## Bab 2 Implicit JOIN (JOIN Implisit)

## 2.1 Karakteristik dan Sintaksis Dasar Implicit JOIN

### A. Fondasi Konseptual Implicit JOIN

- _Implicit JOIN_ adalah metode penggabungan tabel dalam SQL tanpa menggunakan kata kunci `JOIN` secara eksplisit.
- Penggabungan ini dilakukan dengan menentukan dua atau lebih tabel secara langsung di dalam klausul `FROM` dengan memisahkannya menggunakan tanda koma (`,`).

Berikut adalah tabel karakteristik dari _Implicit JOIN_:

|Karakteristik|Deskripsi|
|:--|:--|
|**Pemisah Tabel**|Menggunakan tanda koma (`,`) di klausul `FROM` untuk mendaftarkan tabel yang ingin digabungkan.|
|**Sintaksis Dasar**|Menghubungkan tabel secara implisit melalui klausul `WHERE`.|
|**Keterbacaan**|Sederhana untuk penggabungan dua tabel berskala kecil, namun rentan menimbulkan kesalahan jika jumlah tabel bertambah banyak.|

Contoh sintaksis dasar penggabungan implisit tanpa kriteria pembatas:

```
SELECT * FROM employees, salaries;
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menerangkan bahwa dalam penulisan query standar satu tabel, pengguna umumnya menuliskan klausul `FROM` diikuti oleh satu nama tabel saja (contoh: `SELECT * FROM nama_tabel`).
- Pada skenario multi-tabel menggunakan _Implicit JOIN_, database dipaksa untuk memproses beberapa tabel sekaligus hanya dengan menambahkan tanda koma di dalam klausul `FROM`.

---

## 2.2 Cartesian Join / Full Join (Cartesian Product)

### A. Konsep Cartesian Product

- Jika penggabungan tabel secara implisit dilakukan tanpa menentukan kondisi pembatas atau kriteria pencocokan baris di klausul `WHERE`, sistem akan menghasilkan _Cartesian Join_ atau _Full Join_ (dikenal juga sebagai _Cartesian Product_).
- Dalam kondisi ini, setiap baris data di tabel pertama akan digabungkan secara paksa dengan setiap baris data di tabel kedua.
- Hal ini menyebabkan pelipatgandaan jumlah baris secara ekstrem di mana total baris hasil akhir merupakan hasil perkalian dari jumlah baris tabel pertama dengan jumlah baris tabel kedua.
- Hasil akhir dari _Cartesian Product_ ini tidak valid secara logis karena menghubungkan baris-baris data yang sebenarnya tidak memiliki hubungan relasional asli di dunia nyata.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahaya dan ketidakakuratan logika dari _Cartesian Product_ dengan memberikan contoh konkret menggunakan database sampel "Sakila":
    - Tabel pelanggan (`customer`) memiliki total 599 baris data.
    - Tabel pembayaran (`payment`) memiliki total 16.044 baris data.
    - Jika query dijalankan dengan penggabungan implisit tanpa filter kriteria (`SELECT * FROM customer, payment;`), maka jumlah baris yang dihasilkan adalah perkalian ekstrem: 599 × 16.044, yang menghasilkan sekitar 9,6 juta baris data.
    - Eksekusi ini menghasilkan data sampah yang tidak berguna karena terdapat 598 kombinasi baris yang tidak berhubungan logis untuk setiap satu transaksi pembayaran yang ada.
- Dosen memaparkan contoh kasus kesalahan logika lainnya menggunakan tabel kota (`city`) dan tabel negara (`country`):
    - Ketika query dituliskan sebagai `SELECT * FROM city, country;` kemudian pengguna memfilter kota tertentu seperti Abu Dhabi menggunakan klausul `WHERE city = 'Abu Dhabi'`, baris kota Abu Dhabi tersebut akan dipetakan (_mapping_) secara salah ke seluruh baris negara yang terdaftar di database (seperti Afghanistan, Algeria, American Samoa, Angola, dan lain-lain).
    - Secara realitas dunia nyata, pemetaan ini salah fatal karena kota Abu Dhabi hanya boleh berpasangan dengan satu negara saja, yaitu United Arab Emirates (UAE).

---

## 2.3 Membatasi Hasil Cartesian Join Menggunakan Klausul WHERE

### A. Penerapan Kondisi Key Join

- Untuk mereduksi hasil _Cartesian Product_ dan mengembalikan data yang benar-benar berelasi logis, pengguna wajib menyertakan kondisi filter pencocokan kunci (_matching keys_ / _key join_) di dalam klausul `WHERE`.
- Operator perbandingan (`=`) digunakan untuk memastikan bahwa nilai kunci pengenal pada tabel pertama memiliki nilai yang sama persis dengan kunci rujukan pada tabel kedua.

Contoh sintaksis pembatasan hasil menggunakan klausul `WHERE`:

```
SELECT * FROM employees, salaries WHERE employees.emp_no = salaries.emp_no;
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menerangkan bahwa dengan menambahkan kondisi kesamaan kunci (`WHERE payment.customer_id = customer.customer_id`), hasil query pada tabel pelanggan dan pembayaran akan disaring secara tepat.
- Hasil pencarian menyusut dari 9,6 juta baris menjadi hanya 16.044 baris sesuai dengan jumlah riwayat pembayaran riil yang ada, karena sistem hanya menampilkan transaksi yang dicatat atas nama pelanggan yang bersangkutan.
- Pada contoh kasus kota Abu Dhabi, dosen mempraktikkan perbaikan query dengan menyertakan kolom penghubung `country_id` sebagai _key join_:

```
SELECT * FROM city, country WHERE city.country_id = country.country_id AND city = 'Abu Dhabi';
```

- Penambahan kondisi ini membuat query hanya mengembalikan satu baris data yang valid secara akurat, yaitu kota Abu Dhabi berpasangan dengan negara United Arab Emirates.
- Dosen menekankan bahwa pengguna wajib memahami struktur database terlebih dahulu sebelum menentukan kolom yang bertindak sebagai _key join_:
    - Penggabungan tabel `customer` dan `payment` harus menggunakan kolom `customer_id` (kolom `payment_id` tidak dapat digunakan karena tidak tersedia pada tabel `customer`).
    - Penggabungan tabel `address` dan `city` dihubungkan menggunakan kolom `city_id`.

---

## 2.4 Penggunaan Alias Tabel (Table Aliases)

### A. Penyederhanaan Kode SQL

- Menuliskan nama tabel secara lengkap secara berulang kali di dalam klausul `SELECT` maupun `WHERE` dapat membuat query menjadi terlalu panjang, rumit, dan rentan terhadap kesalahan penulisan (_typo_).
- SQL menyediakan fitur untuk mendefinisikan alias tabel yang lebih pendek (_shorter aliases_) dengan memberikan label satu huruf atau singkatan pendek di dalam klausul `FROM`.
- Label alias ini diletakkan langsung setelah nama tabel (penggunaan kata kunci `AS` bersifat opsional).
- Setelah alias didefinisikan, seluruh referensi kolom dari tabel tersebut di klausul `SELECT` dan `WHERE` harus menggunakan alias yang telah ditetapkan.

Contoh sintaksis penggunaan alias tabel:

```
SELECT * FROM employees E, salaries S WHERE E.emp_no = S.emp_no;
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menerangkan bahwa penamaan alias tabel seperti `customer C` atau `payment P` sangat mempermudah efisiensi penulisan kode.
- Dengan alias tersebut, ekspresi pencocokan kunci pada klausul `WHERE` yang semula panjang cukup ditulis dengan singkat: `WHERE C.customer_id = P.customer_id`.

---

## 2.5 Pemilihan Kolom Spesifik

### A. Efisiensi Pengambilan Data

- Penggunaan tanda bintang (`*`) sangat tidak disarankan dalam penulisan query multi-tabel karena akan menarik seluruh kolom dari semua tabel secara bersamaan, sehingga membebani memori dan kinerja jaringan database.
- Praktik terbaik (_best practices_) adalah melakukan pemilihan kolom secara spesifik (_specific columns_) di klausul `SELECT`.
- Nama kolom yang dipilih harus diawali dengan alias tabel atau nama tabel asal (dengan format `alias.nama_kolom`) untuk menghindari ambiguitas atau konflik ketika terdapat kolom dengan nama yang sama di antara tabel-tabel yang digabungkan.

Contoh sintaksis pemilihan kolom spesifik menggunakan alias:

```
SELECT E.first_name, E.last_name, S.salary FROM employees E, salaries S WHERE E.emp_no = S.emp_no;
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen mencontohkan query terarah untuk menampilkan informasi transaksi pelanggan dengan hanya mengambil kolom nama depan (`first_name`), nama belakang (`last_name`), nilai transaksi (`amount`), dan tanggal pembayaran (`payment_date`):

```
SELECT C.first_name, C.last_name, P.amount, P.payment_date
FROM customer C, payment P
WHERE C.customer_id = P.customer_id;
```

- Hasil dari query tersebut menyajikan data gabungan secara bersih dan teratur yang diurutkan secara otomatis berdasarkan tanggal transaksi pembayaran (`payment_date`) dari yang terawal.



## Bab 3 Explicit JOIN  dan JOIN Statement (JOIN Eksplisit)

## 3.1 Pengenalan Explicit JOIN dan Perbedaannya dengan Implicit JOIN

### A. Definisi dan Konsep Dasar

- _Explicit JOIN_ (atau biasa disebut _JOIN Statement_) adalah mekanisme penggabungan baris dari dua atau lebih tabel secara eksplisit menggunakan kata kunci (_keyword_) `JOIN` dan klausul pengait `ON` untuk mendefinisikan hubungan antar-kolom (_key join_).
- Berbeda dengan _Implicit JOIN_ yang menggabungkan tabel menggunakan tanda koma (`,`) pada klausul `FROM` dan menyaringnya di klausul `WHERE`, _Explicit JOIN_ memisahkan logika penggabungan tabel (_join logic_) secara terpisah dari logika pemfilteran data (_filter logic_).

|Karakteristik|Implicit JOIN|Explicit JOIN|
|:--|:--|:--|
|**Sintaksis Penggabungan**|Menggunakan tanda koma (`,`) pada klausul `FROM`.|Menggunakan keyword `JOIN` secara eksplisit antar-tabel.|
|**Penyelarasan Kolom Kunci (_Key Join_)**|Ditulis pada klausul `WHERE` bersama dengan filter baris biasa.|Ditulis secara khusus pada klausul `ON` setelah keyword `JOIN`.|
|**Keterbacaan (_Readability_)**|Sulit dibaca pada query kompleks karena logika join bercampur dengan filter data.|Jauh lebih terstruktur, rapi, dan mudah dipelihara (_maintainable_) seiring kompleksitas query bertambah.|

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa penggunaan _Explicit JOIN_ sangat direkomendasikan dalam praktik database profesional karena pemisahan yang jelas antara kolom kunci relasi (`ON`) dan kondisi filter data (`WHERE`).
- Ketika menulis kode, dosen juga menyarankan untuk membiasakan memberikan indentasi (seperti memberikan karakter tab atau baris baru di bawah klausul `SELECT`, `FROM`, `JOIN`, dan `ON`) agar query SQL lebih mudah dibaca dan dievaluasi oleh tim pengembang lain.

---

## 3.2 Jenis-Jenis Explicit JOIN: INNER JOIN, LEFT JOIN, dan RIGHT JOIN

### A. INNER JOIN (atau JOIN)

- Kata kunci `INNER JOIN` digunakan untuk mengambil baris-baris data yang memiliki nilai kecocokan (_matching values_) di kedua tabel yang dihubungkan.
- Jika suatu baris di tabel pertama tidak memiliki pasangan nilai yang cocok di tabel kedua, atau sebaliknya, maka baris data tersebut tidak akan ditampilkan dalam hasil query.
- Sintaks Dasar:

```
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

- Catatan Penulisan: Di dalam MySQL dan mayoritas sistem database relasional, menuliskan keyword `JOIN` saja tanpa kata `INNER` secara otomatis diartikan sebagai `INNER JOIN`.

#### [Wawasan Diskusi / Audio Insight]

- **Aturan Kolom Penghubung**: Menanggapi pertanyaan mahasiswa mengenai apakah kolom yang digunakan sebagai penghubung (_link_) harus selalu berupa _Primary Key_ di satu tabel dan _Foreign Key_ di tabel lainnya, dosen membenarkan hal tersebut. Secara konseptual, relasi antar-tabel dibangun dengan menghubungkan kunci utama (_Primary Key_) dari satu entitas ke kunci asing (_Foreign Key_) di entitas yang bergantung padanya agar integritas data terjaga.
- **Studi Kasus Multi-Tabel (3 Tabel)**: Dosen mendemonstrasikan penggabungan tiga tabel sekaligus dalam database _Sakila_ untuk melacak film yang sedang disewa.
    - Tabel `film` (alias `FM`) dihubungkan ke tabel jembatan `inventory` menggunakan kolom `film_id`.
    - Tabel `inventory` kemudian dihubungkan ke tabel `rental` menggunakan kolom `inventory_id`.
    - Proses pencarian ini hanya bisa dilakukan secara bertahap melalui relasi kunci yang berantai ini.

### B. LEFT (OUTER) JOIN

- Kata kunci `LEFT JOIN` (atau disebut `LEFT OUTER JOIN` di beberapa database) mengembalikan seluruh baris dari tabel sebelah kiri (tabel pertama/utama), beserta baris yang memiliki nilai cocok dari tabel sebelah kanan (tabel kedua).
- Jika tidak ada kecocokan baris di tabel sebelah kanan, maka kolom-kolom dari tabel sebelah kanan tersebut akan diisi dengan nilai kosong atau `NULL`.
- Sintaks Dasar:

```
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

#### [Wawasan Diskusi / Audio Insight]

- **Deteksi Data Tidak Berpasangan**: Dosen menjelaskan bahwa kegunaan utama dari `LEFT JOIN` adalah untuk mengidentifikasi data yang tidak memiliki pasangan relasi.
- Sebagai contoh, kita dapat menggunakan `LEFT JOIN` antara tabel `film` (kiri) dan tabel `inventory` (kanan) untuk mencari daftar film yang belum pernah masuk ke inventori toko (atau belum pernah disewa), di mana kolom inventori akan menghasilkan nilai `NULL`.
- Contoh lainnya adalah mengidentifikasi pelanggan (_customer_) baru yang terdaftar tetapi belum pernah melakukan transaksi pembayaran (_payment_), sehingga nilai pembayaran di sisi kanan bernilai `NULL`.

### C. RIGHT (OUTER) JOIN

- Kata kunci `RIGHT JOIN` (atau `RIGHT OUTER JOIN`) merupakan kebalikan dari `LEFT JOIN`. Perintah ini mengembalikan seluruh baris dari tabel sebelah kanan, beserta baris yang cocok dari tabel sebelah kiri.
- Jika tidak ada baris yang cocok di tabel sebelah kiri, maka kolom-kolom dari tabel kiri akan diisi dengan nilai `NULL`.
- Sintaks Dasar:

```
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen memaparkan bahwa setiap operasi `RIGHT JOIN` sebenarnya selalu dapat ditulis ulang (_rewritten_) menjadi bentuk `LEFT JOIN` hanya dengan membalik urutan penulisan tabelnya di dalam query.
- Sebagai contoh, kueri `inventory RIGHT JOIN film` menghasilkan keluaran yang sama persis dengan kueri `film LEFT JOIN inventory`. Dalam dunia industri, para pengembang umumnya lebih menyukai penggunaan `LEFT JOIN` karena arah pembacaan logika yang mengalir dari kiri ke kanan.
- Contoh visual yang ditunjukkan dosen adalah relasi antara `new_employees` dan `dept_info`. Dengan menggunakan `RIGHT JOIN`, kita dapat menampilkan semua daftar departemen yang ada di tabel kanan (`dept_info`) meskipun departemen tersebut belum memiliki satu pun karyawan dari tabel kiri (`new_employees`).

---

## 3.3 FULL (OUTER) JOIN dan Self JOIN

### A. FULL (OUTER) JOIN

- `FULL OUTER JOIN` digunakan untuk mengembalikan semua baris ketika terdapat kecocokan baik di tabel sebelah kiri maupun tabel sebelah kanan.
- Jika ada baris di tabel kiri yang tidak memiliki pasangan di tabel kanan, atau baris di tabel kanan yang tidak memiliki pasangan di tabel kiri, kolom dari sisi yang tidak cocok akan diisi dengan nilai `NULL`.

### B. Self JOIN

- _Self JOIN_ adalah operasi penggabungan suatu tabel dengan dirinya sendiri (_regular join to itself_).
- Karena tabel yang digabungkan sama, kita **wajib** memberikan alias yang berbeda untuk tabel tersebut (misalnya `T1` dan `T2`) pada klausul query agar database dapat membedakan peran masing-masing kolom.
- _Self JOIN_ dapat ditulis menggunakan gaya penggabungan implisit maupun eksplisit.

#### [Wawasan Diskusi / Audio Insight]

- **Pencarian Pasangan Data Unik**: Dosen menjelaskan bahwa _Self JOIN_ sangat berguna ketika kita ingin membandingkan baris-baris data dalam satu tabel yang sama berdasarkan kriteria tertentu.
- **Studi Kasus 1: Durasi Film yang Sama**:
    - Kita ingin mencari pasangan film berbeda yang memiliki durasi pemutaran (_length_) yang sama persis di dalam database _Sakila_.
    - Query ditulis dengan menghubungkan tabel `film T1` dengan `film T2` berdasarkan kesamaan kolom `length`, tetapi dibatasi agar tidak membandingkan baris yang sama dengan menggunakan operator tidak sama dengan (`<>` atau `!=`) pada kolom `film_id`.
    - Contoh kueri eksplisit:

```
SELECT T1.title, T2.title, T1.length
FROM film T1
JOIN film T2
ON T1.film_id <> T2.film_id AND T1.length = T2.length;
```

- **Studi Kasus 2: Tanggal Lahir Karyawan yang Sama**:
    - Kita ingin mencari karyawan berbeda yang memiliki tanggal lahir (_birth_date_) yang sama persis di dalam tabel `employees`.
    - Query ditulis dengan relasi:

```
SELECT T1.first_name, T1.last_name, T2.first_name, T2.last_name, T1.birth_date
FROM employees T1
JOIN employees T2
ON T1.emp_no <> T2.emp_no AND T1.birth_date = T2.birth_date;
```

- **Operator Tidak Sama Dengan**: Menjawab kebingungan mahasiswa mengenai arti simbol `<>` atau `!=` dalam query tersebut, dosen menjelaskan bahwa operator tersebut berarti "tidak sama dengan". Syarat ini mutlak dipasang agar database tidak menampilkan hasil redundan di mana suatu film atau karyawan berpasangan dengan dirinya sendiri.



## Bab 4 Mengakses Database Menggunakan Python (Python MySQL Connector)

## 4.1 Langkah Persiapan (Prerequisites) dan Virtual Environment

### A. Pengenalan Python MySQL Connector

- Python MySQL Connector merupakan library resmi yang memungkinkan program Python untuk berinteraksi, mengirimkan kueri, dan memanipulasi database MySQL secara langsung dari lingkungan Python.

### B. Langkah Instalasi Package

- Untuk mulai menggunakan konektor, package `mysql-connector-python` harus diinstal terlebih dahulu di dalam lingkungan terminal atau command prompt sistem operasi.
- Perintah instalasi standar menggunakan pip:

```
pip install mysql-connector-python
```

- Atau jika menggunakan installer Python spesifik pada sistem Windows:

```
python -m pip install mysql-connector-python
```

#### [Wawasan Diskusi / Audio Insight]

- **Penanganan Masalah Instalasi**: Dalam diskusi kelas, terdapat kasus di mana sistem operasi memblokir instalasi package global (misalnya ketika sistem Python dikelola oleh package manager seperti _UV_).
- Dosen mengonfirmasi bahwa jika menemui kendala perizinan sistem ini, pengguna dapat menginstal package tersebut dengan menambahkan flag `--break-system-packages` agar sistem mengizinkan instalasi library konektor dan pandas:

```
pip install mysql-connector-python --break-system-packages
```

- Namun, praktik terbaik yang direkomendasikan adalah menggunakan lingkungan virtual terisolasi (_Virtual Environment_) alih-alih memaksakan instalasi global pada sistem utama.

### C. Pengelolaan Lingkungan Kerja dengan Anaconda/Conda (Virtual Environment)

- Manajemen lingkungan (_Environment Management_) sangat penting saat mengelola beberapa proyek pemrograman yang berbeda.
- Penggunaan Conda memungkinkan pembuatan lingkungan virtual terisolasi sehingga dependensi library antar-proyek tidak saling bertabrakan.
- Langkah-langkah pembuatan dan aktivasi lingkungan kerja di terminal:
    1. Membuat environment baru (contoh nama: `Purwadika`) dengan versi Python tertentu (misal versi 3.11):

```
conda create -n Purwadika python=3.11
```

2. Mengaktifkan lingkungan kerja yang baru dibuat:

```
conda activate Purwadika
```

3. Melakukan instalasi seluruh library pendukung yang dibutuhkan di dalam environment tersebut:

```
pip install mysql-connector-python pandas python-dotenv
```

#### [Wawasan Diskusi / Audio Insight]

- **Pentingnya Isolasi Environment**: Dosen menerangkan mengapa pembuatan environment baru sangat direkomendasikan. Jika seorang programmer bekerja pada lima proyek berbeda, satu proyek mungkin membutuhkan modul Pandas versi lama sementara proyek lainnya membutuhkan Pandas versi terbaru. Jika diinstal secara global, perubahan versi untuk proyek terbaru akan merusak kode pada proyek lama. Dengan Conda environment, dependensi setiap proyek disimpan terpisah dan aman.
- **Konfigurasi VSCode Interpreter**: Setelah membuat environment di terminal, pengguna harus menyinkronkan VSCode agar menggunakan interpreter dari environment yang tepat. Caranya dengan mengklik menu pilihan interpreter di pojok kanan bawah editor VSCode (Select Python Interpreter) dan memilih `Purwadika`. Jika pilihan tersebut belum muncul di menu, dosen menyarankan untuk menutup (_close_) VSCode terlebih dahulu dan membukanya kembali agar daftar interpreter ter-refresh secara otomatis.

---

## 4.2 Pembuatan Koneksi dan Eksekusi Query

### A. Membangun Koneksi Database

- Setelah mengaktifkan environment dan menginstal modul konektor, langkah awal di dalam script Python adalah mengimpor modul `mysql.connector`.
- Koneksi ke database MySQL dibangun menggunakan metode `mysql.connector.connect()` dengan menyertakan parameter kredensial yang sesuai.

Sintaks penulisan impor library dan pembuatan koneksi dasar:

```
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='YourPassword',
    database='world'
)
```

Berikut adalah tabel parameter kredensial yang digunakan dalam metode koneksi:

|Parameter|Tipe Data|Deskripsi / Fungsi|
|:--|:--|:--|
|`host`|String|Alamat server database berada (contoh: `'localhost'` jika database di komputer lokal).|
|`user`|String|Nama pengguna database yang sah (contoh: `'root'` atau nama pengguna kustom).|
|`passwd` atau `password`|String|Kata sandi rahasia untuk masuk ke server database MySQL.|
|`database`|String|Nama skema database spesifik yang ingin diakses (contoh: `'world'` atau `'sakila'`).|

### B. Eksekusi Query Menggunakan Kursor (Method 1)

- Untuk mengirim perintah SQL dari Python ke MySQL server, program membutuhkan objek perantara bernama kursor (_cursor_).
- Langkah eksekusi query standar terdiri dari membuat kursor, menjalankan query, dan mengambil seluruh baris data menggunakan metode `fetchall()`.
- Untuk memudahkan analisis, hasil pengambilan data (_fetch_) diubah ke dalam bentuk struktur tabel Pandas DataFrame.

Sintaks eksekusi query standar (Metode Pertama):

```
# Membuat akses ke database menggunakan cursor
mycursor = mydb.cursor()

# Menulis query SQL
query = 'select * from city'

# Mengeksekusi query di server database
mycursor.execute(query)

# Menyimpan seluruh baris hasil ke dalam variabel
result = mycursor.fetchall()

# Mengubah data hasil ke bentuk Pandas DataFrame
df = pd.DataFrame(result, columns=mycursor.column_names)

# Menampilkan 5 baris pertama data
df.head(5)
```

---

## 4.3 Optimasi Query dengan Fungsi Kustom dan Keamanan Kredensial

### A. Pembuatan Fungsi SQL DataFrame Kustom (Method 2)

- Menuliskan kode pembuatan kursor dan penarikan data secara berulang kali sangat tidak efisien jika kueri database dilakukan berkali-kali.
- Praktik terbaik untuk mengatasi hal ini adalah membuat fungsi pembungkus (_wrapper function_) kustom yang langsung menerima parameter query SQL dan mengembalikan objek Pandas DataFrame secara otomatis.

Sintaks pembuatan dan penggunaan fungsi kustom:

```
# Membuat fungsi pembungkus kustom
def sql_df(yourQuery):
    mycursor = mydb.cursor()
    mycursor.execute(yourQuery)
    myresult = mycursor.fetchall()
    df = pd.DataFrame(myresult, columns=mycursor.column_names)
    return df

# Melakukan pengujian kueri database menggunakan fungsi
sql_df('''
    select * from city limit 5
''')
```

### B. Penerapan Keamanan Kredensial Menggunakan .env (Dotenv)

- Menyimpan password database secara langsung dalam bentuk teks biasa (_hardcoded password_) di dalam file script Python sangat dilarang karena berisiko terekspos ketika kode diunggah ke repository publik seperti GitHub.
- Keamanan kredensial dikelola menggunakan file konfigurasi lingkungan bernama `.env`.

#### [Wawasan Diskusi / Audio Insight]

- **Penggunaan File `.env` dan `.gitignore`**: Dosen menjelaskan bahwa file `.env` asli berisi data sensitif yang tidak boleh diunggah ke repository publik, sehingga file tersebut harus dimasukkan ke dalam daftar `.gitignore`.
- Sebagai gantinya, dosen menyediakan file duplikat bernama `.env.copy` atau `env_copy` sebagai template. Template ini berisi kerangka variabel tanpa password asli yang berfungsi sebagai panduan bagi mahasiswa untuk menyalinnya menjadi file `.env` mandiri di komputer masing-masing.
- Mahasiswa menyalin template tersebut dan mengedit isinya menggunakan kredensial database pribadi mereka:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=password_pribadi_anda
```

- Di dalam script Python, variabel rahasia ini dimuat menggunakan library `python-dotenv` dan modul `os` untuk mengamankan koneksi database:

```
import os
from dotenv import load_dotenv
import mysql.connector

# Memuat file environment .env
load_dotenv()

# Mengambil variabel kredensial aman dari environment
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASSWORD')

# Menghubungkan menggunakan kredensial aman
mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    passwd=db_pass,
    database='sakila'
)
```



## Bab 5 Sesi Latihan & Pembahasan (SQL Exercise - Database Sakila)


## 5.1 Pengantar Latihan Praktis Database Sakila

### A. Petunjuk dan Persiapan Latihan

- Latihan praktis ini menggunakan database sampel standar industri bernama **"Sakila"**, yang merepresentasikan sistem operasional bisnis penyewaan film (_movie rental_).
- Pengerjaan instruksi SQL dapat dilakukan langsung menggunakan aplikasi klien basis data seperti **MySQL Workbench**, **DBeaver**, maupun secara terprogram lewat Jupyter Notebook/Jupyterlab menggunakan modul Python SQL Connector.
- Aktivitas penarikan data difokuskan pada manipulasi tabel tunggal, penggabungan multi-tabel (_multi-table join_), operasi agregasi, pemfilteran pola string menggunakan operator `LIKE`, hingga penggunaan kueri bersarang (_subquery_).

#### [Wawasan Diskusi / Audio Insight]

- Dosen mengingatkan mahasiswa untuk melakukan pembaharuan kode (_git pull_) terlebih dahulu pada repositori lokal masing-masing guna memastikan bahan latihan dan skema database "Sakila" serta "World" versi terbaru sudah tersinkronisasi sebelum sesi latihan dimulai.
- Jika mahasiswa menggunakan Jupyterlab, dosen menyarankan untuk mengaktifkan _Virtual Environment_ yang telah dibuat sebelumnya agar library konektor dapat dipanggil tanpa hambatan dependensi.

---

## 5.2 Pembahasan Soal 1 s.d. 5: Kueri Dasar, Pemfilteran, dan Agregasi

### A. Nomor 1: Pemilihan Kolom dan Pembatasan Baris (Tabel payment)

- **Tujuan**: Menampilkan 10 baris data pertama dari tabel `payment` dengan memilih kolom `customer_id`, `rental_id`, `amount`, dan `payment_date`.
- **Formulasi Query**:

```
SELECT customer_id, rental_id, amount, payment_date
FROM payment
LIMIT 10;
```

- **Analisis Teknis**: Langkah ini menggunakan perintah proyeksi kolom secara spesifik guna menghemat memori transfer data dibandingkan menggunakan tanda bintang (`*`), serta membatasi baris hasil kueri tepat sebanyak 10 baris teratas menggunakan klausul `LIMIT`.

### B. Nomor 2: Pemfilteran Teks Menggunakan Wildcard (Tabel film)

- **Tujuan**: Menampilkan 10 judul film (`title`), tahun rilis (`release_year`), dan durasi sewa (`rental_duration`) yang judulnya diawali dengan huruf "S".
- **Formulasi Query**:

```
SELECT title, release_year, rental_duration
FROM film
WHERE title LIKE 'S%'
LIMIT 10;
```

- **Analisis Teknis**: Karakter `%` pada klausa `LIKE 'S%'` bertindak sebagai _wildcard_ yang mewakili karakter apa pun setelah huruf "S" di awal teks.

### C. Nomor 3: Pengelompokan Data dan Pembulatan Nilai Rata-Rata (Tabel film)

- **Tujuan**: Mengelompokkan data berdasarkan durasi rental (`rental_duration`) untuk menampilkan nilai durasi sewa, jumlah film di setiap kelompok, serta rata-rata panjang film (`length`) dengan pembulatan 2 angka desimal. Judul kolom diubah menggunakan alias bahasa Indonesia.
- **Formulasi Query**:

```
SELECT
    rental_duration AS durasi_rental,
    COUNT(*) AS banyak_film,
    ROUND(AVG(length), 2) AS rata_rata_durasi_film
FROM film
GROUP BY rental_duration;
```

- **Analisis Teknis**: Fungsi agregasi `COUNT(*)` menghitung total baris per kelompok, sedangkan `AVG(length)` menghitung nilai rata-rata yang kemudian dibulatkan menggunakan fungsi `ROUND(..., 2)`.

#### [Wawasan Diskusi / Audio Insight]

- Dosen memberikan masukan penting mengenai estetika penulisan kueri. Sangat disarankan untuk menerapkan indentasi yang konsisten (seperti menjorokkan kolom di bawah klausa `SELECT` atau menaruh klausa `FROM` dan `GROUP BY` pada baris baru) demi meningkatkan keterbacaan (_readability_) kueri SQL oleh anggota tim pengembang lainnya.

### D. Nomor 4: Pemfilteran Kondisional di Atas Rata-Rata (Tabel film)

- **Tujuan**: Menampilkan `title`, durasi film (`length`), dan `rating` yang durasinya lebih tinggi dari rata-rata durasi seluruh film dalam database. Hasil dibatasi 25 baris dan diurutkan dari durasi terlama.
- **Formulasi Query**:

```
SELECT title, length, rating
FROM film
WHERE length > (SELECT AVG(length) FROM film)
ORDER BY length DESC
LIMIT 25;
```

- **Analisis Teknis**: Kueri ini menggunakan _Scalar Subquery_ di dalam klausul `WHERE` untuk menghitung nilai rata-rata dinamis secara global terlebih dahulu sebelum digunakan sebagai pembanding baris demi baris pada tabel utama.

### E. Nomor 5: Agregasi Multi-Fungsi dengan Group By (Tabel film)

- **Tujuan**: Menampilkan ringkasan statistik per kategori `rating` film, mencakup biaya penggantian tertinggi (_Replacement Cost_), tarif sewa terendah (_Rental Rate_), dan rata-rata durasi film (`length`).
- **Formulasi Query**:

```
SELECT
    rating,
    MAX(replacement_cost) AS Replacement_Cost_Tertinggi,
    MIN(rental_rate) AS Rental_Rate_Terendah,
    AVG(length) AS Rata_Rata_Durasi
FROM film
GROUP BY rating;
```

Berikut adalah rangkuman karakteristik hasil kueri agregasi berdasarkan klasifikasi rating film:

|Kategori Rating|Replacement Cost Tertinggi|Rental Rate Terendah|Perkiraan Rata-Rata Durasi (Menit)|
|:--|:--|:--|:--|
|**G**|29.99|0.99|~111.05|
|**PG**|29.99|0.99|~112.01|
|**PG-13**|29.99|0.99|~120.44|
|**R**|29.99|0.99|~118.66|
|**NC-17**|29.99|0.99|~113.23|

---

## 5.3 Pembahasan Soal 6 s.d. 10: Join Multi-Tabel, Pengurutan Kompleks, dan Subquery

### A. Nomor 6: Penggabungan Dua Tabel dengan Kriteria Karakter Akhir

- **Tujuan**: Menampilkan 15 daftar film yang judulnya diakhiri dengan huruf "K", menyajikan kolom judul film, durasi, serta nama bahasanya.
- **Formulasi Query**:

```
SELECT
    F.title AS Judul,
    F.length AS Durasi,
    L.name AS Bahasa_Film
FROM film F
INNER JOIN language L
ON F.language_id = L.language_id
WHERE F.title LIKE '%K'
LIMIT 15;
```

- **Analisis Teknis**: Kolom `language_id` bertindak sebagai kunci relasi (_key join_) yang menghubungkan tabel `film` (sebagai _Foreign Key_) dengan tabel `language` (sebagai _Primary Key_). Kondisi `LIKE '%K'` memastikan hanya judul berakhiran "K" yang lolos filter.

### B. Nomor 7: Penggabungan Tiga Tabel Berantai

- **Tujuan**: Menampilkan judul film, nama depan aktor, dan nama belakang aktor khusus untuk aktor yang memiliki `actor_id = 14`.
- **Formulasi Query**:

```
SELECT
    F.title AS Judul_Film,
    A.first_name AS First_Name,
    A.last_name AS Last_Name
FROM film F
INNER JOIN film_actor FA ON F.film_id = FA.film_id
INNER JOIN actor A ON FA.actor_id = A.actor_id
WHERE A.actor_id = 14;
```

- **Analisis Teknis**: Karena tabel `film` dan `actor` tidak memiliki hubungan relasional langsung (hubungan _Many-to-Many_), kueri harus melakukan penggabungan berantai (_nested join_) melewati tabel perantara (_bridge table_) yaitu `film_actor`.

### C. Nomor 8: Pemfilteran Karakter Ganda dan Pengurutan Abjad (Tabel city)

- **Tujuan**: Menampilkan kota (`city`) dan `country_id` dari tabel `city` yang namanya mengandung huruf "d" di posisi mana pun dan wajib diakhiri dengan huruf "a". Hasil dibatasi 15 data dan diurutkan berdasarkan abjad kota.
- **Formulasi Query**:

```
SELECT city, country_id
FROM city
WHERE city LIKE '%d%a'
ORDER BY city ASC
LIMIT 15;
```

#### [Wawasan Diskusi / Audio Insight]

- Dalam diskusi kelas, dosen menjelaskan efisiensi penulisan filter string. Mahasiswa awalnya menggunakan dua klausa terpisah yaitu `city LIKE '%d%' AND city LIKE '%a'`. Dosen mengonfirmasi bahwa penulisan tersebut dapat disederhanakan dan dioptimalkan menjadi satu ekspresi pola tunggal yaitu `LIKE '%d%a'`, karena pola tersebut secara otomatis menjamin adanya huruf "d" di bagian tengah/awal teks dan diakhiri secara mutlak oleh huruf "a".

### D. Nomor 9: Agregasi Hasil Penggabungan Tiga Tabel

- **Tujuan**: Menampilkan nama kategori/genre film dan jumlah total film yang tergolong dalam setiap genre tersebut, diurutkan dari jumlah film paling sedikit (_ascending_).
- **Formulasi Query**:

```
SELECT
    C.name AS Genre,
    COUNT(FC.film_id) AS Banyak_Film
FROM category C
INNER JOIN film_category FC ON C.category_id = FC.category_id
INNER JOIN film F ON FC.film_id = F.film_id
GROUP BY C.name
ORDER BY Banyak_Film ASC;
```

- **Analisis Teknis**: Operasi ini menggabungkan tabel `category` ke tabel riwayat kategori `film_category`, lalu ke tabel utama `film`. Hasil penggabungan kemudian dikelompokkan berdasarkan nama genre menggunakan klausul `GROUP BY C.name` untuk menghitung frekuensi film menggunakan fungsi agregasi `COUNT()`.

### E. Nomor 10: Pemfilteran Kompleks Menggunakan Subquery (Tabel film)

- **Tujuan**: Menampilkan `title`, `description`, `length`, dan `rating` untuk 10 film yang judulnya berakhiran dengan huruf "h" dan memiliki durasi di atas rata-rata panjang film keseluruhan secara global.
- **Formulasi Query**:

```
SELECT title, description, length, rating
FROM film
WHERE title LIKE '%H'
  AND length > (SELECT AVG(length) FROM film)
ORDER BY title ASC
LIMIT 10;
```

#### [Wawasan Diskusi / Audio Insight]

- **Keterbatasan Fungsi Agregat**: Mahasiswa menanyakan mengapa ekspresi pemfilteran tidak bisa ditulis secara langsung seperti `WHERE length > AVG(length)`. Dosen menerangkan aturan dasar SQL bahwa fungsi agregat seperti `AVG()` tidak dapat ditempatkan langsung di dalam klausul `WHERE` pada tingkat kueri yang sama. Hal ini karena proses filter `WHERE` dieksekusi oleh mesin database sebelum proses kalkulasi agregat baris dilakukan.
- **Solusi Kueri Bersarang**: Solusi mutlak untuk masalah di atas adalah membungkus fungsi agregat di dalam subquery mandiri `(SELECT AVG(length) FROM film)`. Subquery tersebut akan dihitung terlebih dahulu untuk menghasilkan satu nilai skalar tunggal (misalnya nilai rata-rata 115 menit), yang kemudian disuntikkan ke kueri utama sebagai nilai konstan pembanding durasi masing-masing baris film.
- **Ketentuan Group By**: Jika fungsi agregat ingin ditampilkan bersama dengan kolom non-agregat di tingkat SELECT utama, maka seluruh kolom non-agregat tersebut (seperti `title`, `description`, `length`, `rating`) wajib didaftarkan ke dalam klausul `GROUP BY` agar tidak menimbulkan kegagalan eksekusi (_SQL error_). Oleh karena itu, penggunaan subquery jauh lebih bersih dan efisien untuk kasus pemfilteran baris individual seperti ini.



## module 1 session 10 notes

![[Pasted image 20260821191541.png]]Primary key: unique identity,
Foerign Key; Kolom yang merefer ke sebuha key dari tabel lain. 

![[Pasted image 20260821191705.png]]
Entity itu departemennya
Primary key itu isinya. 



environment location: C:\Users\reine\miniconda3\envs\purwadhika

# To activate this environment, use
#
#     $ conda activate purwadhika
#
# To deactivate an active environment, use
#
#     $ conda deactivate



pip install pandas python-dotenv DONE



-- 0. Use the "sakila" database.
USE sakila;

-- 1. From the "payment" table, show 10 rows of customer_id,
--    rental_id, amount, and payment_date.
SELECT customer_id, rental_id, amount, payment_date
FROM payment
LIMIT 10;

-- 2. From the "film" table, show 10 titles, release year, and
--    rental duration, for titles that start with the letter "S".
SELECT title, release_year, rental_duration
FROM film
WHERE title LIKE 'S%'
LIMIT 10;

-- 3. From the "film" table, show the rental duration, how many
--    films exist for each rental duration, and the average film
--    length. Group the count and average by rental duration, and
--    round the average to 2 decimal places.
--    Rename the headers to 'Durasi_Rental', 'Banyak_Film', and
--    'Rata_Rata_Durasi_Film'.
SELECT 
    rental_duration AS 'Durasi_Rental', 
    COUNT(film_id) AS 'Banyak_Film', 
    ROUND(AVG(length), 2) AS 'Rata_Rata_Durasi_Film'
FROM film
GROUP BY rental_duration;

-- 4. From the "film" table, show the title, length, and rating
--    for films whose length is above the overall average film
--    length. Show 25 rows.
SELECT title, length, rating
FROM film
WHERE length > (SELECT AVG(length) FROM film)
LIMIT 25;

-- 5. From the "film" table, show the rating, highest replacement
--    cost, lowest rental rate, and average length, grouped by
--    rating.
--    Rename the headers to 'Rating', 'Replacement_Cost_Tertinggi',
--    'Rental_Rate_Terendah', and 'Rata_Rata_Durasi'.
SELECT 
    rating AS 'Rating', 
    MAX(replacement_cost) AS 'Replacement_Cost_Tertinggi', 
    MIN(rental_rate) AS 'Rental_Rate_Terendah', 
    AVG(length) AS 'Rata_Rata_Durasi'
FROM film
GROUP BY rating;

-- 6. Show 15 films whose title ends with the letter "K", along
--    with their title, length, and language.
--    Note: join the "film" table with the "language" table first.
SELECT f.title, f.length, l.name AS language
FROM film f
JOIN language l ON f.language_id = l.language_id
WHERE f.title LIKE '%K'
LIMIT 15;

-- 7. Show the film title (from "film"), first name, and last name
--    (from "actor") for the actor with actor_id = 14.
--    Note: join "film", "film_actor", and "actor" first.
SELECT f.title, a.first_name, a.last_name
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.actor_id = 14;

-- 8. From the "city" table, show city and country_id. Only show
--    cities whose name contains the letter "d" anywhere and ends
--    with the letter "a". Show 15 rows ordered by city ascending.
SELECT city, country_id
FROM city
WHERE city LIKE '%d%' AND city LIKE '%a'
ORDER BY city ASC
LIMIT 15;

-- 9. Show the genre name (from "category") and how many films
--    exist in each genre. Join "film", "film_category", and
--    "category" first, and order by film count ascending.
SELECT c.name AS genre_name, COUNT(fc.film_id) AS film_count
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name
ORDER BY film_count ASC;

-- 10. From the "film" table, show title, description, length,
--     and rating for the 10 films whose title ends with the
--     letter "h" and whose length is above the average. Order
--     by title ascending.
SELECT title, description, length, rating
FROM film
WHERE title LIKE '%h' AND length > (SELECT AVG(length) FROM film)
ORDER BY title ASC
LIMIT 10;



---


# Module 1 Session 11 Statistics Fundamental


## Bab 1 Pengantar Statistika (Introduction to Statistics)


## 1.1 Definisi Statistika

### A. Fondasi Konseptual

- Statistika didefinisikan sebagai metodologi untuk mengumpulkan (_collecting_), menganalisis (_analyzing_), menginterpretasikan (_interpreting_), dan menarik kesimpulan (_drawing conclusion_) dari data.
- Secara lebih luas, statistika merupakan seni dan sains dalam merancang studi (_designing studies_) dan menganalisis data yang dihasilkan oleh studi tersebut.
- Tujuan utama (_ultimate goal_) dari statistika adalah menerjemahkan data menjadi pengetahuan (_knowledge_) dan pemahaman mengenai dunia di sekitar kita.
- Singkatnya, statistika adalah seni dan sains untuk belajar dari data (_learning from data_).

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa statistika pada dasarnya adalah "seni dalam mempelajari data".
- Statistika adalah subjek yang sangat luas (_broad subject_) dengan banyak aplikasi di berbagai macam bidang (_various field_).

---

## 1.2 Aplikasi Statistika di Berbagai Bidang

### A. Bidang Penerapan Praktis

Penerapan praktis statistika dalam industri IT, medis, dan manufaktur dapat dirangkum dalam tabel berikut:

|Bidang / Metodologi|Karakteristik / Kasus Penggunaan|
|:--|:--|
|**Experimental Design**|Digunakan untuk melakukan _A/B Testing_ pada desain aplikasi atau web baru.|
|**Survey**|Digunakan untuk memprediksi hasil pemilihan umum (_election_) menggunakan _Exit Poll_ atau Hitung Cepat (_Quick Count_).|
|**Research**|Digunakan untuk menarik kesimpulan ilmiah dalam studi penelitian medis (_Medical Research Studies_).|
|**Quality Control**|Digunakan untuk menjaga kualitas produk yang dihasilkan di pabrik (_factory_).|

#### [Wawasan Diskusi / Audio Insight]

- **A/B Testing**: Ketika suatu aplikasi akan menerapkan desain baru, dilakukan pengujian terlebih dahulu pada dua kelompok pengguna, yaitu Kelompok A dan Kelompok B. Dosen menjelaskan contoh pembagian di mana Kelompok A menerima 50% pengguna aktif lama (_existing users_) dengan desain baru, sedangkan Kelompok B menerima sisa 50% dengan desain lama. Keberhasilan diukur dengan melihat matriks tertentu, seperti peningkatan pembelian (_conversion rate_) akibat perbedaan desain tersebut.
- **Quick Count vs Real Count**: Hitung cepat (_quick count_) merupakan metode penghitungan cepat di mana data tidak dihitung seluruhnya, melainkan hanya diambil sampelnya secara acak (_random_) dari Tempat Pemungutan Suara (TPS). Hasil _quick count_ biasanya sedikit berbeda dengan _real count_ (misalnya jika hasil _quick count_ 60%, hasil _real count_ bisa berkisar antara 58% hingga 62%) dengan tingkat kepercayaan (_confidence level_) tertentu.
- **Research**: Statistika sangat krusial untuk membuat kesimpulan (_making conclusion_) tidak hanya pada penelitian medis, tetapi juga pada berbagai macam bidang penelitian ilmiah lainnya.

---

## 1.3 Tiga Tahapan Utama dalam Proses Statistika (Step-by-Step Statistics)

### A. Alur Kerja Statistika

Proses analisis statistika terdiri dari tiga tahapan utama yang terstruktur secara berurutan:

1. **Design**
    - Tahap perencanaan penelitian dan pengumpulan data.
    - Aktivitas utama meliputi memformulasikan masalah penelitian (_formulate research problem_), mendefinisikan populasi dan sampel (_define population and sample_), serta melakukan pengumpulan data (_data collection_).
2. **Description**
    - Tahap merangkum dan mengeksplorasi data yang telah dikumpulkan.
    - Aktivitas utama meliputi pembuatan visualisasi data dalam bentuk ringkasan grafis (_graphical summary_), ringkasan numerik (_numerical summary_), dan ringkasan tabel (_table summary_).
3. **Inference**
    - Tahap membuat prediksi dan melakukan generalisasi mengenai fenomena yang direpresentasikan oleh data tersebut.
    - Aktivitas utama adalah menggunakan metode yang tepat untuk memecahkan masalah penelitian (_solve the problem_) dan melaporkan hasilnya (_report the result_).

#### [Wawasan Diskusi / Audio Insight]

- Pada tahap **Design**, aktivitas awal adalah merancang formulasi masalah, menentukan karakteristik populasi, merancang sampel, serta merencanakan bagaimana data akan dikumpulkan.
- Pada tahap **Description**, teknik-teknik visualisasi data (_data visualization_) diterapkan agar data yang rumit dapat dipahami secara sederhana sebelum dianalisis lebih lanjut.
- Pada tahap **Inference**, peneliti menggunakan metode statistik yang sesuai untuk memecahkan masalah penelitian dan melaporkan hasil akhirnya secara ilmiah.

---

## 1.4 Dua Cabang Besar Statistika (Type of Statistics)

### A. Klasifikasi Cabang Statistika

Statistika secara umum dibagi menjadi dua cabang utama berdasarkan fokus analisisnya:

|Cabang Statistika|Fokus Utama|Metodologi & Karakteristik|
|:--|:--|:--|
|**Descriptive Statistics**|Berfokus pada perangkuman dan penggambaran data yang dimiliki.|Terdiri dari metode untuk mengorganisasikan, menyederhanakan, dan merangkum informasi.|
|**Inferential Statistics**|Berfokus pada penggunaan data sampel untuk membuat kesimpulan mengenai populasi.|Terdiri dari metode untuk menarik kesimpulan dan mengukur tingkat keandalan kesimpulan (_reliability of conclusion_) berdasarkan sampel dari populasi tersebut.|

#### [Wawasan Diskusi / Audio Insight]

- **Descriptive Statistics**: Digunakan murni untuk mendeskripsikan data yang ada, seperti menghitung rata-rata (_mean_), mengidentifikasi kategori yang paling sering muncul (modus/_mode_), atau melihat tren kenaikan dan penurunan data dari waktu ke waktu tanpa melakukan prediksi atau generalisasi lebih lanjut.
- **Inferential Statistics**: Cabang ini penting karena mengumpulkan keseluruhan data populasi sangat sulit dilakukan. Oleh karena itu, kita mengambil sebagian data sebagai sampel, lalu menggunakan statistik sampel tersebut untuk menarik kesimpulan dan melakukan estimasi mengenai parameter populasi dengan tingkat kepercayaan (_confidence level_) tertentu.
- Contoh hubungan kedua cabang ini adalah _quick count_ (yang menggunakan sampel) untuk mengestimasi hasil pemilu akhir pada _real count_ (populasi).

---

### B. Representasi Konseptual Berbasis Kode

Berikut adalah pemodelan konseptual dari Bab 1 menggunakan representasi kode Python:

```
# Pemodelan konseptual cabang statistika dan tahapan metodologinya
class StatisticsFundamental:
    def __init__(self):
        self.definition = "The art and science of learning from data"
        self.workflow_phases = {
            "Phase 1": "Design (Formulate problem, Define population/sample, Ingest data)",
            "Phase 2": "Description (Summarize data visually and numerically)",
            "Phase 3": "Inference (Generalize and predict based on sample data)"
        }
        self.branches = {
            "Descriptive_Statistics": {
                "fokus": "Summarize and describe current dataset",
                "tools": ["graphs", "charts", "tables", "numerical summaries"]
            },
            "Inferential_Statistics": {
                "fokus": "Draw conclusions about population from representative sample",
                "tools": ["hypothesis testing", "estimation", "confidence levels"]
            }
        }
```

Gemini Notebook can be inaccurate; please double check its responses.



## Bab 2 Data, Variabel, dan Skala Pengukuran (Data, Variables, and Scale of Measurement)


## 2.1 Definisi Data (Definition of Data)

### A. Unit Informasi

- Data didefinisikan sebagai unit informasi individual (_individual units of information_), seperti data satu orang, satu buku, satu barang, satu bangunan, satu mobil, atau satu perusahaan.
- Dalam struktur dataset, representasi data diatur dalam format baris dan kolom yang terstruktur:
    - Setiap baris (_row_) mewakili satu unit observasi (_observation unit_ / _unit of observation_).
    - Setiap kolom (_column_) mewakili satu variabel (_variable_) yang menyimpan karakteristik, sifat, atau atribut spesifik yang diamati dari setiap unit informasi tersebut.
    - Sebagai contoh, pada dataset buku terlaris Amazon:
        - Baris 0, 1, 2, dst. masing-masing mewakili satu objek buku fisik yang diobservasi.
        - Kolom-kolom seperti _Name_ (judul buku), _Author_ (penulis), _User Rating_, _Reviews_, _Price_, _Year_, dan _Genre_ mewakili variabel yang diukur dari setiap buku tersebut.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa di luar pemahaman database relasional konvensional, statistik mendefinisikan data secara spesifik sebagai unit observasi individual.
- Dalam analisis data praktis, sangat krusial untuk langsung mengidentifikasi baris sebagai representasi dari unit observasi tunggal dan kolom sebagai dimensi variabelnya sebelum melakukan manipulasi data lebih lanjut.

## 2.2 Klasifikasi Variabel (Classification of Variables)

### A. Karakteristik Variabel

- Karakteristik atau sifat yang bervariasi dari satu orang atau objek ke orang atau objek lainnya disebut sebagai variabel (contoh: _Height_, _Weight_, _Eye Color_, dll.).
- Variabel secara mendasar dikelompokkan menjadi dua kategori utama berdasarkan sifat datanya:
    1. **Qualitative (Categorical)**
        - Observasi di mana data yang dikumpulkan termasuk dalam satu set kelompok kategori yang berbeda (_distinct categories_).
        - Terbagi menjadi dua tipe:
            - **Nominal**: Kategori-kategori data yang tidak memiliki urutan, peringkat, atau tingkatan logis yang jelas. Contoh: _Type of fruits_ (jenis buah), _Country name_ (nama negara), _Gender_ (Male/Female), dan _Color_ (warna).
            - **Ordinal**: Kategori-kategori data yang memiliki urutan, peringkat, atau tingkatan logis yang jelas. Contoh: _Education level_ (SD, SMP, SMA, S1, S2, S3), _Satisfaction level_ (Sangat tidak puas, Tidak puas, Biasa saja, Puas, Sangat puas), dan _Job level_ (Officer, Supervisor, Manager, General Manager).
    2. **Quantitative (Numerical)**
        - Observasi di mana data berupa nilai numerik yang logis untuk dilakukan operasi matematika seperti penjumlahan atau pengurangan.
        - Terbagi menjadi dua tipe:
            - **Discrete**: Variabel numerik yang nilainya berupa bilangan bulat (_integer_) dan tidak dapat didefinisikan dengan bilangan desimal. Data ini biasanya diperoleh dari hasil perhitungan (_counting_). Contoh: _Number of rooms_ (jumlah ruangan), _Number of clicks_ (jumlah klik), dan _Violation frequency_ (frekuensi pelanggaran).
            - **Continuous**: Variabel numerik yang nilainya diperoleh dari hasil pengukuran (_measurement_) sepanjang nilai kontinu (_continuum value_) dan dapat didefinisikan dengan bilangan desimal bergantung tingkat kepresisian alat pengukur. Contoh: _Height_ (tinggi badan), _Weight_ (berat badan), _Price_ (harga), dan _Age_ (usia).

### B. Signifikansi Penentuan Tipe Variabel dalam Data Science

- Penentuan tipe variabel sangat krusial karena dalam praktiknya, metodologi _Data Analysis_ dan pemodelan prediktif sepenuhnya bergantung pada tipe variabel tersebut:
    - Menentukan kelayakan penggunaan ukuran pemusatan data seperti rata-rata (_average/mean_) untuk mendeskripsikan kelompok data (contoh: tidak logis menggunakan rata-rata untuk mendeskripsikan data kualitatif).
    - Menentukan jenis algoritma pembelajaran mesin (_machine learning_) yang tepat, misalnya memilih pendekatan klasifikasi (_Classification_) atau regresi (_Regression_) saat membangun model prediksi (contoh: menggunakan _Classification_ untuk memprediksi apakah seorang pengguna akan pergi/_Churn_ atau tidak, dan menggunakan _Regression_ untuk memprediksi harga atau nilai numerik kontinu lainnya).

#### [Wawasan Diskusi / Audio Insight]

- **Klarifikasi Desimal pada Discrete**: Dosen memberikan analogi jumlah ruangan (_number of rooms_). Peneliti tidak dapat menyatakan jumlah ruangan bernilai 1,5 atau 1,1 karena ruangan secara fisis harus dihitung dalam unit bilangan bulat utuh. Hal serupa berlaku untuk _number of clicks_ di mana pengguna tidak dapat mengklik setengah kali.
- **Karakteristik Kontinu pada Continuous**: Untuk data kontinu seperti tinggi badan (_height_), rentang nilai di antara 150 cm dan 151 cm tidak kosong (_void_), melainkan terdapat probabilitas nilai desimal tak terhingga (seperti 150,5 cm atau 150,7 cm) bergantung pada tingkat ketelitian alat ukur. Hal ini juga berlaku untuk variabel usia (_age_) di mana waktu terus berjalan kontinu tanpa jeda kosong di antara ulang tahun ke-50 dan ke-51.
- **Klarifikasi Istilah Nominal**: Dosen mengklarifikasi miskonsepsi istilah "nominal" dalam Bahasa Indonesia (yang sering kali diasosiasikan dengan jumlah uang, contoh: "nominal Rp10.000"). Dalam terminologi tipe data statistika internasional, **Nominal** murni berarti data kategorikal tanpa urutan tingkatan fisis (contoh: warna merah tidak memiliki tingkatan lebih tinggi atau lebih rendah dari warna biru).

## 2.3 Skala Pengukuran (Scale of Measurement)

### A. Empat Tingkatan Skala Pengukuran

Skala pengukuran menentukan batasan matematis dan jenis operasi analisis yang diizinkan pada variabel. Terdapat empat tingkatan skala yang disusun secara hierarkis dari yang terendah hingga tertinggi:

1. **Nominal**
    - Skala pengukuran paling dasar yang hanya berfungsi untuk mengklasifikasikan (_classify_) data ke dalam kategori-kategori berbeda tanpa adanya jarak fisis (_distance_) maupun urutan logis (_order_).
2. **Ordinal**
    - Skala yang mengklasifikasikan data dan memiliki urutan atau peringkat tingkatan fisis (_order_) yang jelas, namun jarak (_distance_) antar nilai kategori tersebut tidak dapat diukur secara kuantitatif.
3. **Interval**
    - Variabel kuantitatif di mana karakteristiknya diukur sepanjang nilai kontinu, memiliki urutan, serta memiliki jarak (_distance_) antar nilai yang konsisten dan dapat diukur.
    - Sifat mutlak: Tidak memiliki nilai nol mutlak (_non-absolute zero_), artinya nilai nol (0) tidak menunjukkan ketiadaan absolut dari variabel tersebut (contoh: suhu 0 derajat Celsius memiliki eksistensi dingin fisis dan suhu tetap dapat turun ke angka negatif).
    - Operasi perkalian atau pembagian tidak logis (_not sensible_) untuk dilakukan pada skala ini. Contoh: Suhu 40 derajat Celsius tidak menunjukkan tingkat panas dua kali lipat dari suhu 20 derajat Celsius.
4. **Ratio (Rasio)**
    - Skala pengukuran tertinggi yang memenuhi seluruh kondisi skala interval dengan tambahan kepemilikan nilai nol mutlak (_absolute zero_). Nilai nol (0) menunjukkan ketiadaan mutlak dari variabel yang diukur.
    - Operasi perkalian atau pembagian logis (_sensible_) untuk dilakukan. Nilai rasio biasanya bernilai lebih besar dari nol. Contoh: Tinggi badan (_Height_ 180 cm). Tinggi badan 360 cm secara matematis merupakan dua kali lipat dari tinggi badan 180 cm. Jika tinggi badan bernilai 0 cm, artinya objek tersebut tidak memiliki eksistensi fisik.

### B. Ringkasan Karakteristik Skala Pengukuran

Karakteristik matematis masing-masing skala pengukuran dapat dirangkum secara komparatif dalam tabel berikut:

|Scale|Classify|Order|Distance|Zero Type|Multiplication / Division|
|:--|:-:|:-:|:-:|:-:|:-:|
|**Nominal**|Yes|No|No|No|No|
|**Ordinal**|Yes|Yes|No|No|No|
|**Interval**|Yes|Yes|Yes|Non-Absolute|No|
|**Ratio**|Yes|Yes|Yes|Absolute|Yes|

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan perbedaan fisis antara Interval dan Ratio menggunakan variabel _Temperature_ dan _Height_. Suhu 0 derajat Celsius masih ada fisisnya, sedangkan tinggi 0 cm atau berat badan 0 kg menandakan ketiadaan materi fisis dari objek tersebut. Nilai dari variabel rasio juga secara umum tidak dapat bernilai negatif (selalu lebih besar atau sama dengan nol), berbeda dengan variabel interval yang sangat memungkinkan bernilai negatif (seperti suhu udara di bawah nol derajat Celsius).

---

### C. Representasi Konseptual Berbasis Kode

Berikut adalah pemodelan konseptual dari Bab 2 menggunakan representasi kode Python:

```
class VariableClassifier:
    def __init__(self, name, datatype):
        self.variable_name = name
        self.datatype = datatype  # 'Qualitative' or 'Quantitative'

    def classify_sub_type(self, has_order=False, is_integer=False):
        if self.datatype == 'Qualitative':
            return 'Ordinal' if has_order else 'Nominal'
        elif self.datatype == 'Quantitative':
            return 'Discrete' if is_integer else 'Continuous'
        return 'Unknown'

class ScaleOfMeasurement:
    def __init__(self, scale_name):
        self.scale_name = scale_name  # 'Nominal', 'Ordinal', 'Interval', 'Ratio'

    def get_allowed_operations(self):
        operations = {
            'Classify': True,
            'Order': False,
            'Distance': False,
            'Absolute_Zero': False,
            'Multiplication_Division': False
        }
        if self.scale_name in ['Ordinal', 'Interval', 'Ratio']:
            operations['Order'] = True
        if self.scale_name in ['Interval', 'Ratio']:
            operations['Distance'] = True
        if self.scale_name == 'Ratio':
            operations['Absolute_Zero'] = True
            operations['Multiplication_Division'] = True
        return operations
```



## Bab 3 Berpikir Desain dalam Statistika (Design Thinking of Statistics)


## 3.1 Aspek Utama Desain Statistika (Key Aspects of Statistical Design)

### A. Pendahuluan Berpikir Desain (Design Thinking)

- Berpikir desain dalam statistika berfokus pada perencanaan yang matang sebelum data dikumpulkan dan dianalisis untuk memastikan keandalan hasil akhir.
- Terdapat lima aspek penting yang harus dirancang dalam proses statistika agar data yang diperoleh relevan dan representatif.

### B. Karakteristik Aspek Desain

Lima aspek utama dalam perancangan desain statistika dapat dirangkum dalam tabel berikut:

|Aspek Desain|Deskripsi Singkat|
|:--|:--|
|**Type of Study**|Menentukan jenis studi yang sesuai, apakah berupa eksperimen aktif atau observasi pasif.|
|**Population and Sample**|Mengidentifikasi target utama penyelidikan dan menentukan bagian representatif yang akan diamati.|
|**Randomness**|Menjamin keacakan dalam pengambilan sampel untuk menghindari bias dan menyeimbangkan faktor pengganggu.|
|**Sampling**|Menerapkan metode pemilihan sampel yang sistematis dari populasi yang terdefinisi.|
|**Experimental**|Merancang kondisi pengujian terkontrol dengan memberikan perlakuan khusus pada objek penelitian.|

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa sebelum melangkah ke tahap analisis atau pemodelan, perancangan desain (tahap _Design_) adalah fondasi mutlak yang menentukan validitas seluruh proses statistika berikutnya.

---

## 3.2 Jenis Penelitian (Type of Study)

### A. Studi Eksperimental (Experimental Study)

- Peneliti melakukan intervensi aktif dengan menempatkan subjek penelitian ke dalam kondisi eksperimen tertentu yang disebut _Treatments_.
- Peneliti kemudian mengamati dampak atau hasil dari perlakuan tersebut pada variabel respon (_Response Variable_).
- Studi ini memiliki variabel penjelas (_Explanatory Variable_) sebagai faktor penyebab dan variabel respon sebagai hasil atau akibat.
- Contoh nyata: _A/B Testing_ pada desain antarmuka aplikasi atau situs web baru untuk meningkatkan tingkat konversi (_Conversion Rate_).

### B. Studi Observasional (Observational Study)

- Peneliti bertindak pasif dengan hanya mengamati nilai dari variabel respon dan variabel penjelas dari subjek sampel tanpa memberikan perlakuan khusus atau melakukan intervensi apa pun.
- Contoh nyata: Survei sampel acak di Tempat Pemungutan Suara (TPS) untuk keperluan Hitung Cepat (_Quick Count_).

### C. Perbandingan Karakteristik Studi

Berikut adalah tabel komparatif antara kedua jenis penelitian:

|Karakteristik|Studi Eksperimental (Experimental Study)|Studi Observasional (Observational Study)|
|:--|:--|:--|
|**Intervensi Peneliti**|Aktif memberikan perlakuan (_Treatment_).|Pasif, hanya mengamati kondisi alami.|
|**Variabel Penjelas**|Ditentukan dan dikontrol oleh peneliti.|Diukur secara alami tanpa manipulasi.|
|**Tujuan Utama**|Menguji hubungan sebab-akibat (_Causal Relationship_).|Menggambarkan asosiasi atau pola dalam data asli.|
|**Contoh Kasus**|_A/B Testing_ desain tata letak (_Layout_) baru aplikasi.|Pengumpulan sampel survei suara pemilu di lapangan.|

#### [Wawasan Diskusi / Audio Insight]

- **Matriks Keberhasilan A/B Testing**: Dalam contoh _A/B Testing_, _Conversion Rate_ diposisikan sebagai variabel respon (_Response Variable_), sedangkan variasi desain (misalnya desain baru vs desain lama) adalah variabel penjelas (_Explanatory Variable_).
- **Pembuktian Statistik**: Dosen menerangkan bahwa jika kelompok desain baru menunjukkan _Conversion Rate_ sedikit lebih tinggi (misalnya 20.2% dibandingkan desain lama yang bernilai 20.0%), perbedaan tersebut tidak boleh langsung dianggap sebagai bukti keberhasilan mutlak. Hal ini karena perbedaan kecil tersebut bisa terjadi akibat faktor kebetulan. Statistika diperlukan untuk mengonfirmasi signifikansi perbedaan tersebut secara konkret melalui pengujian hipotesis.

---

## 3.3 Populasi dan Sampel (Population and Sample)

### A. Klasifikasi Populasi

Populasi didefinisikan sebagai keseluruhan kelompok individu atau objek yang menjadi target utama dalam suatu penyelidikan. Populasi dikelompokkan menjadi dua kategori:

|Tipe Populasi|Karakteristik|Contoh|
|:--|:--|:--|
|**Finite Population**|Populasi terbatas yang anggotanya dapat didaftarkan dan dihitung secara fisik.|Jumlah mahasiswa aktif di Purwadhika, jumlah kursi di dalam ruang kelas.|
|**Hypothetical Population**|Populasi abstrak yang muncul dari fenomena berkelanjutan yang sedang dipertimbangkan.|Total produksi bola lampu sebuah pabrik jika terus menggunakan peralatan, metode, dan bahan baku yang sama.|

### B. Konsep Parameter dan Statistik

- **Parameter**: Ringkasan numerik yang menggambarkan karakteristik populasi. Nilai parameter populasi umumnya tidak diketahui secara pasti karena keterbatasan pengukuran menyeluruh.
- **Statistik**: Ringkasan numerik yang dihitung dari data sampel yang diambil dari populasi. Statistik sampel digunakan sebagai estimasi untuk menarik kesimpulan (_Inference_) mengenai parameter populasi.

### C. Rasionalisasi Penggunaan Sampel

Sampel adalah bagian dari populasi yang diamati langsung untuk merepresentasikan keseluruhan populasi. Penggunaan sampel sangat krusial karena adanya keterbatasan dalam tiga faktor utama:

- **Resource**: Keterbatasan sumber daya manusia dan peralatan pengumpul data.
- **Time**: Keterbatasan waktu pengerjaan studi.
- **Cost**: Biaya tinggi yang dibutuhkan jika harus mengukur seluruh populasi.

#### [Wawasan Diskusi / Audio Insight]

- **Analogi Tes Darah**: Dosen memberikan analogi bahwa ketika dokter ingin menguji kondisi kesehatan pasien melalui darah, dokter hanya mengambil beberapa mililiter sampel darah pasien (sampel), bukan menguras seluruh darah dari tubuh pasien (populasi).
- **Analogi Memasak**: Ketika seseorang sedang memasak sayur, ia cukup mencicipi satu sendok kecil kuah (sampel) untuk mengetahui rasa masakan tersebut, tanpa perlu memakan seluruh isi panci (populasi).
- **Keterwakilan Sampel**: Jika sampel diambil dengan metodologi yang baik sehingga bersifat representatif, maka rata-rata sampel (_Sample Mean_) dapat menggambarkan rata-rata populasi (_Population Mean_), dan median sampel (_Sample Median_) dapat menggambarkan median populasi (_Population Median_).

---

## 3.4 Metodologi Pengambilan Sampel (Sampling Methods)

### A. Prinsip Sampling & Sampling Bias

- **Sampling Frame**: Representasi fisik atau daftar seluruh anggota populasi yang dapat diakses untuk diambil sampelnya.
- **Sampling Bias**: Kesalahan dalam pengumpulan sampel yang mengakibatkan sampel tidak representatif terhadap populasi, sehingga kesimpulan yang ditarik menjadi menyimpang.

#### [Wawasan Diskusi / Audio Insight]

- **Analogi Pinggiran Gosong**: Dosen memberikan ilustrasi bias ketika mencicipi masakan istri yang baru matang hanya pada bagian pinggir panci yang kebetulan gosong. Hal ini memicu kesimpulan bias bahwa seluruh masakan terasa pahit, padahal bagian tengahnya matang dengan sempurna.
- **Kasus Data Rumah Sakit (Penyakit Jantung)**: Data fiktif dari sebuah rumah sakit menunjukkan proporsi penderita penyakit jantung pada usia muda (di bawah 50 tahun) mencapai 88.8%, jauh lebih tinggi dibanding usia di atas 50 tahun yang hanya 57.8%. Secara medis hal ini tidak logis.
- **Penyebab Bias Kasus Rumah Sakit**: Bias terjadi karena data tidak dikumpulkan secara acak (_Randomly_). Anak muda memiliki tingkat kesadaran kesehatan yang lebih rendah dan umumnya hanya datang ke rumah sakit jika sudah merasakan gejala penyakit yang parah (sehingga probabilitas terdeteksi sakit jantung sangat tinggi saat diperiksa). Sebaliknya, orang tua memiliki kesadaran tinggi untuk rutin melakukan pemeriksaan kesehatan (_Medical Check-Up_) secara berkala terlepas dari apakah mereka merasa sakit atau tidak. Data tersebut adalah bagian dari populasi namun tidak representatif.

### B. Teknik Sampling Probabilitas

Untuk menghindari bias, sampel harus diambil menggunakan metode ilmiah yang memanfaatkan keacakan (_Randomness_). Empat metode sampling probabilitas utama dirangkum dalam tabel berikut:

|Metode Sampling|Karakteristik Operasional|Contoh Kasus|
|:--|:--|:--|
|**Simple Random Sample**|Setiap anggota populasi memiliki peluang yang sama besar untuk terpilih secara acak murni.|Mengundi nomor induk mahasiswa untuk survei kepuasan.|
|**Systematic Sample**|Anggota sampel dipilih berdasarkan interval numerik tertentu setelah titik awal acak ditetapkan.|Memilih setiap orang ke-10 yang mendaftar pada platform digital.|
|**Stratified Sample**|Populasi dibagi ke dalam kelompok-kelompok homogen yang saling lepas (_Strata_), kemudian sampel acak diambil dari setiap kelompok.|Membagi populasi berdasarkan tingkat pendidikan (SD, SMP, SMA, S1) lalu mengambil sampel secara acak dari tiap tingkatan tersebut.|
|**Cluster Sample**|Populasi dibagi ke dalam kelompok-kelompok heterogen (_Clusters_) berdasarkan geografis, lalu beberapa kluster dipilih secara acak untuk disensus.|Memilih beberapa Tempat Pemungutan Suara (TPS) secara acak dari berbagai kecamatan untuk mewakili suara satu kota.|

#### [Wawasan Diskusi / Audio Insight]

- **Cluster Sampling pada Quick Count**: Metode _Cluster Sampling_ sangat sering digunakan dalam hitung cepat pemilu. Di lapangan, sering kali terdapat TPS tertentu yang merupakan basis kekuatan atau "kandang" dari calon tertentu yang sangat dominan. Jika peneliti menggunakan acak sederhana tanpa klusterisasi geografis, ada risiko sampel yang terpilih menumpuk pada TPS dominan tersebut sehingga hasilnya bias. Dengan _Cluster Sampling_, peneliti dipaksa mengambil sampel dari berbagai kluster geografis yang terpisah (kecamatan atau kelurahan berbeda) untuk menjaga keterwakilan data secara nasional.

---

## 3.5 Desain Eksperimen yang Baik (Experimental Design)

### A. Unsur Dasar Eksperimen

Eksperimen yang dirancang dengan baik harus memenuhi tiga pilar utama berikut:

- **Control Comparison Group**: Adanya kelompok kontrol yang menerima perlakuan standar atau plasebo sebagai dasar pembanding untuk mengukur efektivitas perlakuan baru.
- **Randomization**: Alokasi unit eksperimental ke kelompok perlakuan secara acak untuk menyeimbangkan efek dari variabel pengganggu yang tidak terkontrol (_Lurking Variables / Covariates_).
- **Blinding**: Penyamaran subjek atau peneliti agar tidak mengetahui perlakuan mana yang diberikan, guna menghindari bias subjektif selama proses penilaian.

### B. Kasus Uji A/B Testing

Sebuah platform belanja digital (_Marketplace_) menguji efektivitas desain antarmuka aplikasi baru untuk melihat pengaruhnya terhadap _Conversion Rate_. Skema eksperimen dijalankan sebagai berikut:

|Parameter Eksperimen|Detail Implementasi Kasus|
|:--|:--|
|**Subject / Experimental Unit**|Pengguna baru yang terdaftar di platform (_People_).|
|**Total Sampel Pengguna**|240 pengguna baru yang dipilih secara acak.|
|**Kelompok Kontrol (Control Group)**|122 pengguna yang diarahkan ke desain lama (Layout A).|
|**Kelompok Perlakuan (Treatment Group)**|118 pengguna yang diarahkan ke desain baru (Layout B).|
|**Variabel Respon (Response Variable)**|_Conversion Rate_ (proporsi pengguna yang melakukan pembelian).|

#### [Wawasan Diskusi / Audio Insight]

- **Reduksi Efek Covariate**: Dengan membagi 240 pengguna tersebut secara acak (_Randomly_) ke dalam kelompok Layout A (122 pengguna) dan Layout B (118 pengguna), efek dari variabel pengganggu (_Covariates_) seperti faktor usia, jenis kelamin, latar belakang pekerjaan, maupun perangkat yang digunakan akan terbagi rata dan seimbang di antara kedua kelompok. Hal ini memastikan bahwa perbedaan performa _Conversion Rate_ akhir benar-benar disebabkan oleh perbedaan desain antarmuka, bukan karena ketidakseimbangan karakteristik bawaan pengguna.

---

## 3.6 Representasi Konseptual Berbasis Kode

Berikut adalah pemodelan konseptual dari Bab 3 menggunakan representasi kode Python:

```
class ExperimentalDesignSimulation:
    def __init__(self):
        self.p_aspects = ["Type of Study", "Population and Sample", "Randomness", "Sampling", "Experimental"]
        self.sampling_methods = {
            "Simple_Random": "Equal probability for all members",
            "Systematic": "Selection using regular intervals",
            "Stratified": "Random sampling from homogeneous subgroups",
            "Cluster": "Random selection of geographic subgroups"
        }
        self.good_experiment_rules = ["Control Group", "Randomization", "Blinding"]

    def run_ab_test_allocation(self, total_users=240):
        # Alokasi pengguna secara acak untuk menyeimbangkan covariates
        import random
        users = [f"User_{i}" for i in range(1, total_users + 1)]
        random.shuffle(users)

        control_group = users[:122]  # Layout A
        treatment_group = users[122:] # Layout B

        return {
            "Control_Group_Size": len(control_group),
            "Treatment_Group_Size": len(treatment_group)
        }
```



## Bab 4 Statistika Deskriptif (Descriptive Statistics)


## 4.1 Definisi Ringkasan Deskriptif

### A. Fondasi Konseptual

- **Descriptive Statistics** merupakan kegiatan yang mencakup pengorganisasian, perangkuman, dan penggambaran karakteristik utama dari data yang dimiliki tanpa tujuan untuk melakukan prediksi atau generalisasi ke populasi yang lebih luas.
- Metode desktriptif ini diimplementasikan melalui pembuatan grafik, diagram, tabel, serta penghitungan berbagai ukuran deskriptif numerik seperti nilai rata-rata, variasi, dan persentil.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa tujuan utama dari **Descriptive Statistics** adalah mendeskripsikan data secara akurat menggunakan grafik, chart, tabel, serta perhitungan ukuran deskriptif (seperti _average_, _variation_, dan _percentile_) agar pola internal data dapat terbaca dengan mudah sebelum melangkah ke analisis inferensial yang lebih kompleks.

---

## 4.2 Ukuran Pemusatan Data (Measures of Central Tendency)

### A. Karakteristik dan Metodologi

**Measures of Central Tendency** adalah cara mendeskripsikan posisi sentral atau titik tengah dari distribusi frekuensi suatu kelompok data.

Tiga ukuran pemusatan data yang paling sering digunakan dirangkum dalam tabel berikut:

|Ukuran Pemusatan|Cara Penghitungan / Karakteristik|Relevansi dan Sensitivitas Terhadap Data|
|:--|:--|:--|
|**Mean** (Rata-rata)|Jumlah seluruh nilai observasi dibagi dengan total jumlah observasi.|Sangat cocok untuk variabel kuantitatif dengan distribusi simetrik (_symmetric distribution_). Sangat sensitif terhadap pencilan (_outliers_).|
|**Median** (Nilai Tengah)|Nilai tengah dari daftar data yang telah diurutkan dari terkecil ke terbesar. Posisi median dicari dengan formula `(n + 1) / 2`.|Sangat cocok untuk data dengan distribusi tidak simetrik atau miring (_skewed distribution_) karena tidak terpengaruh oleh pencilan (_outliers_).|
|**Mode** (Modus)|Nilai dari variabel kualitatif atau kuantitatif terhitung (_countable_) yang frekuensi kemunculannya paling sering.|Sangat cocok untuk mengidentifikasi pusat data kualitatif/kategorikal. Sulit diterapkan pada variabel kontinu yang sangat presisi karena setiap nilai cenderung unik.|

#### [Wawasan Diskusi / Audio Insight]

- **Kondisi Penggunaan Modus pada Data Kontinu**: Dosen menjelaskan bahwa modus sangat tidak cocok untuk data kuantitatif kontinu yang bernilai presisi tinggi (misalnya data tinggi badan dengan beberapa angka desimal di belakang koma, seperti `160.1234` cm). Hal ini dikarenakan data tersebut cenderung unik sehingga kemunculannya hampir selalu satu kali. Modus baru dapat digunakan pada data tersebut jika datanya dikelompokkan terlebih dahulu ke dalam kategori interval (misalnya kategori interval `160 - 170` cm, `170 - 180` cm).
- **Analogi Skewness Pendapatan (Mean vs Median)**: Dosen memberikan contoh konkret mengenai bias penggunaan rata-rata pada data pendapatan warga di negara dengan kesenjangan sosial yang sangat tinggi (_highly skewed_).
    - Jika ada 10 orang dengan pendapatan berkisar di angka normal `7 - 9` juta rupiah, namun ada 1 orang yang memiliki pendapatan luar biasa sebesar `100` juta rupiah, maka nilai rata-rata (_mean_) akan melonjak naik ke atas dan tidak representatif bagi mayoritas kelompok tersebut.
    - Sebaliknya, nilai tengah (_median_) tidak akan terpengaruh oleh satu nilai ekstrem (`100` juta) karena posisi tengahnya tetap konsisten berada di kisaran angka `7 - 9` juta rupiah. Oleh karena itu, untuk data miring (_skewed_), median merupakan representasi pusat data yang jauh lebih andal.
- **Deteksi Skewness Melalui Deviasi Mean dan Median**: Perbedaan nilai yang jauh antara _mean_ dan _median_ di dalam suatu studi ilmiah sering kali digunakan sebagai indikator awal bahwa sebaran data tersebut tidak simetris (_skewed_) dan mengandung banyak pencilan (_outliers_).
- **Modus untuk Data Kualitatif**: Modus sangat efektif sebagai ukuran pemusatan data kategorikal (non-angka). Dosen memberikan contoh riil mengenai pencarian merek mobil terpopuler di Jakarta dari data `1` juta unit kendaraan. Melalui penghitungan frekuensi, ditemukan `500.000` unit merek Toyota dan `300.000` unit merek Daihatsu. Dengan demikian, modus dari variabel kualitatif merek mobil tersebut adalah Toyota.

---

## 4.3 Ukuran Penyebaran Data (Measures of Spread / Variability)

### A. Karakteristik dan Metodologi

**Measures of Spread** digunakan untuk merangkum kelompok data dengan menggambarkan seberapa jauh sebaran data tersebut dari pusatnya. Memahami variabilitas sangat krusial karena dua kelompok data dapat memiliki nilai pusat yang sama namun memiliki tingkat keragaman yang berbeda jauh.

Karakteristik metode pengukuran penyebaran data dirangkum dalam tabel berikut:

|Ukuran Penyebaran|Deskripsi Metodologis|Karakteristik Utama|
|:--|:--|:--|
|**Range** (Rentang)|Selisih antara nilai observasi terbesar (_maximum_) dan terkecil (_minimum_). Formula: `Range = Max - Min`.|Sangat sederhana namun terlalu sensitif terhadap nilai ekstrem (_overly sensitive to extreme values_).|
|**Percentile** (Persentil)|Nilai di mana suatu persentase tertentu `p` dari observasi berada pada atau di bawah nilai tersebut.|Membagi distribusi menjadi 100 bagian yang sama untuk menentukan posisi relatif data.|
|**Quartile** (Kuartil)|Kasus khusus dari persentil yang membagi data terurut menjadi 4 bagian sama besar.|Terdiri dari `Q1` (persentil 25), `Q2` (persentil 50 / Median), dan `Q3` (persentil 75).|
|**Interquartile Range** (IQR)|Jarak antara kuartil atas (_third quartile_) dan kuartil bawah (_first quartile_). Formula: `IQR = Q3 - Q1`.|Digunakan untuk menggantikan simpangan baku pada data miring dan mendeteksi pencilan (_outliers_).|
|**Standard Deviation** (Simpangan Baku)|Akar kuadrat dari varians, menunjukkan rata-rata penyimpangan absolute data dari nilai rata-ratanya (_mean_).|Sering digunakan bersama _mean_ untuk data berdistribusi simetris (_symmetric distribution_). Sangat dipengaruhi oleh pencilan.|

#### [Wawasan Diskusi / Audio Insight]

- **Ilustrasi Kebutuhan Analisis Spread**: Dosen memberikan simulasi tentang pentingnya melihat ukuran penyebaran di samping ukuran pemusatan.
    - Dua negara memiliki rata-rata gaji yang sama, yaitu `10` juta rupiah.
    - Negara A memiliki rentang (_range_) gaji yang sempit, yaitu hanya berkisar antara `9` juta hingga `11` juta rupiah. Distribusi pendapatan di Negara A ini sangat merata.
    - Negara B memiliki rata-rata yang sama (`10` juta rupiah), tetapi rentang (_range_) gajinya sangat lebar, yaitu dari `1` juta hingga `100` juta rupiah. Kesenjangan sosial di Negara B ini sangat tinggi.
    - Jika peneliti hanya menyajikan nilai rata-rata saja tanpa menyertakan ukuran penyebaran (_measures of spread_), informasi kesenjangan yang sangat penting tersebut akan hilang sepenuhnya.
- **Analogi Persentil Nilai Siswa**: Dosen memberikan analogi bahwa apabila seorang siswa berada pada persentil ke-75 dari 100 siswa, hal ini menunjukkan bahwa nilai siswa tersebut setara atau lebih tinggi dari 75% siswa lainnya di dalam kelompok tersebut.

---

## 4.4 Deteksi Pencilan dan Estimasi Standar Deviasi Berbasis IQR

### A. Rumus Deteksi Outlier (The 1.5 x IQR Rule)

_Interquartile Range_ (IQR) memiliki peran penting dalam mendeteksi adanya data pencilan (_outliers_). Batas toleransi nilai normal ditentukan menggunakan aturan konstanta `1.5`:

- Batas Bawah (_Lower Bound_) = `Q1 - 1.5 x IQR`
- Batas Atas (_Upper Bound_) = `Q3 + 1.5 x IQR`

Setiap titik data yang nilainya jatuh di bawah batas bawah atau di atas batas atas secara matematis diklasifikasikan sebagai **Outlier**.

Selain itu, jika data terdistribusi secara normal, simpangan baku (_standard deviation_) dapat diestimasi secara aproksimasi dari nilai IQR menggunakan formula:

- `S = 1.34898 x IQR`

---

### B. Studi Kasus Perhitungan Manual Berbasis Contoh Modul

Berdasarkan data usia pasien dari modul yang berjumlah `8` observasi (data telah diurutkan): `22, 22, 23, 23, 24, 27, 28, 29`

Langkah-langkah penghitungan deskriptif numerik:

1. **Mean**:
    - `(22 + 22 + 23 + 23 + 24 + 27 + 28 + 29) / 8 = 24.75` tahun.
2. **Median (Q2)**:
    - Karena jumlah observasi genap (`n = 8`), median diperoleh dari rata-rata dua nilai tengah (data ke-4 dan data ke-5): `(23 + 24) / 2 = 23.5` tahun.
3. **Kuartil 1 (Q1)**:
    - Diperoleh nilai sebesar `22.75` tahun.
4. **Kuartil 3 (Q3)**:
    - Diperoleh nilai sebesar `27.25` tahun.
5. **IQR**:
    - `IQR = Q3 - Q1 = 27.25 - 22.75 = 4.5` tahun.
6. **Range**:
    - `Range = Max - Min = 29 - 22 = 7` tahun.
7. **Standard Deviation (s)**:
    - Diperoleh nilai sebesar `2.63391` tahun.

#### [Wawasan Diskusi / Audio Insight]

- **Simulasi Penghitungan Deteksi Outlier Bersama Mahasiswa**: Dosen menuntun mahasiswa (_Rainer_) secara langsung untuk menghitung batas pencilan dari data usia pasien tersebut:
    - Nilai pengali konstanta: `1.5 x IQR = 1.5 x 4.5 = 6.75` tahun.
    - Penghitungan Batas Bawah: `Q1 - 6.75 = 22.75 - 6.75 = 16.00` tahun.
    - Penghitungan Batas Atas: `Q3 + 6.75 = 27.25 + 6.75 = 34.00` tahun.
    - **Kesimpulan Analisis**: Karena nilai observasi usia pasien terkecil adalah `22` tahun (masih di atas `16.00`) dan usia terbesar adalah `29` tahun (masih di bawah `34.00`), maka secara matematis disimpulkan **tidak ada outlier** di dalam dataset pasien tersebut.

---

## 4.5 Representasi Konseptual Berbasis Kode

### A. Pemodelan Statistika Deskriptif dalam Python

Dalam ekosistem pemrograman Python, seluruh perhitungan ringkasan statistika deskriptif di atas dapat dipanggil secara instan menggunakan library _Pandas_ melalui fungsi `.describe()`.

Berikut adalah representasi kode untuk melakukan kalkulasi statistika deskriptif pada dataset kuantitatif:

```
import pandas as pd

# Representasi konseptual data usia pasien dari modul
data_pasien = {
    'Patient': ['Andrew', 'Jacob', 'Ros', 'Andersen', 'Lina', 'Robert', 'Jack', 'Annie'],
    'Gender': ['Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female'],
    'Age': [22, 22, 23, 23, 29, 24, 27, 28]
}

df = pd.DataFrame(data_pasien)

# Menampilkan ringkasan statistika deskriptif untuk variabel kuantitatif (Age)
summary_statistics = df['Age'].describe()

# Implementasi penghitungan manual aturan IQR untuk deteksi outlier
q1 = df['Age'].quantile(0.25)
q3 = df['Age'].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
```



## Bab 5 Distribusi Normal (Normal Distribution)


## 5.1 Definisi dan Karakteristik Distribusi Normal

### A. Fondasi Konseptual

- **Distribusi Normal**, juga dikenal sebagai **Gaussian Distribution**, adalah jenis distribusi probabilitas kontinu yang memiliki kurva kepadatan berbentuk lonceng (_bell-shaped curve_).
- Kurva kepadatan ini memiliki karakteristik utama sebagai berikut:
    - **Simetris**: Sisi kiri dan kanan kurva merupakan cerminan satu sama lain.
    - **Terpusat**: Kurva berpusat tepat pada nilai rata-rata (_mean_) dari dataset.
    - **Penyebaran**: Tingkat kelebaran atau kerampingan kurva sepenuhnya ditentukan oleh nilai simpangan baku (_standard deviation_).
    - **Frekuensi Data**: Data yang berada di dekat nilai rata-rata memiliki frekuensi kemunculan yang jauh lebih tinggi dibandingkan dengan data yang berada jauh dari nilai rata-rata.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa Distribusi Normal adalah salah satu konsep yang akan sangat sering ditemui di berbagai tempat, khususnya saat membahas topik statistika inferensial (_statistical inference_).
- Distribusi ini juga menjadi asumsi dasar dari banyak algoritma dalam bidang _Data Science_ dan _Machine Learning_.
- Pada kurva normal sempurna, posisi nilai rata-rata (_mean_) dan nilai tengah (_median_) berada tepat di tengah-tengah kurva simetris tersebut, sehingga nilai $Mean = Median$.
- Dalam praktik lapangan, data aktual jarang sekali mengikuti kurva normal secara sempurna (_perfectly normally distributed_). Namun, dosen menyatakan bahwa data tersebut masih dapat diasumsikan terdistribusi normal selama penyimpangan visualnya dari kurva teoritis tergolong sangat kecil atau tidak signifikan.

---

## 5.2 Pentingnya Distribusi Normal

### A. Relevansi Praktis dalam Data Science

- Banyak variabel dependen (_dependent variables_) di dalam populasi secara umum diasumsikan terdistribusi secara normal.
- Jika suatu variabel terbukti mendekati terdistribusi normal (_approximately normally distributed_), kita dapat dengan valid melakukan inferensi atau penarikan kesimpulan mengenai nilai-nilai dari variabel tersebut.
- Beberapa teknik pembersihan data (_data cleaning_) serta algoritma pembelajaran mesin (_machine learning_) memerlukan pemenuhan asumsi bahwa data masukan wajib terdistribusi secara normal.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa dalam tahapan pemodelan _Machine Learning_, beberapa algoritma mengharuskan pemenuhan asumsi normalitas data.
- Apabila data aktual yang dimiliki ternyata miring (_skewed_) atau tidak normal, praktisi data harus melakukan penanganan khusus, salah satunya dengan menerapkan teknik transformasi data (_data transformation_) agar bentuk distribusinya bergeser mendekati normal.
- Penanganan ini bersifat sangat kontekstual (_case-by-case_); jika algoritma yang digunakan tidak mensyaratkan normalitas, maka transformasi data tidak perlu dilakukan.

---

## 5.3 Aturan Empiris Simpangan Baku (Empirical Rule)

### A. Aturan Persentase Distribusi Lonceng

Jika sebuah distribusi data terbukti berbentuk lonceng (_bell-shaped_), maka berlaku aturan empiris (_empirical rule_) untuk menentukan proporsi penyebaran data sebagai berikut:

- Sekitar **68%** observasi jatuh di dalam rentang $\bar{x} - s$ hingga $\bar{x} + s$ (rata-rata plus-minus satu kali simpangan baku).
- Sekitar **95%** observasi jatuh di dalam rentang $\bar{x} - 2s$ hingga $\bar{x} + 2s$ (rata-rata plus-minus dua kali simpangan baku).
- Sekitar **99.7%** observasi jatuh di dalam rentang $\bar{x} - 3s$ hingga $\bar{x} + 3s$ (rata-rata plus-minus tiga kali simpangan baku).
- Simpangan baku dapat diestimasi secara kasar (_rough estimation_) dari persebaran data menggunakan rumus: $$s \approx \frac{\text{Rentang}}{4} = \frac{\text{Max} - \text{Min}}{4}$$

#### [Wawasan Diskusi / Audio Insight]

- Aturan persentase ini merupakan karakteristik mutlak yang hanya berlaku pada data yang simetris atau berbentuk lonceng.
- Pada distribusi data yang miring (_skewed_), persentase observasi yang jatuh pada rentang simpangan baku tersebut akan bergeser dan tidak akan mengikuti rasio 68%, 95%, dan 99.7% secara presisi karena konsentrasi data yang berat sebelah.

---

## 5.4 Uji Normalitas (Normality Assessment)

Metodologi pengujian untuk menentukan apakah suatu dataset dimodelkan dengan baik oleh Distribusi Normal terbagi menjadi dua pendekatan utama:

### A. Metode Grafis (Graphical Methods)

|Alat Visualisasi|Cara Kerja dan Karakteristik Deteksi|
|:--|:--|
|**Histogram**|Visualisasi yang menampilkan distribusi frekuensi variabel tunggal secara cepat. Dilakukan dengan membandingkan diagram batang aktual sampel terhadap kurva lonceng teoritis merah. Jika penyimpangan batang aktual sangat minim, data dianggap normal.|
|**Box Plot**|Digunakan untuk mendeteksi non-normalitas sampel dengan melihat posisi garis median. Pada data simetris, median berada tepat di tengah kotak. Namun, deviasi pada kelebaran atau keruncingan kurva (_width/pointiness_) sangat sulit diidentifikasi secara visual hanya menggunakan alat ini.|
|**QQ Plot**|Singkatan dari _Quantile vs Quantile Plot_. Alat ini memplot kuantil teoretis terhadap kuantil aktual dari variabel. QQ Plot mampu menampilkan deviasi dari distribusi normal secara jauh lebih jelas dan sensitif dibandingkan Histogram atau Box Plot.|

#### [Wawasan Diskusi / Audio Insight]

- **Karakteristik Visual QQ Plot**: Pada data yang berdistribusi normal, titik-titik plot akan berbaris merapat mengikuti garis lurus diagonal secara sempurna. Pada data miring ke kanan (_right-skewed_), titik plot akan melengkung melonjak di bagian kanan atas garis diagonal. Sebaliknya, pada data miring ke kiri (_left-skewed_), titik plot akan mencong dan melengkung di bagian kiri bawah garis diagonal.
- **Pembersihan Outlier Berdasarkan Box Plot**: Dosen menjelaskan bahwa dalam siklus pengembangan _machine learning_, Box Plot sering dipakai untuk menyaring outlier (dengan formula batas luar $1.5 \times \text{IQR}$). Namun, penghapusan ini tidak boleh dilakukan sembarangan. Sebagai contoh, dalam kasus deteksi penipuan kartu kredit (_fraud detection_), transaksi fraud yang bersifat pencilan (hanya bernilai sekitar 0.5% hingga 1%) adalah data yang paling krusial untuk dipelajari. Jika data outlier tersebut dihapus, model tidak akan pernah bisa mendeteksi transaksi fraud.

### B. Uji Hipotesis Formal (Frequentist Test)

|Nama Uji Statistik|Deskripsi Metodologi dan Batasan|
|:--|:--|
|**Kolmogorov-Smirnov Test (KS Test)**|Menghitung jarak supremum antara fungsi distribusi empiris sampel dengan distribusi teoretis normal. Memiliki kekuatan uji (_statistical power_) yang rendah, sehingga membutuhkan jumlah sampel yang sangat besar untuk menolak hipotesis nol, serta sangat sensitif terhadap pencilan (_outliers_). Nilai statistik KS akan bernilai 0 jika data mengikuti distribusi normal sempurna.|
|**Lilliefors Test**|Merupakan perbaikan langsung dari KS Test di mana rata-rata dan varians populasi diestimasi langsung dari sampel data alih-alih ditentukan oleh pengguna. Meskipun lebih baik dari KS Test, kekuatan statistiknya masih lebih rendah dibandingkan Shapiro-Wilk Test.|
|**Shapiro-Wilk Test**|Uji normalitas yang paling kuat (_most powerful test_). Dirancang secara eksklusif khusus untuk Distribusi Normal dan tidak dapat diaplikasikan untuk pengujian terhadap jenis distribusi probabilitas lainnya.|
|**D'Agostino and Pearson's Test**|Uji normalitas omnibus yang menggabungkan parameter kemiringan (_skewness_) dan keruncingan (_kurtosis_). Berlandaskan pada prinsip bahwa statistik uji akan berdistribusi Chi-Square dengan 2 derajat kebebasan (_degrees of freedom_) jika data terdistribusi normal.|

### C. Aturan Interpretasi Nilai Probabilitas (P-Value)

Keputusan akhir untuk mengasumsikan normalitas data didasarkan pada ambang batas signifikansi nilai _P-Value_ sebagai berikut:

- **Jika P-Value > 0.05**: Kita mengasumsikan data terdistribusi normal (_assume a normal distribution_).
- **Jika P-Value < 0.05**: Kita tidak mengasumsikan data terdistribusi normal (_do not assume a normal distribution_).

#### [Wawasan Diskusi / Audio Insight]

- Dosen mengklarifikasi bahwa dalam kurikulum Bootcamp AI (terutama untuk jalur _AI Engineering_ yang berfokus pada teknologi _Generative AI_), uji statistik frequentist formal ini sangat jarang digunakan secara praktis di industri nyata.
- Praktisi di lapangan umumnya lebih mengandalkan visualisasi grafis (_Graphical Methods_) yang instan dan informatif untuk mendeteksi kelayakan distribusi data.
- Penjelasan uji frequentist ini disertakan agar mahasiswa memiliki pemahaman teoretis yang kuat dan tidak merasa asing saat istilah-istilah ini muncul dalam diskusi atau dokumentasi teknis lanjutan.

---

### D. Representasi Konseptual Berbasis Kode

Berikut adalah pemodelan konseptual pengujian normalitas menggunakan representasi kode Python:

```
# Pemodelan konseptual uji normalitas menggunakan scipy.stats
class NormalityTestingModel:
    def __init__(self, dataset_name, data_values):
        self.dataset_name = dataset_name
        self.data = data_values
        self.alpha_significance = 0.05

    def evaluate_p_value(self, p_value, test_name):
        if p_value > self.alpha_significance:
            return f"[{test_name}] P-Value: {p_value:.5f} > {self.alpha_significance}. Assume a normal distribution."
        else:
            return f"[{test_name}] P-Value: {p_value:.5f} <= {self.alpha_significance}. Do not assume a normal distribution."

    def run_shapiro_wilk_test(self):
        # Shapiro-Wilk merupakan uji normalitas paling kuat (most powerful)
        # return (statistic, p_value)
        pass

    def run_kolmogorov_smirnov_test(self):
        # KS Test mengukur jarak supremum, sensitif terhadap outliers
        # return (statistic, p_value)
        pass
```



## Bab 6 Ringkasan Grafis dalam Statistika Deskriptif (Graphical Summary)


## 6.1 Pemilihan Grafik Berdasarkan Tipe Variabel

### A. Klasifikasi Visualisasi

Dalam statistika deskriptif, pemilihan jenis grafik atau diagram sangat bergantung pada tipe variabel yang sedang dianalisis. Pemilihan alat visualisasi yang tepat memastikan distribusi, komposisi, atau korelasi data dapat tersampaikan secara akurat.

Berikut adalah panduan klasifikasi pemilihan visualisasi berdasarkan tipe variabel:

|Tipe Variabel|Jenis Alat Visualisasi|Tujuan Utama Analisis|
|:--|:--|:--|
|**Numerical Variable**|Histogram, Boxplot, Scatterplot|Mengamati bentuk distribusi, mendeteksi pencilan, dan melihat tren atau korelasi antar variabel kuantitatif.|
|**Categorical Variable**|Pie Chart, Bar Plot|Mengamati komposisi, proporsi, atau perbandingan frekuensi antar kategori variabel kualitatif.|
|**Both Numerical & Categorical**|Bar Plot, Boxplot|Membandingkan nilai agregat kuantitatif atau membandingkan sebaran data numerik di berbagai kelompok kategori.|

---

## 6.2 Penjelasan Alat Visualisasi

### A. Histogram

- Histogram adalah grafik yang merepresentasikan distribusi frekuensi data numerik secara akurat menggunakan batang tegak.
- Lebar dari setiap batang menunjukkan interval kelas data (_bin_), sedangkan tinggi batang mewakili frekuensi atau jumlah kejadian dari data yang berada di dalam interval tersebut.
- Melalui histogram, bentuk pola sebaran data dapat diidentifikasi secara cepat, apakah data tersebut simetris (terdistribusi normal), memiliki dua puncak (_bimodal_), miring ke kanan (_right-skewed_), miring ke kiri (_left-skewed_), atau merata (_uniform_).

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa proses pembuatan histogram dilakukan secara sederhana dengan memetakan rentang data numerik ke dalam kategori interval tertentu (_bins_). Sebagai contoh nyata, jika terdapat rentang data usia pasien antara 0 hingga 20 tahun dengan frekuensi sebanyak 1 orang, interval 21 hingga 25 tahun dengan frekuensi sebanyak 8 orang, dan interval 26 hingga 30 tahun dengan frekuensi sebanyak 2 orang, maka data poin tersebut langsung diplot ke dalam grafik sesuai tinggi frekuensi masing-masing kelas intervalnya.

---

### B. Box Plot

- Box Plot (atau juga dikenal dengan nama _Box-and-Whisker Plot_) adalah metode visualisasi grafis yang menggambarkan distribusi data numerik berdasarkan ringkasan lima angka (_five-number summary_): nilai minimum, kuartil pertama (Q1), median (Q2), kuartil ketiga (Q3), dan nilai maksimum.
- Visualisasi ini digambarkan dengan sebuah kotak persegi panjang (_box_) dari kuartil bawah hingga kuartil atas, sebuah garis pembatas horizontal di dalam kotak yang menunjukkan nilai median, serta garis perpanjangan (_whiskers_) ke arah luar kotak untuk menunjukkan batas nilai ekstrem non-pencilan.
- Alat ini sangat efektif untuk mendeteksi keberadaan data pencilan (_outliers_) yang divisualisasikan berupa titik-titik data yang terisolasi di luar batas maksimum atau minimum teoritis.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa Box Plot merupakan teknik visualisasi yang sangat unggul untuk mendeteksi keberadaan pencilan secara instan. Meskipun Box Plot mampu membandingkan persebaran beberapa variabel atau kelompok secara sekaligus, alat ini memiliki keterbatasan dalam mengidentifikasi secara mendetail variasi kelancipan (_pointiness_) atau kelebaran puncak kurva jika dibandingkan dengan histogram.

---

### C. Scatter Plot

- Scatter Plot (Diagram Pencar) adalah grafik dua dimensi yang menampilkan titik-titik koordinat data untuk memvisualisasikan hubungan atau korelasi antara dua variabel kuantitatif.
- Setiap titik data pada diagram mewakili sepasang nilai dari sumbu horizontal (sumbu X) dan sumbu vertikal (sumbu Y).
- Titik-titik data pada diagram ini tidak dihubungkan oleh garis kontinu untuk menjaga representasi keunikan dari setiap observasi individu.
- Dalam bidang ilmu data (_Data Science_), diagram ini adalah alat fundamental untuk mendeteksi arah korelasi (positif, negatif, atau tidak ada korelasi) serta kekuatan hubungan linear antara dua variabel kuantitatif.

#### [Wawasan Diskusi / Audio Insight]

- Sebagai contoh kasus nyata penerapan Scatter Plot, dosen mencontohkan analisis hubungan antara variabel total tagihan (_total bill_) dengan variabel jumlah tip yang diberikan oleh pelanggan di restoran. Melalui scatter plot, kita dapat dengan mudah membaca kecenderungan atau tren di mana pelanggan yang memiliki total tagihan makanan lebih besar cenderung memberikan tip dengan jumlah yang lebih tinggi pula.

---

### D. Pie Chart

- Pie Chart (Diagram Lingkaran) adalah visualisasi berbentuk lingkaran yang dibagi menjadi beberapa sektor/irisan untuk menunjukkan proporsi persentase atau komposisi dari masing-masing kategori pada variabel kualitatif.
- Luas atau sudut dari setiap irisan sebanding dengan nilai persentase frekuensi relatif dari kategori yang diwakilinya.
- Sifat dari masing-masing kategori dalam diagram ini harus saling lepas (_mutually exclusive_) dan mencakup seluruh populasi data secara non-overlapping.
- Penggunaan alat ini sangat tidak direkomendasikan apabila variabel kualitatif memiliki terlalu banyak kategori karena akan menyulitkan perbandingan visual antarsektor yang sempit.

---

### E. Bar Chart

- Bar Chart (Diagram Batang) adalah representasi visual untuk data kategorikal yang digambarkan menggunakan batang persegi panjang dengan panjang atau tinggi yang sebanding dengan nilai kuantitatif yang diwakilinya.
- Berbeda dengan histogram yang batangnya saling menempel untuk menunjukkan kesinambungan data kontinu, batang pada Bar Chart memiliki jarak pemisah karena mewakili kategori diskret yang berbeda.
- Dalam analisis data tingkat lanjut, Bar Chart sering digunakan untuk melakukan agregasi nilai kuantitatif berdasarkan kategori tertentu menggunakan fungsi matematika spesifik (seperti nilai rata-rata, jumlah total, nilai minimum, nilai maksimum, atau simpangan baku).

#### [Wawasan Diskusi / Audio Insight]

- Dosen menguraikan bahwa dalam praktik ilmu data, Bar Chart sering digunakan untuk menunjukkan komposisi sekaligus hubungan antara satu variabel kuantitatif dengan satu variabel kategorikal. Bar Chart memungkinkan pembuat keputusan untuk membandingkan performa antarkategori secara langsung dan objektif berdasarkan hasil fungsi agregasi yang telah dihitung sebelumnya.

---

### F. Representasi Konseptual Berbasis Kode

Berikut adalah pemodelan konseptual dari visualisasi grafis statistika menggunakan representasi kode Python:

````
# Pemodelan visualisasi data berdasarkan tipe variabel
class GraphicalSummary:
    def __init__(self):
        self.numerical_plots = ["histogram", "boxplot", "scatterplot"]
        self.categorical_plots = ["pie_chart", "bar_plot"]
        self.mixed_plots = ["bar_plot", "boxplot"]

    def suggest_plot(self, variable_x_type, variable_y_type=None):
        if variable_y_type is None:
            if variable_x_type == "numerical":
                return self.numerical_plots[:2] # Suggest Histogram or Boxplot
            elif variable_x_type == "categorical":
                return self.categorical_plots
        else:
            if variable_x_type == "numerical" and variable_y_type == "numerical":
                return ["scatterplot"]
            elif (variable_x_type == "numerical" and variable_y_type == "categorical") or \
                 (variable_x_type == "categorical" and variable_y_type == "numerical"):
                return self.mixed_plots
        return []
```\n
````



## Bab 7 Diskusi Kuliah dan Relevansinya dengan AI Bootcamp


## 7.1 Buku Rekomendasi Kuliah

### A. Analisis Kritis Penyajian Data

- Dalam sesi perkuliahan, direkomendasikan sebuah buku klasik bidang statistika yang sangat berpengaruh yaitu _How to Lie with Statistics_ karya Darrell Huff.
- Buku ini menguraikan bagaimana metode-metode statistika dapat dimanfaatkan sebagai pedang bermata dua (_double-edged sword_).
- Melalui teknik manipulasi visualisasi grafik, pemilihan sampel yang bias, atau penyajian nilai rata-rata (_mean_) yang dipengaruhi pencilan pada data miring (_skewed data_), pelaku penyaji data dapat mengelabui pemahaman audiens tanpa harus memalsukan angka-angka matematisnya secara ilegal.
- Pemahaman kritis terhadap bias metodologi ini sangat penting agar praktisi tidak mudah teperdaya oleh laporan visual atau tajuk utama berita (_headline news_) yang menyesatkan.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa statistika sering kali menyajikan fakta yang secara matematis benar, namun perspektif dan cara interpretasi penyajiannya dibuat berbeda untuk mengarahkan opini publik. Oleh karena itu, sebagai profesional di bidang data, kita harus kritis dengan menanyakan asal-usul data, bagaimana sampel diambil, serta metode statistik apa yang digunakan sebelum mempercayai sebuah kesimpulan data.

---

## 7.2 Peran Statistika Bagi AI Engineer

### A. Validasi dan Pembersihan Data

- Peran statistika bagi seorang _AI Engineer_ (terutama yang berkutat di bidang _Generative AI_) sangat krusial dan tidak terbatas pada pemodelan matematika saja.
- **Validasi Keakuratan**: Pemahaman statistika mencegah terjadinya kepercayaan buta (_blind trust_) terhadap hasil performa model yang dideklarasikan oleh _Data Scientist_. Seorang _AI Engineer_ harus mampu mengaudit kelayakan model secara independen sebelum melakukan proses penyebaran model (_deployment_).
- **Pembersihan Data (_Data Cleaning_)**: Statistika menyediakan kerangka kerja ilmiah untuk mengidentifikasi data rusak, data bising (_noise_), dan pencilan yang dapat merusak kualitas pelatihan model _Machine Learning_.
- **Transformasi Distribusi**: Algoritma cerdas tertentu membutuhkan data input yang memenuhi asumsi distribusi normal. Statistika memberikan metode transformasi (seperti transformasi logaritma) untuk menormalkan sebaran data yang miring (_skewed_).

#### [Wawasan Diskusi / Audio Insight]

- Dosen menggarisbawahi bahwa di era perkembangan teknologi kecerdasan buatan modern, _AI Engineer_ tidak harus menghafal seluruh rumus rumit matematika teoretis. Namun, pemahaman konsep statistika dasar mutlak diperlukan untuk memastikan bahwa model yang diintegrasikan ke dalam sistem produksi benar-benar andal, bersih dari bias sampel, dan bekerja sesuai parameter fisis dunia nyata.

---

## 7.3 Penanganan Kasus Riil Data Science

### A. Deteksi Fraud Kartu Kredit

- Dalam skenario industri keuangan nyata, data pencilan (_outliers_) tidak boleh serta merta dihapus dari dataset pelatihan model.
- Pada kasus deteksi transaksi mencurigakan (_Fraud Detection_), transaksi ilegal/fraud merupakan kejadian yang sangat langka dengan proporsi berkisar antara 0.5% hingga 1% dari total populasi transaksi.
- Kejadian langka ini terdeteksi sebagai pencilan secara statistik. Jika praktisi menghapus seluruh pencilan dengan tujuan memperbagus bentuk distribusi data agar simetris, maka esensi dan tujuan utama dari pembuatan model deteksi fraud tersebut akan hilang sepenuhnya karena data transaksi ilegal telah terhapus dari sistem.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menegaskan pentingnya analisis _case-by-case_. Kita tidak boleh melakukan pukul rata untuk menghapus pencilan menggunakan aturan baku 1.5 IQR jika masalah bisnis utama kita justru berfokus pada analisis perilaku anomali tersebut.

---

### B. Penanganan Imbalanced Data

- Dataset dengan proporsi kelas yang sangat timpang (seperti 99% transaksi normal vs 1% transaksi fraud) disebut dengan istilah _Imbalanced Data_.
- **Bahaya Akurasi (_Misleading Accuracy_)**: Jika model _Machine Learning_ dilatih pada data yang sangat tidak seimbang tanpa penanganan khusus, model tersebut cenderung memprediksi semua masukan ke dalam kelas mayoritas. Model yang selalu menebak "transaksi normal" pada kasus di atas akan menghasilkan akurasi sebesar 99%, namun model tersebut tidak memiliki nilai guna praktis fungsional (_not meaningful_) karena gagal mendeteksi satu pun transaksi fraud.
- **Solusi Rekayasa Data (_Data Sampling_)**:
    - _Down-sampling_: Mengurangi jumlah sampel dari kelas mayoritas secara acak agar memiliki rasio seimbang (50:50) dengan kelas minoritas. Metode ini mengorbankan banyak volume data latih.
    - _Up-sampling_: Menambahkan jumlah sampel pada kelas minoritas dengan memproduksi data tiruan secara sintetik agar volumenya setara dengan kelas mayoritas.
- **Solusi Pemilihan Metrik Evaluasi**: Menghindari penggunaan metrik akurasi (_accuracy_), dan beralih ke metrik yang sensitif terhadap kelas minoritas seperti presisi (_precision_) dan _recall_.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menyimpulkan bahwa akurasi tinggi sering kali mengecoh praktisi pemula. Memahami kapan akurasi bersifat menyesatkan dan kapan harus menggunakan metrik _precision_ dan _recall_ adalah pembeda utama antara praktisi data yang kompeten dengan yang tidak.

---

### C. Representasi Konseptual Berbasis Kode

Berikut adalah pemodelan konseptual dari evaluasi model pada dataset tidak seimbang menggunakan representasi kode Python:

````
# Pemodelan evaluasi performa model pada imbalanced dataset
class ImbalancedDataEvaluator:
    def __init__(self, true_fraud, predicted_fraud):
        self.actual = true_fraud
        self.predicted = predicted_fraud

    def calculate_metrics(self):
        # Logika perhitungan presisi dan recall tanpa menggunakan akurasi yang bias
        true_positives = sum(1 for a, p in zip(self.actual, self.predicted) if a == 1 and p == 1)
        predicted_positives = sum(self.predicted)
        actual_positives = sum(self.actual)

        precision = true_positives / predicted_positives if predicted_positives > 0 else 0.0
        recall = true_positives / actual_positives if actual_positives > 0 else 0.0

        return {
            "Precision_Fokus_Presisi_Deteksi": precision,
            "Recall_Fokus_Cakupan_Deteksi": recall
        }
```\n
````



## Statistic

Art & science mentranslate data menjadi sebuah knowledge. 
Analisa disini bisa mengkonkretkan fenomena yang terjadi.

Aplikasi:
1. Experimen design: A/B testing. 
2. Survey:
3. Research
4. Quality Control


Step:
1. Design: Formulasi masalah, populasi dan data collection.
2. Description: Menyimpulkan dan explorasi data. 
3. Inference: Membuat prediksi dan mengeneralisasi fenomena dengan data tsb. 

Tipe statistik:

1. Deskriptif: summarize dan describe. 
2. Inferential: Menggunakan sample. 

Data, varibales dan scale of measurement:
1. Data adalah individual unit of infomration.
	1. Kolom variable. 
	2. Row observation unit. 

## Ringkasan Variabel Statistik

- **Kualitatif (Kategorikal):** Data berupa label, nama, atau kategori. Bukan angka yang bisa dihitung secara matematis.
    
    - **Nominal:** Data kategorikal yang **tidak ada urutan atau tingkatannya**. Semuanya setara. (Catatan: Bukan uang).
        
        - _Contoh:_ Jenis material (Plastik PET, Kertas, Logam), jenis kelamin, atau warna mobil.
            
    - **Ordinal:** Data kategorikal yang **ada urutan atau tingkatannya**, tetapi jarak antar tingkatannya tidak memiliki nilai matematis yang pasti.
        
        - _Contoh:_ Tingkat kualitas barang (Grade A, Grade B, Grade C), tingkat kepuasan (Buruk, Sedang, Baik).
            
- **Kuantitatif (Numerikal):** Data berupa angka nyata yang bisa dihitung dengan interval atau rasio.
    
    - **Diskrit (Discrete):** Data yang diperoleh dari hasil **menghitung**. Nilainya pasti terpisah-pisah dan berupa bilangan bulat (tidak mungkin ada nilai koma/desimal).
        
        - _Contoh:_ Jumlah truk yang masuk ke fasilitas hari ini, jumlah armada, jumlah karyawan. (Tidak mungkin ada 1,5 truk).
            
    - **Kontinu (Continuous):** Data yang diperoleh dari hasil **mengukur**. Nilainya berkesinambungan dan bisa berupa pecahan atau desimal sedetail mungkin.
        
        - _Contoh:_ Berat total muatan (misalnya 15,45 ton), suhu ruangan, atau jarak tempuh perjalanan.

Data analysis akan tergantung tipe datanya. 


Population: dikaratkeristikan sebagai set of individual or object yang menjadi insterest dalam penelitian. 
1. Population parameter: sebuah rinkasan numerik dari sample yang diambil dari populasi. 

Sample: Set of individual or object yang menjadi representasi dari sebuah populasi. 
1. Mengapa butuh sample"
	1. Batasan waktu
	2. Batasan biaya
	3. Btasan sumber daya
2. Metode melakukan sample adalah sampling.
	1. harus represent populasi. 
	2. Harus didefinisikan frame smaplingnya
	3. random
3. Jenis:
	1. Simple random sampling: acak.
	2. Stratified sample: dipilih golongannya dari grup secara random
	3. Systematic sampling: diambil acar dari populasi dengan interval yang diset. 
	4. Cluster sampling: merepresentasikan geografis tertentu. 

Randomness:
1. Kesalahan randomness membuat data bias. 

Good experiment:
1. Memiliki kelompok kontrol. Diambil random. Blinding (penyamaran).
2. Experimental unit: subject yang dikenakan experiment. 
3. Treatment: kondisi yang titetapkan. 
4. Randomness: 


Deskriptive statistics:
1. Mempresentasikan hasil analisa statistic. 


Histogram:
1. Cara simple melihat distribusi single variable. 
## Penjelasan Bentuk Distribusi Histogram

- **Symmetric atau Normally Distributed (Distribusi Normal)**
    
    - **Definisi:** Data terpusat di tengah dan bentuknya simetris seperti lonceng (_bell curve_). Pada distribusi ini, nilai rata-rata (_mean_), nilai tengah (_median_), dan nilai yang paling sering muncul (_modus_) posisinya hampir sama di tengah-tengah.
        
    - **Contoh Praktis:** Berat standar _bale_ kardus hasil mesin _press_. Mayoritas _bale_ akan berada di sekitar berat rata-rata (misal 500 kg), dengan sedikit _bale_ yang meleset menjadi terlalu ringan atau terlalu berat.
        
- **Right Skewed (Condong ke Kanan / Skewness Positif)**
    
    - **Definisi:** "Ekor" grafik memanjang ke arah kanan. Ini berarti sebagian besar data justru menumpuk di nilai-nilai rendah (sebelah kiri), tetapi ada beberapa data ekstrem (_outlier_) yang nilainya sangat tinggi sehingga menarik rata-ratanya ke kanan.
        
    - **Contoh Praktis:** Waktu perbaikan atau _downtime_ mesin operasional. Sebagian besar perbaikan biasanya cepat diselesaikan (nilai rendah di kiri), tetapi sesekali ada kerusakan parah yang memakan waktu berhari-hari untuk diperbaiki (ekor panjang di kanan).
        
- **Left Skewed (Condong ke Kiri / Skewness Negatif)**
    
    - **Definisi:** Kebalikan dari _right skewed_, "ekor" grafik memanjang ke arah kiri. Sebagian besar data menumpuk di nilai-nilai tinggi (sebelah kanan), namun ada beberapa data ekstrem yang nilainya sangat rendah.
        
    - **Contoh Praktis:** Pemenuhan kapasitas muatan truk sebelum dikirim ke pabrik peleburan. Kebanyakan truk akan berangkat dengan kapasitas muatan yang hampir penuh (menumpuk di kanan), tetapi sesekali ada truk yang terpaksa berangkat dengan muatan sedikit karena alasan mendesak (ekor di kiri).
        
- **Bimodal**
    
    - **Definisi:** Memiliki dua puncak (_modus_) yang menonjol. Ini biasanya menjadi petunjuk kuat bahwa ada dua kondisi, kelompok, atau sifat berbeda yang tercampur di dalam satu kumpulan data tersebut.
        
    - **Contoh Praktis:** Jam kedatangan suplai material. Puncak pertama mungkin terjadi di pagi hari (misal jam 09:00 - 10:00) saat pengiriman pertama, dan puncak kedua terjadi di sore hari (misal jam 15:00 - 16:00) untuk pengiriman penutup.
        
- **Uniform (Seragam)**
    
    - **Definisi:** Distribusi data terlihat datar atau merata. Frekuensi kemunculan untuk setiap rentang nilai hampir sama, tidak ada satu nilai pun yang mendominasi.
        
    - **Contoh Praktis:** Pengeluaran rutin untuk barang habis pakai harian (seperti karung atau sarung tangan kerja) di mana jumlah permintaannya relatif konstan dan stabil setiap hari tanpa ada fluktuasi atau lonjakan berarti.

mengetes normal distribusi data:


Scatterplot:
1. Melihat korelasi antar 2 variable numerikal.
2. 



---


# Module 1 Session 12 Python Data Manipulation With Pandas and Numpy


## Bab I Pendahuluan Analisis Data (Introduction to Data Analysis)


## 1.1 Definisi dan Landasan Analisis Data (Introduction to Data Analysis)

### A. Konsep Dasar dan Definisi

- _Data Analysis_ adalah proses penemuan (discovery) dan penyampaian (communication) pola-pola yang bermakna (meaningful patterns) di dalam data.
- _Analytics_ didefinisikan sebagai scientific process untuk mentransformasikan data menjadi _insight_ guna mendukung pengambilan keputusan yang lebih baik.
- Bidang _analytics_ mengandalkan penerapan secara simultan dari beberapa disiplin ilmu, yaitu:
- _Statistics_ (Statistika).
- _Computer programming_ (Pemrograman Komputer).
- _Operations research_ (Riset Operasi).

### B. Tujuan dan Peran Visualisasi Data

- Tujuan utama dari _Data Analysis_ adalah memperoleh _actionable insights_ yang dapat menghasilkan keputusan yang lebih cerdas (smarter decisions) serta hasil bisnis yang lebih baik (better business outcomes).
- Dalam menyampaikan temuan atau wawasan (_insights_), proses _Data Analysis_ sangat mengutamakan penggunaan _data visualization_ agar informasi tersebut lebih mudah dipahami dan dikomunikasikan secara efektif.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa di era modern ini, tantangan utama organisasi bukanlah ketiadaan data, melainkan melimpahnya data yang dimiliki tanpa adanya kemampuan untuk memanfaatkannya secara optimal (_too much data and unable to utilize it_). Hal inilah yang mendorong tingginya permintaan terhadap peran-peran seperti _data analyst_ dan _data scientist_ dalam beberapa tahun terakhir.
- Dosen menekankan bahwa jika hasil analisis data tidak dapat dipahami oleh pengambil keputusan, maka data tersebut tidak akan berguna. Oleh karena itu, _data visualization_ menjadi metode krusial untuk menjembatani wawasan teknis dengan keputusan strategis.

---

## 1.2 Bahasa Pemrograman Python dalam Analisis Data (Why Python?)

### A. Karakteristik Python sebagai Alat Analisis

- Python merupakan bahasa pemrograman yang bersifat _open source_ (bebas digunakan tanpa biaya lisensi), _interpreted_, _high level language_, dan mendukung pendekatan _object-oriented programming_ yang sangat baik.
- Kemudahan penggunaan (_ease of use_) dan sintaksis yang sederhana (_simple syntax_) menjadikan Python mudah diadaptasi oleh individu yang tidak memiliki latar belakang pemrograman (_coding background_).
- Python menyediakan fungsionalitas dan pustaka lengkap untuk menangani perhitungan matematika (_mathematics_), statistik (_statistics_), dan fungsi ilmiah (_scientific functions_) yang dibutuhkan dalam aplikasi _data science_.

### B. Relevansi Industri

- Python diakui sebagai salah satu bahasa pemrograman terbaik yang digunakan secara luas oleh para _data scientist_ untuk berbagai proyek dan aplikasi _data science_.

#### [Wawasan Diskusi / Audio Insight]

- Dosen memaparkan bahwa sifat Python sebagai _high-level language_ membuatnya sangat mendekati bahasa manusia, sehingga kodenya jauh lebih intuitif untuk dipahami oleh pemula sekalipun.
- Relevansi penggunaan Python dalam analisis data ini sangat sejalan dengan kurikulum dan kompetensi yang dipelajari peserta didik dalam program _bootcamp_ saat ini.

---

## 1.3 Library Utama Analisis Data (NumPy & Pandas Overview)

### A. NumPy (Numerical Python)

- NumPy adalah library Python yang menyediakan fungsi matematika berkinerja tinggi untuk menangani _large dimension array_.
- Library ini menyediakan fitur komputasi untuk operasi _n-arrays_ dan matriks (matrices) di Python.
- Keunggulan utama NumPy adalah kemampuan _vectorization_ pada operasi matematika terhadap tipe array NumPy, yang meningkatkan performa dan mempercepat waktu eksekusi program.
- NumPy mempermudah pengerjaan dengan array dan matriks multidimensi berskala besar.

### B. Pandas

- Pandas adalah library Python yang sangat populer dan dirancang untuk manipulasi dan analisis data terstruktur.
- Pandas menyediakan metode termudah untuk melakukan analisis data, manipulasi, agregasi, serta visualisasi terhadap data terstruktur dalam jumlah besar.
- Pandas merupakan alat yang sangat ideal untuk proses _data wrangling_.
- Pandas memiliki dua struktur data utama, yaitu:

1. _Series_: Digunakan untuk menangani dan menyimpan data satu dimensi (one-dimensional data).
2. _DataFrame_: Digunakan untuk menangani dan menyimpan data dua dimensi (two-dimensional data).

#### [Wawasan Diskusi / Audio Insight]

- **Perbandingan NumPy dengan Library Math Standar bawaan Python**: Dosen menjelaskan bahwa meskipun Python memiliki library bawaan bernama `math`, library tersebut tidak dirancang untuk menangani struktur data _array_ atau matriks berdimensi tinggi. NumPy hadir khusus untuk memproses operasi matematika pada array berdimensi besar (_higher dimension arrays_) dengan performa yang sangat cepat.
- **Struktur Array dalam NumPy**: Dosen memberikan analogi bahwa array satu dimensi (1D array) mirip dengan struktur List horizontal di Python, sedangkan array dua dimensi (2D array) analog dengan struktur _list of list_. NumPy bahkan mampu mendukung komputasi hingga array 10 dimensi.
- **Relevansi NumPy dalam AI dan Machine Learning**: Di dalam pengembangan AI atau _machine learning_, seluruh nilai data disimpan di dalam struktur array. Nilai-nilai tersebut tidak disimpan menggunakan tipe data Python List standar karena proses perhitungannya yang lambat. Sebagai solusinya, data tersebut dibungkus dalam tipe data NumPy Array guna mempercepat proses pelatihan model (_training process_).
- **Hubungan Integrasi NumPy dan Pandas**: Dosen menjelaskan bahwa saat melakukan instalasi Pandas (misalnya melalui instruksi instalasi pustaka), sistem secara otomatis juga menginstal NumPy. Hal ini dikarenakan _under the hood_ (di bawah kap mesinnya), Pandas dibangun di atas NumPy dan menggunakan library NumPy untuk merepresentasikan serta menyimpan objek _Series_ dan _DataFrame_. Integrasi tingkat rendah ini yang membuat pemrosesan data di Pandas menjadi sangat cepat.
- **Perbedaan Series dan DataFrame**: Secara sederhana, Dosen menjelaskan bahwa _DataFrame_ berbentuk tabel (dua dimensi), sedangkan _Series_ hanya terdiri dari satu kolom saja (satu dimensi).

---

## 1.4 Tabel Istilah Teknis dan Karakteristik

Berikut adalah tabel rangkuman istilah teknis dan karakteristik library yang digunakan dalam materi pendahuluan ini:

|Istilah Teknis / Library|Karakteristik dan Deskripsi Utama|
|:--|:--|
|_Data Analysis_|Proses penemuan (discovery) dan komunikasi pola bermakna di dalam data untuk pengambilan keputusan berbasis bukti.|
|_Actionable Insights_|Temuan atau wawasan dari data yang dapat langsung diimplementasikan menjadi tindakan bisnis yang strategis.|
|_Data Visualization_|Metode penyampaian temuan analisis secara visual agar lebih mudah dipahami oleh pengambil keputusan.|
|_Data Wrangling_|Proses pembersihan, penataan, dan manipulasi data terstruktur agar siap dianalisis lebih lanjut.|
|_NumPy Array_|Tipe data terstruktur yang menyimpan nilai homogen (tipe data sama), bersifat mutable, berindeks mulai dari 0, dan mendukung dimensi n-D.|
|_Series_|Struktur data satu dimensi (1D) pada Pandas yang mendukung indeks berlabel (axis labels) dan objek Python arbitrer.|
|_DataFrame_|Struktur data dua dimensi (2D) pada Pandas berbentuk tabel yang terdiri dari kumpulan objek Series yang berbagi indeks yang sama.|

---

## 1.5 Panduan Instalasi dan Impor Library

Untuk memulai analisis data menggunakan Python, kedua library utama ini harus diinstal dan diimpor terlebih dahulu ke dalam lingkungan pemrograman.

### A. Instruksi Instalasi

Kedua library ini merupakan _external packages_, sehingga harus diinstal terlebih dahulu menggunakan package manager seperti `pip` atau `conda`.

```
pip install numpy
pip install pandas
```

### B. Instruksi Impor Library

Dalam konvensi pemrograman Python, library diimpor menggunakan alias standar untuk menyingkat penulisan kode.

```
import numpy as np
import pandas as pd
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa penamaan alias seperti `np` untuk NumPy dan `pd` untuk Pandas bukanlah aturan mutlak bahasa pemrograman, melainkan sebuah konvensi atau kesepakatan bersama (_convention_) di kalangan data scientist untuk mempermudah penulisan kode. Programmer bebas menggunakan alias lain seperti `npy` atau bahkan tidak menggunakan alias sama sekali, namun sangat direkomendasikan mengikuti konvensi industri ini.
- Dosen menyarankan agar proses instalasi pustaka eksternal ini dilakukan di dalam lingkungan virtual (_virtual environment_) yang terisolasi (seperti Anaconda Environment) untuk menghindari konflik versi antar proyek.



## Bab II Pemrograman NumPy (Numerical Python) Array


## 2.1 Pengenalan Array (Introduction to Array)

### A. Fondasi Konseptual

- _Array_ adalah tipe data terstruktur yang menyimpan beberapa nilai dengan tipe data yang sama (homogen).
- Karakteristik utama dari array adalah:
    - Bersifat _mutable_ (nilainya dapat diubah setelah didefinisikan).
    - Menggunakan sistem indeks berbasis nol (_zero-based indexing_) yang dimulai dari angka 0.
    - Dapat berbentuk satu dimensi (1D), dua dimensi (2D/Matriks), tiga dimensi (3D), hingga banyak dimensi (nD).

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan bahwa struktur array satu dimensi (1D) secara visual analog dengan List horizontal dasar di Python, sedangkan array dua dimensi (2D) analog dengan struktur _list of list_. Untuk komputasi tingkat tinggi, NumPy mampu mendukung representasi data hingga 10 dimensi.

---

## 2.2 Kelebihan NumPy Array (Advantages of NumPy Array)

### A. Performa dan Efisiensi Memori

- Kecepatan eksekusi NumPy Array mencapai hingga 50 kali lebih cepat dibandingkan dengan Python List standar.
- Sangat efisien dalam alokasi memori dan pengelolaan sumber daya komputasi, menjadikannya pilihan utama untuk pemrosesan data berskala besar (_large-scale data_).

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa dalam pengembangan Kecerdasan Buatan (AI) dan _Machine Learning_, seluruh data wajib disimpan dalam bentuk array. Nilai-nilai data ini tidak disimpan menggunakan tipe data Python List standar karena proses perhitungan matematika pada List standar sangat lambat. Dosen menyajikan contoh kasus pengujian komputasi (_time execution_) di mana operasi penjumlahan vektor menggunakan NumPy Array terbukti berjalan puluhan kali lipat lebih cepat dibandingkan perulangan (_looping_) pada Python List biasa. Oleh karena itu, penggunaan NumPy Array adalah mutlak di bidang data science di mana kecepatan (_speed_) dan optimalisasi sumber daya (_resource optimization_) menjadi prioritas.

---

## 2.3 Cara Instalasi dan Pemakaian (Installation and Usage)

### A. Prosedur Teknis

- Karena NumPy merupakan library eksternal (_external package_), pengguna harus menginstalnya terlebih dahulu menggunakan package manager seperti `pip` atau `conda`.
- Impor pustaka di dalam script Python dilakukan menggunakan alias standar konvensional untuk menyingkat penulisan kode.

#### [Wawasan Diskusi / Audio Insight]

- Dosen merekomendasikan agar proses instalasi pustaka ini dilakukan di dalam lingkungan virtual (_virtual environment_) yang terisolasi (seperti Anaconda Environment) untuk menghindari konflik versi antar proyek pemrograman yang berbeda.

---

## 2.4 Pembuatan Array (Array Creation)

### A. Metode Konversi Objek Python

- NumPy Array dapat dibuat dengan mengonversi objek Python List (untuk array 1D) atau _List of List_ (untuk matriks/array 2D atau 3D) menggunakan fungsi `np.array()`.

### B. Metode Pembuatan Otomatis (Built-in Functions)

NumPy menyediakan berbagai fungsi bawaan untuk menghasilkan array secara otomatis tanpa mendefinisikan list manual:

- `np.arange()`: Membuat array dengan jangkauan nilai tertentu dari batas awal (_start_) hingga sebelum batas akhir (_stop_) dengan parameter langkah (_step_) tertentu.
- `np.zeros()`: Membuat array berisi angka 0 (mendukung dimensi 1D maupun multidimensi dengan parameter tuple bentuk).
- `np.ones()`: Membuat array berisi angka 1.
- `np.eye()`: Membuat matriks identitas (matriks persegi diagonal di mana nilai diagonal utamanya adalah 1 dan elemen lainnya adalah 0).
- `np.linspace()` (_linear space_): Membuat array dengan membagi interval angka tertentu menjadi beberapa elemen dengan jarak yang sama besar.

### C. Metode Pembuatan Acak (np.random Module)

Fungsi penghasil bilangan acak dalam modul `np.random` meliputi:

- `np.random.rand()`: Membuat array berisi angka desimal acak (_float_) dengan distribusi seragam (_uniform distribution_) di dalam interval [0, 1).
- `np.random.randn()`: Membuat array berisi angka acak berdasarkan distribusi normal standar (_normally distributed_ dengan mean = 0 dan standar deviasi = 1).
- `np.random.randint()`: Membuat array berisi bilangan bulat acak (_integer_) dengan menentukan batas minimum, batas maksimum (eksklusif), dan jumlah data yang diinginkan.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan perbedaan fungsional antara `np.arange()` dan `np.linspace()`. Fungsi `np.arange()` menerima parameter _step_ (selisih nilai antar elemen), sedangkan `np.linspace()` menerima parameter jumlah total elemen yang diinginkan (_count_), di mana NumPy secara otomatis menghitung selisih jarak yang sama (_equal space_) antar elemen tersebut. Sebagai contoh, jika memanggil `np.linspace(0, 10, 50)`, NumPy akan menghasilkan 50 angka acak dengan jarak yang sama persis dari 0 hingga 10.
- Dosen menjelaskan matriks identitas yang dihasilkan oleh `np.eye(4)` sebagai matriks 4x4 dengan angka 1 yang berbaris diagonal secara menyilang dari kiri atas ke kanan bawah, dan sisanya bernilai 0.
- Terkait modul acak, Dosen menyoroti pentingnya menggunakan `np.random.randint()` untuk menghasilkan bilangan bulat guna menghindari output berupa desimal panjang (_float_) yang dihasilkan oleh `np.random.rand()` atau `np.random.randn()`.

---

## 2.5 Atribut dan Method NumPy Array (Attributes and Methods)

### A. Atribut Struktural dan Tipe Data

- `.shape`: Mengembalikan dimensi dari array dalam format tuple (misalnya `(3,)` untuk array 1D berisi 3 elemen, atau `(3, 3)` untuk matriks 2D).
- `.reshape()`: Mengubah dimensi atau bentuk bentuk array (misalnya dari satu dimensi ke matriks dua dimensi) tanpa memodifikasi data aslinya.
- `.dtype`: Menunjukkan tipe data elemen dalam array beserta presisi memorinya (misalnya `int32` yang menggunakan memori 32 bits vs `int64` yang menggunakan 64 bits).

### B. Method Statistik Nilai Ekstrem

- `.max()`: Mengembalikan nilai terbesar di dalam array.
- `.min()`: Mengembalikan nilai terkecil di dalam array.
- `.argmax()`: Mengembalikan posisi indeks dari nilai terbesar.
- `.argmin()`: Mengembalikan posisi indeks dari nilai terkecil.

#### [Wawasan Diskusi / Audio Insight]

- **Aturan Reshape -1**: Dosen membagikan teknik penting mengenai penggunaan nilai parameter `-1` pada method `.reshape()`. Jika kita memberikan parameter `-1` (seperti `.reshape(-1)`), NumPy akan meratakan (_flatten_) dimensi array dari bentuk apa pun (2D atau 3D) kembali menjadi array satu dimensi (1D) secara otomatis tanpa kita perlu menghitung secara manual jumlah elemennya.
- **Konsep Presisi Data**: Dosen mencontohkan bahwa array yang berisi bilangan bulat acak default biasanya bertipe `int32` atau `int64` tergantung pada sistem operasinya, sedangkan array yang dibuat melalui pembagian interval seperti `np.linspace()` otomatis bertipe data desimal `float64`.

---

## 2.6 Indexing dan Slicing pada NumPy Array

### A. Pengambilan Elemen Tunggal

- Untuk array satu dimensi (1D), pengambilan elemen menggunakan kurung siku tunggal `[indeks]`.
- Untuk array dua dimensi (2D), pengambilan elemen dilakukan menggunakan koordinat baris dan kolom dengan format `[indeks_baris, indeks_kolom]`.

### B. Pemotongan Array (_Slicing_)

- Pemotongan array menggunakan operator titik dua `:` dengan sintaksis `[start:stop:step]`.
- Aturan mutlak slicing di NumPy: **"A slice is a view, not a copy"**. Saat kita melakukan slicing pada suatu array dan menyimpan hasilnya ke variabel baru, variabel baru tersebut hanyalah sebuah pandangan (_view_) yang merujuk pada memori array aslinya. Jika nilai di dalam slice tersebut diubah, data pada array aslinya akan ikut berubah.
- Untuk menduplikasi data secara independen agar array asli tidak terpengaruh, kita wajib menggunakan method `.copy()` secara eksplisit.

### C. _Fancy Indexing_

- Mengakses beberapa baris atau kolom spesifik secara non-berurutan dengan mengirimkan list indeks di dalam tanda kurung siku ganda `[[indeks1, indeks2, ...]]`.

#### [Wawasan Diskusi / Audio Insight]

- Dosen memperingatkan bahaya modifikasi data pada hasil slicing tanpa menyalinnya terlebih dahulu. Jika kita menuliskan `slice_of_arr[:] = 99`, maka seluruh elemen array asli pada rentang tersebut juga akan berubah menjadi 99 karena kedua variabel merujuk pada alamat memori yang sama (_by reference_). Solusinya adalah selalu menggunakan `arr.copy()` ketika ingin memanipulasi potongan data tanpa merusak data mentah asli.
- Dosen menunjukkan bahwa penulisan indeks 2D dapat dilakukan dengan dua cara: format tradisional `arr[baris][kolom]` atau format yang lebih bersih dan direkomendasikan (_cleaner format_) yaitu `arr[baris, kolom]`.

---

## 2.7 Operasi Aritmatika & Broadcasting

### A. Operasi Element-wise

- Seluruh operasi aritmatika standar (seperti `+`, `-`, `*`, `/`) pada NumPy Array dilakukan secara _element-wise_ (operasi diterapkan secara individual pada setiap elemen yang bersesuaian), bukan menggunakan aturan perkalian matriks aljabar linier standar.

### B. Aturan Penyiaran (_Broadcasting Rules_)

- _Broadcasting_ adalah mekanisme otomatis di mana NumPy menangani operasi aritmatika antara dua array dengan bentuk (_shape_) yang berbeda. Array yang lebih kecil akan "diregangkan" secara virtual agar kompatibel dengan array yang lebih besar.
- Syarat kompatibilitas dimensi dinilai mulai dari sumbu paling kanan (_trailing rightmost axis_) bergerak ke arah kiri. Dua dimensi dinyatakan kompatibel jika:
    1. Ukuran dimensi pada sumbu tersebut sama besar, ATAU
    2. Salah satu dimensi pada sumbu tersebut bernilai tepat 1.

### C. Fungsi Matematika NumPy (Universal Functions)

NumPy menyediakan fungsi matematika instan yang beroperasi secara _element-wise_ pada array, antara lain:

- `np.sqrt()`: Menghitung akar kuadrat dari setiap elemen.
- `np.exp()`: Menghitung eksponensial basis $e$ pangkat elemen ($e^x$).
- `np.sin()`: Menghitung nilai trigonometri sinus.
- `np.log()`: Menghitung logaritma natural (basis $e$).

### D. Operator Perbandingan dan Filtering (Masking)

- Operator perbandingan (seperti `> arr`) akan menghasilkan array bertipe boolean (_True_ atau _False_) untuk setiap elemen. Array boolean ini dapat digunakan sebagai filter (mask) untuk menyaring elemen-elemen tertentu dari array asli.

#### [Wawasan Diskusi / Audio Insight]

- Dosen memberikan contoh konkret kalkulasi _broadcasting_ antara array $A$ berukuran $4 \times 3$ dan array $B$ berukuran $1 \times 3$ (atau skalar tunggal). Array $B$ akan diregangkan secara virtual ke bawah untuk meniru baris-baris array $A$ sehingga operasi dapat dijalankan.
- Dosen memaparkan kasus eror _broadcasting_ yang sering dialami mahasiswa, misalnya melakukan operasi antara array $4 \times 3$ dan array berukuran $4$ (tanpa dimensi kedua). Sumbu paling kanan dari array pertama adalah 3, sedangkan sumbu paling kanan dari array kedua adalah 4. Karena nilainya tidak sama dan tidak ada yang bernilai 1, operasi tersebut akan memicu eror ketidakcocokan dimensi. Solusi untuk memperbaikinya adalah dengan melakukan _reshape_ pada array kedua menjadi $4 \times 1$ terlebih dahulu agar sumbu paling kanan bernilai 1, sehingga kompatibel untuk diregangkan secara virtual.
- Terkait fungsi `np.exp()`, Dosen meluruskan pemahaman mahasiswa bahwa rumus perhitungan eksponensial ini adalah menaikkan konstanta matematika $e$ (sekitar 2.718) ke pangkat nilai elemen array tersebut, bukan sebaliknya.

---

## 2.8 Fungsi NumPy Tambahan (Additional NumPy Functions)

### A. Manipulasi Struktur Array

- `np.where()`: Berfungsi untuk melakukan penyaringan berbasis kondisi dan mengganti elemen array secara kondisional. Formatnya adalah `np.where(kondisi, nilai_jika_benar, nilai_jika_salah)`.
- `np.insert()`: Menyisipkan elemen ke dalam array pada posisi indeks tertentu.
- `np.concatenate()`: Menggabungkan dua atau lebih array sepanjang sumbu (_axis_) yang ditentukan.
- `np.transpose()` atau atribut `.T`: Membalikkan dimensi array (baris menjadi kolom, dan sebaliknya).
- `np.flatten()`: Meratakan array multidimensi menjadi array satu dimensi (1D).
- `np.stack()`: Menumpuk array sepanjang sumbu baru.
- `np.split()`: Membagi satu array menjadi beberapa sub-array kecil.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan kegunaan praktis `np.where()` untuk membersihkan data, misalnya mengganti seluruh nilai negatif dalam array dengan angka 0 tanpa merusak nilai positifnya.
- Dosen mendemonstrasikan bahwa melakukan operasi `.transpose()` pada matriks $2 \times 3$ akan mengubah bentuknya secara instan menjadi matriks $3 \times 2$ dengan memutar baris menjadi kolom.

---

## 2.9 Rangkuman Istilah Teknis dan Karakteristik

Berikut adalah tabel rangkuman istilah teknis dan karakteristik pemrosesan data menggunakan library NumPy:

|Istilah Teknis / Library|Karakteristik dan Deskripsi Utama|
|:--|:--|
|_Vectorization_|Penerapan operasi matematika secara simultan pada seluruh elemen array tanpa memerlukan perulangan (_loop_) manual.|
|_Broadcasting_|Aturan otomatis NumPy untuk menyesuaikan dimensi array yang berbeda bentuk agar dapat dioperasikan secara aritmatika.|
|_Mutable_|Sifat dari objek array yang memungkinkan pengubahan nilainya secara langsung di memori setelah objek tersebut didefinisikan.|
|_View_|Representasi visual atau referensi potongan data (_slice_) yang merujuk langsung ke memori array asli, bukan salinan independen.|
|_Fancy Indexing_|Teknik pemanggilan beberapa elemen spesifik pada indeks non-berurutan menggunakan kurung siku ganda.|
|_Universal Functions_|Fungsi-fungsi matematika bawaan NumPy yang dioptimalkan untuk eksekusi cepat pada setiap elemen array (_element-wise_).|
|_Identity Matrix_|Matriks diagonal khusus di mana seluruh elemen pada diagonal utama bernilai 1 dan elemen lainnya bernilai 0.|

---

## 2.10 Panduan Sintaksis dan Praktik Kode

### A. Contoh Pembuatan dan Manipulasi Dasar Array

Di bawah ini adalah implementasi praktis pembuatan array, pengubahan dimensi, slicing, serta operasi aritmatika menggunakan NumPy.

```
import numpy as np

# 1. Membuat array dari Python List
list_data = [1, 2, 3, 4, 5]
arr_1d = np.array(list_data)

# 2. Membuat matriks 2D dari List of List
matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr_2d = np.array(matrix_data)

# 3. Membuat array otomatis dengan np.arange dan np.linspace
arr_range = np.arange(0, 11, 2)  # Menghasilkan [0, 2, 4, 6, 8, 10]
arr_linear = np.linspace(0, 10, 5)  # Menghasilkan 5 angka berjarak sama dari 0 hingga 10

# 4. Membuat array acak bilangan bulat
arr_random_int = np.random.randint(1, 100, 10)  # 10 angka acak bulat antara 1 s.d. 99

# 5. Mengubah bentuk dimensi (reshape)
arr_flat = np.arange(12)  # 0 s.d. 11
matrix_3x4 = arr_flat.reshape(3, 4)  # Mengubah menjadi matriks 3 baris 4 kolom
arr_recovered = matrix_3x4.reshape(-1)  # Meratakan kembali menjadi 1D array
```

### B. Contoh Slicing, Copy, dan Filtering

Implementasi pengambilan subset data, penyalinan memori yang aman, dan teknik penyaringan nilai (_filtering_).

```
import numpy as np

# Inisialisasi array awal
arr = np.arange(0, 11)

# Slicing dan bahaya "View"
potongan_view = arr[0:6]
potongan_view[:] = 99  # Mengubah potongan akan mengubah array asli!

# Menggunakan .copy() untuk keamanan data
arr_reset = np.arange(0, 11)
potongan_copy = arr_reset[0:6].copy()
potongan_copy[:] = 100  # Array asli (arr_reset) tetap aman tidak berubah

# Filtering berdasarkan kriteria boolean (Masking)
arr_data = np.array([5, 12, 8, 21, 3, 15])
kondisi_filter = arr_data > 10  # Menghasilkan [False, True, False, True, False, True]
hasil_saring = arr_data[kondisi_filter]  # Menghasilkan [12, 21, 15]
```

---

## 2.11 Tugas Latihan Kuliah (Exercises)

### Latihan 1: Pembuatan Bordered Grid (Tepi Matriks)

```
import numpy as np

# Langkah 1: Buat matriks 10x10 berisi angka 0
grid = np.zeros((10, 10))

# Langkah 2: Timpa tepi baris pertama dan baris terakhir dengan angka 4
grid[0, :] = 4
grid[-1, :] = 4

# Langkah 3: Timpa tepi kolom pertama dan kolom terakhir dengan angka 4
grid[:, 0] = 4
grid[:, -1] = 4

# Cetak hasil matriks bordered
print(grid)
```

### Latihan 2: Pembuatan Random Matrix & Reverse Rows

```
import numpy as np

# Simulasi input pengguna
banyak_data = 16
batas_bawah = 1
batas_atas = 50

# Langkah 1: Bangkitkan array 1D dari bilangan bulat acak
arr_1d = np.random.randint(batas_bawah, batas_atas + 1, banyak_data)

# Langkah 2: Ubah menjadi matriks 2D berdimensi 4x4
matrix_2d = arr_1d.reshape(4, 4)
print("Matriks 2D Awal:")
print(matrix_2d)

# Langkah 3: Balikkan urutan kolom pada setiap baris secara horizontal
matrix_reversed = matrix_2d[:, ::-1]
print("\nMatriks 2D Setelah Reverse Columns:")
print(matrix_reversed)
```



## Bab III Pandas - DataFrame & Manipulasi Data


## 3.1 Pengenalan Pandas

### A. Konsep Dasar Pandas

- Pandas adalah library tingkat tinggi (high-level data manipulation tool) yang dirancang untuk analisis dan manipulasi data terstruktur secara cepat dan efisien.
- Library ini dikembangkan oleh Wes McKinney dan dibangun di atas paket NumPy, yang menjadikannya sangat andal untuk melakukan manipulasi datatabular.
- Pandas merupakan alat utama yang sangat ideal untuk proses data wrangling (pembersihan, penataan, dan transformasi data mentah).

### B. Struktur Data Utama: Series vs DataFrame

- **Series**: Struktur data satu dimensi (1D) yang serupa dengan array 1D pada NumPy, tetapi memiliki kelebihan berupa indeks berlabel (axis labels) dan mampu menyimpan tipe objek Python apa pun (tidak harus numerik).
- **DataFrame**: Struktur data dua dimensi (2D) berbentuk tabel yang terdiri dari baris dan kolom (seperti spreadsheet atau tabel database). DataFrame dapat dianalogikan sebagai kumpulan objek Series yang digabungkan bersama dan berbagi indeks yang sama.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa saat melakukan instalasi Pandas (melalui pip atau conda), sistem secara otomatis juga menginstal NumPy. Di bawah kap mesinnya (under the hood), Pandas menggunakan library NumPy untuk merepresentasikan dan menyimpan objek Series dan DataFrame. Integrasi tingkat rendah ini menjadi alasan mengapa pemrosesan data tabular menggunakan Pandas dapat berjalan dengan sangat cepat.
- Dosen juga memberikan penjelasan bahwa DataFrame merupakan workhorse (kuda beban) dari seluruh analisis data menggunakan Pandas, yang strukturnya terinspirasi langsung dari bahasa pemrograman R.

---

## 3.2 Pembuatan Pandas Series dan DataFrame

### A. Cara Membuat Series

- Series dapat dibuat dari berbagai tipe objek Python seperti list, NumPy array, maupun dictionary menggunakan fungsi `pd.Series()`.
- Jika dibuat menggunakan dictionary, key pada dictionary tersebut otomatis akan menjadi indeks berlabel, dan value akan menjadi nilai datanya.

### B. Cara Membuat DataFrame

- DataFrame dapat dikonstruksi dari list, list yang digabungkan menggunakan fungsi `zip()`, dictionary, atau NumPy Array 2D.
- Pembuatan DataFrame acak sering menggunakan generator data dari NumPy. Untuk memastikan hasil pengacakan data tetap konsisten ketika program dijalankan ulang, digunakan pengunci kode berupa nilai Seed (`np.random.seed()`).

#### [Wawasan Diskusi / Audio Insight]

- Dosen menunjukkan contoh implementasi kode pembuatan DataFrame acak berukuran 5 baris dan 4 kolom menggunakan data distribusi normal standar.
- Indeks baris didefinisikan secara eksplisit menggunakan karakter alfabet 'A', 'B', 'C', 'D', 'E' yang dipisahkan menggunakan metode `.split()`, begitu pula dengan indeks kolom 'W', 'X', 'Y', 'Z'.

```
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
```

---

## 3.3 Indexing dan Slicing pada DataFrame

### A. Pengaksesan Kolom

- Memilih satu kolom akan menghasilkan objek Series, dilakukan dengan memanggil nama kolom di dalam kurung siku `df['NamaKolom']`. Pengaksesan menggunakan atribut `df.NamaKolom` juga dimungkinkan, tetapi sangat tidak direkomendasikan karena rawan konflik dengan metode bawaan.
- Memilih beberapa kolom sekaligus dilakukan dengan melewatkan sebuah list di dalam kurung siku ganda `df[['Kolom1', 'Kolom2']]`, yang akan menghasilkan objek DataFrame baru.

### B. Pengaksesan Menggunakan .loc[] dan .iloc[]

- **Atribut .loc[]**: Digunakan untuk mengakses baris dan kolom berdasarkan label nama. Slicing baris menggunakan `.loc['A':'C']` bersifat inklusif terhadap batas akhir (artinya baris 'C' akan ikut ditampilkan).
- **Atribut .iloc[]**: Digunakan untuk mengakses data berdasarkan lokasi indeks angka (integer-based location) yang dimulai dari 0. Slicing baris menggunakan `.iloc[0:2]` bersifat eksklusif terhadap batas akhir (artinya baris pada indeks ke-2 tidak akan ditampilkan).

### C. Conditional Filtering

- Digunakan untuk menyaring data berdasarkan kondisi boolean tertentu. Operasi perbandingan seperti `df > 0` akan menguji setiap elemen di dalam DataFrame dan menghasilkan boolean mask (tabel berisi nilai True dan False).
- Menyaring baris secara spesifik dilakukan dengan memasukkan kondisi di dalam kurung siku DataFrame utama, misalnya `df[df['W'] > 0]`. Jika ingin mengambil nilai kolom tertentu saja dari hasil filter tersebut, dapat ditambahkan nama kolom di akhir baris kode.

#### [Wawasan Diskusi / Audio Insight]

- Dosen memperingatkan agar mahasiswa memahami perbedaan perilaku slicing antara `.loc` dan `.iloc`. Pada `.loc['A':'C']`, baris C ditampilkan karena pencarian berbasis nama label. Sedangkan pada `.iloc[0:2]`, baris pada indeks ke-2 ditiadakan karena mengandalkan perilaku eksklusif indeks integer Python standar.
- Dosen memberikan contoh sintaks pengaksesan elemen tunggal maupun kelompok menggunakan kedua atribut tersebut.

```
# Pengaksesan baris tunggal berdasarkan label
df.loc['A']

# Pengaksesan baris 'A' dan kolom 'Y'
df.loc['A', 'Y']

# Slicing baris 'A' sampai 'C' secara inklusif
df.loc['A':'C']

# Pengaksesan baris A dan B untuk kolom W dan Y
df.loc[['A', 'B'], ['W', 'Y']]

# Pengaksesan baris berdasarkan indeks angka (baris ketiga/indeks 2)
df.iloc[2]

# Slicing baris dari indeks 0 hingga sebelum indeks 4 dengan langkah 2
df.iloc[0:4:2]

# Pengaksesan elemen tunggal pada baris indeks 1 dan kolom indeks 3
df.iloc[1, 3]

# Pengaksesan baris indeks 1 dan 3 sekaligus
df.iloc[[1, 3]]

# Filtering seluruh elemen DataFrame yang bernilai positif
df[df > 0]

# Menyaring baris yang memiliki nilai kolom 'W' positif
df[df['W'] > 0]

# Mengambil nilai kolom 'Y' dari baris yang nilai kolom 'W'-nya positif
df[df['W'] > 0]['Y']
```

---

## 3.4 Manipulasi DataFrame

### A. Menambahkan Baris dan Kolom

- Kolom baru dapat ditambahkan dengan langsung menetapkan nilainya (baik nilai konstan maupun hasil kalkulasi matematis kolom lain) ke dalam nama kolom baru.
- Penambahan kolom pada posisi spesifik di tengah tabel dapat memanfaatkan metode `.insert()` dengan menyertakan indeks lokasi tujuan.
- Baris baru dapat dimasukkan dengan menetapkan baris baru tersebut menggunakan atribut `.loc[]`.

### B. Menghapus Baris dan Kolom (.drop)

- Metode `.drop()` digunakan untuk menghapus baris atau kolom dari DataFrame.
- Parameter `axis` sangat krusial dalam metode ini: menetapkan `axis=1` untuk menghapus kolom, dan `axis=0` untuk menghapus baris.

### C. Reset Index, Set Index, dan Inplace Parameter

- **reset_index()**: Mengatur ulang indeks DataFrame kembali ke indeks numerik default (0, 1... n) dan memindahkan indeks lama menjadi kolom baru berlabel 'index'.
- **set_index()**: Menetapkan salah satu kolom DataFrame untuk digunakan sebagai indeks baris yang baru, menggantikan indeks yang lama.
- **inplace=True**: Secara default, metode modifikasi seperti `.drop()`, `.reset_index()`, dan `.set_index()` tidak mengubah DataFrame asli melainkan mengembalikan salinan baru (not inplace). Untuk memperbarui data asli secara permanen tanpa perlu menetapkannya kembali ke variabel baru, parameter `inplace=True` wajib disertakan.

### D. Multi-Index (Hierarchical Indexing)

- Multi-Index memungkinkan pembuatan indeks bertingkat (hierarki) pada DataFrame.
- Indeks ini dapat dikonstruksi dari kumpulan tuple menggunakan fungsi `pd.MultiIndex.from_tuples()`. Pengaksesan data bertingkat ini dilakukan menggunakan metode `.loc[]` atau metode `.xs()` (cross-section) yang sangat efisien untuk menembus level indeks tertentu.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menjelaskan kegunaan parameter `inplace=True` sebagai langkah pengamanan (safeguard) agar pengguna tidak kehilangan data aslinya akibat eksekusi perintah pembersihan data yang salah secara tidak sengaja.
- Dosen mengilustrasikan bahwa Multi-Index sangat berguna ketika kita memiliki data yang terbagi ke dalam kelompok besar (seperti wilayah atau kota) dan sub-kelompok di dalamnya (seperti kode cabang atau nomor urut).

```
# Menambahkan kolom baru hasil penjumlahan kolom W dan Y
df['new'] = df['W'] + df['Y']

# Menambahkan kolom baru bernama 'new' di indeks kolom ke-2
df.insert(2, 'new', [1, 2, 3, 4, 5])

# Menambahkan baris baru dengan label 'new'
df.loc['new'] = [1, 2, 3, 4]

# Menghapus kolom 'new' secara sementara (tidak permanen)
df.drop('new', axis=1)

# Menghapus baris 'E' secara permanen dari DataFrame asli
df.drop('E', axis=0, inplace=True)

# Mengembalikan indeks ke angka default
df.reset_index()

# Menetapkan kolom bernama 'States' menjadi indeks baru secara permanen
df.set_index('States', inplace=True)
```

---

## 3.5 Pengurutan dan Analisis Statistik Deskriptif

### A. Pengurutan Data (Sorting)

- **sort_values()**: Digunakan untuk mengurutkan DataFrame berdasarkan nilai pada satu atau beberapa kolom tertentu. Defaultnya diurutkan secara menaik (ascending), namun dapat diatur menjadi menurun menggunakan parameter `ascending=False`.
- **sort_index()**: Digunakan untuk mengurutkan baris DataFrame berdasarkan indeksnya.

### B. Fungsi, Method, dan Atribut Statistik

- Pandas menyediakan serangkaian alat instan untuk meninjau struktur data, tipe data, serta statistik dasar DataFrame:
    - Atribut `.shape`: Mengembalikan jumlah baris dan kolom dalam tuple.
    - Atribut `.columns`: Menampilkan daftar nama kolom.
    - Atribut `.dtypes`: Mengetahui tipe data masing-masing kolom.
    - Method `.head()` dan `.tail()`: Menampilkan baris teratas dan terbawah tabel (secara default menampilkan 5 baris).
    - Method `.info()`: Menghasilkan informasi lengkap struktur DataFrame meliputi tipe data, jumlah nilai non-null, dan penggunaan memori.
    - Method `.describe()`: Menghitung statistik deskriptif otomatis (mean, std, min, max, kuartil) untuk seluruh kolom bertipe numerik.
    - Method statistik spesifik: `.mean()`, `.median()`, `.std()`, `.min()`, dan `.max()`.
    - Method keunikan: `.unique()` untuk melihat nilai unik, `.nunique()` untuk menghitung jumlah nilai unik, dan `.value_counts()` untuk menghitung frekuensi kemunculan nilai pada suatu kolom.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menyarankan agar pemula selalu membiasakan diri memanggil `.head()` atau `.info()` setelah mengimpor data eksternal. Langkah peninjauan awal ini krusial untuk mendeteksi apakah data telah dimuat dengan benar serta melihat tipe data awal setiap kolom.

```
# Meninjau statistik deskriptif otomatis
df.describe()

# Menampilkan informasi struktural DataFrame
df.info()

# Mengurutkan DataFrame berdasarkan nilai kolom 'col1' secara menurun
df.sort_values(by='col1', ascending=False)

# Menghitung frekuensi kemunculan nilai unik pada kolom 'col2'
df['col2'].value_counts()
```

---

## 3.6 Penanganan Missing Values dan Pengelompokan Data

### A. Penanganan Missing Values (Data Kosong)

- Data kosong atau bernilai null direpresentasikan sebagai NaN (Not a Number) dalam Pandas.
- **Deteksi**: Menggunakan metode `.isna()` untuk menghasilkan tabel boolean, atau dipadukan dengan `.isna().sum()` untuk langsung menghitung jumlah baris kosong di setiap kolom.
- **Pembersihan (Hapus)**: Menggunakan metode `.dropna()` untuk membuang seluruh baris atau kolom yang memiliki nilai kosong.
- **Imputasi (Isi)**: Menggunakan metode `.fillna()` untuk mengganti data kosong dengan nilai tertentu, misalnya string statis atau nilai dinamis berupa rata-rata kolom tersebut (`df['Age'].mean()`).

### B. Pengelompokan Data (Grouping)

- Pengelompokan data didasarkan pada nilai kategori pada kolom tertentu menggunakan metode `.groupby()`.
- Setelah dikelompokkan, kita wajib menggunakan fungsi agregat (seperti `.mean()`, `.sum()`, atau `.count()`) untuk menghasilkan nilai ringkasan statistik dari masing-masing kelompok tersebut.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menerangkan bahwa dalam proyek nyata, membuang data kosong menggunakan `.dropna()` sering kali bukan solusi terbaik karena dapat melenyapkan informasi berharga lainnya pada baris tersebut. Oleh karena itu, teknik pengisian data kosong (`.fillna()`) dengan nilai rata-rata (_mean imputation_) sangat direkomendasikan untuk menjaga integritas data.
- Dosen mengilustrasikan operasi `.groupby('Company')` yang dipadukan dengan fungsi `.mean()`. Pandas secara cerdas hanya akan menghitung nilai rata-rata untuk kolom yang bertipe numerik (seperti kolom Sales), dan mengabaikan kolom bertipe string/kategori.

```
# Menghitung jumlah data kosong per kolom
df.isna().sum()

# Mengisi data kosong pada kolom 'Age' dengan nilai rata-rata usia
df['Age'].fillna(value=df['Age'].mean(), inplace=True)

# Mengelompokkan data berdasarkan kolom 'Company' dan menghitung rata-rata nilai numerik
df.groupby('Company').mean()
```

---

## 3.7 Penggabungan DataFrame dan Operasi Lanjutan

### A. Merging, Joining, dan Concatenating

- **pd.merge()**: Menggabungkan dua DataFrame berdasarkan kesamaan kolom kunci (key) tertentu. Konsep penggabungannya analog dengan SQL Join, yang mendukung tipe gabungan _inner_, _left_, _right_, dan _outer_.
- **.join()**: Menggabungkan dua DataFrame berdasarkan indeks barisnya, bukan berdasarkan kolom kunci.
- **pd.concat()**: Menyatukan atau menumpuk beberapa DataFrame. Penggabungan dapat dilakukan secara vertikal ke bawah (default: `axis=0`) atau secara horizontal berdampingan (`axis=1`).

### B. Operasi Aritmatika Antar Kolom, .apply(), dan Pivot Table

- **Operasi Aritmatika**: Operasi aritmatika dasar (penjumlahan, pengurangan, perkalian, pembagian) dapat langsung dilakukan antar kolom DataFrame secara element-wise.
- **Metode .apply()**: Digunakan untuk menerapkan fungsi buatan sendiri (custom function) atau fungsi bawaan Python ke seluruh elemen kolom DataFrame.
- **Fungsi Lambda**: Digunakan untuk menulis fungsi anonim sekali pakai secara ringkas di dalam metode `.apply()`.
- **Pivot Table**: Metode `.pivot_table()` digunakan untuk mereorganisasi, merangkum, dan mentransformasikan struktur data tabular agar lebih mudah dianalisis berdasarkan variabel kunci tertentu.

#### [Wawasan Diskusi / Audio Insight]

- Dosen memperlihatkan perbedaan konkret antara penggabungan vertikal dan horizontal menggunakan `pd.concat()`. Jika menggunakan `axis=1`, pastikan baris data memiliki indeks yang sejajar agar tidak menghasilkan banyak nilai NaN pada baris yang tidak cocok.
- Dosen memberikan contoh fungsionalitas `.apply()` dengan fungsi Lambda untuk manipulasi string atau operasi matematika cepat, yang jauh lebih efisien dibandingkan menulis iterasi loop manual menggunakan `for` di Python.

```
# Penggabungan horizontal beberapa DataFrame berdasarkan keselarasan indeks
pd.concat([df1, df2, df3], axis=1)

# Penggabungan dua DataFrame berdasarkan kolom kunci 'key'
pd.merge(left_df, right_df, on='key', how='inner')

# Operasi pembagian antar kolom
df['col6'] = df['col2'] / df['col1']

# Menerapkan fungsi buatan sendiri menggunakan .apply()
def times2(x):
    return x * 2

df['col1'].apply(times2)

# Menerapkan fungsi kuadrat instan menggunakan fungsi anonim Lambda
df['col1'].apply(lambda x: x ** 2)

# Membuat Pivot Table dari DataFrame
df.pivot_table(values='D', index=['A', 'B'], columns=['C'])
```

---

## 3.8 Membaca dan Menyimpan Data (File I/O)

### A. Metode Import Berkas

- Pandas mendukung fungsionalitas tinggi untuk membaca berkas dari berbagai format populer di industri:
    - CSV: `pd.read_csv()`
    - Excel: `pd.read_excel()`
    - JSON: `pd.read_json()`
    - HTML: `pd.read_html()`

### B. Metode Export Berkas

- DataFrame yang telah selesai diproses dapat langsung disimpan kembali ke dalam format file fisik:
    - CSV: `df.to_csv()`
    - Excel: `df.to_excel()`
    - JSON: `df.to_json()`

#### [Wawasan Diskusi / Audio Insight]

- Dosen memaparkan batasan fungsionalitas File I/O pada Pandas. Meskipun Pandas sangat andal dalam mengimpor data dari dokumen web menggunakan `pd.read_html()`, Pandas tidak memiliki fungsi bawaan untuk mengekspor atau menyimpan DataFrame langsung menjadi file fisik berformat `.html`.
- Saat mengekspor data ke format CSV atau Excel, dosen sangat menganjurkan untuk menambahkan parameter `index=False` agar indeks numerik Pandas tidak ikut tersimpan sebagai kolom baru yang tidak perlu di dalam file eksternal tersebut.

```
# Membaca file CSV
df = pd.read_csv('dataset.csv')

# Menyimpan DataFrame ke file Excel tanpa menyertakan kolom indeks numerik
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
```

---

## 3.9 Tabel Istilah Teknis dan Karakteristik

Berikut adalah tabel rangkuman fungsi, metode, dan atribut manipulasi data Pandas yang dipelajari pada materi ini:

|Istilah Teknis / Metode|Karakteristik dan Deskripsi Utama|
|:--|:--|
|_Series_|Struktur data satu dimensi (1D) dengan indeks berlabel yang dapat menyimpan tipe data objek apa pun.|
|_DataFrame_|Struktur data dua dimensi (2D) berbentuk tabel berukuran fleksibel yang terdiri dari kumpulan Series.|
|_.loc[]_|Metode pengaksesan baris/kolom berdasarkan label nama, dengan sifat slicing batas akhir yang inklusif.|
|_.iloc[]_|Metode pengaksesan baris/kolom berdasarkan indeks numerik (integer), bersifat eksklusif batas akhir.|
|_.drop()_|Menghapus kolom (axis=1) atau baris (axis=0). Membutuhkan parameter inplace=True untuk memperbarui data asli.|
|_inplace=True_|Parameter yang digunakan untuk langsung meng-override dan menyimpan perubahan pada objek DataFrame asli.|
|_Multi-Index_|Struktur indeks baris/kolom bertingkat (hierarki) untuk menangani analisis data multidimensi yang kompleks.|
|_.groupby()_|Mengelompokkan baris data berdasarkan kategori kolom tertentu dan wajib diikuti oleh fungsi agregasi.|
|_pd.merge()_|Menggabungkan dua DataFrame berdasarkan kolom kunci yang sama dengan tipe join seperti SQL.|
|_pd.concat()_|Menyatukan atau menumpuk beberapa DataFrame secara vertikal (axis=0) atau horizontal (axis=1).|
|_.apply()_|Menerapkan fungsi khusus atau fungsi Lambda ke setiap elemen di dalam kolom DataFrame secara serentak.|
|_.pivot_table()_|Mereorganisasi dan meringkas data tabular berdasarkan parameter indeks, kolom, dan nilai tertentu.|

---

## 3.10 Tugas Latihan Praktek DataFrame (Titanic Dataset Exercises)

Seluruh latihan praktek di bawah ini menggunakan Titanic dataset yang bersumber dari Kaggle.

### Latihan 1: Penyaringan Penumpang Wanita yang Selamat

- **Tugas**: Melakukan filtering data penumpang untuk menampilkan penumpang wanita saja yang selamat dari bencana.
- **Sintaks Solusi**:

```
df[(df['Sex'] == 'female') & (df['Survived'] == 1)]
```

### Latihan 2: Pengelompokan Usia (AgeGroup) dan Rata-rata Tarif Tiket

- **Tugas**: Menambahkan kolom baru bernama `AgeGroup` dengan aturan: jika usia di bawah 18 tahun diisi dengan "Child", jika tidak diisi dengan "Adult". Kemudian hitung rata-rata tarif tiket (`Fare`) yang dibayarkan oleh masing-masing kelompok tersebut menggunakan `.groupby()`.
- **Sintaks Solusi**:

```
df['AgeGroup'] = df['Age'].apply(lambda age: 'Child' if age < 18 else 'Adult')
df.groupby('AgeGroup')['Fare'].mean()
```

### Latihan 3: Analisis Kelas Kabin (Pclass)

- **Tugas**: Mengelompokkan data berdasarkan kelas kabin (`Pclass`), kemudian hitung total jumlah penumpang dan rata-rata tarif tiket (`Fare`) untuk setiap kelasnya.
- **Sintaks Solusi**:

```
df.groupby('Pclass')['Fare'].agg(['count', 'mean'])
```

### Latihan 4: Tingkat Keselamatan Berdasarkan Kombinasi Kelas dan Gender

- **Tugas**: Melakukan pengelompokan data dengan dua kolom sekaligus (`Pclass` dan `Sex`) untuk menghitung rata-rata tingkat keselamatan penumpang (`Survived`), kemudian urutkan hasilnya dari tingkat keselamatan tertinggi ke terendah.
- **Sintaks Solusi**:

```
df.groupby(['Pclass', 'Sex'])['Survived'].mean().sort_values(ascendi
```



---


# Module 1 Session 13 Data Visualization


## Bab 1  Konsep Dasar Visualisasi Data



## 1.1 Pengertian dan Signifikansi Visualisasi Data

### A. Definisi Visualisasi Data

- **Data Visualization** adalah penyetelan atau penyajian data dalam format gambar atau grafis (_pictorial or graphical format_).
- Bidang ini merupakan suatu disiplin ilmu untuk memahami data dengan menyajikannya secara visual agar pola (_patterns_), tren (_trends_), komposisi (_composition_), perbandingan (_comparison_), dan hubungan (_relationship_) dapat terungkap (_exposed_).

#### [Wawasan Diskusi / Audio Insight]

- Menyampaikan wawasan (_insight_) sering kali sulit jika analis hanya memiliki data mentah (_raw data_).
- Menyajikan data dalam format visual yang mudah dimengerti sangat penting karena otak manusia (_human brain_) memproses informasi visual jauh lebih cepat dan mudah dibandingkan dengan lembar kerja (_spreadsheet_) atau laporan teks biasa.
- Dalam praktik di industri, sering terjadi redundansi di mana pengambil keputusan (_manager_ atau _VP_) tetap meminta data mentah (_raw data_) ditarik secara manual meskipun analis telah menyusun dasbor (_dashboard_) visual yang sangat informatif. Menyajikan tabel mentah tanpa visualisasi adalah praktik yang buruk karena menghambat komunikasi wawasan.

### B. Signifikansi Visualisasi Data dibanding Statistik dan Tabel Mentah

- Visualisasi data mempercepat identifikasi peristiwa tidak biasa (_uncommon event_) atau anomali (_anomaly_).
- Analisis statistik deskriptif mampu merangkum data (_summarize data_), namun sering kali menyembunyikan pola (_hide patterns_) yang krusial. Pola-pola ini tidak akan muncul jika analis hanya mengandalkan ringkasan nilai statistik.

#### [Wawasan Diskusi / Audio Insight]

- Sebagai contoh kasus, saat mendeteksi anomali pada hubungan antara tahun (_year_) dan penjualan (_sales_), menggunakan grafik visual membuat anomali tersebut langsung teridentifikasi. Sebaliknya, jika menggunakan tabel mentah (meskipun hanya terdiri dari 26 baris), proses pencarian anomali akan jauh lebih sulit dan memakan waktu.
- Tantangan analisis tabel mentah ini akan menjadi mustahil ditangani secara manual apabila ukuran data sangat besar, misalnya mencapai 1 juta baris data yang tidak muat dalam satu halaman layar.
- Contoh kasus keterbatasan statistik: Sekumpulan data yang memiliki ringkasan statistik yang mirip (seperti nilai rata-rata/_mean_ sumbu X dan Y, standar deviasi/_standard deviation_, serta korelasi/_correlation_ sebesar -0,06) dapat memiliki bentuk sebaran visual yang sangat berbeda dan unik ketika diplot. Wawasan riil tersebut hanya bisa diperoleh melalui visualisasi data.

---

## 1.2 Metodologi dan Alur Proses Visualisasi Data

### A. Tahapan Eksekusi Visualisasi Data

Modul menetapkan alur sistematis dalam melakukan visualisasi data sebagai berikut:

1. **Memahami Konteks Data (_Understand the Context of Your Data_)**: Memahami asal-usul, tipe, dan domain dari data yang dianalisis sebelum mulai membuat visualisasi.
2. **Merumuskan Pertanyaan Data (_Making Some Questions For Your Data_)**: Menentukan hipotesis atau pertanyaan bisnis yang ingin dipecahkan (seperti mencari produk terlaris atau faktor yang memengaruhi pelanggan).
3. **Memilih Jenis Visualisasi yang Tepat (_Choose Appropriate Type of Visualization_)**: Menentukan jenis grafik yang paling sesuai dengan tipe variabel data yang akan diplot.
4. **Mengidentifikasi Pesan Utama (_Identify the Message of Each Visualization You Made_)**: Memastikan setiap grafik yang dibuat menyampaikan pesan spesifik yang jelas bagi audiens.
5. **Konfigurasi Teknis (_Technical Perspective_)**: Melengkapi grafik dengan judul (_title_), label sumbu (_axis labels_), legenda (_legend_), penanda poin penting (_mark interesting data points_), serta mengoptimalkan penggunaan warna dan ukuran (_color and size_).
6. **Menarik Kesimpulan (_Get Conclusion_)**: Merumuskan kesimpulan akhir dan merekomendasikan keputusan (_decision_) tindakan bisnis berdasarkan visualisasi tersebut.

#### [Wawasan Diskusi / Audio Insight]

- Melakukan eksplorasi data (_explore data_) menggunakan visualisasi sangat krusial di awal proyek sains data untuk membantu analis memahami karakteristik data sebelum melatih model pembelajaran mesin (_machine learning_). Eksplorasi data ini meningkatkan peluang ditemukannya wawasan berharga.
- Memilih jenis grafik yang salah akan mengaburkan perbandingan informasi. Sebagai contoh kasus: data Produk Domestik Bruto (_Gross Domestic Product - GDP_) tidak cocok divisualisasikan dengan grafik garis (_line chart_). Grafik garis secara teknis menyiratkan kontinuitas dan perkembangan variabel dari waktu ke waktu (_over time_), sehingga memerlukan adanya dimensi waktu (_time series data_).
- Visualisasi data tidak boleh berhenti pada penyajian gambar saja; analis wajib menyertakan kesimpulan (_conclusion_) dan rekomendasi keputusan (_decision_) nyata untuk pengambil kebijakan.

---

## 1.3 Prinsip Utama Visualisasi Data yang Efektif

Kualitas efektivitas dari sebuah visualisasi data diukur berdasarkan empat prinsip utama berikut:

|Prinsip Utama|Deskripsi Teknis|
|:--|:--|
|**Clarity**|Kejelasan informasi yang menjamin grafik mudah dipahami dan tidak membingungkan pembaca (_avoid confusion_).|
|**Accuracy**|Akurasi plot yang menjamin representasi visual sesuai dengan nilai data asli (_accurate representation_) dan tidak melenceng.|
|**Simplicity**|Kesederhanaan desain yang memprioritaskan opsi visual paling sederhana guna menghindari kompleksitas yang berlebihan (_avoid complexity_).|
|**Visual Hierarchy**|Hierarki visual yang mengatur elemen grafik secara terstruktur sehingga penyampaian informasi mengalir dengan runut (_storytelling_).|

#### [Wawasan Diskusi / Audio Insight]

- **Clarity (Kejelasan)**: Dosen merujuk pada literatur berjudul _"How to Lie with Data"_ (atau _"How to Lie with Statistics"_). Buku ini menguraikan bagaimana visualisasi data dapat dimanipulasi secara sengaja untuk menghasilkan grafik yang menyesatkan (_misleading_) bagi pembacanya.
- **Accuracy (Akurasi)**: Visualisasi yang tidak akurat (misalnya karena manipulasi skala sumbu) akan mendistorsi perbandingan data yang sebenarnya. Nilai visual yang tampak pada grafik harus benar-benar selaras dengan nilai data (_value data_) asli.
- **Simplicity (Kesederhanaan)**: Analis harus mendahulukan visualisasi yang paling sederhana. Hindari penambahan dekorasi kompleks atau elemen visual berlebih yang tidak relevan karena akan membingungkan audiens.
- **Visual Hierarchy (Hierarki Visual)**: Pengaturan visual yang baik membantu analis bercerita (_storytelling_) secara terstruktur. Struktur visual sebaiknya dibuat mengalir, misalnya: menyajikan tren makro di bagian atas, faktor-faktor pengaruh di bagian tengah, hingga rincian mikro di bagian bawah. Cara ini mencegah alur pembacaan yang melompat-lompat (seperti dari bawah langsung ke atas).

---

## 1.4 Elemen-Elemen pada Grafik Visualisasi

### A. Anatomi Grafik (_Anatomy of a Chart_)

Sebuah grafik visualisasi yang informatif secara teknis wajib memiliki komponen-komponen berikut:

- **Chart Title**: Judul utama yang mendeskripsikan secara eksplisit informasi yang dimuat dalam grafik.
- **Axis Labels**: Label penjelas sumbu koordinat, yang terdiri atas **Horizontal Axis Label (Sumbu X)** dan **Vertical Axis Label (Sumbu Y)** untuk menerangkan variabel apa yang sedang diukur.
- **Axis Values**: Skala nilai numerik atau kategori diskrit yang tertera pada sumbu koordinat, yaitu **Horizontal Axis Values** dan **Vertical Axis Values**.
- **Legend**: Legenda atau keterangan simbol untuk membedakan kategori, variabel, atau grup data yang digambarkan dengan warna atau penanda berbeda.
- **Data Labels**: Teks atau angka yang diletakkan langsung pada titik data untuk menunjukkan nilai kuantitatif aslinya secara presisi.
- **Chart Area**: Wilayah utama tempat data visual (seperti batang, garis, atau titik pencar) diplot.
- **Gridlines**: Garis kisi bantu di latar belakang area grafik untuk memudahkan mata pembaca menyelaraskan posisi titik data dengan nilai pada sumbu koordinat.

#### [Wawasan Diskusi / Audio Insight]

- Dalam implementasi praktis menggunakan bahasa pemrograman Python, elemen-elemen anatomi ini didefinisikan secara manual di dalam blok kode. Sebagai contoh, pustaka `Matplotlib` menyediakan fungsi-fungsi spesifik seperti `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.legend()`, dan `plt.grid()` untuk menampilkan komponen tersebut pada layar.

---

## 1.5 Kategori Utama Visualisasi Berdasarkan Tujuan

Tipe visualisasi data dikelompokkan ke dalam empat kategori utama sesuai dengan tujuan analisis yang ingin dicapai:

### A. Comparison (Perbandingan)

- Digunakan untuk membandingkan nilai kuantitatif antar item atau melacak perubahannya seiring waktu.
- **Comparison Among Items (Perbandingan Antar Item)**:
    - Satu variabel per item (_One variables per items_):
        - Kategori sedikit (_Few items_): Menggunakan **Bar Chart** atau **Bar Plot**.
        - Kategori banyak (_Many items_): Menggunakan **Table with embedded chart**.
    - Dua variabel per item (_Two variables per items_): Menggunakan **Variable with column chart** (grafik kolom berkelompok).
- **Comparison Over Time (Perbandingan Seiring Waktu)**:
    - Satu variabel (_One variable_):
        - Periode banyak (_Many Periods_): Menggunakan **Line Chart**.
        - Periode sedikit (_Few Periods_): Menggunakan **Bar Chart** atau **Bar Plot**.
    - Banyak variabel / Kategori berbeda pada variabel sama (_Many variables / Same variables different categories_): Menggunakan **Multiple Line Chart**.

#### [Wawasan Diskusi / Audio Insight]

- Contoh kasus perbandingan kategori: Jika ingin membandingkan satu variabel diskrit seperti nilai penjualan pada kategori _office supplies_, _furniture_, dan _technology_, pilihan terbaik adalah menggunakan _Bar Chart_.
- Jika terdapat dua variabel (misalnya kategori produk sekaligus pembagian segmen konsumen seperti _consumer_, _corporate_, dan _home office_), visualisasi yang tepat adalah _Variable with column chart_ yang membedakan segmen menggunakan variasi warna batang di dalam kelompok kategori tersebut.
- Contoh kasus perbandingan tren waktu: Apabila data memiliki periode waktu yang sangat panjang atau tingkat kedetailan (_granularity_) yang tinggi (seperti harian atau mingguan dari tahun 2019 sampai 2020), penggunaan grafik garis (_line chart_) jauh lebih mudah dibaca dibandingkan grafik batang (_bar chart_).

### B. Composition (Komposisi)

- Digunakan untuk menunjukkan bagian-bagian atau kontribusi komponen yang membentuk satu kesatuan utuh.
- **Composition Static (Komposisi Statis)**:
    - Menunjukkan bagian dari total (_Share of total_): Menggunakan **Pie Chart**.
    - Akumulasi atau pengurangan nilai dari total (_Accumulation or subtraction of total_): Menggunakan **Waterfall Chart**.
    - Proporsi bagian per item atau kategori (_Share of total per items or category_): Menggunakan **Stacked Bar Chart**.
    - Struktur proporsi dengan kategori yang sangat banyak (_Share of total many items or category_): Menggunakan **Tree Map**.
- **Composition Over Time (Komposisi Seiring Waktu)**:
    - Periode sedikit (_Few Periods_): Menggunakan **Stacked Bar Chart**.
    - Periode banyak (_Many Periods_): Menggunakan **Stacked Area Chart**.

#### [Wawasan Diskusi / Audio Insight]

- Contoh kasus _Tree Map_: Efektif untuk menggambarkan data yang memiliki struktur hierarkis. Misalnya, visualisasi pendapatan produk yang dikelompokkan ke dalam kategori besar (seperti _beverages_, _baked goods_, _snacks_, dan _merchandise_) di mana masing-masing kategori tersebut dipecah lagi ke dalam sub-kategori (seperti kategori _beverages_ yang dipecah menjadi _coffee_ 43%, _tea_ 23%, dan _specialty drinks_ 34%). Ukuran kotak menggambarkan kontribusi nilai aslinya.
- Contoh kasus komposisi seiring waktu: Gunakan _Stacked Bar Chart_ biasa untuk menunjukkan perkembangan nilai absolut komponen seiring waktu. Gunakan _100% Stacked Bar Chart_ apabila fokus analisis adalah membandingkan persentase kontribusi komponen dari waktu ke waktu. Untuk rentang waktu yang sangat panjang dengan banyak titik periode, gunakan _Stacked Area Chart_ (grafik area bertumpuk).

### C. Relationship (Hubungan)

- Digunakan untuk menemukan korelasi, interaksi, atau keterkaitan antara variabel numerik kontinu.
- **Dua variabel (_Two variables_)**: Menggunakan **Scatter Plot**.
- **Tiga variabel (_Three variables_)**: Menggunakan **Bubble Plot**.

#### [Wawasan Diskusi / Audio Insight]

- Contoh kasus hubungan dua variabel: Digunakan untuk memetakan hubungan antara total tagihan (_total bill_) dan besaran uang tip (_tip_) yang diberikan oleh pelanggan restoran. Sumbu X merepresentasikan _total bill_ dan sumbu Y merepresentasikan _tip_. Scatter plot akan memplot titik-titik koordinat untuk melihat tren positif (apakah semakin besar nilai tagihan berkolerasi dengan semakin besarnya tip yang diberikan).

### D. Distribution (Distribusi)

- Digunakan untuk melihat sebaran data, kerapatan data, atau frekuensi kemunculan nilai numerik.
- **Satu variabel (_One variable_)**: Menggunakan **Histogram** atau **Box Plot**.
- **Dua variabel (_Two variables_)**: Menggunakan **Scatter Plot**.

#### [Wawasan Diskusi / Audio Insight]

- Contoh kasus distribusi satu variabel: Menggunakan _Histogram_ untuk membagi variabel numerik tunggal ke dalam interval-interval tertentu (_bins_) guna menghitung berapa banyak frekuensi observasi data yang jatuh ke dalam setiap interval tersebut.
- Aspek visual _Histogram_ dan _Box Plot_ dapat digabungkan ke dalam satu visualisasi kombo (_combo visualization_) untuk memberikan analisis statistik yang lebih lengkap.
- Pilihan lainnya adalah menggunakan _Violin Plot_ yang secara teknis menggabungkan visualisasi _Box Plot_ (untuk ringkasan nilai kuartil dan median) dengan _Kernel Density Plot_ (untuk visualisasi kepadatan frekuensi distribusi data).



## Bab 2  Perkakas (Tools) untuk Visualisasi Data


## 2.1 Pustaka (Library) Visualisasi Data di Python

### A. Karakteristik Library Python

Berikut adalah daftar pustaka (_library_) Python yang digunakan untuk analisis dan visualisasi data beserta karakteristik utamanya:

| Library        | Basis / Ketergantungan | Fungsi & Karakteristik Utama                                                                                                                                                                        |
| :------------- | :--------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Matplotlib** | Mandiri                | Library komprehensif untuk membuat visualisasi statis, animasi, dan interaktif di Python. Berfungsi sebagai pondasi dasar bagi library visualisasi lainnya.                                         |
| **Seaborn**    | Matplotlib             | Library visualisasi data berbasis Matplotlib yang menyediakan high-level interface untuk menggambar grafik statistik yang menarik (_attractive_) dan informatif.                                    |
| **Pandas**     | Python murni (Numpy)   | Tool analisis dan manipulasi data open-source yang cepat, bertenaga, fleksibel, serta mudah digunakan. Memiliki fungsi plotting dasar bawaan untuk visualisasi cepat langsung dari objek DataFrame. |
| **Plotly**     | Mandiri                | Library khusus untuk membuat visualisasi data yang bersifat interaktif.                                                                                                                             |

#### [Wawasan Diskusi / Audio Insight]

- **Matplotlib**: Meskipun sangat bertenaga dan fleksibel untuk membuat kanvas visualisasi, Matplotlib membutuhkan penulisan baris kode yang relatif lebih panjang dan detail untuk mengonfigurasi komponen visualisasi dibanding Seaborn.
- **Seaborn**: Seaborn dikembangkan langsung di atas Matplotlib (analogi seperti Pandas yang dikembangkan di atas Numpy). Antarmuka Seaborn jauh lebih atraktif dan informatif secara visual karena memiliki opsi tema bawaan. Penggunaannya sangat disukai oleh para analis karena sintaks kodenya jauh lebih singkat dan tidak membutuhkan banyak variabel tambahan yang rumit.
- **Pandas**: Pustaka ini utamanya digunakan untuk analisis dan manipulasi data (_data analysis and manipulation_), namun dilengkapi dengan metode plotting cepat (seperti `.hist()` atau `.boxplot()`) untuk keperluan eksplorasi data instan tanpa harus memanggil library visualisasi eksternal terlebih dahulu.

---

## 2.2 Lingkungan Kerja Interaktif (Interactive Python Notebook)

### A. Penggunaan File IPYNB

- Proyek visualisasi data dalam modul ini tidak menggunakan file Python biasa (`.py`), melainkan menggunakan format **IPYNB** (_Interactive Python Notebook_).
- File IPYNB berjalan menggunakan ekstensi **Jupyter** yang harus diaktifkan terlebih dahulu di editor kode (seperti VS Code).
- Keunggulan utama IPYNB adalah kemampuannya untuk mengeksekusi blok kode (_code cell_) secara terpisah dan langsung menampilkan hasil keluaran (_code output_) di bawah sel tersebut, sehingga sangat cocok untuk proses eksplorasi data (_explore data_).

#### [Wawasan Diskusi / Audio Insight]

- **Pengaturan Kernel**: Untuk menjalankan file IPYNB, pengguna harus menentukan **Kernel** yang tepat di bagian kanan atas editor. Kernel ini menentukan lingkungan Python (_Python Environment_) yang akan digunakan. Dalam sesi kuliah ini, mahasiswa diarahkan untuk memilih virtual environment khusus yang telah dibuat sebelumnya (bernama "Purwadika").
- **Instalasi Library**: Jika library seperti Matplotlib atau Seaborn belum terinstal di dalam environment aktif, instalasi dapat dilakukan langsung melalui terminal dengan mengaktifkan virtual environment "Purwadika" terlebih dahulu, kemudian menjalankan perintah berikut:

```
pip install seaborn matplotlib
```

- **Aturan Eksekusi Sel**: Pengguna tidak boleh mengeksekusi blok kode secara acak (_out of order_). Misalnya, mencoba mengeksekusi sel di bagian bawah yang memanggil variabel tertentu (seperti variabel `tips`) sebelum sel atas yang mendefinisikan variabel tersebut dijalankan akan memicu kegagalan runtime atau error variabel tidak ditemukan (_key error_ / _name error_). Sel harus dijalankan secara runut dari atas ke bawah.

---

## 2.3 Perangkat Lunak Business Intelligence (BI) dan Pembuatan Dashboard

### A. Perkakas BI Populer

Selain menggunakan pemrograman Python murni untuk keperluan visualisasi ilmiah dan eksplorasi data, industri juga memanfaatkan perangkat lunak Business Intelligence (BI) khusus untuk kebutuhan pelaporan bisnis interaktif dan pembuatan dasbor (_dashboard_):

|Kategori Perkakas|Contoh Perangkat Lunak|Fungsi Utama di Industri|
|:--|:--|:--|
|**Business Intelligence (BI)**|Power BI, Tableau, Microstrategy, Qlik|Digunakan untuk menyusun dasbor interaktif berskala perusahaan yang terhubung langsung ke sumber data bisnis untuk mendukung pengambilan keputusan.|

#### [Wawasan Diskusi / Audio Insight]

- Alat-alat BI seperti Power BI dan Tableau sangat populer di dunia bisnis karena memudahkan pembuatan laporan interaktif tanpa harus menulis baris kode pemrograman visualisasi yang rumit dari awal.
- Penggunaannya melengkapi visualisasi Python; Python biasanya digunakan oleh analis atau engineer di tahap eksplorasi awal (_exploratory data analysis_) dan persiapan model, sementara perkakas BI digunakan untuk menyajikan dasbor final yang interaktif ke pengambil keputusan tingkat tinggi (_manager_ atau _VP_).



## Bab 3 Tipe-Tipe Visualisasi Data & Implementasi Kode Python


Bab ini membahas secara mendalam berbagai jenis grafik visualisasi data yang umum digunakan di industri, karakteristik unik masing-masing grafik, panduan kapan menggunakannya atau menghindarinya, serta implementasi praktis sintaks kode pemrogramannya menggunakan bahasa Python melalui tiga library utama: **Matplotlib**, **Seaborn**, dan **Pandas**.

---

## 3.1 Histogram

### A. Definisi dan Kegunaan

- **Histogram** adalah grafik distribusi frekuensi yang digunakan untuk menampilkan sebaran data numerik tunggal secara kontinu.
- Grafik ini membagi nilai numerik ke dalam interval-interval tertentu yang disebut **bins** (atau tempat penyimpanan data).
- Tinggi dari setiap batang merepresentasikan frekuensi atau jumlah observasi data yang jatuh ke dalam interval bins tersebut.

### B. Perbedaan Utama Histogram vs Bar Chart

- Histogram digunakan khusus untuk merepresentasikan sebaran data numerik dari variabel kontinu, di mana setiap batang saling bersebelahan secara fisik tanpa jeda ruang guna menekankan kontinuitas data.
- _Bar Chart_ digunakan untuk membandingkan kelompok kategori diskrit (seperti data nominal atau ordinal), di mana terdapat jeda jarak antar batang untuk menunjukkan batas antar kategori yang terpisah.

### C. Implementasi Python

Berikut adalah fungsi penulisan kode untuk menghasilkan Histogram menggunakan tiga library berbeda:

```
# Menggunakan Matplotlib
import matplotlib.pyplot as plt
plt.hist(df['Age'], bins=10)
plt.show()

# Menggunakan Seaborn (histplot atau displot)
import seaborn as sns
sns.histplot(df['Age'], kde=True)
plt.show()

# Menggunakan Pandas
df['Age'].plot(kind='hist', bins=10)
plt.show()
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa parameter **kde** (Kernel Density Estimation) bernilai `True` pada library Seaborn sangat berguna untuk menggambarkan garis perkiraan mulus sebaran data (_density curve_) di atas batang histogram.
- Mengatur ukuran **bins** yang pas sangat penting. Jika bins terlalu sedikit, pola sebaran tidak terlihat; jika bins terlalu banyak, grafik akan tampak berantakan karena terlalu detail.

---

## 3.2 Box Plot

### A. Definisi dan Kegunaan

- **Box Plot** (atau _Box-and-Whisker Plot_) adalah visualisasi grafis untuk menyajikan ringkasan statistik deskriptif lima angka dari kumpulan data numerik.
- Lima angka statistik ringkasan tersebut adalah:
    1. **Minimum**: Batas nilai terkecil bukan pencilan (ditandai oleh ujung garis bawah/_whisker_).
    2. **First Quartile (Q1 / Kuartil Bawah)**: Batas bawah kotak yang menandakan persentil ke-25 dari data.
    3. **Median (Q2 / Kuartil Tengah)**: Garis horizontal di dalam kotak yang menandai nilai tengah atau persentil ke-50.
    4. **Third Quartile (Q3 / Kuartil Atas)**: Batas atas kotak yang menandakan persentil ke-75 dari data.
    5. **Maximum**: Batas nilai terbesar bukan pencilan (ditandai oleh ujung garis atas/_whisker_).
- Jarak antara Q1 dan Q3 disebut **Interquartile Range (IQR)**. Batas garis _whisker_ bawah dihitung dengan rumus `Q1 - 1.5 * IQR` dan batas atas dihitung dengan `Q3 + 1.5 * IQR`.
- Nilai data yang berada di luar batas garis _whisker_ didefinisikan secara matematis sebagai **outliers** (pencilan) dan digambarkan dalam bentuk titik atau berlian terpisah di luar grafik kotak.

### B. Membaca Skewness (Kemiringan Distribusi Data)

Analisis kemiringan distribusi (_skewness_) sebaran data dapat dibaca langsung dari Box Plot berdasarkan posisi garis median terhadap kotak IQR:

|Posisi Garis Median|Karakteristik Skewness|Interpretasi Distribusi Data|
|:--|:--|:--|
|**Garis median berada tepat di tengah-tengah kotak**|Distribusi Simetris (_Normal Distribution_)|Sebaran data merata dan seimbang di sekitar nilai tengah.|
|**Garis median lebih dekat ke bagian bawah kotak (Q1)**|Kemiringan Positif (_Right-Skewed_)|Ekor sebaran data memanjang ke arah kanan (nilai besar), mayoritas data terkonsentrasi di nilai rendah.|
|**Garis median lebih dekat ke bagian atas kotak (Q3)**|Kemiringan Negatif (_Left-Skewed_)|Ekor sebaran data memanjang ke arah kiri (nilai kecil), mayoritas data terkonsentrasi di nilai tinggi.|

### C. Implementasi Python

Sintaks penulisan Box Plot dapat dilakukan dengan library berikut:

```
# Menggunakan Matplotlib
import matplotlib.pyplot as plt
plt.boxplot(df['Fare'])
plt.show()

# Menggunakan Seaborn (bisa membandingkan data numerik terhadap variabel kategorik)
import seaborn as sns
sns.boxplot(data=df, x='Survived', y='Fare')
plt.show()

# Menggunakan Pandas
df.boxplot(column='Fare')
plt.show()
```

#### [Wawasan Diskusi / Audio Insight]

- Box Plot sangat efisien dalam mendeteksi keberadaan _outliers_ secara visual.
- Menggunakan Seaborn memberikan fleksibilitas tinggi karena analis dapat langsung membandingkan sebaran data numerik di sumbu Y (misalnya harga tiket/_Fare_) terhadap variabel kategori di sumbu X (misalnya status keselamatan penumpang/_Survived_).

---

## 3.3 Violin Plot

### A. Definisi dan Kegunaan

- **Violin Plot** adalah tipe visualisasi kombo yang secara teknis menggabungkan seluruh elemen statistik pada Box Plot dengan representasi kepadatan frekuensi sebaran data dari **Kernel Density Plot**.
- Bentuk lekukan luar mirip biola menggambarkan pola kerapatan data (_density estimate_); semakin lebar penampang lekukannya, semakin banyak data yang terkonsentrasi pada tingkat nilai tersebut.

### B. Cara Membaca Violin Plot

- Bagian tengah violin memuat struktur Box Plot mini: terdapat titik putih kecil sebagai penanda nilai median, kotak hitam tebal sebagai rentang IQR (Q1 hingga Q3), serta garis vertikal tipis sebagai _whisker_.
- Bentuk sisi kiri dan kanan violin yang simetris menunjukkan kepadatan distribusi variabel di setiap titik nilai kuantitatifnya.

#### [Wawasan Diskusi / Audio Insight]

- Dosen mengilustrasikan contoh kasus membaca Violin Plot pada variabel usia penumpang Titanic berdasarkan keselamatan. Penumpang yang bertahan hidup (_Survived_) memiliki bentuk violin yang melebar di area usia 40 tahun ke bawah (menandakan mayoritas median yang selamat berumur muda).
- Sebaliknya, kelompok penumpang yang meninggal memiliki konsentrasi visual yang lebih tinggi di rentang usia 40 tahun ke atas.

---

## 3.4 Line Plot

### A. Definisi dan Kegunaan

- **Line Plot** adalah grafik garis yang menampilkan runtunan informasi sebagai rangkaian titik data yang dihubungkan secara kontinu oleh segmen garis lurus.
- Grafik ini sangat ideal untuk melacak perkembangan, perubahan, atau tren data kontinu seiring waktu (sering disebut sebagai **time series data**).

### B. Alasan Menghindari Bar Plot untuk Tren Waktu

- Penggunaan grafik batang (_bar chart_) untuk melacak tren waktu yang sangat panjang tidak disarankan karena batang mengimplikasikan kategori diskrit yang terputus-putus.
- Grafik garis (_line plot_) lebih unggul karena secara visual menonjolkan aliran kontinuitas, laju naik-turunnya tren, serta memudahkan penarikan pola musiman dari waktu ke waktu.

### C. Implementasi Python

```
# Menggunakan Matplotlib
import matplotlib.pyplot as plt
plt.plot(df['Date'], df['Sales'])
plt.show()

# Menggunakan Seaborn (hue membedakan warna garis per kategori)
import seaborn as sns
sns.lineplot(data=df, x='Date', y='Sales', hue='Region')
plt.show()

# Menggunakan Pandas
df.plot(kind='line', x='Date', y='Sales')
plt.show()
```

#### [Wawasan Diskusi / Audio Insight]

- Bila rentang data waktu memiliki tingkat kerapatan (_granularity_) yang sangat tinggi, misalnya data harian dari tahun 2019 sampai 2020, grafik garis adalah satu-satunya opsi terbaik untuk menyajikan pergerakan fluktuasi tanpa membuat visualisasi menjadi berantakan.

---

## 3.5 Scatter Plot

### A. Definisi dan Kegunaan

- **Scatter Plot** (atau diagram pencar) adalah grafik yang memplot titik-titik data individual pada koordinat kartesian dua dimensi (Sumbu X dan Sumbu Y).
- Visualisasi ini digunakan untuk mengidentifikasi arah korelasi, kekuatan hubungan, ketergantungan, atau pola interaksi antara dua buah variabel numerik kontinu.
- Sangat sering diaplikasikan dalam analisis awal _Machine Learning_ untuk mendeteksi linearitas regresi, pengelompokan (_clustering_), serta deteksi pencilan sebaran data.

### B. Kapan Harus Dihindari

- Scatter Plot mutlak tidak bisa digunakan apabila kumpulan data hanya memiliki satu dimensi variabel kuantitatif, karena grafik ini secara teknis memerlukan koordinat pasangan sumbu X dan Y untuk memplot titik koordinat data.

### C. Implementasi Python

```
# Menggunakan Matplotlib
import matplotlib.pyplot as plt
plt.scatter(df['Age'], df['Fare'])
plt.show()

# Menggunakan Seaborn (bisa kustomisasi warna dan gaya penanda kategori)
import seaborn as sns
sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived', style='Sex')
plt.show()

# Menggunakan Pandas
df.plot.scatter(x='Age', y='Fare')
plt.show()
```

#### [Wawasan Diskusi / Audio Insight]

- Korelasi positif digambarkan dengan titik-titik data yang bergerak naik dari kiri bawah ke kanan atas (contoh hubungan peningkatan tagihan terhadap besaran uang tip di restoran).
- Kustomisasi parameter **hue** dan **style** di Seaborn sangat berguna untuk menambahkan dimensi informasi ketiga dan keempat (seperti jenis kelamin dan keselamatan) langsung ke dalam plot titik koordinat.

---

## 3.6 Bar Plot / Bar Chart

### A. Definisi dan Kegunaan

- **Bar Plot** adalah grafik batang yang menyajikan nilai variabel kuantitatif untuk setiap kelompok data kategorikal menggunakan panjang batang yang proporsional.
- Grafik ini sangat ideal untuk membandingkan perbedaan kuantitas, ukuran, atau frekuensi kemunculan nilai diskrit lintas kategori nominal atau ordinal.

### B. Implementasi Python

```
# Menggunakan Matplotlib
import matplotlib.pyplot as plt
plt.bar(df['Category'], df['Revenue'])
plt.show()

# Menggunakan Seaborn (mendukung estimator statistik otomatis)
import seaborn as sns
import numpy as np
sns.barplot(data=df, x='Category', y='Revenue', estimator=np.median)
plt.show()

# Menggunakan Pandas
df.plot.bar(x='Category', y='Revenue')
plt.show()
```

#### [Wawasan Diskusi / Audio Insight]

- Secara bawaan (_default_), library Seaborn menggunakan estimator nilai rata-rata (_mean_). Penggunaan parameter **estimator** yang diatur ke nilai `np.median` atau fungsi statistik lain sangat membantu jika data mengandung bias ekstrem.

---

## 3.7 Pie Chart

### A. Definisi dan Kegunaan

- **Pie Chart** (diagram lingkaran) adalah grafik lingkaran yang dibagi menjadi beberapa irisan (_slices_) untuk memvisualisasikan proporsi bagian terhadap keseluruhan nilai total (_parts of a whole_).
- Besar sudut dan luas irisan berbanding lurus dengan nilai persentase kontribusi masing-masing kategori.

### B. Panduan Kapan Harus Dihindari

Penggunaan Pie Chart sangat dilarang pada kondisi analisis berikut:

- **Analisis Fluktuasi Waktu**: Tidak boleh digunakan untuk menunjukkan perkembangan nilai dari waktu ke waktu karena bentuknya statis.
- **Kategori Terlalu Banyak**: Jika kategori data melebihi 5 grup, irisan lingkaran akan menjadi sangat sempit sehingga sulit dibaca.
- **Nilai Antar Kategori Sangat Berdekatan**: Otak manusia kesulitan membedakan perbedaan ukuran sudut atau luas lingkaran jika nilainya hampir mirip (misalnya membedakan sudut persentase 24% vs 26% secara visual tanpa bantuan label angka).

### C. Implementasi Python

```
# Menggunakan Matplotlib
import matplotlib.pyplot as plt
plt.pie(df['Tips'], labels=df['Day'], autopct='%1.1f%%', explode=(0, 0.1, 0, 0))
plt.axis('equal')
plt.show()

# Menggunakan Pandas
df.plot.pie(y='Tips', labels=df['Day'], autopct='%1.2f%%')
plt.show()
```

#### [Wawasan Diskusi / Audio Insight]

- Dosen merekomendasikan penambahan parameter **explode** untuk memisahkan atau menonjolkan irisan kategori tertentu agar keluar sedikit dari lingkaran utama.
- Menambahkan parameter `autopct` sangat krusial guna menampilkan label teks persentase nilai kuantitatif secara eksplisit di atas masing-masing irisan diagram.

---

## 3.8 Heatmap

### A. Definisi dan Kegunaan

- **Heatmap** adalah peta visualisasi data dua dimensi dalam format tabel kisi (matriks) kompleks yang menggunakan kode warna (_color coding_) untuk mempresentasikan nilai ukuran numeriknya.
- Representasi nilai numerik digambarkan lewat gradasi atau intensitas warna; warna yang lebih pekat atau mencolok merepresentasikan nilai korelasi atau angka kuantitatif yang lebih kuat/tinggi.

### B. Aturan Pembacaan dan Skala Warna

- Heatmap korelasi menyajikan variabel data sebagai baris dan kolom tabel. Sumbu diagonal tengah biasanya bernilai `1.0` karena mengukur korelasi variabel terhadap dirinya sendiri.
- Interpretasi warna dilakukan menggunakan bar legenda visual di samping kanan diagram:
    - **Skala Monokromatik**: Gradasi satu warna dari terang ke gelap.
    - **Skala Divergen**: Menggunakan dua spektrum warna berlawanan (misalnya merah untuk korelasi negatif kuat, kuning untuk netral, dan hijau untuk korelasi positif kuat).

### C. Implementasi Python

```
# Membuat Simple Heatmap menggunakan Matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Misal matriks korelasi numeric
correlation_matrix = df[['total_bill', 'tip', 'size']].corr()
plt.pcolor(correlation_matrix, cmap='RdYlGn')
plt.colorbar()
plt.show()

# Membuat Correlation Heatmap menggunakan Seaborn
import seaborn as sns
import matplotlib.pyplot as plt
correlation_matrix = df[['total_bill', 'tip', 'size']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.show()
```

#### [Wawasan Diskusi / Audio Insight]

- Pada library Seaborn, menambahkan parameter **annot** bernilai `True` sangat penting untuk menampilkan nilai numerik koefisien korelasi asli secara presisi di dalam setiap kotak warna.
- Parameter **cmap** (seperti `'coolwarm'` atau `'RdYlGn'`) membantu analis mengatur peta palet warna grafik agar ramah bagi mata pembaca dan mudah diinterpretasikan.

---

## 3.9 Tipe Visualisasi Tambahan

Berikut adalah tipe visualisasi tingkat lanjut yang dibahas dalam materi kuliah:

### A. Sankey Diagrams

- Berguna untuk memvisualisasikan aliran (_flow_) serta hubungan kuantitas numerik antar beberapa entitas atau variabel dalam satu sistem terintegrasi.
- Umumnya diaplikasikan untuk pemetaan alur proses rekayasa sistem (_process engineering_), perjalanan konversi pengguna digital, atau analisis distribusi aliran energi.

### B. Treemaps

- Visualisasi efisien untuk menampilkan struktur data hierarkis secara bertingkat.
- Grafik ini memecah kategori-kategori utama ke dalam bentuk kotak persegi panjang bersarang (_nested rectangles_).
- Luas ukuran kotak persegi panjang mencerminkan porsi kontribusi nilai kuantitatif aslinya terhadap total keseluruhan.
- _Contoh Kasus_: Pemetaan pendapatan produk (_Product Revenue_) di mana kategori besar (minuman/_Beverages_) dibagi lagi ke dalam beberapa sub-kotak persegi panjang kecil di dalamnya (kopi, teh, dan minuman rasa khusus).

### C. Word Clouds

- Representasi visual interaktif untuk menyajikan data teks tak terstruktur.
- Ukuran fisik dari setiap kata pada grafik digambarkan berbanding lurus dengan tingkat frekuensi kemunculan kata tersebut di dalam dataset dokumen teks asli.

### D. Bubble Plot

- Pengembangan dari Scatter Plot dua dimensi.
- Memungkinkan analisis hubungan antar tiga buah variabel numerik sekaligus, di mana sumbu X menentukan posisi horizontal, sumbu Y menentukan posisi vertikal, dan variabel ketiga direpresentasikan oleh ukuran volume fisik dari lingkaran (_bubble_) titik data tersebut.

### E. Stacked Charts

- **Stacked Bar Chart**: Menggambarkan proporsi relatif atau nilai absolut dari komponen pembentuk kategori seiring waktu pada periode yang relatif singkat (_Few Periods_).
- **Stacked Area Chart**: Sangat efisien untuk melacak kontribusi kumulatif dari beberapa variabel seiring perkembangan waktu yang sangat panjang (_Many Periods_).



## Bab 4 Kesalahan Umum dalam Visualisasi Data (Common Pitfalls)


## 4.1 Pemilihan Jenis Grafik yang Salah (Choosing the Wrong Chart Type)

### A. Line Plot vs. Bar Plot pada Data Kategori dan Waktu

- **Line Plot** secara teknis dirancang khusus untuk menggambarkan kontinuitas dan perkembangan variabel dari waktu ke waktu (_time series data_). Grafik ini memperjelas tren kenaikan atau penurunan secara berkesinambungan.
- **Bar Plot** digunakan untuk menampilkan perbandingan nilai antar kategori diskrit (_discrete categories_). Penggunaan grafik batang memberikan penekanan visual pada perbedaan kuantitas mutlak antar kelompok yang terpisah.
- Memvisualisasikan data kategori diskrit menggunakan _Line Plot_ adalah kesalahan mendasar karena garis kontinu secara keliru menyiratkan adanya hubungan sekuensial atau alur waktu antar kategori tersebut.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menegaskan bahwa untuk data runtun waktu yang memiliki periode sangat sedikit (misalnya evaluasi tahunan dengan hanya 2 atau 3 titik waktu), penggunaan _Bar Plot_ masih diperbolehkan dan tidak dianggap salah sepenuhnya karena keterbatasan titik kontinuitasnya.
- Namun, jika data tidak memiliki elemen waktu sama sekali (misalnya perbandingan GDP antar negara pada satu tahun yang sama), penggunaan _Line Plot_ dilarang keras karena akan menyesatkan penafsiran pembaca seolah-olah ada perkembangan dari satu negara ke negara lain.

### B. Kasus Menghindari Bar Plot (When to Avoid Bar Plot)

- Grafik batang tunggal tidak ideal digunakan ketika analis memiliki beberapa variabel yang secara kolektif merupakan bagian dari satu kesatuan utuh (_parts of a whole_).
- Contoh Kasus: Data penjualan buku fiksi (_Fiction Book Sales_) yang terbagi menjadi lima kategori terpisah (seperti _Young adult, Classics, Mystery, Romance,_ dan _Sci-fi_). Karena kelima kategori tersebut mencakup seluruh pangsa pasar buku fiksi, jumlah akumulasi nilainya merepresentasikan volume total pasar fiksi (100%).
- Jika data ini dipaksakan menggunakan grafik batang biasa lintas tahun, pembaca harus melakukan perhitungan matematika manual secara mandiri untuk memahami kontribusi masing-masing kategori terhadap total volume penjualan dari tahun ke waktu.

#### [Wawasan Diskusi / Audio Insight]

- Dosen menekankan bahwa jika visualisasi memaksa audiens melakukan perhitungan matematika sendiri untuk menarik kesimpulan dasar, maka visualisasi tersebut gagal. Dalam kondisi tersebut, menyajikan data dalam bentuk tabel mentah yang terstruktur jauh lebih baik daripada membuat grafik yang membingungkan.
- Solusi teknis untuk kasus akumulasi bagian dari keseluruhan ini adalah menggunakan _Stacked Bar Chart_ (untuk membandingkan nilai absolut komponen) atau _100% Stacked Bar Chart_ (untuk membandingkan kontribusi persentase komponen seiring waktu).

### C. Kasus Menghindari Pie Chart (When to Avoid Pie Chart)

- **Pie Chart** dilarang keras digunakan dalam analisis yang bertujuan untuk menunjukkan perkembangan atau perubahan nilai suatu variabel dari waktu ke waktu (_over time_).
- **Pie Chart** akan menjadi sangat menyesatkan (_misleading_) apabila analis sengaja atau tidak sengaja menghilangkan sebagian kategori data sehingga total persentase komponen di dalam lingkaran tidak mencapai 100% nilai sebenarnya.

#### [Wawasan Diskusi / Audio Insight]

- Dosen memberikan contoh kasus riil pada tingkat manajemen puncak (_top management_): Jika sebuah perusahaan mengoperasikan tiga divisi terpisah, penggunaan _Pie Chart_ hanya boleh dilakukan untuk membandingkan kontribusi pendapatan dari ketiga divisi tersebut secara lengkap sehingga membentuk akumulasi 100%.
- Jika analis hanya memasukkan data pendapatan dari dua divisi saja ke dalam _Pie Chart_, visualisasi tersebut dikategorikan sebagai manipulasi informasi karena basis pembagian 100% lingkaran telah bergeser secara tidak sah dan memberikan representasi proporsi yang salah.
- Banyak ahli visualisasi merekomendasikan untuk menghindari _Pie Chart_ secara umum karena mata manusia secara alami lebih sulit membandingkan ukuran luas sudut lingkaran (_angle_) dibanding membandingkan tinggi batang linier. Alternatif terbaik pengganti _Pie Chart_ adalah _Bar Chart_, _Box Plot_, atau _Dot Plot_.

---

## 4.2 Kepadatan Informasi yang Berlebihan (Overloading with Information)

### A. Kompleksitas Visual Berlebih pada Plot tunggal

- Memasukkan terlalu banyak komponen visual seperti garis (_lines_), penanda titik (_markers_), legenda, teks, dan elemen dekoratif tambahan (_clutter_) ke dalam satu area grafik akan mengaburkan pola sebaran data asli.
- Kondisi ini dikenal sebagai _Overloading Info_ yang mengakibatkan beban kognitif berlebih bagi audiens (_overwhelming the viewer_) sehingga tujuan penyampaian wawasan utama gagal dicapai.

#### [Wawasan Diskusi / Audio Insight]

- Dosen mencontohkan sebuah grafik tren penjualan produk di mana satu garis tunggal diberi penanda (_marker_) yang berbeda-beda untuk setiap titiknya (misalnya titik berwarna biru bulat, titik orange kotak, dan titik ungu silang).
- Penambahan variasi bentuk _marker_ ini dinilai tidak berguna (_useless_) dan merusak kerapian visual (_decluttering_) karena perbedaan warna garis saja sebenarnya sudah sangat memadai untuk membedakan kategori produk tersebut.
- Contoh kesalahan fatal lainnya adalah memaksa memasukkan seluruh dimensi variabel ke dalam satu grafik scatter plot menggunakan kombinasi warna (_color_) dan bentuk penanda (_style_) sekaligus. Misalnya, memetakan variabel hari dengan warna berbeda dan waktu makan (_lunch_/_dinner_) dengan bentuk bulat dan silang. Grafik kombo ini menjadi terlalu padat, sangat membingungkan untuk dibaca, dan menyulitkan analis untuk menarik wawasan yang bermakna.

---

## 4.3 Skala dan Sumbu yang Tidak Konsisten (Inconsistent Scales and Axes)

### A. Distorsi Analisis Akibat Penyatuan Skala Berbeda

- Plotting dua atau lebih dataset yang memiliki rentang nilai kuantitatif (_scale_) yang berbeda sangat jauh pada sumbu Y (_Y-axis_) yang sama akan menyembunyikan hubungan (_obscure relationships_) dan tren riil data tersebut.
- Dataset yang memiliki nilai numerik kecil akan tertekan ke bagian bawah grafik dan tampak stagnan tanpa fluktuasi, sementara dataset berangka besar akan mendominasi visualisasi.

#### [Wawasan Diskusi / Audio Insight]

- Dosen memaparkan contoh kasus konkrit di mana analis mencoba menggambarkan hubungan antara data Penjualan Bulanan (_Monthly Sales_ dalam satuan dolar yang bernilai ratusan hingga ribuan) dan data Suhu Rata-rata (_Average Temperature_ dalam derajat Celsius yang bernilai kecil antara 20 hingga 40) pada satu grafik sumbu Y yang sama.
- Akibat penyatuan sumbu Y ini, kurva _Average Temperature_ tampak berupa garis lurus horizontal yang flat di dekat angka 0 karena skalanya terdistorsi oleh angka penjualan bulanan yang mencapai ratusan dolar.
- Solusi teknis mutlak untuk mengatasi masalah ini adalah dengan menerapkan sumbu sekunder (_secondary axis_). Sumbu Y sebelah kiri dikonfigurasi khusus untuk skala Penjualan Bulanan (_Monthly Sales_), sedangkan sumbu Y sebelah kanan (_secondary Y-axis_) dikonfigurasi untuk skala Suhu Rata-rata (_Average Temperature_). Dengan demikian, kedua pola fluktuasi data dapat ter-render secara proporsional dan korelasinya dapat dianalisis dengan akurat.

---

## 4.4 Penggunaan Warna yang Menyesatkan (Misleading Use of Colors)

### A. Inkonsistensi Identitas Warna Lintas Grafik

- Penggunaan warna yang tidak konsisten untuk merepresentasikan kategori data yang sama di beberapa grafik berbeda dalam satu presentasi akan membingungkan audiens.
- Otak audiens secara otomatis membangun asosiasi bahwa satu warna tertentu mewakili satu entitas tetap. Ketika asosiasi warna ini diacak pada grafik berikutnya, audiens akan salah menginterpretasikan korelasi antar data.

#### [Wawasan Diskusi / Audio Insight]

- Dosen mencontohkan kasus pembuatan dua grafik batang berdampingan yang menyajikan perbandingan kinerja kategori produk yang sama (misalnya Kategori A, B, C, dan D).
- Pada grafik pertama (Dataset 1), Kategori A digambarkan dengan batang berwarna merah muda (_pink_). Namun pada grafik kedua (Dataset 2) di slide atau halaman yang sama, Kategori A digambarkan dengan batang berwarna hijau.
- Inkonsistensi warna ini dinilai merusak logika penyampaian pesan. Solusi perbaikannya adalah menerapkan palet warna yang seragam lintas grafik: jika Kategori A diwarnai merah muda di grafik pertama, maka Kategori A wajib diwarnai merah muda di seluruh grafik berikutnya dalam dokumen tersebut.

---

## 4.5 Ringkasan Karakteristik Pitfalls Visualisasi Data

Berikut adalah tabel klasifikasi kesalahan umum visualisasi data beserta dampak dan solusi teknis perbaikannya:

|Jenis Pitfall|Deskripsi Singkat Kesalahan|Dampak pada Audiens|Solusi Teknis Perbaikan|
|:--|:--|:--|:--|
|**Wrong Chart Type**|Menggunakan _Line Plot_ untuk kategori non-waktu, atau _Pie Chart_ untuk tren runtun waktu.|Salah menafsirkan adanya kontinuitas atau hubungan sekuensial yang sebenarnya tidak ada.|Gunakan _Bar Plot_ untuk kategori terpisah; _Line Plot_ hanya untuk dimensi waktu kontinu.|
|**Information Overloading**|Menambahkan terlalu banyak garis, warna, dan bentuk _markers_ berbeda dalam satu plot tunggal.|Mengalami beban kognitif tinggi (_overwhelming_) dan pola data penting menjadi tersembunyi.|Terapkan _decluttering_; batasi pemakaian _markers_ jika warna saja sudah cukup membedakan.|
|**Inconsistent Scales**|Memplot dua variabel berskala beda jauh (misal: suhu vs. dolar) pada sumbu Y yang sama.|Grafik variabel berskala kecil tampak flat dan kehilangan visualisasi pola fluktuasinya.|Konfigurasikan sumbu sekunder (_secondary Y-axis_) di sisi kanan grafik untuk variabel kedua.|
|**Misleading Colors**|Menggunakan warna berbeda untuk satu kategori yang sama di grafik yang berbeda.|Membingungkan asosiasi visual audiens dan merusak konsistensi hubungan data.|Terapkan palet warna yang seragam lintas grafik untuk kategori yang identik.|
|**Incomplete Category Pie**|Membuat _Pie Chart_ dengan sengaja mengeliminasi salah satu divisi/kategori penting.|Proporsi total persen (100%) bergeser sehingga menghasilkan representasi persentase yang palsu.|Wajib menyertakan seluruh kategori pembentuk totalitas (100%) di dalam lingkaran.|



## Bab 5 Sesi Praktik & Evaluasi Pembelajaran


## 5.1 Latihan Praktis Menggunakan Dataset Titanic

### A. Deskripsi Tugas Analisis Data dan Grafik

Latihan praktis menggunakan dataset Titanic dirancang untuk menguji kemampuan pengolahan, manipulasi, serta visualisasi data secara langsung menggunakan Python. Latihan ini memanfaatkan library Pandas untuk manipulasi data, serta Matplotlib dan Seaborn untuk pembuatan grafik. Terdapat lima tugas visualisasi utama yang harus diselesaikan oleh peserta:

- **Tugas 1 (Bar Plot - Survivor Comparison)**: Membandingkan jumlah penumpang yang selamat (survivor) dengan penumpang yang tidak selamat menggunakan Bar Plot. Analisis ini ditujukan untuk melihat kelompok mana yang memiliki frekuensi penumpang lebih banyak.
- **Tugas 2 (Histogram - Age Distribution)**: Memvisualisasikan sebaran atau distribusi usia (age) dari seluruh penumpang Titanic menggunakan Histogram untuk mengamati karakteristik demografis penumpang.
- **Tugas 3 (Box Plot - Fare Distribution)**: Membandingkan sebaran nilai tarif (fare) antara kelompok penumpang yang selamat dan yang tidak selamat menggunakan Box Plot. Tujuan tugas ini adalah menganalisis nilai median tarif serta mengidentifikasi keberadaan pencilan (outliers).
- **Tugas 4 (Scatter Plot - Age vs Fare)**: Memvisualisasikan hubungan dua dimensi antara variabel usia (age) dan tarif perjalanan (fare) menggunakan Scatter Plot untuk mengamati ada tidaknya pola korelasi atau sebaran tertentu.
- **Tugas 5 (Correlation Heatmap - Numerical Variables)**: Membuat Heatmap korelasi untuk seluruh variabel kuantitatif (numerik) di dalam dataset Titanic untuk mengidentifikasi pasangan variabel mana yang memiliki kekuatan hubungan korelasi paling tinggi.

#### [Wawasan Diskusi / Audio Insight]

- **Tugas 1 (Bar Plot - Survivor Comparison)**:
    - Berdasarkan proses pengerjaan latihan di kelas, penghitungan jumlah penumpang yang tidak selamat (label 0) dan yang selamat (label 1) dilakukan dengan menerapkan method `.value_counts()` pada kolom `survived`. Hasil perhitungan riil menunjukkan jumlah penumpang tidak selamat sebanyak 549 orang, sedangkan yang selamat sebanyak 342 orang.
    - Untuk mempermudah interpretasi bagi audiens non-teknis, indeks sumbu X (default bernilai 0 dan 1) sebaiknya ditimpa secara manual menggunakan list nama kategori baru seperti `['Not survive', 'Survive']` atau `['No', 'Yes']` agar grafik lebih komunikatif.
- **Tugas 2 & 3 (Distribusi Usia dan Fare)**:
    - Pembacaan sebaran grafik menunjukkan bahwa pada kelompok penumpang kelas dua (second class), penumpang anak-anak atau yang berusia sangat muda memiliki tingkat keselamatan yang tinggi.
    - Box plot tarif membantu analis mendeteksi pencilan (outliers) berupa nilai tarif perjalanan ekstrem yang jauh melampaui rentang sebaran mayoritas penumpang.
- **Tugas 5 (Correlation Heatmap)**:
    - Untuk menghindari bias analisis, data kategorikal (non-numerik) harus disaring terlebih dahulu sebelum dimasukkan ke dalam perhitungan korelasi. Penyaringan dilakukan di Python menggunakan method `.select_dtypes(include='number')` pada data frame.
    - Kolom `PassengerId` wajib dibuang menggunakan method `.drop(columns=['PassengerId'])`. Meskipun bertipe numerik, kolom ini secara esensi hanyalah nomor urut atau identifier unik penumpang. Jika diikutsertakan dalam matriks korelasi, data ini akan mendistorsi interpretasi kekuatan korelasi antar variabel analitik rill lainnya.

---

## 5.2 Metode Evaluasi Akhir

### A. Komponen Penilaian Akhir

Sistem evaluasi kelulusan pada akhir modul pembelajaran ini terdiri atas dua instrumen utama:

1. **Ujian Tertulis (Exam)**: Berupa ujian pilihan ganda (_multiple choice_) yang bertujuan untuk menguji tingkat pemahaman teoritis siswa mengenai prinsip visualisasi, anatomi grafik, serta fungsionalitas perkakas visualisasi data.
2. **Tantangan Pemrograman (Code Challenge)**: Berupa ujian praktis mandiri untuk melatih logika pemrograman, kemampuan algoritma, serta penyelesaian masalah (_problem solving_) menggunakan platform online.

### B. Aturan dan Komposisi Code Challenge LeetCode

Tantangan pemrograman dilakukan menggunakan platform LeetCode dengan rincian komposisi bobot penilaian sebagai berikut:

|Tingkat Kesulitan Soal|Jumlah Soal|Bobot Nilai per Soal|Total Nilai Maksimal|
|:--|:--|:--|:--|
|**Easy**|3 Soal|20 Poin|60 Poin|
|**Medium**|1 Soal|40 Poin|40 Poin|

#### [Wawasan Diskusi / Audio Insight]

- **Mekanisme Bukti Pengerjaan (Submission)**:
    - Pengerjaan soal dilakukan menggunakan akun LeetCode pribadi masing-masing peserta.
    - Siswa wajib menyerahkan dua bukti pengerjaan fisik untuk divalidasi oleh tim pengajar:
        1. **Tautan Profil (Profile Link)**: URL lengkap menuju halaman profil akun LeetCode siswa.
        2. **Tangkapan Layar (Screenshot)**: Gambar tangkapan layar yang memuat informasi nama soal, status pengerjaan yang sukses (**Accepted**), serta nama akun siswa yang bersangkutan secara jelas.
    - Poin penilaian hanya akan dihitung apabila melampirkan kedua bukti di atas secara lengkap.
- **Kebijakan Kejujuran Akademik**:
    - Seluruh tugas tantangan pemrograman wajib diselesaikan secara mandiri. Segala bentuk indikasi plagiarisme, kerja sama tidak sah, atau menyalin solusi murid lain akan ditindak tegas dan memengaruhi penilaian kelulusan.
- **Manajemen Waktu**:
    - Seluruh dokumen bukti harus diunggah melalui formulir pengumpulan resmi sebelum modul pembelajaran berakhir. Keterlambatan pengumpulan akan mengikuti aturan penalti waktu yang dikelola oleh tim operations.



## Lecture Notes Module 1 Session 13

Definisi data visualizaion: presemtaso data pirctorial dan graphical format. 

mengapa penting: 
1. Mengkomunikasikan data menjadi gambar. 
2. Mengeksplorasi kemungkinan visualisasi data yang paling cocok.
3. Mengekspolasi insight dari data yang terbatu oleh visual. 
4. Melihat yang tidak terlihat di tabel. 

cara melakukan visualisasi data:
1. Memahami dulu konteks data. 
2. buat berdasarkan pertanyaan. 
3. Pilih jenis data dan indetifikasi pesannya. 
4. technical:
	1. Title. 
	2. Sumbu x, y
	3. lable
	4. mark data points
	5. memainkan warna
5. memberikan konklusi. 
6. Tipe data visuaslization:
	1. Comparison
	2. Composition
	3. Relationship
	4. Deistribution

Heatmap:
Melihat korelasi data melalui color code. 

Word clouds:
Melihat kata kata apa yang paling seringmuncul. Pakai rasio ukuran. 

Sankey:
Melihat flow. 


Jebakan umum:
1. Memilih tipe data yang salah. 
2. Informasi yang terlalu banyak. 
3. scales dan axis kebanyakan. 
4. Menggunakan warna yang misleading. 

Seaborn:
visualisasi data berbadis matpotlib yang high level iterface. 

Boxplot
![[Pasted image 20260826201856.png]]

linplot:
untuk tipe data yang memiliki time series, agar bisa melihat trend. 
	Kapan pakai ini?
	1. ketika single dan multiple variable diplot waktunya. 

Scatterplot:
variable harus numerik. 
digunakan untuk melihat realtionship antar variable. 
Kapan menghindari ini? ketika tidak memiliki bi-dimentional data. 
tidak cocok untuk mengobservasi pattern waktu. 

barplot:
chart untuk menunjukan data kategorikal. tingginya menunjukan value.
Kapn hindari ini? jika ada banyak yang adalah bagian dari suatu kesatuan. 

Piechart:
Kapan gunakan ini? 

heatmap:
Melihat korelasi 2 variable. 

corrleation heatmapt:
khusus untuk melihat korlasi 2d. 




---
