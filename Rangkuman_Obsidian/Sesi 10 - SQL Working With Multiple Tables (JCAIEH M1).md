---
tags: [jcaieh/module1, sesi-10, sql, relational-model, primary-key, foreign-key, join, inner-join, left-join, right-join, full-join, self-join, cartesian-product, python-mysql-connector, sakila, jcaieh/module1/sesi10]
bootcamp: JCAIEH
module: 1
session: 10
aliases: ["Sesi 10", "SQL Working With Multiple Tables"]
---

# Session 10 — SQL Working With Multiple Tables

This session builds directly on [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] — everything here assumes you already understand `SELECT`, `WHERE`, `GROUP BY`, and basic DBMS terminology from Session 9. The new territory is connecting *more than one table together*.

## Bab 1 Relational Model Constraints (Batasan Model Relasional)

### 1.1 Pengantar Batasan Data dalam Bisnis dan Konsep Referencing

#### A. Fondasi Konseptual Batasan Data

- Dalam sistem bisnis, setiap data yang disimpan di dalam database relasional harus mematuhi batasan (_restrictions_) atau aturan (_rules_) tertentu yang berlaku di dunia nyata.
- Batasan ini berfungsi untuk menjaga integritas, akurasi, dan konsistensi data yang dikelola oleh sistem informasi perusahaan.

> [!tip] Audio Insight — Fondasi untuk skenario multi-tabel
> - Dosen menerangkan bahwa batasan model relasional (_Relational Model Constraints_) merupakan aturan mutlak yang menjamin keandalan data. Ketika sistem beralih dari satu tabel ke skenario multi-tabel (_multiple tables_), batasan relasi ini menjadi fondasi utama agar tidak terjadi ketidaksinkronan data antar-tabel.

#### B. Konsep Referencing

- _Referencing_ adalah konsep di mana suatu entitas dalam tabel relasional merujuk atau mengacu pada entitas di tabel lain untuk melengkapi informasi yang dibutuhkan.
- Contoh hubungan dunia nyata antara _Actress_ (Aktris) dan _Movie_ (Film):
    - Aturan bisnis menyatakan minimal satu aktris bermain dalam satu film (hubungan _One-to-One_).
    - Untuk mencari rincian informasi aktris, entitas _Movie_ akan merujuk (_refer_) ke entitas _Actress_.
    - Sebaliknya, untuk melacak film yang dibintangi aktris tersebut, entitas _Actress_ merujuk ke entitas _Movie_.

> [!tip] Audio Insight — Contoh Odyssey dan Matt Damon
> - Dosen mencontohkan secara konkret menggunakan film "Odyssey" dengan aktor utama "Matt Damon". Informasi film tersebut tercatat dalam tabel `movie`, namun rincian data diri Matt Damon seperti kewarganegaraan atau nilai aset bersih (_network_) disimpan di tabel aktor (`actress`/`actor`).
> - Jika pengguna ingin mengetahui "berapa network value dari aktor utama film Odyssey", informasi tersebut tidak dapat diperoleh hanya dari satu tabel. Sistem harus melakukan pencarian silang melalui hubungan rujukan (_referencing_) dengan menghubungkan tabel `movie` dan tabel `actress`.

Ini adalah contoh SQL yang mengilustrasikan referencing di atas (mengasumsikan skema `movie(movie_id, title, lead_actor_id)` dan `actor(actor_id, name, net_worth)`):

```sql
SELECT movie.title, actor.name, actor.net_worth
FROM movie
JOIN actor ON movie.lead_actor_id = actor.actor_id
WHERE movie.title = 'Odyssey';
```

---

### 1.2 Primary Key dan Foreign Key

#### A. Karakteristik Primary Key dan Foreign Key

- Untuk menghubungkan beberapa tabel, setiap tabel harus memiliki kunci pengidentifikasi yang jelas dan terstandarisasi.

|Karakteristik|Primary Key|Foreign Key|
|:--|:--|:--|
|**Definisi**|Kolom atau sekumpulan kolom yang secara unik mengidentifikasi setiap rekor/baris dalam sebuah tabel.|Kolom atau kumpulan kolom dalam suatu tabel yang merujuk pada _Primary Key_ di tabel lain.|
|**Keunikan Nilai**|Harus bernilai unik (_UNIQUE_); dilarang keras ada duplikasi nilai dalam satu tabel.|Nilainya tidak harus unik di tabel tempatnya berada; dapat menerima nilai yang berulang.|
|**Nilai Kosong**|Tidak boleh mengandung nilai kosong (_cannot contain NULL values_).|Secara umum dapat menerima nilai NULL jika aturan bisnis memperbolehkannya.|
|**Tujuan/Fungsi**|Mengidentifikasi baris data secara unik di tabel asal.|Menghubungkan atau mengaitkan (_link_) dua tabel secara logis.|

> [!tip] Audio Insight — Contoh identifier dunia nyata: NIK dan Plat Nomor
> - Dosen memaparkan beberapa contoh pengidentifikasi unik (_identifier_) di dunia nyata yang bertindak sebagai _Primary Key_:
>     - **Nomor Induk Kependudukan (NIK)**: Dalam database kependudukan Indonesia, NIK wajib bersifat unik dan tidak boleh kosong (_cannot contain NULL values_) karena mengidentifikasi setiap individu secara tunggal. Seseorang tidak boleh memiliki dua NIK, dan dua orang tidak boleh memiliki NIK yang sama.
>     - **Nomor Polisi (Plat Kendaraan)**: Dalam database kepolisian atau Samsat, nomor polisi berfungsi sebagai _Primary Key_ yang mengidentifikasi setiap unit kendaraan secara unik.
> - Untuk menjelaskan konsep _Foreign Key_, dosen menggunakan studi kasus relasi antara Penduduk dan Kendaraan:
>     - Tabel `penduduk` memiliki _Primary Key_ berupa `NIK`.
>     - Tabel `kendaraan` memiliki _Primary Key_ berupa `plat_nomor`.
>     - Karena setiap kendaraan dimiliki oleh seorang penduduk, kolom `NIK` dimasukkan ke dalam tabel `kendaraan` sebagai kolom pemilik kendaraan. Di dalam tabel `kendaraan`, kolom `NIK` ini bertindak sebagai _Foreign Key_ yang merujuk ke _Primary Key_ `NIK` di tabel `penduduk`. Hubungan ini mendefinisikan relasi kata kerja kepemilikan (_memiliki_ atau _dimiliki_).

Contoh SQL mendefinisikan Primary Key dan Foreign Key secara eksplisit (mengembangkan konsep `CREATE TABLE` dari [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]]):

```sql
CREATE TABLE penduduk (
    NIK VARCHAR(16) PRIMARY KEY,
    nama VARCHAR(100)
);

CREATE TABLE kendaraan (
    plat_nomor VARCHAR(10) PRIMARY KEY,
    NIK VARCHAR(16),
    FOREIGN KEY (NIK) REFERENCES penduduk(NIK)
);
```

---

### 1.3 Representasi ERD (Entity Relationship Diagram) dalam Model Data Relasional

#### A. Komponen Utama ERD

- _Entity Relationship Diagram_ (ERD) digunakan untuk menggambarkan skema database relasional secara visual.
- Dua komponen mendasar dari ERD adalah:
    - **Entity (Entitas)**: Representasi dari objek atau benda di dunia nyata yang ingin disimpan datanya (contoh: `departments`, `employees`). Entitas yang valid harus memiliki _Primary Key_ sendiri agar setiap baris datanya dapat diidentifikasi secara unik.
    - **Relation (Relasi)**: Hubungan antar-entitas yang divisualisasikan dengan garis penghubung, atau didefinisikan melalui tabel relasi perantara (_bridge/composite tables_).

#### B. Jenis-Jenis Hubungan (Relationship)

