---
tags: [module1, sesi-03, python, conditional, loop, boolean, if-else, for-loop, while-loop]
aliases: ["Sesi 3", "Conditional and Loop Statement"]
---

# Session 3 — Conditional & Loop Statement

Catatan sesi ketiga ini mencakup review 5 studi kasus latihan mandiri (konversi suhu, konversi jarak, ganjil-genap, hapus kemunculan pertama, palindrome), review Boolean/comparison/logical operators, struktur kondisional (`if`, `if-else`, `if-elif-else`, _nested if_), perulangan (`for`, `while`, `break`, `continue`, `else` pada loop), hingga pembahasan 4 soal latihan akhir sesi.

---

## Bab 1 — Tinjauan dan Pembahasan Exercise Mandiri (Sesi Diskusi Awal)

### 1.1 Studi Kasus 1: Konversi Suhu (Fahrenheit ke Celsius)

**Fondasi Konseptual:**

- **Fungsi (Function):** dideklarasikan menggunakan kata kunci `def`. Fungsi merupakan blok kode terorganisir yang menerima masukan, memprosesnya, dan dapat mengembalikan nilai.
- **Parameter:** variabel lokal yang didefinisikan dalam tanda kurung pada deklarasi fungsi (misalnya `fahrenheit`) untuk menampung argumen yang dikirim saat fungsi dipanggil.
- **Mekanisme Return:** kata kunci `return` digunakan untuk mengirimkan kembali nilai hasil perhitungan di dalam fungsi kepada baris kode yang memanggil fungsi tersebut.

**Implementasi menggunakan fungsi:**

```python
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_degree = convert_to_celsius(95)
print(celsius_degree)  # Output: 35.0
```

**Implementasi tanpa fungsi (langsung/serial):**

```python
fahrenheit = 95
celsius_degree = (fahrenheit - 32) * 5/9
print(celsius_degree)  # Output: 35.0
```

> [!tip] Audio Insight — Aliran Eksekusi Pemrograman: `def` Tidak Langsung Berjalan
> Python mengeksekusi baris kode secara berurutan (serial) dari atas ke bawah. Deklarasi fungsi dengan kata kunci `def` tidak langsung menjalankan logika di dalamnya, melainkan hanya menyimpannya dalam memori. Komputasi baru berjalan ketika fungsi tersebut dipanggil secara eksplisit dengan mengirimkan argumen angka.

> [!warning] Audio Insight — Bahaya Penggunaan Alat Bantu AI Otomatis bagi Pemula
> Penggunaan ekstensi bantu pengodean otomatis (inline suggestion seperti GitHub Copilot) sangat tidak disarankan bagi pemula yang sedang mempelajari dasar pemrograman Python. Rekomendasi otomatis (auto-complete) membuat siswa tidak melatih kemampuan pemecahan masalah (_problem-solving_) secara mandiri.

### 1.2 Studi Kasus 2: Konversi Jarak (Centimeter ke Kilometer)

**Fondasi Konseptual:**

- **Fungsi `input()`:** mengambil masukan teks dari pengguna. Hasil kembalian `input()` secara default selalu bertipe data string (teks).
- **Float Type Casting:** pengubahan tipe data string hasil `input()` secara eksplisit menjadi tipe data desimal (float) agar dapat diproses dalam perhitungan matematika.
- **Manual Concatenation:** menggabungkan string dan variabel menggunakan operator `+`. Mewajibkan konversi tipe data non-string ke string secara manual menggunakan `str()` untuk menghindari error.
- **F-String (Literal String Interpolation):** sintaksis modern dengan awalan huruf `f` sebelum tanda petik string, memungkinkan penyisipan variabel langsung di dalam string menggunakan `{}` tanpa perlu konversi tipe manual.

| Karakteristik | Manual Concatenation (`+`) | F-String (`f"..."`) |
| --- | --- | --- |
| Sintaksis | Menggunakan operator `+` di luar tanda petik | Menggunakan penampung `{}` langsung di dalam string |
| Konversi Tipe Data | Wajib menggunakan `str()` untuk variabel numerik | Konversi ke string terjadi otomatis secara internal |
| Penanganan Spasi | Spasi harus disisipkan secara manual di dalam teks petik | Spasi mengikuti tata letak teks normal di dalam string |
| Tingkat Kerawanan Eror | Tinggi (rawan salah sintaksis dan Type Error) | Rendah (ringkas dan mudah dibaca) |

**Implementasi dengan F-String:**

```python
cm = float(input("Masukkan ukuran dalam satuan centimeter: "))
km = cm / 100000.0
print(f"Ukuran {cm} cm sama dengan {km} km")
```

**Implementasi dengan Manual Concatenation:**

```python
cm = float(input("Masukkan ukuran dalam satuan centimeter: "))
km = cm / 100000.0
print("Ukuran " + str(cm) + " cm = " + str(km) + " km")
```

> [!warning] Audio Insight — Penyebab TypeError pada Concatenation
> Kegagalan berupa `TypeError: can only concatenate str (not "float") to str` terjadi jika programmer memaksakan penggabungan variabel bertipe desimal (float) dengan teks menggunakan operator `+` tanpa membungkusnya terlebih dahulu dengan fungsi `str()`.

> [!warning] Audio Insight — Spasi Manual yang Terlupakan pada Concatenation
> Pada metode manual concatenation, jika programmer lupa menambahkan karakter spasi di dalam string sebelum operator `+`, maka teks hasil cetakan pada konsol akan menempel tanpa jarak.

### 1.3 Studi Kasus 3: Fungsi Pengecekan Bilangan Ganjil dan Genap

**Fondasi Konseptual:**

- **Operator Modulo (`%`):** operator aritmetika yang menghasilkan sisa pembagian dari operasi pembagian dua bilangan bulat.
- **Logika Ganjil/Genap:** bilangan bulat `n` disebut ganjil jika `n % 2 != 0`. Sebaliknya, disebut genap jika `n % 2 == 0`.

**Perbandingan `return` vs `print()`:**

| Karakteristik | Pernyataan `return` | Fungsi `print()` |
| --- | --- | --- |
| Fungsi Utama | Mengembalikan nilai hasil perhitungan ke pemanggil fungsi | Menampilkan teks secara visual ke layar terminal |
| Sifat Nilai | Nilai yang dikembalikan dapat ditampung ke dalam variabel | Tidak menghasilkan nilai yang dapat diolah (mengembalikan `None`) |
| Aliran Kontrol | Menghentikan seluruh proses eksekusi di dalam fungsi seketika | Hanya menampilkan data tanpa memengaruhi aliran kode fungsi |

**Implementasi menggunakan `return`:**

```python
def check_odd_even(n):
    if n % 2 != 0:
        return "odd"
    else:
        return "even"

number_input = int(input("Masukkan angka bulat: "))
result = check_odd_even(number_input)
print(f"Hasil pemeriksaan: Angka {number_input} adalah {result}")
```

**Implementasi menggunakan `print()` langsung:**

```python
def print_odd_even(n):
    if n % 2 != 0:
        print("odd")
    else:
        print("even")

number_input = int(input("Masukkan angka bulat: "))
print_odd_even(number_input)
```

> [!tip] Audio Insight — Interoperabilitas Nilai via `return`
> Penggunaan `return` sangat dianjurkan agar nilai keluaran fungsi dapat dikonsumsi atau digunakan kembali oleh instruksi logika lain di bagian program luar.

> [!warning] Audio Insight — Menangkap Fungsi Tanpa `return` Menghasilkan `None`
> Jika pemanggilan fungsi yang tidak memiliki pernyataan `return` dipaksakan untuk ditampung ke dalam variabel (misalnya `result = print_odd_even(number_input)`), variabel tersebut akan bernilai kosong atau bertipe data `None`.

```python
# Demonstrasi konsekuensi menangkap fungsi tanpa return
hasil_tangkapan = print_odd_even(4)  # akan tetap mencetak "even" ke layar
print(hasil_tangkapan)                # Output: None
```

### 1.4 Studi Kasus 4: Penghapusan Karakter Pertama (Remove First Occurrence)

**Fondasi Konseptual:**

- **Kemunculan Pertama (First Occurrence):** substring target yang ditemukan pertama kali saat string dipindai dari arah kiri (indeks terkecil) ke kanan.
- **Metode `.replace()`:** metode bawaan objek string Python untuk mengganti substring tertentu dengan substring baru. Parameter ketiga mendefinisikan batas maksimal penggantian yang diperbolehkan.

