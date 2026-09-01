---
tags: [jcaieh/module1, sesi-13, data-visualization, matplotlib, seaborn, pandas-plotting, boxplot, histogram, scatterplot, heatmap, chart-selection, jcaieh/module1/sesi13]
bootcamp: JCAIEH
module: 1
session: 13
aliases: ["Sesi 13", "Data Visualization", "Visualisasi Data"]
---

# Sesi 13 - Data Visualization

> Sumber: rangkuman gabungan slide/PDF resmi + transkrip audio kelas (ditandai sebagai callout Audio Insight di bawah), dilengkapi konteks tambahan dan tautan silang ke sesi lain.

---

## Bab 1 Konsep Dasar Visualisasi Data

### 1.1 Pengertian dan Signifikansi Visualisasi Data

#### A. Definisi Visualisasi Data

- **Data Visualization** adalah penyetelan atau penyajian data dalam format gambar atau grafis (_pictorial or graphical format_).
- Bidang ini merupakan suatu disiplin ilmu untuk memahami data dengan menyajikannya secara visual agar pola (_patterns_), tren (_trends_), komposisi (_composition_), perbandingan (_comparison_), dan hubungan (_relationship_) dapat terungkap (_exposed_).

> [!tip] Audio Insight — Otak manusia lebih cepat memproses gambar daripada spreadsheet
> - Menyampaikan wawasan (_insight_) sering kali sulit jika analis hanya memiliki data mentah (_raw data_).
> - Menyajikan data dalam format visual yang mudah dimengerti sangat penting karena otak manusia (_human brain_) memproses informasi visual jauh lebih cepat dan mudah dibandingkan dengan lembar kerja (_spreadsheet_) atau laporan teks biasa.
> - Dalam praktik di industri, sering terjadi redundansi di mana pengambil keputusan (_manager_ atau _VP_) tetap meminta data mentah (_raw data_) ditarik secara manual meskipun analis telah menyusun dasbor (_dashboard_) visual yang sangat informatif. Menyajikan tabel mentah tanpa visualisasi adalah praktik yang buruk karena menghambat komunikasi wawasan.

#### B. Signifikansi Visualisasi Data dibanding Statistik dan Tabel Mentah

- Visualisasi data mempercepat identifikasi peristiwa tidak biasa (_uncommon event_) atau anomali (_anomaly_).
- Analisis statistik deskriptif mampu merangkum data (_summarize data_), namun sering kali menyembunyikan pola (_hide patterns_) yang krusial. Pola-pola ini tidak akan muncul jika analis hanya mengandalkan ringkasan nilai statistik.

> [!tip] Audio Insight — Ringkasan statistik yang sama, bentuk visual bisa sangat berbeda
> - Sebagai contoh kasus, saat mendeteksi anomali pada hubungan antara tahun (_year_) dan penjualan (_sales_), menggunakan grafik visual membuat anomali tersebut langsung teridentifikasi. Sebaliknya, jika menggunakan tabel mentah (meskipun hanya terdiri dari 26 baris), proses pencarian anomali akan jauh lebih sulit dan memakan waktu.
> - Tantangan analisis tabel mentah ini akan menjadi mustahil ditangani secara manual apabila ukuran data sangat besar, misalnya mencapai 1 juta baris data yang tidak muat dalam satu halaman layar.
> - Contoh kasus keterbatasan statistik: Sekumpulan data yang memiliki ringkasan statistik yang mirip (seperti nilai rata-rata/_mean_ sumbu X dan Y, standar deviasi/_standard deviation_, serta korelasi/_correlation_ sebesar -0,06) dapat memiliki bentuk sebaran visual yang sangat berbeda dan unik ketika diplot. Wawasan riil tersebut hanya bisa diperoleh melalui visualisasi data. _(Ini merujuk pada fenomena terkenal "Anscombe's Quartet" / "Datasaurus Dozen" di literatur statistika — dataset dengan mean, std, dan korelasi yang identik tapi bentuk sebaran sangat berbeda.)_

**Contoh kode — membuktikan poin di atas: statistik sama, bentuk beda (mirip Anscombe's Quartet):**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
# Dataset 1: sebaran linear normal
x1 = np.linspace(0, 10, 50)
y1 = 2 * x1 + np.random.normal(0, 2, 50)

# Dataset 2: sebaran melengkung (kuadratik) yang direkayasa agar mean/std mirip
x2 = np.linspace(0, 10, 50)
y2 = -0.5 * (x2 - 5)**2 + 15 + np.random.normal(0, 1, 50)

print("Mean Y1:", round(y1.mean(), 2), "| Std Y1:", round(y1.std(), 2))
print("Mean Y2:", round(y2.mean(), 2), "| Std Y2:", round(y2.std(), 2))
# Ringkasan angka bisa terlihat mirip, tapi baru KELIHATAN jelas bedanya saat diplot:

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].scatter(x1, y1)
axes[0].set_title("Dataset 1: Linear")
axes[1].scatter(x2, y2)
axes[1].set_title("Dataset 2: Kuadratik (melengkung)")
plt.show()
```

---

### 1.2 Metodologi dan Alur Proses Visualisasi Data

#### A. Tahapan Eksekusi Visualisasi Data

1. **Memahami Konteks Data** (_Understand the Context of Your Data_): Memahami asal-usul, tipe, dan domain dari data yang dianalisis sebelum mulai membuat visualisasi.
2. **Merumuskan Pertanyaan Data** (_Making Some Questions For Your Data_): Menentukan hipotesis atau pertanyaan bisnis yang ingin dipecahkan (seperti mencari produk terlaris atau faktor yang memengaruhi pelanggan).
3. **Memilih Jenis Visualisasi yang Tepat** (_Choose Appropriate Type of Visualization_): Menentukan jenis grafik yang paling sesuai dengan tipe variabel data yang akan diplot.
4. **Mengidentifikasi Pesan Utama** (_Identify the Message of Each Visualization You Made_): Memastikan setiap grafik yang dibuat menyampaikan pesan spesifik yang jelas bagi audiens.
5. **Konfigurasi Teknis** (_Technical Perspective_): Melengkapi grafik dengan judul (_title_), label sumbu (_axis labels_), legenda (_legend_), penanda poin penting (_mark interesting data points_), serta mengoptimalkan penggunaan warna dan ukuran (_color and size_).
6. **Menarik Kesimpulan** (_Get Conclusion_): Merumuskan kesimpulan akhir dan merekomendasikan keputusan (_decision_) tindakan bisnis berdasarkan visualisasi tersebut.

> [!tip] Audio Insight — Kenapa grafik garis tidak cocok untuk GDP antar negara
> - Melakukan eksplorasi data (_explore data_) menggunakan visualisasi sangat krusial di awal proyek sains data untuk membantu analis memahami karakteristik data sebelum melatih model pembelajaran mesin (_machine learning_). Eksplorasi data ini meningkatkan peluang ditemukannya wawasan berharga.
> - Memilih jenis grafik yang salah akan mengaburkan perbandingan informasi. Sebagai contoh kasus: data Produk Domestik Bruto (_Gross Domestic Product - GDP_) tidak cocok divisualisasikan dengan grafik garis (_line chart_). Grafik garis secara teknis menyiratkan kontinuitas dan perkembangan variabel dari waktu ke waktu (_over time_), sehingga memerlukan adanya dimensi waktu (_time series data_).
> - Visualisasi data tidak boleh berhenti pada penyajian gambar saja; analis wajib menyertakan kesimpulan (_conclusion_) dan rekomendasi keputusan (_decision_) nyata untuk pengambil kebijakan.

---

### 1.3 Prinsip Utama Visualisasi Data yang Efektif

| Prinsip Utama | Deskripsi Teknis |
|:--|:--|
| **Clarity** | Kejelasan informasi yang menjamin grafik mudah dipahami dan tidak membingungkan pembaca (_avoid confusion_). |
| **Accuracy** | Akurasi plot yang menjamin representasi visual sesuai dengan nilai data asli (_accurate representation_) dan tidak melenceng. |
| **Simplicity** | Kesederhanaan desain yang memprioritaskan opsi visual paling sederhana guna menghindari kompleksitas yang berlebihan (_avoid complexity_). |
| **Visual Hierarchy** | Hierarki visual yang mengatur elemen grafik secara terstruktur sehingga penyampaian informasi mengalir dengan runut (_storytelling_). |

> [!tip] Audio Insight — "How to Lie with Data/Statistics" dan alur storytelling
> - **Clarity (Kejelasan)**: Dosen merujuk pada literatur berjudul _"How to Lie with Data"_ (atau _"How to Lie with Statistics"_ — buku yang sama dibahas di [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]] Bab 7.1). Buku ini menguraikan bagaimana visualisasi data dapat dimanipulasi secara sengaja untuk menghasilkan grafik yang menyesatkan (_misleading_) bagi pembacanya.
> - **Accuracy (Akurasi)**: Visualisasi yang tidak akurat (misalnya karena manipulasi skala sumbu) akan mendistorsi perbandingan data yang sebenarnya. Nilai visual yang tampak pada grafik harus benar-benar selaras dengan nilai data (_value data_) asli.
> - **Simplicity (Kesederhanaan)**: Analis harus mendahulukan visualisasi yang paling sederhana. Hindari penambahan dekorasi kompleks atau elemen visual berlebih yang tidak relevan karena akan membingungkan audiens.
> - **Visual Hierarchy (Hierarki Visual)**: Pengaturan visual yang baik membantu analis bercerita (_storytelling_) secara terstruktur. Struktur visual sebaiknya dibuat mengalir, misalnya: menyajikan tren makro di bagian atas, faktor-faktor pengaruh di bagian tengah, hingga rincian mikro di bagian bawah. Cara ini mencegah alur pembacaan yang melompat-lompat (seperti dari bawah langsung ke atas).

---

### 1.4 Elemen-Elemen pada Grafik Visualisasi

#### A. Anatomi Grafik (_Anatomy of a Chart_)

- **Chart Title**: Judul utama yang mendeskripsikan secara eksplisit informasi yang dimuat dalam grafik.
- **Axis Labels**: Label penjelas sumbu koordinat, yang terdiri atas **Horizontal Axis Label (Sumbu X)** dan **Vertical Axis Label (Sumbu Y)** untuk menerangkan variabel apa yang sedang diukur.
- **Axis Values**: Skala nilai numerik atau kategori diskrit yang tertera pada sumbu koordinat, yaitu **Horizontal Axis Values** dan **Vertical Axis Values**.
- **Legend**: Legenda atau keterangan simbol untuk membedakan kategori, variabel, atau grup data yang digambarkan dengan warna atau penanda berbeda.
- **Data Labels**: Teks atau angka yang diletakkan langsung pada titik data untuk menunjukkan nilai kuantitatif aslinya secara presisi.
- **Chart Area**: Wilayah utama tempat data visual (seperti batang, garis, atau titik pencar) diplot.
- **Gridlines**: Garis kisi bantu di latar belakang area grafik untuk memudahkan mata pembaca menyelaraskan posisi titik data dengan nilai pada sumbu koordinat.

> [!tip] Audio Insight — Fungsi Matplotlib untuk tiap elemen anatomi
> Dalam implementasi praktis menggunakan bahasa pemrograman Python, elemen-elemen anatomi ini didefinisikan secara manual di dalam blok kode. Sebagai contoh, pustaka `Matplotlib` menyediakan fungsi-fungsi spesifik seperti `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.legend()`, dan `plt.grid()` untuk menampilkan komponen tersebut pada layar.

**Contoh kode — anatomi grafik lengkap dalam satu contoh:**

```python
import matplotlib.pyplot as plt

