---
tags: [module1, sesi-05, python, function, scope, file-handling, recursion]
aliases: ["Sesi 5"]
---

# Session 5 — Python Function & File Handling

Study guide ini membahas konsep dasar dan lanjutan mengenai *function* di Python (definisi, parameter, `return`, `lambda`, *nested/callback/recursive function*), konsep *namespace* dan *scope* (`global`, `nonlocal`), serta manipulasi berkas eksternal (*file handling*) menggunakan `open()` dan `with` statement.

---

## Bab 1 — Python Function (Fungsi Python)

### 1.1 Definisi dan Konsep Dasar Fungsi (Function Definition)

#### A. Fondasi Konseptual

- **Analogi Resep Masakan**: Sebuah *function* dianalogikan seperti sebuah resep masakan. Resep tersebut menentukan bahan-bahan yang dibutuhkan (*inputs*), langkah-langkah pembuatan yang harus diikuti (*logic*), serta hidangan hasil akhir yang akan didapatkan (*output*).
- **Prinsip Sekali Tulis**: Mendefinisikan sebuah *function* setara dengan menuliskan resep masakan lalu menyerahkannya kepada Python. Setelah resep tersebut dipahami oleh Python, kita hanya perlu memanggil namanya kapan pun membutuhkan hasil yang sama, tanpa harus menulis ulang langkah-langkah logika tersebut dari awal.

#### B. Karakteristik Utama

- **Blok Kode Terorganisir**: *Function* adalah blok kode terpisah yang dirancang khusus untuk mengeksekusi satu tugas spesifik secara berulang (*specific task*).
- **Keyword Pendefinisian**: Di dalam Python, pembuatan *function* dapat dilakukan menggunakan dua kata kunci utama, yaitu kata kunci `def` atau kata kunci `lambda`.

> [!warning] Audio Insight — Kapan Harus Membuat Function
> Dosen menekankan bahwa *function* dibuat untuk membungkus kode yang akan dijalankan berulang kali. Apabila suatu proses hanya akan dijalankan satu kali saja di dalam seluruh rangkaian program, maka pembuatan *function* sebenarnya tidak terlalu krusial atau tidak dibutuhkan. Tujuan utamanya adalah melakukan generalisasi langkah-langkah logis agar program menjadi lebih efisien.

---

### 1.2 Fungsi Bawaan (Built-In Function)

#### A. Karakteristik Built-In Function

- **Langsung Tersedia**: Python menyediakan sejumlah fungsi yang siap digunakan secara langsung sejak interpreter Python dijalankan.
- **Tanpa Konfigurasi Tambahan**: Pengguna tidak perlu mendefinisikan logika fungsi tersebut secara manual atau mengimpor (*import*) modul eksternal apa pun sebelum memanggilnya.

#### B. Daftar Istilah Built-In Function

| Nama Built-In Function | Karakteristik / Deskripsi Singkat |
|:--|:--|
| `print()` | Menampilkan data atau teks hasil komputasi ke layar atau konsol. |
| `len()` | Menghitung panjang atau jumlah elemen di dalam suatu objek koleksi data. |
| `input()` | Menerima baris input teks langsung dari pengguna melalui keyboard. |
| `range()` | Menghasilkan urutan angka numerik berdasarkan interval tertentu. |

**Contoh gabungan (ditambahkan sebagai pelengkap, tidak ada di sumber asli):**

```python
nama = input("Siapa nama kamu? ")   # menerima input dari keyboard
jumlah_huruf = len(nama)             # menghitung panjang string

for i in range(3):                   # range(3) -> 0, 1, 2
    print(f"Halo {nama}, ini pengulangan ke-{i}")

print(f"Nama kamu punya {jumlah_huruf} huruf.")
# Contoh jika nama = "Budi":
# Halo Budi, ini pengulangan ke-0
# Halo Budi, ini pengulangan ke-1
# Halo Budi, ini pengulangan ke-2
# Nama kamu punya 4 huruf.
```

---

### 1.3 Fungsi dengan Kata Kunci def (Function with def)

#### A. Sintaksis dan Pembuatan Objek

- **Sintaks Standar**: Pendefinisian standar menggunakan kata kunci `def` diikuti dengan nama fungsi, tanda kurung `()`, titik dua `:`, dan blok kode logika yang menjorok ke dalam (*indented block*).
- **Alokasi Memori**: Saat kita mendefinisikan fungsi menggunakan `def`, Python akan membuat sebuah objek fungsi (*function object*) di memori komputer yang menyimpan seluruh instruksi logika di dalam tubuh fungsi tersebut, kemudian mengaitkan nama fungsi sebagai referensi penunjuk (*pointer*) ke objek tersebut.

#### B. Proses Pemanggilan Fungsi (Calling a Function)

- **Eksekusi Logika**: Untuk mengeksekusi objek fungsi tersebut, kita memanggil namanya diikuti dengan tanda kurung `()`.
- **Transfer Kendali**: Saat fungsi dipanggil, kendali program secara otomatis berpindah (*transfer*) ke blok definisi fungsi untuk mengeksekusi semua baris kode di dalamnya. Setelah seluruh kode selesai dieksekusi, kendali program akan melompat kembali ke pernyataan setelah baris pemanggilan fungsi tersebut.

**Contoh (ditambahkan): perbedaan `greet` vs `greet()` yang dijelaskan di Audio Insight di bawah:**

```python
def greet():
    print("Halo!")

print(greet)     # Output: <function greet at 0x000001A2B3C4D5E0> (referensi objek fungsi)
print(greet())   # Output: Halo!
                  #         None  <- karena print(greet()) mencetak hasil return greet(), yaitu None
```

> [!warning] Audio Insight — Perbedaan Pemanggilan dengan Kurung vs Tanpa Kurung
> Dalam sesi demo, diperlihatkan bahwa jika kita menuliskan nama fungsi tanpa menggunakan tanda kurung (misalnya `print(greet)`), Python hanya akan mengembalikan representasi objek fungsi tersebut beserta alamat memorinya (seperti `<function greet at 0x...>`). Namun, jika dipanggil menggunakan kurung (seperti `greet()`), program akan beralih mengeksekusi logika internalnya.
>
> **Fleksibilitas Input-Output**: Fungsi dapat dirancang tanpa memiliki input maupun output sama sekali. Struktur fungsi fleksibel dan dapat dikategorikan menjadi empat jenis: memiliki input dan output, hanya memiliki input, hanya memiliki output, atau tidak memiliki keduanya.

**Contoh empat jenis fungsi (ditambahkan sebagai pelengkap):**