```python
input_string = "Saya akan makan dan akan minum"
search_string = "akan"
result = input_string.replace(search_string, "", 1)
print(result)  # Output: Saya  makan dan akan minum
```

> [!tip] Audio Insight — Sintaksis Penghapusan Karakter dengan String Kosong
> Untuk melakukan penghapusan karakter menggunakan `.replace()`, substring target digantikan dengan _empty string_ atau string kosong yang direpresentasikan dengan sepasang tanda petik tanpa spasi (`""`).

> [!tip] Audio Insight — Mekanisme Kerja Pencarian Indeks pada `.replace()`
> Di bawah sistem Python, string diperlakukan sebagai urutan karakter berindeks mulai dari 0. Ketika `.replace()` dijalankan dengan batasan parameter 1, sistem memindai string dari kiri dan segera mengeksekusi penggantian ketika menemukan kecocokan pertama. Setelah penggantian pertama sukses dilakukan, proses dihentikan sehingga kata "akan" kedua pada kalimat tidak ikut terhapus.

### 1.5 Studi Kasus 5: Pemeriksaan Kata Palindrom

**Fondasi Konseptual:**

- **Definisi Palindrom:** kata atau kalimat yang susunan karakternya tetap sama persis baik dibaca dari depan (normal) maupun dari belakang (terbalik).
- **String Slicing (`[::-1]`):** metode pemotongan terurut menggunakan format indeks `[start:stop:step]`. Nilai `step` negatif `-1` menginstruksikan Python untuk melakukan pemindaian elemen secara mundur (terbalik).
- **Iterable Data Type:** karakteristik string di mana setiap karakter penyusunnya merupakan elemen berurutan yang dapat diakses satu per satu menggunakan nomor indeks.

**Parameter Slicing Python `[start:stop:step]`:**

| Parameter | Peran Utama | Perilaku Jika Dikosongkan |
| --- | --- | --- |
| `start` | Menentukan indeks awal pemotongan | Memulai dari ujung string (ujung kiri jika step positif, ujung kanan jika step negatif) |
| `stop` | Menentukan indeks batas akhir pemotongan (bersifat eksklusif) | Mencakup seluruh elemen hingga ujung string lainnya |
| `step` | Menentukan arah pemindaian dan kelipatan lompatan indeks | Bernilai default `1` (pemindaian normal dari kiri ke kanan) |

```python
word = input("Masukkan kata untuk diperiksa: ")
word_reversed = word[::-1]

if word.lower() == word_reversed.lower():
    print(f"Kata '{word}' tergolong sebagai Palindrom.")
else:
    print(f"Kata '{word}' BUKAN Palindrom.")
```

**Menelusuri `[::-1]` langkah demi langkah** — untuk kata `"madam"` (indeks 0 sampai 4, sesuai zero-based indexing):

| Indeks | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| Karakter | m | a | d | a | m |

`word[::-1]` setara dengan menulis eksplisit `word[len(word)-1 : -(len(word)+1) : -1]`, tapi cukup dibaca sebagai: "mulai dari elemen paling akhir (indeks -1, yaitu `m`), bergerak MUNDUR satu-per-satu MELEWATI SETIAP elemen di antaranya (`a`, `d`, `a`), sampai elemen paling awal (`m`) ikut terbawa karena `stop` dikosongkan." Hasilnya adalah seluruh 5 karakter dibaca terbalik: `"madam"` — bukan hanya elemen di kedua ujung saja.

> [!warning] Audio Insight — Standardisasi Huruf Kecil (`.lower()`) Sebelum Membandingkan
> Karakter huruf kapital dan huruf kecil memiliki nilai representasi biner yang berbeda. Untuk menghindari kegagalan logika perbandingan (misalnya kata "Madam" jika dibalik menjadi "madaM" — huruf besar-kecilnya tidak simetris), seluruh string harus diubah menjadi huruf kecil terlebih dahulu menggunakan `.lower()` sebelum dibandingkan.

> [!tip] Audio Insight — Penyederhanaan Notasi Slicing `[::-1]`
> Penulisan `[::-1]` merupakan bentuk singkat yang secara otomatis memotong string dari indeks paling belakang ke paling depan. Jika ditulis secara eksplisit, parameter `start` diisi dengan panjang string dikurangi satu (`len(word)-1`), parameter `stop` dikosongkan (agar indeks 0 ikut terbawa), dan `step` diisi `-1`.

> [!info] Lihat juga
> Aturan slicing `[start:stop:step]` ini identik untuk `list` dan `tuple`, dibahas lebih dalam dengan tabel indeks positif/negatif di [[Sesi 04 - Data Types Collection Notes]] Bab 5.

---

## Bab 2 — Review Boolean, Comparison, & Logical Operators

### 2.1 Karakteristik dan Definisi Tipe Data Boolean

- **Definisi:** Boolean adalah tipe data primitif yang hanya memiliki dua nilai kebenaran, yaitu `True` dan `False`. Tipe data ini digunakan untuk merepresentasikan hasil dari suatu ekspresi logis.
- **Peran dalam Pemrograman:** nilai Boolean berfungsi sebagai fondasi utama dalam pengambilan keputusan (_decision-making_). Komputer mengevaluasi ekspresi Boolean untuk menentukan jalur eksekusi kode atau blok pernyataan mana yang harus dijalankan berdasarkan kondisi yang terpenuhi.
- **Case Sensitivity:** Python menerapkan aturan penulisan huruf kapital yang ketat untuk konstanta Boolean. Penulisan wajib diawali huruf kapital (`True` dan `False`). Penulisan dengan huruf kecil seluruhnya (`true` atau `false`) akan menyebabkan kegagalan sistem berupa `NameError`.

```python
# Penulisan yang benar
status = True

# Penulisan yang SALAH -> akan memicu NameError: name 'true' is not defined
# status = true
```

> [!tip] Audio Insight — Representasi Evaluasi Logis
> Setiap evaluasi logika dalam Python di balik layar akan dikonversi menjadi salah satu dari dua nilai Boolean tersebut. Nilai ini kemudian dikonsumsi oleh struktur kontrol aliran seperti pernyataan kondisional (`if`, `elif`, `else`) untuk mengarahkan program secara dinamis.

### 2.2 Penerapan Comparison Operators dalam Evaluasi Ekspresi

Operator yang digunakan untuk membandingkan dua buah nilai atau operan. Hasil dari perbandingan ini selalu berupa tipe data Boolean (`True` atau `False`).

| Operator | Nama Operator | Deskripsi Fungsional | Contoh Ekspresi (`x = 5`) | Hasil Evaluasi |
| --- | --- | --- | --- | --- |
| `==` | _Equal to_ | Menghasilkan `True` jika nilai kedua operan sama | `x == 5` | `True` |
| `!=` | _Not equal to_ | Menghasilkan `True` jika nilai kedua operan tidak sama | `x != 8` | `True` |
| `>` | _Greater than_ | Menghasilkan `True` jika nilai operan kiri lebih besar | `x > 3` | `True` |
| `<` | _Less than_ | Menghasilkan `True` jika nilai operan kiri lebih kecil | `x < 3` | `False` |
| `>=` | _Greater than or equal to_ | Menghasilkan `True` jika operan kiri lebih besar atau sama | `x >= 5` | `True` |
| `<=` | _Less than or equal to_ | Menghasilkan `True` jika operan kiri lebih kecil atau sama | `x <= 4` | `False` |

```python
x = 5

print(x == 5)   # Output: True
print(x != 8)   # Output: True
print(x > 10)   # Output: False
print(x <= 5)   # Output: True
```

> [!warning] Audio Insight — Perbedaan Tipe Data dalam Perbandingan (`5 == "5"`)
> Python merupakan bahasa pemrograman yang bersifat _strongly-typed_. Perbandingan nilai angka bertipe data integer dengan string angka (misalnya perbandingan `5 == "5"`) akan menghasilkan nilai `False`. Hal ini dikarenakan Python membandingkan tipe data operan terlebih dahulu sebelum nilainya, sehingga integer `5` dan string `"5"` dianggap tidak setara secara struktural.

```python
print(5 == "5")   # Output: False -> tipe data berbeda (int vs str)
print(5 == 5.0)   # Output: True  -> int dan float dianggap setara jika nilainya sama
```

> [!tip] Audio Insight — Ketiadaan Operator Identitas `===` di Python
> Berbeda dengan beberapa bahasa pemrograman lain (seperti JavaScript) yang menggunakan tiga tanda sama dengan (`===`) untuk mengecek kesamaan nilai dan tipe data sekaligus, Python tidak memiliki operator `===`. Python cukup menggunakan operator `==` untuk membandingkan nilai, karena penanganan tipe data sudah terisolasi secara ketat secara internal.

