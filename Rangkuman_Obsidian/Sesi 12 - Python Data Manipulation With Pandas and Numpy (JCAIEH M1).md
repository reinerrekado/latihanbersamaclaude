---
tags: [jcaieh/module1, sesi-12, numpy, pandas, dataframe, series, data-wrangling, broadcasting, groupby, merge, missing-values, file-io, jcaieh/module1/sesi12]
bootcamp: JCAIEH
module: 1
session: 12
aliases: ["Sesi 12", "Pandas and Numpy", "Data Manipulation"]
---

# Sesi 12 - Python Data Manipulation With Pandas and Numpy

> Sumber: rangkuman gabungan slide/PDF resmi + transkrip audio kelas (ditandai sebagai callout Audio Insight di bawah), dilengkapi contoh kode Python tambahan untuk setiap method/atribut yang disebutkan di modul tapi belum diberi contoh runnable.

---

## Bab I Pendahuluan Analisis Data (Introduction to Data Analysis)

### 1.1 Definisi dan Landasan Analisis Data

#### A. Konsep Dasar dan Definisi

- _Data Analysis_ adalah proses penemuan (discovery) dan penyampaian (communication) pola-pola yang bermakna (meaningful patterns) di dalam data.
- _Analytics_ didefinisikan sebagai scientific process untuk mentransformasikan data menjadi _insight_ guna mendukung pengambilan keputusan yang lebih baik.
- Bidang _analytics_ mengandalkan penerapan secara simultan dari beberapa disiplin ilmu, yaitu:
    - _Statistics_ (Statistika) — lihat [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]].
    - _Computer programming_ (Pemrograman Komputer).
    - _Operations research_ (Riset Operasi).

#### B. Tujuan dan Peran Visualisasi Data

- Tujuan utama dari _Data Analysis_ adalah memperoleh _actionable insights_ yang dapat menghasilkan keputusan yang lebih cerdas (smarter decisions) serta hasil bisnis yang lebih baik (better business outcomes).
- Dalam menyampaikan temuan atau wawasan (_insights_), proses _Data Analysis_ sangat mengutamakan penggunaan _data visualization_ agar informasi tersebut lebih mudah dipahami dan dikomunikasikan secara efektif — lihat [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]].

> [!tip] Audio Insight — Masalahnya bukan kurang data, tapi kelebihan data
> Dosen menjelaskan bahwa di era modern ini, tantangan utama organisasi bukanlah ketiadaan data, melainkan melimpahnya data yang dimiliki tanpa adanya kemampuan untuk memanfaatkannya secara optimal (_too much data and unable to utilize it_). Hal inilah yang mendorong tingginya permintaan terhadap peran-peran seperti _data analyst_ dan _data scientist_ dalam beberapa tahun terakhir. Dosen menekankan bahwa jika hasil analisis data tidak dapat dipahami oleh pengambil keputusan, maka data tersebut tidak akan berguna. Oleh karena itu, _data visualization_ menjadi metode krusial untuk menjembatani wawasan teknis dengan keputusan strategis.

---

### 1.2 Bahasa Pemrograman Python dalam Analisis Data (Why Python?)

#### A. Karakteristik Python sebagai Alat Analisis

- Python merupakan bahasa pemrograman yang bersifat _open source_ (bebas digunakan tanpa biaya lisensi), _interpreted_, _high level language_, dan mendukung pendekatan _object-oriented programming_ yang sangat baik (lihat [[Sesi 07 - Object Oriented Programming (JCAIEH M1)|Sesi 07 - Object Oriented Programming]]).
- Kemudahan penggunaan (_ease of use_) dan sintaksis yang sederhana (_simple syntax_) menjadikan Python mudah diadaptasi oleh individu yang tidak memiliki latar belakang pemrograman (_coding background_).
- Python menyediakan fungsionalitas dan pustaka lengkap untuk menangani perhitungan matematika (_mathematics_), statistik (_statistics_), dan fungsi ilmiah (_scientific functions_) yang dibutuhkan dalam aplikasi _data science_.

#### B. Relevansi Industri

- Python diakui sebagai salah satu bahasa pemrograman terbaik yang digunakan secara luas oleh para _data scientist_ untuk berbagai proyek dan aplikasi _data science_.

> [!tip] Audio Insight — Python sangat mendekati bahasa manusia
> Dosen memaparkan bahwa sifat Python sebagai _high-level language_ membuatnya sangat mendekati bahasa manusia, sehingga kodenya jauh lebih intuitif untuk dipahami oleh pemula sekalipun. Relevansi penggunaan Python dalam analisis data ini sangat sejalan dengan kurikulum dan kompetensi yang dipelajari peserta didik dalam program _bootcamp_ saat ini.

---

### 1.3 Library Utama Analisis Data (NumPy & Pandas Overview)

#### A. NumPy (Numerical Python)

- NumPy adalah library Python yang menyediakan fungsi matematika berkinerja tinggi untuk menangani _large dimension array_.
- Library ini menyediakan fitur komputasi untuk operasi _n-arrays_ dan matriks (matrices) di Python.
- Keunggulan utama NumPy adalah kemampuan _vectorization_ pada operasi matematika terhadap tipe array NumPy, yang meningkatkan performa dan mempercepat waktu eksekusi program.
- NumPy mempermudah pengerjaan dengan array dan matriks multidimensi berskala besar.

#### B. Pandas

- Pandas adalah library Python yang sangat populer dan dirancang untuk manipulasi dan analisis data terstruktur.
- Pandas menyediakan metode termudah untuk melakukan analisis data, manipulasi, agregasi, serta visualisasi terhadap data terstruktur dalam jumlah besar.
- Pandas merupakan alat yang sangat ideal untuk proses _data wrangling_.
- Pandas memiliki dua struktur data utama, yaitu:
    1. _Series_: Digunakan untuk menangani dan menyimpan data satu dimensi (one-dimensional data).
    2. _DataFrame_: Digunakan untuk menangani dan menyimpan data dua dimensi (two-dimensional data).

> [!tip] Audio Insight — NumPy vs `math`, dan hubungan NumPy-Pandas
> - **Perbandingan NumPy dengan Library Math Standar bawaan Python**: Dosen menjelaskan bahwa meskipun Python memiliki library bawaan bernama `math`, library tersebut tidak dirancang untuk menangani struktur data _array_ atau matriks berdimensi tinggi. NumPy hadir khusus untuk memproses operasi matematika pada array berdimensi besar (_higher dimension arrays_) dengan performa yang sangat cepat.
> - **Struktur Array dalam NumPy**: Dosen memberikan analogi bahwa array satu dimensi (1D array) mirip dengan struktur List horizontal di Python, sedangkan array dua dimensi (2D array) analog dengan struktur _list of list_. NumPy bahkan mampu mendukung komputasi hingga array 10 dimensi. Ini adalah "versi upgrade" dari struktur List/Dict yang sudah dipelajari di [[Sesi 04 - Data Types Collection Notes (JCAIEH M1)|Sesi 04 - Data Types Collection Notes]].
> - **Relevansi NumPy dalam AI dan Machine Learning**: Di dalam pengembangan AI atau _machine learning_, seluruh nilai data disimpan di dalam struktur array. Nilai-nilai tersebut tidak disimpan menggunakan tipe data Python List standar karena proses perhitungannya yang lambat. Sebagai solusinya, data tersebut dibungkus dalam tipe data NumPy Array guna mempercepat proses pelatihan model (_training process_).
> - **Hubungan Integrasi NumPy dan Pandas**: Dosen menjelaskan bahwa saat melakukan instalasi Pandas (misalnya melalui instruksi instalasi pustaka), sistem secara otomatis juga menginstal NumPy. Hal ini dikarenakan _under the hood_ (di bawah kap mesinnya), Pandas dibangun di atas NumPy dan menggunakan library NumPy untuk merepresentasikan serta menyimpan objek _Series_ dan _DataFrame_. Integrasi tingkat rendah ini yang membuat pemrosesan data di Pandas menjadi sangat cepat.
> - **Perbedaan Series dan DataFrame**: Secara sederhana, Dosen menjelaskan bahwa _DataFrame_ berbentuk tabel (dua dimensi), sedangkan _Series_ hanya terdiri dari satu kolom saja (satu dimensi).

> [!tip] Upgrade path dari List/Dict Python murni
> Kalau di [[Sesi 04 - Data Types Collection Notes (JCAIEH M1)|Sesi 04 - Data Types Collection Notes]] kamu belajar `list` dan `dict` sebagai wadah data serbaguna, anggap NumPy Array dan Pandas Series/DataFrame sebagai "versi profesional"-nya khusus untuk data numerik/tabular: jauh lebih cepat, mendukung operasi matematis langsung per elemen (`+`, `-`, `*`, `/` tanpa loop manual), dan punya method analisis siap pakai (`.mean()`, `.sort_values()`, dll).

