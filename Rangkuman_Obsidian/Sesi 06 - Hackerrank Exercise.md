---
tags: [module1, sesi-06, python, hackerrank, list, dictionary, sorting, lambda]
aliases: ["Sesi 6"]
---

# Session 6 — Hackerrank Exercise

Study guide ini merangkum pembahasan lima latihan pemrograman Python bergaya HackerRank yang dibahas di kelas: pemrosesan file invoice, Runner-Up Score, Nested List (skor terendah kedua), List Commands, dan Company Logo. Latihan-latihan ini melatih manipulasi *list*, *set*, dan *dictionary*, serta teknik *sorting* lanjutan dengan `lambda`.

> [!tip] Prasyarat
> Latihan-latihan di sesi ini menggabungkan konsep *function*, *file handling* ([[Sesi 05 - Python Function and File Handling]]), dan tipe data koleksi (*list*, *set*, *dictionary* — lihat [[Sesi 04 - Data Types Collection Notes]]).

---

## Bab 1 — Membaca dan Memproses File Invoice (Topik 1A)

Tujuan utama dari topik ini adalah mengekstrak data numerik dari sebuah file teks (`invoice.txt`) yang memiliki struktur data berulang dan menghitung total harga setelah diskon.

### A. Alur Logika Penyelesaian

1. **Membuka File:** Menggunakan fungsi `open()` untuk membaca file `invoice.txt`.
2. **Membaca Line per Line:** Menggunakan `.readlines()` untuk mengambil seluruh baris dalam file.
3. **Iterasi dengan Langkah (Step Looping):** Karena struktur file terdiri dari Nama, Quantity, dan Total, maka Looping dilakukan dengan melompat setiap 3 baris untuk menargetkan baris "Total".
4. **Ekstraksi Nilai (Parsing):**
    - **Metode Karakter:** Memeriksa setiap karakter apakah merupakan digit menggunakan `.isdigit()`.
    - **Metode Split (Direkomendasikan):** Memecah string baris "Total" menggunakan `.split()`. Nilai angka biasanya berada di indeks terakhir `[-1]`.
5. **Perhitungan:** Mengumpulkan semua angka ke dalam List, menjumlahkannya dengan `sum()`, dan mengalikan dengan faktor diskon (misalnya 10%).

### B. Kode Python (Manipulasi File)

```python
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

> [!tip] Lihat juga
> Ini adalah versi lanjutan dari Latihan 5 (`get_total`) di [[Sesi 05 - Python Function and File Handling]] — polanya identik: buka file dengan `with`, `.readlines()`, lompat 3 baris, `.split()`, ambil indeks `[-1]`.

---

## Bab 2 — Menemukan Runner-Up Score (Topik 1B)

Masalah ini melatih kemampuan dalam mengolah Array/List untuk menemukan nilai tertinggi kedua dari sekumpulan skor yang diberikan.

### A. Alur Logika dan Constraints

- **Constraints:**
    - Jumlah skor (N): 2 ≤ N ≤ 10.
    - Rentang skor: −100 hingga 100.
- **Logika Penyelesaian:**
    1. Menerima input N sebagai jumlah data.
    2. Menerima baris skor dan mengubahnya menjadi List of Integer menggunakan `map(int, input().split())`.
    3. **Menghapus Duplikat:** Mengubah List menjadi `set` agar nilai yang sama (seperti dua skor juara pertama) hanya terhitung satu kali.
    4. **Sorting:** Mengurutkan skor secara Ascending.
    5. **Akses Indeks:** Mengambil nilai pada indeks `[-2]` (elemen kedua dari belakang) yang merupakan Runner-Up.

### B. Kode Python (Runner-Up Score)

```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # Menghapus duplikat dengan set dan mengurutkan
    unique_scores = sorted(list(set(arr)))

    # Mencetak nilai tertinggi kedua
    print(unique_scores[-2])
```

**Contoh trace langkah-demi-langkah (ditambahkan sebagai pelengkap):**

```python
# Input: N=5, skor = [5, 3, 6, 6, 5]
arr = [5, 3, 6, 6, 5]
unique = set(arr)               # {5, 3, 6}  <- 6 dan 5 yang duplikat hanya dihitung sekali
unique_sorted = sorted(unique)  # [3, 5, 6]
print(unique_sorted[-2])        # Output: 5  <- runner-up yang benar