bulan = ['Jan', 'Feb', 'Mar', 'Apr']
penjualan_2023 = [100, 120, 90, 140]
penjualan_2024 = [110, 130, 105, 160]

plt.plot(bulan, penjualan_2023, marker='o', label='2023')
plt.plot(bulan, penjualan_2024, marker='o', label='2024')

plt.title("Perbandingan Penjualan Bulanan 2023 vs 2024")   # Chart Title
plt.xlabel("Bulan")                                          # Horizontal Axis Label
plt.ylabel("Penjualan (unit)")                                # Vertical Axis Label
plt.legend()                                                  # Legend
plt.grid(True)                                                 # Gridlines
plt.show()                                                     # Chart Area otomatis terisi oleh plt.plot()
```

---

### 1.5 Kategori Utama Visualisasi Berdasarkan Tujuan

Tipe visualisasi data dikelompokkan ke dalam empat kategori utama sesuai dengan tujuan analisis yang ingin dicapai:

#### A. Comparison (Perbandingan)

- Digunakan untuk membandingkan nilai kuantitatif antar item atau melacak perubahannya seiring waktu.
- **Comparison Among Items (Perbandingan Antar Item)**:
    - Satu variabel per item (_One variables per items_):
        - Kategori sedikit (_Few items_): Menggunakan **Bar Chart** atau **Bar Plot**.
        - Kategori banyak (_Many items_): Menggunakan **Table with embedded chart**.
    - Dua variabel per item (_Two variables per items_): Menggunakan **Variable with column chart** (grafik kolom berkelompok).
- **Comparison Over Time (Perbandingan Seiring Waktu)**:
    - Satu variabel (_One variable_):
        - Periode banyak (_Many Periods_): Menggunakan **Line Chart**.
        - Periode sedikit (_Few Periods_): Menggunakan **Bar Chart** atau **Bar Plot**.
    - Banyak variabel / Kategori berbeda pada variabel sama (_Many variables / Same variables different categories_): Menggunakan **Multiple Line Chart**.

> [!tip] Audio Insight — Contoh kasus Comparison
> - Contoh kasus perbandingan kategori: Jika ingin membandingkan satu variabel diskrit seperti nilai penjualan pada kategori _office supplies_, _furniture_, dan _technology_, pilihan terbaik adalah menggunakan _Bar Chart_.
> - Jika terdapat dua variabel (misalnya kategori produk sekaligus pembagian segmen konsumen seperti _consumer_, _corporate_, dan _home office_), visualisasi yang tepat adalah _Variable with column chart_ yang membedakan segmen menggunakan variasi warna batang di dalam kelompok kategori tersebut.
> - Contoh kasus perbandingan tren waktu: Apabila data memiliki periode waktu yang sangat panjang atau tingkat kedetailan (_granularity_) yang tinggi (seperti harian atau mingguan dari tahun 2019 sampai 2020), penggunaan grafik garis (_line chart_) jauh lebih mudah dibaca dibandingkan grafik batang (_bar chart_).

#### B. Composition (Komposisi)

- Digunakan untuk menunjukkan bagian-bagian atau kontribusi komponen yang membentuk satu kesatuan utuh.
- **Composition Static (Komposisi Statis)**:
    - Menunjukkan bagian dari total (_Share of total_): Menggunakan **Pie Chart**.
    - Akumulasi atau pengurangan nilai dari total (_Accumulation or subtraction of total_): Menggunakan **Waterfall Chart**.
    - Proporsi bagian per item atau kategori (_Share of total per items or category_): Menggunakan **Stacked Bar Chart**.
    - Struktur proporsi dengan kategori yang sangat banyak (_Share of total many items or category_): Menggunakan **Tree Map**.
- **Composition Over Time (Komposisi Seiring Waktu)**:
    - Periode sedikit (_Few Periods_): Menggunakan **Stacked Bar Chart**.
    - Periode banyak (_Many Periods_): Menggunakan **Stacked Area Chart**.

> [!tip] Audio Insight — Contoh Tree Map dan Stacked Chart
> - Contoh kasus _Tree Map_: Efektif untuk menggambarkan data yang memiliki struktur hierarkis. Misalnya, visualisasi pendapatan produk yang dikelompokkan ke dalam kategori besar (seperti _beverages_, _baked goods_, _snacks_, dan _merchandise_) di mana masing-masing kategori tersebut dipecah lagi ke dalam sub-kategori (seperti kategori _beverages_ yang dipecah menjadi _coffee_ 43%, _tea_ 23%, dan _specialty drinks_ 34%). Ukuran kotak menggambarkan kontribusi nilai aslinya.
> - Contoh kasus komposisi seiring waktu: Gunakan _Stacked Bar Chart_ biasa untuk menunjukkan perkembangan nilai absolut komponen seiring waktu. Gunakan _100% Stacked Bar Chart_ apabila fokus analisis adalah membandingkan persentase kontribusi komponen dari waktu ke waktu. Untuk rentang waktu yang sangat panjang dengan banyak titik periode, gunakan _Stacked Area Chart_ (grafik area bertumpuk).

#### C. Relationship (Hubungan)

- Digunakan untuk menemukan korelasi, interaksi, atau keterkaitan antara variabel numerik kontinu.
- **Dua variabel** (_Two variables_): Menggunakan **Scatter Plot**.
- **Tiga variabel** (_Three variables_): Menggunakan **Bubble Plot**.

> [!tip] Audio Insight — Contoh hubungan total bill vs tip
> Contoh kasus hubungan dua variabel: Digunakan untuk memetakan hubungan antara total tagihan (_total bill_) dan besaran uang tip (_tip_) yang diberikan oleh pelanggan restoran. Sumbu X merepresentasikan _total bill_ dan sumbu Y merepresentasikan _tip_. Scatter plot akan memplot titik-titik koordinat untuk melihat tren positif (apakah semakin besar nilai tagihan berkolerasi dengan semakin besarnya tip yang diberikan).

#### D. Distribution (Distribusi)

- Digunakan untuk melihat sebaran data, kerapatan data, atau frekuensi kemunculan nilai numerik.
- **Satu variabel** (_One variable_): Menggunakan **Histogram** atau **Box Plot**.
- **Dua variabel** (_Two variables_): Menggunakan **Scatter Plot**.

> [!tip] Audio Insight — Kombinasi Histogram + Box Plot, dan Violin Plot
> - Contoh kasus distribusi satu variabel: Menggunakan _Histogram_ untuk membagi variabel numerik tunggal ke dalam interval-interval tertentu (_bins_) guna menghitung berapa banyak frekuensi observasi data yang jatuh ke dalam setiap interval tersebut.
> - Aspek visual _Histogram_ dan _Box Plot_ dapat digabungkan ke dalam satu visualisasi kombo (_combo visualization_) untuk memberikan analisis statistik yang lebih lengkap.
> - Pilihan lainnya adalah menggunakan _Violin Plot_ yang secara teknis menggabungkan visualisasi _Box Plot_ (untuk ringkasan nilai kuartil dan median) dengan _Kernel Density Plot_ (untuk visualisasi kepadatan frekuensi distribusi data).

Keempat kategori ini (Comparison, Composition, Relationship, Distribution) berhubungan erat dengan konsep ukuran pemusatan dan penyebaran data di [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]] — kategori **Distribution** khususnya adalah representasi visual langsung dari _measures of spread_ dan bentuk distribusi (skewness, normal, dsb) yang dibahas di sana.

---

## Bab 2 Perkakas (Tools) untuk Visualisasi Data

### 2.1 Pustaka (Library) Visualisasi Data di Python

#### A. Karakteristik Library Python

| Library | Basis / Ketergantungan | Fungsi & Karakteristik Utama |
|:--|:--|:--|
| **Matplotlib** | Mandiri | Library komprehensif untuk membuat visualisasi statis, animasi, dan interaktif di Python. Berfungsi sebagai pondasi dasar bagi library visualisasi lainnya. |
| **Seaborn** | Matplotlib | Library visualisasi data berbasis Matplotlib yang menyediakan high-level interface untuk menggambar grafik statistik yang menarik (_attractive_) dan informatif. |
| **Pandas** | Python murni (Numpy) | Tool analisis dan manipulasi data open-source yang cepat, bertenaga, fleksibel, serta mudah digunakan. Memiliki fungsi plotting dasar bawaan untuk visualisasi cepat langsung dari objek DataFrame. |
| **Plotly** | Mandiri | Library khusus untuk membuat visualisasi data yang bersifat interaktif. |

> [!tip] Audio Insight — Matplotlib vs Seaborn vs Pandas plotting
> - **Matplotlib**: Meskipun sangat bertenaga dan fleksibel untuk membuat kanvas visualisasi, Matplotlib membutuhkan penulisan baris kode yang relatif lebih panjang dan detail untuk mengonfigurasi komponen visualisasi dibanding Seaborn.
> - **Seaborn**: Seaborn dikembangkan langsung di atas Matplotlib (analogi seperti Pandas yang dikembangkan di atas Numpy — lihat [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]]). Antarmuka Seaborn jauh lebih atraktif dan informatif secara visual karena memiliki opsi tema bawaan. Penggunaannya sangat disukai oleh para analis karena sintaks kodenya jauh lebih singkat dan tidak membutuhkan banyak variabel tambahan yang rumit.
> - **Pandas**: Pustaka ini utamanya digunakan untuk analisis dan manipulasi data (_data analysis and manipulation_), namun dilengkapi dengan metode plotting cepat (seperti `.hist()` atau `.boxplot()`) untuk keperluan eksplorasi data instan tanpa harus memanggil library visualisasi eksternal terlebih dahulu.

---

### 2.2 Lingkungan Kerja Interaktif (Interactive Python Notebook)

#### A. Penggunaan File IPYNB

- Proyek visualisasi data dalam modul ini tidak menggunakan file Python biasa (`.py`), melainkan menggunakan format **IPYNB** (_Interactive Python Notebook_).
- File IPYNB berjalan menggunakan ekstensi **Jupyter** yang harus diaktifkan terlebih dahulu di editor kode (seperti VS Code).
- Keunggulan utama IPYNB adalah kemampuannya untuk mengeksekusi blok kode (_code cell_) secara terpisah dan langsung menampilkan hasil keluaran (_code output_) di bawah sel tersebut, sehingga sangat cocok untuk proses eksplorasi data (_explore data_).

> [!warning] Audio Insight — Kernel harus dipilih, sel harus runut dari atas
> - **Pengaturan Kernel**: Untuk menjalankan file IPYNB, pengguna harus menentukan **Kernel** yang tepat di bagian kanan atas editor. Kernel ini menentukan lingkungan Python (_Python Environment_) yang akan digunakan. Dalam sesi kuliah ini, mahasiswa diarahkan untuk memilih virtual environment khusus yang telah dibuat sebelumnya (bernama "Purwadika").
> - **Instalasi Library**: Jika library seperti Matplotlib atau Seaborn belum terinstal di dalam environment aktif, instalasi dapat dilakukan langsung melalui terminal dengan mengaktifkan virtual environment "Purwadika" terlebih dahulu, kemudian menjalankan perintah berikut:
>
> ```
> pip install seaborn matplotlib
> ```
>
> - **Aturan Eksekusi Sel**: Pengguna tidak boleh mengeksekusi blok kode secara acak (_out of order_). Misalnya, mencoba mengeksekusi sel di bagian bawah yang memanggil variabel tertentu (seperti variabel `tips`) sebelum sel atas yang mendefinisikan variabel tersebut dijalankan akan memicu kegagalan runtime atau error variabel tidak ditemukan (_key error_ / _name error_). Sel harus dijalankan secara runut dari atas ke bawah.

---

### 2.3 Perangkat Lunak Business Intelligence (BI) dan Pembuatan Dashboard

#### A. Perkakas BI Populer

| Kategori Perkakas | Contoh Perangkat Lunak | Fungsi Utama di Industri |
|:--|:--|:--|
| **Business Intelligence (BI)** | Power BI, Tableau, Microstrategy, Qlik | Digunakan untuk menyusun dasbor interaktif berskala perusahaan yang terhubung langsung ke sumber data bisnis untuk mendukung pengambilan keputusan. |

> [!tip] Audio Insight — Python untuk eksplorasi, BI untuk dashboard final
> Alat-alat BI seperti Power BI dan Tableau sangat populer di dunia bisnis karena memudahkan pembuatan laporan interaktif tanpa harus menulis baris kode pemrograman visualisasi yang rumit dari awal. Penggunaannya melengkapi visualisasi Python; Python biasanya digunakan oleh analis atau engineer di tahap eksplorasi awal (_exploratory data analysis_) dan persiapan model, sementara perkakas BI digunakan untuk menyajikan dasbor final yang interaktif ke pengambil keputusan tingkat tinggi (_manager_ atau _VP_).

---

## Bab 3 Tipe-Tipe Visualisasi Data & Implementasi Kode Python

Bab ini membahas secara mendalam berbagai jenis grafik visualisasi data yang umum digunakan di industri, karakteristik unik masing-masing grafik, panduan kapan menggunakannya atau menghindarinya, serta implementasi praktis sintaks kode pemrogramannya menggunakan bahasa Python melalui tiga library utama: **Matplotlib**, **Seaborn**, dan **Pandas**.

---

### 3.1 Histogram

#### A. Definisi dan Kegunaan

- **Histogram** adalah grafik distribusi frekuensi yang digunakan untuk menampilkan sebaran data numerik tunggal secara kontinu.
- Grafik ini membagi nilai numerik ke dalam interval-interval tertentu yang disebut **bins** (atau tempat penyimpanan data).
- Tinggi dari setiap batang merepresentasikan frekuensi atau jumlah observasi data yang jatuh ke dalam interval bins tersebut.

#### B. Perbedaan Utama Histogram vs Bar Chart

- Histogram digunakan khusus untuk merepresentasikan sebaran data numerik dari variabel kontinu, di mana setiap batang saling bersebelahan secara fisik tanpa jeda ruang guna menekankan kontinuitas data.
- _Bar Chart_ digunakan untuk membandingkan kelompok kategori diskrit (seperti data nominal atau ordinal), di mana terdapat jeda jarak antar batang untuk menunjukkan batas antar kategori yang terpisah.

#### C. Implementasi Python

```python
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