#### C. Tabel Istilah Teknis dan Karakteristik

| Istilah Teknis / Library | Karakteristik dan Deskripsi Utama |
|:--|:--|
| _Data Analysis_ | Proses penemuan (discovery) dan komunikasi pola bermakna di dalam data untuk pengambilan keputusan berbasis bukti. |
| _Actionable Insights_ | Temuan atau wawasan dari data yang dapat langsung diimplementasikan menjadi tindakan bisnis yang strategis. |
| _Data Visualization_ | Metode penyampaian temuan analisis secara visual agar lebih mudah dipahami oleh pengambil keputusan. |
| _Data Wrangling_ | Proses pembersihan, penataan, dan manipulasi data terstruktur agar siap dianalisis lebih lanjut. |
| _NumPy Array_ | Tipe data terstruktur yang menyimpan nilai homogen (tipe data sama), bersifat mutable, berindeks mulai dari 0, dan mendukung dimensi n-D. |
| _Series_ | Struktur data satu dimensi (1D) pada Pandas yang mendukung indeks berlabel (axis labels) dan objek Python arbitrer. |
| _DataFrame_ | Struktur data dua dimensi (2D) pada Pandas berbentuk tabel yang terdiri dari kumpulan objek Series yang berbagi indeks yang sama. |

### 1.4 Panduan Instalasi dan Impor Library

#### A. Instruksi Instalasi

Kedua library ini merupakan _external packages_, sehingga harus diinstal terlebih dahulu menggunakan package manager seperti `pip` atau `conda`.

```
pip install numpy
pip install pandas
```

#### B. Instruksi Impor Library

```python
import numpy as np
import pandas as pd
```

> [!tip] Audio Insight — Alias `np`/`pd` adalah konvensi, bukan aturan wajib
> Dosen menjelaskan bahwa penamaan alias seperti `np` untuk NumPy dan `pd` untuk Pandas bukanlah aturan mutlak bahasa pemrograman, melainkan sebuah konvensi atau kesepakatan bersama (_convention_) di kalangan data scientist untuk mempermudah penulisan kode. Programmer bebas menggunakan alias lain seperti `npy` atau bahkan tidak menggunakan alias sama sekali, namun sangat direkomendasikan mengikuti konvensi industri ini.
> Dosen juga menyarankan agar proses instalasi pustaka eksternal ini dilakukan di dalam lingkungan virtual (_virtual environment_) yang terisolasi (seperti Anaconda Environment) untuk menghindari konflik versi antar proyek.

---

## Bab II Pemrograman NumPy (Numerical Python) Array

### 2.1 Pengenalan Array (Introduction to Array)

#### A. Fondasi Konseptual

- _Array_ adalah tipe data terstruktur yang menyimpan beberapa nilai dengan tipe data yang sama (homogen).
- Karakteristik utama dari array adalah:
    - Bersifat _mutable_ (nilainya dapat diubah setelah didefinisikan).
    - Menggunakan sistem indeks berbasis nol (_zero-based indexing_) yang dimulai dari angka 0.
    - Dapat berbentuk satu dimensi (1D), dua dimensi (2D/Matriks), tiga dimensi (3D), hingga banyak dimensi (nD).

> [!tip] Audio Insight — Array 1D = List, Array 2D = List of List
> Dosen menjelaskan bahwa struktur array satu dimensi (1D) secara visual analog dengan List horizontal dasar di Python, sedangkan array dua dimensi (2D) analog dengan struktur _list of list_. Untuk komputasi tingkat tinggi, NumPy mampu mendukung representasi data hingga 10 dimensi.

---

### 2.2 Kelebihan NumPy Array (Advantages of NumPy Array)

#### A. Performa dan Efisiensi Memori

- Kecepatan eksekusi NumPy Array mencapai hingga 50 kali lebih cepat dibandingkan dengan Python List standar.
- Sangat efisien dalam alokasi memori dan pengelolaan sumber daya komputasi, menjadikannya pilihan utama untuk pemrosesan data berskala besar (_large-scale data_).

> [!tip] Audio Insight — Mengapa AI/ML wajib pakai array, bukan List
> Dosen menekankan bahwa dalam pengembangan Kecerdasan Buatan (AI) dan _Machine Learning_, seluruh data wajib disimpan dalam bentuk array. Nilai-nilai data ini tidak disimpan menggunakan tipe data Python List standar karena proses perhitungan matematika pada List standar sangat lambat. Dosen menyajikan contoh kasus pengujian komputasi (_time execution_) di mana operasi penjumlahan vektor menggunakan NumPy Array terbukti berjalan puluhan kali lipat lebih cepat dibandingkan perulangan (_looping_) pada Python List biasa. Oleh karena itu, penggunaan NumPy Array adalah mutlak di bidang data science di mana kecepatan (_speed_) dan optimalisasi sumber daya (_resource optimization_) menjadi prioritas.

**Contoh kode — pembuktian kecepatan NumPy vs List biasa:**

```python
import numpy as np
import time

ukuran = 1_000_000
list_python = list(range(ukuran))
array_numpy = np.arange(ukuran)

# Operasi: kalikan setiap elemen dengan 2
awal = time.time()
hasil_list = [x * 2 for x in list_python]
waktu_list = time.time() - awal

awal = time.time()
hasil_array = array_numpy * 2   # vectorization, tanpa loop manual
waktu_array = time.time() - awal

print(f"Python List : {waktu_list:.5f} detik")
print(f"NumPy Array : {waktu_array:.5f} detik")   # jauh lebih cepat
```

---

### 2.3 Cara Instalasi dan Pemakaian (Installation and Usage)

#### A. Prosedur Teknis

- Karena NumPy merupakan library eksternal (_external package_), pengguna harus menginstalnya terlebih dahulu menggunakan package manager seperti `pip` atau `conda`.
- Impor pustaka di dalam script Python dilakukan menggunakan alias standar konvensional untuk menyingkat penulisan kode.

> [!tip] Audio Insight — Gunakan virtual environment
> Dosen merekomendasikan agar proses instalasi pustaka ini dilakukan di dalam lingkungan virtual (_virtual environment_) yang terisolasi (seperti Anaconda Environment) untuk menghindari konflik versi antar proyek pemrograman yang berbeda.

---

### 2.4 Pembuatan Array (Array Creation)

#### A. Metode Konversi Objek Python

- NumPy Array dapat dibuat dengan mengonversi objek Python List (untuk array 1D) atau _List of List_ (untuk matriks/array 2D atau 3D) menggunakan fungsi `np.array()`.

#### B. Metode Pembuatan Otomatis (Built-in Functions)

- `np.arange()`: Membuat array dengan jangkauan nilai tertentu dari batas awal (_start_) hingga sebelum batas akhir (_stop_) dengan parameter langkah (_step_) tertentu.
- `np.zeros()`: Membuat array berisi angka 0 (mendukung dimensi 1D maupun multidimensi dengan parameter tuple bentuk).
- `np.ones()`: Membuat array berisi angka 1.
- `np.eye()`: Membuat matriks identitas (matriks persegi diagonal di mana nilai diagonal utamanya adalah 1 dan elemen lainnya adalah 0).
- `np.linspace()` (_linear space_): Membuat array dengan membagi interval angka tertentu menjadi beberapa elemen dengan jarak yang sama besar.

#### C. Metode Pembuatan Acak (np.random Module)

- `np.random.rand()`: Membuat array berisi angka desimal acak (_float_) dengan distribusi seragam (_uniform distribution_) di dalam interval [0, 1).
- `np.random.randn()`: Membuat array berisi angka acak berdasarkan distribusi normal standar (_normally distributed_ dengan mean = 0 dan standar deviasi = 1). Lihat [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]] Bab 5 untuk konsep distribusi normalnya.
- `np.random.randint()`: Membuat array berisi bilangan bulat acak (_integer_) dengan menentukan batas minimum, batas maksimum (eksklusif), dan jumlah data yang diinginkan.

