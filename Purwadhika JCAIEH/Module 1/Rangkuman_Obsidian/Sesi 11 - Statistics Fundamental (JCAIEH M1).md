---
tags: [jcaieh/module1, sesi-11, statistics, descriptive-statistics, inferential-statistics, sampling, central-tendency, spread, iqr, normal-distribution, empirical-rule, skewness, imbalanced-data, jcaieh/module1/sesi11]
bootcamp: JCAIEH
module: 1
session: 11
aliases: ["Sesi 11", "Statistics Fundamental", "Statistika Fundamental"]
---

# Sesi 11 - Statistics Fundamental

> Sumber: rangkuman gabungan slide/PDF resmi + transkrip audio kelas (ditandai sebagai callout Audio Insight di bawah), dilengkapi contoh kode Python tambahan agar setiap konsep punya pegangan praktis yang bisa langsung dijalankan.

---

## Bab 1 Pengantar Statistika (Introduction to Statistics)

### 1.1 Definisi Statistika

#### A. Fondasi Konseptual

- Statistika didefinisikan sebagai metodologi untuk mengumpulkan (_collecting_), menganalisis (_analyzing_), menginterpretasikan (_interpreting_), dan menarik kesimpulan (_drawing conclusion_) dari data.
- Secara lebih luas, statistika merupakan seni dan sains dalam merancang studi (_designing studies_) dan menganalisis data yang dihasilkan oleh studi tersebut.
- Tujuan utama (_ultimate goal_) dari statistika adalah menerjemahkan data menjadi pengetahuan (_knowledge_) dan pemahaman mengenai dunia di sekitar kita.
- Singkatnya, statistika adalah seni dan sains untuk belajar dari data (_learning from data_).

> [!tip] Audio Insight — Statistika sebagai "seni belajar dari data"
> Dosen menjelaskan bahwa statistika pada dasarnya adalah "seni dalam mempelajari data". Statistika adalah subjek yang sangat luas (_broad subject_) dengan banyak aplikasi di berbagai macam bidang (_various field_).

---

### 1.2 Aplikasi Statistika di Berbagai Bidang

#### A. Bidang Penerapan Praktis

| Bidang / Metodologi | Karakteristik / Kasus Penggunaan |
|:--|:--|
| **Experimental Design** | Digunakan untuk melakukan _A/B Testing_ pada desain aplikasi atau web baru. |
| **Survey** | Digunakan untuk memprediksi hasil pemilihan umum (_election_) menggunakan _Exit Poll_ atau Hitung Cepat (_Quick Count_). |
| **Research** | Digunakan untuk menarik kesimpulan ilmiah dalam studi penelitian medis (_Medical Research Studies_). |
| **Quality Control** | Digunakan untuk menjaga kualitas produk yang dihasilkan di pabrik (_factory_). |

> [!tip] Audio Insight — A/B Testing, Quick Count, dan Research
> - **A/B Testing**: Ketika suatu aplikasi akan menerapkan desain baru, dilakukan pengujian terlebih dahulu pada dua kelompok pengguna, yaitu Kelompok A dan Kelompok B. Dosen menjelaskan contoh pembagian di mana Kelompok A menerima 50% pengguna aktif lama (_existing users_) dengan desain baru, sedangkan Kelompok B menerima sisa 50% dengan desain lama. Keberhasilan diukur dengan melihat matriks tertentu, seperti peningkatan pembelian (_conversion rate_) akibat perbedaan desain tersebut.
> - **Quick Count vs Real Count**: Hitung cepat (_quick count_) merupakan metode penghitungan cepat di mana data tidak dihitung seluruhnya, melainkan hanya diambil sampelnya secara acak (_random_) dari Tempat Pemungutan Suara (TPS). Hasil _quick count_ biasanya sedikit berbeda dengan _real count_ (misalnya jika hasil _quick count_ 60%, hasil _real count_ bisa berkisar antara 58% hingga 62%) dengan tingkat kepercayaan (_confidence level_) tertentu.
> - **Research**: Statistika sangat krusial untuk membuat kesimpulan (_making conclusion_) tidak hanya pada penelitian medis, tetapi juga pada berbagai macam bidang penelitian ilmiah lainnya.

---

### 1.3 Tiga Tahapan Utama dalam Proses Statistika (Step-by-Step Statistics)

#### A. Alur Kerja Statistika