> [!tip] Audio Insight — `kde=True` dan cara memilih jumlah bins
> Dosen menekankan bahwa parameter **kde** (Kernel Density Estimation) bernilai `True` pada library Seaborn sangat berguna untuk menggambarkan garis perkiraan mulus sebaran data (_density curve_) di atas batang histogram.
> Mengatur ukuran **bins** yang pas sangat penting. Jika bins terlalu sedikit, pola sebaran tidak terlihat; jika bins terlalu banyak, grafik akan tampak berantakan karena terlalu detail. Bentuk-bentuk sebaran yang bisa dibaca dari histogram (symmetric, right-skewed, left-skewed, bimodal, uniform) dibahas tuntas dengan contoh industri di [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]] Lampiran.

---

### 3.2 Box Plot

#### A. Definisi dan Kegunaan

- **Box Plot** (atau _Box-and-Whisker Plot_) adalah visualisasi grafis untuk menyajikan ringkasan statistik deskriptif lima angka dari kumpulan data numerik.
- Lima angka statistik ringkasan tersebut adalah:
    1. **Minimum**: Batas nilai terkecil bukan pencilan (ditandai oleh ujung garis bawah/_whisker_).
    2. **First Quartile (Q1 / Kuartil Bawah)**: Batas bawah kotak yang menandakan persentil ke-25 dari data.
    3. **Median (Q2 / Kuartil Tengah)**: Garis horizontal di dalam kotak yang menandai nilai tengah atau persentil ke-50.
    4. **Third Quartile (Q3 / Kuartil Atas)**: Batas atas kotak yang menandakan persentil ke-75 dari data.
    5. **Maximum**: Batas nilai terbesar bukan pencilan (ditandai oleh ujung garis atas/_whisker_).