### 2.3 Mekanisme Penggabungan Kondisi Menggunakan Logical Operators

Operator yang digunakan untuk mengombinasikan atau memanipulasi beberapa ekspresi perbandingan (kondisi) untuk menghasilkan satu nilai Boolean tunggal.

| Operator | Deskripsi Aturan Kebenaran | Contoh Ekspresi (`x = 5`) | Proses Evaluasi Internal | Hasil Akhir |
| --- | --- | --- | --- | --- |
| `and` | Menghasilkan `True` jika **kedua** kondisi bernilai `True` | `x > 3 and x < 10` | `True and True` | `True` |
| `or` | Menghasilkan `True` jika **salah satu** kondisi bernilai `True` | `x < 3 or x == 5` | `False or True` | `True` |
| `not` | Membalikkan nilai Boolean (`True` menjadi `False` dan sebaliknya) | `not (x > 5)` | `not (False)` | `True` |

```python
x = 5

kondisi_and = (x > 3) and (x < 10)
kondisi_or = (x < 3) or (x == 5)
kondisi_not = not (x > 5)

print(f"Hasil AND: {kondisi_and}")  # Output: Hasil AND: True
print(f"Hasil OR: {kondisi_or}")    # Output: Hasil OR: True
print(f"Hasil NOT: {kondisi_not}")  # Output: Hasil NOT: True
```

> [!warning] Audio Insight — Short-Circuit Evaluation pada `and`/`or`
> Python mengevaluasi ekspresi logika dari arah kiri ke kanan.
> - Pada operator `and`, jika kondisi pertama sudah dievaluasi bernilai `False`, Python tidak akan mengevaluasi kondisi kedua karena hasil akhirnya sudah pasti `False` (konsep _short-circuit evaluation_).
> - Pada operator `or`, jika kondisi pertama sudah bernilai `True`, evaluasi akan langsung dihentikan dan menghasilkan nilai `True` tanpa perlu memeriksa kondisi berikutnya.

```python
def cek_dan_print(label, nilai):
    print(f"  -> mengevaluasi {label}")
    return nilai

print("Contoh short-circuit pada 'and':")
hasil = cek_dan_print("kondisi_1 (False)", False) and cek_dan_print("kondisi_2", True)
# Output:
#   -> mengevaluasi kondisi_1 (False)
# kondisi_2 TIDAK PERNAH dievaluasi karena kondisi_1 sudah False
print(hasil)  # Output: False
```

> [!tip] Audio Insight — Gunakan Tanda Kurung pada `not` untuk Kejelasan
> Penggunaan kurung tanda baca pada operator `not` (misalnya `not (x > 5)`) sangat disarankan untuk menegaskan batasan ekspresi mana yang ingin dibalikkan nilainya secara visual agar kode mudah dibaca oleh sesama programmer.

> [!info] Lihat juga
> Ringkasan dasar operator perbandingan dan logika ini pertama kali disinggung secara singkat di [[Sesi 01 - Introduction to DS Python Statistics SQL Git and GitHub]] Bab 5.10.

---

## Bab 3 — Conditional Statement (Pernyataan Kondisional)

### 3.1 Konsep Pengambilan Keputusan (Decision Making) pada Komputer

- **Definisi:** tipe instruksi yang memungkinkan sebuah program komputer untuk melakukan pengambilan keputusan secara otomatis dengan cara mengevaluasi ekspresi tertentu.
- **Evaluasi Boolean:** aliran program ditentukan berdasarkan hasil evaluasi kondisi yang menghasilkan nilai Boolean (`True`/`False`). Jika `True`, blok kode spesifik akan dijalankan; jika `False`, blok kode lain (atau tidak ada kode sama sekali) yang akan dijalankan.

**Representasi Alur Logika (Analogi Kulkas)** — proses memasak sup di dapur dimodelkan sebagai berikut:

1. Seseorang lapar dan berniat memasak, lalu memeriksa bahan masakan di dalam kulkas.
2. **Kondisi Evaluasi:** "Apakah bahan masakan tersedia di dalam kulkas?"
3. **Percabangan Logika:**
   - **Kondisi YES (True):** langsung memulai proses memasak menggunakan bahan yang ada.
   - **Kondisi NO (False):** harus pergi berbelanja bahan makanan terlebih dahulu sebelum bisa memasak.

### 3.2 Struktur Sintaksis `if` dan Aturan Blok Indentasi

- **Pernyataan `if`:** struktur kontrol dasar untuk menjalankan suatu blok kode hanya jika kondisi atau ekspresi logika yang ditentukan bernilai `True`.
- **Aturan Blok Indentasi:** Python tidak menggunakan tanda kurung kurawal `{}` untuk mendefinisikan blok program, melainkan menggunakan spasi kosong (_whitespace indentation_) di awal baris. Standar penulisan blok kode setelah tanda titik dua (`:`) adalah menjorok ke dalam (biasanya 1 tombol `Tab` atau 4 spasi).

**Aliran Kontrol Logika `if`:** ketika kondisi di sebelah `if` bernilai `True`, semua pernyataan di dalam blok indentasi di bawahnya akan dieksekusi. Jika `False`, Python akan melompati seluruh isi blok indentasi tersebut dan melanjutkan eksekusi ke baris kode berikutnya yang tingkat indentasinya kembali sejajar dengan `if`.

```python
user_age = int(input("Masukkan umur anda: "))

if user_age >= 17:
    send_application_form_by_email()
    print("Check your email for the application form!")

print("Have a nice day!")
```

### 3.3 Struktur Sintaksis `if-else` untuk Dua Kondisi Eksklusif

- **Pernyataan `if-else`:** struktur kontrol untuk menangani situasi dengan dua percabangan keputusan yang saling eksklusif (jika `if` terpenuhi jalankan instruksi A, jika tidak jalankan instruksi B).
- **Mekanisme Kerja:** blok kode di bawah `else` bertindak sebagai penampung alternatif (_fallback_), hanya dieksekusi apabila kondisi pengujian utama pada `if` menghasilkan nilai balik `False`.

```python
user_age = int(input("Masukkan umur anda: "))

if user_age >= 17:
    send_application_form_by_email()
    print("Check your email for the application form!")
else:
    print("You are not eligible to sign-up!")

print("Have a nice day!")
```

### 3.4 Struktur Sintaksis `if-elif-else` untuk Multi-Kondisi

- **Pernyataan `elif`** (singkatan _else if_): digunakan untuk menguji kondisi tambahan jika kondisi-kondisi sebelumnya bernilai `False`.
- **Fleksibilitas Penulisan:** dapat menambahkan beberapa `elif` secara berurutan di antara `if` pembuka dan `else` penutup.
- **Blok `else` Akhir:** jalur penampung universal (_default fallback_) — hanya berjalan jika semua kondisi pada rangkaian `if` dan `elif` di atasnya terbukti tidak terpenuhi (`False`).