# Tanpa set() (SALAH):
arr_sorted_tanpa_set = sorted(arr)   # [3, 5, 5, 6, 6]
print(arr_sorted_tanpa_set[-2])       # Output: 6  <- SALAH! ini masih skor tertinggi (duplikat)
```

---

## Bab 3 — Nested List: Skor Terendah Kedua (Topik 2)

### 1. Deskripsi Tantangan (Problem Description)

Tantangan **Nested Lists** pada HackerRank dirancang untuk menguji pemahaman Anda dalam mengelola struktur data list di dalam list (sub-list). Tujuan utama dari latihan ini adalah:

- Menerima input berupa nama mahasiswa (string) dan nilai (float/integer) untuk sejumlah N mahasiswa.
- Menyimpan data tersebut ke dalam struktur data yang terorganisir.
- Mencari dan menampilkan nama mahasiswa yang memiliki **nilai terendah kedua** (*second lowest grade*).

**Visualisasi Struktur Data (Nested List):** Data akan disimpan dalam format seperti berikut:
`students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]`

**Aturan Penulisan Output:** Jika terdapat lebih dari satu mahasiswa yang memiliki nilai terendah kedua tersebut, nama-nama mereka harus diurutkan secara alfabetis sebelum dicetak ke layar.

### 2. Batasan Masalah (Constraints)

Dalam platform kompetitif seperti HackerRank, batasan masalah adalah **Test Case Guarantees**. Anda tidak perlu melakukan validasi manual (seperti blok `if-condition` tambahan) karena input dipastikan memenuhi kriteria berikut:

- **Jumlah mahasiswa (N):** Berkisar antara 2 hingga 5 mahasiswa.
- **Tipe Data:** Nama berupa string dan nilai berupa float atau integer.
- **Kepastian Solusi:** Dipastikan akan selalu ada satu atau lebih mahasiswa yang memiliki nilai terendah kedua (tidak semua mahasiswa memiliki nilai yang sama persis).

### 3. Daftar Fungsi dan Metode Python

| Fungsi/Metode | Deskripsi Singkat |
|---|---|
| `input()` | Meminta input dari pengguna melalui keyboard sebagai string. |
| `int()` / `float()` | Melakukan casting tipe data string ke angka bulat atau desimal. |
| `split()` | Memecah string menjadi list berdasarkan separator (default: spasi). |
| `append()` | Menambahkan elemen baru (termasuk sub-list) ke dalam list utama. |
| `set()` | Digunakan untuk mengisolasi nilai unik (menghapus duplikasi skor) agar nilai terendah kedua dapat diindeks dengan akurat. |
| `sorted()` | Mengurutkan elemen. Mengembalikan list baru dalam urutan menaik (*ascending*). |
| `items()` | Mengambil pasangan *key* (skor) dan *value* (list nama) dari dictionary untuk iterasi. |
| `lambda` | Fungsi anonim untuk kustomisasi logika pengurutan kompleks pada `sorted()`. |

### 4. Logika Penyelesaian Masalah (Problem Solving Logic)

#### 4.1 Pendekatan Nested List (List Comprehension)

1. **Inisialisasi:** Buat list kosong `students = []`.
2. **Input Loop:** Gunakan perulangan untuk memasukkan sub-list `[nama, nilai]` ke dalam list utama menggunakan `append()`.
3. **Ekstraksi Nilai:** Ambil semua skor saja dari list utama (bisa menggunakan *list comprehension*).
4. **Unique & Sort:** Gunakan `set()` pada list skor untuk membuang duplikasi, lalu urutkan dengan `sorted()`.
5. **Identifikasi Target:** Ambil skor pada indeks ke-1 dari list skor unik. Ini adalah nilai terendah kedua.
6. **Filtering:** Filter list `students` untuk mengambil nama mahasiswa yang memiliki skor tersebut, lalu diurutkan secara alfabetis.
7. **Output:** Cetak nama-nama hasil filter satu per satu.

**Implementasi kode pendekatan ini (ditambahkan — di sumber langkahnya dijelaskan tapi kodenya tidak ditulis eksplisit, hanya pendekatan Dictionary di bawah yang ada kodenya):**

```python
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Ekstraksi skor saja menggunakan list comprehension
    scores_only = [s[1] for s in students]

    # Unique & sort
    unique_scores = sorted(set(scores_only))
    second_lowest = unique_scores[1]

    # Filtering nama yang cocok, lalu sort alfabetis
    result_names = sorted([s[0] for s in students if s[1] == second_lowest])

    for name in result_names:
        print(name)