- **One-to-One (Satu-ke-Satu)**: Hubungan di mana satu baris pada tabel pertama berpasangan dengan tepat satu baris pada tabel kedua (misalnya hubungan minimal aktris dan film).
- **One-to-Many (Satu-ke-Banyak)**: Hubungan di mana satu rekor di tabel induk berhubungan dengan banyak rekor di tabel dependen (contoh: satu karyawan dapat memiliki beberapa catatan riwayat gaji pada tabel `salaries`).
- **Many-to-Many (Banyak-ke-Banyak)**: Hubungan di mana banyak rekor di tabel pertama berhubungan dengan banyak rekor di tabel kedua (contoh: departemen memiliki banyak karyawan, dan karyawan dapat bekerja di beberapa departemen). Hubungan ini wajib dipecah menjadi tabel perantara (_bridge table_).

#### C. Composite Primary Key (Kunci Utama Komposit)

- _Composite Primary Key_ merupakan _Primary Key_ yang dibentuk dari kombinasi dua atau lebih kolom di dalam satu tabel demi menjamin keunikan rekor. Hal ini umum diterapkan pada tabel transaksi atau tabel riwayat (_history_).

Contoh SQL Composite Primary Key:

```sql
CREATE TABLE salaries (
    employee_number INT,
    from_date DATE,
    salary DECIMAL(10,2),
    PRIMARY KEY (employee_number, from_date)
);
```

> [!warning] Audio Insight — Koreksi konseptual ERD: employee_number saja tidak cukup unik
> - Dosen mengoreksi ketidakakuratan konseptual dalam diagram ERD contoh yang ada pada slide modul:
>     - Pada diagram slide, tabel `salaries` dan `titles` digambarkan hanya menggunakan `employee_number` as _Primary Key_.
>     - Dosen menjelaskan bahwa rancangan ini salah secara konseptual karena dalam tabel riwayat, `employee_number` pasti akan berulang (duplikat) seiring bertambahnya riwayat gaji bulanan atau perubahan jabatan karyawan bersangkutan.
>     - Solusi yang tepat adalah menerapkan _Composite Primary Key_. Untuk tabel `salaries`, keunikan baris harus dijamin dengan menggabungkan kolom `employee_number` dan kolom tanggal mulai `from_date`. Dengan kombinasi ini, database dapat melacak perubahan riwayat tanpa melanggar batasan keunikan kunci.

---

### 1.4 Terminologi Tabel Relasional: Parent Table dan Dependent Table

#### A. Peran Tabel dalam Relasi

- **Parent Table (Tabel Induk)**: Tabel yang menampung _Primary Key_ yang dirujuk oleh tabel lain. Tabel ini bersifat independen dan menyediakan data acuan.
- **Dependent Table (Tabel Dependen)**: Tabel yang menampung satu atau beberapa _Foreign Key_ yang merujuk pada tabel induk. Tabel ini bergantung pada eksistensi data yang ada di tabel induk.

|Karakteristik|Parent Table|Dependent Table|
|:--|:--|:--|
|**Kepemilikan Kunci**|Menyimpan _Primary Key_ utama yang menjadi target rujukan.|Menyimpan _Foreign Key_ yang merujuk ke tabel lain.|
|**Ketergantungan Data**|Independen; data dapat dimasukkan tanpa bergantung pada tabel lain.|Dependen; data _Foreign Key_ yang dimasukkan wajib eksis di tabel induk.|
|**Contoh Kasus**|`employees` (tabel karyawan) dan `departments` (tabel departemen).|`dept_emp` atau `dept_manager` (tabel relasi penugasan departemen yang menampung referensi ID karyawan dan ID departemen).|

---

## Bab 2 Implicit JOIN (JOIN Implisit)

### 2.1 Karakteristik dan Sintaksis Dasar Implicit JOIN

#### A. Fondasi Konseptual Implicit JOIN

- _Implicit JOIN_ adalah metode penggabungan tabel dalam SQL tanpa menggunakan kata kunci `JOIN` secara eksplisit.
- Penggabungan ini dilakukan dengan menentukan dua atau lebih tabel secara langsung di dalam klausul `FROM` dengan memisahkannya menggunakan tanda koma (`,`).

|Karakteristik|Deskripsi|
|:--|:--|
|**Pemisah Tabel**|Menggunakan tanda koma (`,`) di klausul `FROM` untuk mendaftarkan tabel yang ingin digabungkan.|
|**Sintaksis Dasar**|Menghubungkan tabel secara implisit melalui klausul `WHERE`.|
|**Keterbacaan**|Sederhana untuk penggabungan dua tabel berskala kecil, namun rentan menimbulkan kesalahan jika jumlah tabel bertambah banyak.|

Contoh sintaksis dasar penggabungan implisit tanpa kriteria pembatas:

```sql
SELECT * FROM employees, salaries;
```

> [!tip] Audio Insight — Dari satu tabel ke banyak tabel
> - Dosen menerangkan bahwa dalam penulisan query standar satu tabel, pengguna umumnya menuliskan klausul `FROM` diikuti oleh satu nama tabel saja (contoh: `SELECT * FROM nama_tabel`).
> - Pada skenario multi-tabel menggunakan _Implicit JOIN_, database dipaksa untuk memproses beberapa tabel sekaligus hanya dengan menambahkan tanda koma di dalam klausul `FROM`.

---

### 2.2 Cartesian Join / Full Join (Cartesian Product)

#### A. Konsep Cartesian Product

- Jika penggabungan tabel secara implisit dilakukan tanpa menentukan kondisi pembatas atau kriteria pencocokan baris di klausul `WHERE`, sistem akan menghasilkan _Cartesian Join_ atau _Full Join_ (dikenal juga sebagai _Cartesian Product_).
- Dalam kondisi ini, setiap baris data di tabel pertama akan digabungkan secara paksa dengan setiap baris data di tabel kedua.
- Hal ini menyebabkan pelipatgandaan jumlah baris secara ekstrem di mana total baris hasil akhir merupakan hasil perkalian dari jumlah baris tabel pertama dengan jumlah baris tabel kedua.
- Hasil akhir dari _Cartesian Product_ ini tidak valid secara logis karena menghubungkan baris-baris data yang sebenarnya tidak memiliki hubungan relasional asli di dunia nyata.

> [!warning] Audio Insight — Bahaya nyata Cartesian Product (599 × 16.044 baris)
> - Dosen menjelaskan bahaya dan ketidakakuratan logika dari _Cartesian Product_ dengan memberikan contoh konkret menggunakan database sampel "Sakila":
>     - Tabel pelanggan (`customer`) memiliki total 599 baris data.
>     - Tabel pembayaran (`payment`) memiliki total 16.044 baris data.
>     - Jika query dijalankan dengan penggabungan implisit tanpa filter kriteria (`SELECT * FROM customer, payment;`), maka jumlah baris yang dihasilkan adalah perkalian ekstrem: 599 × 16.044, yang menghasilkan sekitar 9,6 juta baris data.
>     - Eksekusi ini menghasilkan data sampah yang tidak berguna karena terdapat 598 kombinasi baris yang tidak berhubungan logis untuk setiap satu transaksi pembayaran yang ada.
> - Dosen memaparkan contoh kasus kesalahan logika lainnya menggunakan tabel kota (`city`) dan tabel negara (`country`):
>     - Ketika query dituliskan sebagai `SELECT * FROM city, country;` kemudian pengguna memfilter kota tertentu seperti Abu Dhabi menggunakan klausul `WHERE city = 'Abu Dhabi'`, baris kota Abu Dhabi tersebut akan dipetakan (_mapping_) secara salah ke seluruh baris negara yang terdaftar di database (seperti Afghanistan, Algeria, American Samoa, Angola, dan lain-lain).
>     - Secara realitas dunia nyata, pemetaan ini salah fatal karena kota Abu Dhabi hanya boleh berpasangan dengan satu negara saja, yaitu United Arab Emirates (UAE).

Contoh yang menunjukkan bahaya di atas secara langsung (jangan dijalankan pada tabel besar tanpa `LIMIT`):

```sql
-- BAHAYA: tanpa WHERE, hasil = jumlah_baris(customer) x jumlah_baris(payment)
-- yaitu 599 x 16.044 = sekitar 9,6 juta baris "sampah"
SELECT * FROM customer, payment;
```

---

### 2.3 Membatasi Hasil Cartesian Join Menggunakan Klausul WHERE

#### A. Penerapan Kondisi Key Join