```python
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

### 3.5 Analisis Logika Aliran Eksekusi Berurutan (Serial Execution)

| Karakteristik | Struktur `if` Tunggal | Struktur `if-else` | Struktur `if-elif-else` |
| --- | --- | --- | --- |
| **Jumlah Kondisi Maksimum** | 1 Kondisi | 2 Kondisi | Tidak Terbatas (Multi-kondisi) |
| **Cabang Blok Kode yang Dieksekusi** | Maksimal 1 blok kode | Tepat 1 blok kode (Pasti salah satu) | Maksimal 1 blok kode dari rantai evaluasi |
| **Perilaku Bila Kondisi Awal `False`** | Melompati blok dan lanjut ke baris berikutnya | Mengeksekusi blok kode di dalam `else` | Mengevaluasi kondisi `elif` di bawahnya secara berurutan |

**Prinsip Kerja Serial Execution di Python:**

1. Python menguji kondisi dari atas ke bawah.
2. Begitu menemukan satu kondisi yang bernilai `True`, Python **seketika mengeksekusi** blok kode tersebut.
3. Setelah mengeksekusi blok kode yang sesuai, interpreter Python **langsung keluar** dari seluruh rangkaian blok kondisional tersebut (mengabaikan semua `elif` dan `else` yang tersisa di bawahnya), lalu melanjutkan eksekusi ke baris program setelah blok percabangan.

### 3.6 Peringatan: `IndentationError` dan Dead Code

> [!warning] Audio Insight — Identifikasi dan Dampak `IndentationError`
> Python mendeteksi struktur pengelompokan kode berdasarkan konsistensi indentasi. Jika Anda menuliskan baris instruksi di bawah _statement_ `if` tanpa memberikan spasi atau tab, Python akan menghentikan proses eksekusi dan mengeluarkan pesan kegagalan: `IndentationError: expected an indentation block`. Tingkat kerapian indentasi harus seragam di dalam satu blok yang sama — mencampur tab dengan spasi manual akan memicu galat sistem.

> [!warning] Audio Insight — Dead Code Akibat Urutan Kondisi yang Salah
> Karena interpreter Python bekerja secara sekuensial dari atas ke bawah, penentuan urutan kondisi dari yang paling spesifik ke yang paling umum sangatlah krusial. Perhatikan contoh kesalahan penulisan (_logic error_) berikut:
>
> ```python
> user_age = 15
>
> if user_age >= 10:
>     print("Kategori A")
> elif user_age >= 15:
>     print("Kategori B")
> else:
>     print("Kategori C")
> ```
>
> **Masalah:** meskipun `user_age` adalah `15` (secara teknis memenuhi kriteria `>= 15`), program di atas akan selalu menampilkan output `"Kategori A"`. **Penyebab:** kondisi pertama (`user_age >= 10`) dievaluasi terlebih dahulu dan menghasilkan `True` (karena 15 > 10). Akibatnya, blok `"Kategori A"` dieksekusi dan Python langsung keluar dari rantai `if-elif-else`. Blok `elif user_age >= 15` tidak akan pernah dievaluasi — inilah yang disebut _dead code_ (kode yang tidak pernah bisa dijalankan). **Solusi:** kondisi dengan cakupan kriteria yang lebih ketat/sempit (nilai angka lebih besar) harus diletakkan di paling atas sebelum kondisi yang berlingkup luas.

```python
# Versi yang benar - kondisi paling ketat/spesifik ditaruh paling atas
user_age = 15

if user_age >= 15:
    print("Kategori B")   # Output: Kategori B (sekarang terdeteksi dengan benar)
elif user_age >= 10:
    print("Kategori A")
else:
    print("Kategori C")
```

---

## Bab 4 — Nested if (Kondisional Bersarang)

### 4.1 Konsep dan Kasus Penggunaan Keputusan Dependen

_Nested if_ adalah struktur percabangan di mana sebuah pernyataan `if` diletakkan di dalam blok pernyataan `if` lainnya. Konsep ini digunakan untuk menangani situasi **keputusan dependen**, yaitu situasi di mana suatu kondisi kedua (_Inner Condition_) hanya perlu dievaluasi jika kondisi pertama (_Outer Condition_) telah terbukti bernilai `True`.

Apabila _Outer Condition_ dievaluasi bernilai `False`, komputer akan langsung melewati seluruh blok _Nested if_ di dalamnya tanpa melakukan pemeriksaan pada _Inner Condition_.

| Istilah Teknis | Deskripsi Fungsional |
| --- | --- |
| **Outer Condition** | Kondisi tingkat pertama yang dievaluasi paling awal untuk menentukan apakah blok di dalamnya dapat diakses. |
| **Inner Condition** | Kondisi bersarang di dalam _Outer Condition_ yang hanya dievaluasi jika kondisi tingkat pertama bernilai `True`. |
| **Double Indentation** | Aturan penulisan spasi vertikal ganda untuk menegaskan cakupan (_scope_) dari _Inner Condition_. |
| **NameError** | Eror yang terjadi jika program memanggil fungsi atau variabel dalam kondisi yang belum didefinisikan sebelumnya. |

### 4.2 Aturan Double Indentation dan Contoh Implementasi

**Aturan Double Indentation (Indentasi Ganda):**

- Blok kode tingkat pertama (_Outer_) memerlukan indentasi standar sebesar **4 spasi** (atau 1 tab).
- Blok kode bersarang tingkat kedua (_Inner_) memerlukan **indentasi ganda** sebesar **8 spasi** (atau 2 tab) dari tepi kiri baris perintah utama.

**Studi Kasus: Validasi Nomor Induk Kependudukan (NIK)** — program mengevaluasi kelayakan pendaftaran berdasarkan umur pengguna. Jika umur memenuhi syarat kelayakan minimum (17 tahun ke atas), program akan meminta input NIK dan melakukan validasi ganda menggunakan fungsi pembantu `validate_NIK()`.

Kriteria validitas NIK: (1) panjang string NIK harus tepat **16 karakter** (`len(nik) == 16`); (2) seluruh karakter penyusun NIK harus berupa **angka/digit** (`nik.isdigit()`).

```python
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

> [!warning] Audio Insight — Fungsi Harus Didefinisikan Sebelum Dipanggil (`NameError`)
> Dalam pemaparan teori di modul, fungsi seperti `validate_NIK()` dan `send_application_form_by_email()` sering kali diasumsikan sudah terdefinisi secara abstrak untuk menyederhanakan alur logika. Namun, pada praktiknya di Python, fungsi-fungsi tersebut harus didefinisikan secara eksplisit terlebih dahulu di bagian atas kode sebelum dipanggil. Jika langsung dipanggil tanpa definisi, interpreter Python akan menghentikan program dan memicu error `NameError: name 'validate_NIK' is not defined`.

> [!tip] Audio Insight — Penyederhanaan Evaluasi Boolean: `if is_nik_valid:` vs `if is_nik_valid == True:`
> Pada penulisan kondisi bersarang `if is_nik_valid:`, penulisan tersebut secara fungsional identik dengan `if is_nik_valid == True:`. Namun, penggunaan `if is_nik_valid:` sangat direkomendasikan karena lebih bersih (_pythonic_) dan efisien, karena variabel `is_nik_valid` sudah menyimpan nilai tipe data Boolean (`True`/`False`) hasil dari nilai pengembalian (_return value_) fungsi `validate_NIK()`.

> [!tip] Audio Insight — Kombinasi `len()` dan `.isdigit()` dengan Operator `and`
> Proses validasi NIK menggabungkan fungsi bawaan Python `len()` untuk mendapatkan panjang string dan metode objek string `.isdigit()` untuk memastikan tidak ada karakter huruf atau simbol di dalam NIK. Kedua kondisi ini digabungkan secara ketat dengan operator logika `and`, yang mewajibkan kedua evaluasi bernilai `True` agar hasil akhir validasi bernilai `True`.

> [!tip] Audio Insight — Nested if Menghemat Sumber Daya Eksekusi
> Melalui teknik _Nested if_, komputer menghemat sumber daya komputasi dengan tidak menjalankan perintah input NIK atau memanggil fungsi validasi jika usia pengguna di bawah 17 tahun. Blok kode bagian dalam (_inner_) benar-benar terisolasi dan dilindungi oleh _Outer Condition_.

---

## Bab 5 — Looping and Iteration (Perulangan)

### 5.1 Konsep Dasar Perulangan dan Stopping Condition

- **Looping / Iteration:** proses eksekusi sekumpulan instruksi secara berulang-ulang hingga suatu kondisi berhenti yang ditentukan terpenuhi. Digunakan sebagai mekanisme otomatisasi untuk menangani tugas repetitif secara efisien tanpa menulis ulang instruksi yang sama berkali-kali.
- **Stopping Condition:** syarat batas evaluasi yang wajib dipenuhi agar aliran eksekusi program dapat keluar dari siklus perulangan. Jika tidak didefinisikan dengan benar atau tidak pernah tercapai, sistem akan terjebak dalam **Infinite Loop** (perulangan tanpa akhir) yang terus-menerus mengonsumsi memori dan daya komputasi perangkat secara berlebihan hingga program dihentikan secara paksa.

### 5.2 Perbandingan Efisiensi Penulisan Kode

| Kriteria Perbandingan | Tanpa Perulangan | Menggunakan Perulangan |
| --- | --- | --- |
| **Volume Penulisan Kode** | Tinggi (instruksi berulang harus disalin secara manual sebanyak jumlah eksekusi) | Rendah (hanya memerlukan deklarasi struktur perulangan sekali) |
| **Tingkat Keterbacaan** | Buruk dan redundan, menyulitkan proses penelusuran kesalahan | Bersih, ringkas, dan profesional |
| **Kemudahan Pemeliharaan** | Rendah (perubahan satu logika mengharuskan pengeditan di setiap baris duplikat) | Tinggi (perubahan logika cukup dilakukan pada satu blok perulangan) |
| **Fleksibilitas Jumlah Repetisi** | Kaku (jumlah eksekusi sudah terkunci secara statis sejak kode ditulis) | Dinamis (jumlah repetisi dapat berubah mengikuti variabel atau input sistem) |