```python
def tanpa_input_output():         # tidak punya input maupun output
    print("Saya jalan sendiri")

def hanya_input(nama):            # punya input, tidak punya return
    print(f"Halo {nama}")

def hanya_output():                # tidak punya input, tapi punya return
    return "Saya hasil komputasi"

def input_dan_output(a, b):        # punya input dan output
    return a + b

tanpa_input_output()               # Output: Saya jalan sendiri
hanya_input("Sari")                # Output: Halo Sari
print(hanya_output())              # Output: Saya hasil komputasi
print(input_dan_output(2, 3))      # Output: 5
```

---

### 1.4 Fungsi dengan Input (Function with Input)

#### A. Parameter dan Argumen

Untuk meningkatkan fleksibilitas sehingga fungsi dapat menghasilkan keluaran yang dinamis sesuai dengan kondisi penggunaan, kita dapat mendefinisikannya dengan input menggunakan variabel khusus.

| Istilah Teknis | Definisi dan Karakteristik |
|:--|:--|
| *Parameter* | Variabel penampung (*placeholder*) yang dideklarasikan di dalam tanda kurung pada bagian definisi fungsi. |
| *Argument* | Nilai nyata (*actual value*) yang dikirimkan ke fungsi saat fungsi tersebut dipanggil. |

#### B. Nilai Bawaan (Default Value)

- **Fungsi Default**: Kita dapat menentukan nilai bawaan (*default value*) pada parameter fungsi. Jika kita tidak mengirimkan argumen apa pun saat memanggil fungsi tersebut, Python secara otomatis akan menggunakan nilai bawaan yang telah didefinisikan.
- **Sintaks Default Value**: Ditulis dengan format `parameter = value` di dalam kurung definisi fungsi.

**Contoh kode untuk studi kasus `greet(name="Bob", time=None)` (ditambahkan — di sumber hanya dijelaskan dalam prosa):**

```python
def greet(name="Bob", time=None):
    if time:
        print(f"Selamat {time}, {name}!")
    else:
        print(f"Halo, {name}!")

greet()                          # Output: Halo, Bob!
greet("Sari")                    # Output: Halo, Sari!
greet("Sari", "pagi")            # Output: Selamat pagi, Sari!
```

> [!warning] Audio Insight — Studi Kasus Parameter `time=None`
> Pada contoh fungsi `greet(name="Bob", time=None)`, parameter `time` diberi nilai default `None`. Logika internal menggunakan pengkondisian `if time:` untuk mendeteksi apakah argumen `time` dikirimkan oleh pengguna atau tidak. Jika bernilai `None` (yang dievaluasi sebagai *False*), program akan melompat ke blok `else:` dan hanya menyapa nama saja.

---

### 1.5 Pernyataan Kembalian (return Statement)

#### A. Peran return versus print()

- **Batas Tampilan `print()`**: Fungsi `print()` hanya bertugas menampilkan hasil langsung ke layar monitor, sehingga nilai tersebut tidak dapat disimpan atau dimanfaatkan kembali dalam komputasi program.
- **Penyimpanan Hasil dengan `return`**: Pernyataan `return` digunakan untuk mengirimkan nilai kembali (*send a value back*) ke baris tempat fungsi tersebut dipanggil. Nilai ini kemudian dapat disimpan ke dalam variabel, digunakan kembali untuk kalkulasi berikutnya, atau dikirimkan ke fungsi lain.

#### B. Karakteristik Fungsi Berdasarkan Keberadaan return

| Jenis Fungsi | Karakteristik Aliran Data | Hasil jika Ditangkap Variabel |
|:--|:--|:--|
| **Tanpa `return`** | Logika fungsi dieksekusi, nilai hasil komputasi hanya berada di dalam lingkup lokal fungsi tersebut atau dicetak ke layar. | Menghasilkan nilai `None`. |
| **Dengan `return`** | Mengirimkan secara eksplisit nilai hasil perhitungan keluar dari lingkup fungsi menuju pemanggilnya. | Variabel penangkap berhasil menyimpan nilai riil hasil komputasi. |

**Contoh pembanding langsung (ditambahkan):**

```python
def cetak_saja(a, b):
    print(a + b)     # hanya menampilkan, tidak mengembalikan nilai

def kembalikan_hasil(a, b):
    return a + b      # mengirim nilai kembali ke pemanggil

hasil_1 = cetak_saja(2, 3)        # Output tercetak: 5
print(hasil_1)                     # Output: None  <- karena tidak ada return

hasil_2 = kembalikan_hasil(2, 3)  # tidak ada apa pun tercetak di sini
print(hasil_2)                     # Output: 5  <- nilai asli berhasil ditangkap
```

---

### 1.6 Fungsi dengan Kata Kunci lambda (Function with lambda)

#### A. Karakteristik Anonymous Function

- **Fungsi Anonim**: Fungsi yang dibuat menggunakan kata kunci `lambda` adalah fungsi khusus yang tidak memiliki nama (*anonymous function*).
- **Batasan Satu Baris**: Fungsi ini hanya dapat digunakan jika logika di dalamnya sangat sederhana dan dapat dituliskan secara lengkap dalam satu baris ekspresi saja (*single-line expression*).
- **Sintaksis Penulisan**:

```
lambda parameter(s): expression
```

- **Konversi Otomatis**: Semua fungsi standar (`def`) yang hanya memiliki satu baris ekspresi logika di dalamnya dapat dikonversi menjadi fungsi `lambda`.

**Contoh konkret (ditambahkan — sumber hanya menuliskan bentuk sintaksisnya):**

```python
# Versi def
def kali_dua(x):
    return x * 2

# Versi lambda yang setara, disimpan ke variabel
lambda_function = lambda num1, num2: num1 * num2

print(kali_dua(5))               # Output: 10
print(lambda_function(3, 4))     # Output: 12
```

> [!warning] Audio Insight — Penyimpanan Logika ke Variabel & Alternatif Iterasi Manual
> Meskipun `lambda` pada dasarnya adalah fungsi tanpa nama, dalam praktiknya logika tersebut sering disimpan ke dalam sebuah variabel (misalnya `lambda_function = lambda num1, num2:...`) agar variabel tersebut dapat dipanggil seperti fungsi biasa.
>
> Dalam diskusi kelas, dosen mengajukan pertanyaan bagaimana melakukan operasi perkalian setiap elemen list dengan `-2` apabila kita belum memahami fungsi `lambda`. Solusi alternatif yang disepakati adalah menggunakan perulangan (*looping* / *iterator*) dengan membuat list kosong terlebih dahulu, mengalikan setiap elemen satu per satu, dan memasukkannya menggunakan metode `.append()`.

**Kedua pendekatan (ditambahkan sebagai perbandingan konkret):**

