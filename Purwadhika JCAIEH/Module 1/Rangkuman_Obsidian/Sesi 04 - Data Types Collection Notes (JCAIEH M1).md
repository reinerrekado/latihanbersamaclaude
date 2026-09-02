---
tags: [jcaieh/module1, sesi-04, python, list, tuple, set, dictionary, mutable, immutable, hashable, indexing, slicing, jcaieh/module1/sesi04]
bootcamp: JCAIEH
module: 1
session: 4
aliases: ["Sesi 4", "Data Types Collection Notes"]
---

# Session 4 — Data Types Collection Notes

Catatan sesi keempat ini mencakup review latihan bilangan prima, pengantar tipe data koleksi (kategori Sequences/Mappings/Sets, mutability), lalu pembahasan mendalam List, Tuple, Indexing & Slicing, Set, dan Dictionary, ditutup dengan pengenalan platform HackerRank untuk latihan problem solving mandiri.

---

## Bab 1 — Review Sesi Sebelumnya: Sesi Tanya Jawab & Latihan Bilangan Prima

### 1.1 Aturan Validasi Input Range

Sebelum melakukan perhitungan, program harus memvalidasi input _range_ yang dimasukkan oleh pengguna. Input tersebut terdiri dari batas bawah (_lower limit_) dan batas atas (_upper limit_).

**Syarat Kelayakan Input:**

- Harus berupa bilangan bulat positif (_positive integer_).
- Batas bawah tidak boleh bernilai lebih besar dari batas atas.
- Kedua nilai batas tidak boleh bernilai negatif (di bawah 0).

**Tabel Validasi Range Input:**

| Kondisi Input | Status Kelayakan | Tindakan Program |
| --- | --- | --- |
| `lower` > `upper` | Tidak Valid | Menghentikan eksekusi / Memberikan pesan error |
| `lower` < 0 atau `upper` < 0 | Tidak Valid | Menghentikan eksekusi / Memberikan pesan error |
| `lower` >= 0 dan `lower` <= `upper` | Valid | Melanjutkan ke proses perhitungan bilangan prima |

> [!tip] Audio Insight — Validasi Diletakkan di Awal untuk Menghindari Komputasi Sia-sia
> Berdasarkan penjelasan dosen di kelas, penanganan validasi range ini diletakkan di bagian paling awal program menggunakan blok percabangan `if`. Hal ini bertujuan untuk memastikan program tidak melakukan _computation_ yang sia-sia apabila data input dari pengguna terdeteksi tidak valid.

### 1.2 Algoritma Pencarian dan Perhitungan Bilangan Prima

Setelah input dipastikan valid, program akan mengevaluasi setiap angka di dalam rentang (_range_) tersebut untuk mendeteksi apakah angka tersebut merupakan bilangan prima, kemudian mengakumulasikannya.

**Struktur Perulangan Utama (Outer Loop):**

- **Inklusivitas Batas Atas:** rentang iterasi diatur menggunakan `range(lower, upper + 1)`. Penambahan `1` diperlukan karena `range()` bawaan Python bersifat eksklusif di batas akhir (hanya memproses hingga `upper - 1`). Dengan `upper + 1`, batas akhir tetap diikutsertakan.
- **Penyaringan Angka <= 1:** bilangan prima harus lebih besar dari 1. Angka 1 dan di bawahnya langsung diabaikan (_skip_).

**Logika Pembuktian Bilangan Prima** (metode pembuktian terbalik):

1. **Asumsi Awal:** setiap angka yang lolos penyaringan awal diasumsikan sebagai bilangan prima terlebih dahulu dengan mengeset variabel flag `is_prime = True`.
2. **Pencarian Pembagi (Divisor):** program melakukan perulangan kedua (_inner loop_) untuk menguji pembagi (variabel `i`) dari rentang `2` hingga `number - 1` (`range(2, number)`). Angka 1 dan angka itu sendiri dikecualikan.
3. **Pembuktian Negatif:** di dalam _inner loop_, dilakukan operasi modulus (`number % divisor`). Jika ditemukan pembagi yang menghasilkan sisa bagi sama dengan nol (habis dibagi), maka status kelayakan diubah menjadi bukan prima (`is_prime = False`) dan perulangan dalam segera dihentikan dengan `break`, karena satu bukti pembagi sudah cukup untuk menggugurkan kelayakan bilangan prima.
4. **Akumulasi Penjumlahan:** jika setelah perulangan dalam selesai nilai `is_prime` tetap `True`, angka tersebut dipastikan bilangan prima dan ditambahkan ke variabel akumulator total (`total_prima`).

### 1.3 Penanganan Kasus Khusus: Angka 2 sebagai Bilangan Prima

Angka 2 merupakan satu-satunya bilangan prima genap. Algoritma ini mampu menangani angka 2 secara otomatis dan akurat tanpa memerlukan percabangan kondisi tambahan.

**Alur Eksekusi Angka 2:**

1. Angka 2 lolos dari penyaringan awal karena `2 > 1`.
2. Asumsi awal diatur: `is_prime = True`.
3. Program masuk ke _inner loop_ pembagi dengan parameter rentang `range(2, 2)`.
4. Dalam Python, objek `range(2, 2)` tidak menghasilkan elemen angka apa pun (kosong), sehingga perulangan pembagi langsung dilewati (_skip_).
5. Karena perulangan pembagi dilewati, status `is_prime` tidak pernah berubah menjadi `False`.
6. Nilai `is_prime` tetap `True` dan angka 2 didefinisikan sebagai bilangan prima, kemudian diakumulasikan ke dalam variabel total.

**Tabel Tracing Logika Pemeriksaan Angka:**

| Angka (`number`) | Asumsi Awal | Rentang Pembagi (`range(2, number)`) | Evaluasi Modulus | Status Akhir (`is_prime`) | Akumulasi |
| --- | --- | --- | --- | --- | --- |
| 2 | `True` | `range(2, 2)` (Kosong) | Tidak dievaluasi (loop dilewati) | `True` | Ditambahkan ke total |
| 3 | `True` | `range(2, 3)` (Isi: 2) | `3 % 2 != 0` | `True` | Ditambahkan ke total |
| 4 | `True` | `range(2, 4)` (Isi: 2, 3) | `4 % 2 == 0` (Habis dibagi) | `False` (Mengalami `break`) | Diabaikan |

> [!warning] Audio Insight — Mengapa Angka 2 Terdeteksi Prima Tanpa Proses Pembagian
> Dalam rekaman sesi tanya jawab kelas, sempat muncul kebingungan mengenai mengapa angka 2 dapat terdeteksi sebagai prima padahal program tidak melakukan proses pembagian divisor. Dosen memberikan klarifikasi penting bahwa hal ini dikarenakan objek `range(2, 2)` menghasilkan rentang kosong pada interpreter Python. Akibatnya, perulangan pembagi otomatis terlewati, dan program langsung mempertahankan status default `is_prime = True`.

### 1.4 Contoh Implementasi Kode Python