- Untuk mereduksi hasil _Cartesian Product_ dan mengembalikan data yang benar-benar berelasi logis, pengguna wajib menyertakan kondisi filter pencocokan kunci (_matching keys_ / _key join_) di dalam klausul `WHERE`.
- Operator perbandingan (`=`) digunakan untuk memastikan bahwa nilai kunci pengenal pada tabel pertama memiliki nilai yang sama persis dengan kunci rujukan pada tabel kedua.

Contoh sintaksis pembatasan hasil menggunakan klausul `WHERE`:

```sql
SELECT * FROM employees, salaries WHERE employees.emp_no = salaries.emp_no;
```

> [!tip] Audio Insight — Menyusutkan 9,6 juta baris kembali menjadi 16.044
> - Dosen menerangkan bahwa dengan menambahkan kondisi kesamaan kunci (`WHERE payment.customer_id = customer.customer_id`), hasil query pada tabel pelanggan dan pembayaran akan disaring secara tepat.
> - Hasil pencarian menyusut dari 9,6 juta baris menjadi hanya 16.044 baris sesuai dengan jumlah riwayat pembayaran riil yang ada, karena sistem hanya menampilkan transaksi yang dicatat atas nama pelanggan yang bersangkutan.
> - Pada contoh kasus kota Abu Dhabi, dosen mempraktikkan perbaikan query dengan menyertakan kolom penghubung `country_id` sebagai _key join_:

```sql
SELECT * FROM city, country WHERE city.country_id = country.country_id AND city = 'Abu Dhabi';
```

> - Penambahan kondisi ini membuat query hanya mengembalikan satu baris data yang valid secara akurat, yaitu kota Abu Dhabi berpasangan dengan negara United Arab Emirates.
> - Dosen menekankan bahwa pengguna wajib memahami struktur database terlebih dahulu sebelum menentukan kolom yang bertindak sebagai _key join_:
>     - Penggabungan tabel `customer` dan `payment` harus menggunakan kolom `customer_id` (kolom `payment_id` tidak dapat digunakan karena tidak tersedia pada tabel `customer`).
>     - Penggabungan tabel `address` dan `city` dihubungkan menggunakan kolom `city_id`.

---

### 2.4 Penggunaan Alias Tabel (Table Aliases)

#### A. Penyederhanaan Kode SQL

- Menuliskan nama tabel secara lengkap secara berulang kali di dalam klausul `SELECT` maupun `WHERE` dapat membuat query menjadi terlalu panjang, rumit, dan rentan terhadap kesalahan penulisan (_typo_).
- SQL menyediakan fitur untuk mendefinisikan alias tabel yang lebih pendek (_shorter aliases_) dengan memberikan label satu huruf atau singkatan pendek di dalam klausul `FROM`.
- Label alias ini diletakkan langsung setelah nama tabel (penggunaan kata kunci `AS` bersifat opsional).
- Setelah alias didefinisikan, seluruh referensi kolom dari tabel tersebut di klausul `SELECT` dan `WHERE` harus menggunakan alias yang telah ditetapkan.

Contoh sintaksis penggunaan alias tabel:

```sql
SELECT * FROM employees E, salaries S WHERE E.emp_no = S.emp_no;
```

> [!tip] Audio Insight — Alias mempermudah penulisan kondisi WHERE
> - Dosen menerangkan bahwa penamaan alias tabel seperti `customer C` atau `payment P` sangat mempermudah efisiensi penulisan kode.
> - Dengan alias tersebut, ekspresi pencocokan kunci pada klausul `WHERE` yang semula panjang cukup ditulis dengan singkat: `WHERE C.customer_id = P.customer_id`.

---

### 2.5 Pemilihan Kolom Spesifik

#### A. Efisiensi Pengambilan Data

- Penggunaan tanda bintang (`*`) sangat tidak disarankan dalam penulisan query multi-tabel karena akan menarik seluruh kolom dari semua tabel secara bersamaan, sehingga membebani memori dan kinerja jaringan database.
- Praktik terbaik (_best practices_) adalah melakukan pemilihan kolom secara spesifik (_specific columns_) di klausul `SELECT`.
- Nama kolom yang dipilih harus diawali dengan alias tabel atau nama tabel asal (dengan format `alias.nama_kolom`) untuk menghindari ambiguitas atau konflik ketika terdapat kolom dengan nama yang sama di antara tabel-tabel yang digabungkan.

Contoh sintaksis pemilihan kolom spesifik menggunakan alias:

```sql
SELECT E.first_name, E.last_name, S.salary FROM employees E, salaries S WHERE E.emp_no = S.emp_no;
```

> [!tip] Audio Insight — Query terarah untuk transaksi pelanggan
> - Dosen mencontohkan query terarah untuk menampilkan informasi transaksi pelanggan dengan hanya mengambil kolom nama depan (`first_name`), nama belakang (`last_name`), nilai transaksi (`amount`), dan tanggal pembayaran (`payment_date`):

```sql
SELECT C.first_name, C.last_name, P.amount, P.payment_date
FROM customer C, payment P
WHERE C.customer_id = P.customer_id;
```

> - Hasil dari query tersebut menyajikan data gabungan secara bersih dan teratur yang diurutkan secara otomatis berdasarkan tanggal transaksi pembayaran (`payment_date`) dari yang terawal.

---

## Bab 3 Explicit JOIN dan JOIN Statement (JOIN Eksplisit)

### 3.1 Pengenalan Explicit JOIN dan Perbedaannya dengan Implicit JOIN

#### A. Definisi dan Konsep Dasar

- _Explicit JOIN_ (atau biasa disebut _JOIN Statement_) adalah mekanisme penggabungan baris dari dua atau lebih tabel secara eksplisit menggunakan kata kunci (_keyword_) `JOIN` dan klausul pengait `ON` untuk mendefinisikan hubungan antar-kolom (_key join_).
- Berbeda dengan _Implicit JOIN_ yang menggabungkan tabel menggunakan tanda koma (`,`) pada klausul `FROM` dan menyaringnya di klausul `WHERE`, _Explicit JOIN_ memisahkan logika penggabungan tabel (_join logic_) secara terpisah dari logika pemfilteran data (_filter logic_).

|Karakteristik|Implicit JOIN|Explicit JOIN|
|:--|:--|:--|
|**Sintaksis Penggabungan**|Menggunakan tanda koma (`,`) pada klausul `FROM`.|Menggunakan keyword `JOIN` secara eksplisit antar-tabel.|
|**Penyelarasan Kolom Kunci (_Key Join_)**|Ditulis pada klausul `WHERE` bersama dengan filter baris biasa.|Ditulis secara khusus pada klausul `ON` setelah keyword `JOIN`.|
|**Keterbacaan (_Readability_)**|Sulit dibaca pada query kompleks karena logika join bercampur dengan filter data.|Jauh lebih terstruktur, rapi, dan mudah dipelihara (_maintainable_) seiring kompleksitas query bertambah.|

> [!tip] Audio Insight — Explicit JOIN direkomendasikan secara profesional
> - Dosen menekankan bahwa penggunaan _Explicit JOIN_ sangat direkomendasikan dalam praktik database profesional karena pemisahan yang jelas antara kolom kunci relasi (`ON`) dan kondisi filter data (`WHERE`).
> - Ketika menulis kode, dosen juga menyarankan untuk membiasakan memberikan indentasi (seperti memberikan karakter tab atau baris baru di bawah klausul `SELECT`, `FROM`, `JOIN`, dan `ON`) agar query SQL lebih mudah dibaca dan dievaluasi oleh tim pengembang lain.

Perbandingan langsung Implicit vs Explicit JOIN untuk kueri yang menghasilkan output identik:

```sql
-- Implicit JOIN
SELECT E.first_name, S.salary
FROM employees E, salaries S
WHERE E.emp_no = S.emp_no;

-- Explicit JOIN (setara persis, tapi lebih terstruktur)
SELECT E.first_name, S.salary
FROM employees E
JOIN salaries S
  ON E.emp_no = S.emp_no;
```

---

### 3.2 Jenis-Jenis Explicit JOIN: INNER JOIN, LEFT JOIN, dan RIGHT JOIN

#### A. INNER JOIN (atau JOIN)