```python
angka = [1, 2, 3, 4]

# Pendekatan tanpa lambda (looping manual)
hasil_loop = []
for n in angka:
    hasil_loop.append(n * -2)
print(hasil_loop)                       # Output: [-2, -4, -6, -8]

# Pendekatan dengan lambda + map()
hasil_lambda = list(map(lambda n: n * -2, angka))
print(hasil_lambda)                     # Output: [-2, -4, -6, -8]
```

> [!tip] Lihat juga
> `map()` dengan `lambda` juga dipakai secara intensif untuk parsing input di [[Sesi 06 - Hackerrank Exercise]] (misalnya `map(int, input().split())`), dan `lambda` sebagai kunci `sorted()` untuk multi-kriteria sorting juga dibahas lebih lanjut di sesi tersebut.

---

### 1.7 Praktik Penulisan Fungsi yang Bersih (Writing Clean Functions)

#### A. Aturan Emas Clean Function

Untuk menghasilkan kode program yang mudah dibaca (*readable*), mudah diuji (*testable*), mudah dipelihara (*maintainable*), serta mudah dipahami oleh orang lain, kita harus menerapkan aturan berikut:

1. Menggunakan nama fungsi yang deskriptif (*descriptive function name*).
2. Menggunakan nama parameter yang bermakna (*meaningful parameter name*).
3. Menentukan petunjuk tipe data (*type hint*) untuk parameter input dan nilai kembalian (*return value*).
4. Menyediakan dokumentasi deskriptif yang jelas (*docstring*) untuk menerangkan fungsionalitas blok kode tersebut.

#### B. Studi Kasus Perbandingan Keterbacaan

Perbandingan visual dilakukan antara fungsi `calc()` yang ditulis buruk dan fungsi `get_median()` yang ditulis dengan kaidah *clean function* untuk menghitung nilai tengah (*median*) dari sebuah list.

- **Fungsi calc() (Buruk/Membingungkan)**: menggunakan nama fungsi `calc()` yang terlalu umum dan tidak deskriptif; nama parameter menggunakan singkatan `lst` tanpa petunjuk tipe data; variabel penampung di dalamnya disingkat menjadi `mid1` dan `mid2` tanpa penjelasan; tidak memiliki dokumentasi (*docstring*) sehingga sulit dipahami maksudnya secara instan.
- **Fungsi get_median() (Sangat Baik/Bersih)**: menggunakan nama fungsi `get_median()` yang sangat jelas; menetapkan *type hint* pada parameter input (`data: list`) dan tipe data hasil kembalian (`-> float`); dilengkapi *docstring* tiga tanda petik `"""` yang menjelaskan tugas fungsi, deskripsi argumen yang dibutuhkan, serta apa yang dikembalikan.

**Contoh implementasi konkret dari kedua gaya (ditambahkan — sumber hanya mendeskripsikan perbedaannya, tanpa kode literal):**

```python
# Versi buruk
def calc(lst):
    lst = sorted(lst)
    mid1 = len(lst) // 2
    mid2 = (len(lst) - 1) // 2
    return (lst[mid1] + lst[mid2]) / 2

# Versi bersih (clean function)
def get_median(data: list) -> float:
    """
    Menghitung nilai tengah (median) dari sekumpulan angka.

    Args:
        data (list): daftar angka yang akan dicari mediannya.

    Returns:
        float: nilai median dari data tersebut.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid_high = n // 2
    mid_low = (n - 1) // 2
    return (sorted_data[mid_high] + sorted_data[mid_low]) / 2

print(get_median([7, 1, 3]))        # Output: 3.0
print(get_median([7, 1, 3, 9]))     # Output: 5.0
```

> [!warning] Audio Insight — Sifat Type Hint di Python & Penanganan Error pada Input Non-List
> Berdasarkan pertanyaan mahasiswa di kelas mengenai batasan tipe data pada *type hint*, dosen menegaskan bahwa *type hint* di Python **tidak memicu error secara otomatis saat runtime** jika tipe data yang dimasukkan berbeda (misalnya kita memasukkan string pada fungsi yang ditandai dengan tipe data list). *Type hint* murni bersifat sebagai panduan dokumentasi (*documentation aid*) untuk membantu programmer, rekan kerja, maupun agen AI memahami struktur input-output yang diharapkan tanpa harus menelusuri isi logika di dalam fungsi tersebut.
>
> Ketika mendiskusikan pembatasan input tipe data pada fungsi `process_data(data: list) -> list`, seorang mahasiswa bertanya mengenai perilaku program apabila diinputkan data selain `list` dan bagaimana cara menangani error tersebut. Dosen menjelaskan bahwa di luar pemeriksaan petunjuk tipe data, penanganan error (*error handling*) dapat diimplementasikan menggunakan blok konstruksi `try` dan `except`. Ketika proses pemanggilan fungsi diletakkan di dalam blok `try` dan terjadi kesalahan tipe data (*type error* atau kesalahan komputasi lainnya), kesalahan tersebut akan ditangkap (*catch*) oleh blok `except` sehingga program tidak langsung terhenti secara tidak normal.

**Contoh pembuktian bahwa type hint TIDAK memicu error (ditambahkan):**

```python
def process_data(data: list) -> list:
    return data

# Type hint mengatakan "data harus list", tapi Python tetap menjalankannya
# meskipun kita mengirim string, karena type hint hanya dokumentasi, bukan validasi.
hasil = process_data("bukan list")
print(hasil)          # Output: bukan list  (tidak ada error!)

# Untuk benar-benar menangani input yang salah, gunakan try/except:
def process_data_aman(data: list) -> list:
    try:
        return [x * 2 for x in data]
    except TypeError:
        return "Error: input tidak bisa diproses sebagai list"

print(process_data_aman([1, 2, 3]))   # Output: [2, 4, 6]
print(process_data_aman(5))            # Output: Error: input tidak bisa diproses sebagai list
```

---

## Bab 2 — Python Namespace and Scope (Namespace dan Ruang Lingkup)

### 2.1 Konsep Namespace (Ruang Nama)

#### A. Fondasi Konseptual Namespace

- **Definisi**: *Namespace* adalah sebuah area penyimpanan berlabel yang bertugas melacak nama-nama (*names*) yang kita buat di dalam program beserta objek (*objects*) yang dirujuk oleh nama-nama tersebut.
- **Analogi Loker Penyimpanan**: *Namespace* dapat dianalogikan seperti area penyimpanan berlabel di mana Python menyimpan nama variabel atau nama fungsi sebagai label penunjuk (*pointer*) ke nilai atau objek data yang sesungguhnya di memori komputer.

#### B. Tiga Tingkatan Namespace