> [!warning] Audio Insight — `np.arange()` vs `np.linspace()`, matriks identitas, dan kenapa pakai `randint`
> Dosen menjelaskan perbedaan fungsional antara `np.arange()` dan `np.linspace()`. Fungsi `np.arange()` menerima parameter _step_ (selisih nilai antar elemen), sedangkan `np.linspace()` menerima parameter jumlah total elemen yang diinginkan (_count_), di mana NumPy secara otomatis menghitung selisih jarak yang sama (_equal space_) antar elemen tersebut. Sebagai contoh, jika memanggil `np.linspace(0, 10, 50)`, NumPy akan menghasilkan 50 angka acak dengan jarak yang sama persis dari 0 hingga 10.
> Dosen menjelaskan matriks identitas yang dihasilkan oleh `np.eye(4)` sebagai matriks 4x4 dengan angka 1 yang berbaris diagonal secara menyilang dari kiri atas ke kanan bawah, dan sisanya bernilai 0.
> Terkait modul acak, Dosen menyoroti pentingnya menggunakan `np.random.randint()` untuk menghasilkan bilangan bulat guna menghindari output berupa desimal panjang (_float_) yang dihasilkan oleh `np.random.rand()` atau `np.random.randn()`.

#### Fokus Klarifikasi: `np.arange()` vs `np.linspace()` — mana yang minta "jarak" dan mana yang minta "jumlah"?

Cara paling gampang mengingat perbedaannya: **`np.arange()` adalah versi NumPy dari fungsi bawaan Python `range()`** yang sudah kamu kenal — dan `range(start, stop, step)` selalu minta parameter ke-3 berupa **step** (langkah/jarak antar elemen). `np.arange()` mewarisi kebiasaan ini persis.

`np.linspace()` sebaliknya: namanya "linear SPACE", kamu memberi tahu NumPy **berapa BANYAK titik (count)** yang kamu inginkan, dan NumPy sendiri yang menghitung jarak antar titik supaya semuanya rata (linear).

| Fungsi | Parameter ke-3 | Apa yang KAMU tentukan | Apa yang DIHITUNG OTOMATIS oleh NumPy |
|:--|:--|:--|:--|
| `np.arange(start, stop, step)` | `step` (jarak) | Jarak antar elemen | Jumlah elemen yang dihasilkan |
| `np.linspace(start, stop, num)` | `num` (jumlah) | Jumlah elemen yang dihasilkan | Jarak antar elemen |

```python
import numpy as np

# np.arange(start, stop, STEP) -> kamu tentukan JARAK, jumlah elemen dihitung otomatis
a = np.arange(0, 10, 2)
print(a)          # [0 2 4 6 8]  -> jarak antar elemen = 2 (yang KITA tentukan)
print(len(a))      # 5  -> jumlah elemen ini DIHITUNG OTOMATIS oleh NumPy

# np.linspace(start, stop, COUNT) -> kamu tentukan JUMLAH ELEMEN, jarak dihitung otomatis
b = np.linspace(0, 10, 5)
print(b)          # [ 0.   2.5  5.   7.5 10. ]
print(len(b))      # 5  -> jumlah elemen ini KITA tentukan langsung
# jarak antar elemen (2.5) DIHITUNG OTOMATIS oleh NumPy agar merata dari 0 sampai 10

# Perhatikan juga: np.linspace() secara default MENYERTAKAN titik akhir (10 ikut muncul),
# sedangkan np.arange() TIDAK menyertakan titik stop (10 tidak muncul di hasil 'a').
```

**Contoh kode — array otomatis lainnya (`zeros`, `ones`, `eye`, `random`):**

```python
import numpy as np

nol = np.zeros((2, 3))          # matriks 2x3 berisi angka 0
satu = np.ones((3, 3))           # matriks 3x3 berisi angka 1
identitas = np.eye(4)            # matriks identitas 4x4 (diagonal 1, sisanya 0)

np.random.seed(0)
acak_uniform = np.random.rand(5)        # 5 angka desimal acak antara [0, 1)
acak_normal = np.random.randn(5)        # 5 angka acak dari distribusi normal standar (mean=0, std=1)
acak_integer = np.random.randint(1, 100, 5)  # 5 bilangan bulat acak antara 1 s.d. 99

print("Zeros:\n", nol)
print("Ones:\n", satu)
print("Identity:\n", identitas)
print("Random uniform:", acak_uniform)
print("Random normal:", acak_normal)
print("Random integer:", acak_integer)
```

---

### 2.5 Atribut dan Method NumPy Array (Attributes and Methods)

#### A. Atribut Struktural dan Tipe Data

- `.shape`: Mengembalikan dimensi dari array dalam format tuple (misalnya `(3,)` untuk array 1D berisi 3 elemen, atau `(3, 3)` untuk matriks 2D).
- `.reshape()`: Mengubah dimensi atau bentuk bentuk array (misalnya dari satu dimensi ke matriks dua dimensi) tanpa memodifikasi data aslinya.
- `.dtype`: Menunjukkan tipe data elemen dalam array beserta presisi memorinya (misalnya `int32` yang menggunakan memori 32 bits vs `int64` yang menggunakan 64 bits).

#### B. Method Statistik Nilai Ekstrem

- `.max()`: Mengembalikan nilai terbesar di dalam array.
- `.min()`: Mengembalikan nilai terkecil di dalam array.
- `.argmax()`: Mengembalikan posisi indeks dari nilai terbesar.
- `.argmin()`: Mengembalikan posisi indeks dari nilai terkecil.

> [!warning] Audio Insight — Aturan `.reshape(-1)` dan presisi data `int32`/`float64`
> - **Aturan Reshape -1**: Dosen membagikan teknik penting mengenai penggunaan nilai parameter `-1` pada method `.reshape()`. Jika kita memberikan parameter `-1` (seperti `.reshape(-1)`), NumPy akan meratakan (_flatten_) dimensi array dari bentuk apa pun (2D atau 3D) kembali menjadi array satu dimensi (1D) secara otomatis tanpa kita perlu menghitung secara manual jumlah elemennya.
> - **Konsep Presisi Data**: Dosen mencontohkan bahwa array yang berisi bilangan bulat acak default biasanya bertipe `int32` atau `int64` tergantung pada sistem operasinya, sedangkan array yang dibuat melalui pembagian interval seperti `np.linspace()` otomatis bertipe data desimal `float64`.

#### Fokus Klarifikasi: `.max()` vs `.argmax()` — nilainya atau posisinya?

Kuncinya ada di awalan **"arg"**, yang dalam konteks ini berarti **argument/posisi indeks**, bukan nilai itu sendiri:

- `.max()` menjawab pertanyaan **"berapa NILAI-nya?"**
- `.argmax()` menjawab pertanyaan **"di POSISI/INDEKS ke berapa nilai itu berada?"**

```python
import numpy as np

nilai_ujian = np.array([70, 85, 60, 95, 88])
#                idx:    0   1   2   3   4

print(nilai_ujian.max())     # 95   -> ini NILAI tertinggi itu sendiri
print(nilai_ujian.argmax())  # 3    -> ini POSISI/INDEKS tempat nilai 95 berada (indeks ke-3)

print(nilai_ujian.min())     # 60   -> NILAI terendah
print(nilai_ujian.argmin())  # 2    -> POSISI/INDEKS nilai 60 (indeks ke-2)

# Pembuktian: argmax() SELALU bisa dipakai untuk "menunjuk balik" ke nilai max()
print(nilai_ujian[nilai_ujian.argmax()])  # 95 -> identik dengan hasil .max()
```

Analogi: kalau `.max()` itu seperti menjawab "siapa yang menang lombanya?" (95 = nilainya), maka `.argmax()` itu seperti menjawab "peserta nomor urut berapa yang menang?" (indeks ke-3 = posisinya di barisan).

**Contoh kode — `.shape`, `.dtype`, `.reshape()` lengkap:**

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.shape)   # (6,) -> array 1D dengan 6 elemen
print(arr.dtype)    # int64 (atau int32 tergantung OS)

matrix = arr.reshape(2, 3)   # ubah jadi 2 baris, 3 kolom
print(matrix.shape)          # (2, 3)
print(matrix)
# [[1 2 3]
#  [4 5 6]]

flat_lagi = matrix.reshape(-1)  # -1 = "hitung otomatis", flatten kembali ke 1D
print(flat_lagi)                # [1 2 3 4 5 6]