1. **Design** — Tahap perencanaan penelitian dan pengumpulan data. Aktivitas utama meliputi memformulasikan masalah penelitian (_formulate research problem_), mendefinisikan [[Kamus & Cheatsheet (JCAIEH M1)#P|populasi]] dan [[Kamus & Cheatsheet (JCAIEH M1)#S|sampel]] (_define population and sample_), serta melakukan pengumpulan data (_data collection_).
2. **Description** — Tahap merangkum dan mengeksplorasi data yang telah dikumpulkan. Aktivitas utama meliputi pembuatan visualisasi data dalam bentuk ringkasan grafis (_graphical summary_), ringkasan numerik (_numerical summary_), dan ringkasan tabel (_table summary_). Lihat [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]] untuk toolkit visualnya.
3. **Inference** — Tahap membuat prediksi dan melakukan generalisasi mengenai fenomena yang direpresentasikan oleh data tersebut. Aktivitas utama adalah menggunakan metode yang tepat untuk memecahkan masalah penelitian (_solve the problem_) dan melaporkan hasilnya (_report the result_).

> [!tip] Audio Insight — Rincian tiap tahap Design → Description → Inference
> - Pada tahap **Design**, aktivitas awal adalah merancang formulasi masalah, menentukan karakteristik populasi, merancang sampel, serta merencanakan bagaimana data akan dikumpulkan.
> - Pada tahap **Description**, teknik-teknik visualisasi data (_data visualization_) diterapkan agar data yang rumit dapat dipahami secara sederhana sebelum dianalisis lebih lanjut.
> - Pada tahap **Inference**, peneliti menggunakan metode statistik yang sesuai untuk memecahkan masalah penelitian dan melaporkan hasil akhirnya secara ilmiah.

---

### 1.4 Dua Cabang Besar Statistika (Type of Statistics)

#### A. Klasifikasi Cabang Statistika

| Cabang Statistika | Fokus Utama | Metodologi & Karakteristik |
|:--|:--|:--|
| **[[Kamus & Cheatsheet (JCAIEH M1)#D|Descriptive Statistics]]** | Berfokus pada perangkuman dan penggambaran data yang dimiliki. | Terdiri dari metode untuk mengorganisasikan, menyederhanakan, dan merangkum informasi. |
| **[[Kamus & Cheatsheet (JCAIEH M1)#I|Inferential Statistics]]** | Berfokus pada penggunaan data sampel untuk membuat kesimpulan mengenai populasi. | Terdiri dari metode untuk menarik kesimpulan dan mengukur tingkat keandalan kesimpulan (_reliability of conclusion_) berdasarkan sampel dari populasi tersebut. |

> [!tip] Audio Insight — Descriptive vs Inferential dalam praktik
> - **Descriptive Statistics**: Digunakan murni untuk mendeskripsikan data yang ada, seperti menghitung rata-rata (_mean_), mengidentifikasi kategori yang paling sering muncul (modus/_mode_), atau melihat tren kenaikan dan penurunan data dari waktu ke waktu tanpa melakukan prediksi atau generalisasi lebih lanjut.
> - **Inferential Statistics**: Cabang ini penting karena mengumpulkan keseluruhan data populasi sangat sulit dilakukan. Oleh karena itu, kita mengambil sebagian data sebagai sampel, lalu menggunakan statistik sampel tersebut untuk menarik kesimpulan dan melakukan estimasi mengenai parameter populasi dengan tingkat kepercayaan (_confidence level_) tertentu.
> - Contoh hubungan kedua cabang ini adalah _quick count_ (yang menggunakan sampel) untuk mengestimasi hasil pemilu akhir pada _real count_ (populasi).

#### B. Representasi Konseptual Berbasis Kode

```python
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

---

## Bab 2 Data, Variabel, dan Skala Pengukuran (Data, Variables, and Scale of Measurement)

### 2.1 Definisi Data (Definition of Data)

#### A. Unit Informasi

- Data didefinisikan sebagai unit informasi individual (_individual units of information_), seperti data satu orang, satu buku, satu barang, satu bangunan, satu mobil, atau satu perusahaan.
- Dalam struktur dataset, representasi data diatur dalam format baris dan kolom yang terstruktur:
    - Setiap baris (_row_) mewakili satu unit observasi (_observation unit_ / _unit of observation_).
    - Setiap kolom (_column_) mewakili satu variabel (_variable_) yang menyimpan karakteristik, sifat, atau atribut spesifik yang diamati dari setiap unit informasi tersebut.
    - Sebagai contoh, pada dataset buku terlaris Amazon:
        - Baris 0, 1, 2, dst. masing-masing mewakili satu objek buku fisik yang diobservasi.
        - Kolom-kolom seperti _Name_ (judul buku), _Author_ (penulis), _User Rating_, _Reviews_, _Price_, _Year_, dan _Genre_ mewakili variabel yang diukur dari setiap buku tersebut.

> [!tip] Audio Insight — Definisi "data" versi statistika vs database
> Dosen menjelaskan bahwa di luar pemahaman database relasional konvensional, statistik mendefinisikan data secara spesifik sebagai unit observasi individual. Dalam analisis data praktis, sangat krusial untuk langsung mengidentifikasi baris sebagai representasi dari unit observasi tunggal dan kolom sebagai dimensi variabelnya sebelum melakukan manipulasi data lebih lanjut. Konsep baris = observasi, kolom = variabel ini persis sama dengan struktur tabel di [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] dan `DataFrame` pada [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]].

**Contoh kode — memverifikasi struktur baris/kolom sebuah dataset:**

```python
import pandas as pd

data_buku = {
    'Name': ['Buku A', 'Buku B', 'Buku C'],
    'Author': ['Penulis X', 'Penulis Y', 'Penulis Z'],
    'User Rating': [4.7, 4.5, 4.9],
    'Price': [15, 8, 22]
}
df = pd.DataFrame(data_buku)

print(df.shape)   # (3, 4) -> 3 baris (observasi), 4 kolom (variabel)
print(df.index)   # RangeIndex menunjukkan setiap baris = satu unit observasi
print(df.columns) # Index(['Name', 'Author', 'User Rating', 'Price']) -> masing-masing = satu variabel
```

---

### 2.2 Klasifikasi Variabel (Classification of Variables)

#### A. Karakteristik Variabel

- Karakteristik atau sifat yang bervariasi dari satu orang atau objek ke orang atau objek lainnya disebut sebagai variabel (contoh: _Height_, _Weight_, _Eye Color_, dll.).
- Variabel secara mendasar dikelompokkan menjadi dua kategori utama berdasarkan sifat datanya:
    1. **Qualitative (Categorical)** — Observasi di mana data yang dikumpulkan termasuk dalam satu set kelompok kategori yang berbeda (_distinct categories_). Terbagi menjadi dua tipe:
        - **[[Kamus & Cheatsheet (JCAIEH M1)#N|Nominal]]**: Kategori-kategori data yang tidak memiliki urutan, peringkat, atau tingkatan logis yang jelas. Contoh: _Type of fruits_ (jenis buah), _Country name_ (nama negara), _Gender_ (Male/Female), dan _Color_ (warna).
        - **[[Kamus & Cheatsheet (JCAIEH M1)#O|Ordinal]]**: Kategori-kategori data yang memiliki urutan, peringkat, atau tingkatan logis yang jelas. Contoh: _Education level_ (SD, SMP, SMA, S1, S2, S3), _Satisfaction level_ (Sangat tidak puas, Tidak puas, Biasa saja, Puas, Sangat puas), dan _Job level_ (Officer, Supervisor, Manager, General Manager).
    2. **Quantitative (Numerical)** — Observasi di mana data berupa nilai numerik yang logis untuk dilakukan operasi matematika seperti penjumlahan atau pengurangan. Terbagi menjadi dua tipe:
        - **[[Kamus & Cheatsheet (JCAIEH M1)#D|Discrete]]**: Variabel numerik yang nilainya berupa bilangan bulat (_integer_) dan tidak dapat didefinisikan dengan bilangan desimal. Data ini biasanya diperoleh dari hasil perhitungan (_counting_). Contoh: _Number of rooms_ (jumlah ruangan), _Number of clicks_ (jumlah klik), dan _Violation frequency_ (frekuensi pelanggaran).
        - **[[Kamus & Cheatsheet (JCAIEH M1)#C|Continuous]]**: Variabel numerik yang nilainya diperoleh dari hasil pengukuran (_measurement_) sepanjang nilai kontinu (_continuum value_) dan dapat didefinisikan dengan bilangan desimal bergantung tingkat kepresisian alat pengukur. Contoh: _Height_ (tinggi badan), _Weight_ (berat badan), _Price_ (harga), dan _Age_ (usia).

#### B. Signifikansi Penentuan Tipe Variabel dalam Data Science

- Penentuan tipe variabel sangat krusial karena dalam praktiknya, metodologi _Data Analysis_ dan pemodelan prediktif sepenuhnya bergantung pada tipe variabel tersebut:
    - Menentukan kelayakan penggunaan ukuran pemusatan data seperti rata-rata (_average/mean_) untuk mendeskripsikan kelompok data (contoh: tidak logis menggunakan rata-rata untuk mendeskripsikan data kualitatif).
    - Menentukan jenis algoritma pembelajaran mesin (_machine learning_) yang tepat, misalnya memilih pendekatan klasifikasi (_Classification_) atau regresi (_Regression_) saat membangun model prediksi (contoh: menggunakan _Classification_ untuk memprediksi apakah seorang pengguna akan pergi/_Churn_ atau tidak, dan menggunakan _Regression_ untuk memprediksi harga atau nilai numerik kontinu lainnya).

> [!warning] Audio Insight — Klarifikasi istilah yang sering disalahpahami
> - **Klarifikasi Desimal pada Discrete**: Dosen memberikan analogi jumlah ruangan (_number of rooms_). Peneliti tidak dapat menyatakan jumlah ruangan bernilai 1,5 atau 1,1 karena ruangan secara fisis harus dihitung dalam unit bilangan bulat utuh. Hal serupa berlaku untuk _number of clicks_ di mana pengguna tidak dapat mengklik setengah kali.
> - **Karakteristik Kontinu pada Continuous**: Untuk data kontinu seperti tinggi badan (_height_), rentang nilai di antara 150 cm dan 151 cm tidak kosong (_void_), melainkan terdapat probabilitas nilai desimal tak terhingga (seperti 150,5 cm atau 150,7 cm) bergantung pada tingkat ketelitian alat ukur. Hal ini juga berlaku untuk variabel usia (_age_) di mana waktu terus berjalan kontinu tanpa jeda kosong di antara ulang tahun ke-50 dan ke-51.
> - **Klarifikasi Istilah Nominal**: Dosen mengklarifikasi miskonsepsi istilah "nominal" dalam Bahasa Indonesia (yang sering kali diasosiasikan dengan jumlah uang, contoh: "nominal Rp10.000"). Dalam terminologi tipe data statistika internasional, **Nominal** murni berarti data kategorikal tanpa urutan tingkatan fisis (contoh: warna merah tidak memiliki tingkatan lebih tinggi atau lebih rendah dari warna biru).

**Contoh kode — klasifikasi variabel dengan pandas (`dtype` Python bukan otomatis sama dengan skala statistik, jadi tetap perlu penilaian manual):**

```python
import pandas as pd

df = pd.DataFrame({
    'gender': ['Male', 'Female', 'Male'],                      # Qualitative - Nominal
    'satisfaction': ['Puas', 'Biasa saja', 'Sangat puas'],      # Qualitative - Ordinal
    'number_of_rooms': [2, 3, 1],                               # Quantitative - Discrete
    'height_cm': [165.5, 172.3, 158.9]                          # Quantitative - Continuous
})

print(df.dtypes)
# gender               object   <- tipe Python, BUKAN otomatis "Nominal"
# satisfaction         object   <- tipe Python juga tidak tahu ini "Ordinal"
# number_of_rooms       int64   <- cocok dengan Discrete
# height_cm           float64   <- cocok dengan Continuous

# Pandas TIDAK tahu bahwa 'satisfaction' punya urutan logis (Biasa saja < Puas < Sangat puas).
# Untuk merepresentasikan sifat Ordinal secara eksplisit, gunakan CategoricalDtype:
from pandas.api.types import CategoricalDtype

urutan_kepuasan = CategoricalDtype(
    categories=['Buruk', 'Biasa saja', 'Puas', 'Sangat puas'],
    ordered=True
)
df['satisfaction'] = df['satisfaction'].astype(urutan_kepuasan)
print(df['satisfaction'] > 'Biasa saja')  # sekarang perbandingan urutan logis bisa dilakukan
```

---

### 2.3 Skala Pengukuran (Scale of Measurement)

#### A. Empat Tingkatan Skala Pengukuran

Skala pengukuran menentukan batasan matematis dan jenis operasi analisis yang diizinkan pada variabel. Terdapat empat tingkatan skala yang disusun secara hierarkis dari yang terendah hingga tertinggi:

1. **Nominal** — Skala pengukuran paling dasar yang hanya berfungsi untuk mengklasifikasikan (_classify_) data ke dalam kategori-kategori berbeda tanpa adanya jarak fisis (_distance_) maupun urutan logis (_order_).
2. **Ordinal** — Skala yang mengklasifikasikan data dan memiliki urutan atau peringkat tingkatan fisis (_order_) yang jelas, namun jarak (_distance_) antar nilai kategori tersebut tidak dapat diukur secara kuantitatif.
3. **[[Kamus & Cheatsheet (JCAIEH M1)#I|Interval]]** — Variabel kuantitatif di mana karakteristiknya diukur sepanjang nilai kontinu, memiliki urutan, serta memiliki jarak (_distance_) antar nilai yang konsisten dan dapat diukur.
    - Sifat mutlak: Tidak memiliki nilai nol mutlak (_non-absolute zero_), artinya nilai nol (0) tidak menunjukkan ketiadaan absolut dari variabel tersebut (contoh: suhu 0 derajat Celsius memiliki eksistensi dingin fisis dan suhu tetap dapat turun ke angka negatif).
    - Operasi perkalian atau pembagian tidak logis (_not sensible_) untuk dilakukan pada skala ini. Contoh: Suhu 40 derajat Celsius tidak menunjukkan tingkat panas dua kali lipat dari suhu 20 derajat Celsius.
4. **[[Kamus & Cheatsheet (JCAIEH M1)#R|Ratio]] (Rasio)** — Skala pengukuran tertinggi yang memenuhi seluruh kondisi skala interval dengan tambahan kepemilikan nilai nol mutlak (_absolute zero_). Nilai nol (0) menunjukkan ketiadaan mutlak dari variabel yang diukur.
    - Operasi perkalian atau pembagian logis (_sensible_) untuk dilakukan. Nilai rasio biasanya bernilai lebih besar dari nol. Contoh: Tinggi badan (_Height_ 180 cm). Tinggi badan 360 cm secara matematis merupakan dua kali lipat dari tinggi badan 180 cm. Jika tinggi badan bernilai 0 cm, artinya objek tersebut tidak memiliki eksistensi fisik.

#### B. Ringkasan Karakteristik Skala Pengukuran

| Scale | Classify | Order | Distance | Zero Type | Multiplication / Division |
|:--|:-:|:-:|:-:|:-:|:-:|
| **Nominal** | Yes | No | No | No | No |
| **Ordinal** | Yes | Yes | No | No | No |
| **Interval** | Yes | Yes | Yes | Non-Absolute | No |
| **Ratio** | Yes | Yes | Yes | Absolute | Yes |

> [!warning] Audio Insight — Interval vs Ratio: Temperature vs Height
> Dosen menekankan perbedaan fisis antara Interval dan Ratio menggunakan variabel _Temperature_ dan _Height_. Suhu 0 derajat Celsius masih ada fisisnya, sedangkan tinggi 0 cm atau berat badan 0 kg menandakan ketiadaan materi fisis dari objek tersebut. Nilai dari variabel rasio juga secara umum tidak dapat bernilai negatif (selalu lebih besar atau sama dengan nol), berbeda dengan variabel interval yang sangat memungkinkan bernilai negatif (seperti suhu udara di bawah nol derajat Celsius).

#### D. Fokus Klarifikasi: Interval vs Ratio (Uji Nol Absolut, langkah demi langkah)

Ini adalah salah satu pasangan konsep yang paling sering tertukar. Kuncinya: **jangan mulai dari "bisakah nilainya negatif?"** — mulai dari pertanyaan yang lebih mendasar.

**Urutan penalaran yang benar (jangan dibalik):**

1. **Pertanyaan PRIMER (tes nol absolut)**: Kalau nilai variabel ini = 0, apakah itu berarti "objek/kuantitas ini benar-benar TIDAK ADA / TIDAK PUNYA apa-apa"?
   - Jika **ya** → kandidat kuat **Ratio**.
   - Jika **tidak** (nol tetap punya eksistensi fisik) → **Interval**.
2. **Pertanyaan SEKUNDER (hanya sebagai pengecekan tambahan, bukan penentu utama)**: Apakah variabel ini SECARA MATEMATIS bisa bernilai negatif?
   - Skala Ratio *pada umumnya* tidak bisa negatif (karena nol sudah jadi batas bawah absolut — tidak ada "tinggi badan −5 cm").
   - Skala Interval *bisa* negatif (karena nol bukan batas mutlak — suhu bisa −5°C).

Perhatikan bahwa pertanyaan sekunder adalah **akibat** dari jawaban pertanyaan primer, bukan tes yang berdiri sendiri. Kesalahan umum adalah menyimpulkan langsung dari "variabel ini tidak pernah saya lihat bernilai negatif dalam praktik" menjadi "berarti nol-nya pasti tidak absolut" — ini terbalik. Sesuatu bisa saja "dalam praktik tidak pernah negatif" tapi tetap Interval, kalau nolnya bukan nol absolut (skor IQ adalah contohnya — lihat tabel di bawah).

| Variabel | Bisa negatif secara matematis? | Apakah 0 = ketiadaan total? | Skala | Alasan |
|:--|:-:|:-:|:-:|:--|
| Suhu (°Celsius/°Fahrenheit) | Ya | Tidak (0°C tetap ada suhunya) | **Interval** | 0 hanya titik kalibrasi historis (titik beku air), bukan "tidak ada suhu". |
| Tinggi badan (cm) | Tidak | Ya (0 cm = tidak ada objek) | **Ratio** | 0 cm berarti benar-benar tidak ada panjang untuk diukur. |
| Tahun kalender (Masehi) | Ya (contoh: 500 SM) | Tidak (tahun 0 bukan "waktu tidak ada") | **Interval** | Titik nol kalender adalah kesepakatan, bukan ketiadaan waktu absolut. |
| Skor IQ | Tidak (dalam praktik tidak pernah 0 atau negatif) | Tidak (skor 0 tidak berarti "kecerdasan nol mutlak") | **Interval** | Ini contoh penting: variabel yang *tidak pernah negatif dalam praktik* tetap bisa Interval, karena tes primernya (nol absolut) yang gagal, bukan tes sekundernya. |
| Saldo rekening bank (Rupiah) | Ya (bisa minus/utang) | Ya (Rp 0 = benar-benar tidak punya saldo) | **Ratio*** | *Catatan: umumnya diperlakukan sebagai Ratio karena Rp 0 = tidak ada uang, meskipun secara teknis saldo bisa minus (kasus edge, sering dibahas debat di literatur). |

**Kesimpulan praktis**: kalau ragu, **selalu tanya dulu apa arti fisis dari angka 0** sebelum menanyakan soal negatif. "Bisa negatif" hanyalah petunjuk pendukung yang muncul SETELAH kamu tahu jawaban soal nol absolut — bukan jalan pintas untuk menyimpulkan langsung.

```python
def klasifikasi_skala(nama_variabel: str, nol_berarti_tiada_absolut: bool) -> str:
    """
    Tes PRIMER untuk membedakan Interval vs Ratio: apakah nilai nol berarti
    ketiadaan absolut dari variabel tersebut?
    (Uji "bisa negatif" sengaja TIDAK dijadikan input utama fungsi ini,
    karena ia hanya akibat/turunan dari jawaban tes primer, bukan penentu.)
    """
    if nol_berarti_tiada_absolut:
        return f"{nama_variabel}: RATIO (nol = ketiadaan absolut)"
    else:
        return f"{nama_variabel}: INTERVAL (nol bukan ketiadaan absolut)"

print(klasifikasi_skala("Suhu Celsius", nol_berarti_tiada_absolut=False))   # -> INTERVAL
print(klasifikasi_skala("Tinggi Badan", nol_berarti_tiada_absolut=True))    # -> RATIO
print(klasifikasi_skala("Skor IQ", nol_berarti_tiada_absolut=False))        # -> INTERVAL (meski jarang/tidak pernah negatif!)
```

#### C. Representasi Konseptual Berbasis Kode

```python
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

---

## Bab 3 Berpikir Desain dalam Statistika (Design Thinking of Statistics)

### 3.1 Aspek Utama Desain Statistika (Key Aspects of Statistical Design)

#### A. Pendahuluan Berpikir Desain (Design Thinking)

- Berpikir desain dalam statistika berfokus pada perencanaan yang matang sebelum data dikumpulkan dan dianalisis untuk memastikan keandalan hasil akhir.
- Terdapat lima aspek penting yang harus dirancang dalam proses statistika agar data yang diperoleh relevan dan representatif.

#### B. Karakteristik Aspek Desain

| Aspek Desain | Deskripsi Singkat |
|:--|:--|
| **Type of Study** | Menentukan jenis studi yang sesuai, apakah berupa eksperimen aktif atau observasi pasif. |
| **Population and Sample** | Mengidentifikasi target utama penyelidikan dan menentukan bagian representatif yang akan diamati. |
| **Randomness** | Menjamin keacakan dalam pengambilan sampel untuk menghindari bias dan menyeimbangkan faktor pengganggu. |
| **Sampling** | Menerapkan metode pemilihan sampel yang sistematis dari populasi yang terdefinisi. |
| **Experimental** | Merancang kondisi pengujian terkontrol dengan memberikan perlakuan khusus pada objek penelitian. |

> [!tip] Audio Insight — Design sebagai fondasi mutlak
> Dosen menekankan bahwa sebelum melangkah ke tahap analisis atau pemodelan, perancangan desain (tahap _Design_) adalah fondasi mutlak yang menentukan validitas seluruh proses statistika berikutnya.

---

### 3.2 Jenis Penelitian (Type of Study)

#### A. Studi Eksperimental (Experimental Study)

- Peneliti melakukan intervensi aktif dengan menempatkan subjek penelitian ke dalam kondisi eksperimen tertentu yang disebut _Treatments_.
- Peneliti kemudian mengamati dampak atau hasil dari perlakuan tersebut pada variabel respon (_Response Variable_).
- Studi ini memiliki variabel penjelas (_Explanatory Variable_) sebagai faktor penyebab dan variabel respon sebagai hasil atau akibat.
- Contoh nyata: _A/B Testing_ pada desain antarmuka aplikasi atau situs web baru untuk meningkatkan tingkat konversi (_Conversion Rate_).

#### B. Studi Observasional (Observational Study)

- Peneliti bertindak pasif dengan hanya mengamati nilai dari variabel respon dan variabel penjelas dari subjek sampel tanpa memberikan perlakuan khusus atau melakukan intervensi apa pun.
- Contoh nyata: Survei sampel acak di Tempat Pemungutan Suara (TPS) untuk keperluan Hitung Cepat (_Quick Count_).

#### C. Perbandingan Karakteristik Studi

| Karakteristik | Studi Eksperimental (Experimental Study) | Studi Observasional (Observational Study) |
|:--|:--|:--|
| **Intervensi Peneliti** | Aktif memberikan perlakuan (_Treatment_). | Pasif, hanya mengamati kondisi alami. |
| **Variabel Penjelas** | Ditentukan dan dikontrol oleh peneliti. | Diukur secara alami tanpa manipulasi. |
| **Tujuan Utama** | Menguji hubungan sebab-akibat (_Causal Relationship_). | Menggambarkan asosiasi atau pola dalam data asli. |
| **Contoh Kasus** | _A/B Testing_ desain tata letak (_Layout_) baru aplikasi. | Pengumpulan sampel survei suara pemilu di lapangan. |

> [!warning] Audio Insight — Jangan langsung percaya selisih kecil
> - **Matriks Keberhasilan A/B Testing**: Dalam contoh _A/B Testing_, _Conversion Rate_ diposisikan sebagai variabel respon (_Response Variable_), sedangkan variasi desain (misalnya desain baru vs desain lama) adalah variabel penjelas (_Explanatory Variable_).
> - **Pembuktian Statistik**: Dosen menerangkan bahwa jika kelompok desain baru menunjukkan _Conversion Rate_ sedikit lebih tinggi (misalnya 20.2% dibandingkan desain lama yang bernilai 20.0%), perbedaan tersebut tidak boleh langsung dianggap sebagai bukti keberhasilan mutlak. Hal ini karena perbedaan kecil tersebut bisa terjadi akibat faktor kebetulan. Statistika diperlukan untuk mengonfirmasi signifikansi perbedaan tersebut secara konkret melalui pengujian hipotesis.

---

### 3.3 Populasi dan Sampel (Population and Sample)

#### A. Klasifikasi Populasi

| Tipe Populasi | Karakteristik | Contoh |
|:--|:--|:--|
| **Finite Population** | Populasi terbatas yang anggotanya dapat didaftarkan dan dihitung secara fisik. | Jumlah mahasiswa aktif di Purwadhika, jumlah kursi di dalam ruang kelas. |
| **Hypothetical Population** | Populasi abstrak yang muncul dari fenomena berkelanjutan yang sedang dipertimbangkan. | Total produksi bola lampu sebuah pabrik jika terus menggunakan peralatan, metode, dan bahan baku yang sama. |

#### B. Konsep Parameter dan Statistik

- **Parameter**: Ringkasan numerik yang menggambarkan karakteristik populasi. Nilai parameter populasi umumnya tidak diketahui secara pasti karena keterbatasan pengukuran menyeluruh.
- **Statistik**: Ringkasan numerik yang dihitung dari data sampel yang diambil dari populasi. Statistik sampel digunakan sebagai estimasi untuk menarik kesimpulan (_Inference_) mengenai parameter populasi.

#### C. Rasionalisasi Penggunaan Sampel

Sampel adalah bagian dari populasi yang diamati langsung untuk merepresentasikan keseluruhan populasi. Penggunaan sampel sangat krusial karena adanya keterbatasan dalam tiga faktor utama:

- **Resource**: Keterbatasan sumber daya manusia dan peralatan pengumpul data.
- **Time**: Keterbatasan waktu pengerjaan studi.
- **Cost**: Biaya tinggi yang dibutuhkan jika harus mengukur seluruh populasi.

> [!tip] Audio Insight — Analogi tes darah dan memasak
> - **Analogi Tes Darah**: Dosen memberikan analogi bahwa ketika dokter ingin menguji kondisi kesehatan pasien melalui darah, dokter hanya mengambil beberapa mililiter sampel darah pasien (sampel), bukan menguras seluruh darah dari tubuh pasien (populasi).
> - **Analogi Memasak**: Ketika seseorang sedang memasak sayur, ia cukup mencicipi satu sendok kecil kuah (sampel) untuk mengetahui rasa masakan tersebut, tanpa perlu memakan seluruh isi panci (populasi).
> - **Keterwakilan Sampel**: Jika sampel diambil dengan metodologi yang baik sehingga bersifat representatif, maka rata-rata sampel (_Sample Mean_) dapat menggambarkan rata-rata populasi (_Population Mean_), dan median sampel (_Sample Median_) dapat menggambarkan median populasi (_Population Median_).

---

### 3.4 Metodologi Pengambilan Sampel (Sampling Methods)

#### A. Prinsip Sampling & Sampling Bias

- **Sampling Frame**: Representasi fisik atau daftar seluruh anggota populasi yang dapat diakses untuk diambil sampelnya.
- **[[Kamus & Cheatsheet (JCAIEH M1)#S|Sampling Bias]]**: Kesalahan dalam pengumpulan sampel yang mengakibatkan sampel tidak representatif terhadap populasi, sehingga kesimpulan yang ditarik menjadi menyimpang.

> [!warning] Audio Insight — Bias pinggiran gosong dan kasus rumah sakit
> - **Analogi Pinggiran Gosong**: Dosen memberikan ilustrasi bias ketika mencicipi masakan istri yang baru matang hanya pada bagian pinggir panci yang kebetulan gosong. Hal ini memicu kesimpulan bias bahwa seluruh masakan terasa pahit, padahal bagian tengahnya matang dengan sempurna.
> - **Kasus Data Rumah Sakit (Penyakit Jantung)**: Data fiktif dari sebuah rumah sakit menunjukkan proporsi penderita penyakit jantung pada usia muda (di bawah 50 tahun) mencapai 88.8%, jauh lebih tinggi dibanding usia di atas 50 tahun yang hanya 57.8%. Secara medis hal ini tidak logis.
> - **Penyebab Bias Kasus Rumah Sakit**: Bias terjadi karena data tidak dikumpulkan secara acak (_Randomly_). Anak muda memiliki tingkat kesadaran kesehatan yang lebih rendah dan umumnya hanya datang ke rumah sakit jika sudah merasakan gejala penyakit yang parah (sehingga probabilitas terdeteksi sakit jantung sangat tinggi saat diperiksa). Sebaliknya, orang tua memiliki kesadaran tinggi untuk rutin melakukan pemeriksaan kesehatan (_Medical Check-Up_) secara berkala terlepas dari apakah mereka merasa sakit atau tidak. Data tersebut adalah bagian dari populasi namun tidak representatif.

#### B. Teknik Sampling Probabilitas

| Metode Sampling | Karakteristik Operasional | Contoh Kasus |
|:--|:--|:--|
| **[[Kamus & Cheatsheet (JCAIEH M1)#S|Simple Random Sample]]** | Setiap anggota populasi memiliki peluang yang sama besar untuk terpilih secara acak murni. | Mengundi nomor induk mahasiswa untuk survei kepuasan. |
| **Systematic Sample** | Anggota sampel dipilih berdasarkan interval numerik tertentu setelah titik awal acak ditetapkan. | Memilih setiap orang ke-10 yang mendaftar pada platform digital. |
| **[[Kamus & Cheatsheet (JCAIEH M1)#S|Stratified Sample]]** | Populasi dibagi ke dalam kelompok-kelompok homogen yang saling lepas (_Strata_), kemudian sampel acak diambil dari setiap kelompok. | Membagi populasi berdasarkan tingkat pendidikan (SD, SMP, SMA, S1) lalu mengambil sampel secara acak dari tiap tingkatan tersebut. |
| **[[Kamus & Cheatsheet (JCAIEH M1)#C|Cluster Sample]]** | Populasi dibagi ke dalam kelompok-kelompok heterogen (_Clusters_) berdasarkan geografis, lalu beberapa kluster dipilih secara acak untuk disensus. | Memilih beberapa Tempat Pemungutan Suara (TPS) secara acak dari berbagai kecamatan untuk mewakili suara satu kota. |

> [!tip] Audio Insight — Cluster Sampling dan "kandang suara" pada Quick Count
> Metode _Cluster Sampling_ sangat sering digunakan dalam hitung cepat pemilu. Di lapangan, sering kali terdapat TPS tertentu yang merupakan basis kekuatan atau "kandang" dari calon tertentu yang sangat dominan. Jika peneliti menggunakan acak sederhana tanpa klusterisasi geografis, ada risiko sampel yang terpilih menumpuk pada TPS dominan tersebut sehingga hasilnya bias. Dengan _Cluster Sampling_, peneliti dipaksa mengambil sampel dari berbagai kluster geografis yang terpisah (kecamatan atau kelurahan berbeda) untuk menjaga keterwakilan data secara nasional.

**Contoh kode — mempraktikkan keempat metode sampling dengan pandas/numpy:**

```python
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'id_mahasiswa': range(1, 101),
    'jurusan': np.random.choice(['Data Science', 'AI Engineering', 'Web Dev'], size=100),
    'kota': np.random.choice(['Jakarta', 'Bandung', 'Surabaya', 'Medan'], size=100)
})

# 1. Simple Random Sample: setiap baris punya peluang sama untuk terpilih
simple_random = df.sample(n=10, random_state=42)

# 2. Systematic Sample: titik awal acak, lalu ambil tiap baris ke-10 setelahnya
start = np.random.randint(0, 10)
systematic = df.iloc[start::10]

# 3. Stratified Sample: ambil proporsi sampel yang SAMA dari tiap kelompok 'jurusan'
stratified = df.groupby('jurusan', group_keys=False).apply(
    lambda grup: grup.sample(frac=0.1, random_state=42)
)

# 4. Cluster Sample: pilih beberapa 'kota' (cluster) secara acak, lalu ambil SEMUA anggotanya
kota_terpilih = np.random.choice(df['kota'].unique(), size=2, replace=False)
cluster_sample = df[df['kota'].isin(kota_terpilih)]

print("Simple random  :", len(simple_random), "baris")
print("Systematic     :", len(systematic), "baris")
print("Stratified     :", len(stratified), "baris")
print("Cluster        :", len(cluster_sample), "baris, dari kota:", list(kota_terpilih))
```

---

### 3.5 Desain Eksperimen yang Baik (Experimental Design)

#### A. Unsur Dasar Eksperimen

Eksperimen yang dirancang dengan baik harus memenuhi tiga pilar utama berikut:

- **Control Comparison Group**: Adanya kelompok kontrol yang menerima perlakuan standar atau plasebo sebagai dasar pembanding untuk mengukur efektivitas perlakuan baru.
- **Randomization**: Alokasi unit eksperimental ke kelompok perlakuan secara acak untuk menyeimbangkan efek dari variabel pengganggu yang tidak terkontrol (_Lurking Variables / Covariates_).
- **Blinding**: Penyamaran subjek atau peneliti agar tidak mengetahui perlakuan mana yang diberikan, guna menghindari bias subjektif selama proses penilaian.

#### B. Kasus Uji A/B Testing

Sebuah platform belanja digital (_Marketplace_) menguji efektivitas desain antarmuka aplikasi baru untuk melihat pengaruhnya terhadap _Conversion Rate_. Skema eksperimen dijalankan sebagai berikut:

| Parameter Eksperimen | Detail Implementasi Kasus |
|:--|:--|
| **Subject / Experimental Unit** | Pengguna baru yang terdaftar di platform (_People_). |
| **Total Sampel Pengguna** | 240 pengguna baru yang dipilih secara acak. |
| **Kelompok Kontrol (Control Group)** | 122 pengguna yang diarahkan ke desain lama (Layout A). |
| **Kelompok Perlakuan (Treatment Group)** | 118 pengguna yang diarahkan ke desain baru (Layout B). |
| **Variabel Respon (Response Variable)** | _Conversion Rate_ (proporsi pengguna yang melakukan pembelian). |

> [!tip] Audio Insight — Randomisasi menyeimbangkan Covariates
> Dengan membagi 240 pengguna tersebut secara acak (_Randomly_) ke dalam kelompok Layout A (122 pengguna) dan Layout B (118 pengguna), efek dari variabel pengganggu (_Covariates_) seperti faktor usia, jenis kelamin, latar belakang pekerjaan, maupun perangkat yang digunakan akan terbagi rata dan seimbang di antara kedua kelompok. Hal ini memastikan bahwa perbedaan performa _Conversion Rate_ akhir benar-benar disebabkan oleh perbedaan desain antarmuka, bukan karena ketidakseimbangan karakteristik bawaan pengguna.

#### C. Representasi Konseptual Berbasis Kode

```python
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

---

## Bab 4 Statistika Deskriptif (Descriptive Statistics)

### 4.1 Definisi Ringkasan Deskriptif

#### A. Fondasi Konseptual

- **Descriptive Statistics** merupakan kegiatan yang mencakup pengorganisasian, perangkuman, dan penggambaran karakteristik utama dari data yang dimiliki tanpa tujuan untuk melakukan prediksi atau generalisasi ke populasi yang lebih luas.
- Metode desktriptif ini diimplementasikan melalui pembuatan grafik, diagram, tabel, serta penghitungan berbagai ukuran deskriptif numerik seperti nilai rata-rata, variasi, dan persentil.

> [!tip] Audio Insight — Tujuan utama Descriptive Statistics
> Dosen menekankan bahwa tujuan utama dari **Descriptive Statistics** adalah mendeskripsikan data secara akurat menggunakan grafik, chart, tabel, serta perhitungan ukuran deskriptif (seperti _average_, _variation_, dan _percentile_) agar pola internal data dapat terbaca dengan mudah sebelum melangkah ke analisis inferensial yang lebih kompleks.

---

### 4.2 Ukuran Pemusatan Data (Measures of Central Tendency)

#### A. Karakteristik dan Metodologi

**[[Kamus & Cheatsheet (JCAIEH M1)#C|Measures of Central Tendency]]** adalah cara mendeskripsikan posisi sentral atau titik tengah dari distribusi frekuensi suatu kelompok data.

| Ukuran Pemusatan | Cara Penghitungan / Karakteristik | Relevansi dan Sensitivitas Terhadap Data |
|:--|:--|:--|
| **[[Kamus & Cheatsheet (JCAIEH M1)#M|Mean]]** (Rata-rata) | Jumlah seluruh nilai observasi dibagi dengan total jumlah observasi. | Sangat cocok untuk variabel kuantitatif dengan distribusi simetrik (_symmetric distribution_). Sangat sensitif terhadap pencilan (_[[Kamus & Cheatsheet (JCAIEH M1)#O|outliers]]_). |
| **[[Kamus & Cheatsheet (JCAIEH M1)#M|Median]]** (Nilai Tengah) | Nilai tengah dari daftar data yang telah diurutkan dari terkecil ke terbesar. Posisi median dicari dengan formula `(n + 1) / 2`. | Sangat cocok untuk data dengan distribusi tidak simetrik atau miring (_[[Kamus & Cheatsheet (JCAIEH M1)#S|skewed distribution]]_) karena tidak terpengaruh oleh pencilan (_outliers_). |
| **[[Kamus & Cheatsheet (JCAIEH M1)#M|Mode]]** (Modus) | Nilai dari variabel kualitatif atau kuantitatif terhitung (_countable_) yang frekuensi kemunculannya paling sering. | Sangat cocok untuk mengidentifikasi pusat data kualitatif/kategorikal. Sulit diterapkan pada variabel kontinu yang sangat presisi karena setiap nilai cenderung unik. |

> [!warning] Audio Insight — Analogi kesenjangan gaji (Mean vs Median) dan deteksi Skewness
> - **Kondisi Penggunaan Modus pada Data Kontinu**: Dosen menjelaskan bahwa modus sangat tidak cocok untuk data kuantitatif kontinu yang bernilai presisi tinggi (misalnya data tinggi badan dengan beberapa angka desimal di belakang koma, seperti `160.1234` cm). Hal ini dikarenakan data tersebut cenderung unik sehingga kemunculannya hampir selalu satu kali. Modus baru dapat digunakan pada data tersebut jika datanya dikelompokkan terlebih dahulu ke dalam kategori interval (misalnya kategori interval `160 - 170` cm, `170 - 180` cm).
> - **Analogi Skewness Pendapatan (Mean vs Median)**: Dosen memberikan contoh konkret mengenai bias penggunaan rata-rata pada data pendapatan warga di negara dengan kesenjangan sosial yang sangat tinggi (_highly skewed_).
>     - Jika ada 10 orang dengan pendapatan berkisar di angka normal `7 - 9` juta rupiah, namun ada 1 orang yang memiliki pendapatan luar biasa sebesar `100` juta rupiah, maka nilai rata-rata (_mean_) akan melonjak naik ke atas dan tidak representatif bagi mayoritas kelompok tersebut.
>     - Sebaliknya, nilai tengah (_median_) tidak akan terpengaruh oleh satu nilai ekstrem (`100` juta) karena posisi tengahnya tetap konsisten berada di kisaran angka `7 - 9` juta rupiah. Oleh karena itu, untuk data miring (_skewed_), median merupakan representasi pusat data yang jauh lebih andal.
> - **Deteksi Skewness Melalui Deviasi Mean dan Median**: Perbedaan nilai yang jauh antara _mean_ dan _median_ di dalam suatu studi ilmiah sering kali digunakan sebagai indikator awal bahwa sebaran data tersebut tidak simetris (_skewed_) dan mengandung banyak pencilan (_outliers_).
> - **Modus untuk Data Kualitatif**: Modus sangat efektif sebagai ukuran pemusatan data kategorikal (non-angka). Dosen memberikan contoh riil mengenai pencarian merek mobil terpopuler di Jakarta dari data `1` juta unit kendaraan. Melalui penghitungan frekuensi, ditemukan `500.000` unit merek Toyota dan `300.000` unit merek Daihatsu. Dengan demikian, modus dari variabel kualitatif merek mobil tersebut adalah Toyota.

> [!tip] Analogi ini juga menjelaskan arah Box Plot
> Analogi "10 karyawan reguler bergaji 7-9 juta vs 1 direktur bergaji 100 juta" ini persis konsep yang sama dengan arah kemiringan (_skew_) pada [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]] Bab 3.2 ([[Kamus & Cheatsheet (JCAIEH M1)#B|Box Plot]]). Mayoritas data (karyawan) menumpuk rendah, tapi ekor ditarik ke kanan oleh minoritas ekstrem (direktur) — inilah **[[Kamus & Cheatsheet (JCAIEH M1)#R|right-skewed]]**. Lihat penjelasan lengkapnya di sana.

**Contoh kode — membuktikan analogi gaji karyawan vs direktur secara langsung:**

```python
import pandas as pd

# 8 "karyawan reguler" (7-9.5 juta) + 1 "direktur" (100 juta) = highly skewed
gaji_tim = pd.Series([7, 7, 7.5, 8, 8, 8.5, 9, 9.5, 100])  # dalam juta rupiah

print("Mean  :", gaji_tim.mean())     # ~18.28 juta -> DITARIK NAIK oleh outlier, tidak representatif
print("Median:", gaji_tim.median())   # 8.0 juta    -> tahan terhadap outlier, mewakili mayoritas
print("Mode  :", gaji_tim.mode()[0])  # 7.0 juta    -> nilai yang paling sering muncul

# Kesimpulan: median (8 juta) jauh lebih mewakili "gaji tipikal tim" ini
# dibanding mean (18.28 juta) yang sudah terdistorsi oleh 1 gaji direktur.
```

**Contoh kode — mode untuk data kategorikal (kasus merek mobil terpopuler):**

```python
import pandas as pd

merek_mobil = pd.Series(['Toyota'] * 500000 + ['Daihatsu'] * 300000 + ['Honda'] * 200000)
print(merek_mobil.mode()[0])       # 'Toyota'
print(merek_mobil.value_counts()) # menampilkan frekuensi tiap merek, Toyota di posisi teratas
```

---

### 4.3 Ukuran Penyebaran Data (Measures of Spread / Variability)

#### A. Karakteristik dan Metodologi

**Measures of Spread** digunakan untuk merangkum kelompok data dengan menggambarkan seberapa jauh sebaran data tersebut dari pusatnya. Memahami variabilitas sangat krusial karena dua kelompok data dapat memiliki nilai pusat yang sama namun memiliki tingkat keragaman yang berbeda jauh.

| Ukuran Penyebaran | Deskripsi Metodologis | Karakteristik Utama |
|:--|:--|:--|
| **[[Kamus & Cheatsheet (JCAIEH M1)#R|Range]]** (Rentang) | Selisih antara nilai observasi terbesar (_maximum_) dan terkecil (_minimum_). Formula: `Range = Max - Min`. | Sangat sederhana namun terlalu sensitif terhadap nilai ekstrem (_overly sensitive to extreme values_). |
| **[[Kamus & Cheatsheet (JCAIEH M1)#P|Percentile]]** (Persentil) | Nilai di mana suatu persentase tertentu `p` dari observasi berada pada atau di bawah nilai tersebut. | Membagi distribusi menjadi 100 bagian yang sama untuk menentukan posisi relatif data. |
| **[[Kamus & Cheatsheet (JCAIEH M1)#Q|Quartile]]** (Kuartil) | Kasus khusus dari persentil yang membagi data terurut menjadi 4 bagian sama besar. | Terdiri dari `Q1` (persentil 25), `Q2` (persentil 50 / Median), dan `Q3` (persentil 75). |
| **[[Kamus & Cheatsheet (JCAIEH M1)#I|Interquartile Range]]** (IQR) | Jarak antara kuartil atas (_third quartile_) dan kuartil bawah (_first quartile_). Formula: `IQR = Q3 - Q1`. | Digunakan untuk menggantikan simpangan baku pada data miring dan mendeteksi pencilan (_outliers_). |
| **[[Kamus & Cheatsheet (JCAIEH M1)#S|Standard Deviation]]** (Simpangan Baku) | Akar kuadrat dari varians, menunjukkan rata-rata penyimpangan absolute data dari nilai rata-ratanya (_mean_). | Sering digunakan bersama _mean_ untuk data berdistribusi simetris (_symmetric distribution_). Sangat dipengaruhi oleh pencilan. |

> [!tip] Audio Insight — Kenapa spread penting: dua negara, gaji rata-rata sama
> - **Ilustrasi Kebutuhan Analisis Spread**: Dosen memberikan simulasi tentang pentingnya melihat ukuran penyebaran di samping ukuran pemusatan.
>     - Dua negara memiliki rata-rata gaji yang sama, yaitu `10` juta rupiah.
>     - Negara A memiliki rentang (_range_) gaji yang sempit, yaitu hanya berkisar antara `9` juta hingga `11` juta rupiah. Distribusi pendapatan di Negara A ini sangat merata.
>     - Negara B memiliki rata-rata yang sama (`10` juta rupiah), tetapi rentang (_range_) gajinya sangat lebar, yaitu dari `1` juta hingga `100` juta rupiah. Kesenjangan sosial di Negara B ini sangat tinggi.
>     - Jika peneliti hanya menyajikan nilai rata-rata saja tanpa menyertakan ukuran penyebaran (_measures of spread_), informasi kesenjangan yang sangat penting tersebut akan hilang sepenuhnya.
> - **Analogi Persentil Nilai Siswa**: Dosen memberikan analogi bahwa apabila seorang siswa berada pada persentil ke-75 dari 100 siswa, hal ini menunjukkan bahwa nilai siswa tersebut setara atau lebih tinggi dari 75% siswa lainnya di dalam kelompok tersebut.

**Contoh kode — Negara A vs Negara B, mean sama tapi spread beda jauh:**

```python
import pandas as pd

negara_a = pd.Series([9, 9.5, 10, 10, 10.5, 11])          # rentang sempit, merata
negara_b = pd.Series([1, 3, 8, 12, 20, 100])                # rentang sangat lebar, timpang

print("Mean Negara A:", negara_a.mean(), "| Std Negara A:", round(negara_a.std(), 2))
print("Mean Negara B:", negara_b.mean(), "| Std Negara B:", round(negara_b.std(), 2))
# Mean keduanya identik/mirip (~10), tapi Std Negara B jauh lebih besar
# -> membuktikan mean saja TIDAK CUKUP untuk menceritakan kondisi ekonomi riil.
```

---

### 4.4 Deteksi Pencilan dan Estimasi Standar Deviasi Berbasis IQR

#### A. Rumus Deteksi Outlier (The 1.5 x IQR Rule)

_Interquartile Range_ (IQR) memiliki peran penting dalam mendeteksi adanya data pencilan (_outliers_). Batas toleransi nilai normal ditentukan menggunakan aturan konstanta `1.5`:

- Batas Bawah (_Lower Bound_) = `Q1 - 1.5 x IQR`
- Batas Atas (_Upper Bound_) = `Q3 + 1.5 x IQR`

Setiap titik data yang nilainya jatuh di bawah batas bawah atau di atas batas atas secara matematis diklasifikasikan sebagai **Outlier**.

Selain itu, jika data terdistribusi secara normal, simpangan baku (_standard deviation_) dapat diestimasi secara aproksimasi dari nilai IQR menggunakan formula:

- `S = 1.34898 x IQR`

#### Fokus Klarifikasi: IQR itu sendiri vs Aturan 1.5×IQR (dua rumus berbeda, jangan dicampur)

Ini pasangan formula yang gampang tertukar karena namanya mirip. Sebenarnya ini adalah **dua langkah terpisah** yang berurutan:

**Langkah 1 — Menghitung IQR (ini murni tentang UKURAN LEBAR sebaran data, belum menyinggung outlier sama sekali):**

$$IQR = Q3 - Q1$$

IQR di titik ini HANYA sebuah angka tunggal yang menyatakan "seberapa lebar 50% data bagian tengah". Tidak ada angka `1.5` yang terlibat sama sekali di langkah ini.

**Langkah 2 — BARU SETELAH punya angka IQR, kita pakai angka itu untuk membuat pagar batas outlier, dengan mengalikannya dengan konstanta 1.5 (aturan terpisah, ditempelkan DI ATAS hasil langkah 1):**

$$\text{Lower Bound} = Q1 - (1.5 \times IQR) \qquad \text{Upper Bound} = Q3 + (1.5 \times IQR)$$

Jadi `1.5 × IQR` **bukan bagian dari definisi/rumus IQR itu sendiri** — ia adalah aturan tambahan (konvensi Tukey) yang HANYA dipakai ketika tujuannya adalah mendeteksi outlier. Kalau kamu hanya ingin tahu "seberapa lebar sebaran data", cukup `Q3 - Q1` saja, titik, tanpa `1.5`.

```python
import pandas as pd

age = pd.Series([22, 22, 23, 23, 24, 27, 28, 29])

# LANGKAH 1: hitung IQR -> murni ukuran lebar sebaran, TIDAK melibatkan angka 1.5 sama sekali
q1 = age.quantile(0.25)
q3 = age.quantile(0.75)
iqr = q3 - q1
print("IQR (lebar sebaran saja):", iqr)  # 4.5  <- ini SUDAH final sebagai definisi IQR

# LANGKAH 2: BARU sekarang pakai IQR itu untuk membuat pagar outlier (rumus TERPISAH, pakai 1.5x)
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print("Lower Bound (pagar outlier):", lower_bound)  # 16.0
print("Upper Bound (pagar outlier):", upper_bound)  # 34.0

# IQR TETAP 4.5 -- angka itu tidak pernah berubah menjadi 6.75.
# Yang menjadi 6.75 adalah HASIL PERKALIAN 1.5 x IQR, sebuah angka BARU dan TERPISAH
# yang dipakai untuk menghitung pagar, bukan IQR itu sendiri.
print("1.5 x IQR (angka bantu, BUKAN IQR):", 1.5 * iqr)  # 6.75
```

---

### B. Studi Kasus Perhitungan Manual Berbasis Contoh Modul

Berdasarkan data usia pasien dari modul yang berjumlah `8` observasi (data telah diurutkan): `22, 22, 23, 23, 24, 27, 28, 29`

Langkah-langkah penghitungan deskriptif numerik:

1. **Mean**: `(22 + 22 + 23 + 23 + 24 + 27 + 28 + 29) / 8 = 24.75` tahun.
2. **Median (Q2)**: Karena jumlah observasi genap (`n = 8`), median diperoleh dari rata-rata dua nilai tengah (data ke-4 dan data ke-5): `(23 + 24) / 2 = 23.5` tahun.
3. **Kuartil 1 (Q1)**: Diperoleh nilai sebesar `22.75` tahun.
4. **Kuartil 3 (Q3)**: Diperoleh nilai sebesar `27.25` tahun.
5. **IQR**: `IQR = Q3 - Q1 = 27.25 - 22.75 = 4.5` tahun.
6. **Range**: `Range = Max - Min = 29 - 22 = 7` tahun.
7. **Standard Deviation (s)**: Diperoleh nilai sebesar `2.63391` tahun.

> [!warning] Audio Insight — Simulasi penghitungan bersama mahasiswa (Rainer)
> Dosen menuntun mahasiswa (_Rainer_) secara langsung untuk menghitung batas pencilan dari data usia pasien tersebut:
> - Nilai pengali konstanta: `1.5 x IQR = 1.5 x 4.5 = 6.75` tahun.
> - Penghitungan Batas Bawah: `Q1 - 6.75 = 22.75 - 6.75 = 16.00` tahun.
> - Penghitungan Batas Atas: `Q3 + 6.75 = 27.25 + 6.75 = 34.00` tahun.
> - **Kesimpulan Analisis**: Karena nilai observasi usia pasien terkecil adalah `22` tahun (masih di atas `16.00`) dan usia terbesar adalah `29` tahun (masih di bawah `34.00`), maka secara matematis disimpulkan **tidak ada outlier** di dalam dataset pasien tersebut.

> [!tip] Nuansa teknis: hasil `.std()` pandas bisa berbeda dari perhitungan manual modul
> Nilai `2.63391` pada langkah 7 di atas dihitung menggunakan formula **simpangan baku populasi** (pembagi `n`), bukan simpangan baku sampel (pembagi `n-1`). Perhatikan bahwa `pandas.Series.std()` **secara default menggunakan `ddof=1` (pembagi n-1, gaya sampel)**, sehingga hasilnya akan sedikit berbeda dari `2.63391` kecuali kamu eksplisit set `ddof=0`. Ini detail kecil yang gampang bikin bingung saat mencocokkan hasil kode dengan hitungan manual di modul — lihat pembuktian di kode di bawah.

**Contoh kode — replikasi penuh studi kasus usia pasien, termasuk isu `ddof`:**

```python
import pandas as pd

age = pd.Series([22, 22, 23, 23, 24, 27, 28, 29])

print("Mean         :", age.mean())                    # 24.75
print("Median       :", age.median())                  # 23.5
print("Q1           :", age.quantile(0.25))             # 22.75
print("Q3           :", age.quantile(0.75))             # 27.25
print("IQR          :", age.quantile(0.75) - age.quantile(0.25))  # 4.5
print("Range        :", age.max() - age.min())          # 7

print("Std (sample, ddof=1, DEFAULT pandas):", age.std())        # ~2.8156 (BEDA dari modul!)
print("Std (population, ddof=0, sesuai modul):", age.std(ddof=0))  # ~2.6339 (COCOK dengan modul)

lower_bound = age.quantile(0.25) - 1.5 * (age.quantile(0.75) - age.quantile(0.25))
upper_bound = age.quantile(0.75) + 1.5 * (age.quantile(0.75) - age.quantile(0.25))
outliers = age[(age < lower_bound) | (age > upper_bound)]
print("Lower/Upper Bound:", lower_bound, "/", upper_bound)  # 16.0 / 34.0
print("Outliers ditemukan:", list(outliers))                # [] -> kosong, tidak ada outlier
```

---

### 4.5 Representasi Konseptual Berbasis Kode

#### A. Pemodelan Statistika Deskriptif dalam Python

Dalam ekosistem pemrograman Python, seluruh perhitungan ringkasan statistika deskriptif di atas dapat dipanggil secara instan menggunakan library _Pandas_ melalui fungsi `.describe()`. Lihat juga [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] untuk penjelasan lengkap method-method Pandas ini.

```python
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

---

## Bab 5 Distribusi Normal (Normal Distribution)

### 5.1 Definisi dan Karakteristik Distribusi Normal

#### A. Fondasi Konseptual

- **[[Kamus & Cheatsheet (JCAIEH M1)#N|Distribusi Normal]]**, juga dikenal sebagai **Gaussian Distribution**, adalah jenis distribusi probabilitas kontinu yang memiliki kurva kepadatan berbentuk lonceng (_bell-shaped curve_).
- Kurva kepadatan ini memiliki karakteristik utama sebagai berikut:
    - **Simetris**: Sisi kiri dan kanan kurva merupakan cerminan satu sama lain.
    - **Terpusat**: Kurva berpusat tepat pada nilai rata-rata (_mean_) dari dataset.
    - **Penyebaran**: Tingkat kelebaran atau kerampingan kurva sepenuhnya ditentukan oleh nilai simpangan baku (_standard deviation_).
    - **Frekuensi Data**: Data yang berada di dekat nilai rata-rata memiliki frekuensi kemunculan yang jauh lebih tinggi dibandingkan dengan data yang berada jauh dari nilai rata-rata.

> [!tip] Audio Insight — Mean = Median pada distribusi normal sempurna
> Dosen menjelaskan bahwa Distribusi Normal adalah salah satu konsep yang akan sangat sering ditemui di berbagai tempat, khususnya saat membahas topik statistika inferensial (_statistical inference_). Distribusi ini juga menjadi asumsi dasar dari banyak algoritma dalam bidang _Data Science_ dan _Machine Learning_. Pada kurva normal sempurna, posisi nilai rata-rata (_mean_) dan nilai tengah (_median_) berada tepat di tengah-tengah kurva simetris tersebut, sehingga nilai $Mean = Median$. Dalam praktik lapangan, data aktual jarang sekali mengikuti kurva normal secara sempurna (_perfectly normally distributed_). Namun, dosen menyatakan bahwa data tersebut masih dapat diasumsikan terdistribusi normal selama penyimpangan visualnya dari kurva teoritis tergolong sangat kecil atau tidak signifikan.

**Contoh kode — membangkitkan dan memvisualisasikan distribusi normal:**

```python
import numpy as np

np.random.seed(0)
tinggi_badan = np.random.normal(loc=170, scale=8, size=1000)  # mean=170cm, std=8cm, 1000 data

print("Mean simulasi  :", tinggi_badan.mean())    # mendekati 170
print("Median simulasi:", np.median(tinggi_badan)) # mendekati mean -> tanda distribusi simetris
print("Std simulasi   :", tinggi_badan.std())      # mendekati 8
```

---

### 5.2 Pentingnya Distribusi Normal

#### A. Relevansi Praktis dalam Data Science

- Banyak variabel dependen (_dependent variables_) di dalam populasi secara umum diasumsikan terdistribusi secara normal.
- Jika suatu variabel terbukti mendekati terdistribusi normal (_approximately normally distributed_), kita dapat dengan valid melakukan inferensi atau penarikan kesimpulan mengenai nilai-nilai dari variabel tersebut.
- Beberapa teknik pembersihan data (_data cleaning_) serta algoritma pembelajaran mesin (_machine learning_) memerlukan pemenuhan asumsi bahwa data masukan wajib terdistribusi secara normal.

> [!tip] Audio Insight — Transformasi data bersifat case-by-case
> Dosen menekankan bahwa dalam tahapan pemodelan _Machine Learning_, beberapa algoritma mengharuskan pemenuhan asumsi normalitas data. Apabila data aktual yang dimiliki ternyata miring (_skewed_) atau tidak normal, praktisi data harus melakukan penanganan khusus, salah satunya dengan menerapkan teknik transformasi data (_data transformation_) agar bentuk distribusinya bergeser mendekati normal. Penanganan ini bersifat sangat kontekstual (_case-by-case_); jika algoritma yang digunakan tidak mensyaratkan normalitas, maka transformasi data tidak perlu dilakukan.

**Contoh kode — transformasi logaritma sederhana pada data skewed:**

```python
import numpy as np
from scipy import stats

# Simulasi data pendapatan yang right-skewed (mirip analogi gaji karyawan vs direktur)
np.random.seed(1)
pendapatan_skewed = np.random.exponential(scale=10, size=500) + 5

print("Skewness sebelum transformasi:", stats.skew(pendapatan_skewed))   # nilai positif besar

pendapatan_log = np.log(pendapatan_skewed)  # transformasi logaritma natural
print("Skewness sesudah transformasi:", stats.skew(pendapatan_log))       # mendekati 0, lebih simetris
```

---

### 5.3 Aturan Empiris Simpangan Baku (Empirical Rule)

#### A. Aturan Persentase Distribusi Lonceng

Jika sebuah distribusi data terbukti berbentuk lonceng (_bell-shaped_), maka berlaku [[Kamus & Cheatsheet (JCAIEH M1)#E|aturan empiris]] (_empirical rule_) untuk menentukan proporsi penyebaran data sebagai berikut:

- Sekitar **68%** observasi jatuh di dalam rentang $\bar{x} - s$ hingga $\bar{x} + s$ (rata-rata plus-minus satu kali simpangan baku).
- Sekitar **95%** observasi jatuh di dalam rentang $\bar{x} - 2s$ hingga $\bar{x} + 2s$ (rata-rata plus-minus dua kali simpangan baku).
- Sekitar **99.7%** observasi jatuh di dalam rentang $\bar{x} - 3s$ hingga $\bar{x} + 3s$ (rata-rata plus-minus tiga kali simpangan baku).
- Simpangan baku dapat diestimasi secara kasar (_rough estimation_) dari persebaran data menggunakan rumus: $$s \approx \frac{\text{Rentang}}{4} = \frac{\text{Max} - \text{Min}}{4}$$

> [!warning] Audio Insight — Empirical Rule hanya berlaku pada data simetris
> Aturan persentase ini merupakan karakteristik mutlak yang hanya berlaku pada data yang simetris atau berbentuk lonceng. Pada distribusi data yang miring (_skewed_), persentase observasi yang jatuh pada rentang simpangan baku tersebut akan bergeser dan tidak akan mengikuti rasio 68%, 95%, dan 99.7% secara presisi karena konsentrasi data yang berat sebelah.

**Contoh kode — membuktikan Empirical Rule secara numerik:**

```python
import numpy as np

np.random.seed(0)
data = np.random.normal(loc=170, scale=8, size=10000)  # simulasi tinggi badan (cm)

mean = data.mean()
std = data.std()

dalam_1_std = np.sum((data > mean - std) & (data < mean + std)) / len(data)
dalam_2_std = np.sum((data > mean - 2*std) & (data < mean + 2*std)) / len(data)
dalam_3_std = np.sum((data > mean - 3*std) & (data < mean + 3*std)) / len(data)

print(f"Dalam 1 std (mean +/- s)  : {dalam_1_std:.1%}")   # mendekati 68%
print(f"Dalam 2 std (mean +/- 2s) : {dalam_2_std:.1%}")   # mendekati 95%
print(f"Dalam 3 std (mean +/- 3s) : {dalam_3_std:.1%}")   # mendekati 99.7%

# Estimasi kasar std dari range
estimasi_std = (data.max() - data.min()) / 4
print("Std asli   :", std)
print("Estimasi std dari range/4:", estimasi_std)  # perkiraan kasar, tidak selalu presisi
```

---

### 5.4 Uji Normalitas (Normality Assessment)

Metodologi pengujian untuk menentukan apakah suatu dataset dimodelkan dengan baik oleh Distribusi Normal terbagi menjadi dua pendekatan utama:

#### A. Metode Grafis (Graphical Methods)

| Alat Visualisasi | Cara Kerja dan Karakteristik Deteksi |
|:--|:--|
| **Histogram** | Visualisasi yang menampilkan distribusi frekuensi variabel tunggal secara cepat. Dilakukan dengan membandingkan diagram batang aktual sampel terhadap kurva lonceng teoritis merah. Jika penyimpangan batang aktual sangat minim, data dianggap normal. |
| **Box Plot** | Digunakan untuk mendeteksi non-normalitas sampel dengan melihat posisi garis median. Pada data simetris, median berada tepat di tengah kotak. Namun, deviasi pada kelebaran atau keruncingan kurva (_width/pointiness_) sangat sulit diidentifikasi secara visual hanya menggunakan alat ini. |
| **QQ Plot** | Singkatan dari _Quantile vs Quantile Plot_. Alat ini memplot kuantil teoretis terhadap kuantil aktual dari variabel. QQ Plot mampu menampilkan deviasi dari distribusi normal secara jauh lebih jelas dan sensitif dibandingkan Histogram atau Box Plot. |

> [!warning] Audio Insight — QQ Plot dan bahaya menghapus outlier fraud
> - **Karakteristik Visual QQ Plot**: Pada data yang berdistribusi normal, titik-titik plot akan berbaris merapat mengikuti garis lurus diagonal secara sempurna. Pada data miring ke kanan (_right-skewed_), titik plot akan melengkung melonjak di bagian kanan atas garis diagonal. Sebaliknya, pada data miring ke kiri (_left-skewed_), titik plot akan mencong dan melengkung di bagian kiri bawah garis diagonal.
> - **Pembersihan Outlier Berdasarkan Box Plot**: Dosen menjelaskan bahwa dalam siklus pengembangan _machine learning_, Box Plot sering dipakai untuk menyaring outlier (dengan formula batas luar $1.5 \times \text{IQR}$). Namun, penghapusan ini tidak boleh dilakukan sembarangan. Sebagai contoh, dalam kasus deteksi penipuan kartu kredit (_fraud detection_), transaksi fraud yang bersifat pencilan (hanya bernilai sekitar 0.5% hingga 1%) adalah data yang paling krusial untuk dipelajari. Jika data outlier tersebut dihapus, model tidak akan pernah bisa mendeteksi transaksi fraud.

Lihat [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]] Bab 3.1-3.2 untuk syntax lengkap membuat Histogram, Box Plot, dan QQ Plot.

**Contoh kode — QQ Plot dengan scipy dan matplotlib:**

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(2)
data_normal = np.random.normal(loc=0, scale=1, size=200)

stats.probplot(data_normal, dist="norm", plot=plt)
plt.title("QQ Plot - Data Normal")
plt.show()
```

#### B. Uji Hipotesis Formal (Frequentist Test)

| Nama Uji Statistik | Deskripsi Metodologi dan Batasan |
|:--|:--|
| **Kolmogorov-Smirnov Test (KS Test)** | Menghitung jarak supremum antara fungsi distribusi empiris sampel dengan distribusi teoretis normal. Memiliki kekuatan uji (_statistical power_) yang rendah, sehingga membutuhkan jumlah sampel yang sangat besar untuk menolak hipotesis nol, serta sangat sensitif terhadap pencilan (_outliers_). Nilai statistik KS akan bernilai 0 jika data mengikuti distribusi normal sempurna. |
| **Lilliefors Test** | Merupakan perbaikan langsung dari KS Test di mana rata-rata dan varians populasi diestimasi langsung dari sampel data alih-alih ditentukan oleh pengguna. Meskipun lebih baik dari KS Test, kekuatan statistiknya masih lebih rendah dibandingkan Shapiro-Wilk Test. |
| **Shapiro-Wilk Test** | Uji normalitas yang paling kuat (_most powerful test_). Dirancang secara eksklusif khusus untuk Distribusi Normal dan tidak dapat diaplikasikan untuk pengujian terhadap jenis distribusi probabilitas lainnya. |
| **D'Agostino and Pearson's Test** | Uji normalitas omnibus yang menggabungkan parameter kemiringan (_skewness_) dan keruncingan (_kurtosis_). Berlandaskan pada prinsip bahwa statistik uji akan berdistribusi Chi-Square dengan 2 derajat kebebasan (_degrees of freedom_) jika data terdistribusi normal. |

#### C. Aturan Interpretasi Nilai Probabilitas (P-Value)

Keputusan akhir untuk mengasumsikan normalitas data didasarkan pada ambang batas signifikansi nilai _P-Value_ sebagai berikut:

- **Jika P-Value > 0.05**: Kita mengasumsikan data terdistribusi normal (_assume a normal distribution_).
- **Jika P-Value < 0.05**: Kita tidak mengasumsikan data terdistribusi normal (_do not assume a normal distribution_).

> [!tip] Audio Insight — Uji frequentist jarang dipakai praktis di AI Engineering
> Dosen mengklarifikasi bahwa dalam kurikulum Bootcamp AI (terutama untuk jalur _AI Engineering_ yang berfokus pada teknologi _Generative AI_), uji statistik frequentist formal ini sangat jarang digunakan secara praktis di industri nyata. Praktisi di lapangan umumnya lebih mengandalkan visualisasi grafis (_Graphical Methods_) yang instan dan informatif untuk mendeteksi kelayakan distribusi data. Penjelasan uji frequentist ini disertakan agar mahasiswa memiliki pemahaman teoretis yang kuat dan tidak merasa asing saat istilah-istilah ini muncul dalam diskusi atau dokumentasi teknis lanjutan.

#### D. Representasi Konseptual Berbasis Kode

```python
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

**Contoh kode — implementasi NYATA (bukan konseptual) memakai `scipy.stats`, langsung bisa dijalankan:**

```python
from scipy import stats
import numpy as np

# Kasus 1: data yang memang normal
np.random.seed(1)
data_normal = np.random.normal(loc=50, scale=5, size=100)
stat_sw, p_sw = stats.shapiro(data_normal)
print(f"Shapiro-Wilk (data normal)  -> statistic={stat_sw:.4f}, p-value={p_sw:.4f}")

# Kasus 2: data yang jelas skewed (eksponensial)
data_skewed = np.random.exponential(scale=5, size=100)
stat_sw2, p_sw2 = stats.shapiro(data_skewed)
print(f"Shapiro-Wilk (data skewed)  -> statistic={stat_sw2:.4f}, p-value={p_sw2:.4f}")

for label, p in [("data_normal", p_sw), ("data_skewed", p_sw2)]:
    if p > 0.05:
        print(f"{label}: P-Value > 0.05 -> Asumsikan terdistribusi normal.")
    else:
        print(f"{label}: P-Value <= 0.05 -> JANGAN asumsikan terdistribusi normal.")

# Kolmogorov-Smirnov Test (membandingkan data dengan distribusi normal standar)
stat_ks, p_ks = stats.kstest(data_normal, 'norm', args=(data_normal.mean(), data_normal.std()))
print(f"KS Test -> statistic={stat_ks:.4f}, p-value={p_ks:.4f}")
```

---

## Bab 6 Ringkasan Grafis dalam Statistika Deskriptif (Graphical Summary)

### 6.1 Pemilihan Grafik Berdasarkan Tipe Variabel

#### A. Klasifikasi Visualisasi

Dalam statistika deskriptif, pemilihan jenis grafik atau diagram sangat bergantung pada tipe variabel yang sedang dianalisis. Pemilihan alat visualisasi yang tepat memastikan distribusi, komposisi, atau korelasi data dapat tersampaikan secara akurat.

| Tipe Variabel | Jenis Alat Visualisasi | Tujuan Utama Analisis |
|:--|:--|:--|
| **Numerical Variable** | Histogram, Boxplot, Scatterplot | Mengamati bentuk distribusi, mendeteksi pencilan, dan melihat tren atau korelasi antar variabel kuantitatif. |
| **Categorical Variable** | Pie Chart, Bar Plot | Mengamati komposisi, proporsi, atau perbandingan frekuensi antar kategori variabel kualitatif. |
| **Both Numerical & Categorical** | Bar Plot, Boxplot | Membandingkan nilai agregat kuantitatif atau membandingkan sebaran data numerik di berbagai kelompok kategori. |

> Bab ini adalah ringkasan singkat — penjelasan lengkap dan sintaks kode setiap jenis grafik (Histogram, Box Plot, Scatter Plot, Pie Chart, Bar Chart) ada di [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]] Bab 3.

### 6.2 Penjelasan Alat Visualisasi

#### A. Histogram

- Histogram adalah grafik yang merepresentasikan distribusi frekuensi data numerik secara akurat menggunakan batang tegak.
- Lebar dari setiap batang menunjukkan interval kelas data (_bin_), sedangkan tinggi batang mewakili frekuensi atau jumlah kejadian dari data yang berada di dalam interval tersebut.
- Melalui histogram, bentuk pola sebaran data dapat diidentifikasi secara cepat, apakah data tersebut simetris (terdistribusi normal), memiliki dua puncak (_bimodal_), miring ke kanan (_right-skewed_), miring ke kiri (_left-skewed_), atau merata (_uniform_).

> [!tip] Audio Insight — Cara sederhana membangun histogram dari data usia
> Dosen menjelaskan bahwa proses pembuatan histogram dilakukan secara sederhana dengan memetakan rentang data numerik ke dalam kategori interval tertentu (_bins_). Sebagai contoh nyata, jika terdapat rentang data usia pasien antara 0 hingga 20 tahun dengan frekuensi sebanyak 1 orang, interval 21 hingga 25 tahun dengan frekuensi sebanyak 8 orang, dan interval 26 hingga 30 tahun dengan frekuensi sebanyak 2 orang, maka data poin tersebut langsung diplot ke dalam grafik sesuai tinggi frekuensi masing-masing kelas intervalnya.

---

#### B. Box Plot

- Box Plot (atau juga dikenal dengan nama _Box-and-Whisker Plot_) adalah metode visualisasi grafis yang menggambarkan distribusi data numerik berdasarkan ringkasan lima angka (_five-number summary_): nilai minimum, kuartil pertama (Q1), median (Q2), kuartil ketiga (Q3), dan nilai maksimum.
- Visualisasi ini digambarkan dengan sebuah kotak persegi panjang (_box_) dari kuartil bawah hingga kuartil atas, sebuah garis pembatas horizontal di dalam kotak yang menunjukkan nilai median, serta garis perpanjangan (_whiskers_) ke arah luar kotak untuk menunjukkan batas nilai ekstrem non-pencilan.
- Alat ini sangat efektif untuk mendeteksi keberadaan data pencilan (_outliers_) yang divisualisasikan berupa titik-titik data yang terisolasi di luar batas maksimum atau minimum teoritis.

> [!tip] Audio Insight — Kelebihan dan keterbatasan Box Plot
> Dosen menekankan bahwa Box Plot merupakan teknik visualisasi yang sangat unggul untuk mendeteksi keberadaan pencilan secara instan. Meskipun Box Plot mampu membandingkan persebaran beberapa variabel atau kelompok secara sekaligus, alat ini memiliki keterbatasan dalam mengidentifikasi secara mendetail variasi kelancipan (_pointiness_) atau kelebaran puncak kurva jika dibandingkan dengan histogram.

> [!warning] Cara membaca arah skew dari posisi median di Box Plot — lihat [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]]
> Penjelasan lengkap dan langkah-demi-langkah untuk membaca arah kemiringan (_right-skewed_ vs _left-skewed_) dari posisi garis median di dalam kotak Box Plot — termasuk contoh angka konkret — ada di [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]] Bab 3.2 bagian "Fokus Klarifikasi". Ringkasannya: **median dekat Q1 (bawah) = right-skewed**, **median dekat Q3 (atas) = left-skewed**. Ini sering tertukar karena terasa berlawanan dengan intuisi — cek penjelasan detailnya di sana.

---

#### C. Scatter Plot

- Scatter Plot (Diagram Pencar) adalah grafik dua dimensi yang menampilkan titik-titik koordinat data untuk memvisualisasikan hubungan atau korelasi antara dua variabel kuantitatif.
- Setiap titik data pada diagram mewakili sepasang nilai dari sumbu horizontal (sumbu X) dan sumbu vertikal (sumbu Y).
- Titik-titik data pada diagram ini tidak dihubungkan oleh garis kontinu untuk menjaga representasi keunikan dari setiap observasi individu.
- Dalam bidang ilmu data (_Data Science_), diagram ini adalah alat fundamental untuk mendeteksi arah korelasi (positif, negatif, atau tidak ada korelasi) serta kekuatan hubungan linear antara dua variabel kuantitatif.

> [!tip] Audio Insight — Contoh nyata: total tagihan vs tip restoran
> Sebagai contoh kasus nyata penerapan Scatter Plot, dosen mencontohkan analisis hubungan antara variabel total tagihan (_total bill_) dengan variabel jumlah tip yang diberikan oleh pelanggan di restoran. Melalui scatter plot, kita dapat dengan mudah membaca kecenderungan atau tren di mana pelanggan yang memiliki total tagihan makanan lebih besar cenderung memberikan tip dengan jumlah yang lebih tinggi pula.

---

#### D. Pie Chart

- Pie Chart (Diagram Lingkaran) adalah visualisasi berbentuk lingkaran yang dibagi menjadi beberapa sektor/irisan untuk menunjukkan proporsi persentase atau komposisi dari masing-masing kategori pada variabel kualitatif.
- Luas atau sudut dari setiap irisan sebanding dengan nilai persentase frekuensi relatif dari kategori yang diwakilinya.
- Sifat dari masing-masing kategori dalam diagram ini harus saling lepas (_mutually exclusive_) dan mencakup seluruh populasi data secara non-overlapping.
- Penggunaan alat ini sangat tidak direkomendasikan apabila variabel kualitatif memiliki terlalu banyak kategori karena akan menyulitkan perbandingan visual antarsektor yang sempit.

---

#### E. Bar Chart

- Bar Chart (Diagram Batang) adalah representasi visual untuk data kategorikal yang digambarkan menggunakan batang persegi panjang dengan panjang atau tinggi yang sebanding dengan nilai kuantitatif yang diwakilinya.
- Berbeda dengan histogram yang batangnya saling menempel untuk menunjukkan kesinambungan data kontinu, batang pada Bar Chart memiliki jarak pemisah karena mewakili kategori diskret yang berbeda.
- Dalam analisis data tingkat lanjut, Bar Chart sering digunakan untuk melakukan agregasi nilai kuantitatif berdasarkan kategori tertentu menggunakan fungsi matematika spesifik (seperti nilai rata-rata, jumlah total, nilai minimum, nilai maksimum, atau simpangan baku).

> [!tip] Audio Insight — Bar Chart untuk agregasi kategori
> Dosen menguraikan bahwa dalam praktik ilmu data, Bar Chart sering digunakan untuk menunjukkan komposisi sekaligus hubungan antara satu variabel kuantitatif dengan satu variabel kategorikal. Bar Chart memungkinkan pembuat keputusan untuk membandingkan performa antarkategori secara langsung dan objektif berdasarkan hasil fungsi agregasi yang telah dihitung sebelumnya. Konsep "agregasi per kategori" ini persis sama dengan `.groupby()` di [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] dan klausa `GROUP BY` di [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]].

---

#### F. Representasi Konseptual Berbasis Kode

```python
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
```

---

## Bab 7 Diskusi Kuliah dan Relevansinya dengan AI Bootcamp

### 7.1 Buku Rekomendasi Kuliah

#### A. Analisis Kritis Penyajian Data

- Dalam sesi perkuliahan, direkomendasikan sebuah buku klasik bidang statistika yang sangat berpengaruh yaitu _How to Lie with Statistics_ karya Darrell Huff.
- Buku ini menguraikan bagaimana metode-metode statistika dapat dimanfaatkan sebagai pedang bermata dua (_double-edged sword_).
- Melalui teknik manipulasi visualisasi grafik, pemilihan sampel yang bias, atau penyajian nilai rata-rata (_mean_) yang dipengaruhi pencilan pada data miring (_skewed data_), pelaku penyaji data dapat mengelabui pemahaman audiens tanpa harus memalsukan angka-angka matematisnya secara ilegal.
- Pemahaman kritis terhadap bias metodologi ini sangat penting agar praktisi tidak mudah teperdaya oleh laporan visual atau tajuk utama berita (_headline news_) yang menyesatkan.

> [!tip] Audio Insight — Kritis terhadap asal-usul data
> Dosen menjelaskan bahwa statistika sering kali menyajikan fakta yang secara matematis benar, namun perspektif dan cara interpretasi penyajiannya dibuat berbeda untuk mengarahkan opini publik. Oleh karena itu, sebagai profesional di bidang data, kita harus kritis dengan menanyakan asal-usul data, bagaimana sampel diambil, serta metode statistik apa yang digunakan sebelum mempercayai sebuah kesimpulan data. Buku yang sama ini juga dirujuk di [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]] Bab 1.3 sebagai landasan prinsip _Clarity_ dan _Accuracy_ dalam visualisasi.

---

### 7.2 Peran Statistika Bagi AI Engineer

#### A. Validasi dan Pembersihan Data

- Peran statistika bagi seorang _AI Engineer_ (terutama yang berkutat di bidang _Generative AI_) sangat krusial dan tidak terbatas pada pemodelan matematika saja.
- **Validasi Keakuratan**: Pemahaman statistika mencegah terjadinya kepercayaan buta (_blind trust_) terhadap hasil performa model yang dideklarasikan oleh _Data Scientist_. Seorang _AI Engineer_ harus mampu mengaudit kelayakan model secara independen sebelum melakukan proses penyebaran model (_deployment_).
- **Pembersihan Data (_Data Cleaning_)**: Statistika menyediakan kerangka kerja ilmiah untuk mengidentifikasi data rusak, data bising (_noise_), dan pencilan yang dapat merusak kualitas pelatihan model _Machine Learning_.
- **Transformasi Distribusi**: Algoritma cerdas tertentu membutuhkan data input yang memenuhi asumsi distribusi normal. Statistika memberikan metode transformasi (seperti transformasi logaritma) untuk menormalkan sebaran data yang miring (_skewed_).

> [!tip] Audio Insight — AI Engineer tidak perlu hafal rumus, tapi harus paham konsep
> Dosen menggarisbawahi bahwa di era perkembangan teknologi kecerdasan buatan modern, _AI Engineer_ tidak harus menghafal seluruh rumus rumit matematika teoretis. Namun, pemahaman konsep statistika dasar mutlak diperlukan untuk memastikan bahwa model yang diintegrasikan ke dalam sistem produksi benar-benar andal, bersih dari bias sampel, dan bekerja sesuai parameter fisis dunia nyata.

---

### 7.3 Penanganan Kasus Riil Data Science

#### A. Deteksi Fraud Kartu Kredit

- Dalam skenario industri keuangan nyata, data pencilan (_outliers_) tidak boleh serta merta dihapus dari dataset pelatihan model.
- Pada kasus deteksi transaksi mencurigakan (_Fraud Detection_), transaksi ilegal/fraud merupakan kejadian yang sangat langka dengan proporsi berkisar antara 0.5% hingga 1% dari total populasi transaksi.
- Kejadian langka ini terdeteksi sebagai pencilan secara statistik. Jika praktisi menghapus seluruh pencilan dengan tujuan memperbagus bentuk distribusi data agar simetris, maka esensi dan tujuan utama dari pembuatan model deteksi fraud tersebut akan hilang sepenuhnya karena data transaksi ilegal telah terhapus dari sistem.

> [!warning] Audio Insight — Jangan pukul rata hapus outlier
> Dosen menegaskan pentingnya analisis _case-by-case_. Kita tidak boleh melakukan pukul rata untuk menghapus pencilan menggunakan aturan baku 1.5 IQR jika masalah bisnis utama kita justru berfokus pada analisis perilaku anomali tersebut.

---

#### B. Penanganan Imbalanced Data

- Dataset dengan proporsi kelas yang sangat timpang (seperti 99% transaksi normal vs 1% transaksi fraud) disebut dengan istilah _[[Kamus & Cheatsheet (JCAIEH M1)#I|Imbalanced Data]]_.
- **Bahaya Akurasi (_Misleading Accuracy_)**: Jika model _Machine Learning_ dilatih pada data yang sangat tidak seimbang tanpa penanganan khusus, model tersebut cenderung memprediksi semua masukan ke dalam kelas mayoritas. Model yang selalu menebak "transaksi normal" pada kasus di atas akan menghasilkan akurasi sebesar 99%, namun model tersebut tidak memiliki nilai guna praktis fungsional (_not meaningful_) karena gagal mendeteksi satu pun transaksi fraud.
- **Solusi Rekayasa Data (_Data Sampling_)**:
    - _Down-sampling_: Mengurangi jumlah sampel dari kelas mayoritas secara acak agar memiliki rasio seimbang (50:50) dengan kelas minoritas. Metode ini mengorbankan banyak volume data latih.
    - _Up-sampling_: Menambahkan jumlah sampel pada kelas minoritas dengan memproduksi data tiruan secara sintetik agar volumenya setara dengan kelas mayoritas.
- **Solusi Pemilihan Metrik Evaluasi**: Menghindari penggunaan metrik akurasi (_accuracy_), dan beralih ke metrik yang sensitif terhadap kelas minoritas seperti presisi (_precision_) dan _recall_.

> [!warning] Audio Insight — Akurasi tinggi bisa menyesatkan
> Dosen menyimpulkan bahwa akurasi tinggi sering kali mengecoh praktisi pemula. Memahami kapan akurasi bersifat menyesatkan dan kapan harus menggunakan metrik _precision_ dan _recall_ adalah pembeda utama antara praktisi data yang kompeten dengan yang tidak.

**Contoh kode — membuktikan bahaya "misleading accuracy" dengan angka nyata:**

```python
from sklearn.metrics import precision_score, recall_score, accuracy_score

# Simulasi: 990 transaksi normal (0), 10 transaksi fraud (1) -> 1% imbalanced
y_true = [0] * 990 + [1] * 10
y_pred = [0] * 1000  # model "malas" yang SELALU menebak "normal"

print("Accuracy :", accuracy_score(y_true, y_pred))                          # 0.99 -> KELIHATANNYA bagus...
print("Precision:", precision_score(y_true, y_pred, zero_division=0))         # 0.0  -> tapi TIDAK PERNAH benar saat prediksi fraud
print("Recall   :", recall_score(y_true, y_pred, zero_division=0))            # 0.0  -> gagal total mendeteksi fraud yang ada

# Kesimpulan: akurasi 99% ini MENYESATKAN karena model tidak punya nilai guna
# untuk tujuan bisnis sebenarnya, yaitu MENANGKAP transaksi fraud.
```

#### C. Representasi Konseptual Berbasis Kode

```python
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
```

---

## Lampiran: Catatan Tambahan dari Sesi (Contoh Praktis Tambahan)

Bagian ini berisi catatan pelengkap dari sesi kelas yang memuat beberapa contoh kasus industri tambahan (di luar contoh gaji/pendapatan yang sudah dibahas di Bab 4) untuk memperkaya intuisi mengenai bentuk-bentuk distribusi.

### Bentuk-Bentuk Distribusi Histogram — Contoh Industri Tambahan

- **Symmetric / Normally Distributed** — Data terpusat di tengah dan bentuknya simetris seperti lonceng (_bell curve_). Mean, median, dan modus posisinya hampir sama di tengah.
    - _Contoh Praktis_: Berat standar _bale_ kardus hasil mesin _press_. Mayoritas _bale_ akan berada di sekitar berat rata-rata (misal 500 kg), dengan sedikit _bale_ yang meleset menjadi terlalu ringan atau terlalu berat.
- **Right Skewed (Condong ke Kanan / Skewness Positif)** — "Ekor" grafik memanjang ke arah kanan. Sebagian besar data menumpuk di nilai-nilai rendah (kiri), tetapi ada beberapa data ekstrem (_outlier_) yang nilainya sangat tinggi sehingga menarik rata-ratanya ke kanan.
    - _Contoh Praktis_: Waktu perbaikan atau _downtime_ mesin operasional. Sebagian besar perbaikan biasanya cepat diselesaikan (nilai rendah di kiri), tetapi sesekali ada kerusakan parah yang memakan waktu berhari-hari untuk diperbaiki (ekor panjang di kanan).
- **Left Skewed (Condong ke Kiri / Skewness Negatif)** — Kebalikan dari _right skewed_: "ekor" grafik memanjang ke arah kiri. Sebagian besar data menumpuk di nilai-nilai tinggi (kanan), namun ada beberapa data ekstrem yang nilainya sangat rendah.
    - _Contoh Praktis_: Pemenuhan kapasitas muatan truk sebelum dikirim ke pabrik peleburan. Kebanyakan truk akan berangkat dengan kapasitas muatan yang hampir penuh (menumpuk di kanan), tetapi sesekali ada truk yang terpaksa berangkat dengan muatan sedikit karena alasan mendesak (ekor di kiri).
- **Bimodal** — Memiliki dua puncak (_modus_) yang menonjol. Biasanya menjadi petunjuk kuat bahwa ada dua kondisi, kelompok, atau sifat berbeda yang tercampur di dalam satu kumpulan data tersebut.
    - _Contoh Praktis_: Jam kedatangan suplai material. Puncak pertama mungkin terjadi di pagi hari (misal jam 09:00–10:00) saat pengiriman pertama, dan puncak kedua terjadi di sore hari (misal jam 15:00–16:00) untuk pengiriman penutup.
- **Uniform (Seragam)** — Distribusi data terlihat datar atau merata. Frekuensi kemunculan untuk setiap rentang nilai hampir sama, tidak ada satu nilai pun yang mendominasi.
    - _Contoh Praktis_: Pengeluaran rutin untuk barang habis pakai harian (seperti karung atau sarung tangan kerja) di mana jumlah permintaannya relatif konstan dan stabil setiap hari tanpa ada fluktuasi atau lonjakan berarti.

> [!tip] Menghubungkan bentuk distribusi dengan arah skew di Box Plot
> Contoh "waktu perbaikan mesin" (right-skewed) dan "muatan truk" (left-skewed) di atas adalah cara lain untuk melatih intuisi arah skew — lengkapi dengan pembacaan Box Plot-nya di [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]] Bab 3.2.

**Contoh kode — mensimulasikan dan membandingkan kelima bentuk distribusi di atas:**

```python
import numpy as np

np.random.seed(3)

# Symmetric: berat bale kardus di sekitar 500kg
berat_bale = np.random.normal(loc=500, scale=15, size=1000)

# Right-skewed: downtime mesin (mayoritas cepat, sedikit yang sangat lama)
downtime_mesin = np.random.exponential(scale=2, size=1000)  # dalam jam

# Left-skewed: kapasitas muatan truk (mayoritas hampir penuh/100%, sedikit yang rendah)
kapasitas_truk = 100 - np.random.exponential(scale=8, size=1000)

# Bimodal: jam kedatangan supplier (gabungan dua distribusi normal)
jam_pagi = np.random.normal(loc=9.5, scale=0.5, size=500)
jam_sore = np.random.normal(loc=15.5, scale=0.5, size=500)
jam_kedatangan = np.concatenate([jam_pagi, jam_sore])

# Uniform: permintaan sarung tangan harian
permintaan_harian = np.random.uniform(low=40, high=60, size=1000)

for nama, data in [("Symmetric (bale kardus)", berat_bale),
                    ("Right-skewed (downtime)", downtime_mesin),
                    ("Left-skewed (kapasitas truk)", kapasitas_truk),
                    ("Bimodal (jam kedatangan)", jam_kedatangan),
                    ("Uniform (permintaan harian)", permintaan_harian)]:
    print(f"{nama:32s} | mean={np.mean(data):8.2f} | median={np.median(data):8.2f}")
    # Perhatikan: pada Symmetric & Uniform, mean ~ median.
    # Pada Right-skewed, mean > median. Pada Left-skewed, mean < median.
```

---

## Ringkasan Kilat Sesi (Cheat Sheet)

| Konsep | Rumus / Kunci |
|:--|:--|
| Mean | jumlah semua nilai / n |
| Median | nilai tengah data terurut, posisi `(n+1)/2` |
| IQR | `Q3 - Q1` (murni lebar sebaran, TANPA 1.5x) |
| Batas Outlier | `Q1 - 1.5*IQR` dan `Q3 + 1.5*IQR` (langkah terpisah SETELAH IQR dihitung) |
| Empirical Rule | 68% (±1s), 95% (±2s), 99.7% (±3s) — hanya untuk data simetris |
| Interval vs Ratio | tes primer: apakah 0 = ketiadaan absolut? (bukan "bisa negatif?") |
| Skewness & Box Plot | median dekat Q1 → right-skewed; median dekat Q3 → left-skewed (lihat [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]]) |
| Imbalanced Data | jangan pakai accuracy saja — pakai precision & recall |

---

**Lihat juga:** [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] (implementasi `.describe()`, `.mean()`, `.std()`, `.quantile()` di Pandas) · [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]] (Histogram, Box Plot, dan visualisasi distribusi) · [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] (konsep agregasi yang setara dengan `GROUP BY`).

---

## 🔗 Terkait

- [[Sesi 13 - Data Visualization (JCAIEH M1)|Sesi 13 - Data Visualization]] — Box Plot, IQR, deteksi outlier, dan arah skewness yang dijelaskan matematis di sini (Bab 4.2-4.4) divisualisasikan langsung di sana (Bab 3.2).
- [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] — method `.describe()`, `.mean()`, `.std()`, dan `.quantile()` adalah implementasi Pandas langsung dari konsep statistika deskriptif di sesi ini.
- [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] — struktur baris = unit observasi, kolom = variabel yang dibahas di Bab 2.1 persis sama dengan struktur tabel relasional SQL.