**Studi Kasus: Mengaduk Sup**

```python
# Tanpa Perulangan
stir_the_soup()
stir_the_soup()
stir_the_soup()
stir_the_soup()
stir_the_soup()

# Menggunakan Perulangan
while not soup_cooked:
    stir_the_soup()
```

### 5.3 Cabang Sintaksis Perulangan Utama di Python

1. **for Loop** — bekerja dengan cara mengiterasi atau menelusuri setiap elemen di dalam objek yang bersifat _Iterable_ (String, List, Tuple, Dictionary, Set, atau objek Range). Umumnya digunakan ketika jumlah putaran perulangan sudah dapat diketahui atau didefinisikan secara pasti sejak awal.
2. **while Loop** — beroperasi berdasarkan evaluasi berkala terhadap suatu kondisi Boolean. Blok instruksi terus dijalankan berulang selama kondisi pengujian menghasilkan nilai `True`. Ketika kondisi berubah `False`, siklus perulangan langsung berhenti.

> [!tip] Audio Insight — Pembeda Fundamental Looping vs Recursion
> Dalam interaksi kelas, dibahas pertanyaan kritis mengenai korelasi perulangan dengan konsep pemrograman rekursif. Dosen menegaskan bahwa meskipun keduanya menghasilkan eksekusi berulang, prinsip kerjanya di dalam memori sangat berbeda:
> - _Recursion_ adalah sebuah fungsi yang memanggil dirinya sendiri dari dalam badan fungsinya sendiri, sehingga membutuhkan alokasi tumpukan memori (_stack_) baru untuk setiap pemanggilan fungsi berantai tersebut hingga batas berhenti (_base case_) dicapai.
> - Sebaliknya, _Looping_ bekerja secara linier di dalam satu cakupan eksekusi yang sama. Program mengevaluasi kondisi secara langsung untuk mengulang instruksi yang didefinisikan (misalnya menjalankan fungsi luar secara berulang seperti `stir_the_soup()`), sehingga jauh lebih hemat dalam penggunaan sumber daya memori komputer.

> [!info] Lihat juga
> Konsep _Recursion_ dan _Base Case_ ini dijelaskan mendalam lewat studi kasus Tower of Hanoi di [[Sesi 01 - Introduction to DS Python Statistics SQL Git and GitHub]] Bab 3, termasuk implementasi Python-nya.

---

## Bab 6 — Perulangan dengan Sintaksis `for`

### 6.1 Fungsi `range()` dan Konfigurasi Parameternya

Fungsi `range()` adalah fungsi bawaan Python yang digunakan untuk menghasilkan urutan (_sequence_) angka numerik secara berurutan. Secara default, urutan ini selalu dimulai dari angka `0` dengan kelipatan penambahan (_increment_) sebesar `1`. Aliran angka yang dihasilkan akan selalu berhenti tepat **satu angka sebelum** angka batas akhir (_stop value_) yang ditentukan.

Fungsi `range()` menerima tiga parameter konfigurasi: `range(start, stop, step)`.

| Parameter | Sifat | Deskripsi | Nilai Default |
| --- | --- | --- | --- |
| **`start`** | Opsional | Menentukan angka awal dimulainya urutan. | `0` |
| **`stop`** | Wajib | Menentukan batas akhir urutan. Angka pada posisi ini bersifat eksklusif (tidak dimasukkan ke dalam hasil). | Tidak ada |
| **`step`** | Opsional | Menentukan besarnya nilai lompatan atau kelipatan penambahan (_increment_). | `1` |

**Skenario 1: Satu Parameter `range(stop)`**

```python
# Menghasilkan angka dari 0 sampai sebelum 10 dengan langkah 1
for number in range(10):
    print(number, end=" ")
# Output: 0 1 2 3 4 5 6 7 8 9
```

**Skenario 2: Dua Parameter `range(start, stop)`**

```python
# Menghasilkan angka dari 1 sampai sebelum 10 dengan langkah 1
for number in range(1, 10):
    print(number, end=" ")
# Output: 1 2 3 4 5 6 7 8 9
```

**Skenario 3: Tiga Parameter `range(start, stop, step)`**

```python
# Menghasilkan angka dari 1 sampai sebelum 10 dengan lompatan 2
for number in range(1, 10, 2):
    print(number, end=" ")
# Output: 1 3 5 7 9
```

**Menelusuri `range(1, 10, 2)` elemen demi elemen** — bukan cuma "1 dan 10" sebagai dua titik ujung, tapi berjalan lewat SETIAP lompatan `step=2` di antara keduanya sampai sebelum 10:

| Iterasi ke- | Nilai `number` | Apakah `< 10`? | Dicetak? |
| --- | --- | --- | --- |
| 1 | 1 | Ya | Ya |
| 2 | 3 | Ya | Ya |
| 3 | 5 | Ya | Ya |
| 4 | 7 | Ya | Ya |
| 5 | 9 | Ya | Ya |
| 6 | 11 | Tidak (11 >= 10) | Berhenti, loop selesai |

> [!warning] Audio Insight — Sifat Eksklusif Parameter `stop`
> Sangat penting untuk mengingat bahwa nilai pada parameter `stop` **tidak akan pernah diikutsertakan** dalam hasil akhir. Sebagai contoh, `range(10)` atau `range(1, 10)` hanya akan menghasilkan angka maksimal sampai `9`.

> [!tip] Audio Insight — Aturan Default Parameter Fungsi
> Di dalam Python, jika sebuah parameter fungsi dideklarasikan menggunakan tanda sama dengan (seperti `start=0`), parameter tersebut bersifat opsional karena sudah memiliki nilai default. Sebaliknya, parameter `stop` tidak memiliki nilai default sehingga wajib didefinisikan secara eksplisit oleh programmer ketika memanggil fungsi `range()`.

### 6.2 Karakteristik Iterable Data Types

Objek _Iterable_ adalah tipe data atau objek apa pun dalam Python yang elemen-elemen penyusunnya dapat diakses, dijelajahi, atau dilalui satu per satu secara berurutan (_traversed_). Objek ini berfungsi sebagai wadah penampung nilai yang nantinya akan dikonsumsi oleh struktur perulangan seperti `for loop`.

| Tipe Data | Contoh Deklarasi | Deskripsi Karakteristik Iterasi |
| --- | --- | --- |
| **String** | `"Python"` | Mengiterasi setiap karakter huruf penyusun string secara berurutan (`'P'`, `'y'`, `'t'`, `'h'`, `'o'`, `'n'`). |
| **List** | `["Apple", "Banana", "Orange"]` | Mengiterasi setiap elemen objek di dalam kurung siku secara berurutan. |
| **Tuple** | `(10, 20, 30)` | Mengiterasi objek berurutan yang bersifat tidak dapat diubah (_immutable_). |
| **Dictionary** | `{"name": "John", "age": 20}` | Mengiterasi pasangan kunci (_keys_) dan nilai (_values_). Secara default hanya mengembalikan kunci. |
| **Set** | `{1, 2, 3}` | Mengiterasi sekumpulan nilai unik yang tidak terurut secara berurutan. |
| **Range** | `range(5)` | Mengiterasi urutan numerik dinamis yang dihasilkan dari fungsi pembatas. |

> [!info] Lihat juga
> Kategori tipe data _Sequences_, _Mappings_, dan _Sets_ ini (termasuk `range` sebagai _sequence_ yang _immutable_) dirangkum secara sistematis dalam satu tabel besar `mutable`/`immutable` di [[Sesi 04 - Data Types Collection Notes]] Bab 2.

### 6.3 Sintaksis Dasar `for` loop

Sintaksis `for loop` di Python dirancang khusus untuk melakukan iterasi langsung pada elemen-elemen dari objek _iterable_ tanpa memerlukan evaluasi kondisi Boolean eksplisit seperti pada perulangan `while`. Jumlah pengulangan ditentukan secara otomatis berdasarkan jumlah elemen yang tersedia di dalam objek wadah tersebut.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
```

Pada iterasi pertama, `fruit` menyimpan `"apple"`, iterasi kedua `"banana"`, iterasi ketiga `"cherry"`. Perulangan otomatis berakhir ketika sistem mendeteksi tidak ada lagi elemen yang tersisa di dalam list `fruits`.

> [!tip] Audio Insight — Persistensi Variabel Perulangan Setelah Loop Selesai
> Variabel penampung sementara yang digunakan di baris deklarasi `for loop` (misalnya variabel `number` pada `for number in range(10)`) **tidak akan dihapus** dari memori komputer setelah perulangan selesai berjalan. Variabel tersebut tetap menyimpan nilai terakhir yang diproses dalam iterasi (dalam contoh ini, nilai terakhir yang tersimpan adalah `9`).

```python
for number in range(10):
    pass