```python
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

> [!info] Lihat juga
> Soal bilangan prima ini pertama kali dibahas sebagai Soal 4 di [[Sesi 03 - Conditional and Loop Statement (JCAIEH M1)|Sesi 03 - Conditional and Loop Statement]] Bab 8.2 — di sini logikanya di-review ulang dengan penekanan pada kasus edge case angka 2.

---

## Bab 2 — Pengantar Tipe Data Koleksi (Collection Data Types) di Python

### 2.1 Definisi dan Kategori Collection Data Types

[[Kamus & Cheatsheet (JCAIEH M1)#C|Collection Data Types]] adalah objek yang menampung nol atau lebih objek anggota yang disebut sebagai elemen. Python menyediakan berbagai macam tipe koleksi bawaan (_built-in_) maupun pembantu (_auxiliary_) untuk efisiensi penyimpanan data.

Secara garis besar, Collection Data Types di Python dibagi ke dalam 3 kategori utama: **Sequences** (Urutan), **Mappings** (Pemetaan), dan **Sets** (Himpunan).

| Type | Class | Category | Kind | Mutable |
| --- | --- | --- | --- | --- |
| `ranges` | `range` | _sequences_ | _Non-primitive_ | No |
| `tuples` | `tuple` | _sequences_ | _Non-primitive_ | No |
| `lists` | `list` | _sequences_ | _Non-primitive_ | Yes |
| `dictionaries` | `dict` | _mappings_ | _Non-primitive_ | Yes |
| `sets` | `set` | _sets_ | _Non-primitive_ | Yes |
| `frozen sets` | `frozenset` | _sets_ | _Non-primitive_ | No |

### 2.2 Karakteristik Mutability

Sifat _mutability_ mengacu pada kemampuan suatu tipe data untuk diubah nilainya setelah objek dideklarasikan di dalam memori komputer:

- **[[Kamus & Cheatsheet (JCAIEH M1)#M|Mutable]] (Bisa Diubah):** elemen-elemen di dalam objek dapat dimodifikasi, ditambah, dihapus, atau diganti setelah objek berhasil dibuat. Contoh: `list`, `dict`, `set`.
- **[[Kamus & Cheatsheet (JCAIEH M1)#I|Immutable]] (Tidak Bisa Diubah / Read-Only):** elemen-elemen bersifat statis dan sama sekali tidak dapat diubah, diganti, atau dimodifikasi setelah deklarasi awal. Contoh: `range`, `tuple`, `frozenset`.

```python
# Demonstrasi cepat mutable vs immutable
angka_list = [1, 2, 3]
angka_list[0] = 99          # BOLEH -> list bersifat mutable
print(angka_list)           # Output: [99, 2, 3]

angka_tuple = (1, 2, 3)
# angka_tuple[0] = 99        # akan memicu: TypeError: 'tuple' object does not support item assignment
```

> [!info] Lihat juga
> Konsep _mutable_/_immutable_ ini sudah disinggung sekilas saat pengenalan List/Tuple/Set/Dict di [[Sesi 01 - Introduction to DS Python Statistics SQL Git and GitHub (JCAIEH M1)|Sesi 01 - Introduction to DS Python Statistics SQL Git and GitHub]] Bab 5.4. Di sesi ini kita membahasnya jauh lebih dalam, termasuk perbedaan `id()` memori antar variabel (lihat Bab 3.2.3 di bawah).

> [!tip] Audio Insight — Alur Kerja Git dalam Pembelajaran Praktis
> Di dalam pelaksanaan kelas AI Engineering Purwadhika, dosen mengintegrasikan sistem pengontrol versi (_version control system_) menggunakan platform GitHub untuk mengelola materi latihan praktis secara efisien. Alur kerja Git yang wajib diikuti oleh siswa:
> 1. **Kloning Repositori Awal (`git clone`):** siswa melakukan pengunduhan atau penyalinan repositori pusat GitHub di awal kelas agar semua materi latihan tersimpan secara lokal.
> 2. **Pembaruan Berkas Materi (`git pull`):** ketika ada folder latihan baru atau pembaruan materi yang diunggah oleh dosen (seperti materi folder `collection data type`), siswa tidak perlu melakukan kloning ulang — cukup menjalankan `git pull` pada terminal mereka untuk menarik seluruh berkas materi terbaru dari repositori pusat.
>
> ```bash
> git pull
> ```
>
> Penerapan metode ini bertujuan melatih kemampuan praktis siswa dalam berinteraksi dengan Git agar siap menghadapi standar industri pekerjaan sebagai AI Engineer. (Lihat detail perintah Git lengkap di [[Sesi 02 - Intro to Git and GitHub (JCAIEH M1)|Sesi 02 - Intro to Git and GitHub]].)

---

## Bab 3 — Tipe Data Python List

### 3.1 Konsep Dasar List

[[Kamus & Cheatsheet (JCAIEH M1)#L|List]] adalah salah satu tipe data koleksi bawaan di Python yang digunakan untuk menyimpan beberapa nilai (elemen) dalam satu variabel tunggal. Penggunaan list bertujuan untuk menghindari pembuatan banyak variabel individual secara tidak praktis (misalnya menghindari deklarasi `student_1`, `student_2`, hingga `student_100` secara manual).

**Karakteristik teknis tipe data List:**

- Ditulis menggunakan kurung siku `[...]`.
- Setiap elemen di dalamnya memiliki indeks (_ordered_) yang dimulai dari angka 0 (_zero-based indexing_).
- Bersifat _mutable_ — nilai elemen di dalamnya dapat diubah, ditambah, atau dihapus setelah objek dideklarasikan.
- Mendukung penyimpanan data campuran (_mixed types_) — satu list dapat menampung integer, string, float, boolean, hingga objek list lain (_nested list_).

### 3.1.1 Deklarasi List

| Jenis List | Sintaks Deklarasi | Karakteristik / Hasil |
| --- | --- | --- |
| List Kosong | `empty_list = []` atau `empty_list = list()` | Menghasilkan objek list dengan jumlah elemen nol. Kedua metode ini bernilai setara (_equal_). |
| List Homogen | `students = ["andi", "budi", "cinta"]` | Menyimpan beberapa nilai dengan tipe data yang sama (string). |
| List Campuran (_Mixed List_) | `mixed_list = [1, "andi", [2.5, range(10)]]` | Menyimpan elemen dengan tipe campuran (integer, string, dan list bersarang berisi float serta objek range). |

```python
mixed_list = [1, "andi", [2.5, range(10)]]

# Mengakses elemen di dalam nested list -> perlu pengindeksan ganda
print(mixed_list[1])       # Output: andi
print(mixed_list[2])       # Output: [2.5, range(0, 10)]
print(mixed_list[2][0])    # Output: 2.5  -> akses spesifik elemen di dalam list bersarang
```

### 3.2 Metode dan Fungsi Bawaan List

**3.2.1 Metode untuk Menambahkan Elemen:**

- `.append(item)`: menambahkan satu elemen baru di bagian paling akhir list.
- `.insert(index, item)`: menyisipkan satu elemen baru pada posisi indeks spesifik. Elemen di posisi indeks tersebut dan setelahnya akan bergeser ke kanan.
- `.extend(iterable)`: menggabungkan seluruh elemen dari objek iterable lain (seperti list lain) secara sejajar ke dalam list utama.

```python
buah = ["apple", "banana"]

buah.append("cherry")
print(buah)  # Output: ['apple', 'banana', 'cherry']

buah.insert(1, "avocado")
print(buah)  # Output: ['apple', 'avocado', 'banana', 'cherry']

buah.extend(["date", "elderberry"])
print(buah)  # Output: ['apple', 'avocado', 'banana', 'cherry', 'date', 'elderberry']
```

**3.2.2 Metode untuk Menghapus Elemen:**

- `.pop(index)`: menghapus elemen berdasarkan posisi indeks dan mengembalikan (_return_) nilai elemen tersebut. Jika indeks dikosongkan, secara default menghapus dan mengembalikan elemen paling terakhir.
- `.remove(value)`: menghapus elemen pertama yang memiliki nilai cocok dengan parameter. Jika nilai tidak ditemukan, Python akan memicu `ValueError`.
- `.clear()`: mengosongkan seluruh isi list, menghasilkan list kosong tanpa menghapus objek list itu sendiri dari memori.

```python
angka = [10, 20, 30, 40]

hasil_pop = angka.pop(1)
print(hasil_pop)  # Output: 20 (nilai yang dihapus)
print(angka)       # Output: [10, 30, 40]

hasil_pop_default = angka.pop()
print(hasil_pop_default)  # Output: 40 (elemen terakhir, karena index dikosongkan)
print(angka)                # Output: [10, 30]

angka.remove(10)
print(angka)  # Output: [30]

# angka.remove(999)  -> akan memicu ValueError: list.remove(x): x not in list

angka.clear()
print(angka)  # Output: []
```

**3.2.3 Metode untuk Menggandakan List (`.copy()` vs Referensi)**

Dalam Python, melakukan penugasan langsung variabel list baru ke variabel list lama (`new_list = old_list`) tidak melakukan penggandaan objek secara fisik di memori. Kedua variabel tersebut akan merujuk (_point_) ke alamat memori (_memory address_) yang sama.

Untuk menduplikasi list secara aman ke alamat memori yang berbeda, wajib menggunakan metode `.copy()` untuk menghasilkan salinan dangkal (_[[Kamus & Cheatsheet (JCAIEH M1)#S|shallow copy]]_).

| Metode Pendekatan | Sintaks Kode | Karakteristik Perubahan Data | Dampak pada Objek Memori |
| --- | --- | --- | --- |
| Referensi Langsung (Tanpa Copy) | `list_b = list_a` | Perubahan elemen pada `list_b` akan otomatis memengaruhi `list_a` (dan sebaliknya). | Kedua variabel memiliki ID memori yang sama (`id(list_a) == id(list_b)`). |
| Shallow Copy (Dengan `.copy()`) | `list_b = list_a.copy()` | Perubahan elemen pada `list_b` tidak akan memengaruhi `list_a`. | Kedua variabel merujuk pada objek memori yang berbeda (`id(list_a) != id(list_b)`). |

```python
list_a = [1, 2, 3]