- Kata kunci `INNER JOIN` digunakan untuk mengambil baris-baris data yang memiliki nilai kecocokan (_matching values_) di kedua tabel yang dihubungkan.
- Jika suatu baris di tabel pertama tidak memiliki pasangan nilai yang cocok di tabel kedua, atau sebaliknya, maka baris data tersebut tidak akan ditampilkan dalam hasil query.

Sintaks Dasar:

```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

- Catatan Penulisan: Di dalam MySQL dan mayoritas sistem database relasional, menuliskan keyword `JOIN` saja tanpa kata `INNER` secara otomatis diartikan sebagai `INNER JOIN`.

> [!tip] Audio Insight — Aturan PK/FK sebagai penghubung, dan studi kasus 3-tabel Sakila
> - **Aturan Kolom Penghubung**: Menanggapi pertanyaan mahasiswa mengenai apakah kolom yang digunakan sebagai penghubung (_link_) harus selalu berupa _Primary Key_ di satu tabel dan _Foreign Key_ di tabel lainnya, dosen membenarkan hal tersebut. Secara konseptual, relasi antar-tabel dibangun dengan menghubungkan kunci utama (_Primary Key_) dari satu entitas ke kunci asing (_Foreign Key_) di entitas yang bergantung padanya agar integritas data terjaga.
> - **Studi Kasus Multi-Tabel (3 Tabel)**: Dosen mendemonstrasikan penggabungan tiga tabel sekaligus dalam database _Sakila_ untuk melacak film yang sedang disewa.
>     - Tabel `film` (alias `FM`) dihubungkan ke tabel jembatan `inventory` menggunakan kolom `film_id`.
>     - Tabel `inventory` kemudian dihubungkan ke tabel `rental` menggunakan kolom `inventory_id`.
>     - Proses pencarian ini hanya bisa dilakukan secara bertahap melalui relasi kunci yang berantai ini.

Contoh SQL untuk studi kasus 3-tabel di atas (melacak film mana yang sedang disewa):

```sql
SELECT FM.title, I.inventory_id, R.rental_date, R.return_date
FROM film FM
INNER JOIN inventory I ON FM.film_id = I.film_id
INNER JOIN rental R ON I.inventory_id = R.inventory_id
WHERE R.return_date IS NULL;   -- return_date NULL berarti masih dipinjam
```

#### B. LEFT (OUTER) JOIN

- Kata kunci `LEFT JOIN` (atau disebut `LEFT OUTER JOIN` di beberapa database) mengembalikan seluruh baris dari tabel sebelah kiri (tabel pertama/utama), beserta baris yang memiliki nilai cocok dari tabel sebelah kanan (tabel kedua).
- Jika tidak ada kecocokan baris di tabel sebelah kanan, maka kolom-kolom dari tabel sebelah kanan tersebut akan diisi dengan nilai kosong atau `NULL`.

Sintaks Dasar:

```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

> [!tip] Audio Insight — LEFT JOIN untuk mendeteksi data yang tidak berpasangan
> - **Deteksi Data Tidak Berpasangan**: Dosen menjelaskan bahwa kegunaan utama dari `LEFT JOIN` adalah untuk mengidentifikasi data yang tidak memiliki pasangan relasi.
> - Sebagai contoh, kita dapat menggunakan `LEFT JOIN` antara tabel `film` (kiri) dan tabel `inventory` (kanan) untuk mencari daftar film yang belum pernah masuk ke inventori toko (atau belum pernah disewa), di mana kolom inventori akan menghasilkan nilai `NULL`.
> - Contoh lainnya adalah mengidentifikasi pelanggan (_customer_) baru yang terdaftar tetapi belum pernah melakukan transaksi pembayaran (_payment_), sehingga nilai pembayaran di sisi kanan bernilai `NULL`.

Contoh SQL: film yang belum pernah masuk inventori (memanfaatkan `IS NULL` untuk menyaring hasil yang tidak berpasangan):

```sql
SELECT FM.title, I.inventory_id
FROM film FM
LEFT JOIN inventory I ON FM.film_id = I.film_id
WHERE I.inventory_id IS NULL;
```

#### C. RIGHT (OUTER) JOIN

- Kata kunci `RIGHT JOIN` (atau `RIGHT OUTER JOIN`) merupakan kebalikan dari `LEFT JOIN`. Perintah ini mengembalikan seluruh baris dari tabel sebelah kanan, beserta baris yang cocok dari tabel sebelah kiri.
- Jika tidak ada baris yang cocok di tabel sebelah kiri, maka kolom-kolom dari tabel kiri akan diisi dengan nilai `NULL`.

Sintaks Dasar:

```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

> [!warning] Audio Insight — RIGHT JOIN selalu bisa ditulis ulang sebagai LEFT JOIN
> - Dosen memaparkan bahwa setiap operasi `RIGHT JOIN` sebenarnya selalu dapat ditulis ulang (_rewritten_) menjadi bentuk `LEFT JOIN` hanya dengan membalik urutan penulisan tabelnya di dalam query.
> - Sebagai contoh, kueri `inventory RIGHT JOIN film` menghasilkan keluaran yang sama persis dengan kueri `film LEFT JOIN inventory`. Dalam dunia industri, para pengembang umumnya lebih menyukai penggunaan `LEFT JOIN` karena arah pembacaan logika yang mengalir dari kiri ke kanan.
> - Contoh visual yang ditunjukkan dosen adalah relasi antara `new_employees` dan `dept_info`. Dengan menggunakan `RIGHT JOIN`, kita dapat menampilkan semua daftar departemen yang ada di tabel kanan (`dept_info`) meskipun departemen tersebut belum memiliki satu pun karyawan dari tabel kiri (`new_employees`).

#### D. Penelusuran Langkah-demi-Langkah: Arah LEFT vs RIGHT JOIN

Titik yang paling sering membuat bingung: **"kiri" dan "kanan" mengacu pada urutan tabel di dalam kalimat query, bukan posisi di layar atau makna bisnis apa pun.**

Aturan mutlak untuk mengingat arah:
- Kata yang ditulis **segera setelah `FROM`** = tabel **KIRI**.
- Kata yang ditulis **segera setelah `LEFT JOIN` / `RIGHT JOIN`** = tabel **KANAN**.
- `LEFT JOIN` → **semua baris tabel KIRI dipertahankan**, meskipun tidak ada pasangannya di kanan (kolom kanan jadi `NULL`).
- `RIGHT JOIN` → **semua baris tabel KANAN dipertahankan**, meskipun tidak ada pasangannya di kiri (kolom kiri jadi `NULL`).

Mari telusuri dengan data contoh kecil. Anggap dua tabel berikut:

`film` (3 baris):

| film_id | title |
|:--|:--|
| 1 | Alpha |
| 2 | Bravo |
| 3 | Charlie |

`inventory` (2 baris — Charlie belum pernah masuk inventori toko):

| inventory_id | film_id |
|:--|:--|
| 101 | 1 |
| 102 | 2 |

**Query A — LEFT JOIN** (`film` di kiri, jadi seluruh baris `film` dipertahankan):

```sql
SELECT FM.title, I.inventory_id
FROM film FM
LEFT JOIN inventory I ON FM.film_id = I.film_id;
```

Langkah eksekusi:
1. Ambil seluruh baris dari `film` (tabel KIRI, karena berada segera setelah `FROM`) — semua 3 baris dipertahankan apa pun yang terjadi.
2. Untuk tiap baris `film`, cari baris `inventory` yang `film_id`-nya cocok.
3. Alpha (film_id=1) cocok dengan inventory_id 101 → pasangkan.
4. Bravo (film_id=2) cocok dengan inventory_id 102 → pasangkan.
5. Charlie (film_id=3) **tidak ada** yang cocok di `inventory` → kolom `inventory_id` diisi `NULL`, tapi baris Charlie **tetap muncul** karena `film` adalah tabel kiri pada `LEFT JOIN`.

Hasil Query A:

| title | inventory_id |
|:--|:--|
| Alpha | 101 |
| Bravo | 102 |
| Charlie | `NULL` |

**Query B — RIGHT JOIN** (tabel dan urutan penulisan yang SAMA, hanya keyword yang diganti):

```sql
SELECT FM.title, I.inventory_id
FROM film FM
RIGHT JOIN inventory I ON FM.film_id = I.film_id;
```

Langkah eksekusi:
1. Sekarang `inventory` menjadi tabel yang dipertahankan seluruhnya, karena ia berada tepat setelah keyword `RIGHT JOIN` (tabel KANAN yang jadi prioritas).
2. Ambil seluruh baris dari `inventory` — hanya ada 2 baris (101, 102) — Charlie tidak pernah ada di tabel ini sama sekali sehingga tidak bisa muncul.
3. Untuk tiap baris `inventory`, cari baris `film` yang `film_id`-nya cocok — keduanya cocok (Alpha, Bravo).

Hasil Query B:

| title | inventory_id |
|:--|:--|
| Alpha | 101 |
| Bravo | 102 |

**Perhatikan:** Query B (`RIGHT JOIN`) di atas kebetulan menghasilkan output yang identik dengan `INNER JOIN` biasa, karena setiap baris `inventory` memang punya pasangan di `film`. Baris Charlie yang "hilang" dari Query B bukan karena `RIGHT JOIN` salah, melainkan karena Charlie memang tidak pernah masuk ke `inventory` — dan `inventory` adalah tabel kanan yang dipertahankan penuh, bukan `film`.

**Cara tercepat menghindari salah arah:** jika Anda ingin "pertahankan semua baris dari tabel X, meskipun tabel Y tidak punya pasangan", maka tabel X **harus** Anda tulis:
- segera setelah `FROM`, dan gunakan `LEFT JOIN`, **atau**
- segera setelah `RIGHT JOIN` (tabel Y ditulis di `FROM`).

Kedua kueri berikut ini identik persis — inilah bukti konkret dari insight dosen di atas ("RIGHT JOIN selalu bisa ditulis ulang sebagai LEFT JOIN"):

```sql
-- Versi RIGHT JOIN
SELECT NE.first_name, D.dept_name
FROM new_employees NE
RIGHT JOIN dept_info D ON NE.dept_id = D.dept_id;