```

#### 4.2 Pendekatan Dictionary (**Highly Recommended**)

Pendekatan ini sangat disarankan untuk skenario data yang lebih besar karena memetakan satu skor ke banyak nama secara efisien.

1. **Struktur Data:** Gunakan dictionary dengan **Skor** sebagai *Key* dan **List Nama** sebagai *Value*.
2. **Pemetaan:** Saat iterasi input, cek apakah skor sudah ada di dictionary. Jika belum, buat entri baru; jika sudah ada, tambahkan nama ke dalam list value-nya.
3. **Sorting Keys:** Ambil semua *keys* (skor) dari dictionary, kemudian urutkan.
4. **Identifikasi Skor:** Pilih skor pada posisi indeks ke-1 (terendah kedua).
5. **Tie-breaker & Output:** Ambil list nama yang berasosiasi dengan skor tersebut. Urutkan list nama tersebut secara alfabetis (sebagai penangan jika ada lebih dari satu nama), lalu cetak.

### 5. Implementasi Kode Python (Nested List — Dictionary Approach)

```python
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

**Trace contoh (ditambahkan) menggunakan data di visualisasi 1. di atas:**

```python
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
unique_grades = sorted(set([37.21, 37.21, 37.2, 41.0, 39.0]))  # [37.2, 37.21, 39.0, 41.0]
second_lowest_grade = unique_grades[1]   # 37.21
result_names = sorted(['Harry', 'Berry'])  # ['Berry', 'Harry']
# Output:
# Berry
# Harry
```

### 6. Command Parsing — List Operations (terkait, dibahas lebih lengkap di Bab 4)