arr_linspace = np.linspace(0, 1, 5)
print(arr_linspace.dtype)   # float64 -> hasil pembagian interval selalu desimal
```

---

### 2.6 Indexing dan Slicing pada NumPy Array

#### A. Pengambilan Elemen Tunggal

- Untuk array satu dimensi (1D), pengambilan elemen menggunakan kurung siku tunggal `[indeks]`.
- Untuk array dua dimensi (2D), pengambilan elemen dilakukan menggunakan koordinat baris dan kolom dengan format `[indeks_baris, indeks_kolom]`.

#### B. Pemotongan Array (_Slicing_)

- Pemotongan array menggunakan operator titik dua `:` dengan sintaksis `[start:stop:step]`.
- Aturan mutlak slicing di NumPy: **"A slice is a view, not a copy"**. Saat kita melakukan slicing pada suatu array dan menyimpan hasilnya ke variabel baru, variabel baru tersebut hanyalah sebuah pandangan (_view_) yang merujuk pada memori array aslinya. Jika nilai di dalam slice tersebut diubah, data pada array aslinya akan ikut berubah.
- Untuk menduplikasi data secara independen agar array asli tidak terpengaruh, kita wajib menggunakan method `.copy()` secara eksplisit.

#### C. _Fancy Indexing_

- Mengakses beberapa baris atau kolom spesifik secara non-berurutan dengan mengirimkan list indeks di dalam tanda kurung siku ganda `[[indeks1, indeks2, ...]]`.

> [!warning] Audio Insight — Bahaya modifikasi hasil slicing tanpa `.copy()`
> Dosen memperingatkan bahaya modifikasi data pada hasil slicing tanpa menyalinnya terlebih dahulu. Jika kita menuliskan `slice_of_arr[:] = 99`, maka seluruh elemen array asli pada rentang tersebut juga akan berubah menjadi 99 karena kedua variabel merujuk pada alamat memori yang sama (_by reference_). Solusinya adalah selalu menggunakan `arr.copy()` ketika ingin memanipulasi potongan data tanpa merusak data mentah asli.
> Dosen menunjukkan bahwa penulisan indeks 2D dapat dilakukan dengan dua cara: format tradisional `arr[baris][kolom]` atau format yang lebih bersih dan direkomendasikan (_cleaner format_) yaitu `arr[baris, kolom]`.

**Contoh kode — slicing, view vs copy, dan fancy indexing:**

```python
import numpy as np

# Inisialisasi array awal
arr = np.arange(0, 11)

# Slicing dan bahaya "View"
potongan_view = arr[0:6]
potongan_view[:] = 99  # Mengubah potongan akan mengubah array asli!
print(arr)  # array asli IKUT berubah -> [99 99 99 99 99 99  6  7  8  9 10]

# Menggunakan .copy() untuk keamanan data
arr_reset = np.arange(0, 11)
potongan_copy = arr_reset[0:6].copy()
potongan_copy[:] = 100  # Array asli (arr_reset) tetap aman tidak berubah
print(arr_reset)  # tetap [0 1 2 3 4 5 6 7 8 9 10]

# Filtering berdasarkan kriteria boolean (Masking)
arr_data = np.array([5, 12, 8, 21, 3, 15])
kondisi_filter = arr_data > 10  # Menghasilkan [False, True, False, True, False, True]
hasil_saring = arr_data[kondisi_filter]  # Menghasilkan [12, 21, 15]

# Indexing 2D: format tradisional vs format bersih yang direkomendasikan
matrix_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_2d[1][2])   # format tradisional -> 6
print(matrix_2d[1, 2])   # format bersih (direkomendasikan) -> 6, hasil sama

# Fancy Indexing: ambil baris ke-0 dan ke-2 sekaligus (non-berurutan)
print(matrix_2d[[0, 2]])
# [[1 2 3]
#  [7 8 9]]
```

---

### 2.7 Operasi Aritmatika & Broadcasting

#### A. Operasi Element-wise

- Seluruh operasi aritmatika standar (seperti `+`, `-`, `*`, `/`) pada NumPy Array dilakukan secara _element-wise_ (operasi diterapkan secara individual pada setiap elemen yang bersesuaian), bukan menggunakan aturan perkalian matriks aljabar linier standar.

#### B. Aturan Penyiaran (_Broadcasting Rules_)

- _Broadcasting_ adalah mekanisme otomatis di mana NumPy menangani operasi aritmatika antara dua array dengan bentuk (_shape_) yang berbeda. Array yang lebih kecil akan "diregangkan" secara virtual agar kompatibel dengan array yang lebih besar.
- Syarat kompatibilitas dimensi dinilai mulai dari sumbu paling kanan (_trailing rightmost axis_) bergerak ke arah kiri. Dua dimensi dinyatakan kompatibel jika:
    1. Ukuran dimensi pada sumbu tersebut sama besar, ATAU
    2. Salah satu dimensi pada sumbu tersebut bernilai tepat 1.

#### C. Fungsi Matematika NumPy (Universal Functions)

- `np.sqrt()`: Menghitung akar kuadrat dari setiap elemen.
- `np.exp()`: Menghitung eksponensial basis $e$ pangkat elemen ($e^x$).
- `np.sin()`: Menghitung nilai trigonometri sinus.
- `np.log()`: Menghitung logaritma natural (basis $e$).

#### D. Operator Perbandingan dan Filtering (Masking)

- Operator perbandingan (seperti `> arr`) akan menghasilkan array bertipe boolean (_True_ atau _False_) untuk setiap elemen. Array boolean ini dapat digunakan sebagai filter (mask) untuk menyaring elemen-elemen tertentu dari array asli.

> [!warning] Audio Insight — Kasus error broadcasting dan koreksi `np.exp()`
> Dosen memberikan contoh konkret kalkulasi _broadcasting_ antara array $A$ berukuran $4 \times 3$ dan array $B$ berukuran $1 \times 3$ (atau skalar tunggal). Array $B$ akan diregangkan secara virtual ke bawah untuk meniru baris-baris array $A$ sehingga operasi dapat dijalankan.
> Dosen memaparkan kasus eror _broadcasting_ yang sering dialami mahasiswa, misalnya melakukan operasi antara array $4 \times 3$ dan array berukuran $4$ (tanpa dimensi kedua). Sumbu paling kanan dari array pertama adalah 3, sedangkan sumbu paling kanan dari array kedua adalah 4. Karena nilainya tidak sama dan tidak ada yang bernilai 1, operasi tersebut akan memicu eror ketidakcocokan dimensi. Solusi untuk memperbaikinya adalah dengan melakukan _reshape_ pada array kedua menjadi $4 \times 1$ terlebih dahulu agar sumbu paling kanan bernilai 1, sehingga kompatibel untuk diregangkan secara virtual.
> Terkait fungsi `np.exp()`, Dosen meluruskan pemahaman mahasiswa bahwa rumus perhitungan eksponensial ini adalah menaikkan konstanta matematika $e$ (sekitar 2.718) ke pangkat nilai elemen array tersebut, bukan sebaliknya.

**Contoh kode — broadcasting yang benar vs yang error, dan Universal Functions:**

```python
import numpy as np

# Broadcasting yang BERHASIL: A (4x3) dengan B (1x3) -> B diregangkan ke bawah
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # shape (4, 3)
B = np.array([10, 20, 30])                                       # shape (3,) -> diperlakukan sebagai (1, 3)
print(A + B)
# setiap baris A ditambah [10, 20, 30]

# Broadcasting yang GAGAL: A (4x3) dengan C (4,) -> sumbu kanan tidak cocok (3 vs 4)
C = np.array([1, 2, 3, 4])  # shape (4,)
try:
    hasil_gagal = A + C
except ValueError as e:
    print("Error:", e)   # ValueError: operands could not be broadcast together

# SOLUSI: reshape C menjadi (4, 1) agar sumbu kanannya bernilai 1 (kompatibel)
C_reshaped = C.reshape(4, 1)  # shape (4, 1)
hasil_benar = A + C_reshaped   # sekarang berhasil, C diregangkan ke KANAN sepanjang kolom
print(hasil_benar)

# Universal Functions (element-wise)
angka = np.array([1, 4, 9, 16])
print(np.sqrt(angka))   # [1. 2. 3. 4.]
print(np.exp(np.array([0, 1, 2])))  # [1. 2.71828183 7.3890561] -> e^0, e^1, e^2 (BUKAN 0^e, dst)
print(np.log(np.array([1, np.e, np.e**2])))  # [0. 1. 2.] -> logaritma natural (basis e)

# Filtering/Masking
data = np.array([5, 12, 8, 21, 3, 15])
mask = data > 10
print(data[mask])   # [12 21 15]
```

---

### 2.8 Fungsi NumPy Tambahan (Additional NumPy Functions)

#### A. Manipulasi Struktur Array

- `np.where()`: Berfungsi untuk melakukan penyaringan berbasis kondisi dan mengganti elemen array secara kondisional. Formatnya adalah `np.where(kondisi, nilai_jika_benar, nilai_jika_salah)`.
- `np.insert()`: Menyisipkan elemen ke dalam array pada posisi indeks tertentu.
- `np.concatenate()`: Menggabungkan dua atau lebih array sepanjang sumbu (_axis_) yang ditentukan.
- `np.transpose()` atau atribut `.T`: Membalikkan dimensi array (baris menjadi kolom, dan sebaliknya).
- `np.flatten()`: Meratakan array multidimensi menjadi array satu dimensi (1D). _(catatan: ini sebenarnya method milik objek array — dipanggil sebagai `arr.flatten()`, bukan `np.flatten(arr)`)_.
- `np.stack()`: Menumpuk array sepanjang sumbu baru.
- `np.split()`: Membagi satu array menjadi beberapa sub-array kecil.

> [!tip] Audio Insight — `np.where()` untuk bersihkan data negatif, dan `.transpose()`
> Dosen menjelaskan kegunaan praktis `np.where()` untuk membersihkan data, misalnya mengganti seluruh nilai negatif dalam array dengan angka 0 tanpa merusak nilai positifnya.
> Dosen mendemonstrasikan bahwa melakukan operasi `.transpose()` pada matriks $2 \times 3$ akan mengubah bentuknya secara instan menjadi matriks $3 \times 2$ dengan memutar baris menjadi kolom.

**Contoh kode — seluruh fungsi manipulasi struktur array di atas:**

```python
import numpy as np