-- Versi LEFT JOIN yang setara persis (tabel ditukar urutan penulisannya)
SELECT NE.first_name, D.dept_name
FROM dept_info D
LEFT JOIN new_employees NE ON NE.dept_id = D.dept_id;
```

Karena arah pembacaan kiri-ke-kanan lebih alami, sebagian besar developer di industri memang membiasakan diri **selalu memakai `LEFT JOIN`** dan menyusun ulang urutan tabel di `FROM`, daripada memakai `RIGHT JOIN` secara langsung.

---

### 3.3 FULL (OUTER) JOIN dan Self JOIN

#### A. FULL (OUTER) JOIN

- `FULL OUTER JOIN` digunakan untuk mengembalikan semua baris ketika terdapat kecocokan baik di tabel sebelah kiri maupun tabel sebelah kanan.
- Jika ada baris di tabel kiri yang tidak memiliki pasangan di tabel kanan, atau baris di tabel kanan yang tidak memiliki pasangan di tabel kiri, kolom dari sisi yang tidak cocok akan diisi dengan nilai `NULL`.

Contoh sintaksis (catatan: MySQL tidak mendukung `FULL OUTER JOIN` secara native — biasanya disimulasikan dengan `UNION` dari `LEFT JOIN` dan `RIGHT JOIN`; di database lain seperti PostgreSQL, sintaks di bawah berjalan langsung):

```sql
SELECT FM.title, I.inventory_id
FROM film FM
FULL OUTER JOIN inventory I ON FM.film_id = I.film_id;

-- Simulasi FULL OUTER JOIN di MySQL menggunakan UNION:
SELECT FM.title, I.inventory_id
FROM film FM
LEFT JOIN inventory I ON FM.film_id = I.film_id
UNION
SELECT FM.title, I.inventory_id
FROM film FM
RIGHT JOIN inventory I ON FM.film_id = I.film_id;
```

#### B. Self JOIN

- _Self JOIN_ adalah operasi penggabungan suatu tabel dengan dirinya sendiri (_regular join to itself_).
- Karena tabel yang digabungkan sama, kita **wajib** memberikan alias yang berbeda untuk tabel tersebut (misalnya `T1` dan `T2`) pada klausul query agar database dapat membedakan peran masing-masing kolom.
- _Self JOIN_ dapat ditulis menggunakan gaya penggabungan implisit maupun eksplisit.

> [!warning] Audio Insight — Self JOIN: alias wajib, dan operator `<>` untuk menghindari duplikat diri sendiri
> - **Pencarian Pasangan Data Unik**: Dosen menjelaskan bahwa _Self JOIN_ sangat berguna ketika kita ingin membandingkan baris-baris data dalam satu tabel yang sama berdasarkan kriteria tertentu.
> - **Studi Kasus 1: Durasi Film yang Sama**:
>     - Kita ingin mencari pasangan film berbeda yang memiliki durasi pemutaran (_length_) yang sama persis di dalam database _Sakila_.
>     - Query ditulis dengan menghubungkan tabel `film T1` dengan `film T2` berdasarkan kesamaan kolom `length`, tetapi dibatasi agar tidak membandingkan baris yang sama dengan menggunakan operator tidak sama dengan (`<>` atau `!=`) pada kolom `film_id`.
> - **Studi Kasus 2: Tanggal Lahir Karyawan yang Sama**:
>     - Kita ingin mencari karyawan berbeda yang memiliki tanggal lahir (_birth_date_) yang sama persis di dalam tabel `employees`.
> - **Operator Tidak Sama Dengan**: Menjawab kebingungan mahasiswa mengenai arti simbol `<>` atau `!=` dalam query tersebut, dosen menjelaskan bahwa operator tersebut berarti "tidak sama dengan". Syarat ini mutlak dipasang agar database tidak menampilkan hasil redundan di mana suatu film atau karyawan berpasangan dengan dirinya sendiri.

Contoh kueri eksplisit (Studi Kasus 1):

```sql
SELECT T1.title, T2.title, T1.length
FROM film T1
JOIN film T2
ON T1.film_id <> T2.film_id AND T1.length = T2.length;
```

Contoh kueri (Studi Kasus 2):

```sql
SELECT T1.first_name, T1.last_name, T2.first_name, T2.last_name, T1.birth_date
FROM employees T1
JOIN employees T2
ON T1.emp_no <> T2.emp_no AND T1.birth_date = T2.birth_date;
```

#### C. Penelusuran Langkah-demi-Langkah: Kenapa Alias Wajib pada Self JOIN

Berbeda dari alias tabel pada JOIN biasa (yang sifatnya opsional/rekomendasi), pada Self JOIN alias **benar-benar wajib secara sintaksis** — jika dilewatkan, MySQL akan langsung menolak query dengan pesan error.

**Buktinya, coba jalankan versi TANPA alias berikut ini:**

```sql
-- INI AKAN ERROR: "Not unique table/alias: 'film'"
SELECT film.title, film.length
FROM film
JOIN film
ON film.length = film.length;
```

Kenapa error? Karena di dalam klausul `FROM film JOIN film`, database membaca nama tabel `film` yang muncul dua kali dan tidak tahu cara membedakan "film yang mana" yang dimaksud oleh `film.title` pada `SELECT`, atau `film.length` di kiri vs kanan pada `ON`. Bagi mesin database, kedua kemunculan `film` ini terlihat sebagai referensi yang ambigu ke objek yang sama persis.

**Versi yang benar, dengan alias `T1` dan `T2`:**

```sql
SELECT T1.title AS Film_A, T2.title AS Film_B, T1.length
FROM film T1
JOIN film T2
  ON T1.length = T2.length
 AND T1.film_id <> T2.film_id