- **Built-in Namespace**: Berisi nama bawaan yang disediakan langsung oleh Python. *Namespace* ini otomatis dibuat saat interpreter Python dijalankan dan langsung tersedia di seluruh bagian program tanpa memerlukan konfigurasi atau impor modul eksternal (contoh: `print()`, `range()`, `input()`, `len()`).
- **Global Namespace**: Berisi nama-nama variabel, fungsi, atau kelas yang didefinisikan secara umum di tingkat program utama (tingkat modul atau file aktif).
- **Local Namespace**: Berisi nama-nama yang didefinisikan secara khusus di dalam tubuh suatu fungsi. *Namespace* ini bersifat sementara; hanya dibuat saat fungsi dieksekusi dan akan dihapus dari memori begitu fungsi selesai dijalankan.

---

### 2.2 Konsep Scope (Ruang Lingkup)

#### A. Definisi Scope

- **Definisi**: *Scope* adalah aturan yang menentukan di bagian mana saja suatu nama atau variabel yang telah dibuat dapat diakses secara langsung di dalam kode program.
- **Aturan Akses**: Keberadaan sebuah variabel di dalam *Namespace* tertentu tidak menjamin variabel tersebut dapat dibaca dari mana saja. Aturan *Scope* membatasi visibilitas variabel untuk menjaga integritas data dalam program.

#### B. Perbandingan Variabel Global dan Lokal

| Karakteristik Perbandingan | Global Variable | Local Variable |
|:--|:--|:--|
| **Lokasi Pendefinisian** | Dibuat di luar tubuh fungsi (tingkat modul/file utama). | Dibuat di dalam tubuh fungsi tertentu. |
| **Aksesibilitas Langsung** | Dapat diakses dari bagian mana pun di dalam file yang sama (baik di dalam maupun di luar fungsi). | Hanya dapat diakses dari dalam tubuh fungsi tempat variabel tersebut didefinisikan. |
| **Siklus Hidup (*Lifetime*)** | Bertahan selama seluruh rangkaian program utama berjalan. | Hanya bertahan selama fungsi tempat ia didefinisikan sedang dieksekusi. |

**Contoh yang menunjukkan variabel bernama sama di scope berbeda (ditambahkan sesuai deskripsi Audio Insight di bawah):**

```python
message = "Halo dari global"     # variabel global

def tampilkan_pesan():
    message = "Halo dari lokal"   # variabel lokal, BEDA dengan yang global
    print(message)                 # Output: Halo dari lokal

tampilkan_pesan()
print(message)                     # Output: Halo dari global (tidak berubah)
```

> [!warning] Audio Insight — Variabel dengan Nama Sama di Scope Berbeda
> Dalam sesi diskusi tanya jawab, muncul pertanyaan mengenai apakah penamaan variabel boleh sama di tingkatan *scope* yang berbeda. Berdasarkan demonstrasi langsung di kelas, diperlihatkan bahwa penamaan variabel yang sama diperbolehkan. Jika ada variabel bernama `message` di lingkup global dan variabel bernama `message` di lingkup lokal fungsi, Python memperlakukannya sebagai dua variabel yang sepenuhnya berbeda. Saat fungsi dieksekusi, Python memprioritaskan variabel lokal terlebih dahulu. Setelah fungsi selesai berjalan, program akan kembali merujuk pada nilai variabel global di luar fungsi tanpa terjadi tumpang tindih.

---

### 2.3 Kata Kunci global (global Keyword)

#### A. Fungsi global Keyword

- **Tujuan Penggunaan**: Di dalam Python, *global keyword* digunakan untuk memberikan instruksi eksplisit kepada interpreter agar menggunakan dan memodifikasi variabel yang berada di lingkup global (*global scope*) dari dalam konteks lokal fungsi.
- **Sintaksis Deklarasi**:

```python
global variable_name
```

#### B. Konsekuensi UnboundLocalError

- **Pemicu Error**: Apabila kita mencoba mengubah nilai (*reassign/modify*) sebuah variabel global secara langsung di dalam fungsi tanpa mendeklarasikan kata kunci `global`, Python secara otomatis akan menganggap variabel tersebut sebagai variabel lokal baru.
- **Mekanisme Kegagalan**: Saat program mencoba melakukan operasi perubahan nilai (misalnya `position += 1`), Python akan mencari definisi awal variabel lokal tersebut di dalam fungsi. Karena nilai awalnya tidak ditemukan di lingkup lokal, interpreter akan menghentikan eksekusi program dan melempar kesalahan berupa `UnboundLocalError`.

**Kode lengkap studi kasus `position` (ditambahkan — sumber hanya menjelaskan dalam prosa di Audio Insight):**

```python
position = 0

# VERSI BERMASALAH (tanpa global) -> akan menghasilkan UnboundLocalError
def move_forward_error():
    position += 1     # Python menganggap 'position' di sini variabel LOKAL baru
                       # tapi belum pernah didefinisikan di lokal -> Error!

# move_forward_error()  # -> UnboundLocalError: local variable 'position' referenced before assignment

# VERSI YANG BENAR (dengan global)
def move_forward():
    global position    # memberi tahu Python: pakai 'position' yang di global
    position += 1

move_forward()
print(position)        # Output: 1
```

> [!warning] Audio Insight — Studi Kasus Kesalahan Kode `position`
> Dalam sesi demo pemrograman, dosen memperlihatkan contoh variabel global koordinat `position = 0`. Ketika dibuat fungsi `move_forward()` yang di dalamnya langsung berisi kode `position += 1`, program mengalami kegagalan *runtime* dengan pesan `UnboundLocalError`. Masalah ini dipecahkan dengan menambahkan baris deklarasi `global position` di bagian paling atas di dalam tubuh fungsi sebelum melakukan operasi penambahan nilai. Dengan demikian, nilai variabel `position` di tingkat global berhasil diperbarui menjadi `1` ketika fungsi tersebut dipanggil.

---

### 2.4 Kata Kunci nonlocal (nonlocal Keyword)

#### A. Definisi dan Fungsi nonlocal Keyword

- **Tujuan Penggunaan**: Kata kunci `nonlocal` digunakan khusus di dalam fungsi bersarang (*nested function*) untuk memberitahu Python secara eksplisit agar mengakses dan mengubah variabel yang didefinisikan pada fungsi pembungkus terdekat (*nearest enclosing function scope*).
- **Penjembatan Scope**: Keyword ini berfungsi menjembatani perbedaan antara lingkup lokal terdalam dengan lingkup lokal satu tingkat di atasnya, tanpa harus menaikkan variabel tersebut ke tingkat modul global yang terlalu tinggi.

#### B. Karakteristik Penggunaan nonlocal