# np.where(): ganti nilai negatif jadi 0, biarkan nilai positif apa adanya
data = np.array([-5, 3, -2, 8, -1, 10])
data_bersih = np.where(data < 0, 0, data)
print(data_bersih)   # [0 3 0 8 0 10]

# np.insert(): sisipkan angka 99 pada indeks ke-2
arr = np.array([1, 2, 3, 4])
arr_sisip = np.insert(arr, 2, 99)
print(arr_sisip)   # [ 1  2 99  3  4]

# np.concatenate(): gabungkan dua array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate([a, b]))   # [1 2 3 4 5 6]

# np.transpose() / .T: putar baris jadi kolom
matrix = np.array([[1, 2, 3], [4, 5, 6]])   # shape (2, 3)
print(matrix.T)                              # shape (3, 2)
# [[1 4]
#  [2 5]
#  [3 6]]

# .flatten(): ratakan matriks multidimensi jadi 1D (method milik array)
print(matrix.flatten())   # [1 2 3 4 5 6]

# np.stack(): tumpuk beberapa array 1D menjadi satu array 2D baru
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.stack([x, y]))
# [[1 2 3]
#  [4 5 6]]

# np.split(): bagi satu array jadi beberapa sub-array sama besar
arr_besar = np.arange(9)
bagian = np.split(arr_besar, 3)
print(bagian)   # [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
```

### 2.9 Rangkuman Istilah Teknis dan Karakteristik

| Istilah Teknis / Library | Karakteristik dan Deskripsi Utama |
|:--|:--|
| _Vectorization_ | Penerapan operasi matematika secara simultan pada seluruh elemen array tanpa memerlukan perulangan (_loop_) manual. |
| _Broadcasting_ | Aturan otomatis NumPy untuk menyesuaikan dimensi array yang berbeda bentuk agar dapat dioperasikan secara aritmatika. |
| _Mutable_ | Sifat dari objek array yang memungkinkan pengubahan nilainya secara langsung di memori setelah objek tersebut didefinisikan. |
| _View_ | Representasi visual atau referensi potongan data (_slice_) yang merujuk langsung ke memori array asli, bukan salinan independen. |
| _Fancy Indexing_ | Teknik pemanggilan beberapa elemen spesifik pada indeks non-berurutan menggunakan kurung siku ganda. |
| _Universal Functions_ | Fungsi-fungsi matematika bawaan NumPy yang dioptimalkan untuk eksekusi cepat pada setiap elemen array (_element-wise_). |
| _Identity Matrix_ | Matriks diagonal khusus di mana seluruh elemen pada diagonal utama bernilai 1 dan elemen lainnya bernilai 0. |

### 2.10 Panduan Sintaksis dan Praktik Kode

#### A. Contoh Pembuatan dan Manipulasi Dasar Array

```python
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

#### B. Contoh Slicing, Copy, dan Filtering

```python
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

### 2.11 Tugas Latihan Kuliah (Exercises)

#### Latihan 1: Pembuatan Bordered Grid (Tepi Matriks)

```python
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

#### Latihan 2: Pembuatan Random Matrix & Reverse Rows

```python
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

---

## Bab III Pandas - DataFrame & Manipulasi Data

### 3.1 Pengenalan Pandas

#### A. Konsep Dasar Pandas

- Pandas adalah library tingkat tinggi (high-level data manipulation tool) yang dirancang untuk analisis dan manipulasi data terstruktur secara cepat dan efisien.
- Library ini dikembangkan oleh Wes McKinney dan dibangun di atas paket NumPy, yang menjadikannya sangat andal untuk melakukan manipulasi datatabular.
- Pandas merupakan alat utama yang sangat ideal untuk proses data wrangling (pembersihan, penataan, dan transformasi data mentah).

#### B. Struktur Data Utama: Series vs DataFrame

- **Series**: Struktur data satu dimensi (1D) yang serupa dengan array 1D pada NumPy, tetapi memiliki kelebihan berupa indeks berlabel (axis labels) dan mampu menyimpan tipe objek Python apa pun (tidak harus numerik).
- **DataFrame**: Struktur data dua dimensi (2D) berbentuk tabel yang terdiri dari baris dan kolom (seperti spreadsheet atau tabel database). DataFrame dapat dianalogikan sebagai kumpulan objek Series yang digabungkan bersama dan berbagi indeks yang sama.

> [!tip] Audio Insight — DataFrame adalah "workhorse" Pandas, terinspirasi dari R
> Dosen menekankan bahwa saat melakukan instalasi Pandas (melalui pip atau conda), sistem secara otomatis juga menginstal NumPy. Di bawah kap mesinnya (under the hood), Pandas menggunakan library NumPy untuk merepresentasikan dan menyimpan objek Series dan DataFrame. Integrasi tingkat rendah ini menjadi alasan mengapa pemrosesan data tabular menggunakan Pandas dapat berjalan dengan sangat cepat.
> Dosen juga memberikan penjelasan bahwa DataFrame merupakan workhorse (kuda beban) dari seluruh analisis data menggunakan Pandas, yang strukturnya terinspirasi langsung dari bahasa pemrograman R.

**Contoh kode — variasi cara membuat Series (list, dict, NumPy array):**

```python
import pandas as pd
import numpy as np

# Dari list biasa -> indeks default 0, 1, 2, ...
s1 = pd.Series([10, 20, 30])
print(s1)

# Dari dict -> KEY otomatis jadi INDEKS berlabel, VALUE jadi datanya
s2 = pd.Series({'a': 100, 'b': 200, 'c': 300})
print(s2)
# a    100
# b    200
# c    300

# Dari NumPy array, dengan indeks berlabel eksplisit
s3 = pd.Series(np.array([1.5, 2.5, 3.5]), index=['x', 'y', 'z'])
print(s3)
```

---

### 3.2 Pembuatan Pandas Series dan DataFrame

#### A. Cara Membuat Series

- Series dapat dibuat dari berbagai tipe objek Python seperti list, NumPy array, maupun dictionary menggunakan fungsi `pd.Series()`.
- Jika dibuat menggunakan dictionary, key pada dictionary tersebut otomatis akan menjadi indeks berlabel, dan value akan menjadi nilai datanya.

#### B. Cara Membuat DataFrame

- DataFrame dapat dikonstruksi dari list, list yang digabungkan menggunakan fungsi `zip()`, dictionary, atau NumPy Array 2D.
- Pembuatan DataFrame acak sering menggunakan generator data dari NumPy. Untuk memastikan hasil pengacakan data tetap konsisten ketika program dijalankan ulang, digunakan pengunci kode berupa nilai Seed (`np.random.seed()`).

> [!tip] Audio Insight — DataFrame acak 5x4 dengan indeks alfabet
> Dosen menunjukkan contoh implementasi kode pembuatan DataFrame acak berukuran 5 baris dan 4 kolom menggunakan data distribusi normal standar. Indeks baris didefinisikan secara eksplisit menggunakan karakter alfabet 'A', 'B', 'C', 'D', 'E' yang dipisahkan menggunakan metode `.split()`, begitu pula dengan indeks kolom 'W', 'X', 'Y', 'Z'.

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
```

**Contoh kode — cara lain membuat DataFrame (dari `zip()`, dict, dan array 2D NumPy):**

```python
import pandas as pd
import numpy as np

# Dari zip() -> pasangkan dua list jadi baris-baris tabel
nama = ['Andi', 'Budi', 'Citra']
umur = [25, 30, 28]
df_zip = pd.DataFrame(list(zip(nama, umur)), columns=['Nama', 'Umur'])

# Dari dictionary -> key jadi nama kolom
df_dict = pd.DataFrame({
    'Nama': ['Andi', 'Budi', 'Citra'],
    'Umur': [25, 30, 28]
})

# Dari NumPy Array 2D -> tanpa nama kolom eksplisit, default 0, 1, 2, ...
data_2d = np.array([[1, 2, 3], [4, 5, 6]])
df_array = pd.DataFrame(data_2d, columns=['Kolom1', 'Kolom2', 'Kolom3'])

print(df_zip)
print(df_dict)
print(df_array)
```