LIMIT 10;
```

Langkah eksekusi ditelusuri:
1. `FROM film T1` — database membuat "salinan logis" pertama dari tabel `film`, dan memberinya label sementara `T1`. Ini bukan salinan data fisik, hanya sebuah alias/nama panggilan yang berlaku selama query ini berjalan.
2. `JOIN film T2` — database membuat "salinan logis" kedua dari tabel yang **sama persis** (`film`), diberi label `T2`. Sekarang ada dua "sisi" dari tabel yang sama, masing-masing dengan nama panggilannya sendiri.
3. `ON T1.length = T2.length` — pasangkan setiap baris `T1` dengan setiap baris `T2` yang punya nilai `length` sama.
4. `AND T1.film_id <> T2.film_id` — buang pasangan di mana `T1` dan `T2` sebenarnya merujuk ke **baris fisik yang sama** (misalnya film "Alpha" dipasangkan dengan dirinya sendiri, yang tentu punya `length` sama dengan dirinya sendiri — hasil ini tidak berguna).
5. Hasil akhir: pasangan dua film **berbeda** yang kebetulan punya durasi identik.

**Intinya:** alias di Self JOIN bukan sekadar mempersingkat penulisan (seperti pada JOIN antar-tabel berbeda) — alias di sini adalah **satu-satunya cara** database bisa membedakan dua peran dari tabel yang persis sama. Tanpa alias, query gagal total dengan error, bukan sekadar kurang rapi.

---

## Bab 4 Mengakses Database Menggunakan Python (Python MySQL Connector)

### 4.1 Langkah Persiapan (Prerequisites) dan Virtual Environment

#### A. Pengenalan Python MySQL Connector

- Python MySQL Connector merupakan library resmi yang memungkinkan program Python untuk berinteraksi, mengirimkan kueri, dan memanipulasi database MySQL secara langsung dari lingkungan Python.

#### B. Langkah Instalasi Package

- Untuk mulai menggunakan konektor, package `mysql-connector-python` harus diinstal terlebih dahulu di dalam lingkungan terminal atau command prompt sistem operasi.

Perintah instalasi standar menggunakan pip:

```bash
pip install mysql-connector-python
```

Atau jika menggunakan installer Python spesifik pada sistem Windows:

```bash
python -m pip install mysql-connector-python
```

> [!tip] Audio Insight — Mengatasi instalasi package yang diblokir sistem
> - **Penanganan Masalah Instalasi**: Dalam diskusi kelas, terdapat kasus di mana sistem operasi memblokir instalasi package global (misalnya ketika sistem Python dikelola oleh package manager seperti _UV_).
> - Dosen mengonfirmasi bahwa jika menemui kendala perizinan sistem ini, pengguna dapat menginstal package tersebut dengan menambahkan flag `--break-system-packages` agar sistem mengizinkan instalasi library konektor dan pandas:

```bash
pip install mysql-connector-python --break-system-packages
```

> - Namun, praktik terbaik yang direkomendasikan adalah menggunakan lingkungan virtual terisolasi (_Virtual Environment_) alih-alih memaksakan instalasi global pada sistem utama.

#### C. Pengelolaan Lingkungan Kerja dengan Anaconda/Conda (Virtual Environment)

- Manajemen lingkungan (_Environment Management_) sangat penting saat mengelola beberapa proyek pemrograman yang berbeda.
- Penggunaan Conda memungkinkan pembuatan lingkungan virtual terisolasi sehingga dependensi library antar-proyek tidak saling bertabrakan.
- Langkah-langkah pembuatan dan aktivasi lingkungan kerja di terminal:

```bash
# 1. Membuat environment baru (contoh nama: Purwadika) dengan Python 3.11
conda create -n Purwadika python=3.11

# 2. Mengaktifkan lingkungan kerja yang baru dibuat
conda activate Purwadika

# 3. Instalasi seluruh library pendukung yang dibutuhkan
pip install mysql-connector-python pandas python-dotenv
```

> [!tip] Audio Insight — Kenapa environment isolation penting, dan sinkronisasi VSCode
> - **Pentingnya Isolasi Environment**: Dosen menerangkan mengapa pembuatan environment baru sangat direkomendasikan. Jika seorang programmer bekerja pada lima proyek berbeda, satu proyek mungkin membutuhkan modul Pandas versi lama sementara proyek lainnya membutuhkan Pandas versi terbaru. Jika diinstal secara global, perubahan versi untuk proyek terbaru akan merusak kode pada proyek lama. Dengan Conda environment, dependensi setiap proyek disimpan terpisah dan aman.
> - **Konfigurasi VSCode Interpreter**: Setelah membuat environment di terminal, pengguna harus menyinkronkan VSCode agar menggunakan interpreter dari environment yang tepat. Caranya dengan mengklik menu pilihan interpreter di pojok kanan bawah editor VSCode (Select Python Interpreter) dan memilih `Purwadika`. Jika pilihan tersebut belum muncul di menu, dosen menyarankan untuk menutup (_close_) VSCode terlebih dahulu dan membukanya kembali agar daftar interpreter ter-refresh secara otomatis.

Manajemen environment dan package Python ini melengkapi dasar-dasar Python yang sudah dipelajari di [[Sesi 05 - Python Function and File Handling (JCAIEH M1)|Sesi 05 - Python Function and File Handling]] dan [[Sesi 08 - Python and Modular Programming (JCAIEH M1)|Sesi 08 - Python and Modular Programming]] — sekarang kita menggabungkan Python dengan database sungguhan.

---

### 4.2 Pembuatan Koneksi dan Eksekusi Query

#### A. Membangun Koneksi Database

- Setelah mengaktifkan environment dan menginstal modul konektor, langkah awal di dalam script Python adalah mengimpor modul `mysql.connector`.
- Koneksi ke database MySQL dibangun menggunakan metode `mysql.connector.connect()` dengan menyertakan parameter kredensial yang sesuai.

```python
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='YourPassword',
    database='world'
)
```

|Parameter|Tipe Data|Deskripsi / Fungsi|
|:--|:--|:--|
|`host`|String|Alamat server database berada (contoh: `'localhost'` jika database di komputer lokal).|
|`user`|String|Nama pengguna database yang sah (contoh: `'root'` atau nama pengguna kustom).|
|`passwd` atau `password`|String|Kata sandi rahasia untuk masuk ke server database MySQL.|
|`database`|String|Nama skema database spesifik yang ingin diakses (contoh: `'world'` atau `'sakila'`).|

Parameter-parameter ini persis sama dengan parameter koneksi GUI/CLI yang sudah dibahas di [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] Bab 12 — bedanya di sini kita menuliskannya di dalam kode Python, bukan mengisi form GUI.

#### B. Eksekusi Query Menggunakan Kursor (Method 1)

- Untuk mengirim perintah SQL dari Python ke MySQL server, program membutuhkan objek perantara bernama kursor (_cursor_).
- Langkah eksekusi query standar terdiri dari membuat kursor, menjalankan query, dan mengambil seluruh baris data menggunakan metode `fetchall()`.
- Untuk memudahkan analisis, hasil pengambilan data (_fetch_) diubah ke dalam bentuk struktur tabel Pandas DataFrame.

```python
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

Hasil `df` di atas adalah objek Pandas DataFrame biasa — semua teknik manipulasi data yang dipelajari di [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] (filtering, `.groupby()`, dsb.) bisa langsung diterapkan pada `df` ini setelah data ditarik dari MySQL.

---

### 4.3 Optimasi Query dengan Fungsi Kustom dan Keamanan Kredensial

#### A. Pembuatan Fungsi SQL DataFrame Kustom (Method 2)

- Menuliskan kode pembuatan kursor dan penarikan data secara berulang kali sangat tidak efisien jika kueri database dilakukan berkali-kali.
- Praktik terbaik untuk mengatasi hal ini adalah membuat fungsi pembungkus (_wrapper function_) kustom yang langsung menerima parameter query SQL dan mengembalikan objek Pandas DataFrame secara otomatis.