- **Khusus Nested Function**: Kata kunci `nonlocal` hanya valid dan hanya dapat bekerja di dalam struktur fungsi bersarang (*nested function*). Penggunaannya di luar struktur ini akan menyebabkan kesalahan sintaksis.
- **Menghindari Duplikasi Memori**: Deklarasi keyword ini memastikan bahwa Python tidak menginisialisasi variabel lokal baru di dalam fungsi terdalam, melainkan langsung memanipulasi variabel milik fungsi pembungkusnya di memori komputer.

**Kode lengkap studi kasus `fun()`/`gun()` (ditambahkan — sumber hanya menjelaskan dalam prosa di Audio Insight), dibandingkan dengan versi yang salah pakai `global`:**

```python
def fun():
    x = 10

    def gun():
        nonlocal x    # merujuk 'x' milik fun(), BUKAN variabel global
        x += 5
        print(f"Di dalam gun(), x = {x}")

    gun()
    print(f"Di dalam fun() setelah gun() dipanggil, x = {x}")

fun()
# Output:
# Di dalam gun(), x = 15
# Di dalam fun() setelah gun() dipanggil, x = 15

# Bandingkan jika salah menggunakan 'global' padahal x bukan variabel global:
def fun_salah():
    x = 10

    def gun_salah():
        global x       # Python akan mencari 'x' di GLOBAL, bukan di fun_salah()
        x += 5          # karena 'x' global belum pernah dibuat -> membuat 'x' global BARU

    gun_salah()
    print(f"x di dalam fun_salah tetap: {x}")  # Output: 10 (tidak berubah, karena gun_salah mengubah x GLOBAL yang berbeda)

fun_salah()
print(f"x di luar (global), muncul karena 'global x' tadi: {x}")  # Output: 15
```

> [!warning] Audio Insight — Asal-Usul nonlocal dalam Diskusi Kelas
> Pembahasan mengenai keyword `nonlocal` berawal dari pertanyaan mahasiswa yang menanyakan keberadaan alternatif kata kunci selain `global` untuk fungsi bersarang. Dosen bersama mahasiswa kemudian mengeksplorasi dokumentasi mengenai skenario fungsi bersarang `fun()` yang di dalamnya mendefinisikan fungsi `gun()`. Diperlihatkan bahwa apabila kita ingin agar perubahan variabel di dalam fungsi terdalam `gun()` ikut mengubah nilai variabel di fungsi pembungkus `fun()`, kita harus menggunakan keyword `nonlocal`. Jika kita menggunakan keyword `global`, Python justru akan mencari variabel tersebut di tingkat teratas modul file (luar fungsi `fun()`), yang dapat menyebabkan error jika variabel global tersebut memang tidak pernah dibuat sejak awal.

---

## Bab 3 — Nested, Callback, and Recursive Function (Fungsi Bersarang, Callback, dan Rekursif)

### 3.1 Nested Function (Fungsi Bersarang)

#### A. Konsep Dasar dan Lingkup Akses

- **Definisi**: *Nested Function* adalah praktik mendefinisikan suatu fungsi pembantu (*helper function*) di dalam tubuh fungsi utama (*enclosing function*).
- **Alokasi dan Lingkup**: Fungsi bagian dalam (*inner function*) hanya akan diciptakan dan dialokasikan di memori saat fungsi utama sedang dieksekusi. Begitu fungsi utama selesai dijalankan, fungsi bagian dalam tersebut akan dihapus dari memori.
- **Batasan Akses**: Karena didefinisikan di dalam lingkup lokal fungsi utama, *nested function* murni bersifat lokal dan tidak dapat diakses atau dipanggil secara langsung dari lingkup global (di luar fungsi utama).
- **Studi Kasus Perhitungan Pajak**: Implementasi fungsi pembantu `add_tax` yang didefinisikan di dalam fungsi utama `calculate_total` untuk menambahkan komponen pajak sebesar 11% pada setiap harga barang.

```python
def calculate_total(prices):
    tax_rate = 0.11

    def add_tax(price):
        return price * (1 + tax_rate)

    total = 0
    for price in prices:
        total += add_tax(price)
    return total

print(calculate_total([100, 200, 300]))   # Output: 666.0
```

#### B. Karakteristik Utama Nested Function

- **Enclosing Scope Access**: Fungsi bagian dalam memiliki hak akses langsung untuk membaca variabel-variabel yang dideklarasikan pada lingkup fungsi luar (seperti variabel `tax_rate`).
- **Encapsulation (Enkapsulasi)**: Menyembunyikan fungsionalitas spesifik yang hanya relevan bagi fungsi utama, mencegah polusi nama fungsi pada lingkup global.

> [!warning] Audio Insight — Proteksi Logika Internal
> Berdasarkan hasil demo di kelas, apabila kita mencoba memanggil fungsi `add_tax()` secara langsung dari lingkup luar program, Python akan memicu kesalahan (*error*) karena nama fungsi tersebut tidak terdaftar di lingkup global (*NameError*). Logika internal ini sepenuhnya terproteksi di dalam fungsi pembungkusnya.

```python
# Pembuktian NameError (ditambahkan)
# add_tax(100)   # -> NameError: name 'add_tax' is not defined
```

---

### 3.2 Callback Function (Fungsi Callback)

#### A. Konsep Dasar dan Fleksibilitas Kode

- **Definisi**: *Callback Function* adalah sebuah fungsi yang dilewatkan sebagai argumen atau nilai input ke dalam fungsi lain.
- **Mekanisme Kerja**: Fungsi penerima bertindak sebagai pengontrol aliran utama, sementara logika operasi spesifik didelegasikan kepada fungsi callback yang dikirimkan. Fungsi penerima dapat mengeksekusi fungsi callback tersebut kapan saja di dalam tubuh logikanya saat diperlukan.
- **Studi Kasus Kalkulator Multi-Operasi**: Fungsi `kalkulator` dirancang sebagai pengendali utama yang menerima parameter `operasi` berupa fungsi callback, serta dua operand `a` dan `b`.

```python
def tambah(a, b):
    return a + b

def kurang(a, b):
    if a >= b:
        return a - b
    else:
        return b - a

def kalkulator(operasi, a, b):
    return operasi(a, b)

print(kalkulator(tambah, 1, 3))   # Output: 4
print(kalkulator(kurang, 1, 3))   # Output: 2
```

#### B. Karakteristik Penggunaan Callback

- **Modularitas Tinggi**: Kita dapat dengan mudah menambahkan fungsi operasi baru (seperti perkalian atau pembagian) tanpa perlu mengubah struktur logika internal pada fungsi `kalkulator`.
- **Dinamis**: Eksekusi logika di dalam fungsi utama sepenuhnya bergantung pada fungsi callback mana yang dikirimkan saat pemanggilan dilakukan.