- Jarak antara Q1 dan Q3 disebut **Interquartile Range (IQR)**. Batas garis _whisker_ bawah dihitung dengan rumus `Q1 - 1.5 * IQR` dan batas atas dihitung dengan `Q3 + 1.5 * IQR`. Lihat [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]] Bab 4.4 untuk penjelasan lengkap kenapa `1.5 * IQR` adalah aturan TERPISAH dari IQR itu sendiri.
- Nilai data yang berada di luar batas garis _whisker_ didefinisikan secara matematis sebagai **outliers** (pencilan) dan digambarkan dalam bentuk titik atau berlian terpisah di luar grafik kotak.

#### B. Membaca Skewness (Kemiringan Distribusi Data)

Analisis kemiringan distribusi (_skewness_) sebaran data dapat dibaca langsung dari Box Plot berdasarkan posisi garis median terhadap kotak IQR:

| Posisi Garis Median | Karakteristik Skewness | Interpretasi Distribusi Data |
|:--|:--|:--|
| **Garis median berada tepat di tengah-tengah kotak** | Distribusi Simetris (_Normal Distribution_) | Sebaran data merata dan seimbang di sekitar nilai tengah. |
| **Garis median lebih dekat ke bagian bawah kotak (Q1)** | Kemiringan Positif (_Right-Skewed_) | Ekor sebaran data memanjang ke arah kanan (nilai besar), mayoritas data terkonsentrasi di nilai rendah. |
| **Garis median lebih dekat ke bagian atas kotak (Q3)** | Kemiringan Negatif (_Left-Skewed_) | Ekor sebaran data memanjang ke arah kiri (nilai kecil), mayoritas data terkonsentrasi di nilai tinggi. |

#### Fokus Klarifikasi: kenapa "median dekat Q1" = right-skewed (bukan sebaliknya)

Ini poin yang paling sering terasa berlawanan dengan intuisi. Berikut jalur penalarannya langkah demi langkah, memakai analogi yang sama dengan [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]] Bab 4.2 (gaji karyawan vs direktur):

**Langkah 1 — Ingat dulu siapa yang "menumpuk" dan siapa yang jadi "ekor".**
Bayangkan 9 karyawan reguler bergaji 7-9 juta, dan 1 direktur bergaji 100 juta.
- Mayoritas data (9 karyawan) **menumpuk rapat di nilai RENDAH**.
- Satu nilai ekstrem (direktur) **menarik EKOR ke arah nilai TINGGI (kanan)**.
- Inilah definisi **right-skewed**: ekornya panjang ke kanan.

**Langkah 2 — Sekarang pikirkan di mana Q1, median, dan Q3 jatuh pada kondisi ini.**
Karena mayoritas data (karyawan) menumpuk padat di nilai rendah, maka:
- Q1 (persentil 25) dan **median (persentil 50) sama-sama jatuh di ZONA PADAT nilai rendah** — mereka berdekatan satu sama lain, karena banyak data terjejal di sana.
- Q3 (persentil 75) harus "melompat jauh" ke nilai yang jauh lebih tinggi untuk mencakup wilayah yang jarang berisi data (termasuk ekor panjang menuju si direktur).

**Langkah 3 — Bandingkan jarak median ke Q1 vs jarak median ke Q3.**
Karena median dan Q1 sama-sama berada di zona padat (berdekatan), sedangkan Q3 harus melompat jauh ke zona jarang (outlier), maka **jarak median↔Q1 jadi PENDEK**, sementara **jarak median↔Q3 jadi PANJANG**. Secara visual, ini membuat median terlihat "lebih dekat ke Q1" di dalam kotak.

**Kesimpulan**: median dekat Q1 bukan karena "mayoritas data ada di Q1" secara langsung — tapi karena mayoritas data yang PADAT membuat Q1 DAN median berdekatan, sementara ekor panjang ke kanan (nilai besar yang jarang) mendorong Q3 menjauh. Yang menentukan arah skew adalah **ke mana arah ekor memanjang**, bukan "di mana mayoritas data berada" secara terpisah dari posisi median.

**Aturan hafalan singkat**: **"Ekor panjang ke kanan → median terdorong mendekat ke Q1 (kiri kotak) → RIGHT-skewed."** Sebaliknya, **"Ekor panjang ke kiri → median terdorong mendekat ke Q3 (kanan kotak) → LEFT-skewed."** Nama "right/left-skewed" mengikuti ke mana **ekornya** mengarah, bukan ke mana mediannya bergeser.

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
# 9 "karyawan" bergaji rendah dan padat + 1 "direktur" bergaji ekstrem tinggi
gaji_karyawan = np.random.normal(loc=8, scale=0.7, size=90)      # menumpuk di 7-9 juta
gaji_direktur = np.array([100] * 10)                                # outlier ekstrem tinggi
gaji_tim = np.concatenate([gaji_karyawan, gaji_direktur])

q1 = np.percentile(gaji_tim, 25)
median = np.percentile(gaji_tim, 50)
q3 = np.percentile(gaji_tim, 75)

print(f"Q1={q1:.2f} | Median={median:.2f} | Q3={q3:.2f}")
print(f"Jarak Median-Q1: {median - q1:.2f}  (pendek, karena sama-sama di zona padat)")
print(f"Jarak Q3-Median: {q3 - median:.2f}  (panjang, karena Q3 melompat ke arah ekor)")
# Median jauh lebih dekat ke Q1 dibanding ke Q3 -> RIGHT-SKEWED, sesuai prediksi

plt.boxplot(gaji_tim, vert=False)
plt.title("Box Plot Gaji Tim: Right-Skewed (median dekat Q1)")
plt.xlabel("Gaji (juta rupiah)")
plt.show()
```

#### C. Implementasi Python

```python
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

> [!tip] Audio Insight — Box Plot vs Seaborn untuk perbandingan antar kategori
> Box Plot sangat efisien dalam mendeteksi keberadaan _outliers_ secara visual. Menggunakan Seaborn memberikan fleksibilitas tinggi karena analis dapat langsung membandingkan sebaran data numerik di sumbu Y (misalnya harga tiket/_Fare_) terhadap variabel kategori di sumbu X (misalnya status keselamatan penumpang/_Survived_).

---

### 3.3 Violin Plot

#### A. Definisi dan Kegunaan

- **Violin Plot** adalah tipe visualisasi kombo yang secara teknis menggabungkan seluruh elemen statistik pada Box Plot dengan representasi kepadatan frekuensi sebaran data dari **Kernel Density Plot**.
- Bentuk lekukan luar mirip biola menggambarkan pola kerapatan data (_density estimate_); semakin lebar penampang lekukannya, semakin banyak data yang terkonsentrasi pada tingkat nilai tersebut.

#### B. Cara Membaca Violin Plot

- Bagian tengah violin memuat struktur Box Plot mini: terdapat titik putih kecil sebagai penanda nilai median, kotak hitam tebal sebagai rentang IQR (Q1 hingga Q3), serta garis vertikal tipis sebagai _whisker_.
- Bentuk sisi kiri dan kanan violin yang simetris menunjukkan kepadatan distribusi variabel di setiap titik nilai kuantitatifnya.

> [!tip] Audio Insight — Violin Plot usia penumpang Titanic
> Dosen mengilustrasikan contoh kasus membaca Violin Plot pada variabel usia penumpang Titanic berdasarkan keselamatan. Penumpang yang bertahan hidup (_Survived_) memiliki bentuk violin yang melebar di area usia 40 tahun ke bawah (menandakan mayoritas median yang selamat berumur muda). Sebaliknya, kelompok penumpang yang meninggal memiliki konsentrasi visual yang lebih tinggi di rentang usia 40 tahun ke atas.

**Contoh kode — Violin Plot dengan Seaborn (belum ada di sumber, ditambahkan agar lengkap):**

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.violinplot(data=df, x='Survived', y='Age')
plt.title("Sebaran Usia Penumpang Titanic Berdasarkan Status Keselamatan")
plt.show()
```

---

### 3.4 Line Plot

#### A. Definisi dan Kegunaan

- **Line Plot** adalah grafik garis yang menampilkan runtunan informasi sebagai rangkaian titik data yang dihubungkan secara kontinu oleh segmen garis lurus.
- Grafik ini sangat ideal untuk melacak perkembangan, perubahan, atau tren data kontinu seiring waktu (sering disebut sebagai **time series data**).

#### B. Alasan Menghindari Bar Plot untuk Tren Waktu

- Penggunaan grafik batang (_bar chart_) untuk melacak tren waktu yang sangat panjang tidak disarankan karena batang mengimplikasikan kategori diskrit yang terputus-putus.
- Grafik garis (_line plot_) lebih unggul karena secara visual menonjolkan aliran kontinuitas, laju naik-turunnya tren, serta memudahkan penarikan pola musiman dari waktu ke waktu.

#### C. Implementasi Python

```python
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