---

### 3.3 Indexing dan Slicing pada DataFrame

#### A. Pengaksesan Kolom

- Memilih satu kolom akan menghasilkan objek Series, dilakukan dengan memanggil nama kolom di dalam kurung siku `df['NamaKolom']`. Pengaksesan menggunakan atribut `df.NamaKolom` juga dimungkinkan, tetapi sangat tidak direkomendasikan karena rawan konflik dengan metode bawaan.
- Memilih beberapa kolom sekaligus dilakukan dengan melewatkan sebuah list di dalam kurung siku ganda `df[['Kolom1', 'Kolom2']]`, yang akan menghasilkan objek DataFrame baru.

#### B. Pengaksesan Menggunakan .loc[] dan .iloc[]

- **Atribut .loc[]**: Digunakan untuk mengakses baris dan kolom berdasarkan label nama. Slicing baris menggunakan `.loc['A':'C']` bersifat inklusif terhadap batas akhir (artinya baris 'C' akan ikut ditampilkan).
- **Atribut .iloc[]**: Digunakan untuk mengakses data berdasarkan lokasi indeks angka (integer-based location) yang dimulai dari 0. Slicing baris menggunakan `.iloc[0:2]` bersifat eksklusif terhadap batas akhir (artinya baris pada indeks ke-2 tidak akan ditampilkan).

#### C. Conditional Filtering

- Digunakan untuk menyaring data berdasarkan kondisi boolean tertentu. Operasi perbandingan seperti `df > 0` akan menguji setiap elemen di dalam DataFrame dan menghasilkan boolean mask (tabel berisi nilai True dan False).
- Menyaring baris secara spesifik dilakukan dengan memasukkan kondisi di dalam kurung siku DataFrame utama, misalnya `df[df['W'] > 0]`. Jika ingin mengambil nilai kolom tertentu saja dari hasil filter tersebut, dapat ditambahkan nama kolom di akhir baris kode.

> [!tip] Conditional filtering Pandas = `WHERE` di SQL
> `df[df['W'] > 0]` (Bandingkan dengan [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|klausa WHERE di SQL]] — konsep sama, sintaks beda: `df[df['col'] > value]` ≈ `WHERE col > value`.)

> [!warning] Audio Insight — `.loc` inklusif vs `.iloc` eksklusif
> Dosen memperingatkan agar mahasiswa memahami perbedaan perilaku slicing antara `.loc` dan `.iloc`. Pada `.loc['A':'C']`, baris C ditampilkan karena pencarian berbasis nama label. Sedangkan pada `.iloc[0:2]`, baris pada indeks ke-2 ditiadakan karena mengandalkan perilaku eksklusif indeks integer Python standar.
> Dosen memberikan contoh sintaks pengaksesan elemen tunggal maupun kelompok menggunakan kedua atribut tersebut.

```python
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

### 3.4 Manipulasi DataFrame

#### A. Menambahkan Baris dan Kolom

- Kolom baru dapat ditambahkan dengan langsung menetapkan nilainya (baik nilai konstan maupun hasil kalkulasi matematis kolom lain) ke dalam nama kolom baru.
- Penambahan kolom pada posisi spesifik di tengah tabel dapat memanfaatkan metode `.insert()` dengan menyertakan indeks lokasi tujuan.
- Baris baru dapat dimasukkan dengan menetapkan baris baru tersebut menggunakan atribut `.loc[]`.

#### B. Menghapus Baris dan Kolom (.drop)

- Metode `.drop()` digunakan untuk menghapus baris atau kolom dari DataFrame.
- Parameter `axis` sangat krusial dalam metode ini: menetapkan `axis=1` untuk menghapus kolom, dan `axis=0` untuk menghapus baris.

#### C. Reset Index, Set Index, dan Inplace Parameter

- **reset_index()**: Mengatur ulang indeks DataFrame kembali ke indeks numerik default (0, 1... n) dan memindahkan indeks lama menjadi kolom baru berlabel 'index'.
- **set_index()**: Menetapkan salah satu kolom DataFrame untuk digunakan sebagai indeks baris yang baru, menggantikan indeks yang lama.
- **inplace=True**: Secara default, metode modifikasi seperti `.drop()`, `.reset_index()`, dan `.set_index()` tidak mengubah DataFrame asli melainkan mengembalikan salinan baru (not inplace). Untuk memperbarui data asli secara permanen tanpa perlu menetapkannya kembali ke variabel baru, parameter `inplace=True` wajib disertakan.

#### D. Multi-Index (Hierarchical Indexing)

- Multi-Index memungkinkan pembuatan indeks bertingkat (hierarki) pada DataFrame.
- Indeks ini dapat dikonstruksi dari kumpulan tuple menggunakan fungsi `pd.MultiIndex.from_tuples()`. Pengaksesan data bertingkat ini dilakukan menggunakan metode `.loc[]` atau metode `.xs()` (cross-section) yang sangat efisien untuk menembus level indeks tertentu.

> [!tip] Audio Insight — `inplace=True` sebagai pengaman, dan kegunaan Multi-Index
> Dosen menjelaskan kegunaan parameter `inplace=True` sebagai langkah pengamanan (safeguard) agar pengguna tidak kehilangan data aslinya akibat eksekusi perintah pembersihan data yang salah secara tidak sengaja.
> Dosen mengilustrasikan bahwa Multi-Index sangat berguna ketika kita memiliki data yang terbagi ke dalam kelompok besar (seperti wilayah atau kota) dan sub-kelompok di dalamnya (seperti kode cabang atau nomor urut).

```python
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

**Contoh kode — Multi-Index secara lengkap (`from_tuples` dan `.xs()`):**

```python
import pandas as pd
import numpy as np

# Membuat MultiIndex dari kumpulan tuple: (kota, cabang)
tuples = [('Jakarta', 'Cabang1'), ('Jakarta', 'Cabang2'),
          ('Bandung', 'Cabang1'), ('Bandung', 'Cabang2')]
multi_index = pd.MultiIndex.from_tuples(tuples, names=['Kota', 'Cabang'])

df_multi = pd.DataFrame(np.random.randn(4, 2), index=multi_index, columns=['Penjualan', 'Profit'])
print(df_multi)

# Akses level luar (semua cabang di Jakarta) via .loc
print(df_multi.loc['Jakarta'])

# Akses level dalam (semua data 'Cabang1' lintas kota) via .xs() -> cross-section
print(df_multi.xs('Cabang1', level='Cabang'))
```

---

### 3.5 Pengurutan dan Analisis Statistik Deskriptif

#### A. Pengurutan Data (Sorting)

- **sort_values()**: Digunakan untuk mengurutkan DataFrame berdasarkan nilai pada satu atau beberapa kolom tertentu. Defaultnya diurutkan secara menaik (ascending), namun dapat diatur menjadi menurun menggunakan parameter `ascending=False`.
- **sort_index()**: Digunakan untuk mengurutkan baris DataFrame berdasarkan indeksnya.

> [!tip] `.sort_values()` = `ORDER BY` di SQL
> (Bandingkan dengan [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|klausa ORDER BY di SQL]] — konsep sama, sintaks beda: `df.sort_values('col', ascending=False)` ≈ `ORDER BY col DESC`.)

#### B. Fungsi, Method, dan Atribut Statistik

- Atribut `.shape`: Mengembalikan jumlah baris dan kolom dalam tuple.
- Atribut `.columns`: Menampilkan daftar nama kolom.
- Atribut `.dtypes`: Mengetahui tipe data masing-masing kolom.
- Method `.head()` dan `.tail()`: Menampilkan baris teratas dan terbawah tabel (secara default menampilkan 5 baris).
- Method `.info()`: Menghasilkan informasi lengkap struktur DataFrame meliputi tipe data, jumlah nilai non-null, dan penggunaan memori.
- Method `.describe()`: Menghitung statistik deskriptif otomatis (mean, std, min, max, kuartil) untuk seluruh kolom bertipe numerik — lihat [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]] Bab 4 untuk arti tiap statistiknya.
- Method statistik spesifik: `.mean()`, `.median()`, `.std()`, `.min()`, dan `.max()` — padanan langsung fungsi agregat SQL `AVG()`, `MIN()`, `MAX()` yang dipelajari di [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] (Bandingkan: `df['col'].mean()` ≈ `SELECT AVG(col) FROM tabel`).
- Method keunikan: `.unique()` untuk melihat nilai unik, `.nunique()` untuk menghitung jumlah nilai unik, dan `.value_counts()` untuk menghitung frekuensi kemunculan nilai pada suatu kolom.