# Referensi langsung -> BAHAYA, list_b dan list_a adalah objek yang SAMA
list_b = list_a
list_b.append(4)
print(list_a)  # Output: [1, 2, 3, 4] -> list_a IKUT BERUBAH walau yang diubah list_b!

# Shallow copy -> AMAN, list_c adalah salinan terpisah
list_c = list_a.copy()
list_c.append(5)
print(list_a)  # Output: [1, 2, 3, 4] -> list_a TIDAK berubah
print(list_c)  # Output: [1, 2, 3, 4, 5]
```

**3.2.4 Fungsi Bawaan (Built-in Functions) pada List:**

- `len(list_obj)`: mengembalikan jumlah total elemen di dalam list.
- `sorted(list_obj)`: mengembalikan list baru yang elemennya telah terurut secara menaik (_ascending_ secara default) tanpa memodifikasi urutan elemen pada objek list asli.

```python
angka = [5, 2, 9, 1]
print(len(angka))     # Output: 4
print(sorted(angka))  # Output: [1, 2, 5, 9]
print(angka)           # Output: [5, 2, 9, 1] -> list asli TIDAK berubah
```

### 3.3 Konsep List Comprehension

_[[Kamus & Cheatsheet (JCAIEH M1)#L|List comprehension]]_ adalah fitur Python yang menawarkan sintaksis lebih ringkas untuk membuat list baru berdasarkan elemen-elemen dari list atau objek iterable yang sudah ada.

**Sintaksis dasar:**

```python
newlist = [expression for item in iterable if condition]
```

**Keterangan komponen:**

1. `expression`: hasil akhir atau manipulasi elemen yang akan dimasukkan ke dalam list baru.
2. `for item in iterable`: proses perulangan dasar untuk mengambil tiap elemen dari objek asal.
3. `if condition`: operasi penyaringan (_filtering_) opsional — elemen hanya diproses oleh `expression` jika kondisi ini terpenuhi (`True`).

**Perbandingan Implementasi — menyaring buah dengan huruf `"a"` dan mengubahnya menjadi uppercase:**

```python
# Pendekatan Konvensional (Tanpa List Comprehension)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruit_with_a = []

for fruit in fruits:
    if "a" in fruit:
        fruit_with_a.append(fruit.upper())

print(fruit_with_a)
# Output: ['APPLE', 'BANANA', 'DATE']
```

```python
# Pendekatan Modern (Dengan List Comprehension)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruit_with_a = [fruit.upper() for fruit in fruits if "a" in fruit]

print(fruit_with_a)
# Output: ['APPLE', 'BANANA', 'DATE']
```

> [!tip] Audio Insight — Perbedaan `.extend()` dan `.append()` untuk Menambah List ke List
> Berdasarkan penjelasan interaktif di kelas, terdapat perbedaan mendasar ketika menambahkan elemen berupa list ke dalam list lain:
> - Jika menggunakan `.append(list_lain)`, seluruh objek `list_lain` dimasukkan utuh sebagai **satu elemen tunggal bersarang (nested list)** di bagian akhir list utama.
> - Jika menggunakan `.extend(list_lain)`, Python akan **membongkar (_unpack_)** seluruh elemen dari `list_lain` terlebih dahulu, lalu menggabungkannya satu per satu secara sejajar dengan elemen di list utama.
>
> ```python
> list_a = [1, 2, 3]
> list_b = [4, 5, 6]
>
> # Menggunakan .append()
> list_b_append = list_b.copy()
> list_b_append.append(list_a)
> # Hasil: [4, 5, 6, [1, 2, 3]]
>
> # Menggunakan .extend()
> list_b_extend = list_b.copy()
> list_b_extend.extend(list_a)
> # Hasil: [4, 5, 6, 1, 2, 3]
> ```

> [!warning] Audio Insight — Operator `is` vs Operator `==` (Kesamaan Nilai vs Kesamaan Memori)
> Dalam sesi tanya jawab, dijelaskan perbedaan mendasar antara membandingkan nilai variabel dan membandingkan lokasi fisik memori:
> - Operator `==` digunakan untuk mengevaluasi **kesamaan nilai** (_value equality_) antar variabel.
> - Operator `is` digunakan untuk mengevaluasi **kesamaan identitas memori** (_reference equality_) — memastikan apakah kedua variabel merujuk pada alamat memori yang persis sama.
> - Setiap objek variabel di memori memiliki alamat unik yang dapat dilacak menggunakan fungsi bawaan `id(nama_variabel)`.
>
> ```python
> # Contoh Tracing Identitas Memori
> list_x = [1, 2, 3]
> list_y = list_x.copy()
>
> print(list_x == list_y)  # True  (Nilai elemen di dalamnya sama)
> print(list_x is list_y)  # False (Disimpan di alamat memori yang berbeda karena hasil .copy())
> print(id(list_x) == id(list_y))  # False
> ```

> [!tip] Audio Insight — Cara Membaca List Comprehension Tahap demi Tahap
> Bagi programmer pemula, sintaksis list comprehension seringkali membingungkan karena urutan penulisannya yang terbalik dibandingkan perulangan `for` biasa. Dosen memberikan metode praktis untuk membaca dan merancang list comprehension secara bertahap:
> 1. **Tentukan Sumber Data (Looping):** fokus terlebih dahulu pada blok perulangan tengah, yaitu `for item in iterable`.
> 2. **Tentukan Penyaringan (Filtering):** baca blok kondisi di bagian paling kanan, yaitu `if condition`. Tentukan elemen mana saja yang memenuhi syarat untuk lolos seleksi.
> 3. **Tentukan Aksi Akhir (Expression):** baca blok ekspresi di bagian paling kiri, yaitu manipulasi apa yang ingin diterapkan pada elemen yang lolos seleksi sebelum dimasukkan ke list baru (seperti `.upper()`, `.capitalize()`, atau operasi aritmatika).
>
> Metode ini terbukti mempermudah siswa kelas AI Engineering dalam menyelesaikan tugas penyaringan karakter teks dan operasi matematika secara cepat tanpa mengalami kegagalan logika pemrograman.

> [!info] Lihat juga
> List comprehension adalah nenek moyang langsung dari operasi vektor di Pandas/NumPy — lihat [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] untuk cara serupa memfilter dan mentransformasi kolom data tanpa loop eksplisit.

---

## Bab 4 — Tipe Data Python Tuple

### 4.1 Konsep Dasar dan Karakteristik Tuple

[[Kamus & Cheatsheet (JCAIEH M1)#T|Tuple]] adalah tipe data koleksi di Python yang digunakan untuk menyimpan beberapa nilai di dalam satu variabel tunggal, mirip dengan List. Perbedaan mendasar antara List dan Tuple terletak pada sifat keterubahannya (_mutability_). Tuple bersifat _immutable_ — nilai atau elemen di dalamnya bersifat _read-only_ dan tidak dapat diubah, ditambah, atau dihapus setelah objek Tuple dideklarasikan di dalam memori komputer.

**Kasus Penggunaan Utama** — Tuple ideal untuk menampung kumpulan data yang nilainya bersifat konstan atau tidak boleh mengalami modifikasi sepanjang program berjalan:

- **Geolokasi:** menyimpan koordinat wilayah dalam format `(latitude, longitude)`, misalnya `jakarta_geolocation = (-6.200000, 106.816666)`.
- **Representasi Warna:** menyimpan format warna RGB (Red, Green, Blue), misalnya `white = (255, 255, 255)`.

**Karakteristik dan Sintaksis Penulisan:**

| Karakteristik | Deskripsi Teknis |
| --- | --- |
| **Sifat Memori** | _Immutable_ (Read-Only) |
| **Sintaksis** | Kurung biasa `(...)` |
| **Pengindeksan** | Berbasis Nol (_Zero-based indexing_) |
| **Kompatibilitas** | Mendukung _mixed types_, elemen kosong, dan _nested tuple_ |

Tuple kosong dapat dideklarasikan menggunakan fungsi pembantu `tuple()` atau kurung biasa kosong `()`.

### 4.2 Deklarasi Khusus Single Item Tuple

Dalam menulis Tuple yang hanya memiliki satu elemen (_[[Kamus & Cheatsheet (JCAIEH M1)#S|single item tuple]]_), terdapat aturan penulisan sintaksis khusus yang wajib dipenuhi agar interpreter Python dapat mengenali objek tersebut sebagai Tuple, bukan sebagai tipe data primitif biasa.

- **Aturan Tanda Koma Akhir:** wajib menambahkan tanda koma `,` langsung setelah elemen pertama di dalam tanda kurung.
- **Contoh Sintaksis Valid:** `my_tuple = (5,)`.
- **Konsekuensi Kegagalan Sintaksis:** jika dideklarasikan tanpa tanda koma (misalnya `my_tuple = (5)`), Python akan mendeteksinya sebagai pengelompokan operasi matematika biasa (_parenthesis grouping_) dan variabel tersebut akan dideklarasikan sebagai tipe data `int` dengan nilai `5`.

```python
salah_dikira_int = (5)
print(type(salah_dikira_int))  # Output: <class 'int'>  -> BUKAN tuple!