print(number)  # Output: 9 -> variabel 'number' masih hidup dan menyimpan nilai terakhir
```

> [!tip] Audio Insight — Fleksibilitas Penamaan Variabel Loop
> Nama variabel penampung setelah kata kunci `for` bebas dinamai apa saja oleh programmer (misalnya `for x in range(5)` atau `for buah in fruits`). Aturan utamanya adalah nama variabel tersebut harus dipanggil dengan ejaan yang persis sama di dalam blok kode pengolahan data di bawahnya.

### 6.4 Fungsi `enumerate()` untuk Pelacakan Pasangan Indeks dan Nilai

Fungsi `enumerate()` adalah fungsi penolong bawaan Python yang digunakan untuk mengiterasi suatu objek _iterable_ sekaligus melacak posisi indeks dari masing-masing elemen yang sedang diproses. Fungsi ini menghilangkan kebutuhan programmer untuk membuat dan menambahkan nilai variabel pencatat indeks (_counter_) secara manual di dalam blok perulangan.

`enumerate()` bekerja dengan mengemas indeks dan elemen terkait ke dalam format pasangan data _tuple_ dengan pola: `(index, element)`.

```python
kata = "hai"
for indeks, huruf in enumerate(kata):
    print(f"Huruf ke-{indeks} dari '{kata}' adalah {huruf}")
# Output:
# Huruf ke-0 dari 'hai' adalah h
# Huruf ke-1 dari 'hai' adalah a
# Huruf ke-2 dari 'hai' adalah i
```

**Parameter `start` pada `enumerate()`** — secara default penomoran indeks dimulai dari `0`, namun bisa diatur dengan parameter `start`:

```python
fruits = ["apple", "banana", "cherry"]
# Mengatur penghitungan indeks dimulai dari angka 1
for indeks, buah in enumerate(fruits, start=1):
    print(f"Peringkat {indeks}: {buah}")
# Output:
# Peringkat 1: apple
# Peringkat 2: banana
# Peringkat 3: cherry
```

> [!warning] Audio Insight — `start` pada `enumerate()` Tidak Melakukan Skipping Data
> Menentukan nilai `start=1` (atau angka lainnya) pada `enumerate()` hanya mengubah representasi angka pencatat indeks yang ditampilkan ke terminal, tetapi **tidak melakukan operasi pemotongan (_skipping_)** pada data. Elemen pertama (indeks ke-0 pada list asli) akan tetap diproses penuh sebagai elemen pertama dalam iterasi, namun nomor pencatatnya saja yang digeser menjadi angka 1.

> [!tip] Audio Insight — `enumerate()` Lebih Pythonic Dibanding `range(len(...))`
> Melakukan pelacakan indeks menggunakan `enumerate()` dinilai jauh lebih bersih, aman, dan efisien (_pythonic_) dibandingkan metode konvensional yang mengombinasikan fungsi `range()` dan fungsi panjang data `len()` secara manual:
>
> ```python
> # Metode Manual (Kurang Efisien)
> for i in range(len(fruits)):
>     print(f"Indeks {i}: {fruits[i]}")
> ```

### 6.5 Iterasi Spesifik pada Tipe Data Dictionary

Tipe data Dictionary menyimpan data dalam format pasangan kunci dan nilai (_key-value pairs_). Ketika kita melakukan perulangan `for` langsung pada objek dictionary, Python secara default hanya akan mengembalikan elemen kuncinya (_keys_) saja. Untuk melakukan iterasi secara spesifik pada bagian tertentu dari dictionary, Python menyediakan tiga metode bawaan.

| Metode | Deskripsi Fungsional | Contoh Implementasi |
| --- | --- | --- |
| **Default (Tanpa Metode)** | Hanya mengiterasi bagian kunci (_keys_) saja. | `for key in person:` |
| **`.keys()`** | Menegaskan iterasi khusus pada kumpulan kunci saja. | `for key in person.keys():` |
| **`.values()`** | Mengiterasi khusus pada kumpulan nilai (_values_) saja. | `for val in person.values():` |
| **`.items()`** | Mengiterasi pasangan kunci dan nilai sekaligus secara bersamaan. | `for key, val in person.items():` |

```python
person = {"name": "John", "age": 20, "weight": 73}

for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 20
# weight: 73
```

> [!tip] Audio Insight — Format Penulisan Dictionary
> Penulisan dictionary dideklarasikan menggunakan kurung kurawal `{}`. Karakter yang ditulis sebelum tanda titik dua (`:`) bertindak sebagai Kunci (_Key_), sedangkan karakter setelah titik dua bertindak sebagai Nilai (_Value_).

> [!warning] Audio Insight — Urutan Penangkapan Variabel pada `.items()`
> Saat menggunakan metode `.items()`, kita wajib menyediakan dua variabel penampung pada baris deklarasi `for` (misalnya `for key, value in person.items()`). Python akan selalu mengirimkan data kunci ke variabel pertama dan data nilai ke variabel kedua secara berurutan. Jangan membalik urutan variabel jika ingin menjaga kejelasan logika kode.

> [!info] Lihat juga
> Tipe data Dictionary dan metode `.keys()`/`.values()`/`.items()` ini dibahas lebih dalam (termasuk `.get()`, `.update()`, `.setdefault()`) di [[Sesi 04 - Data Types Collection Notes]] Bab 7.

### 6.6 Implementasi Pernyataan `pass` sebagai Placeholder

Pernyataan `pass` adalah pernyataan kosong (_null statement_) di Python yang tidak melakukan operasi atau tindakan apa pun saat dieksekusi oleh komputer. Di Python, blok struktur kontrol seperti `if` atau `for loop` tidak diperbolehkan memiliki blok instruksi yang kosong secara sintaksis — jika terjadi, Python Interpreter akan menghentikan program dan memicu kesalahan eror sintaks.

`pass` digunakan sebagai penampung sementara (_placeholder_) untuk menjaga struktur sintaksis program tetap valid ketika programmer sedang merancang kerangka perulangan namun belum menuliskan logika pemrosesan data di dalamnya.

```python
# Kerangka perulangan yang belum selesai ditulis logikanya
for number in range(100):
    pass  # Menjaga agar kode tidak mengalami eror saat dijalankan
```

> [!warning] Audio Insight — Tanpa `pass`, Blok Kosong Memicu `IndentationError`/`SyntaxError`
> Tanpa adanya instruksi `pass` di dalam badan perulangan kosong, program Python akan langsung memicu kesalahan fatal berupa `IndentationError` atau `SyntaxError`.

> [!warning] Audio Insight — Perbedaan `pass` vs `continue`
> Pernyataan `pass` sama sekali tidak memengaruhi alur perulangan — komputer tetap menjalankan semua tahapan iterasi secara normal tanpa melakukan aksi apa pun. Sementara pernyataan `continue` akan melompati sisa instruksi yang ada di bawahnya dalam iterasi saat ini dan langsung berpindah ke langkah iterasi berikutnya. (Lihat `continue` di Bab 7.3 di bawah.)

---

## Bab 7 — Perulangan dengan Sintaksis `while`

### 7.1 Aliran Kontrol Perulangan Berbasis Evaluasi Kondisi Boolean

- **Definisi:** _while loop_ di Python adalah salah satu dari dua cabang sintaksis perulangan utama yang mengandalkan evaluasi kondisi logika untuk mengontrol perulangan. Program akan mengeksekusi blok kode di dalamnya secara berulang-ulang selama kondisi yang didefinisikan tersebut terus bernilai `True`.
- **Mekanisme Aliran Kontrol:** komputer melakukan pemeriksaan kondisi terlebih dahulu sebelum mengeksekusi blok perulangan. (1) Jika kondisi `True`, blok instruksi dijalankan. (2) Setelah satu putaran eksekusi selesai, kondisi diperiksa kembali di bagian atas. (3) Jika kondisi berubah `False`, perulangan langsung terhenti, dilanjutkan ke baris instruksi setelah blok perulangan.

| Istilah Teknis | Deskripsi Fungsional |
| --- | --- |
| _Initial Condition_ | Nilai awal variabel kontrol sebelum masuk ke dalam perulangan. |
| _Condition Evaluation_ | Proses di mana komputer mengevaluasi ekspresi logika untuk memeriksa status _True_ atau _False_. |
| _Stopping Condition_ | Keadaan atau nilai tertentu di mana kondisi _while_ menjadi _False_, yang memaksa perulangan untuk berhenti secara normal. |
| _Loop Increment / Decrement_ | Pembaruan nilai variabel kontrol di dalam perulangan untuk mencegah terjadinya perulangan tanpa akhir (_Infinite Loop_). |

**Deret hitung bertambah (increment):**

```python
count = 1
while count <= 3:
    print(count)
    count += 1