> [!tip] Audio Insight — Line Plot untuk data harian rentang panjang
> Bila rentang data waktu memiliki tingkat kerapatan (_granularity_) yang sangat tinggi, misalnya data harian dari tahun 2019 sampai 2020, grafik garis adalah satu-satunya opsi terbaik untuk menyajikan pergerakan fluktuasi tanpa membuat visualisasi menjadi berantakan.

---

### 3.5 Scatter Plot

#### A. Definisi dan Kegunaan

- **Scatter Plot** (atau diagram pencar) adalah grafik yang memplot titik-titik data individual pada koordinat kartesian dua dimensi (Sumbu X dan Sumbu Y).
- Visualisasi ini digunakan untuk mengidentifikasi arah korelasi, kekuatan hubungan, ketergantungan, atau pola interaksi antara dua buah variabel numerik kontinu.
- Sangat sering diaplikasikan dalam analisis awal _Machine Learning_ untuk mendeteksi linearitas regresi, pengelompokan (_clustering_), serta deteksi pencilan sebaran data.

#### B. Kapan Harus Dihindari

- Scatter Plot mutlak tidak bisa digunakan apabila kumpulan data hanya memiliki satu dimensi variabel kuantitatif, karena grafik ini secara teknis memerlukan koordinat pasangan sumbu X dan Y untuk memplot titik koordinat data.

#### C. Implementasi Python

```python
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

> [!tip] Audio Insight — Korelasi positif dan dimensi tambahan hue/style
> Korelasi positif digambarkan dengan titik-titik data yang bergerak naik dari kiri bawah ke kanan atas (contoh hubungan peningkatan tagihan terhadap besaran uang tip di restoran). Kustomisasi parameter **hue** dan **style** di Seaborn sangat berguna untuk menambahkan dimensi informasi ketiga dan keempat (seperti jenis kelamin dan keselamatan) langsung ke dalam plot titik koordinat.

---

### 3.6 Bar Plot / Bar Chart

#### A. Definisi dan Kegunaan

- **Bar Plot** adalah grafik batang yang menyajikan nilai variabel kuantitatif untuk setiap kelompok data kategorikal menggunakan panjang batang yang proporsional.
- Grafik ini sangat ideal untuk membandingkan perbedaan kuantitas, ukuran, atau frekuensi kemunculan nilai diskrit lintas kategori nominal atau ordinal.

#### B. Implementasi Python

```python
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

> [!tip] Audio Insight — Estimator default Seaborn adalah mean
> Secara bawaan (_default_), library Seaborn menggunakan estimator nilai rata-rata (_mean_). Penggunaan parameter **estimator** yang diatur ke nilai `np.median` atau fungsi statistik lain sangat membantu jika data mengandung bias ekstrem. Ini persis konsep fungsi agregasi pada `.groupby()` di [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] dan `GROUP BY` di [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] — Bar Plot pada dasarnya adalah "visualisasi dari hasil agregasi per kategori".

---

### 3.7 Pie Chart

#### A. Definisi dan Kegunaan

- **Pie Chart** (diagram lingkaran) adalah grafik lingkaran yang dibagi menjadi beberapa irisan (_slices_) untuk memvisualisasikan proporsi bagian terhadap keseluruhan nilai total (_parts of a whole_).
- Besar sudut dan luas irisan berbanding lurus dengan nilai persentase kontribusi masing-masing kategori.

#### B. Panduan Kapan Harus Dihindari

Penggunaan Pie Chart sangat dilarang pada kondisi analisis berikut:

- **Analisis Fluktuasi Waktu**: Tidak boleh digunakan untuk menunjukkan perkembangan nilai dari waktu ke waktu karena bentuknya statis.
- **Kategori Terlalu Banyak**: Jika kategori data melebihi 5 grup, irisan lingkaran akan menjadi sangat sempit sehingga sulit dibaca.
- **Nilai Antar Kategori Sangat Berdekatan**: Otak manusia kesulitan membedakan perbedaan ukuran sudut atau luas lingkaran jika nilainya hampir mirip (misalnya membedakan sudut persentase 24% vs 26% secara visual tanpa bantuan label angka).

#### C. Implementasi Python

```python
# Menggunakan Matplotlib
import matplotlib.pyplot as plt
plt.pie(df['Tips'], labels=df['Day'], autopct='%1.1f%%', explode=(0, 0.1, 0, 0))
plt.axis('equal')
plt.show()

# Menggunakan Pandas
df.plot.pie(y='Tips', labels=df['Day'], autopct='%1.2f%%')
plt.show()
```

> [!tip] Audio Insight — Parameter `explode` dan `autopct`
> Dosen merekomendasikan penambahan parameter **explode** untuk memisahkan atau menonjolkan irisan kategori tertentu agar keluar sedikit dari lingkaran utama. Menambahkan parameter `autopct` sangat krusial guna menampilkan label teks persentase nilai kuantitatif secara eksplisit di atas masing-masing irisan diagram.

---

### 3.8 Heatmap

#### A. Definisi dan Kegunaan

- **Heatmap** adalah peta visualisasi data dua dimensi dalam format tabel kisi (matriks) kompleks yang menggunakan kode warna (_color coding_) untuk mempresentasikan nilai ukuran numeriknya.
- Representasi nilai numerik digambarkan lewat gradasi atau intensitas warna; warna yang lebih pekat atau mencolok merepresentasikan nilai korelasi atau angka kuantitatif yang lebih kuat/tinggi.

#### B. Aturan Pembacaan dan Skala Warna

- Heatmap korelasi menyajikan variabel data sebagai baris dan kolom tabel. Sumbu diagonal tengah biasanya bernilai `1.0` karena mengukur korelasi variabel terhadap dirinya sendiri.
- Interpretasi warna dilakukan menggunakan bar legenda visual di samping kanan diagram:
    - **Skala Monokromatik**: Gradasi satu warna dari terang ke gelap.
    - **Skala Divergen**: Menggunakan dua spektrum warna berlawanan (misalnya merah untuk korelasi negatif kuat, kuning untuk netral, dan hijau untuk korelasi positif kuat).

#### C. Implementasi Python

```python
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

> [!tip] Audio Insight — Parameter `annot` dan `cmap`
> Pada library Seaborn, menambahkan parameter **annot** bernilai `True` sangat penting untuk menampilkan nilai numerik koefisien korelasi asli secara presisi di dalam setiap kotak warna. Parameter **cmap** (seperti `'coolwarm'` atau `'RdYlGn'`) membantu analis mengatur peta palet warna grafik agar ramah bagi mata pembaca dan mudah diinterpretasikan.

---

### 3.9 Tipe Visualisasi Tambahan

#### A. Sankey Diagrams

- Berguna untuk memvisualisasikan aliran (_flow_) serta hubungan kuantitas numerik antar beberapa entitas atau variabel dalam satu sistem terintegrasi.
- Umumnya diaplikasikan untuk pemetaan alur proses rekayasa sistem (_process engineering_), perjalanan konversi pengguna digital, atau analisis distribusi aliran energi.

#### B. Treemaps

- Visualisasi efisien untuk menampilkan struktur data hierarkis secara bertingkat.
- Grafik ini memecah kategori-kategori utama ke dalam bentuk kotak persegi panjang bersarang (_nested rectangles_).
- Luas ukuran kotak persegi panjang mencerminkan porsi kontribusi nilai kuantitatif aslinya terhadap total keseluruhan.
- _Contoh Kasus_: Pemetaan pendapatan produk (_Product Revenue_) di mana kategori besar (minuman/_Beverages_) dibagi lagi ke dalam beberapa sub-kotak persegi panjang kecil di dalamnya (kopi, teh, dan minuman rasa khusus).

#### C. Word Clouds

- Representasi visual interaktif untuk menyajikan data teks tak terstruktur.
- Ukuran fisik dari setiap kata pada grafik digambarkan berbanding lurus dengan tingkat frekuensi kemunculan kata tersebut di dalam dataset dokumen teks asli.

#### D. Bubble Plot

- Pengembangan dari Scatter Plot dua dimensi.
- Memungkinkan analisis hubungan antar tiga buah variabel numerik sekaligus, di mana sumbu X menentukan posisi horizontal, sumbu Y menentukan posisi vertikal, dan variabel ketiga direpresentasikan oleh ukuran volume fisik dari lingkaran (_bubble_) titik data tersebut.

#### E. Stacked Charts

- **Stacked Bar Chart**: Menggambarkan proporsi relatif atau nilai absolut dari komponen pembentuk kategori seiring waktu pada periode yang relatif singkat (_Few Periods_).
- **Stacked Area Chart**: Sangat efisien untuk melacak kontribusi kumulatif dari beberapa variabel seiring perkembangan waktu yang sangat panjang (_Many Periods_).

**Contoh kode — Bubble Plot dan Stacked Bar Chart (belum ada di sumber, ditambahkan agar lengkap):**

```python
import matplotlib.pyplot as plt
import pandas as pd