benar_single_tuple = (5,)
print(type(benar_single_tuple))  # Output: <class 'tuple'>
```

### 4.3 Metode dan Fungsi Bawaan Tuple

Karena sifatnya yang _immutable_, Tuple tidak memiliki metode manipulasi elemen seperti `.append()` atau `.pop()`. Metode bawaan Tuple dirancang khusus hanya untuk mengakses nilai atau melakukan pelacakan informasi elemen.

| Metode / Fungsi | Jenis | Deskripsi |
| --- | --- | --- |
| `.index(value)` | _Method_ | Mengembalikan indeks posisi pertama dari nilai yang dicari. Menghasilkan error jika nilai tidak ditemukan. |
| `.count(value)` | _Method_ | Menghitung dan mengembalikan frekuensi kemunculan nilai tertentu di dalam Tuple. |
| `len(tuple_obj)` | _Function_ | Mengembalikan jumlah total elemen yang ada di dalam objek Tuple. |

### 4.4 Contoh Implementasi Kode Python

```python
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
print("Latitude:", latitude)               # Output: Latitude: -6.2
print("Single Item Type:", type(single_item))  # Output: Single Item Type: <class 'tuple'>
print("Jumlah elemen Fibonacci:", total_elements)  # Output: Jumlah elemen Fibonacci: 7
```

> [!warning] Audio Insight — `.index()` Memicu `ValueError` Jika Nilai Tidak Ditemukan
> Berdasarkan penjelasan dosen dalam rekaman audio kelas, penggunaan metode `.index()` untuk mencari posisi elemen di dalam Tuple harus dilakukan secara hati-hati. Jika Anda memanggil `.index()` untuk nilai yang sama sekali tidak terdaftar di dalam Tuple, interpreter Python akan segera memicu kegagalan runtime berupa `ValueError: tuple.index(x): x not in tuple`. Untuk mengatasi crash ini pada program nyata, praktisi AI Engineering disarankan melakukan pengecekan keanggotaan menggunakan operator `in` sebelum menjalankan pencarian indeks, atau menggunakan blok penanganan pengecualian `try-except`.

```python
fibonacci_numbers = (1, 1, 2, 3, 5, 8, 13)

# Cara aman: cek dulu dengan operator 'in' sebelum .index()
if 99 in fibonacci_numbers:
    print(fibonacci_numbers.index(99))
else:
    print("Nilai 99 tidak ditemukan di dalam tuple")
# Output: Nilai 99 tidak ditemukan di dalam tuple
```

> [!tip] Audio Insight — Mengapa Python Mewajibkan Koma pada Single Item Tuple
> Dalam sesi tanya jawab interaktif, dijelaskan secara mendalam mengapa Python mewajibkan penulisan koma pada Tuple beranggota tunggal seperti `(5,)`. Tanda kurung biasa `(...)` di Python memiliki peran ganda: (1) sebagai pendefinisi objek Tuple; (2) sebagai operator pengelompokan prioritas matematika (_parenthesis grouping_), seperti dalam rumus `(2 + 3) * 5`. Apabila Anda menuliskan `my_tuple = (5)` tanpa koma, Python memprioritaskannya sebagai ekspresi matematika biasa, sehingga objek Tuple tidak pernah dibuat. Penambahan koma `,` di dalam kurung memberikan petunjuk mutlak kepada interpreter Python bahwa ekspresi tersebut harus dievaluasi sebagai sebuah objek Tuple.

---

## Bab 5 — Indexing dan Slicing pada List dan Tuple

### 5.1 Indexing (Pengindeksan) Elemen Tunggal

Setiap elemen di dalam tipe data `list` dan `tuple` memiliki posisi spesifik yang disebut sebagai indeks, digunakan untuk menunjuk dan mengakses elemen tunggal secara langsung.

**Aturan Pengindeksan Python** — Python menggunakan sistem pengindeksan berbasis nol (_[[Kamus & Cheatsheet (JCAIEH M1)#Z|zero-based indexing]]_), yang berarti elemen pertama selalu dimulai dari indeks `0`. Python juga mendukung pengindeksan negatif untuk mempermudah akses elemen dari arah belakang.

- **Indeks Positif:** dimulai dari `0` untuk elemen pertama di sebelah kiri, bergerak maju ke kanan (`1`, `2`, `3`, dst).
- **[[Kamus & Cheatsheet (JCAIEH M1)#N|Indeks Negatif]]:** dimulai dari `-1` untuk elemen terakhir di sebelah kanan, bergerak mundur ke kiri (`-2`, `-3`, `-4`, dst).

**Tabel Skema Indeks Positif dan Negatif** untuk `students = ["andi", "budi", "cinta", "doni"]`:

| Elemen | "andi" | "budi" | "cinta" | "doni" |
| --- | :-: | :-: | :-: | :-: |
| **Indeks Positif** | `0` | `1` | `2` | `3` |
| **Indeks Negatif** | `-4` | `-3` | `-2` | `-1` |

```python
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

### 5.2 Slicing (Pemotongan Bagian) Data