# Output:
# 1
# 2
# 3
```

**Deret hitung berkurang (decrement) — skenario pembelian cokelat:**

```python
money = 10
while money > 0:
    print("Buying $1 Chocolate...")
    money = money - 1
```

> [!tip] Audio Insight — `while` Digunakan Saat Jumlah Perulangan Tidak Pasti
> Berbeda dengan _for loop_ yang iterasi elemennya sudah pasti berdasarkan panjang objek iterable, _while loop_ digunakan ketika jumlah perulangan tidak diketahui secara pasti di awal dan sepenuhnya bergantung pada perubahan kondisi logika yang dinamis selama runtime.

> [!tip] Audio Insight — Perilaku Memori Variabel Kontrol
> Setiap kali variabel kontrol (seperti `count` atau `money`) diperbarui di dalam blok perulangan, nilai barunya akan langsung diperbarui di dalam memori. Proses evaluasi logika pada baris _while_ selalu menggunakan nilai terbaru dari variabel kontrol tersebut pada iterasi berikutnya.

### 7.2 Identifikasi Bahaya dan Dampak Infinite Loop

- **Definisi Infinite Loop:** situasi di mana perulangan berjalan secara terus-menerus tanpa pernah berhenti karena kondisi evaluasi logika _while_ selalu bernilai `True`.
- **Penyebab Utama:** programmer lupa menuliskan instruksi pembaruan nilai variabel kontrol (increment/decrement) atau kondisi berhenti (_stopping condition_) yang dikonfigurasi tidak akan pernah bisa tercapai.

| Karakteristik | Deskripsi Dampak |
| --- | --- |
| **Konsumsi CPU** | Menggunakan sumber daya pemrosesan CPU perangkat secara penuh, dapat menyebabkan sistem hang atau melambat. |
| **Penggunaan Memori** | Dapat menyebabkan kebocoran memori jika ada alokasi data baru secara terus-menerus di dalam perulangan. |
| **Pencegahan** | Selalu pastikan adanya pembaruan nilai variabel kontrol (increment/decrement) di dalam blok perulangan sebelum menjalankan program. |

```python
# PERINGATAN: Kode ini memicu Infinite Loop jika dijalankan (JANGAN dijalankan sungguhan)
money = 10
while money > 0:
    print("Buying $1 Chocolate...")
    # Nilai money tidak pernah dikurangi, sehingga kondisi money > 0 selalu True
```

> [!warning] Audio Insight — Cara Menghentikan Paksa Infinite Loop di VS Code
> Jika programmer tidak sengaja menjalankan _Infinite Loop_ di terminal, eksekusi program dapat dihentikan secara paksa dengan menekan tombol kombinasi `Ctrl + C` di dalam terminal Python.

> [!tip] Audio Insight — Menggunakan `time.sleep()` untuk Mengamati Infinite Loop
> Dalam sesi latihan pengujian _Infinite Loop_, fungsi `time.sleep(0.3)` dari pustaka `time` Python dapat dimanfaatkan untuk memberi jeda komputasi sebesar 0.3 detik per iterasi. Hal ini bertujuan agar eksekusi perulangan berjalan cukup lambat sehingga proses _infinite loop_ dapat diamati secara visual pada layar terminal tanpa langsung membebani CPU komputer secara ekstrem.

```python
import time

count = 1
while count <= 5:
    print(f"Iterasi ke-{count}")
    time.sleep(0.3)  # jeda 0.3 detik per iterasi agar bisa diamati
    count += 1
```

### 7.3 Pernyataan Aliran Perulangan: `break` dan `continue`

Python menyediakan kata kunci kontrol aliran khusus untuk memodifikasi jalannya eksekusi perulangan dari dalam blok kode:

- **Pernyataan `break`:** menghentikan perulangan secara paksa pada saat itu juga, tanpa memedulikan apakah kondisi _while_ masih bernilai `True` atau tidak. Setelah `break` dipicu, komputer langsung melompat keluar dari perulangan.
- **Pernyataan `continue`:** melompati sisa instruksi di bawahnya pada iterasi yang sedang berjalan, lalu memaksa program untuk segera melompat ke bagian awal perulangan untuk melakukan evaluasi kondisi atau iterasi berikutnya.

| Karakteristik | Pernyataan `break` | Pernyataan `continue` |
| --- | --- | --- |
| **Dampak Terhadap Perulangan** | Menghentikan dan keluar dari seluruh perulangan seketika | Hanya melompati iterasi berjalan dan melanjutkan ke iterasi berikutnya |
| **Titik Keluar (_Exit Point_)** | Langsung menuju baris kode pertama di luar blok perulangan | Kembali ke baris evaluasi kondisi _while_ di bagian atas |
| **Tujuan Umum** | Menangani kondisi darurat atau batas maksimum (seperti stok habis) | Melompati eksekusi instruksi tertentu untuk kasus-kasus spesifik |

**Implementasi dengan `break`** — perulangan terhenti paksa saat stok cokelat habis (`chocolate_stock == 0`), meskipun pembeli masih memiliki uang (`money > 0`):

```python
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

**Implementasi dengan `continue`** — pada hari ke-7 cokelat dibagikan gratis. Eksekusi pemotongan uang pembeli diloncati, namun perulangan tetap berlanjut ke hari berikutnya:

```python
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

> [!warning] Audio Insight — Bahaya Infinite Loop dengan `continue`
> Ketika menggunakan pernyataan `continue`, urutan penulisan kode pembaruan variabel kontrol harus diletakkan dengan cermat. Pada contoh kasus "hari gratis" di atas, instruksi `day = day + 1` diletakkan tepat **sebelum** kata kunci `continue` agar nilai hari tetap bertambah. Jika pembaruan nilai variabel kontrol hanya diletakkan di akhir blok _while_ (di bawah pernyataan `continue`), program akan terjebak dalam _Infinite Loop_ karena variabel hari akan bernilai 7 selamanya tanpa pernah diperbarui.

```python
# CONTOH SALAH -> Infinite Loop! day+1 diletakkan SETELAH continue, tidak pernah tercapai
money = 10
day = 1

while money > 0:
    print("Buying $1 Chocolate...")
    if day == 7:
        print("Free chocolate today!")
        continue          # loop langsung kembali ke atas, baris di bawah ini tak pernah jalan
    money = money - 1
    day = day + 1          # <- baris ini tidak pernah tercapai saat day == 7, day macet di 7 selamanya
```

### 7.4 Sintaksis `else` dalam Loop

- **Definisi:** di Python, blok pernyataan `else` dapat dikaitkan dengan perulangan `while` atau `for`. Blok `else` ini memiliki karakteristik unik di mana instruksi di dalamnya **hanya akan dijalankan apabila perulangan berakhir secara normal** (kondisi perulangan bernilai `False`).
- **Kondisi Eksklusi:** jika perulangan dihentikan di tengah jalan secara paksa menggunakan `break`, maka blok `else` di bawah perulangan tersebut **tidak akan pernah dieksekusi**.

| Status Akhir Perulangan | Apakah Blok `else` Dieksekusi? | Alasan Aliran Sistem |
| --- | --- | --- |
| Perulangan selesai secara normal (_while_ menjadi _False_) | **Ya** | Sistem mendeteksi perulangan selesai tanpa adanya interupsi eksternal. |
| Perulangan berhenti akibat pernyataan _break_ | **Tidak** | Sistem mendeteksi adanya interupsi paksa yang melompati bagian penutup perulangan. |

**Studi Kasus Validasi Password / Login Attempt** — sistem percobaan autentikasi maksimal 3 kali. Jika pengguna berhasil login sebelum percobaan habis, program memicu `break` sehingga blok `else` diabaikan. Jika percobaan habis tanpa jawaban benar, perulangan selesai normal dan blok `else` dijalankan:

```python
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

> [!tip] Audio Insight — `else` pada Loop Menyederhanakan Kebutuhan Flag Manual
> Fitur _else in loop_ sangat berguna untuk menyederhanakan kode yang membutuhkan penanda status (_flag_). Tanpa menggunakan blok `else` ini, programmer harus membuat variabel penanda tambahan (seperti `is_locked = True`) dan melakukan pengecekan kondisi logika bersyarat di luar blok perulangan secara manual, yang membuat kode menjadi lebih panjang dan kurang efisien.