# Bubble Plot: sumbu X, Y, dan ukuran bubble (variabel ketiga)
df_bubble = pd.DataFrame({
    'total_bill': [20, 35, 15, 50],
    'tip': [3, 5, 2, 8],
    'size': [2, 4, 1, 6]   # jumlah orang -> jadi ukuran bubble
})
plt.scatter(df_bubble['total_bill'], df_bubble['tip'], s=df_bubble['size'] * 50, alpha=0.5)
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Bubble Plot: Total Bill vs Tip (ukuran = jumlah orang)")
plt.show()

# Stacked Bar Chart sederhana dengan Pandas
df_stacked = pd.DataFrame({
    'Tahun': [2022, 2023, 2024],
    'Produk_A': [30, 40, 35],
    'Produk_B': [20, 25, 45]
}).set_index('Tahun')
df_stacked.plot(kind='bar', stacked=True)
plt.title("Stacked Bar Chart: Kontribusi Produk A vs B per Tahun")
plt.show()
```

---

## Bab 4 Kesalahan Umum dalam Visualisasi Data (Common Pitfalls)

### 4.1 Pemilihan Jenis Grafik yang Salah (Choosing the Wrong Chart Type)

#### A. Line Plot vs. Bar Plot pada Data Kategori dan Waktu

- **Line Plot** secara teknis dirancang khusus untuk menggambarkan kontinuitas dan perkembangan variabel dari waktu ke waktu (_time series data_). Grafik ini memperjelas tren kenaikan atau penurunan secara berkesinambungan.
- **Bar Plot** digunakan untuk menampilkan perbandingan nilai antar kategori diskrit (_discrete categories_). Penggunaan grafik batang memberikan penekanan visual pada perbedaan kuantitas mutlak antar kelompok yang terpisah.
- Memvisualisasikan data kategori diskrit menggunakan _Line Plot_ adalah kesalahan mendasar karena garis kontinu secara keliru menyiratkan adanya hubungan sekuensial atau alur waktu antar kategori tersebut.

> [!warning] Audio Insight — Bar Plot masih boleh untuk periode sangat sedikit
> Dosen menegaskan bahwa untuk data runtun waktu yang memiliki periode sangat sedikit (misalnya evaluasi tahunan dengan hanya 2 atau 3 titik waktu), penggunaan _Bar Plot_ masih diperbolehkan dan tidak dianggap salah sepenuhnya karena keterbatasan titik kontinuitasnya. Namun, jika data tidak memiliki elemen waktu sama sekali (misalnya perbandingan GDP antar negara pada satu tahun yang sama), penggunaan _Line Plot_ dilarang keras karena akan menyesatkan penafsiran pembaca seolah-olah ada perkembangan dari satu negara ke negara lain.

#### B. Kasus Menghindari Bar Plot (When to Avoid Bar Plot)

- Grafik batang tunggal tidak ideal digunakan ketika analis memiliki beberapa variabel yang secara kolektif merupakan bagian dari satu kesatuan utuh (_parts of a whole_).
- Contoh Kasus: Data penjualan buku fiksi (_Fiction Book Sales_) yang terbagi menjadi lima kategori terpisah (seperti _Young adult, Classics, Mystery, Romance,_ dan _Sci-fi_). Karena kelima kategori tersebut mencakup seluruh pangsa pasar buku fiksi, jumlah akumulasi nilainya merepresentasikan volume total pasar fiksi (100%).
- Jika data ini dipaksakan menggunakan grafik batang biasa lintas tahun, pembaca harus melakukan perhitungan matematika manual secara mandiri untuk memahami kontribusi masing-masing kategori terhadap total volume penjualan dari tahun ke waktu.

> [!warning] Audio Insight — Visualisasi yang memaksa audiens berhitung sendiri = gagal
> Dosen menekankan bahwa jika visualisasi memaksa audiens melakukan perhitungan matematika sendiri untuk menarik kesimpulan dasar, maka visualisasi tersebut gagal. Dalam kondisi tersebut, menyajikan data dalam bentuk tabel mentah yang terstruktur jauh lebih baik daripada membuat grafik yang membingungkan. Solusi teknis untuk kasus akumulasi bagian dari keseluruhan ini adalah menggunakan _Stacked Bar Chart_ (untuk membandingkan nilai absolut komponen) atau _100% Stacked Bar Chart_ (untuk membandingkan kontribusi persentase komponen seiring waktu).

#### C. Kasus Menghindari Pie Chart (When to Avoid Pie Chart)

- **Pie Chart** dilarang keras digunakan dalam analisis yang bertujuan untuk menunjukkan perkembangan atau perubahan nilai suatu variabel dari waktu ke waktu (_over time_).
- **Pie Chart** akan menjadi sangat menyesatkan (_misleading_) apabila analis sengaja atau tidak sengaja menghilangkan sebagian kategori data sehingga total persentase komponen di dalam lingkaran tidak mencapai 100% nilai sebenarnya.

> [!warning] Audio Insight — Pie Chart dengan kategori hilang = manipulasi data
> Dosen memberikan contoh kasus riil pada tingkat manajemen puncak (_top management_): Jika sebuah perusahaan mengoperasikan tiga divisi terpisah, penggunaan _Pie Chart_ hanya boleh dilakukan untuk membandingkan kontribusi pendapatan dari ketiga divisi tersebut secara lengkap sehingga membentuk akumulasi 100%. Jika analis hanya memasukkan data pendapatan dari dua divisi saja ke dalam _Pie Chart_, visualisasi tersebut dikategorikan sebagai manipulasi informasi karena basis pembagian 100% lingkaran telah bergeser secara tidak sah dan memberikan representasi proporsi yang salah.
> Banyak ahli visualisasi merekomendasikan untuk menghindari _Pie Chart_ secara umum karena mata manusia secara alami lebih sulit membandingkan ukuran luas sudut lingkaran (_angle_) dibanding membandingkan tinggi batang linier. Alternatif terbaik pengganti _Pie Chart_ adalah _Bar Chart_, _Box Plot_, atau _Dot Plot_.

---

### 4.2 Kepadatan Informasi yang Berlebihan (Overloading with Information)

#### A. Kompleksitas Visual Berlebih pada Plot tunggal

- Memasukkan terlalu banyak komponen visual seperti garis (_lines_), penanda titik (_markers_), legenda, teks, dan elemen dekoratif tambahan (_clutter_) ke dalam satu area grafik akan mengaburkan pola sebaran data asli.
- Kondisi ini dikenal sebagai _Overloading Info_ yang mengakibatkan beban kognitif berlebih bagi audiens (_overwhelming the viewer_) sehingga tujuan penyampaian wawasan utama gagal dicapai.

> [!warning] Audio Insight — Marker berlebih dan kombinasi hue+style yang membingungkan
> Dosen mencontohkan sebuah grafik tren penjualan produk di mana satu garis tunggal diberi penanda (_marker_) yang berbeda-beda untuk setiap titiknya (misalnya titik berwarna biru bulat, titik orange kotak, dan titik ungu silang). Penambahan variasi bentuk _marker_ ini dinilai tidak berguna (_useless_) dan merusak kerapian visual (_decluttering_) karena perbedaan warna garis saja sebenarnya sudah sangat memadai untuk membedakan kategori produk tersebut.
> Contoh kesalahan fatal lainnya adalah memaksa memasukkan seluruh dimensi variabel ke dalam satu grafik scatter plot menggunakan kombinasi warna (_color_) dan bentuk penanda (_style_) sekaligus. Misalnya, memetakan variabel hari dengan warna berbeda dan waktu makan (_lunch_/_dinner_) dengan bentuk bulat dan silang. Grafik kombo ini menjadi terlalu padat, sangat membingungkan untuk dibaca, dan menyulitkan analis untuk menarik wawasan yang bermakna.

---

### 4.3 Skala dan Sumbu yang Tidak Konsisten (Inconsistent Scales and Axes)

#### A. Distorsi Analisis Akibat Penyatuan Skala Berbeda

- Plotting dua atau lebih dataset yang memiliki rentang nilai kuantitatif (_scale_) yang berbeda sangat jauh pada sumbu Y (_Y-axis_) yang sama akan menyembunyikan hubungan (_obscure relationships_) dan tren riil data tersebut.
- Dataset yang memiliki nilai numerik kecil akan tertekan ke bagian bawah grafik dan tampak stagnan tanpa fluktuasi, sementara dataset berangka besar akan mendominasi visualisasi.

> [!warning] Audio Insight — Solusi: sumbu Y sekunder (secondary axis)
> Dosen memaparkan contoh kasus konkrit di mana analis mencoba menggambarkan hubungan antara data Penjualan Bulanan (_Monthly Sales_ dalam satuan dolar yang bernilai ratusan hingga ribuan) dan data Suhu Rata-rata (_Average Temperature_ dalam derajat Celsius yang bernilai kecil antara 20 hingga 40) pada satu grafik sumbu Y yang sama.
> Akibat penyatuan sumbu Y ini, kurva _Average Temperature_ tampak berupa garis lurus horizontal yang flat di dekat angka 0 karena skalanya terdistorsi oleh angka penjualan bulanan yang mencapai ratusan dolar.
> Solusi teknis mutlak untuk mengatasi masalah ini adalah dengan menerapkan sumbu sekunder (_secondary axis_). Sumbu Y sebelah kiri dikonfigurasi khusus untuk skala Penjualan Bulanan (_Monthly Sales_), sedangkan sumbu Y sebelah kanan (_secondary Y-axis_) dikonfigurasi untuk skala Suhu Rata-rata (_Average Temperature_). Dengan demikian, kedua pola fluktuasi data dapat ter-render secara proporsional dan korelasinya dapat dianalisis dengan akurat.

**Contoh kode — implementasi secondary Y-axis di Matplotlib (belum ada di sumber, ditambahkan agar lengkap):**

```python
import matplotlib.pyplot as plt