> [!warning] Audio Insight — Aturan Pemanggilan Tanpa Kurung
> Dosen memberikan penekanan penting mengenai sintaksis pemanggilan. Saat melemparkan fungsi sebagai argumen (misalnya `kalkulator(tambah, 1, 3)`), nama fungsi `tambah` harus dituliskan **tanpa tanda kurung `()`**. Jika dituliskan dengan kurung, Python akan mengeksekusi fungsi tersebut terlebih dahulu dan mengirimkan nilai hasilnya, bukan referensi objek fungsinya. Tanda kurung baru diaplikasikan di dalam tubuh fungsi penerima (`operasi(a, b)`).

```python
# Pembuktian perbedaan (ditambahkan)
kalkulator(tambah, 1, 3)     # BENAR: mengirim fungsi 'tambah' sebagai referensi
# kalkulator(tambah(1, 3), 1, 3)  # SALAH secara konsep: tambah(1,3) dieksekusi dulu jadi 4,
                                   # lalu kalkulator akan mencoba memanggil 4(1, 3) -> TypeError: 'int' object is not callable
```

---

### 3.3 Recursive Function (Fungsi Rekursif)

#### A. Konsep Dasar dan Cara Kerja

- **Definisi**: *Recursive Function* adalah fungsi yang memecahkan masalah komputasi dengan cara memanggil dirinya sendiri secara berulang-ulang.
- **Strategi Penyelesaian**: Pendekatan rekursif membagi satu masalah besar menjadi serangkaian sub-masalah sejenis yang berukuran lebih kecil, menyelesaikannya secara bertahap, lalu menggabungkan kembali hasilnya.
- **Komponen Mutlak**: Setiap fungsi rekursif wajib memiliki dua komponen utama:
    1. *Base Case* (*Stopping Condition*): Kondisi batas dasar yang dievaluasi menggunakan percabangan `if` untuk menghentikan pemanggilan diri sendiri.
    2. *Recursive Case*: Bagian logika di mana fungsi memanggil dirinya sendiri dengan argumen yang nilainya semakin mendekati *Base Case*.
- **Studi Kasus Hitung Mundur (Countdown)**: Fungsi `countdown` menerima sebuah bilangan, mencetaknya, lalu memanggil dirinya sendiri dengan nilai bilangan yang dikurangi 1 hingga menyentuh angka 1.

```python
def countdown(num):
    print(num)
    if num > 1:
        countdown(num - 1)

countdown(3)
# Output:
# 3
# 2
# 1
```

#### B. Perbandingan Karakteristik Rekursif dan Iterasi

| Karakteristik Perbandingan | Fungsi Rekursif | Iterasi Biasa (Looping) |
|:--|:--|:--|
| **Mekanisme Pengulangan** | Pemanggilan fungsi ke dirinya sendiri secara berulang. | Menggunakan instruksi `for` atau `while`. |
| **Kondisi Berhenti** | Ditentukan secara eksplisit pada pernyataan *Base Case*. | Ditentukan oleh kondisi terminasi loop yang bernilai `False`. |
| **Efisiensi Memori** | Lebih boros memori (membutuhkan ruang untuk *Call Stack*). | Sangat efisien (variabel kontrol diperbarui pada alamat memori yang sama). |
| **Risiko Kegagalan** | Menyebabkan crash sistem akibat kehabisan memori *stack*. | Mengakibatkan program berjalan tanpa henti (*infinite loop*). |

> [!warning] Audio Insight — Bahaya Konsumsi Memori (Stack Overflow) & Tower of Hanoi
> Dalam sesi pemaparan, dosen mengingatkan dampak fatal apabila fungsi rekursif ditulis tanpa memiliki *stopping condition* yang valid. Setiap kali fungsi memanggil dirinya sendiri, Python akan membuka bingkai memori baru di dalam *call stack*. Jika pemanggilan terjadi tanpa batas (*infinite call*), memori RAM komputer akan terkuras habis dengan sangat cepat, yang mengakibatkan program langsung mengalami crash atau hang.
>
> Masalah pemindahan cakram klasik seperti *Tower of Hanoi* yang sempat dibahas merupakan contoh nyata di mana pendekatan rekursif memberikan solusi penulisan kode yang jauh lebih sederhana, elegan, dan mudah dipahami dibandingkan dengan perulangan iteratif yang membutuhkan logika pelacakan posisi sangat rumit.

**Contoh recursion tanpa base case yang valid (ditambahkan, JANGAN dijalankan — hanya ilustrasi bahaya `RecursionError`):**

```python
def countdown_bahaya(num):
    print(num)
    countdown_bahaya(num - 1)   # tidak ada 'if' untuk berhenti!

# countdown_bahaya(3)  # -> akan terus turun ...2, 1, 0, -1, -2... sampai
#                         RecursionError: maximum recursion depth exceeded
```

---

### 3.4 Panduan dan Implementasi Latihan Mandiri (Exercises)

Sesi latihan mandiri di kelas berfokus pada penerapan fungsi dinamis, penanganan parameter default, serta optimasi logika matematika.

#### A. Latihan 1: Luas Lingkaran Fleksibel (get_circle_area)

**Deskripsi Tugas**: Buatlah fungsi `get_circle_area` yang menerima parameter `radius` dan `diameter` yang masing-masing bernilai default `None`. Fungsi harus menghitung luas lingkaran berdasarkan input yang dikirimkan. Jika kedua input diberikan sekaligus, prioritaskan penggunaan `radius`. Hasil akhir wajib dibulatkan ke dalam 3 angka desimal.

```python
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

print(get_circle_area(radius=5))          # Output: 78.54
print(get_circle_area(diameter=10))       # Output: 78.54
print(get_circle_area(radius=5, diameter=100))  # Output: 78.54 (radius diprioritaskan)
```

> [!warning] Audio Insight — Penyusunan Aliran Kondisi (Prioritas)
> Logika prioritas diselesaikan dengan menaruh pengecekan `radius is not None` pada blok `if` paling atas. Sifat pengeksekusian percabangan di Python memastikan bahwa jika kondisi pertama bernilai `True`, blok di bawahnya (`elif` diameter) akan dilewati sepenuhnya. Hal ini menjamin parameter radius selalu diutamakan secara otomatis.

#### B. Latihan 2: Konverter Suhu (convert_temperature)

**Deskripsi Tugas**: Buatlah fungsi `convert_temperature` yang menerima input nilai temperatur (`temp`) dan unit skalanya (`unit` berupa string `"C"` atau `"F"`). Kembalikan nilai hasil konversi suhu yang sesuai.