```python
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

Pola "wrapper function" ini adalah aplikasi langsung dari konsep pendefinisian fungsi (`def`) dan modular programming yang dipelajari di [[Sesi 08 - Python and Modular Programming (JCAIEH M1)|Sesi 08 - Python and Modular Programming]] — alih-alih menulis ulang kode cursor/execute/fetchall setiap kali, logika berulang itu dibungkus jadi satu fungsi yang bisa dipakai berkali-kali.

#### B. Penerapan Keamanan Kredensial Menggunakan .env (Dotenv)

- Menyimpan password database secara langsung dalam bentuk teks biasa (_hardcoded password_) di dalam file script Python sangat dilarang karena berisiko terekspos ketika kode diunggah ke repository publik seperti GitHub.
- Keamanan kredensial dikelola menggunakan file konfigurasi lingkungan bernama `.env`.

> [!tip] Audio Insight — File `.env` dan `.gitignore`
> - **Penggunaan File `.env` dan `.gitignore`**: Dosen menjelaskan bahwa file `.env` asli berisi data sensitif yang tidak boleh diunggah ke repository publik, sehingga file tersebut harus dimasukkan ke dalam daftar `.gitignore`.
> - Sebagai gantinya, dosen menyediakan file duplikat bernama `.env.copy` atau `env_copy` sebagai template. Template ini berisi kerangka variabel tanpa password asli yang berfungsi sebagai panduan bagi mahasiswa untuk menyalinnya menjadi file `.env` mandiri di komputer masing-masing.
> - Mahasiswa menyalin template tersebut dan mengedit isinya menggunakan kredensial database pribadi mereka:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=password_pribadi_anda
```

- Di dalam script Python, variabel rahasia ini dimuat menggunakan library `python-dotenv` dan modul `os` untuk mengamankan koneksi database:

```python
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

Membaca file `.env` dan mengelola file konfigurasi seperti ini adalah bentuk lanjutan dari file handling yang dipelajari di [[Sesi 05 - Python Function and File Handling (JCAIEH M1)|Sesi 05 - Python Function and File Handling]] — bedanya di sini file yang dibaca berisi kredensial rahasia, bukan data biasa, sehingga penanganannya (lewat `.gitignore`) menjadi krusial untuk keamanan.

---

## Bab 5 Sesi Latihan & Pembahasan (SQL Exercise — Database Sakila)

### 5.1 Pengantar Latihan Praktis Database Sakila

#### A. Petunjuk dan Persiapan Latihan

- Latihan praktis ini menggunakan database sampel standar industri bernama **"Sakila"**, yang merepresentasikan sistem operasional bisnis penyewaan film (_movie rental_).
- Pengerjaan instruksi SQL dapat dilakukan langsung menggunakan aplikasi klien basis data seperti **MySQL Workbench**, **DBeaver**, maupun secara terprogram lewat Jupyter Notebook/Jupyterlab menggunakan modul Python SQL Connector.
- Aktivitas penarikan data difokuskan pada manipulasi tabel tunggal, penggabungan multi-tabel (_multi-table join_), operasi agregasi, pemfilteran pola string menggunakan operator `LIKE`, hingga penggunaan kueri bersarang (_subquery_).

> [!tip] Audio Insight — Git pull dan aktivasi Virtual Environment sebelum latihan
> - Dosen mengingatkan mahasiswa untuk melakukan pembaharuan kode (_git pull_) terlebih dahulu pada repositori lokal masing-masing guna memastikan bahan latihan dan skema database "Sakila" serta "World" versi terbaru sudah tersinkronisasi sebelum sesi latihan dimulai. (Lihat [[Sesi 02 - Intro to Git and GitHub (JCAIEH M1)|Sesi 02 - Intro to Git and GitHub]] untuk dasar-dasar `git pull`.)
> - Jika mahasiswa menggunakan Jupyterlab, dosen menyarankan untuk mengaktifkan _Virtual Environment_ yang telah dibuat sebelumnya agar library konektor dapat dipanggil tanpa hambatan dependensi.

---

### 5.2 Pembahasan Soal 1 s.d. 5: Kueri Dasar, Pemfilteran, dan Agregasi

#### A. Nomor 1: Pemilihan Kolom dan Pembatasan Baris (Tabel payment)

- **Tujuan**: Menampilkan 10 baris data pertama dari tabel `payment` dengan memilih kolom `customer_id`, `rental_id`, `amount`, dan `payment_date`.

```sql
SELECT customer_id, rental_id, amount, payment_date
FROM payment
LIMIT 10;
```

- **Analisis Teknis**: Langkah ini menggunakan perintah proyeksi kolom secara spesifik guna menghemat memori transfer data dibandingkan menggunakan tanda bintang (`*`), serta membatasi baris hasil kueri tepat sebanyak 10 baris teratas menggunakan klausul `LIMIT`.

#### B. Nomor 2: Pemfilteran Teks Menggunakan Wildcard (Tabel film)

- **Tujuan**: Menampilkan 10 judul film (`title`), tahun rilis (`release_year`), dan durasi sewa (`rental_duration`) yang judulnya diawali dengan huruf "S".

```sql
SELECT title, release_year, rental_duration
FROM film
WHERE title LIKE 'S%'
LIMIT 10;
```

- **Analisis Teknis**: Karakter `%` pada klausa `LIKE 'S%'` bertindak sebagai _wildcard_ yang mewakili karakter apa pun setelah huruf "S" di awal teks.

#### C. Nomor 3: Pengelompokan Data dan Pembulatan Nilai Rata-Rata (Tabel film)

- **Tujuan**: Mengelompokkan data berdasarkan durasi rental (`rental_duration`) untuk menampilkan nilai durasi sewa, jumlah film di setiap kelompok, serta rata-rata panjang film (`length`) dengan pembulatan 2 angka desimal. Judul kolom diubah menggunakan alias bahasa Indonesia.

```sql
SELECT
    rental_duration AS durasi_rental,
    COUNT(*) AS banyak_film,
    ROUND(AVG(length), 2) AS rata_rata_durasi_film
FROM film
GROUP BY rental_duration;
```

- **Analisis Teknis**: Fungsi agregasi `COUNT(*)` menghitung total baris per kelompok, sedangkan `AVG(length)` menghitung nilai rata-rata yang kemudian dibulatkan menggunakan fungsi `ROUND(..., 2)`.

> [!tip] Audio Insight — Estetika indentasi kueri
> - Dosen memberikan masukan penting mengenai estetika penulisan kueri. Sangat disarankan untuk menerapkan indentasi yang konsisten (seperti menjorokkan kolom di bawah klausa `SELECT` atau menaruh klausa `FROM` dan `GROUP BY` pada baris baru) demi meningkatkan keterbacaan (_readability_) kueri SQL oleh anggota tim pengembang lainnya.

#### D. Nomor 4: Pemfilteran Kondisional di Atas Rata-Rata (Tabel film)

- **Tujuan**: Menampilkan `title`, durasi film (`length`), dan `rating` yang durasinya lebih tinggi dari rata-rata durasi seluruh film dalam database. Hasil dibatasi 25 baris dan diurutkan dari durasi terlama.

```sql
SELECT title, length, rating
FROM film
WHERE length > (SELECT AVG(length) FROM film)
ORDER BY length DESC
LIMIT 25;
```

- **Analisis Teknis**: Kueri ini menggunakan _Scalar Subquery_ di dalam klausul `WHERE` untuk menghitung nilai rata-rata dinamis secara global terlebih dahulu sebelum digunakan sebagai pembanding baris demi baris pada tabel utama. Konsep subquery ini dibahas lengkap di [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] Bab 11.

#### E. Nomor 5: Agregasi Multi-Fungsi dengan Group By (Tabel film)

- **Tujuan**: Menampilkan ringkasan statistik per kategori `rating` film, mencakup biaya penggantian tertinggi (_Replacement Cost_), tarif sewa terendah (_Rental Rate_), dan rata-rata durasi film (`length`).

```sql
SELECT
    rating,
    MAX(replacement_cost) AS Replacement_Cost_Tertinggi,
    MIN(rental_rate) AS Rental_Rate_Terendah,
    AVG(length) AS Rata_Rata_Durasi
FROM film
GROUP BY rating;
```

|Kategori Rating|Replacement Cost Tertinggi|Rental Rate Terendah|Perkiraan Rata-Rata Durasi (Menit)|
|:--|:--|:--|:--|
|**G**|29.99|0.99|~111.05|
|**PG**|29.99|0.99|~112.01|
|**PG-13**|29.99|0.99|~120.44|
|**R**|29.99|0.99|~118.66|
|**NC-17**|29.99|0.99|~113.23|

---

### 5.3 Pembahasan Soal 6 s.d. 10: Join Multi-Tabel, Pengurutan Kompleks, dan Subquery

#### A. Nomor 6: Penggabungan Dua Tabel dengan Kriteria Karakter Akhir

- **Tujuan**: Menampilkan 15 daftar film yang judulnya diakhiri dengan huruf "K", menyajikan kolom judul film, durasi, serta nama bahasanya.

```sql
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

