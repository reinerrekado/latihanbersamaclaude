---
tags: [jcaieh/module1, sesi-08, python, modular-programming, module, package, import, name-guard, jcaieh/module1/sesi08]
bootcamp: JCAIEH
module: 1
session: 8
aliases: ["Sesi 8"]
---

# Session 8 — Python & Modular Programming

Study guide ini membahas [[Kamus & Cheatsheet (JCAIEH M1)#M|pemrograman modular]] di Python: mengapa [[Kamus & Cheatsheet (JCAIEH M1)#M|kode monolitik]] bermasalah saat proyek membesar, cara membuat dan mengimpor [[Kamus & Cheatsheet (JCAIEH M1)#M|modul]] (`import` vs `from ... import ...`), [[Kamus & Cheatsheet (JCAIEH M1)#A|alias impor]], struktur hierarki [[Kamus & Cheatsheet (JCAIEH M1)#P|Project]] → [[Kamus & Cheatsheet (JCAIEH M1)#P|Package]] → Module, pelindung eksekusi `if __name__ == "__main__"`, konsep *Package* (`__init__.py`, *[[Kamus & Cheatsheet (JCAIEH M1)#D|Deep Import]]* vs *[[Kamus & Cheatsheet (JCAIEH M1)#S|Shallow Import]]*), tips praktik terbaik, hingga tiga latihan bertingkat (basic, intermediate, advanced).

---

## Bab 1 — Pengenalan Pemrograman Modular (Introduction to Modular Programming)

### A. Fondasi Konseptual

- **Definisi Pemrograman Modular**: Pendekatan pemrograman yang memecah atau membagi program besar menjadi komponen-komponen atau modul-modul kecil yang dapat digunakan kembali (*reusable components*). Setiap file Python (`.py`) dalam paradigma ini diidentifikasi sebagai satu modul terpisah.
- **Definisi Kode Monolitik**: Pendekatan pemrograman tradisional di mana seluruh fungsi, variabel, dan logika program digabungkan ke dalam satu file tunggal (*single file*).
- **Prinsip Dasar**: Pemrograman modular bertujuan untuk mengelola kompleksitas sistem (*complexity*) seiring bertambahnya skala proyek dan volume kode (*line of code*) yang ditulis.

> [!warning] Audio Insight — Pertumbuhan Organik File Monolitik
> Pada proyek riil, file monolitik sering kali bertumbuh secara organik. Ketika sebuah fitur baru dikembangkan, developer cenderung langsung menambahkan fungsi baru ke dalam file utama yang sama. Pada titik tertentu, sistem ini akan mengalami masalah skalabilitas (*scale up*) yang signifikan. Meskipun secara fungsional kode tersebut tetap berjalan (*works*), kode tersebut akan menjadi terlalu kompleks dan tidak terstruktur.

---

### B. Tantangan Kode Monolitik (Monolithic Code Challenges)

Ketika program bertumbuh menjadi lebih besar (misalnya mencapai 500 baris kode atau lebih), terdapat lima tantangan utama yang muncul akibat penggunaan kode monolitik:

1. **Sulit Dibaca (*Difficult to Read*)**: Penumpukan seluruh fungsi dan logika di dalam satu file menyebabkan bagian kode tertentu tertimbun, sehingga sulit untuk dicari dan dipahami alurnya.
2. **Sulit Dipelihara (*Difficult to Maintain*)**: Kode monolitik menjadi sangat rapuh seiring waktu. Satu perubahan kecil atau kesalahan ketik (*typo*) pada satu bagian dapat merusak bagian lain yang tidak berhubungan (*break unrelated features*).
3. **Sulit Didebug (*Difficult to Debug*)**: Proses pelacakan sumber kesalahan (*error*) menjadi sangat rumit karena seluruh jalannya program berada di dalam satu ruang lingkup file yang sama.
4. **Sulit Digunakan Kembali (*Difficult to Reuse*)**: Fungsi yang didefinisikan dalam kode monolitik tidak dapat dipanggil oleh file lain secara langsung. Untuk menggunakannya kembali, developer terpaksa melakukan salin-tempel (*copy-paste*) kode secara manual.
5. **Sulit Berkolaborasi (*Difficult to Collaborate*)**: Ketika beberapa developer bekerja pada file monolitik yang sama, proses integrasi kode akan sering mengalami konflik penggabungan (*[[Kamus & Cheatsheet (JCAIEH M1)#M|merge conflict]]*) di repositori Git/GitHub.

| Karakteristik | Kode Monolitik (*Monolithic Code*) | Pemrograman Modular (*Modular Programming*) |
|:--|:--|:--|
| **Struktur Berkas** | Terpusat dalam satu file tunggal (*single file*) | Terbagi ke dalam beberapa file modul kecil |
| **Keterbacaan** | Rendah, logika penting tertimbun dalam ratusan baris | Tinggi, kode bersih (*clean*) dan ringkas (*concise*) |
| **Dampak Kesalahan** | Tinggi, satu kesalahan dapat merusak seluruh sistem (*break*) | Terisolasi pada modul yang bersangkutan saja |
| **Kemudahan Pengujian** | Sulit karena ketergantungan antar-fungsi sangat erat | Mudah karena pengujian unit (*unit testing*) dapat dilakukan secara terisolasi |
| **Kolaborasi Tim** | Sering memicu *merge conflict* yang sulit diresolusi | Lebih lancar melalui pembagian tanggung jawab modul (*clear responsibility*) |

> [!warning] Audio Insight — Masalah Pencarian Kode, Kerentanan Berantai, dan Mekanisme Kolaborasi Tim
> **Masalah Pencarian Kode**: Dosen mencontohkan bahwa pada kode monolitik, logika pembersihan teks (*text cleaning logic*) dapat dengan mudah "terkubur" di antara ratusan baris kode lainnya, membuat developer kesulitan menemukannya kembali saat dibutuhkan.
>
> **Kerentanan Berantai**: Satu *typo* kecil pada fungsi di file monolitik dapat menghentikan jalannya seluruh program (*break the whole file*) secara total.
>
> **Mekanisme Kolaborasi Tim**: Jika proyek dikelola secara modular, pembagian tugas menjadi lebih jelas. Sebagai contoh, developer A dapat fokus mengerjakan tahap *preprocessing*, developer B pada *model training*, dan developer C pada pemuatan data (*load results*). Setiap developer bekerja pada file modul terpisah dan membuat cabang (*[[Kamus & Cheatsheet (JCAIEH M1)#B|branch]]*) Git masing-masing. Saat dilakukan penggabungan (*merge*), sistem Git akan mengenalinya sebagai file baru atau perubahan terpisah, sehingga dapat melakukan penggabungan otomatis (*auto-merge*) tanpa memicu konflik terus-menerus. Sebaliknya, jika bekerja pada satu file yang sama, baris-baris kode akan saling tumpang tindih dan memicu *conflict* yang harus diresolusi manual (*resolve conflict*) secara berulang.

> [!tip] Lihat juga
> *Merge conflict* dan konsep *branch* di atas sudah diperkenalkan di [[Sesi 02 - Intro to Git and GitHub (JCAIEH M1)|Sesi 02 - Intro to Git and GitHub]] — pemrograman modular adalah salah satu alasan konkret mengapa struktur branch/merge Git menjadi jauh lebih efektif digunakan.

---

### C. Batasan dan Evaluasi Kebutuhan Modularisasi

- **Efek Samping Kompleksitas**: Modularisasi pada dasarnya menambahkan sedikit kompleksitas (*complexity*) pada struktur proyek (misalnya dalam mengelola jalur file, impor, dan hubungan antar-modul) demi mendapatkan keteraturan.
- **Prinsip Evaluasi**: Jika program yang dibangun sangat sederhana, berukuran kecil, dan hanya berupa skrip sekali pakai, pemrograman modular tidak perlu dipaksakan. Memaksakan modularisasi pada kasus yang tidak tepat justru akan menambah kompleksitas yang tidak perlu (*unnecessary complexity*).

> [!tip] Audio Insight — Modularisasi Sebagai Investasi Struktural
> Dosen menekankan pentingnya melihat kondisi nyata sebelum memutuskan melakukan modularisasi. Modularisasi adalah investasi struktural. Jika hanya membuat satu file kecil sederhana, pendekatan satu file (monolitik) justru lebih efisien karena menghindari kompleksitas berlebih yang tidak mendatangkan manfaat nyata.

---

## Bab 2 — Modul dalam Python (Module in Python)

### A. Fondasi Konseptual

- **Definisi Modul**: Sebuah file Python tunggal berekstensi `.py` yang berisi sekumpulan kode terorganisasi dan dapat digunakan kembali (*reusable code*). Modul dapat berisi definisi fungsi (*functions*), kelas (*classes*), maupun variabel.
- **Tujuan Pembuatan Modul**: Memisahkan logika program yang sejenis ke dalam file terpisah guna meningkatkan kerapian, memudahkan proses pemeliharaan (*maintenance*), mempermudah proses pencarian kesalahan (*debugging*), serta meningkatkan reusabilitas kode (*code reusability*).
- **Struktur Berkas Sederhana**:
    - `calculator.py`: Berkas modul yang menyimpan fungsi-fungsi utilitas kalkulasi.
    - `main.py`: Berkas skrip utama yang mengimpor dan memanfaatkan utilitas dari `calculator.py`.

> [!warning] Audio Insight — Fleksibilitas Isi Modul dan Kemudahan Pelacakan Masalah
> Berdasarkan diskusi kelas, dosen mengonfirmasi bahwa isi dari sebuah modul Python tidak terbatas pada fungsi (*functions*) saja. Modul juga dapat diisi dengan pendefinisian kelas (*classes*) atau variabel sesuai kebutuhan rancangan program.
>
> Dosen menjelaskan bahwa pengorganisasian kode ke dalam modul sangat membantu proses pemecahan masalah (*debugging*). Jika terjadi kesalahan kalkulasi, developer dapat langsung menuju ke file `calculator.py` tanpa perlu memeriksa ratusan baris kode lainnya di berkas utama.

> [!tip] Lihat juga
> "Modul dapat berisi *classes*" — ini artinya *class* seperti `BankAccount` atau `MachineLearningModel` yang dibuat di [[Sesi 07 - Object Oriented Programming (JCAIEH M1)|Sesi 07 - Object Oriented Programming]] dalam praktiknya justru sebaiknya diletakkan di dalam file modul terpisah (`bank_account.py`, `model.py`), lalu diimpor ke `main.py`.

---

### B. Metode Pengimporan Modul (Importing Module)

Ada dua metode utama yang digunakan untuk mengimpor modul di Python, masing-masing memiliki karakteristik penulisan (*syntax*) dan pengelolaan ruang nama (*namespace*) yang berbeda:

1. **Metode Mengimpor Seluruh Modul (`import module_name`)**
    - **Karakteristik**: Mengimpor keseluruhan modul ke dalam berkas aktif.
    - **Cara Pemanggilan**: Setiap pemanggilan fungsi atau komponen di dalam modul wajib diawali dengan nama modul sebagai *namespace* (contoh: `module_name.function_name()`).
    - **Dampak Kelalaian Namespace**: Jika nama modul tidak disertakan saat pemanggilan fungsi, Python tidak akan mengenali fungsi tersebut dan akan memicu kesalahan sistem (*NameError*).
2. **Metode Mengimpor Komponen Spesifik (`from module_name import function_name`)**
    - **Karakteristik**: Hanya mengimpor komponen atau fungsi tertentu yang dideklarasikan secara eksplisit ke dalam berkas aktif. Komponen lain yang tidak disebutkan di baris impor tidak akan dapat diakses.
    - **Cara Pemanggilan**: Fungsi dapat dipanggil secara langsung menggunakan namanya tanpa perlu menambahkan prefiks nama modul di depannya (contoh: `function_name()`).
    - **Kelebihan**: Membuat penulisan kode pada berkas utama terasa lebih bersih, ringkas, dan efisien (*clean and concise*).

| Metode Impor | Sintaksis Impor | Contoh Pemanggilan Fungsi | Pengaruh terhadap Namespace | Reusabilitas |
|:--|:--|:--|:--|:--|
| **Mengimpor Seluruh Modul** | `import calculator` | `calculator.add(2, 3)` | Melindungi *namespace* agar tidak terjadi bentrokan nama variabel atau fungsi | Tinggi, mengimpor seluruh fungsionalitas modul sekaligus |
| **Mengimpor Komponen Spesifik** | `from calculator import add` | `add(2, 3)` | Memasukkan komponen langsung ke *namespace* lokal berkas aktif | Terbatas, hanya mengimpor komponen yang dideklarasikan saja |

> [!warning] Audio Insight — Dampak Kesalahan Tanpa Namespace dan Alur Pengimporan
> Dosen mendemonstrasikan secara langsung di kelas kesalahan yang terjadi ketika developer menggunakan `import calculator` tetapi memanggil fungsi secara langsung seperti `add(2, 3)`. Python akan mengeluarkan pesan *error* "NameError: name 'add' is not defined" karena Python kehilangan rujukan lokasi definisi fungsi tersebut. Hal ini membuktikan pentingnya pemahaman *namespace* dalam modul.
>
> Dosen memberikan simulasi penulisan modul matematika alternatif bernama `math_utils.py` yang berisi fungsi `add(a, b)` dan `multiply(a, b)`. Dengan menggunakan `from math_utils import add, multiply`, kode di berkas utama menjadi jauh lebih terbaca karena fungsi-fungsi tersebut langsung dikenali oleh berkas pengeksekusi tanpa embel-embel nama file di depannya.

**Contoh pembuktian NameError (ditambahkan):**

```python
# main.py
import calculator

# result = add(2, 3)   # -> NameError: name 'add' is not defined
result = calculator.add(2, 3)   # BENAR: pakai namespace 'calculator.'
print(result)                    # Output: 5
```

---

### C. Demonstrasi dan Implementasi Kode

Berikut adalah contoh struktur kode bersih untuk implementasi modul pertama sesuai dengan standar latihan di kelas:

**1. Pembuatan Berkas Modul (`calculator.py`)**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**2. Implementasi pada Berkas Utama dengan Metode Impor Utuh (`main.py`)**

```python
import calculator

result_add = calculator.add(2, 3)
result_sub = calculator.subtract(5, 2)

print(result_add)
print(result_sub)
```

**3. Implementasi pada Berkas Utama dengan Metode Impor Spesifik (`main.py`)**

```python
from calculator import add, subtract

result_add = add(2, 3)
result_sub = subtract(5, 2)

print(result_add)
print(result_sub)
```

> [!tip] Audio Insight — Pilihan Pendekatan Impor
> Kedua pendekatan di atas sepenuhnya valid dan bekerja dengan baik (*works*). Keputusan pemilihan metode impor sangat bergantung pada preferensi kerapian penulisan kode serta kebutuhan perlindungan ruang nama (*namespace*) dari variabel lain yang ada pada proyek Anda.

---

## Bab 3 — Mengorganisasi Proyek (Organizing a Project)

### A. Fondasi Konseptual

- **Hierarki Proyek Python**: Pengorganisasian kode dalam Python mengikuti struktur hierarki tiga tingkat guna memisahkan ruang lingkup kerja dan tanggung jawab kode secara terstruktur.
- **Tiga Komponen Utama**:
    - **Project**: Keseluruhan aplikasi atau pustaka (*library*) secara utuh dan lengkap yang sedang dibangun.
    - **Package**: Direktori atau folder fisik yang digunakan untuk mengelompokkan beberapa modul Python yang memiliki keterkaitan fungsional.
    - **Module**: Satu berkas Python tunggal (berkas berekstensi `.py`) yang berisi kode program berupa kelas (*class*), fungsi (*function*), atau variabel yang dapat digunakan kembali.

| Istilah | Karakteristik Utama | Representasi Fisik |
|:--|:--|:--|
| **Project** | Aplikasi lengkap atau pustaka (*library*) secara menyeluruh | Folder utama proyek (*root directory*) |
| **Package** | Folder pengelompok modul-modul yang saling berhubungan | Folder khusus berisi file `__init__.py` |
| **Module** | Berkas kode tunggal berisi fungsi atau kelas siap pakai | Berkas berekstensi `.py` |

> [!warning] Audio Insight — Pentingnya Memahami Hierarki Project-Package-Module
> Dosen menekankan bahwa pemahaman hierarki ini sangat penting ketika proyek bertumbuh dari skrip tunggal menjadi aplikasi skala besar. Secara sederhana, modul adalah berkas individu, package adalah folder yang membungkus berkas-berkas tersebut, dan project adalah seluruh ekosistem aplikasi tersebut. Modul tidak hanya terbatas pada pendefinisian fungsi (*functions*), melainkan dapat berisi kelas (*classes*) dan variabel global.

---

### B. Studi Kasus Penerapan: Customer Churn Prediction

- **Prinsip Pembagian Tanggung Jawab (*Separation of Responsibility*)**: Dalam merancang proyek pemrograman modular, setiap modul wajib didefinisikan untuk memegang satu tanggung jawab spesifik yang jelas (*clear responsibility*). Pembuatan modul tidak boleh dilakukan secara acak (*random*).
- **Alur Kerja Logis Proyek**:
    1. **Load Data**: Memuat dataset mentah dari sumber penyimpanan.
    2. **Preprocessing Data**: Melakukan pembersihan data (*cleaning*) dan transformasi.
    3. **Model Training**: Melatih model kecerdasan buatan (*AI model*) menggunakan data hasil pemrosesan.
    4. **Model Evaluation**: Mengevaluasi performa model menggunakan metrik pengujian.
    5. **Orchestration**: Mengatur jalannya seluruh proses dari awal hingga akhir melalui berkas utama.
- **Pembagian Tugas dan Berkas Modul**:

| Nama Berkas Modul | Tanggung Jawab Spesifik (*Responsibility*) | Fitur / Fungsionalitas Utama |
|:--|:--|:--|
| **`data.py`** | Memuat data (*load the data*) | Fungsi untuk membaca dataset mentah dari penyimpanan lokal atau *cloud* |
| **`preprocessing.py`** | Pra-pemrosesan data (*preprocessing data*) | Menangani nilai kosong (*missing values*), menghapus data duplikat (*duplicate removal*), dan penyandian fitur (*encoding features*) |
| **`model.py`** | Pelatihan model (*training the model*) | Mendefinisikan algoritma AI dan melatih model di atas data bersih |
| **`evaluate.py`** | Evaluasi model (*evaluate the model*) | Menghitung performa model menggunakan metrik evaluasi |
| **`main.py`** | Mengorkestrasi sistem (*orchestrate*) | Mengimpor seluruh modul fungsional dan menjalankan alur kerja proyek secara teratur |

> [!warning] Audio Insight — Masalah Pembuatan Modul Secara Acak dan Efisiensi Kolaborasi
> Dosen mengingatkan agar pengembang tidak membagi modul secara sembarangan (seperti membuat `modul_A.py` atau `modul_B.py` tanpa pembagian fungsi yang jelas). Setiap modul harus memiliki nama yang mendeskripsikan tanggung jawabnya agar kode mudah dipelihara (*maintainable*).
>
> Jika terjadi *error* pada tahap pembersihan data duplikat, pengembang dapat langsung menuju berkas `preprocessing.py` tanpa mengganggu berkas `model.py` atau `main.py`. Pola modular ini juga memfasilitasi kerja paralel dalam tim. Misalnya, Developer A bekerja pada `preprocessing.py`, Developer B pada `model.py`, dan Developer C pada `evaluate.py`. Karena bekerja pada file terpisah, mereka dapat membuat cabang (*branch*) Git masing-masing, meminimalkan terjadinya konflik penggabungan (*merge conflict*), dan memungkinkan Git melakukan penggabungan otomatis (*auto-merge*).
>
> Setelah modularisasi diterapkan, berkas `main.py` menjadi sangat bersih, ringkas (*concise*), dan mudah dibaca karena hanya berisi panggilan tingkat tinggi (*high-level calls*) terhadap fungsi-fungsi yang diimpor dari modul lain.

---

### C. Teknik Penggunaan Alias dalam Impor

- **Definisi [[Kamus & Cheatsheet (JCAIEH M1)#A|Alias]]**: Mekanisme mempersingkat nama modul yang diimpor menggunakan kata kunci `as`.
- **Manfaat Utama**:
    - Mempersingkat penulisan kode saat memanggil fungsi dari modul dengan nama yang panjang.
    - Menghindari konflik ruang nama (*namespace conflict*) di dalam berkas aktif.
- **Konstruksi Konflik Ruang Nama (*[[Kamus & Cheatsheet (JCAIEH M1)#N|Namespace Conflict]]*)**: Konflik ini terjadi apabila sebuah nama variabel yang dideklarasikan di dalam file utama memiliki nama yang persis sama dengan nama modul yang diimpor. Python akan mengalami tumpang tindih nama sehingga menyebabkan kesalahan eksekusi program (*NameError* atau kegagalan pemanggilan fungsi).

> [!tip] Dua Jenis Alasan Memakai Alias — Jangan Tertukar
> Materi ini menyebut alias untuk dua tujuan yang berbeda. Keduanya sama-sama pakai `as`, tapi motivasinya beda — jangan disamakan:
>
> **1. Alias untuk KONVENSI (mempersingkat penulisan, bukan karena ada konflik)**
> Dipakai karena nama modul aslinya panjang/sering diketik berulang, dan sudah menjadi kebiasaan umum di komunitas Python — bukan karena akan terjadi bentrok nama. Contoh paling terkenal (akan sering ditemui mulai [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]]):
> ```python
> import pandas as pd
> import numpy as np
>
> df = pd.DataFrame({"a": [1, 2, 3]})   # 'pd' hanya singkatan, tidak ada variabel bernama 'pandas' yang bentrok
> ```
> Di sini, sekalipun kita TIDAK memakai alias (`import pandas`, lalu `pandas.DataFrame(...)`), kodenya tetap akan bekerja dengan benar. Alasan pakai `as pd` murni kenyamanan/konvensi industri.
>
> **2. Alias untuk MENGHINDARI KONFLIK (ada variabel lain yang namanya sama persis dengan nama modul)**
> Dipakai karena kalau TIDAK diberi alias, program akan benar-benar error atau salah perilaku, sebab ada variabel lokal yang namanya sama persis dengan nama modul. Ini kasus `import model as model_modul` pada contoh kode di bawah — tanpa alias, baris `model = "Random Forest Classifier"` akan menimpa nama `model` sehingga Python tidak bisa lagi mengenali `model` sebagai modul.
>
> Cara membedakan keduanya: tanya "kalau alias ini dihapus, apakah kode masih benar?" — kalau jawabannya "masih benar, cuma lebih panjang" berarti itu alias konvensi; kalau jawabannya "akan error/salah" berarti itu alias wajib untuk menghindari konflik.

Berikut adalah contoh implementasi pengorganisasian proyek dan penggunaan alias secara aman dalam Python:

```python
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

> [!warning] Audio Insight — Pembuktian Namespace Conflict Tanpa Alias
> Dosen mencontohkan bahwa pada berkas `main.py` di atas, variabel `model` dideklarasikan untuk menampung teks `"Random Forest Classifier"`. Jika modul `model.py` diimpor secara biasa dengan perintah `import model`, maka pemanggilan fungsi di bawahnya seperti `model.train()` akan memicu *error* karena interpreter Python menganggap `model` sebagai variabel bertipe string, bukan sebagai modul. Dengan menggunakan alias `import model as model_modul`, ruang nama modul dialihkan ke `model_modul`, sehingga variabel lokal `model` dapat digunakan secara bersamaan tanpa memicu konflik ruang nama (*namespace conflict*).

**Pembuktian konflik jika alias TIDAK dipakai (ditambahkan):**

```python
# main_salah.py
import model              # tanpa alias

model = "Random Forest Classifier"   # menimpa 'model' -> sekarang 'model' adalah string, BUKAN modul lagi!

model.train_model()        # -> AttributeError: 'str' object has no attribute 'train_model'
```

---

## Bab 4 — Penggunaan Kondisional `__name__ == "__main__"`

### A. Fondasi Konseptual

- **Masalah Eksekusi Otomatis**: Saat sebuah file Python diimpor sebagai modul oleh file lain, interpreter Python akan mengeksekusi seluruh baris kode di dalam modul tersebut dari atas ke bawah. Jika di dalam file modul tersebut terdapat kode pengujian, deklarasi variabel uji coba, atau fungsi cetak (*print statement*), baris-baris tersebut akan ikut dijalankan secara otomatis saat proses impor dilakukan. Hal ini menghasilkan eksekusi yang tidak diinginkan pada berkas utama (*main program*).
- **Definisi `__name__ == "__main__"`**: Konstruksi kondisional ini bertindak sebagai pelindung eksekusi (*[[Kamus & Cheatsheet (JCAIEH M1)#N|name guard]]*) yang mengontrol aliran eksekusi berkas Python. Kondisional ini memberikan instruksi kepada Python untuk hanya mengeksekusi blok kode di bawahnya apabila berkas tersebut dijalankan secara langsung sebagai proses utama (*main process* atau *main execution*) melalui terminal.
- **Karakteristik Perilaku**: Jika berkas tersebut hanya diimpor ke berkas lain sebagai modul pustaka, pemeriksaan kondisional ini akan bernilai salah (*False*) dan blok kode di dalamnya akan diabaikan sehingga tidak ikut dieksekusi.

> [!tip] Lihat juga
> Mekanisme `__name__` ini sudah diperkenalkan sekilas di [[Sesi 07 - Object Oriented Programming (JCAIEH M1)|Sesi 07 - Object Oriented Programming]] Bab 6.2 lewat contoh `class BankAccount`. Di sini konsepnya dibahas lebih menyeluruh sebagai *name guard* untuk modul.

---

### B. Cara Kerja dan Mekanisme Variabel `__name__`

- **Mekanisme Variabel Bawaan**: Python memiliki variabel khusus bawaan bernama `__name__` yang secara otomatis didefinisikan untuk setiap berkas script yang dijalankan.
- **Nilai Variabel Berdasarkan Konteks Eksekusi**:
    - **Eksekusi Langsung**: Saat sebuah file Python dijalankan secara langsung dari terminal, variabel `__name__` di dalam file tersebut akan diisi dengan string `"__main__"`. Nilai ini bersifat mutlak untuk berkas yang bertindak sebagai titik masuk eksekusi (*entry point*).
    - **Proses Impor Modul**: Saat file tersebut diimpor sebagai modul ke dalam file lain, variabel `__name__` di dalam file modul tersebut tidak akan bernilai `"__main__"`, melainkan berubah nilai secara otomatis menjadi nama asli dari modul itu sendiri (misalnya `"calculator"`).

| Skenario Eksekusi | Nilai Variabel `__name__` di Berkas Aktif | Status Evaluasi `__name__ == "__main__"` | Dampak terhadap Blok Kode Pelindung |
|:--|:--|:--|:--|
| **Berkas Utama dijalankan langsung** | `"__main__"` | Benar (*True*) | Blok kode di dalam kondisional dieksekusi |
| **Berkas Modul diimpor ke berkas lain** | Nama modul tersebut (misalnya `"calculator"`) | Salah (*False*) | Blok kode di dalam kondisional dilewati/diabaikan |

> [!warning] Audio Insight — Pembuktian Nilai Variabel dan Independensi Nama Berkas Utama
> Melalui sesi interaksi tanya jawab antara mahasiswa (Anwar) dan dosen, dibuktikan secara langsung isi dari variabel `__name__` menggunakan perintah cetak (*print statement*). Saat berkas utama dijalankan langsung, hasil cetak menunjukkan variabel `__name__` di file utama bernilai `"__main__"`. Namun, ketika modul pendukung diimpor, variabel `__name__` di dalam file modul pendukung tersebut tercetak sebagai nama modul itu sendiri, bukan `"__main__"`. Perbedaan nilai inilah yang membuat evaluasi logika kondisional berhasil memisahkan proses impor dan eksekusi langsung secara akurat.
>
> Dalam diskusi kelas dengan mahasiswa (Stepen), dosen menguji coba mengganti nama berkas utama dari `main.py` menjadi `main_code.py` lalu menjalankannya langsung. Hasilnya menunjukkan bahwa variabel `__name__` pada berkas utama yang dieksekusi tetap bernilai `"__main__"`. Nilai `"__main__"` bersifat konseptual untuk menandai proses utama dan sama sekali tidak bergantung pada nama fisik file script di dalam sistem penyimpanan komputer Anda.

---

### C. Manfaat Menggunakan Name Guard

- **Mencegah Eksekusi yang Tidak Diinginkan (*Prevent Unwanted Execution*)**: Menghentikan jalannya kode eksekusi utama, kode demonstrasi, pengujian, atau fungsi cetak secara otomatis ketika file tersebut diimpor oleh file program lain.
- **Meningkatkan Penggunaan Kembali Kode (*Boost Code Reusability*)**: Memungkinkan satu file Python tunggal berfungsi ganda secara fleksibel, yaitu sebagai pustaka modul yang menyediakan fungsi-fungsi untuk diimpor berkas lain, sekaligus sebagai script mandiri (*independent script*) yang memiliki fungsi eksekusi mandiri ketika dijalankan langsung.
- **Pengujian Cepat dan Terisolasi (*Easy Quick Testing / Isolated Unit Test*)**: Memudahkan developer dalam menuliskan dan menjalankan kode pengujian unit khusus secara langsung di bagian bawah file modul guna memastikan fungsi-fungsi di dalamnya bekerja dengan benar, tanpa khawatir kode tes tersebut akan mengganggu atau mengotori output dari berkas lain yang mengimpor modul tersebut.

---

### D. Demonstrasi Kasus dan Implementasi Kode

Berikut adalah contoh perbandingan penulisan modul kalkulator tanpa pelindung (*no guard*) dengan modul kalkulator yang dilengkapi pelindung (*name guard*) beserta cara kerjanya saat diimpor oleh file utama:

```python
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

**Output yang dihasilkan saat `main.py` dijalankan (ditambahkan agar terlihat jelas perbedaannya):**

```
--- Memulai Proses Impor Modul Tanpa Pelindung ---
Hasil penjumlahan di calculator_no_guard: 3
--- Memulai Proses Impor Modul Dengan Pelindung ---
Hasil panggilan fungsi add secara aman: 12
```

> [!warning] Audio Insight — Kesalahpahaman Umum: Name Guard Menghalangi Impor Fungsi
> Dalam diskusi kelas, mahasiswa (Stepen) sempat mengalami kebingungan karena berasumsi bahwa penggunaan blok kondisional `if __name__ == "__main__":` akan menghalangi fungsi-fungsi penting di dalam modul untuk diimpor. Dosen menegaskan bahwa pemahaman tersebut keliru. Blok pelindung eksekusi hanya menyaring dan menghentikan baris perintah eksekusi langsung (seperti pembuatan variabel hasil dan fungsi cetak demonstrasi di baris terbawah modul). Sementara itu, definisi fungsi utama (seperti `def add(a, b)`) tetap terdaftar dengan sempurna di dalam memori dan dapat diimpor serta digunakan oleh berkas eksternal kapan saja tanpa hambatan.
>
> **Readability vs Penyusunan Baris Kode**: Saat membedah tugas kelompok, dosen menyarankan agar penulisan variabel-variabel penampung hasil fungsi di dalam fungsi pelaporan (*report function*) dideklarasikan secara runtut dan terpisah daripada menyatukannya ke dalam satu baris panjang (*single line assignment*). Mengisolasi variabel penampung di baris-baris terpisah sebelum mencetaknya sangat meningkatkan keterbacaan kode (*readability*) dan mempermudah pelacakan alur data (*data tracing*) saat terjadi kesalahan.

---

## Bab 5 — Package dalam Python (Packages in Python)

### A. Fondasi Konseptual

- **Definisi Package**: Folder atau direktori terorganisasi di dalam Python yang membungkus beberapa modul yang saling berkaitan agar mudah dikelola ketika skala proyek bertumbuh besar.
- **Pembeda Utama (Folder Biasa vs Package)**: Folder biasa hanya bertindak sebagai tempat penyimpanan fisik berkas di dalam sistem operasi. Sementara itu, Package adalah direktori khusus yang dikenali oleh interpreter Python sebagai pustaka (*library*) karena di dalamnya terdapat berkas inisialisasi bernama `__init__.py`.
- **File Inisialisasi `__init__.py`**: Berkas khusus (dapat berupa berkas kosong) yang wajib diletakkan di dalam direktori folder untuk memberi tahu Python bahwa folder tersebut merupakan sebuah package dan harus diperlakukan sebagai package. Jika folder tidak memiliki berkas `__init__.py`, maka folder tersebut hanya akan dianggap sebagai folder biasa dan proses impor fungsionalitas di tingkat folder akan gagal.

| Aspek Karakteristik | Folder Biasa | Package dalam Python |
|:--|:--|:--|
| **Keberadaan `__init__.py`** | Tidak memiliki berkas `__init__.py` | Wajib memiliki berkas `__init__.py` |
| **Pengenalan oleh Python** | Hanya dianggap sebagai direktori penyimpanan fisik biasa | Dikenali sebagai satu kesatuan package atau pustaka (*library*) |
| **Kemudahan Impor** | Memerlukan rute impor panjang (*Deep Import*) | Mendukung penyederhanaan impor (*Shallow Import*) |
| **Ekspos Fungsi** | Modul di dalamnya harus diakses secara manual dan individual | Fungsi terpilih dapat diekspos langsung di level folder utama |

> [!warning] Audio Insight — Fungsi `__init__.py` dan Nested Packages
> Di dalam kelas, dosen berdiskusi dengan Brian mengenai komponen penyusun direktori `preprocessing/`. Direktori tersebut membungkus modul-modul seperti `clean.py`, `encoder.py`, dan `standardizer.py`. Dosen memperjelas bahwa berkas `__init__.py` bukanlah modul biasa, melainkan file konfigurasi inisialisasi khusus yang mengendalikan perilaku pengimporan package tersebut.
>
> Stepen menanyakan kemungkinan pembuatan package bertingkat atau di dalam package terdapat package lain (*nested packages*). Dosen memverifikasi bahwa struktur bertingkat (*nested*) sangat mungkin dibuat di Python. Namun, pada implementasi proyek riil (*real world cases*), pembuatan folder yang terlalu bertingkat-tingkat umumnya dihindari demi menjaga kesederhanaan dan mencegah kompleksitas navigasi struktur proyek yang berlebihan.

---

### B. Perbedaan Metode Impor pada Package (*Deep Import* vs *Shallow Import*)

- **Deep Import**: Metode pengimporan di mana pengembang harus merujuk nama modul dan rute jalurnya secara lengkap hingga ke tingkat berkas modul paling dalam untuk memanggil fungsi tertentu.
    - *Sintaksis*: `from package.module import function`
    - *Karakteristik*: Mengharuskan pengguna package memahami detail internal struktur folder dan nama berkas modul yang spesifik.
- **Shallow Import**: Metode pengimporan praktis langsung di tingkat folder package utama tanpa perlu merujuk nama berkas modul secara mendalam.
    - *Sintaksis*: `from package import function`
    - *Karakteristik*: Struktur internal didelegasikan ke berkas `__init__.py` yang bertugas memetakan dan mengekspos (*expose*) fungsi-fungsi terpilih ke permukaan package agar langsung dapat digunakan oleh berkas utama.

| Karakteristik Perbandingan | Deep Import | Shallow Import |
|:--|:--|:--|
| **Konstruksi Impor** | Rute impor panjang hingga ke file `.py` spesifik | Rute impor pendek langsung ke folder package utama |
| **Pengetahuan Struktur** | Pengembang wajib tahu nama berkas modul internal secara detail | Pengembang cukup memanggil langsung dari nama package utama |
| **Kerapian Kode** | Lebih panjang dan kompleks jika struktur folder sangat dalam | Lebih bersih, ringkas (*concise*), dan mudah dibaca |
| **Ketergantungan `__init__.py`** | Tetap berjalan meskipun berkas `__init__.py` kosong | Wajib mengonfigurasi ekspos fungsi di dalam `__init__.py` |

> [!warning] Audio Insight — Konsekuensi Tanpa Inisialisasi dan Efisiensi Kerja Tim
> Dosen mendemonstrasikan bahwa jika baris ekspor di dalam berkas `__init__.py` dimatikan (misalnya dikomentari), maka perintah impor ringkas (*Shallow Import*) akan memicu kesalahan sistem berupa `NameError` atau `cannot import name 'clean_text' from 'utils'`. Tanpa deklarasi eksplisit di dalam `__init__.py`, Python akan selalu memaksa pengembang menggunakan jalur impor panjang (*longer form*) yang berbelit-belit.
>
> Pembagian modul di dalam package (seperti memisahkan fungsi ke dalam `clean.py`, `encoder.py`, dan `standardizer.py`) sangat mempermudah kolaborasi paralel dalam tim. Dosen mencontohkan bahwa Developer A (Brian) dapat fokus mengerjakan modul pembersihan teks (`clean.py`), Developer B (Evo) pada modul penyandian (`encoder.py`), dan Developer C (Anwar) pada modul penskalaan data (`standardizer.py`). Meskipun dikerjakan terpisah oleh orang yang berbeda, pengguna akhir (*end-user*) dari package tersebut tidak akan terganggu karena mereka cukup memanggil satu jalur impor ringkas yang sama yang telah disatukan di dalam `__init__.py`.

---

### C. Demonstrasi dan Implementasi Kode

Berikut adalah contoh struktur direktori proyek modular menggunakan konsep package beserta konfigurasi berkas inisialisasi dan pengimporannya pada berkas utama secara aman:

**1. Struktur Direktori Proyek**:

```
ai_project/
├── main.py
└── preprocessing/
    ├── __init__.py
    ├── clean_text.py
    └── encoder.py
```

**2. Isi Berkas Modul `clean_text.py`**:

```python
def standardize_text(text):
    # Melakukan pembersihan teks dasar dengan menghapus spasi di awal/akhir dan mengubah ke huruf kecil
    return text.strip().lower()
```

**3. Isi Berkas Modul `encoder.py`**:

```python
def categorical_encoder():
    print("Encoding categorical features...")
```

**4. Isi Berkas Inisialisasi `__init__.py`**:

```python
# Menentukan fungsi dari modul internal mana saja yang ingin diekspos ke tingkat package
from .clean_text import standardize_text
from .encoder import categorical_encoder
```

**5. Isi Berkas Utama `main.py` (Menggunakan Shallow Import)**:

```python
# Mengimpor fungsi secara ringkas langsung dari tingkat package utama
from preprocessing import standardize_text, categorical_encoder

raw_text = "   Hello World   "
cleaned = standardize_text(raw_text)

print(f"Hasil Clean Text: '{cleaned}'")
categorical_encoder()
```

**Perbandingan langsung Deep Import vs Shallow Import untuk struktur yang sama (ditambahkan):**

```python
# DEEP IMPORT - harus tahu nama file modul internal secara spesifik
from preprocessing.clean_text import standardize_text
from preprocessing.encoder import categorical_encoder

# SHALLOW IMPORT - cukup tahu nama package saja (karena __init__.py sudah mengekspos)
from preprocessing import standardize_text, categorical_encoder
```

> [!tip] Lihat juga
> Pola impor `import nama_library` yang akan sering ditemui saat menyambungkan Python ke database di [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] (misalnya `import mysql.connector` atau `import sqlite3`) sebenarnya adalah *package* pihak ketiga yang strukturnya persis mengikuti konsep Deep Import / Shallow Import di atas.

---

## Bab 6 — Tips Pemrograman Modular (Modular Programming Tips)

### A. Prinsip Desain dan Pengorganisasian (*Design Principles*)

- **Patuhi Prinsip Single Responsibility (*[[Kamus & Cheatsheet (JCAIEH M1)#S|Single Responsibility Principle]]*)**: Setiap file modul atau fungsi hanya boleh bertanggung jawab atas satu tugas atau pekerjaan spesifik. Jangan menggabungkan logika yang tidak berkaitan (seperti pembersihan data dan pelatihan model) ke dalam satu modul tunggal.
- **Atur dengan Struktur Folder yang Jelas (*Clear Folder Structure*)**: Kelompokkan berkas-berkas modul secara logis di dalam direktori proyek agar alur navigasi proyek mudah dipahami oleh anggota tim pengembang lainnya.
- **Gunakan Pelindung `if __name__ == "__main__"`**: Selalu bungkus kode eksekusi utama atau kode pengujian unit di dalam file modul utilitas menggunakan blok pelindung ini. Hal ini memastikan kode uji coba tersebut tidak berjalan secara otomatis saat modul diimpor oleh berkas lain.

> [!warning] Audio Insight — Kepentingan Single Responsibility Principle
> Dosen menekankan bahwa penerapan *Single Responsibility Principle* sangat krusial dalam proyek tim berskala besar. Ketika terjadi kegagalan sistem pada proses pembersihan data, pengembang dapat langsung melacak dan memperbaiki kesalahan tersebut hanya pada berkas `preprocessing.py`. Proses pemeliharaan ini menjadi sangat efisien karena tidak ada risiko kode pelatihan model di berkas `model.py` atau berkas orkestrasi di `main.py` ikut terganggu.

---

### B. Praktik Terbaik Menghindari Masalah Teknis (*Technical Best Practices*)

- **Hindari Impor Melingkar (*[[Kamus & Cheatsheet (JCAIEH M1)#C|Avoid Circular Imports]]*)**: Impor melingkar terjadi ketika `file_A.py` mengimpor `file_B.py`, sementara pada saat yang sama `file_B.py` juga mengimpor `file_A.py`. Hal ini harus dihindari karena akan membingungkan interpreter Python dan memicu kesalahan urutan eksekusi (*execution order errors*).
- **Gunakan Parameter dan Hindari Hardcoding (*Pass Parameters & Avoid Hardcoding*)**: Jangan menuliskan nilai, nama berkas, atau konfigurasi secara statis (*[[Kamus & Cheatsheet (JCAIEH M1)#H|hardcoding]]*) di dalam modul fungsional. Sebaliknya, gunakan argumen atau parameter dinamis agar modul dapat digunakan kembali secara fleksibel untuk berbagai kumpulan data yang berbeda.
- **Tambahkan Berkas `__init__.py` untuk Packages**: Selalu sertakan berkas inisialisasi `__init__.py` di dalam folder modul Anda. Hal ini dilakukan untuk mendeklarasikan folder tersebut secara eksplisit sebagai sebuah *Package* resmi dan mengaktifkan metode pengimporan yang rapi (*cleaner import*).

| Aturan Praktis | Tujuan Utama | Contoh Penerapan / Solusi |
|:--|:--|:--|
| **Single Responsibility** | Menjaga fokus satu tugas per file | Memisahkan file `data.py` dari `preprocessing.py` |
| **Avoid Circular Imports** | Mencegah error eksekusi melingkar | Mendesain jalur impor searah (file A mengimpor file B, tetapi tidak sebaliknya) |
| **Avoid Hardcoding** | Menjaga modularitas tetap fleksibel | Menggunakan fungsi `load_data(file_path)` alih-alih mengunci nama file di dalam fungsi |
| **Use `__init__.py`** | Mendeklarasikan folder sebagai package | Membuat berkas kosong `__init__.py` di dalam direktori modul |

> [!warning] Audio Insight — Bahaya Hardcoding dan Penyelesaian Circular Import
> Dosen mencontohkan bahwa jika kita menuliskan langsung nama berkas secara statis di dalam modul fungsional (misalnya langsung mengunci nama berkas `sales_2024.csv` di dalam fungsi pembaca data), fungsi tersebut akan menjadi kaku. Ketika data berganti menjadi `sales_2025.csv` pada tahun berikutnya, pengembang terpaksa harus membongkar dan mengubah kode di dalam modul tersebut. Solusi terbaik adalah melewatkan nama berkas sebagai parameter dinamis ke dalam fungsi (seperti `load_data(file_name)`), sehingga modul tetap fleksibel dan tidak perlu diubah kembali di masa mendatang.
>
> Untuk menghindari kegagalan eksekusi akibat impor melingkar, pengembang harus menyusun ketergantungan antar-modul secara linear atau searah. Jika dua modul membutuhkan fungsi satu sama lain, fungsi-fungsi tersebut sebaiknya dipecah kembali ke dalam modul utilitas ketiga yang netral untuk diimpor oleh kedua modul tersebut.

**Contoh hardcoding vs parameter dinamis (ditambahkan):**

```python
# BURUK: hardcoding nama file di dalam fungsi
def load_data_buruk():
    with open("sales_2024.csv", "r") as f:
        return f.read()
# Setiap tahun ganti nama file -> harus edit fungsi ini

# BAIK: nama file dilewatkan sebagai parameter
def load_data(file_name):
    with open(file_name, "r") as f:
        return f.read()

load_data("sales_2024.csv")
load_data("sales_2025.csv")   # tidak perlu ubah fungsi sama sekali
```

**Contoh circular import dan solusinya (ditambahkan):**

```python
# file_A.py
# from file_B import fungsi_b   # file_A butuh sesuatu dari file_B

# file_B.py
# from file_A import fungsi_a   # file_B butuh sesuatu dari file_A
# -> ImportError / circular import saat salah satu file dijalankan

# SOLUSI: pindahkan fungsi yang dibutuhkan bersama ke modul netral ketiga
# file_utils.py
def fungsi_bersama():
    pass

# file_A.py dan file_B.py sama-sama mengimpor dari file_utils.py, bukan dari satu sama lain
```

---

### C. Batasan dan Evaluasi Kebutuhan Modularisasi

- **Pertimbangan Kompleksitas**: Modularisasi pada dasarnya memperkenalkan sedikit kompleksitas tambahan pada struktur proyek (seperti pengelolaan direktori, file inisialisasi, penentuan jalur impor, dan hubungan antar-modul).
- **Prinsip Evaluasi**: Jika program yang sedang dibangun sangat sederhana, berukuran kecil, dan hanya berupa skrip sekali pakai (*one-off script*), pemrograman modular tidak perlu dipaksakan. Pendekatan satu file tunggal (*monolithic*) justru lebih efisien untuk kasus-kasus sederhana guna menghindari kompleksitas yang tidak mendatangkan manfaat nyata (*unnecessary complexity*).

> [!tip] Audio Insight — Jangan Over-Engineering
> Dosen mengingatkan mahasiswa untuk tidak terlalu ekstrem dalam melakukan modularisasi (*over-engineering*). Sebelum memecah program menjadi banyak modul, selalu lakukan evaluasi terlebih dahulu mengenai skala proyek yang dikerjakan. Modularisasi adalah sebuah investasi jangka panjang untuk keteraturan struktur kode; jika keuntungan keteraturan tersebut tidak melebihi beban kompleksitas pengelolaan berkas yang baru, maka pertahankan struktur file tunggal yang sederhana.

---

## Bab 7 — Latihan Praktis (Practice Exercises)

### A. Latihan 1: Basic (Create Your First Module)

- **Tujuan Skenario**: Mahasiswa diarahkan untuk memecah logika pemrograman tunggal menjadi struktur modular sederhana dengan memisahkan fungsi utilitas perhitungan nilai siswa ke dalam modul terpisah dan memanggilnya melalui berkas eksekusi utama.
- **Spesifikasi Modul (`grades_utils.py`)**:
    - `calc_average(scores)`: Menerima masukan berupa daftar nilai (*list of numbers*) dan mengembalikan nilai rata-rata yang dibulatkan hingga dua angka di belakang desimal.
    - `get_grade(average)`: Menentukan huruf mutu berdasarkan nilai rata-rata dengan ketentuan klasifikasi standar.
- **Skema Klasifikasi Nilai**:

| Batas Nilai Rata-Rata | Huruf Mutu (*Grade*) |
|:--|:--|
| Lebih besar atau sama dengan 90 | A |
| Lebih besar atau sama dengan 80 | B |
| Lebih besar atau sama dengan 70 | C |
| Lebih besar atau sama dengan 60 | D |
| Di bawah 60 | E |

**Implementasi Kode Sumber**:

```python
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

```python
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

> [!warning] Audio Insight — Demonstrasi Mahasiswa dan Dukungan Tipe Objek Modul
> **Demonstrasi Mahasiswa**: Brian mempresentasikan kode miliknya di depan kelas, menggunakan fungsi bawaan `round(..., 2)` untuk membatasi presisi nilai desimal rata-rata tepat dua angka di belakang koma guna memenuhi spesifikasi tugas.
>
> **Dukungan Tipe Objek Modul**: Atas pertanyaan Stepen, dosen mengonfirmasi secara eksplisit bahwa modul Python bersifat fleksibel. Modul tidak hanya terbatas untuk membungkus fungsi (*functions*), melainkan dapat menampung definisi kelas (*classes*) maupun variabel di dalamnya.

---

### B. Latihan 2: Intermediate (Control Execution with `__name__`)

- **Tujuan Skenario**: Mengontrol eksekusi kode pada modul utilitas menggunakan pelindung eksekusi (*name guard*) untuk memisahkan logika pengujian internal dari logika aplikasi utama.
- **Spesifikasi Tugas**: Menambahkan baris cetak uji coba (*test print* atau *self test*) secara langsung di dalam berkas `grades_utils.py` menggunakan kondisional `if __name__ == "__main__":`.
- **Perbandingan Ekspektasi Eksekusi**:

| Konteks Eksekusi Berkas | Hasil Output yang Diharapkan | Status Blok Guard |
|:--|:--|:--|
| Berkas `grades_utils.py` dijalankan secara langsung | Menampilkan pesan *self test* dan hasil pengujian lokal | Dieksekusi (*True*) |
| Berkas `grades_utils.py` diimpor ke berkas `main.py` | Berkas utama berjalan normal tanpa menampilkan pesan pengujian lokal | Dilewati (*False*) |

**Implementasi Kode Sumber**:

```python
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

> [!warning] Audio Insight — Demonstrasi Mahasiswa (Adiba)
> Mbak Adiba membagikan layar pengujiannya yang menunjukkan bahwa kode pengujian lokal yang dibungkus di dalam kondisional `if __name__ == "__main__":` berhasil disembunyikan secara otomatis saat berkas utama `main.py` dijalankan, sehingga mencegah polusi konsol akibat tereksekusinya pengujian yang tidak diinginkan (*unwanted execution*).

---

### C. Latihan 3: Advanced (Build a Package)

- **Tujuan Skenario**: Mereorganisasi kode penilai siswa ke dalam satu struktur folder paket (*Package*) bernama `grades` untuk mengaktifkan pengimporan praktis tingkat permukaan (*Shallow Import*) menggunakan bantuan file inisialisasi `__init__.py`.
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
    - `loader.py`: Menyediakan fungsi `get_scores()` untuk mengambil data nilai siswa (dalam skenario ini mengembalikan data list statis).
    - `calculator.py`: Menyediakan fungsi `calculate_average(scores)` dan `get_grade(average)`.
    - `report.py`: Menyediakan fungsi `print_report()` yang bertugas mengoordinasikan seluruh alur pemuatan data, kalkulasi, hingga pencetakan laporan ke konsol.

**Implementasi Kode Sumber**:

```python
# grades/loader.py
def get_scores():
    return [80, 90, 75]
```

```python
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

```python
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

```python
# grades/__init__.py
# Mengekspos fungsi spesifik ke tingkat package (Shallow Import)
from grades.calculator import get_grade
from grades.report import print_report
```

```python
# main.py
# Melakukan Shallow Import langsung dari tingkat package 'grades'
from grades import get_grade, print_report

# Menguji fungsionalitas laporan yang terkoordinasi
print_report()
```

**Output yang dihasilkan (ditambahkan):**

```
----- STUDENT GRADE REPORT -----
Raw Scores    : [80, 90, 75]
Average Score : 81.67
Final Grade   : B
```

> [!warning] Audio Insight — Optimalisasi Overhead dan Pertanyaan Desain Bersarang
> Dosen memberikan koreksi penting pada berkas `report.py`. Disarankan untuk menampung pemanggilan fungsi `get_scores()` ke dalam sebuah variabel lokal (misalnya `scores = get_scores()`) alih-alih memanggil fungsinya secara berulang di baris kode berikutnya. Memanggil fungsi yang sama berkali-kali akan menimbulkan beban komputasi tambahan (*overhead*) yang tidak efisien. Menampung nilai ke dalam variabel lokal membantu program berjalan lebih cepat dan menjaga kerapian penulisan kode (*readability*).
>
> Menjawab keingintahuan Stepen mengenai apakah package bisa dibuat bertingkat (*nested packages*), dosen menjelaskan bahwa dalam praktik industri nyata, struktur paket yang terlalu dalam (*deeply nested*) sangat jarang digunakan karena memperumit manajemen jalur impor (*path management*). Struktur datar yang rapi dan terukur jauh lebih direkomendasikan.

---

### D. Algoritma Terperinci: `calc_average` dan `get_grade`

Bagian ini merinci langkah demi langkah algoritma dari dua fungsi utilitas yang dipakai di ketiga latihan Bab 7 di atas — berguna untuk latihan berpikir algoritmik sebelum menuliskan kode.

**1. Algoritma Fungsi `calc_average(scores)`**

Fungsi ini bertujuan untuk menghitung nilai rata-rata dari daftar nilai yang diberikan dan membulatkannya.

1. **Menerima Input**: Sebuah daftar (list) berisi angka-angka nilai, kita sebut sebagai `scores`.
2. **Validasi Data Kosong**:
    - Periksa apakah list `scores` tersebut kosong atau tidak.
    - **Jika kosong**, langsung kembalikan nilai **0.0** (langkah ini penting untuk menghindari error pembagian dengan nol / *ZeroDivisionError*).
3. **Proses Perhitungan**:
    - **Langkah A**: Hitung jumlah total seluruh nilai di dalam list (`sum`).
    - **Langkah B**: Hitung banyaknya data atau jumlah elemen di dalam list (`length`).
    - **Langkah C**: Bagi hasil **Langkah A** dengan **Langkah B** untuk mendapatkan nilai rata-rata kasar.
4. **Pembulatan**: Bulatkan hasil nilai rata-rata tersebut hingga **2 angka di belakang koma**.
5. **Kembalikan Hasil (Output)**: Kirimkan nilai rata-rata yang sudah dibulatkan tersebut kembali ke program utama (`main.py`).

**Implementasi lengkap dengan validasi data kosong (ditambahkan — versi `calc_average` di Bab 7.A/B/C di atas belum menyertakan validasi ini secara eksplisit):**

```python
def calc_average(scores):
    if len(scores) == 0:      # Langkah 2: validasi data kosong
        return 0.0             # menghindari ZeroDivisionError

    total = sum(scores)         # Langkah A
    count = len(scores)         # Langkah B
    average = total / count     # Langkah C
    return round(average, 2)    # Langkah 4-5: pembulatan dan return

print(calc_average([80, 90, 75]))   # Output: 81.67
print(calc_average([]))              # Output: 0.0 (tanpa error)
```

**2. Algoritma Fungsi `get_grade(average)`**

Fungsi ini menentukan huruf mutu (grade) berdasarkan nilai rata-rata menggunakan logika percabangan (*conditional statement*).

1. **Menerima Input**: Sebuah angka desimal/integer yang merupakan nilai rata-rata, kita sebut sebagai `average`.
2. **Evaluasi Kondisi (dari nilai tertinggi ke terendah)**:
    - **Kondisi 1**: Apakah `average` **lebih besar dari atau sama dengan 90**? Jika **Ya**, tentukan grade = **"A"**. Selesai.
    - **Kondisi 2**: Jika tidak, apakah `average` **lebih besar dari atau sama dengan 80**? Jika **Ya**, tentukan grade = **"B"**. Selesai.
    - **Kondisi 3**: Jika tidak, apakah `average` **lebih besar dari atau sama dengan 70**? Jika **Ya**, tentukan grade = **"C"**. Selesai.
    - **Kondisi 4**: Jika tidak, apakah `average` **lebih besar dari atau sama dengan 60**? Jika **Ya**, tentukan grade = **"D"**. Selesai.
    - **Kondisi 5 (Pilihan Terakhir)**: Jika semua kondisi di atas tidak terpenuhi (nilai di bawah 60): tentukan grade = **"E"**. Selesai.
3. **Kembalikan Hasil (Output)**: Kirimkan huruf grade yang terpilih kembali ke program utama.

> [!tip] Mengapa urutan `if/elif` dari tertinggi ke terendah itu penting
> Karena begitu satu kondisi `True`, Python langsung berhenti mengevaluasi kondisi lain di bawahnya (persis seperti prinsip prioritas `if/elif` yang dibahas di [[Sesi 05 - Python Function and File Handling (JCAIEH M1)|Sesi 05 - Python Function and File Handling]] Bab 3.4.A). Jika urutannya dibalik (mulai dari `average >= 60` di atas), maka nilai 95 pun akan langsung "tertangkap" sebagai grade D di kondisi pertama — salah total. Urutan tertinggi ke terendah memastikan setiap angka jatuh ke kategori yang benar-benar paling sesuai.

---

### E. Materi Tambahan & Catatan Diskusi Kuliah

#### 1. Manajemen Pembaruan Repositori Git

- **Kasus Kendala**: Mahasiswa sering melakukan kloning ulang seluruh repositori secara penuh (*git clone*) saat pengajar memperbarui bahan ajar atau latihan baru di GitHub, yang mana tindakan ini tidak praktis.
- **Solusi Perintah**: Mahasiswa cukup membuka terminal, mengarahkan direktori aktif ke dalam folder repositori lokal yang lama, lalu menjalankan perintah git pull:

```bash
git pull
```

Perintah ini akan secara otomatis mendeteksi perubahan terbaru di repositori GitHub pengajar dan mengunduh berkas atau folder baru secara cepat tanpa merusak pekerjaan lokal yang telah dimodifikasi.

> [!tip] Lihat juga
> `git pull` melengkapi perintah-perintah dasar Git (`git add`, `git commit`, `git push`, `git clone`) yang sudah dibahas di [[Sesi 02 - Intro to Git and GitHub (JCAIEH M1)|Sesi 02 - Intro to Git and GitHub]].

#### 2. Persiapan Pertemuan Berikutnya: Pengenalan Perkakas SQL

Pada sesi berikutnya, materi perkuliahan akan beralih ke pembahasan SQL (*Structured Query Language*). Dosen menyarankan mahasiswa untuk menyiapkan perkakas manajemen basis data.

**Rekomendasi Perkakas Evaluasi**:

| Nama Perkakas (*Tools*) | Ruang Lingkup Dukungan | Karakteristik Penggunaan |
|:--|:--|:--|
| **MySQL Workbench** | Khusus untuk MySQL saja | Antarmuka grafis (UI) resmi untuk berinteraksi dengan server basis data MySQL. |
| **DBeaver** | Mendukung multi-basis data (*Database agnostic*) | Sangat direkomendasikan karena mendukung berbagai jenis basis data (MySQL, PostgreSQL, Google BigQuery, dll.). Perkakas ini sangat populer di industri karena fleksibilitasnya dalam mengelola berbagai ekosistem basis data yang berbeda secara bersamaan dalam satu aplikasi. |

> [!tip] Lihat juga
> Kedua perkakas ini menjadi pintu masuk pembahasan [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] — sesi berikutnya setelah sesi ini.

---

## 🔗 Terkait

- [[Sesi 07 - Object Oriented Programming (JCAIEH M1)|Sesi 07 - Object Oriented Programming]] — class seperti `BankAccount` yang dibuat di Sesi 07 idealnya diletakkan di file modul terpisah, dan mekanisme `if __name__ == "__main__"` yang diperkenalkan sekilas di sana dibahas menyeluruh di sesi ini sebagai *name guard*.
- [[Sesi 02 - Intro to Git and GitHub (JCAIEH M1)|Sesi 02 - Intro to Git and GitHub]] — konsep branch/merge Git yang dibahas di Sesi 02 menjadi jauh lebih efektif digunakan justru karena pemrograman modular (kerja paralel per file mengurangi merge conflict).
- [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] — pola `import mysql.connector`/`import sqlite3` di Sesi 09 adalah package pihak ketiga yang strukturnya mengikuti konsep Deep Import/Shallow Import di sesi ini.