bulan = ['Jan', 'Feb', 'Mar', 'Apr']
penjualan = [500, 800, 650, 900]        # dalam ratusan dolar
suhu = [28, 30, 27, 32]                  # dalam derajat Celsius

fig, ax1 = plt.subplots()

ax1.set_xlabel('Bulan')
ax1.set_ylabel('Penjualan ($)', color='tab:blue')
ax1.plot(bulan, penjualan, color='tab:blue', marker='o')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()  # buat sumbu Y kedua yang berbagi sumbu X yang sama
ax2.set_ylabel('Suhu (°C)', color='tab:red')
ax2.plot(bulan, suhu, color='tab:red', marker='s')
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title("Penjualan vs Suhu (dengan Secondary Y-Axis)")
fig.tight_layout()
plt.show()
```

---

### 4.4 Penggunaan Warna yang Menyesatkan (Misleading Use of Colors)

#### A. Inkonsistensi Identitas Warna Lintas Grafik

- Penggunaan warna yang tidak konsisten untuk merepresentasikan kategori data yang sama di beberapa grafik berbeda dalam satu presentasi akan membingungkan audiens.
- Otak audiens secara otomatis membangun asosiasi bahwa satu warna tertentu mewakili satu entitas tetap. Ketika asosiasi warna ini diacak pada grafik berikutnya, audiens akan salah menginterpretasikan korelasi antar data.

> [!warning] Audio Insight — Konsistensi warna kategori A di semua grafik
> Dosen mencontohkan kasus pembuatan dua grafik batang berdampingan yang menyajikan perbandingan kinerja kategori produk yang sama (misalnya Kategori A, B, C, dan D). Pada grafik pertama (Dataset 1), Kategori A digambarkan dengan batang berwarna merah muda (_pink_). Namun pada grafik kedua (Dataset 2) di slide atau halaman yang sama, Kategori A digambarkan dengan batang berwarna hijau.
> Inkonsistensi warna ini dinilai merusak logika penyampaian pesan. Solusi perbaikannya adalah menerapkan palet warna yang seragam lintas grafik: jika Kategori A diwarnai merah muda di grafik pertama, maka Kategori A wajib diwarnai merah muda di seluruh grafik berikutnya dalam dokumen tersebut.

---

### 4.5 Ringkasan Karakteristik Pitfalls Visualisasi Data

| Jenis Pitfall | Deskripsi Singkat Kesalahan | Dampak pada Audiens | Solusi Teknis Perbaikan |
|:--|:--|:--|:--|
| **Wrong Chart Type** | Menggunakan _Line Plot_ untuk kategori non-waktu, atau _Pie Chart_ untuk tren runtun waktu. | Salah menafsirkan adanya kontinuitas atau hubungan sekuensial yang sebenarnya tidak ada. | Gunakan _Bar Plot_ untuk kategori terpisah; _Line Plot_ hanya untuk dimensi waktu kontinu. |
| **Information Overloading** | Menambahkan terlalu banyak garis, warna, dan bentuk _markers_ berbeda dalam satu plot tunggal. | Mengalami beban kognitif tinggi (_overwhelming_) dan pola data penting menjadi tersembunyi. | Terapkan _decluttering_; batasi pemakaian _markers_ jika warna saja sudah cukup membedakan. |
| **Inconsistent Scales** | Memplot dua variabel berskala beda jauh (misal: suhu vs. dolar) pada sumbu Y yang sama. | Grafik variabel berskala kecil tampak flat dan kehilangan visualisasi pola fluktuasinya. | Konfigurasikan sumbu sekunder (_secondary Y-axis_) di sisi kanan grafik untuk variabel kedua. |
| **Misleading Colors** | Menggunakan warna berbeda untuk satu kategori yang sama di grafik yang berbeda. | Membingungkan asosiasi visual audiens dan merusak konsistensi hubungan data. | Terapkan palet warna yang seragam lintas grafik untuk kategori yang identik. |
| **Incomplete Category Pie** | Membuat _Pie Chart_ dengan sengaja mengeliminasi salah satu divisi/kategori penting. | Proporsi total persen (100%) bergeser sehingga menghasilkan representasi persentase yang palsu. | Wajib menyertakan seluruh kategori pembentuk totalitas (100%) di dalam lingkaran. |

---

## Bab 5 Sesi Praktik & Evaluasi Pembelajaran

### 5.1 Latihan Praktis Menggunakan Dataset Titanic

#### A. Deskripsi Tugas Analisis Data dan Grafik

Latihan praktis menggunakan dataset Titanic dirancang untuk menguji kemampuan pengolahan, manipulasi, serta visualisasi data secara langsung menggunakan Python. Latihan ini memanfaatkan library Pandas untuk manipulasi data (lihat [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]]), serta Matplotlib dan Seaborn untuk pembuatan grafik. Terdapat lima tugas visualisasi utama yang harus diselesaikan oleh peserta:

- **Tugas 1 (Bar Plot - Survivor Comparison)**: Membandingkan jumlah penumpang yang selamat (survivor) dengan penumpang yang tidak selamat menggunakan Bar Plot. Analisis ini ditujukan untuk melihat kelompok mana yang memiliki frekuensi penumpang lebih banyak.
- **Tugas 2 (Histogram - Age Distribution)**: Memvisualisasikan sebaran atau distribusi usia (age) dari seluruh penumpang Titanic menggunakan Histogram untuk mengamati karakteristik demografis penumpang.
- **Tugas 3 (Box Plot - Fare Distribution)**: Membandingkan sebaran nilai tarif (fare) antara kelompok penumpang yang selamat dan yang tidak selamat menggunakan Box Plot. Tujuan tugas ini adalah menganalisis nilai median tarif serta mengidentifikasi keberadaan pencilan (outliers).
- **Tugas 4 (Scatter Plot - Age vs Fare)**: Memvisualisasikan hubungan dua dimensi antara variabel usia (age) dan tarif perjalanan (fare) menggunakan Scatter Plot untuk mengamati ada tidaknya pola korelasi atau sebaran tertentu.
- **Tugas 5 (Correlation Heatmap - Numerical Variables)**: Membuat Heatmap korelasi untuk seluruh variabel kuantitatif (numerik) di dalam dataset Titanic untuk mengidentifikasi pasangan variabel mana yang memiliki kekuatan hubungan korelasi paling tinggi.

> [!tip] Audio Insight — Temuan riil dari pengerjaan latihan di kelas
> - **Tugas 1 (Bar Plot - Survivor Comparison)**: Berdasarkan proses pengerjaan latihan di kelas, penghitungan jumlah penumpang yang tidak selamat (label 0) dan yang selamat (label 1) dilakukan dengan menerapkan method `.value_counts()` pada kolom `survived`. Hasil perhitungan riil menunjukkan jumlah penumpang tidak selamat sebanyak 549 orang, sedangkan yang selamat sebanyak 342 orang.
>   Untuk mempermudah interpretasi bagi audiens non-teknis, indeks sumbu X (default bernilai 0 dan 1) sebaiknya ditimpa secara manual menggunakan list nama kategori baru seperti `['Not survive', 'Survive']` atau `['No', 'Yes']` agar grafik lebih komunikatif.
> - **Tugas 2 & 3 (Distribusi Usia dan Fare)**: Pembacaan sebaran grafik menunjukkan bahwa pada kelompok penumpang kelas dua (second class), penumpang anak-anak atau yang berusia sangat muda memiliki tingkat keselamatan yang tinggi. Box plot tarif membantu analis mendeteksi pencilan (outliers) berupa nilai tarif perjalanan ekstrem yang jauh melampaui rentang sebaran mayoritas penumpang.
> - **Tugas 5 (Correlation Heatmap)**: Untuk menghindari bias analisis, data kategorikal (non-numerik) harus disaring terlebih dahulu sebelum dimasukkan ke dalam perhitungan korelasi. Penyaringan dilakukan di Python menggunakan method `.select_dtypes(include='number')` pada data frame. Kolom `PassengerId` wajib dibuang menggunakan method `.drop(columns=['PassengerId'])`. Meskipun bertipe numerik, kolom ini secara esensi hanyalah nomor urut atau identifier unik penumpang. Jika diikutsertakan dalam matriks korelasi, data ini akan mendistorsi interpretasi kekuatan korelasi antar variabel analitik rill lainnya.

**Contoh kode — implementasi penuh kelima tugas di atas (disusun berdasarkan deskripsi tugas dan insight kelas):**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')  # dataset Titanic bawaan Seaborn (kolom huruf kecil, mis. 'survived', 'fare')

# Tugas 1: Bar Plot perbandingan survivor
jumlah_survived = df['survived'].value_counts()
plt.bar(['Not survive', 'Survive'], jumlah_survived.sort_index())
plt.title("Jumlah Penumpang: Survive vs Not Survive")
plt.ylabel("Jumlah Penumpang")
plt.show()
# Hasil riil di kelas: 549 tidak selamat, 342 selamat

# Tugas 2: Histogram distribusi usia
sns.histplot(df['age'].dropna(), bins=20, kde=True)
plt.title("Distribusi Usia Penumpang Titanic")
plt.xlabel("Usia")
plt.show()

# Tugas 3: Box Plot tarif berdasarkan status selamat
sns.boxplot(data=df, x='survived', y='fare')
plt.title("Distribusi Fare: Survived vs Not Survived")
plt.show()

# Tugas 4: Scatter Plot usia vs tarif
sns.scatterplot(data=df, x='age', y='fare', hue='survived')
plt.title("Hubungan Usia dan Tarif Tiket")
plt.show()

# Tugas 5: Correlation Heatmap (hanya kolom numerik, buang PassengerId jika ada)
df_numerik = df.select_dtypes(include='number')
if 'PassengerId' in df_numerik.columns:
    df_numerik = df_numerik.drop(columns=['PassengerId'])
correlation_matrix = df_numerik.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap - Variabel Numerik Titanic")
plt.show()
```