Program menerima sejumlah N perintah (seperti `insert`, `append`, `remove`, `pop`, `reverse`). Logika menggunakan `if-elif` untuk mengecek jenis perintah pada indeks `[0]` setelah string di-split. Lihat implementasi lengkap di [[#Bab 4 — Latihan HackerRank List Commands (Topik 3)|Bab 4]] sesi ini.

> [!warning] Audio Insight — Lazy Operator, Efisiensi Dictionary, Tuple Trick, dan Constraints
> **Lazy Operator:** Fungsi `map()` adalah *lazy operator*. Artinya, Python tidak langsung memproses pemetaan di memori sampai data tersebut benar-benar diminta (misalnya saat dikonversi menjadi `set` atau `list`). Ini sangat efisien untuk menangani dataset besar.
>
> **Efisiensi Dictionary:** Dictionary jauh lebih intuitif untuk memetakan hubungan *one-to-many* (satu skor milik banyak mahasiswa). Hal ini mencerminkan cara kerja pengindeksan data di dunia nyata.
>
> **Kustomisasi Sorting (The Tuple Trick):** Dalam kasus lebih kompleks seperti soal "Company Logo", kita sering menggunakan `lambda` untuk multi-kriteria sorting. Contoh: `sorted(data, key=lambda x: (-x[1], x[0]))`.
> - `-x[1]` (negatif) memaksa angka diurutkan secara **descending** (terbesar ke terkecil).
> - `x[0]` memastikan string diurutkan secara **ascending** (A ke Z).
> - Ini adalah teknik "Senior Instructor" untuk menangani dua aturan pengurutan dalam satu baris kode.
>
> **Pentingnya Constraints:** Ingatlah bahwa batasan di HackerRank adalah janji sistem. Anda tidak perlu membuang waktu menulis kode defensif (seperti `if N < 2`) jika sistem sudah menjamin bahwa N minimal bernilai 2. Fokuslah pada efisiensi logika inti.

> [!tip] Wawasan tambahan (dari bagian awal sesi)
> - **Lazy Operation pada Map:** Fungsi `map()` di Python bersifat "lazy". Artinya, proses konversi (misalnya menjadi integer) tidak langsung dilakukan sampai hasilnya dibutuhkan (seperti saat dikonversi menjadi `list` atau `set`).
> - **Keuntungan Menggunakan Set:** Dalam kasus mencari Runner-Up, penggunaan `set()` sangat krusial jika terdapat nilai tertinggi yang ganda. Tanpa `set()`, juara kedua mungkin tidak akan ditemukan jika juara pertama memiliki skor yang sama di beberapa entri.
> - **Efisiensi Split:** Menggunakan `.split()` jauh lebih efisien dan bersih daripada melakukan iterasi karakter per karakter untuk mencari angka di dalam sebuah kalimat string.
> - **Constraint di HackerRank:** Batasan (Constraints) yang tertulis di soal merupakan acuan bagi pemrogram bahwa input data tidak akan keluar dari rentang tersebut. Pemrogram tidak wajib membuat validasi manual menggunakan `if` untuk mengecek constraint tersebut kecuali diminta secara eksplisit.
> - **Lambda dalam Sorting:** Untuk sorting yang kompleks (misalnya mengurutkan berdasarkan kemunculan terbanyak sekaligus urutan alfabet), Python dapat menggunakan parameter `key` dengan `lambda` untuk menentukan prioritas pengurutan pada Dictionary.

---

## Bab 4 — Latihan HackerRank List Commands (Topik 3)

Dokumen ini menyajikan panduan komprehensif untuk menyelesaikan tantangan pemrograman Python pada platform HackerRank, khususnya Topik 3 mengenai **List Commands**. Panduan ini disusun berdasarkan diskusi teknis, alur logika penyelesaian masalah, dan wawasan instruksional guna memastikan pemahaman mendalam terhadap manipulasi objek list di Python.

### 1. Deskripsi Latihan

Tantangan ini mengharuskan pengembang untuk menginisialisasi sebuah list kosong dan melakukan serangkaian perintah manipulasi berdasarkan input yang diberikan. Terdapat N buah perintah yang harus diproses satu per satu, di mana setiap perintah merujuk pada metode bawaan (*built-in methods*) dari tipe data list di Python.

### 2. Daftar Fungsi dan Metode List

| Perintah | Deskripsi Fungsi | Contoh Input |
|---|---|---|
| `insert` | Memasukkan integer e pada indeks ke-i | `insert 0 5` |
| `print` | Mencetak seluruh isi list ke layar | `print` |
| `remove` | Menghapus kemunculan pertama dari elemen e | `remove 6` |
| `append` | Menambahkan elemen e ke akhir list | `append 10` |
| `sort` | Mengurutkan elemen di dalam list secara ascending | `sort` |
| `pop` | Menghapus elemen terakhir dari list | `pop` |
| `reverse` | Membalik urutan elemen di dalam list | `reverse` |

### 3. Constraints dan Format Input

- **Format Input:** Baris pertama berisi integer N yang menyatakan jumlah perintah. N baris berikutnya berisi perintah-perintah yang disebutkan dalam tabel di atas.
- **Batasan:** Perintah harus diproses secara berurutan sesuai urutan input.
- **Tipe Data:** Input yang diterima dari keyboard awalnya berupa string, sehingga diperlukan konversi tipe data (*casting*) untuk parameter angka.

### 4. Alur Logika Penyelesaian

1. **Inisialisasi:** Buat sebuah variabel list kosong (misalnya `numbers = []`).
2. **Input Jumlah Perintah:** Baca nilai N dan konversi menjadi integer menggunakan `int(input())`.
3. **Iterasi Perintah:** Lakukan perulangan (*loop*) sebanyak N kali.
4. **Parsing Input:**
    - Gunakan metode `.split()` pada input string untuk memecah perintah.
    - Secara default, `.split()` akan membagi string berdasarkan spasi.
    - Elemen pertama (indeks 0) dari hasil split adalah tipe perintah (`command type`).
5. **Logika Kondisional:**
    - Gunakan struktur `if-elif-else` untuk menentukan aksi berdasarkan `command type`.
    - Jika perintah membutuhkan parameter (seperti `insert`, `append`, atau `remove`), ambil elemen berikutnya dari hasil split dan lakukan *casting* ke integer.
6. **Eksekusi:** Panggil metode list yang sesuai pada variabel list yang telah diinisialisasi.

### 5. Implementasi Kode Python

```python
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

> [!warning] Audio Insight — Fleksibilitas .split(), Pentingnya Casting, dan Penanganan Error Indeks
> **Fleksibilitas .split():** Metode `.split()` tanpa parameter secara otomatis mendeteksi *white space* (spasi, tab, enter) sebagai pemisah. Hal ini sangat berguna untuk menangani input seperti `insert 0 5` yang memiliki panjang elemen berbeda dengan perintah `print`.
>
> **Pentingnya Casting:** Semua input yang diambil melalui fungsi `input()` di Python secara default bertipe string. Kegagalan melakukan *casting* ke `int()` saat menjalankan perintah `insert` atau `append` akan menyebabkan error atau perilaku program yang tidak diinginkan karena list akan menyimpan string, bukan angka.
>
> **Penanganan Error Indeks:** Saat melakukan parsing perintah seperti `parts[1]` atau `parts[2]`, pengembang harus memastikan bahwa elemen tersebut memang ada dalam hasil split untuk menghindari `IndexError: list index out of range`. Namun, dalam konteks HackerRank, input biasanya dijamin sesuai dengan format yang dijanjikan.
>
> **Lazy Operation:** Memahami konsep operasional di Python sangat penting. Contohnya, fungsi `map()` bersifat *lazy operation*, artinya fungsi tersebut tidak akan dieksekusi sampai hasilnya benar-benar dibutuhkan oleh fungsi lain (seperti saat dikonversi menjadi `list` atau `set`).
>
> **Manipulasi Dictionaries:** Meskipun Topik 3 fokus pada List, penggunaan Dictionary juga dibahas sebagai alternatif efektif jika masalah melibatkan pemetaan kunci dan nilai (misalnya skor dan nama mahasiswa), di mana kunci dapat diurutkan secara independen dari nilainya.

**Contoh casting yang gagal (ditambahkan sebagai ilustrasi bahaya):**

```python
numbers_salah = []
parts = "append 10".split()
# Tanpa casting:
numbers_salah.append(parts[1])   # parts[1] masih string "10"
print(numbers_salah)              # Output: ['10']  <- string, bukan angka!
print(numbers_salah[0] + 1)       # -> TypeError: can only concatenate str (not "int") to str

# Dengan casting (BENAR):
numbers_benar = []
numbers_benar.append(int(parts[1]))
print(numbers_benar)              # Output: [10]
print(numbers_benar[0] + 1)       # Output: 11
```

---

## Bab 5 — Latihan HackerRank Company Logo (Topik 4)

Study Guide ini disusun untuk membantu memahami logika penyelesaian masalah pemrograman Python melalui platform HackerRank, khususnya pada tantangan _Company Logo_. Dokumen ini merangkum diskusi teknis mengenai penggunaan tipe data Dictionary, fungsi Lambda untuk sorting kustom, serta penanganan batasan (constraints) dalam kode.

### 1. Logika Penyelesaian Masalah: Company Logo

Masalah utama dalam _Company Logo_ adalah menghitung frekuensi kemunculan setiap karakter dalam sebuah String dan menampilkan tiga karakter yang paling sering muncul. Jika jumlah kemunculan sama, maka karakter diurutkan berdasarkan urutan alfabet (alphabetical order).

#### 1.1 Pendekatan Dictionary

Dictionary digunakan sebagai instrumen penghitung (*counter*) karena efisiensinya dalam memetakan kunci (Key) ke nilai (Value).

- **Key:** Menyimpan karakter unik dari String (huruf).
- **Value:** Menyimpan jumlah kemunculan karakter tersebut (integer).
- **Proses:** Lakukan Loop pada setiap karakter dalam String. Jika karakter belum ada dalam Dictionary, inisialisasi dengan nilai 1. Jika sudah ada, lakukan increment pada Value-nya.

#### 1.2 Pendekatan Fungsi Lambda untuk Sorting

Fungsi Lambda sangat krusial dalam metode `sorted()` untuk menangani dua kriteria pengurutan sekaligus:

1. **Prioritas 1 (Occurrence Count):** Diurutkan secara Descending (besar ke kecil). Dalam kode, ini diwakili dengan tanda negatif (`-`) pada Value.
2. **Prioritas 2 (Alphabetical):** Jika frekuensi sama, diurutkan secara Ascending (A-Z). Dalam kode, ini diwakili dengan nilai positif pada Key.

### 2. Constraints (Batasan Masalah)

- **Panjang String S:** Minimal 3 karakter dan maksimal 10⁴ karakter (3 ≤ len(S) ≤ 10⁴).
- **Karakter Unik:** String dijamin memiliki setidaknya 3 karakter yang berbeda.
- **Format Huruf:** String biasanya berisi *lowercase letters* (huruf kecil).
- **Output:** Hanya menampilkan **top three** (tiga besar) karakter yang paling sering muncul beserta jumlah kemunculannya.

### 3. Daftar Fungsi dan Metode Python

| Fungsi / Metode | Kegunaan |
|---|---|
| `.split()` | Memecah String menjadi List berdasarkan separator (default-nya adalah *white space*). |
| `set()` | Mengubah List menjadi Set untuk menghapus nilai duplikat (menghasilkan nilai unik). |
| `sorted()` | Mengurutkan elemen dalam *iterable* (seperti List atau Dictionary Items). |
| `.items()` | Mengembalikan pasangan Key dan Value dari Dictionary untuk keperluan iterasi atau sorting. |
| `lambda` | Fungsi anonim untuk mendefinisikan logika sorting kustom dalam satu baris. |
| `.append()` | Menambahkan elemen baru ke posisi terakhir dalam sebuah List. |
| `int()` | Melakukan casting atau konversi tipe data String/Float menjadi Integer. |
| `input()` | Mengambil input dari pengguna melalui keyboard. |

### 4. Implementasi Kode Python

#### 4.1 Solusi Company Logo (Dictionary & Lambda)

```python
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

**Trace contoh (ditambahkan):**

```python
s = "aabbbccde"
# letter_counter setelah loop: {'a': 2, 'b': 3, 'c': 2, 'd': 1, 'e': 1}
# result setelah sorted(key=lambda x: (-x[1], x[0])):
#   [('b', 3), ('a', 2), ('c', 2), ('d', 1), ('e', 1)]
#   -> 'b' menang karena jumlah terbanyak (3)
#   -> 'a' dan 'c' sama-sama 2, tapi 'a' menang karena alfabet lebih dulu
# Output:
# b 3
# a 2
# c 2
```

#### 4.2 Logika Runner-Up Score (Set & Sorted) — versi ringkas

```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # Menghapus duplikat dengan set, lalu di-sort
    unique_scores = sorted(set(arr))

    # Mengambil skor tertinggi kedua (index -2)
    print(unique_scores[-2])
```

> [!warning] Audio Insight — HackerRank untuk Technical Test, Lazy Operator, dan Handling Constraints
> **Pentingnya HackerRank:** Platform ini sering digunakan untuk *Technical Test* pada peran IT seperti Software Engineer, AI Engineer, dan Data Scientist. Memahami logika di sini membantu mempersiapkan diri untuk tes masuk kerja.
>
> **Lazy Operator pada fungsi map():** Fungsi `map()` bersifat *lazy*. Artinya, proses konversi (seperti mengubah String ke Integer) tidak langsung dijalankan sampai hasilnya benar-benar dibutuhkan (misalnya saat diubah menjadi List atau Set).
>
> **Dictionary vs List:** Untuk kasus pencarian frekuensi karakter, Dictionary jauh lebih intuitif dan efisien dibandingkan Nested List karena kita bisa langsung mengakses Key (karakter) untuk melakukan *update* nilai kemunculannya.
>
> **Handling Constraints:** Di HackerRank, batasan (constraints) adalah acuan untuk test case. Programmer tidak perlu membuat pengecekan `if` manual untuk memvalidasi apakah input sudah sesuai batasan, karena sistem dijamin memberikan input yang masuk dalam rentang batasan tersebut.
>
> **Logika Slicing dan Sorting:** Penggunaan indeks negatif (seperti `[-2]`) adalah cara cepat di Python untuk mengakses elemen dari urutan paling belakang tanpa perlu menghitung panjang List secara manual.

> [!tip] Lihat juga
> Teknik `lambda x: (-x[1], x[0])` di atas dibangun di atas dasar `lambda` yang dijelaskan di [[Sesi 05 - Python Function and File Handling]] Bab 1.6 — kalau masih ragu dengan sintaks `lambda parameter: expression`, kembali ke sana dulu sebelum mendalami *multi-criteria sorting* ini.