```python
def convert_temperature(temp, unit):
    if unit == "C":
        return (temp * 9/5) + 32
    elif unit == "F":
        return (temp - 32) * 5/9
    else:
        raise ValueError("Unit skala tidak valid. Gunakan 'C' atau 'F'.")

print(convert_temperature(100, "C"))   # Output: 212.0
print(convert_temperature(32, "F"))    # Output: 0.0
```

> [!warning] Audio Insight — Penerapan Error Handling
> Untuk mengantisipasi input unit yang tidak valid (misalnya pengguna memasukkan selain huruf "C" atau "F"), sangat disarankan untuk mengimplementasikan pelemparan pengecualian (*raising exception*) berupa `ValueError` agar sistem tidak menghasilkan kalkulasi yang salah saat eksekusi runtime.

#### C. Latihan 3: Analisis Bilangan Bulat Komprehensif (analyze_number)

**Deskripsi Tugas**: Buatlah fungsi `analyze_number` yang menganalisis sebuah bilangan bulat untuk:
1. Menentukan apakah angka tersebut bernilai positif, negatif, atau nol.
2. Menentukan apakah angka tersebut ganjil (*odd*) atau genap (*even*).
3. Khusus untuk bilangan positif, periksa apakah angka tersebut termasuk bilangan prima (*prime*) atau bukan.
4. Gabungkan seluruh hasil analisis ke dalam satu pesan teks terformat.

```python
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

print(analyze_number(7))    # Output: Prime and odd
print(analyze_number(8))    # Output: Positive and even
print(analyze_number(-3))   # Output: Negative and odd
print(analyze_number(0))    # Output: Zero
```

> [!warning] Audio Insight — Optimasi Matematika, Modularitas, dan Bug Perulangan (Adiba Live Coding Case)
> Pada sesi pembahasan live coding, diperlihatkan teknik optimasi pencarian bilangan prima menggunakan batas nilai akar kuadrat (`int(n**0.5) + 1`). Penggunaan metode ini menghemat siklus perulangan secara drastis dibandingkan melakukan iterasi penuh hingga `n-1`, terutama untuk nilai angka pengujian yang sangat besar.
>
> Memisahkan pengecekan prima ke dalam fungsi pembantu eksternal `is_prime()` merupakan praktik penulisan kode bersih yang sangat direkomendasikan (*Separation of Concerns*). Kode menjadi lebih mudah dibaca dan diuji secara terisolasi.
>
> Dalam sesi analisis kegagalan kode siswa, diidentifikasi bug di mana bilangan prima salah dideteksi karena peletakan pernyataan `return True` yang salah ditaruh di dalam blok perulangan `for` loop secara tidak sengaja. Kesalahan ini menyebabkan loop langsung berhenti pada iterasi pertama tanpa menguji angka pembagi lainnya. Solusinya adalah memindahkan pernyataan `return True` ke luar blok perulangan `for` untuk memastikan seluruh rentang angka pembagi selesai diuji secara menyeluruh.

**Ilustrasi bug tersebut secara konkret (ditambahkan):**

```python
# VERSI SALAH (bug 'return True' di dalam loop)
def is_prime_salah(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i != 0:
            return True    # BUG: berhenti di percobaan pembagi PERTAMA saja!
    return False

print(is_prime_salah(9))   # Output SALAH: True (padahal 9 = 3x3, bukan prima)
                             # karena 9 % 2 != 0 langsung return True, tanpa sempat cek 9 % 3

# VERSI BENAR: 'return True' dipindah ke LUAR loop (lihat is_prime() di atas)
print(is_prime(9))         # Output BENAR: False
```

---

## Bab 4 — Working with External Files in Python (Bekerja dengan File Eksternal)

### 4.1 Fondasi Konseptual File Eksternal

#### A. Penyimpanan Sementara versus Permanen

- **Batas Variabel**: Selama program dijalankan, data disimpan secara sementara (*temporary*) di dalam memori RAM menggunakan variabel. Begitu interpreter Python dimatikan atau program selesai dieksekusi, seluruh data tersebut akan terhapus sepenuhnya.
- **Peran File Eksternal**: Berkas eksternal memungkinkan program untuk menyimpan data secara permanen (*persistently*) ke dalam media penyimpanan fisik (seperti Hard Disk atau SSD). Program dapat membaca kembali data tersebut kapan saja bahkan setelah komputer dimatikan.

#### B. Alur Interaksi File di Python

- **Membuka (Open)**: Menghubungkan program Python dengan sistem penyimpanan sistem operasi menggunakan fungsi bawaan `open()`. Langkah ini menghasilkan objek file (*file object*) atau penunjuk (*file handler*) di memori.
- **Memproses (Read/Write)**: Melakukan manipulasi isi file seperti mengambil data (*reading*) atau memasukkan data baru (*writing*).
- **Menutup (Close)**: Memutuskan koneksi berkas eksternal menggunakan metode `.close()` untuk membebaskan sumber daya memori dan mengunci kembali berkas agar tidak terjadi korupsi data (*data corruption*).

> [!tip] Lihat juga
> Pola "buka koneksi → proses → tutup koneksi" ini akan muncul lagi dalam bentuk yang sangat mirip saat menyambungkan Python ke database di [[Sesi 09 - Intro to Database and SQL]] (membuka *connection*, menjalankan query, lalu menutup koneksi).

---

### 4.2 Membuka File (Opening a File)

#### A. Sintaksis Dasar Fungsi open()

```python
file_object = open(filepath, mode)
```

#### B. Karakteristik Mode Akses File

| Mode | Nama Operasi | Deskripsi Karakteristik | Perilaku terhadap Berkas |
|:--|:--|:--|:--|
| `"r"` | *Read* | Membuka file khusus untuk dibaca. | Berkas yang dituju wajib sudah ada sebelumnya di direktori. Jika tidak ada, Python akan memicu kesalahan *FileNotFoundError*. |
| `"w"` | *Write* | Membuka file khusus untuk ditulis. | Jika berkas sudah ada, seluruh isi lamanya akan dihapus total (*truncated* / ditimpa). Jika berkas belum ada, berkas baru akan otomatis dibuat. |
| `"a"` | *Append* | Membuka file untuk ditambahkan datanya di bagian paling akhir. | Nilai baru akan ditulis mulai dari baris akhir tanpa merusak atau menghapus data lama. Jika berkas belum ada, berkas baru otomatis dibuat. |

---

### 4.3 Membaca dan Menulis File (Reading and Writing a File)

#### A. Operasi Tulis (write)

```python
file = open("data.txt", "w")
file.write("Hello, Python!")
file.close()
```