[[Kamus & Cheatsheet (JCAIEH M1)#S|Slicing]] digunakan apabila program memerlukan sebagian porsi data (_portion_) atau sub-koleksi dari `list` atau `tuple`, bukan hanya satu elemen tunggal.

**Format Sintaksis Slicing:**

```python
list_or_tuple[start:stop:step]
```

- **`start`**: indeks awal pemotongan (inklusif). Jika dikosongkan, Python akan memulai dari indeks paling awal (`0`).
- **`stop`**: indeks batas akhir pemotongan (eksklusif). Pemotongan hanya akan dilakukan hingga indeks `stop - 1`. Jika dikosongkan, pemotongan akan berjalan hingga elemen terakhir.
- **`step`**: jarak lompatan antar elemen yang diambil selama proses pemotongan. Nilai default parameter ini adalah `1`.

```python
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

**Menelusuri `students[0:3:2]` elemen demi elemen** — bukan hanya "indeks 0 dan 3" sebagai dua titik ujung, tapi setiap indeks yang dilewati dari `start=0` sampai sebelum `stop=3` dengan lompatan `step=2` dicek satu per satu:

| Indeks yang dicek | Nilai di indeks tsb | Apakah `< stop (3)`? | Termasuk dalam hasil? |
| --- | --- | --- | --- |
| 0 | "andi" | Ya | Ya |
| 0 + step (2) | "cinta" | Ya (2 < 3) | Ya |
| 2 + step (4) | — | Tidak (4 >= 3), berhenti | — |

Hasil akhirnya: `["andi", "cinta"]` — elemen di indeks 1 ("budi") sengaja **dilewati**, bukan ikut terbawa, karena `step=2` melompati satu indeks setiap kali.

### 5.3 Penanganan Kasus Out-of-Range (Batas Indeks)

Python memiliki karakteristik unik yang sangat berbeda dalam menangani kondisi batas indeks yang melampaui kapasitas elemen (_[[Kamus & Cheatsheet (JCAIEH M1)#O|out-of-range]]_) antara operasi indexing langsung dan slicing.

- **Akses Indexing Langsung:** jika program mencoba mengakses satu indeks tertentu yang nilainya melebihi kapasitas elemen yang ada (misalnya mengakses indeks ke-10 pada list yang hanya memiliki 4 elemen), Python akan segera menghentikan program dan memicu error `IndexError: list index out of range`.
- **Akses Slicing:** jika operasi slicing dideklarasikan melewati batas indeks elemen yang tersedia (misalnya slicing mulai dari indeks ke-10), Python tidak akan memicu error apa pun. Interpreter Python secara aman akan mengembalikan koleksi kosong (`[]` untuk list atau `()` untuk tuple).

| Fitur / Operasi | Sintaksis Contoh | Kondisi Indeks | Perilaku Interpreter Python |
| --- | --- | --- | --- |
| **Indexing** | `students[10]` | Melebihi kapasitas (_out-of-range_) | Crash dengan memicu `IndexError` |
| **Slicing** | `students[10:]` | Melebihi kapasitas (_out-of-range_) | Lolos tanpa error, mengembalikan koleksi kosong (`[]` atau `()`) |

```python
students = ["andi", "budi", "cinta", "doni"]

# print(students[10])   -> akan memicu: IndexError: list index out of range

# Contoh penanganan out-of-range pada Slicing (Aman dari error)
slicing_kosong = students[10:]
print(slicing_kosong)  # Output: []
```

> [!tip] Audio Insight — Efisiensi Penggunaan Indeks Negatif `-1`
> Di dalam rekaman kelas, dosen menekankan pentingnya pembiasaan penggunaan indeks negatif `-1` untuk mengambil data terakhir dari sebuah list atau tuple. Pendekatan ini dinilai jauh lebih efisien dan intuitif secara industri karena pengembang tidak perlu memanggil fungsi `len(list_or_tuple) - 1` untuk menghitung total elemen terlebih dahulu hanya untuk menjangkau elemen paling akhir.

> [!tip] Audio Insight — Mengapa Slicing Tidak Pernah Crash (Fail-Safe Mechanism)
> Dalam sesi diskusi praktis, dijelaskan alasan mengapa Python membiarkan operasi slicing yang di luar rentang (_out-of-range_) tetap berjalan tanpa memicu crash. Slicing dirancang untuk mengambil "porsi segmen data yang tersedia". Apabila segmen yang diminta berada di luar batas elemen aktual, Python mengasumsikan bahwa tidak ada elemen yang dapat diiris pada rentang tersebut, sehingga mengembalikan kontainer kosong (`[]` atau `()`) dianggap sebagai output logis yang aman untuk kelancaran jalannya aplikasi (_fail-safe mechanism_).

> [!info] Lihat juga
> Aturan slicing `[start:stop:step]` ini persis sama dengan slicing string `word[::-1]` yang dibahas di [[Sesi 03 - Conditional and Loop Statement (JCAIEH M1)|Sesi 03 - Conditional and Loop Statement]] Bab 1.5 (studi kasus palindrome).

---

## Bab 6 — Tipe Data Python Set

### 6.1 Konsep Dasar Set

[[Kamus & Cheatsheet (JCAIEH M1)#S|Set]] adalah tipe data koleksi di Python yang digunakan untuk menyimpan elemen-elemen unik secara otomatis dengan menghapus seluruh nilai duplikat. Sifat ini sangat berguna dalam menyaring data yang terdaftar lebih dari satu kali secara tidak sengaja.

**Karakteristik Utama Set:**

- **Unordered (Tidak Terurut):** elemen di dalam Set tidak memiliki posisi atau urutan yang konsisten.
- **Unindexed (Tidak Memiliki Indeks):** karena tidak terurut, elemen Set tidak dapat diakses menggunakan indeks seperti `my_set[0]`. Upaya melakukan indexing langsung pada Set akan menghasilkan kesalahan `TypeError: 'set' object is not subscriptable`.
- **Unique Elements Only:** Set secara otomatis mengabaikan dan menghapus nilai duplikat saat inisialisasi maupun saat manipulasi data.

**Tabel Karakteristik Deklarasi Set:**

| Kasus Deklarasi | Sintaksis | Keterangan Teknis |
| --- | --- | --- |
| Set dengan elemen | `{val1, val2, ...}` | Ditulis menggunakan kurung kurawal `{...}` dengan pemisah koma antar elemen. |
| Set kosong | `set()` | Wajib dideklarasikan menggunakan fungsi `set()`. |
| Kurung kurawal kosong | `{}` | **DILARANG** untuk Set kosong karena Python otomatis mendeteksinya sebagai Dictionary kosong. |
| Set Bersarang (_Nested Set_) | `frozenset()` | Set tidak dapat langsung menampung Set lain sebagai elemennya karena elemen Set harus bersifat _[[Kamus & Cheatsheet (JCAIEH M1)#H|hashable]]_ (_immutable_). Set bagian dalam wajib dibungkus dengan `frozenset()`. |

```python
data_duplikat = {1, 2, 2, 3}
print(data_duplikat)  # Output: {1, 2, 3} -> duplikat otomatis hilang

kurung_kosong = {}
print(type(kurung_kosong))  # Output: <class 'dict'> -> BUKAN set kosong!

set_kosong_benar = set()
print(type(set_kosong_benar))  # Output: <class 'set'>

# my_set[0]  -> akan memicu TypeError: 'set' object is not subscriptable

# Set bersarang wajib pakai frozenset karena elemen set harus hashable/immutable
set_bersarang = {frozenset({1, 2}), frozenset({3, 4})}
print(set_bersarang)  # Output: {frozenset({1, 2}), frozenset({3, 4})}
```

### 6.2 Metode dan Fungsi Bawaan Set

Sebagai objek _mutable_, elemen di dalam Set dapat ditambah atau dihapus setelah dideklarasikan.

**6.2.1 Penambahan Elemen:**

- `.add(item)`: menambahkan satu elemen tunggal ke dalam Set.
- `.update(iterable)`: menambahkan banyak elemen sekaligus dari objek lain yang bersifat _iterable_ (seperti List, Tuple, atau Set lain).

**6.2.2 Penghapusan Elemen:**

- `.remove(value)`: menghapus elemen tertentu berdasarkan nilainya. Jika nilai yang dicari tidak ditemukan di dalam Set, Python akan memicu kesalahan `KeyError`.
- `.discard(value)`: menghapus elemen tertentu berdasarkan nilainya secara aman. Jika nilai yang dicari tidak ditemukan, metode ini **tidak** akan memicu kesalahan dan eksekusi program tetap berjalan normal.
- `.pop()`: menghapus dan mengembalikan satu elemen acak dari Set. Karena Set bersifat tidak terurut, elemen yang dihapus tidak dapat diprediksi secara konsisten.
- `.clear()`: mengosongkan seluruh isi Set, menghasilkan Set kosong yang setara dengan `set()`.

```python
film = {"Inception", "The Matrix"}

film.remove("Inception")
print(film)  # Output: {'The Matrix'}

# film.remove("Interstellar")  -> akan memicu KeyError: 'Interstellar' (tidak ada di set)

film.discard("Interstellar")  # AMAN - tidak error walau "Interstellar" tidak ada
print(film)  # Output: {'The Matrix'} (tidak berubah, tapi tidak crash)
```

**6.2.3 Fungsi Umum & Duplikasi:**

- `len(set_name)`: mengembalikan jumlah elemen unik yang tersimpan di dalam Set.
- `.copy()`: membuat salinan dangkal (_shallow copy_) dari Set pada alamat memori yang berbeda untuk mencegah terjadinya bug referensi memori yang sama.

### 6.3 Operasi Matematika Set (Set Operations)

Set di Python mendukung operasi aljabar himpunan matematika, baik menggunakan metode bawaan maupun operator simbolis khusus.

| Operasi | Deskripsi Himpunan | Metode Bawaan | Operator | Contoh Hasil (`A` dan `B`) |
| --- | --- | --- | --- | --- |
| **[[Kamus & Cheatsheet (JCAIEH M1)#U|Union]]** | Menggabungkan seluruh elemen unik dari kedua himpunan. | `A.union(B)` | `A \| B` | `A={'a','b'}, B={'b','c'}` → Hasil: `{'a','b','c'}` |
| **[[Kamus & Cheatsheet (JCAIEH M1)#I|Intersection]]** | Mengambil elemen yang ada di kedua himpunan secara bersamaan. | `A.intersection(B)` | `A & B` | `A={'a','b'}, B={'b','c'}` → Hasil: `{'b'}` |
| **Difference** | Mengambil elemen himpunan pertama yang tidak ada di himpunan kedua. | `A.difference(B)` | `A - B` | `A={'a','b'}, B={'b','c'}` → Hasil: `{'a'}` |
| **[[Kamus & Cheatsheet (JCAIEH M1)#S|Symmetric Difference]]** | Mengambil elemen unik dari masing-masing himpunan yang tidak saling beririsan. | `A.symmetric_difference(B)` | `A ^ B` | `A={'a','b'}, B={'b','c'}` → Hasil: `{'a','c'}` |

**Hubungan dan Perbandingan Antar Himpunan:**

- **Subset** (`.issubset()` atau `<=`): `True` jika seluruh elemen himpunan `A` terkandung di dalam himpunan `B`.
- **Superset** (`.issuperset()` atau `>=`): `True` jika seluruh elemen himpunan `B` terkandung di dalam himpunan `A`.
- **Proper Subset** (`<`): `True` jika `A` adalah subset dari `B` dan `A` tidak sama dengan `B` (ada elemen di `B` yang tidak dimiliki `A`).
- **Proper Superset** (`>`): `True` jika `A` adalah superset dari `B` dan `A` tidak sama dengan `B`.

```python
A = {"a", "b"}
B = {"a", "b", "c"}

print(A.issubset(B))     # Output: True  (A <= B)
print(B.issuperset(A))   # Output: True  (B >= A)
print(A < B)               # Output: True  (proper subset -> A subset dari B DAN A != B)
print(A <= A)              # Output: True  (subset biasa -> A tetap subset dari dirinya sendiri)
print(A < A)                # Output: False (proper subset -> A TIDAK proper subset dari dirinya sendiri)
```

> [!tip] Audio Insight — Konversi Timbal Balik List dan Set
> Berdasarkan diskusi interaktif di kelas, terdapat penjelasan penting mengenai konversi tipe data:
> - List dapat dikonversi ke Set menggunakan fungsi `set(my_list)` untuk menyaring nilai duplikat secara instan.
> - Set yang telah bersih dari duplikat dapat dikonversi kembali menjadi List menggunakan fungsi `list(my_set)` sehingga datanya dapat dimanipulasi menggunakan indeks.
> - **Konsekuensi Memori:** proses konversi ini bersifat destruktif terhadap elemen duplikat asal. Elemen duplikat yang telah dibuang saat diubah menjadi Set tidak akan bisa dikembalikan lagi saat dikonversi ulang menjadi List.

> [!tip] Audio Insight — Studi Kasus Latihan Kelas: Analisis Pembagian Kelas Siswa
> Dalam sesi latihan mandiri kelas, siswa memecahkan studi kasus pembagian siswa berdasarkan dua kelas minat, `Python Class` dan `SQL Class`. Implementasi logisnya menggunakan metode aljabar himpunan:
> 1. **Mencari Siswa yang Mengambil Kedua Kelas (Irisan/Intersection):** mendeteksi siswa yang terdaftar di kelas Python sekaligus kelas SQL — contohnya Citra dan Doni.
> 2. **Mencari Siswa yang Hanya Mengambil Satu Kelas (Beda Setara/Symmetric Difference):** memisahkan siswa yang hanya mengambil salah satu kelas saja — seperti Andi, Budi, Efraim, dan Fajar.
> 3. **Mencari Siswa yang Hanya Mengambil Kelas Python (Selisih/Difference):** memisahkan siswa kelas Python murni dengan mengeluarkan nama siswa yang juga mengambil kelas SQL — menghasilkan Andi dan Budi.

### 6.4 Contoh Implementasi Kode Python

```python
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
print("Siswa di kedua kelas:", both_classes)  # Output: {'citra', 'doni'}

# Menghitung siswa yang hanya mengambil salah satu kelas (Symmetric Difference)
one_class_only = python_class ^ sql_class
print("Siswa di satu kelas saja:", one_class_only)  # Output: {'andi', 'budi', 'efraim', 'fajar'}

# Menghitung siswa yang hanya mengambil kelas Python saja (Difference)
pure_python = python_class - sql_class
print("Siswa kelas Python saja:", pure_python)  # Output: {'andi', 'budi'}
```

> [!info] Lihat juga
> Set (`.union`, `.intersection`) berkaitan langsung dengan konsep `JOIN` di SQL — lihat [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] dan [[Sesi 10 - SQL Working With Multiple Tables (JCAIEH M1)|Sesi 10 - SQL Working With Multiple Tables]], di mana `INNER JOIN` secara konseptual mirip dengan _intersection_, dan `UNION` di SQL persis meniru nama operasi set ini.

---

## Bab 7 — Tipe Data Python Dictionary

### 7.1 Konsep Dasar dan Karakteristik Dictionary

Python [[Kamus & Cheatsheet (JCAIEH M1)#D|Dictionary]] adalah tipe data koleksi yang menyimpan data dalam bentuk pasangan _key-value_ (kunci-nilai). Struktur ini dirancang untuk mempermudah pencarian dan pengambilan data secara cepat menggunakan sebuah _key_ sebagai pencari, berbeda dengan List atau Tuple yang mengandalkan posisi indeks angka.

**Aturan Penulisan dan Karakteristik Key-Value:**

- **Sintaksis:** ditulis menggunakan kurung kurawal `{...}` dengan pasangan _key_ dan _value_ yang dipisahkan oleh tanda titik dua (`key: value`). Masing-masing item dipisahkan dengan tanda koma.
- **Keunikan Key:** _Key_ bertindak sebagai pengindeks unik sehingga tidak boleh ada _key_ yang duplikat. Jika terdapat _key_ yang sama saat deklarasi, nilai terakhir akan menimpa nilai sebelumnya.
- **Sifat Value:** _Value_ bebas, diperbolehkan memiliki nilai yang sama (duplikat), dan dapat berupa tipe data apa pun (string, integer, float, boolean, list, tuple, set, atau dictionary lain).
- **Mutability:** Dictionary termasuk kategori tipe data yang _mutable_ — dapat ditambah, dihapus, atau diperbarui pasangan _key-value_-nya setelah dideklarasikan.

**Tabel Karakteristik Komponen Dictionary:**

| Komponen | Karakteristik Utama | Keunikan | Sifat Mutability | Tipe Data yang Diperbolehkan |
| --- | --- | --- | --- | --- |
| **Key** | Bertindak sebagai alamat/indeks | Harus Unik | Immutable | Tipe data dasar yang bersifat _hashable_ (string, number, tuple) |
| **Value** | Data yang disimpan | Boleh Duplikat | Mutable / Immutable | Semua jenis tipe data (termasuk list dan dictionary lain) |
| **Item** | Representasi satu pasang _key-value_ | Ditentukan oleh _Key_ | Mutable | Gabungan pasangan _key_ dan _value_ |

```python
data_duplikat_key = {"nama": "andi", "nama": "budi"}
print(data_duplikat_key)  # Output: {'nama': 'budi'} -> value terakhir menimpa yang pertama
```

> [!info] Lihat juga
> Baris "Key harus _hashable_ (immutable)" ini adalah alasan mengapa `list` **tidak bisa** dijadikan _key_ dictionary (`TypeError: unhashable type: 'list'`), sedangkan `tuple` bisa — ini menjelaskan langsung mengapa Set hanya bisa menampung `frozenset` sebagai elemen bersarang (lihat Bab 6.1 di atas): keduanya sama-sama membutuhkan elemen yang _hashable_.

### 7.2 Deklarasi Dictionary

**Cara Deklarasi Dictionary Kosong** — ada dua cara: (1) menggunakan kurung kurawal kosong `{}`; (2) menggunakan fungsi bawaan `dict()`. _Catatan penting: pendeklarasian menggunakan kurung kurawal kosong `{}` otomatis diidentifikasi sebagai dictionary kosong oleh Python, bukan set kosong_ (berbeda dengan Set yang justru wajib pakai `set()` — lihat Bab 6.1).

**Cara Deklarasi Dictionary dengan Data Awal** — penulisan data awal dilakukan dengan format pasangan langsung di dalam kurung kurawal. Dictionary juga mendukung struktur bersarang (_nested dictionary_) di mana sebuah _value_ di dalamnya berupa dictionary lain.

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

### 7.3 Akses dan Pembaruan Nilai Dictionary

**Mengakses Nilai (Accessing Value)** — terdapat dua metode utama:

1. **Menggunakan Kurung Siku (`dictionary["key"]`)**: mengakses nilai secara langsung lewat kata kunci. Jika _key_ yang dicari tidak terdaftar, Python akan langsung memicu error berupa `KeyError` dan menghentikan jalannya program.
2. **Menggunakan Metode `.get(key, default_value)`**: jauh lebih aman untuk menghindari crash. Jika _key_ ditemukan, mengembalikan nilainya. Jika tidak ditemukan, mengembalikan nilai default yang ditentukan (atau `None` jika nilai default dikosongkan) tanpa memicu error.

**Memperbarui atau Menambah Nilai** — dilakukan secara langsung dengan sintaksis penugasan nilai: `dictionary["key"] = value`. Jika _key_ **sudah ada**, nilai lama akan langsung ditimpa (_overwrite_). Jika _key_ **belum ada**, Python otomatis membuat pasangan _key-value_ baru.

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

# print(student_data["gpa_terakhir"])  -> akan memicu KeyError: 'gpa_terakhir'

# Mengakses nilai dengan .get() secara aman
# Key "is_active" tidak ada di dictionary, sehingga mengembalikan nilai default (False)
status_aktif = student_data.get("is_active", False)
print(status_aktif)  # Output: False

# Memperbarui nilai yang sudah ada
student_data["is_graduated"] = True

# Menambahkan pasangan key-value baru karena key "scholarship" belum ada
student_data["scholarship"] = True
```

### 7.4 Metode dan Fungsi Bawaan Dictionary

| Metode | Deskripsi Kerja | Contoh Sintaksis | Hasil Tindakan |
| --- | --- | --- | --- |
| `.update()` | Menambah atau memperbarui satu atau lebih pasangan _key-value_ sekaligus. | `dict.update({"gpa": 3.5})` | Mengubah nilai "gpa" menjadi 3.5 |
| `.setdefault()` | Mengambil nilai dari _key_; jika _key_ belum ada, otomatis menambahkannya dengan nilai default. | `dict.setdefault("minor", "math")` | Menambah "minor": "math" jika belum ada |
| `.get()` | Mengambil nilai berdasarkan _key_ secara aman tanpa memicu crash program. | `dict.get("age", 0)` | Mengembalikan nilai "age" atau 0 jika tidak ada |
| `.keys()` | Mengembalikan seluruh _keys_ di dalam objek koleksi khusus. | `dict.keys()` | Berupa `dict_keys([...])` |
| `.values()` | Mengembalikan seluruh _values_ di dalam objek koleksi khusus. | `dict.values()` | Berupa `dict_values([...])` |
| `.items()` | Mengembalikan seluruh pasangan _key-value_ dalam bentuk tuple. | `dict.items()` | Berupa `dict_items([(key, value), ...])` |
| `.pop()` | Menghapus item berdasarkan _key_ yang ditentukan dan mengembalikan nilainya. | `dict.pop("is_graduated")` | Menghapus item dan mengembalikan status boolean-nya |
| `.popitem()` | Menghapus dan mengembalikan pasangan _key-value_ yang terakhir kali dimasukkan. | `dict.popitem()` | Mengembalikan tuple pasangan terakhir yang dihapus |
| `.clear()` | Menghapus seluruh pasangan _key-value_ hingga dictionary menjadi kosong. | `dict.clear()` | Objek dictionary menjadi kosong `{}` |
| `.copy()` | Membuat salinan baru di alamat memori berbeda (_shallow copy_). | `new_dict = dict.copy()` | Mencegah perubahan data pada objek asli |

**Fungsi Umum Bawaan Python:**

- **`len(dictionary)`**: menghitung jumlah total elemen (pasangan _key-value_) yang tersimpan.
- **`sorted(dictionary)`**: mengurutkan kata kunci (_keys_) secara naik (_ascending_/alfabetis) dan mengembalikan hasilnya dalam bentuk List baru. Tidak mengubah susunan dictionary asli.

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
print(list(semua_kunci))  # Output: ['name', 'age', 'major', 'gpa', 'is_graduated', 'is_active', 'minor']

# 4. Menghapus data dengan .pop()
nilai_terhapus = student_data.pop("is_graduated")
print(nilai_terhapus)  # Output: False

# 5. Mengurutkan keys menggunakan sorted()
kunci_terurut = sorted(student_data)
print(kunci_terurut)  # Output: ['age', 'gpa', 'is_active', 'major', 'minor', 'name']
```

> [!warning] Audio Insight — Sederhanakan Lookup dengan `.get(key, default)` Bukan `if-else`
> Pada sesi latihan kelas, terdapat tugas pemrograman di mana siswa diminta membuat fungsi untuk mencari nama siswa berdasarkan kode ID yang diinputkan pengguna. Ketentuannya: jika ID tidak ditemukan, sistem harus menampilkan tulisan `"not found"`.
>
> Salah satu siswa (Anwar) menggunakan pendekatan kondisional klasik `if-else` untuk mengevaluasi apakah hasil pencarian bernilai kosong atau tidak:
>
> ```python
> # Pendekatan kondisional if-else (kurang efisien)
> hasil_cari = student_dict.get(input_id)
> if hasil_cari == None:
>     print("not found")
> else:
>     print(hasil_cari)
> ```
>
> Dosen memberikan koreksi penting untuk memotong redundansi kode tersebut. Metode `.get()` bawaan Python memiliki parameter opsional kedua yang dirancang khusus sebagai nilai pengembalian default (_default value_). Dengan memanfaatkan fitur ini, logika di atas dapat diringkas menjadi satu baris kode yang jauh lebih efisien, bersih, dan mudah dibaca:
>
> ```python
> # Solusi satu baris yang disarankan dosen
> print(student_dict.get(input_id, "not found"))
> ```
>
> Penerapan ini menghilangkan kebutuhan pemeriksaan manual `if-else` karena interpreter Python akan langsung menangani penyaringan tersebut di tingkat internal.

> [!warning] Audio Insight — `.update()` (Agresif/Menimpa) vs `.setdefault()` (Pasif/Defensif)
> Berdasarkan penjelasan dosen di kelas, terdapat perbedaan mendasar pada cara kerja manipulasi data antara metode `.update()` dan `.setdefault()`:
> - Metode `.update()` bertindak secara **agresif**. Jika _key_ yang dimasukkan sudah ada di dalam dictionary, nilai lama akan langsung ditimpa (_overwritten_). Jika _key_ belum ada, baru pasangan tersebut ditambahkan.
> - Metode `.setdefault()` bertindak secara **pasif/defensif**. Metode ini **hanya akan menambahkan data jika key yang dimaksud belum ada** di dalam dictionary. Jika _key_ tersebut sudah terdaftar, metode ini tidak akan mengubah nilai asli yang tersimpan dan hanya mengembalikan nilai lama yang ada.

```python
data = {"gpa": 3.2}

data.update({"gpa": 4.0})      # gpa sudah ada -> DITIMPA
print(data)  # Output: {'gpa': 4.0}

data.setdefault("gpa", 1.0)    # gpa sudah ada -> TIDAK diubah, hanya mengembalikan nilai lama
print(data)  # Output: {'gpa': 4.0} -> tetap 4.0, bukan 1.0!

data.setdefault("minor", "math")  # "minor" belum ada -> DITAMBAHKAN
print(data)  # Output: {'gpa': 4.0, 'minor': 'math'}
```

> [!warning] Audio Insight — `sorted()` pada Dictionary Hanya Mengurutkan Keys, Bukan Values
> Sering terjadi kesalahpahaman bahwa fungsi `sorted()` akan mengurutkan seluruh struktur dictionary beserta nilainya. Dosen menegaskan bahwa fungsi `sorted(student_data)` hanya akan mengekstrak kata kunci (_keys_) saja, mengurutkannya secara alfabetis atau menaik, lalu mengembalikannya sebagai tipe data List baru. Nilai (_values_) di dalam dictionary sama sekali tidak diikutkan dalam proses pengurutan ataupun diubah posisinya.

### 7.5 Catatan Tambahan: Sintaksis Akses Dictionary

```python
dictionary["key"]
```

Notasi kurung siku dengan _string key_ di dalamnya ini adalah cara paling dasar dan paling sering dipakai untuk mengambil nilai dari dictionary — lihat perbandingannya dengan `.get()` di Bab 7.3 di atas.

> [!info] Lihat juga
> Struktur _key-value_ pada Dictionary Python adalah cikal bakal konsep **row/record** di SQL dan **JSON** pada umumnya — lihat [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]]. Dictionary juga menjadi format input paling umum untuk membuat `Series`/`DataFrame` di [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] (misalnya `pd.DataFrame([student_data])`).

---

## Bab 8 — Praktik Logika Pemecahan Masalah (Problem Solving) Mandiri

### 8.1 Pengenalan Platform HackerRank

[[Kamus & Cheatsheet (JCAIEH M1)#H|HackerRank]] adalah platform evaluasi kode daring (_online code evaluation platform_) yang digunakan oleh pengembang untuk melatih logika pemrograman secara interaktif, serta digunakan oleh industri sebagai instrumen penyaringan kandidat teknis.

**Prosedur Pendaftaran Akun (Sign Up):**

- Mengakses portal resmi di alamat `hackerrank.com`.
- Memilih opsi registrasi khusus untuk pengembang, yaitu **"For Developers"** — menyediakan akses gratis (_free_) tanpa batasan waktu untuk modul-modul dasar latihan.
- Mengisi data kredensial atau menghubungkannya dengan akun GitHub atau email personal untuk verifikasi identitas.

**Navigasi Jalur Persiapan (Prepare Path):**

- Memilih menu **Prepare** di dalam dasbor utama.
- Memilih spesialisasi bahasa pemrograman: **Python**.
- Mengonfigurasi parameter penyaringan agar materi yang muncul sesuai dengan cakupan kelas dasar.

### 8.2 Struktur Latihan dan Kurikulum Rekomendasi

**Parameter Penyaringan Kategori Latihan:**

| Parameter Filter | Pengaturan Rekomendasi | Deskripsi |
| --- | --- | --- |
| **Difficulty** | _Easy_ (Mudah) | Menyediakan tantangan tingkat dasar untuk memperkuat sintaksis bahasa pemrograman. |
| **Subdomain** | _Python Basic_ | Fokus pada fitur bawaan bahasa Python tanpa melibatkan pustaka (_library_) eksternal yang kompleks. |

**Daftar Tantangan Pemecahan Masalah yang Direkomendasikan** (dari tingkat paling dasar):

- **Pernyataan Kondisional & Operator Aritmatika:** _Python If-Else_, _Arithmetic Operators_, _Python: Division_.
- **Algoritma Perulangan & Fungsi Cetak:** _Loops_, _Write a function_, _Print Function_.
- **Manipulasi Struktur & Koleksi Data:** _List Comprehensions_, _Find the Runner-Up Score!_, _Nested Lists_, _Finding the percentage_, _Lists_, _Tuples_, _sWAP cASE_.

> [!info] Lihat juga
> Daftar latihan HackerRank di atas adalah bahan utama sesi berikutnya — lihat [[Sesi 06 - Hackerrank Exercise (JCAIEH M1)|Sesi 06 - Hackerrank Exercise]] untuk pembahasan solusi latihannya.

### 8.3 Signifikansi Problem Solving dalam Karier AI Engineer

**Peran dalam Tahapan Seleksi Kerja:**

- **Ujian Teknis (Technical Test):** rekrutmen posisi AI Engineer di industri modern hampir selalu menempatkan tes logika pemrograman daring sebagai gerbang penyaringan awal.
- **Dampak Kritis:** kegagalan dalam menyelesaikan tantangan pemrograman dasar pada tahap seleksi awal ini akan langsung membatalkan kelanjutan kandidat ke babak wawancara teknis berikutnya, terlepas dari keahlian mereka dalam pemodelan kecerdasan buatan (_AI modeling_).

**Pembentukan Pola Pikir Terstruktur:**

- Melatih logika berpikir logis dan berurutan saat menyusun kode.
- Meningkatkan efisiensi pemilihan tipe data koleksi (seperti kapan harus menggunakan List vs Set atau Dictionary) berdasarkan kebutuhan kompleksitas algoritma.
- Membiasakan pengembang dengan pengujian kode secara otomatis melalui berbagai skenario kasus uji (_test cases_).

> [!tip] Audio Insight — Strategi Pemilihan Soal Berdasarkan Metrik Success Rate
> Dalam diskusi interaktif di kelas, dosen memberikan panduan taktis bagi siswa dalam menavigasi tumpukan tantangan di platform HackerRank:
> - **Memahami Metrik Success Rate:** setiap soal latihan menyertakan indikator tingkat keberhasilan, seperti `89%`. Persentase ini mengindikasikan tingkat kemudahan soal secara statistik — semakin mendekati 100%, semakin banyak pengembang yang berhasil menyelesaikan seluruh kasus uji dengan benar.
> - **Rekomendasi Alur Belajar:** siswa yang baru memulai disarankan untuk mengurutkan atau memilih soal yang memiliki _success rate_ tinggi terlebih dahulu untuk membiasakan diri dengan format pengumpulan kode, sebelum beralih secara bertahap ke soal dengan _success rate_ lebih rendah atau tingkat kesulitan _Medium_ dan _Hard_.

> [!tip] Audio Insight — Solusi Masalah Pendaftaran Akun ("For Developers" vs "For Employers")
> Selama pelaksanaan praktikum di kelas, terdapat laporan siswa yang mengalami kegagalan pendaftaran akibat kesalahan pemilihan jenis akun. Dosen meluruskan bahwa portal HackerRank membagi registrasi menjadi dua kategori besar: portal untuk industri/perekrut (_For Employers_) dan portal untuk pengembang/siswa (_For Developers_). Pendaftaran mandiri untuk latihan harus diselesaikan melalui opsi **"For Developers"** agar mendapatkan akses kurikulum belajar gratis tanpa batasan waktu trial.

---

## Ringkasan Sesi

Sesi 4 menuntaskan pembahasan tipe data koleksi Python: List (_mutable_, `.append`/`.insert`/`.extend`/`.pop`/`.remove`/`.copy`, list comprehension), Tuple (_immutable_, `.index`/`.count`, aturan koma _single item tuple_), Indexing & Slicing (`[start:stop:step]`, indeks negatif, perilaku _out-of-range_), Set (elemen unik, operasi himpunan union/intersection/difference/symmetric difference), dan Dictionary (_key-value_, `.get`/`.update`/`.setdefault`/`.items`). Sesi ini juga membuka pintu ke latihan mandiri di [[Sesi 06 - Hackerrank Exercise (JCAIEH M1)|Sesi 06 - Hackerrank Exercise]] dan menjadi fondasi konseptual langsung untuk struktur data relasional di [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] serta manipulasi data tabular di [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]].

---

## 🔗 Terkait

- [[Sesi 03 - Conditional and Loop Statement (JCAIEH M1)|Sesi 03 - Conditional and Loop Statement]] — Bab 1 di sini me-review ulang algoritma bilangan prima dan slicing `[::-1]` yang pertama kali muncul di Sesi 3.
- [[Sesi 06 - Hackerrank Exercise (JCAIEH M1)|Sesi 06 - Hackerrank Exercise]] — platform HackerRank yang diperkenalkan di Bab 8 di sini menjadi tempat praktik langsung soal-soal List/Set/Dict pada Sesi 6.
- [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] — List comprehension (Bab 3.3) dan struktur Dictionary (Bab 7) di sini adalah nenek moyang langsung dari operasi vektor NumPy dan pembuatan Series/DataFrame di Sesi 12.