> [!tip] Audio Insight — Biasakan `.head()`/`.info()` di awal eksplorasi
> Dosen menyarankan agar pemula selalu membiasakan diri memanggil `.head()` atau `.info()` setelah mengimpor data eksternal. Langkah peninjauan awal ini krusial untuk mendeteksi apakah data telah dimuat dengan benar serta melihat tipe data awal setiap kolom.

```python
# Meninjau statistik deskriptif otomatis
df.describe()

# Menampilkan informasi struktural DataFrame
df.info()

# Mengurutkan DataFrame berdasarkan nilai kolom 'col1' secara menurun
df.sort_values(by='col1', ascending=False)

# Menghitung frekuensi kemunculan nilai unik pada kolom 'col2'
df['col2'].value_counts()
```

**Contoh kode — atribut & method lain yang disebutkan (`.shape`, `.columns`, `.dtypes`, `sort_index`, `.unique()`, `.nunique()`):**

```python
import pandas as pd

df = pd.DataFrame({
    'col1': [3, 1, 2, 1],
    'col2': ['A', 'B', 'A', 'C']
}, index=[3, 0, 2, 1])

print(df.shape)     # (4, 2)
print(df.columns)   # Index(['col1', 'col2'], dtype='object')
print(df.dtypes)    # col1: int64, col2: object

print(df.head(2))   # 2 baris teratas
print(df.tail(2))   # 2 baris terbawah

print(df.sort_index())          # urutkan berdasarkan LABEL indeks (0,1,2,3)
print(df.sort_values('col1'))    # urutkan berdasarkan NILAI kolom col1

print(df['col2'].unique())    # array(['A', 'B', 'C'], dtype=object)
print(df['col2'].nunique())   # 3 -> jumlah nilai unik
```

---

### 3.6 Penanganan Missing Values dan Pengelompokan Data

#### A. Penanganan Missing Values (Data Kosong)

- Data kosong atau bernilai null direpresentasikan sebagai NaN (Not a Number) dalam Pandas.
- **Deteksi**: Menggunakan metode `.isna()` untuk menghasilkan tabel boolean, atau dipadukan dengan `.isna().sum()` untuk langsung menghitung jumlah baris kosong di setiap kolom.
- **Pembersihan (Hapus)**: Menggunakan metode `.dropna()` untuk membuang seluruh baris atau kolom yang memiliki nilai kosong.
- **Imputasi (Isi)**: Menggunakan metode `.fillna()` untuk mengganti data kosong dengan nilai tertentu, misalnya string statis atau nilai dinamis berupa rata-rata kolom tersebut (`df['Age'].mean()`).

#### B. Pengelompokan Data (Grouping)

- Pengelompokan data didasarkan pada nilai kategori pada kolom tertentu menggunakan metode `.groupby()`.
- Setelah dikelompokkan, kita wajib menggunakan fungsi agregat (seperti `.mean()`, `.sum()`, atau `.count()`) untuk menghasilkan nilai ringkasan statistik dari masing-masing kelompok tersebut.

> [!warning] Audio Insight — `.dropna()` boros informasi, `.groupby()` otomatis abaikan kolom string
> Dosen menerangkan bahwa dalam proyek nyata, membuang data kosong menggunakan `.dropna()` sering kali bukan solusi terbaik karena dapat melenyapkan informasi berharga lainnya pada baris tersebut. Oleh karena itu, teknik pengisian data kosong (`.fillna()`) dengan nilai rata-rata (_mean imputation_) sangat direkomendasikan untuk menjaga integritas data.
> Dosen mengilustrasikan operasi `.groupby('Company')` yang dipadukan dengan fungsi `.mean()`. Pandas secara cerdas hanya akan menghitung nilai rata-rata untuk kolom yang bertipe numerik (seperti kolom Sales), dan mengabaikan kolom bertipe string/kategori.

> [!tip] `.groupby()` = "GROUP BY" versi Pandas
> Konsep `.groupby()` diikuti fungsi agregasi ini sama persis logikanya dengan klausa `GROUP BY` di SQL yang dipelajari di [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]]. Kalau di SQL kamu menulis `SELECT Company, AVG(Sales) FROM tabel GROUP BY Company`, di Pandas kamu menulis `df.groupby('Company')['Sales'].mean()` — hasil akhirnya konseptual sama.

```python
# Menghitung jumlah data kosong per kolom
df.isna().sum()

# Mengisi data kosong pada kolom 'Age' dengan nilai rata-rata usia
df['Age'].fillna(value=df['Age'].mean(), inplace=True)

# Mengelompokkan data berdasarkan kolom 'Company' dan menghitung rata-rata nilai numerik
df.groupby('Company').mean()
```

**Contoh kode — deteksi dan penanganan missing values lebih lengkap:**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Nama': ['Andi', 'Budi', 'Citra', 'Dedi'],
    'Age': [25, np.nan, 30, np.nan],
    'Kota': ['Jakarta', 'Bandung', np.nan, 'Medan']
})

print(df.isna())        # tabel boolean True/False untuk tiap sel
print(df.isna().sum())  # jumlah NaN per kolom -> Age: 2, Kota: 1

df_dropped = df.dropna()             # buang SEMUA baris yang punya minimal 1 NaN
df_filled = df.copy()
df_filled['Age'] = df_filled['Age'].fillna(df_filled['Age'].mean())  # isi dengan rata-rata
df_filled['Kota'] = df_filled['Kota'].fillna('Tidak diketahui')       # isi dengan string statis

print(df_filled)
```

---

### 3.7 Penggabungan DataFrame dan Operasi Lanjutan

#### A. Merging, Joining, dan Concatenating

- **pd.merge()**: Menggabungkan dua DataFrame berdasarkan kesamaan kolom kunci (key) tertentu. Konsep penggabungannya analog dengan SQL Join, yang mendukung tipe gabungan _inner_, _left_, _right_, dan _outer_.
- **.join()**: Menggabungkan dua DataFrame berdasarkan indeks barisnya, bukan berdasarkan kolom kunci.
- **pd.concat()**: Menyatukan atau menumpuk beberapa DataFrame. Penggabungan dapat dilakukan secara vertikal ke bawah (default: `axis=0`) atau secara horizontal berdampingan (`axis=1`).

> [!tip] `pd.merge()` = SQL `JOIN`
> `pd.merge(..., how='inner'/'left'/'right'/'outer')` adalah padanan langsung dari `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, dan `FULL OUTER JOIN` yang dipelajari di [[Sesi 10 - SQL Working With Multiple Tables (JCAIEH M1)|Sesi 10 - SQL Working With Multiple Tables]]. Kalau kamu sudah paham cara kerja JOIN di SQL, `pd.merge()` akan terasa sangat familier.

#### B. Operasi Aritmatika Antar Kolom, .apply(), dan Pivot Table

- **Operasi Aritmatika**: Operasi aritmatika dasar (penjumlahan, pengurangan, perkalian, pembagian) dapat langsung dilakukan antar kolom DataFrame secara element-wise.
- **Metode .apply()**: Digunakan untuk menerapkan fungsi buatan sendiri (custom function) atau fungsi bawaan Python ke seluruh elemen kolom DataFrame.
- **Fungsi Lambda**: Digunakan untuk menulis fungsi anonim sekali pakai secara ringkas di dalam metode `.apply()`.
- **Pivot Table**: Metode `.pivot_table()` digunakan untuk mereorganisasi, merangkum, dan mentransformasikan struktur data tabular agar lebih mudah dianalisis berdasarkan variabel kunci tertentu.

> [!warning] Audio Insight — `pd.concat(axis=1)` butuh indeks selaras, `.apply()` lebih efisien dari loop
> Dosen memperlihatkan perbedaan konkret antara penggabungan vertikal dan horizontal menggunakan `pd.concat()`. Jika menggunakan `axis=1`, pastikan baris data memiliki indeks yang sejajar agar tidak menghasilkan banyak nilai NaN pada baris yang tidak cocok.
> Dosen memberikan contoh fungsionalitas `.apply()` dengan fungsi Lambda untuk manipulasi string atau operasi matematika cepat, yang jauh lebih efisien dibandingkan menulis iterasi loop manual menggunakan `for` di Python.

```python
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

**Contoh kode — `.join()` berbasis indeks (berbeda dari `pd.merge()` yang berbasis kolom kunci):**

```python
import pandas as pd

df_kiri = pd.DataFrame({'Skor': [80, 90, 70]}, index=['Andi', 'Budi', 'Citra'])
df_kanan = pd.DataFrame({'Kelas': ['A', 'B', 'A']}, index=['Andi', 'Budi', 'Dedi'])