#### B. Operasi Baca (read)

```python
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```

> [!warning] Audio Insight — Karakter Newline `\n`
> Dalam sesi demonstrasi kelas, mahasiswa menanyakan perihal penggunaan karakter garis miring terbalik (*backslash*) diikuti huruf n (`\n`) yang disisipkan di dalam kode string. Dosen menjelaskan bahwa itu adalah karakter khusus (*escape character*) untuk merepresentasikan instruksi pindah baris (*enter* / *newline*). Jika karakter ini tidak disertakan, teks yang ditulis berikutnya akan menempel pada baris yang sama.

**Contoh perbandingan langsung (ditambahkan):**

```python
f = open("contoh.txt", "w")
f.write("Baris 1")
f.write("Baris 2")     # tanpa \n
f.close()
# Isi contoh.txt: "Baris 1Baris 2"  <- menempel jadi satu baris!

f2 = open("contoh2.txt", "w")
f2.write("Baris 1\n")
f2.write("Baris 2\n")   # dengan \n
f2.close()
# Isi contoh2.txt:
# Baris 1
# Baris 2
```

---

### 4.4 Pernyataan with (with Statement)

#### A. Risiko Lupa Menutup File

Saat membuka file secara manual menggunakan `open()`, berkas tersebut akan tetap berada dalam status terkunci oleh proses sistem operasi sebelum metode `.close()` dipanggil. Jika program mengalami eror sebelum baris `.close()` dieksekusi, atau jika programmer lupa menuliskan metode `.close()`, berkas tersebut berisiko mengalami kebocoran memori (*memory leak*) atau kerusakan data.

#### B. Manajemen Otomatis dengan with Statement

Di Python, pendekatan terbaik (*best practice*) untuk menangani manipulasi file adalah menggunakan pernyataan `with`. Pernyataan ini menjamin bahwa berkas akan ditutup secara otomatis oleh sistem begitu aliran eksekusi keluar dari blok indentasi `with`, bahkan jika terjadi kesalahan (*exception*) di tengah jalan. Programmer tidak perlu lagi memanggil metode `.close()` secara manual.

```python
# Sintaks standar pembacaan file dengan with statement
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# Di luar blok indentasi ini, file sudah otomatis tertutup dengan aman
```

---

### 4.5 Latihan Mandiri Manipulasi File (Exercises)

Di akhir sesi kuliah, mahasiswa ditantang untuk menyelesaikan skenario dunia nyata yang mengintegrasikan pembuatan fungsi bersih dengan penulisan berkas eksternal.

#### Latihan 4: Program Menyimpan Faktur Belanja (Invoice Saver)

Mahasiswa diminta membuat program interaktif yang menanyakan jumlah buah yang dibeli, meminta nama buah, harga, serta kuantitasnya, lalu menyimpan kalkulasi tersebut secara terstruktur ke dalam file bernama `invoice.txt`.

> [!warning] Audio Insight — Strategi List of Dictionary & Kustomisasi Layout Penulisan
> Dalam sesi demo pengerjaan oleh mahasiswa (Ivo), data input dibungkus terlebih dahulu ke dalam tipe data terstruktur berupa list yang berisi kamus (*list of dictionary*). Struktur ini mempermudah pelacakan data sebelum ditulis ke media fisik.
>
> Untuk memisahkan visualisasi antar item buah di dalam berkas teks, mahasiswa menggunakan logika pemeriksaan pengkondisian. Jika item yang sedang diproses dalam perulangan bukan merupakan item terakhir (`item != items[-1]`), maka program akan menyisipkan karakter enter ganda (`\n\n`) untuk menciptakan jarak pemisah yang rapi. Penulisan ke file dieksekusi secara efisien menggunakan blok `with open("invoice.txt", "w")`.

**Contoh implementasi lengkap (ditambahkan berdasarkan deskripsi Audio Insight di atas — sumber tidak menyertakan kode literalnya):**

```python
items = []
n = int(input("Berapa jenis buah yang dibeli? "))

for _ in range(n):
    nama = input("Nama buah: ")
    harga = int(input("Harga satuan: "))
    qty = int(input("Kuantitas: "))
    items.append({"nama": nama, "harga": harga, "qty": qty, "total": harga * qty})

with open("invoice.txt", "w") as file:
    for item in items:
        file.write(f"Nama: {item['nama']}\n")
        file.write(f"Quantity: {item['qty']}\n")
        file.write(f"Total: {item['total']}")
        if item != items[-1]:      # bukan item terakhir -> beri jarak
            file.write("\n\n")
```

#### Latihan 5: Menghitung Total Belanja dan Diskon (Invoice Reader and Discount)

Mahasiswa diminta membuat fungsi `get_total(list_of_price, discount)` yang bertugas mengambil atau membaca daftar harga total belanja dari berkas `invoice.txt` yang sudah dibuat pada Latihan 4, menjumlahkannya, lalu mengembalikan nilai akhir belanja setelah dikurangi persentase diskon yang ditentukan.

> [!warning] Audio Insight — Pola Integrasi Aliran Data (Data Flow)
> Proses pemecahan masalah dilakukan dengan membagi tugas ke dalam fungsi khusus. Fungsi utama (seperti `read_prices_and_get_total()`) bertugas melakukan pembacaan file `invoice.txt` menggunakan `with open` dalam mode `"r"`, mengekstrak nilai angka total belanja dari string teks, menyimpannya ke dalam list, lalu mengirimkan list tersebut ke dalam fungsi kalkulator `get_total(list_of_price, discount)` untuk mendapatkan harga bersih setelah diskon.

**Contoh implementasi lengkap (ditambahkan, konsisten dengan pola parsing "Total" berjarak 3 baris yang dipakai di [[Sesi 06 - Hackerrank Exercise]]):**

```python
def get_total(list_of_price, discount):
    subtotal = sum(list_of_price)
    return subtotal * (1 - discount / 100)

def read_prices_and_get_total(filepath, discount):
    prices = []
    with open(filepath, "r") as file:
        lines = file.readlines()
        for i in range(2, len(lines), 3):   # baris "Total:" muncul setiap 3 baris
            total_line = lines[i]
            price = int(total_line.split()[-1])
            prices.append(price)
    return get_total(prices, discount)

print(read_prices_and_get_total("invoice.txt", discount=10))
```

> [!tip] Lihat juga
> Pola parsing baris "Total" dengan langkah 3 baris (`range(2, len(lines), 3)`) di atas persis sama dengan pola yang dipakai untuk soal *invoice* di [[Sesi 06 - Hackerrank Exercise]] Bab 1 — keduanya adalah dua versi latihan dari kasus yang sama.