---

### 5.2 Metode Evaluasi Akhir

#### A. Komponen Penilaian Akhir

Sistem evaluasi kelulusan pada akhir modul pembelajaran ini terdiri atas dua instrumen utama:

1. **Ujian Tertulis (Exam)**: Berupa ujian pilihan ganda (_multiple choice_) yang bertujuan untuk menguji tingkat pemahaman teoritis siswa mengenai prinsip visualisasi, anatomi grafik, serta fungsionalitas perkakas visualisasi data.
2. **Tantangan Pemrograman (Code Challenge)**: Berupa ujian praktis mandiri untuk melatih logika pemrograman, kemampuan algoritma, serta penyelesaian masalah (_problem solving_) menggunakan platform online.

#### B. Aturan dan Komposisi Code Challenge LeetCode

| Tingkat Kesulitan Soal | Jumlah Soal | Bobot Nilai per Soal | Total Nilai Maksimal |
|:--|:--|:--|:--|
| **Easy** | 3 Soal | 20 Poin | 60 Poin |
| **Medium** | 1 Soal | 40 Poin | 40 Poin |

> [!tip] Audio Insight — Aturan submission dan kejujuran akademik
> - **Mekanisme Bukti Pengerjaan (Submission)**: Pengerjaan soal dilakukan menggunakan akun LeetCode pribadi masing-masing peserta. Siswa wajib menyerahkan dua bukti pengerjaan fisik untuk divalidasi oleh tim pengajar:
>     1. **Tautan Profil (Profile Link)**: URL lengkap menuju halaman profil akun LeetCode siswa.
>     2. **Tangkapan Layar (Screenshot)**: Gambar tangkapan layar yang memuat informasi nama soal, status pengerjaan yang sukses (**Accepted**), serta nama akun siswa yang bersangkutan secara jelas.
>     - Poin penilaian hanya akan dihitung apabila melampirkan kedua bukti di atas secara lengkap.
> - **Kebijakan Kejujuran Akademik**: Seluruh tugas tantangan pemrograman wajib diselesaikan secara mandiri. Segala bentuk indikasi plagiarisme, kerja sama tidak sah, atau menyalin solusi murid lain akan ditindak tegas dan memengaruhi penilaian kelulusan.
> - **Manajemen Waktu**: Seluruh dokumen bukti harus diunggah melalui formulir pengumpulan resmi sebelum modul pembelajaran berakhir. Keterlambatan pengumpulan akan mengikuti aturan penalti waktu yang dikelola oleh tim operations.

---

## Lampiran: Catatan Mentah Tambahan dari Sesi (Raw Session Notes)

Bagian ini berisi catatan kelas versi ringkas/mentah yang melengkapi Bab 1-5 di atas, termasuk satu gambar Box Plot hasil tangkapan layar dari kelas.

### Ringkasan Definisi Cepat

- **Data visualization**: presentasi data dalam _pictorial_ dan _graphical format_.
- **Mengapa penting**:
    1. Mengkomunikasikan data menjadi gambar.
    2. Mengeksplorasi kemungkinan visualisasi data yang paling cocok.
    3. Mengeksplorasi insight dari data yang terbantu oleh visual.
    4. Melihat pola yang tidak terlihat di tabel mentah.
- **Cara melakukan visualisasi data**:
    1. Memahami dulu konteks data.
    2. Buat pertanyaan berdasarkan data.
    3. Pilih jenis grafik dan identifikasi pesannya.
    4. Aspek teknis: title, sumbu X/Y, label, mark data points, memainkan warna.
    5. Berikan konklusi.
    6. Empat tipe visualisasi: Comparison, Composition, Relationship, Distribution.

### Catatan Cepat per Jenis Grafik

- **Heatmap**: Melihat korelasi data melalui _color code_.
- **Word Clouds**: Melihat kata-kata apa yang paling sering muncul, memakai rasio ukuran.
- **Sankey**: Melihat _flow_ (aliran).
- **Seaborn**: Visualisasi data berbasis Matplotlib yang menyediakan _high level interface_.
- **Box Plot**:

> [!tip] Gambar tangkapan layar Box Plot dari kelas
> Sumber materi menyertakan gambar tangkapan layar berikut sebagai contoh visual Box Plot yang dibahas langsung di kelas: `![[Pasted image 20260826201856.png]]`. Referensi gambar ini dipertahankan apa adanya dari catatan asli — jika file gambar tersebut belum ada di folder attachment vault Obsidian kamu, embed ini akan tampil rusak/kosong sampai file aslinya ditambahkan secara manual.

- **Line Plot**: Untuk tipe data yang memiliki _time series_, agar bisa melihat tren.
    - Kapan pakai ini? Ketika variabel tunggal maupun banyak (_single dan multiple variable_) diplot dengan dimensi waktunya.
- **Scatter Plot**: Variabel harus numerik. Digunakan untuk melihat _relationship_ antar variabel.
    - Kapan menghindari ini? Ketika tidak memiliki data dua dimensi (_bi-dimensional data_). Tidak cocok untuk mengobservasi pola waktu.
- **Bar Plot**: Chart untuk menunjukkan data kategorikal; tingginya menunjukkan value.
    - Kapan hindari ini? Jika ada banyak bagian yang merupakan bagian dari suatu kesatuan (_parts of a whole_) — lihat Bab 4.1.B untuk penjelasan lengkapnya.
- **Pie Chart**: Digunakan untuk menunjukkan proporsi bagian dari keseluruhan — lihat Bab 3.7 dan Bab 4.1.C untuk kapan sebaiknya dihindari.
- **Jebakan umum (Common Pitfalls) — ringkasan cepat**:
    1. Memilih tipe grafik yang salah.
    2. Informasi yang terlalu banyak (overloading).
    3. Skala dan sumbu (scales & axis) yang tidak konsisten.
    4. Menggunakan warna yang menyesatkan (_misleading_).

---

## Ringkasan Kilat Sesi (Cheat Sheet)

| Kebutuhan Analisis | Grafik yang Tepat |
|:--|:--|
| Bandingkan sedikit kategori | Bar Chart |
| Bandingkan tren waktu (banyak periode) | Line Chart |
| Bagian dari keseluruhan (few periods) | Stacked Bar Chart / Pie Chart (hati-hati batasannya) |
| Hubungan 2 variabel numerik | Scatter Plot |
| Hubungan 3 variabel numerik | Bubble Plot |
| Sebaran 1 variabel numerik | Histogram / Box Plot |
| Korelasi banyak variabel numerik sekaligus | Heatmap |
| Median dekat Q1 di Box Plot | Right-skewed (ekor ke kanan) |
| Median dekat Q3 di Box Plot | Left-skewed (ekor ke kiri) |

---

**Lihat juga:** [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]] (dasar statistik di balik Box Plot, IQR, skewness, dan empirical rule) · [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] (persiapan/manipulasi DataFrame sebelum divisualisasikan) · [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] (konsep agregasi `GROUP BY` yang mendasari Bar Chart hasil agregasi).