- **Analisis Teknis**: Kolom `language_id` bertindak sebagai kunci relasi (_key join_) yang menghubungkan tabel `film` (sebagai _Foreign Key_) dengan tabel `language` (sebagai _Primary Key_). Kondisi `LIKE '%K'` memastikan hanya judul berakhiran "K" yang lolos filter.

#### B. Nomor 7: Penggabungan Tiga Tabel Berantai

- **Tujuan**: Menampilkan judul film, nama depan aktor, dan nama belakang aktor khusus untuk aktor yang memiliki `actor_id = 14`.

```sql
SELECT
    F.title AS Judul_Film,
    A.first_name AS First_Name,
    A.last_name AS Last_Name
FROM film F
INNER JOIN film_actor FA ON F.film_id = FA.film_id
INNER JOIN actor A ON FA.actor_id = A.actor_id
WHERE A.actor_id = 14;
```

- **Analisis Teknis**: Karena tabel `film` dan `actor` tidak memiliki hubungan relasional langsung (hubungan _Many-to-Many_), kueri harus melakukan penggabungan berantai (_nested join_) melewati tabel perantara (_bridge table_) yaitu `film_actor`.

#### C. Nomor 8: Pemfilteran Karakter Ganda dan Pengurutan Abjad (Tabel city)

- **Tujuan**: Menampilkan kota (`city`) dan `country_id` dari tabel `city` yang namanya mengandung huruf "d" di posisi mana pun dan wajib diakhiri dengan huruf "a". Hasil dibatasi 15 data dan diurutkan berdasarkan abjad kota.

```sql
SELECT city, country_id
FROM city
WHERE city LIKE '%d%a'
ORDER BY city ASC
LIMIT 15;
```

> [!tip] Audio Insight — Menyederhanakan dua kondisi LIKE menjadi satu pola
> - Dalam diskusi kelas, dosen menjelaskan efisiensi penulisan filter string. Mahasiswa awalnya menggunakan dua klausa terpisah yaitu `city LIKE '%d%' AND city LIKE '%a'`. Dosen mengonfirmasi bahwa penulisan tersebut dapat disederhanakan dan dioptimalkan menjadi satu ekspresi pola tunggal yaitu `LIKE '%d%a'`, karena pola tersebut secara otomatis menjamin adanya huruf "d" di bagian tengah/awal teks dan diakhiri secara mutlak oleh huruf "a".

#### D. Nomor 9: Agregasi Hasil Penggabungan Tiga Tabel

- **Tujuan**: Menampilkan nama kategori/genre film dan jumlah total film yang tergolong dalam setiap genre tersebut, diurutkan dari jumlah film paling sedikit (_ascending_).

```sql
SELECT
    C.name AS Genre,
    COUNT(FC.film_id) AS Banyak_Film
FROM category C
INNER JOIN film_category FC ON C.category_id = FC.category_id
INNER JOIN film F ON FC.film_id = F.film_id
GROUP BY C.name
ORDER BY Banyak_Film ASC;
```

- **Analisis Teknis**: Operasi ini menggabungkan tabel `category` ke tabel riwayat kategori `film_category`, lalu ke tabel utama `film`. Hasil penggabungan kemudian dikelompokkan berdasarkan nama genre menggunakan klausul `GROUP BY C.name` untuk menghitung frekuensi film menggunakan fungsi agregasi `COUNT()`.

#### E. Nomor 10: Pemfilteran Kompleks Menggunakan Subquery (Tabel film)

- **Tujuan**: Menampilkan `title`, `description`, `length`, dan `rating` untuk 10 film yang judulnya berakhiran dengan huruf "h" dan memiliki durasi di atas rata-rata panjang film keseluruhan secara global.

```sql
SELECT title, description, length, rating
FROM film
WHERE title LIKE '%H'
  AND length > (SELECT AVG(length) FROM film)
ORDER BY title ASC
LIMIT 10;
```

> [!tip] Audio Insight — Kenapa harus subquery, bukan WHERE length > AVG(length) langsung
> - **Keterbatasan Fungsi Agregat**: Mahasiswa menanyakan mengapa ekspresi pemfilteran tidak bisa ditulis secara langsung seperti `WHERE length > AVG(length)`. Dosen menerangkan aturan dasar SQL bahwa fungsi agregat seperti `AVG()` tidak dapat ditempatkan langsung di dalam klausul `WHERE` pada tingkat kueri yang sama. Hal ini karena proses filter `WHERE` dieksekusi oleh mesin database sebelum proses kalkulasi agregat baris dilakukan.
> - **Solusi Kueri Bersarang**: Solusi mutlak untuk masalah di atas adalah membungkus fungsi agregat di dalam subquery mandiri `(SELECT AVG(length) FROM film)`. Subquery tersebut akan dihitung terlebih dahulu untuk menghasilkan satu nilai skalar tunggal (misalnya nilai rata-rata 115 menit), yang kemudian disuntikkan ke kueri utama sebagai nilai konstan pembanding durasi masing-masing baris film.
> - **Ketentuan Group By**: Jika fungsi agregat ingin ditampilkan bersama dengan kolom non-agregat di tingkat SELECT utama, maka seluruh kolom non-agregat tersebut (seperti `title`, `description`, `length`, `rating`) wajib didaftarkan ke dalam klausul `GROUP BY` agar tidak menimbulkan kegagalan eksekusi (_SQL error_). Oleh karena itu, penggunaan subquery jauh lebih bersih dan efisien untuk kasus pemfilteran baris individual seperti ini. (Bandingkan dengan aturan `GROUP BY` di [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] Bab 8.)

---

### 5.4 Catatan Praktik Langsung di Kelas (Raw Lecture Notes)

Bagian ini adalah catatan mentah langsung dari sesi kuliah, dipertahankan sebagai referensi tambahan.

**Catatan visual dari slide kelas** (dua gambar tempel dari catatan asli, dideskripsikan berikut karena gambar tidak dapat disalin langsung ke Obsidian ini):

> Gambar 1 (`Pasted image 20260821191541.png`): mengilustrasikan Primary Key sebagai "unique identity" dan Foreign Key sebagai "kolom yang merefer ke sebuah key dari tabel lain."
>
> Gambar 2 (`Pasted image 20260821191705.png`): mengilustrasikan bahwa "Entity itu departemennya" dan "Primary key itu isinya" — yaitu, sebuah entity (misalnya `departments`) diidentifikasi oleh Primary Key-nya sendiri.

**Setup environment yang dipakai di kelas:**

```
environment location: C:\Users\reine\miniconda3\envs\purwadhika

# To activate this environment, use
#     $ conda activate purwadhika
# To deactivate an active environment, use
#     $ conda deactivate

pip install pandas python-dotenv   DONE
```

**Full script latihan Sakila (versi mentah dari catatan kelas, identik secara fungsional dengan pembahasan Soal 1–10 di atas — nama alias/kolom ditulis huruf kecil sesuai gaya penulisan asli dosen):**

```sql
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
```

Latihan Sakila ini menutup Module 1's SQL track. Langkah berikutnya beralih ke fondasi statistika di [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|Sesi 11 - Statistics Fundamental]], lalu kembali ke Python untuk manipulasi data tabular di [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] — di mana `pd.DataFrame` hasil `sql_df()` di Bab 4 session ini akan sering muncul lagi sebagai titik awal analisis.

---

## 🔗 Terkait

- [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|Sesi 09 - Intro to Database and SQL]] — fondasi DDL/DML/WHERE/GROUP BY yang jadi dasar sebelum masuk ke JOIN multi-tabel di sesi ini.
- [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|Sesi 12 - Python Data Manipulation With Pandas and Numpy]] — `pd.merge()`/`.join()` adalah padanan langsung dari INNER/LEFT/RIGHT/FULL JOIN yang dibahas di sesi ini.
- [[Sesi 07 - Object Oriented Programming (JCAIEH M1)|Sesi 07 - Object Oriented Programming]] — Primary/Foreign Key mirip konsep referensi antar-object, meski relasinya di level tabel bukan object.