hasil_join = df_kiri.join(df_kanan, how='left')  # gabung berdasarkan INDEKS, bukan kolom
print(hasil_join)
#        Skor Kelas
# Andi     80     A
# Budi     90     B
# Citra    70   NaN   <- Citra tidak ada padanan index di df_kanan
```

### 3.8 Membaca dan Menyimpan Data (File I/O)

#### A. Metode Import Berkas

- CSV: `pd.read_csv()`
- Excel: `pd.read_excel()`
- JSON: `pd.read_json()`
- HTML: `pd.read_html()`

#### B. Metode Export Berkas

- CSV: `df.to_csv()`
- Excel: `df.to_excel()`
- JSON: `df.to_json()`

> [!warning] Audio Insight — Pandas bisa baca HTML tapi tidak bisa ekspor ke HTML, jangan lupa `index=False`
> Dosen memaparkan batasan fungsionalitas File I/O pada Pandas. Meskipun Pandas sangat andal dalam mengimpor data dari dokumen web menggunakan `pd.read_html()`, Pandas tidak memiliki fungsi bawaan untuk mengekspor atau menyimpan DataFrame langsung menjadi file fisik berformat `.html`.
> Saat mengekspor data ke format CSV atau Excel, dosen sangat menganjurkan untuk menambahkan parameter `index=False` agar indeks numerik Pandas tidak ikut tersimpan sebagai kolom baru yang tidak perlu di dalam file eksternal tersebut.

```python
# Membaca file CSV
df = pd.read_csv('dataset.csv')

# Menyimpan DataFrame ke file Excel tanpa menyertakan kolom indeks numerik
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
```

**Contoh kode — format lain yang disebutkan (JSON, HTML, dan ekspor CSV/JSON):**

```python
import pandas as pd

# Membaca JSON
df_json = pd.read_json('dataset.json')

# Membaca tabel HTML dari sebuah halaman web (mengembalikan LIST of DataFrame, satu per tabel)
daftar_tabel = pd.read_html('https://contoh-situs.com/halaman-berisi-tabel')
df_html = daftar_tabel[0]   # ambil tabel pertama yang ditemukan

# Ekspor ke CSV, tanpa kolom indeks
df.to_csv('hasil_export.csv', index=False)

# Ekspor ke JSON
df.to_json('hasil_export.json', orient='records')
```

### 3.9 Tabel Istilah Teknis dan Karakteristik

| Istilah Teknis / Metode | Karakteristik dan Deskripsi Utama |
|:--|:--|
| _Series_ | Struktur data satu dimensi (1D) dengan indeks berlabel yang dapat menyimpan tipe data objek apa pun. |
| _DataFrame_ | Struktur data dua dimensi (2D) berbentuk tabel berukuran fleksibel yang terdiri dari kumpulan Series. |
| _.loc[]_ | Metode pengaksesan baris/kolom berdasarkan label nama, dengan sifat slicing batas akhir yang inklusif. |
| _.iloc[]_ | Metode pengaksesan baris/kolom berdasarkan indeks numerik (integer), bersifat eksklusif batas akhir. |
| _.drop()_ | Menghapus kolom (axis=1) atau baris (axis=0). Membutuhkan parameter inplace=True untuk memperbarui data asli. |
| _inplace=True_ | Parameter yang digunakan untuk langsung meng-override dan menyimpan perubahan pada objek DataFrame asli. |
| _Multi-Index_ | Struktur indeks baris/kolom bertingkat (hierarki) untuk menangani analisis data multidimensi yang kompleks. |
| _.groupby()_ | Mengelompokkan baris data berdasarkan kategori kolom tertentu dan wajib diikuti oleh fungsi agregasi. |
| _pd.merge()_ | Menggabungkan dua DataFrame berdasarkan kolom kunci yang sama dengan tipe join seperti SQL. |
| _pd.concat()_ | Menyatukan atau menumpuk beberapa DataFrame secara vertikal (axis=0) atau horizontal (axis=1). |
| _.apply()_ | Menerapkan fungsi khusus atau fungsi Lambda ke setiap elemen di dalam kolom DataFrame secara serentak. |
| _.pivot_table()_ | Mereorganisasi dan meringkas data tabular berdasarkan parameter indeks, kolom, dan nilai tertentu. |

---

### 3.10 Tugas Latihan Praktek DataFrame (Titanic Dataset Exercises)

Seluruh latihan praktek di bawah ini menggunakan Titanic dataset yang bersumber dari Kaggle.

#### Latihan 1: Penyaringan Penumpang Wanita yang Selamat

- **Tugas**: Melakukan filtering data penumpang untuk menampilkan penumpang wanita saja yang selamat dari bencana.
- **Sintaks Solusi**:

```python
df[(df['Sex'] == 'female') & (df['Survived'] == 1)]
```

#### Latihan 2: Pengelompokan Usia (AgeGroup) dan Rata-rata Tarif Tiket

- **Tugas**: Menambahkan kolom baru bernama `AgeGroup` dengan aturan: jika usia di bawah 18 tahun diisi dengan "Child", jika tidak diisi dengan "Adult". Kemudian hitung rata-rata tarif tiket (`Fare`) yang dibayarkan oleh masing-masing kelompok tersebut menggunakan `.groupby()`.
- **Sintaks Solusi**:

```python
df['AgeGroup'] = df['Age'].apply(lambda age: 'Child' if age < 18 else 'Adult')
df.groupby('AgeGroup')['Fare'].mean()
```

#### Latihan 3: Analisis Kelas Kabin (Pclass)

- **Tugas**: Mengelompokkan data berdasarkan kelas kabin (`Pclass`), kemudian hitung total jumlah penumpang dan rata-rata tarif tiket (`Fare`) untuk setiap kelasnya.
- **Sintaks Solusi**:

```python
df.groupby('Pclass')['Fare'].agg(['count', 'mean'])
```

#### Latihan 4: Tingkat Keselamatan Berdasarkan Kombinasi Kelas dan Gender

- **Tugas**: Melakukan pengelompokan data dengan dua kolom sekaligus (`Pclass` dan `Sex`) untuk menghitung rata-rata tingkat keselamatan penumpang (`Survived`), kemudian urutkan hasilnya dari tingkat keselamatan tertinggi ke terendah.
- **Sintaks Solusi**:

```python
df.groupby(['Pclass', 'Sex'])['Survived'].mean().sort_values(ascending=False)
```

> [!warning] Catatan transkripsi sumber
> Baris kode Latihan 4 pada dokumen sumber terpotong di tengah kata (`...sort_values(ascendi`). Bagian `ascending=False)` di atas dilengkapi berdasarkan instruksi tugas ("urutkan dari tingkat keselamatan tertinggi ke terendah") dan konvensi parameter `sort_values()` yang sudah dibahas di Bab 3.5 — sangat mungkin benar, tapi ada baiknya dicek ulang terhadap modul/rekaman aslinya jika tersedia.

---

## Ringkasan Kilat Sesi (Cheat Sheet)

| Konsep | Kunci |
|:--|:--|
| `np.arange(start, stop, step)` | kamu tentukan STEP, jumlah elemen dihitung otomatis (mirip `range()`) |
| `np.linspace(start, stop, num)` | kamu tentukan COUNT (num), jarak dihitung otomatis |
| `.max()` vs `.argmax()` | nilai vs posisi/indeks |
| Slice NumPy | VIEW, bukan copy — pakai `.copy()` untuk salinan independen |
| `.loc[]` | label, batas akhir INKLUSIF |
| `.iloc[]` | posisi integer, batas akhir EKSKLUSIF |
| `.groupby()` | wajib diikuti fungsi agregasi (`.mean()`, `.sum()`, dst) — setara `GROUP BY` SQL |
| `pd.merge()` | setara `JOIN` SQL (inner/left/right/outer) |
| `inplace=True` | ubah DataFrame asli langsung, tanpa perlu re-assign ke variabel |

---

## 🔗 Terkait

- [[Sesi 04 - Data Types Collection Notes (JCAIEH M1)|Sesi 04 - Data Types Collection Notes]] — List/Dict sebagai fondasi sebelum NumPy/Pandas.
- [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] dan [[Sesi 10 - SQL Working With Multiple Tables (JCAIEH M1)|Sesi 10 - SQL Working With Multiple Tables]] — padanan SQL untuk `.groupby()`, filtering, `.sort_values()`, dan `.merge()`.
- [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]] — arti statistik di balik `.describe()`, `.mean()`, `.std()`.
- [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]] — DataFrame hasil manipulasi di sesi ini jadi input langsung untuk plotting.