---

## Bab 8 — Studi Komparasi & Pembahasan Soal Latihan Akhir Sesi

### 8.1 Tabel Komparasi Karakteristik Utama Antara `for` Loop vs `while` Loop

| Fitur | _for Loop_ | _while Loop_ |
| --- | --- | --- |
| **Kondisi Penggunaan Terbaik** | Jumlah iterasi sudah diketahui secara pasti sebelum perulangan dimulai. | Jumlah iterasi tidak diketahui secara pasti dan bergantung pada pemenuhan suatu kondisi tertentu. |
| **Mekanisme Berhenti** | Berhenti otomatis setelah seluruh elemen dalam objek _iterable_ selesai diproses atau rentang _range_ berakhir. | Berhenti ketika evaluasi kondisi logika (_loop condition_) berubah bernilai `False`. |
| **Kasus Penggunaan Umum** | Mengiterasi elemen pada tipe data koleksi (list, string, dictionary, tuple, set) atau hasil fungsi `range()`. | Menunggu suatu aksi/kondisi, siklus permainan (_game loops_), membaca _user input_, logika mencoba kembali (_retry logic_). |
| **Dukungan `break`** | Ya. | Ya. |
| **Dukungan `continue`** | Ya. | Ya. |
| **Dukungan `else`** | Ya, dieksekusi jika perulangan selesai normal tanpa interupsi `break`. | Ya, dieksekusi jika perulangan selesai normal (kondisi menjadi `False`) tanpa interupsi `break`. |

### 8.2 Analisis Algoritma dan Pembahasan Solusi Soal Latihan Akhir

**A. Soal 1: Pengecekan Kategori Angka (Ganjil, Genap, atau Nol)**

```python
def check_number_type(number):
    if number == 0:
        print("zero")
    elif number % 2 == 0:
        print("even")
    else:
        print("odd")

check_number_type(10)  # Output: even
check_number_type(1)   # Output: odd
check_number_type(0)   # Output: zero
```

> [!warning] Audio Insight — Nol Harus Dicek Pertama Sebelum Modulo
> Pemeriksaan kondisi `number == 0` harus diletakkan pada percabangan pertama (`if`). Jika tidak, angka `0` akan lolos ke pemeriksaan modulo `0 % 2 == 0` dan teridentifikasi secara salah sebagai bilangan genap (_even_), karena secara aritmetika sisa hasil bagi 0 dengan 2 adalah 0.

> [!tip] Audio Insight — Hapus `pass` Setelah Logika Selesai Ditulis
> Pada saat menggunakan kerangka kode (_skeleton code_), kata kunci `pass` diletakkan sebagai penampung sementara agar program tidak eror saat dibaca oleh Python interpreter. Setelah fungsi atau logika selesai didefinisikan secara konkret, kata kunci `pass` harus dihapus karena tidak lagi diperlukan.

**B. Soal 2: Perhitungan Rata-Rata Angka Dinamis (Hingga Input Berhenti pada Angka 0)**

Program terus-menerus meminta input bilangan bulat sampai pengguna memasukkan `0`. Setelah `0` dimasukkan, program menghitung dan menampilkan rata-rata dari seluruh bilangan bulat yang dimasukkan sebelumnya (`0` sebagai penanda berhenti tidak ikut dihitung).

```python
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

> [!warning] Audio Insight — Penanganan ZeroDivisionError
> Jika pengguna langsung memasukkan angka `0` pada kesempatan pertama tanpa memasukkan angka lain terlebih dahulu, variabel `count` akan bernilai `0`. Pembagian `total / count` (yaitu `0 / 0`) akan memicu kegagalan sistem berupa `ZeroDivisionError`. Oleh karena itu, diperlukan validasi tambahan `if total == 0` atau `if count == 0` untuk langsung mencetak hasil `0` tanpa melakukan komputasi pembagian.

> [!tip] Audio Insight — Aturan Desain Fungsi: Hindari `return print(...)`
> Dalam perancangan fungsi Python yang baik, hindari penulisan `return print(...)`. Pernyataan `return` digunakan untuk mengirimkan kembali nilai murni hasil komputasi kepada pemanggil fungsi agar nilai tersebut dapat diolah kembali. Jika hanya ingin menampilkan teks hasil ke layar terminal tanpa mengembalikan nilai apa pun, gunakan instruksi `print()` secara langsung tanpa menyertakan `return`.

> [!tip] Audio Insight — Peletakan `break` yang Tepat
> Pastikan pernyataan `break` diletakkan dengan indentasi yang tepat setelah proses pelaporan rata-rata selesai dilakukan pada saat input `0` terdeteksi. Hal ini bertujuan agar perulangan `while True` langsung dihentikan secara permanen dalam satu kali proses eksekusi.

**C. Soal 3: Pencarian Nilai Terbesar dari 3 Input Bilangan Bulat (Tanpa `max()`)**

```python
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

> [!tip] Audio Insight — Definisi Nilai Terbesar dan Operator `and`
> Sebuah bilangan bulat didefinisikan sebagai bilangan terbesar dari kelompok tiga angka apabila bilangan tersebut secara bersamaan memiliki nilai yang lebih besar dibandingkan bilangan kedua DAN bilangan ketiga. Logika ini diimplementasikan menggunakan operator logika `and` untuk menggabungkan dua kondisi perbandingan terpisah (`num1 > num2 and num1 > num3`). Kedua perbandingan tersebut wajib bernilai `True` agar variabel penampung `largest` dapat diisi dengan angka bersangkutan. Cabang `else` paling akhir tidak memerlukan kondisi logika eksplisit tambahan — jika angka pertama bukan yang terbesar dan angka kedua juga bukan yang terbesar, maka secara otomatis angka ketiga merupakan nilai terbesar yang tersisa.

**D. Soal 4: Perhitungan Jumlah Bilangan Prima dalam Batas Rentang Tertentu**

Program meminta input batas bawah (_lower bound_) dan batas atas (_upper bound_), lalu menghitung total jumlah (penjumlahan) dari seluruh bilangan prima yang berada di dalam rentang tersebut (inklusif). Jika batas bawah lebih besar dari batas atas atau batas bawah negatif, program menampilkan `"range not valid"`.

```python
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

> [!tip] Audio Insight — Validasi Awal Rentang Data
> Logika kondisional diletakkan di bagian teratas untuk menyaring input abnormal. Skenario seperti `lower > upper` (misal batas bawah 10 dan batas atas 0) atau input bernilai negatif harus langsung menghentikan aliran komputasi utama dan mencetak `"range not valid"`.

> [!tip] Audio Insight — Karakteristik Bilangan Prima
> Bilangan prima adalah bilangan bulat positif yang hanya memiliki dua pembagi positif, yaitu angka 1 dan dirinya sendiri. Bilangan prima terkecil dimulai dari angka 2, sehingga kondisi pemeriksaan `num > 1` wajib disertakan sebelum menguji pembagi potensial lainnya.

> [!warning] Audio Insight — Rentang Inklusif Membutuhkan `upper + 1`
> Saat melakukan iterasi pada perulangan `for` menggunakan fungsi `range()`, batas atas harus ditambahkan dengan angka 1 (`upper + 1`). Hal ini disebabkan karena parameter `stop` pada fungsi `range()` bersifat eksklusif (tidak diikutsertakan dalam iterasi).

> [!info] Lihat juga
> Algoritma pencarian bilangan prima ini dibahas ulang dan ditelusuri lebih detail (termasuk kasus khusus angka 2) di [[Sesi 04 - Data Types Collection Notes]] Bab 1.

---

## Ringkasan Sesi

Sesi 3 membangun kemampuan mengambil keputusan (Boolean, operator perbandingan & logika, `if`/`if-else`/`if-elif-else`/_nested if_) dan melakukan perulangan (`for`, `while`, `range()`, `enumerate()`, `break`, `continue`, `else` pada loop). Studi kasus konversi suhu/jarak, ganjil-genap, penghapusan karakter, dan palindrome yang dibuka di Bab 1 juga muncul di [[Sesi 02 - Intro to Git and GitHub]] sebagai Tugas Besar 2. Materi bilangan prima di Bab 8 menjadi jembatan langsung ke pembahasan tipe data koleksi di [[Sesi 04 - Data Types Collection Notes]], yang membuka bab dengan me-review ulang soal bilangan prima yang sama.
