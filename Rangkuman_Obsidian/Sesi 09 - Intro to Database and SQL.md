---
tags: [module1, sesi-09, sql, database, dbms, ddl, dml, filtering, sorting, aggregate-function, scalar-function, group-by, having, subquery, date-time-functions]
aliases: ["Sesi 9", "Sesi 09", "Intro to Database and SQL"]
---

# Session 9 — Intro to Database & SQL

> Catatan struktur: urutan Bab di file ini disusun ulang dari urutan bab pada sumber asli (yang sempat melompat-lompat: Bab 1 → Bab 10 → Bab 2 → Bab 3 → ... ) agar mengikuti alur belajar yang logis — dari konsep DBMS, ke DDL (membuat struktur), ke DML (mengisi/mengambil data), ke penyaringan, ke fungsi-fungsi lanjutan, dan ditutup dengan koneksi tools serta latihan praktis. Seluruh isi substantif dari sumber asli tetap dipertahankan.

## Bab 1 Pengenalan Database & Database Management System (DBMS)

### 1.1 Definisi dan Karakteristik Database

#### A. Fondasi Konseptual Database

- Database didefinisikan sebagai koleksi data yang terorganisasi, yang secara umum disimpan dan diakses secara elektronik dari sistem komputer.
- Istilah electronic database merujuk pada kumpulan data atau informasi apa pun yang dirancang secara khusus untuk kebutuhan rapid search dan retrieval menggunakan bantuan komputer.
- Pada tingkat kompleksitas yang lebih tinggi, database dikembangkan dengan menerapkan teknik formal design dan modeling.

| Istilah             | Karakteristik Utama                                                           |
| :------------------ | :---------------------------------------------------------------------------- |
| Database            | Organized collection of data yang disimpan secara elektronik.                 |
| Electronic Database | Kumpulan data atau informasi yang dirancang untuk rapid search dan retrieval. |
| Complex Database    | Memerlukan teknik formal design dan modeling dalam pengembangannya.           |

#### B. Mekanisme Penyimpanan Elektronik

- Penyimpanan data dalam sistem komputer ditujukan untuk efisiensi pengolahan informasi digital.
- Pengorganisasian data yang sistematis memungkinkan pencarian informasi yang cepat dan akurat.

> [!tip] Audio Insight — Tujuan database bukan sekadar penyimpanan pasif
> - Database bukan sekadar tempat penyimpanan pasif untuk menaruh data.
> - Tujuan utama penyimpanan data adalah untuk memfasilitasi penggunaan kembali data tersebut di masa mendatang, baik untuk proses retrieve maupun search.
> - Data yang disimpan harus diorganisasikan agar proses pencarian kembali dapat dilakukan secara cepat oleh sistem komputer.

### 1.2 Terminologi Formal dan Peran DBMS

#### A. Komponen Utama Arsitektur Informasi

- Secara formal, istilah "database" merujuk pada satu set related data beserta metode pengorganisasian data tersebut.
- Akses terhadap data yang terorganisasi ini disediakan melalui perantara yang disebut Database Management System (DBMS).
- DBMS terdiri dari integrated set of computer software yang mengizinkan user untuk berinteraksi dengan satu atau lebih database.
- DBMS menyediakan akses terhadap seluruh data yang tersimpan di dalam database, meskipun pembatasan akses dapat diberlakukan untuk melindungi data tertentu.

|Komponen|Deskripsi Fungsional|
|:--|:--|
|Related Data|Kumpulan data yang saling berhubungan secara logis dan terstruktur.|
|DBMS|Integrated set of computer software untuk interaksi user dengan database.|
|Access Restriction|Mekanisme pembatasan akses untuk melindungi integritas dan kerahasiaan data tertentu.|

#### B. Interaksi Pengguna dan Pengaturan Akses

- Pengguna tidak langsung memanipulasi file data fisik, melainkan berinteraksi melalui lapisan software DBMS.
- Pengaturan hak akses diatur oleh DBMS untuk membatasi query atau pembacaan data yang tidak diizinkan.

> [!tip] Audio Insight — DBMS sebagai perantara
> - Database didefinisikan sebagai kumpulan data-data yang saling berhubungan (related data) dan cara penyimpanan data tersebut secara terstruktur.
> - DBMS bertindak sebagai software perantara yang memungkinkan user mengakses, mengelola, dan berinteraksi dengan satu atau lebih database secara efisien.
> - Tanpa adanya DBMS, pengguna akan mengalami kesulitan besar dalam mengontrol dan mengamankan data yang tersebar dalam sistem.

### 1.3 Fungsi Utama dan Efisiensi Kerja DBMS

#### A. Fungsionalitas Teknis DBMS

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

#### B. Peningkatan Produktivitas Kerja

- DBMS mengotomatisasi pencarian data yang jika dilakukan secara manual akan memakan waktu sangat lama.
- Pemrosesan data yang terpusat meminimalkan duplikasi pekerjaan dan kesalahan manusia.

> [!tip] Audio Insight — Analogi Excel vs SQL
> - DBMS mempermudah analisis data bisnis secara cepat tanpa perlu membaca data tabular satu per satu secara manual.
> - **Contoh Kasus Pelanggan:** Jika perusahaan ingin mengetahui pelanggan mana yang paling loyal (sering membeli) atau pelanggan mana yang paling jarang melakukan pembelian, DBMS dapat langsung menjawab pertanyaan tersebut dengan cepat, asalkan data transaksi tersedia di database dan query ditulis dengan benar.
> - **Analogi Efisiensi (Excel vs SQL):** Di Microsoft Excel, pencarian pelanggan loyal dari data tabular yang besar dapat dilakukan menggunakan fitur Pivot. Di dalam DBMS, terdapat bahasa pemrograman khusus (SQL) yang memungkinkan pengguna melakukan pengelompokan dan analisis serupa secara jauh lebih cepat dan efisien dengan menuliskan sintaks kueri yang tepat.
> - DBMS sangat membantu pengguna dalam memahami data yang rumit, namun apabila tingkat kompleksitas data terlalu tinggi, DBMS memerlukan dukungan teknik lain seperti visualisasi data (lihat [[Sesi 13 - Data Visualization]]).

### 1.4 Database dalam Manajemen Bisnis dan Pengambilan Keputusan

#### A. Pemanfaatan Strategis Informasi dalam Bisnis

- Dunia usaha atau bisnis memanfaatkan database untuk melakukan pelacakan terhadap basic transaction.
- Database menyediakan informasi penting yang membantu perusahaan menjalankan bisnis secara lebih efisien.
- Database berfungsi membantu manager dan employee dalam membuat keputusan yang lebih baik.

|Tujuan Bisnis|Manfaat Database|
|:--|:--|
|Tracking|Memantau jalannya transaksi dasar (basic transaction) perusahaan.|
|Efficiency|Menyediakan data operasional untuk efisiensi bisnis.|
|Decision-Making|Menyediakan landasan informasi bagi manajer dan karyawan untuk mengambil keputusan.|

#### B. Pengambilan Keputusan Berbasis Data

- Penggunaan database memastikan setiap kebijakan operasional didasarkan pada fakta keras yang terekam dalam sistem, bukan asumsi subjektif.
- Akurasi pengambilan keputusan meningkat seiring dengan ketersediaan data historis transaksi yang lengkap.

> [!tip] Audio Insight — Data-driven decision making
> - Konsep pengambilan keputusan berbasis data (data-driven decision making) hanya dapat diwujudkan apabila seluruh data bisnis tersimpan dengan baik di dalam database.
> - Para manajer, karyawan, dan seluruh stakeholder yang terkait membutuhkan akses data real-time untuk menghasilkan better decision.
> - DBMS merupakan satu-satunya alat penunjang utama yang memungkinkan para pengambil keputusan tersebut mengakses dan menyaring informasi yang relevan dari database.

Konsep DBMS ini menjadi fondasi untuk [[Sesi 10 - SQL Working With Multiple Tables]], di mana kita akan belajar bagaimana beberapa tabel di dalam satu DBMS bisa saling terhubung lewat Primary Key dan Foreign Key.

---

## Bab 2 Operasi Dasar Database & Pembuatan Tabel (DDL — Data Definition Language)

### 2.1 Operasi Dasar Database

#### A. Pendefinisian dan Manajemen Database

- Database baru didefinisikan dan dibuat pada server database menggunakan perintah Data Definition Language (DDL).
- Pembuatan database menghasilkan ruang penyimpanan kosong di server yang siap diisi dengan berbagai objek database, seperti tabel.
- Operasi manajemen database dasar meliputi pembuatan, melihat daftar database yang aktif, memilih database untuk digunakan, dan menghapus database dari server.

|Perintah SQL|Deskripsi Fungsional|Kode Contoh|
|:--|:--|:--|
|CREATE DATABASE|Membuat database baru di server database.|`CREATE DATABASE Seller;`|
|SHOW DATABASES|Menampilkan daftar seluruh database yang tersedia di server.|`SHOW DATABASES;`|
|USE|Mengaktifkan database tertentu agar query selanjutnya dieksekusi di database tersebut.|`USE Seller;`|
|DROP DATABASE|Menghapus database beserta seluruh tabel dan data di dalamnya secara permanen.|`DROP DATABASE Seller;`|

#### B. Sintaksis dan Eksekusi Perintah SQL

- Setiap perintah DDL diakhiri dengan tanda titik koma (`;`) sebagai pembatas (delimiter) standar dalam SQL, terutama ketika mengeksekusi beberapa perintah sekaligus.
- Penghapusan database menggunakan perintah `DROP DATABASE` harus dilakukan secara hati-hati karena tindakan ini bersifat destruktif dan tidak dapat dibatalkan (undo).

> [!warning] Audio Insight — Urutan operasi, refresh UI, dan database sistem bawaan
> - **Proses Refresh UI:** Saat membuat database baru (misalnya `demo_scratch`) melalui SQL script editor di perangkat lunak GUI seperti DBeaver, database baru tersebut tidak akan langsung muncul di panel navigasi kiri secara otomatis. Pengguna harus melakukan operasi _refresh_ (menekan tombol F5 atau klik kanan -> _Refresh_) untuk memperbarui tampilan antarmuka pengguna.
> - **Urutan Operasi:** Setelah database dibuat menggunakan `CREATE DATABASE`, pengguna wajib mengaktifkan database tersebut dengan perintah `USE` sebelum dapat membuat tabel atau memasukkan data ke dalamnya.
> - **Sistem Bawaan:** Saat pertama kali mengoneksikan database server yang baru diinstal, sistem secara bawaan sudah memiliki database sistem default bernama `sys` yang digunakan untuk keperluan internal sistem DBMS.

**Contoh alur kerja lengkap** (menggabungkan seluruh perintah di atas, urutannya penting):

```sql
SHOW DATABASES;              -- 1. lihat database apa saja yang sudah ada
CREATE DATABASE demo_scratch; -- 2. buat database baru
USE demo_scratch;             -- 3. aktifkan database yang baru dibuat
-- ... di sini baru boleh CREATE TABLE / INSERT / dst ...
DROP DATABASE demo_scratch;   -- 4. (opsional) hapus permanen jika sudah tidak dipakai
```

---

### 2.2 Pembuatan Tabel Baru (CREATE TABLE)

#### A. Struktur dan Definisi Kolom Tabel

- Tabel adalah objek database utama yang menyimpan data dalam bentuk baris (rows) dan kolom (columns).
- Perintah `CREATE TABLE` digunakan untuk mendefinisikan tabel baru dengan menentukan nama tabel, nama kolom, serta tipe data untuk masing-masing kolom.
- Tipe data (Data Type) menentukan jenis nilai yang dapat disimpan oleh suatu kolom, seperti angka bulat (integer) atau karakter teks (character string).

|Karakteristik Struktur|Deskripsi Teknis|
|:--|:--|
|Table Name|Nama pengidentifikasi unik untuk tabel di dalam database yang aktif.|
|Column Name|Nama pengidentifikasi unik untuk setiap kolom dalam tabel.|
|Data Type|Jenis data yang dialokasikan untuk kolom (seperti `int` atau `varchar`).|
|Character Limit|Batas panjang karakter maksimum yang dapat ditampung oleh tipe data string/character.|

#### B. Sintaksis Dasar Pembuatan Tabel

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    column4 datatype
);
```

#### C. Contoh Praktis Pembuatan Tabel Persons

```sql
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
```

- Kolom `PersonID` menggunakan tipe data `int` yang dialokasikan untuk menyimpan bilangan bulat (integer).
- Kolom `LastName`, `FirstName`, `Address`, dan `City` menggunakan tipe data `varchar(255)`, yang berarti kolom-kolom tersebut menampung data karakter alfanumerik variabel dengan batas panjang maksimum 255 karakter.

#### D. Deskripsi dan Verifikasi Struktur Tabel

- Setelah tabel berhasil dibuat, struktur tabel tersebut dapat diverifikasi untuk memastikan tipe data dan batasan kolom telah terkonfigurasi dengan benar.

```sql
DESCRIBE Persons;
```

> [!tip] Audio Insight — Verifikasi struktur, nullability, dan constraint key
> - **Verifikasi Struktur via GUI dan CLI:** Pada aplikasi GUI seperti DBeaver, detail kolom dapat dilihat dengan mengklik ganda nama tabel lalu membuka tab _Data_ atau _Properties_. Di sisi lain, pada CLI, perintah `DESCRIBE` (contoh: `DESCRIBE person;`) akan menampilkan informasi kolom berupa nama kolom (_Field_), tipe data (_Type_), apakah kolom diperbolehkan kosong (_Null_), dan penunjuk kunci (_Key_).
> - **Pengaturan Nullability:** Kolom-kolom pada tabel `Persons` yang baru dibuat secara default akan bernilai `YES` pada kolom _Null_. Ini berarti kolom tersebut bersifat opsional dan diperbolehkan untuk tidak memiliki nilai (bernilai null) saat pengisian data.
> - **Ketiadaan Constraint Key:** Pada contoh dasar ini, belum ada kolom yang didefinisikan sebagai _Primary Key_ atau kunci unik lainnya, sehingga kolom _Key_ pada deskripsi struktur tabel masih kosong. Konsep Primary Key/Foreign Key ini dibahas tuntas di [[Sesi 10 - SQL Working With Multiple Tables]].

---

### 2.3 Pembuatan Tabel Berdasarkan Tabel yang Sudah Ada (CREATE TABLE Using Another Table)

#### A. Konsep Duplikasi Struktur dan Data

- Sistem database mengizinkan pembuatan tabel baru dengan menyalin definisi kolom dari tabel yang sudah ada.
- Metode ini dikenal dengan istilah _CREATE TABLE Using Another Table_.
- Tabel baru yang dihasilkan akan mewarisi definisi kolom yang sama persis dengan tabel sumber, dan secara otomatis terisi oleh data dari tabel sumber berdasarkan query pemilihan yang didefinisikan.

#### B. Sintaksis Duplikasi Tabel

```sql
CREATE TABLE new_table_name AS
SELECT column1, column2
FROM existing_table_name
WHERE condition;
```

- Pengguna dapat menyalin seluruh kolom menggunakan simbol asterisk (`*`) atau hanya memilih beberapa kolom spesifik yang dibutuhkan dari tabel sumber.

#### C. Contoh Praktis Duplikasi Tabel TestTable

```sql
CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers;
```

> [!tip] Audio Insight — Penundaan latihan praktis
> - **Penundaan Latihan Praktis:** Dalam sesi kuliah luring, dosen memutuskan untuk menunda praktik langsung pembuatan tabel menggunakan metode _CREATE TABLE Using Another Table_ ini. Penundaan ini bertujuan agar mahasiswa memahami terlebih dahulu dasar-dasar query pencarian dan manipulasi data dasar menggunakan klausa `SELECT`, `FROM`, dan `WHERE` (DML) secara menyeluruh sebelum melakukan operasi penyalinan struktur database yang lebih kompleks.

---

## Bab 3 Manipulasi Data Dasar & Pemilihan Data (DML — Data Manipulation Language)

### 3.1 Memasukkan Data Baru ke Tabel (INSERT INTO)

#### A. Definisi dan Fungsi Perintah INSERT INTO

- Perintah `INSERT INTO` digunakan untuk menambahkan baris data baru (records) ke dalam suatu tabel di database.
- Data yang dimasukkan harus mematuhi tipe data dan aturan kolom yang didefinisikan saat tabel dibuat pada tahap DDL.

|Metode INSERT|Karakteristik Sintaksis|Keuntungan Utama|
|:--|:--|:--|
|Metode Pertama|Menspesifikasikan nama kolom sebelum klausa VALUES.|Aman jika struktur urutan kolom tabel berubah di masa depan.|
|Metode Kedua|Langsung memasukkan nilai setelah klausa VALUES tanpa nama kolom.|Query lebih pendek dan cepat ditulis, namun nilai wajib sesuai urutan skema kolom.|

#### B. Metode Pertama INSERT INTO (Spesifikasi Nama Kolom)

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

Contoh Kasus:

```sql
INSERT INTO persons (PersonID, LastName, FirstName, Address, City)
VALUES (1, 'Andrew', 'Michael', 'Jln. Mawar', 'BSD');
```

#### C. Metode Kedua INSERT INTO (Tanpa Spesifikasi Nama Kolom)

- Jika nilai ditambahkan untuk seluruh kolom tabel, penulisan nama kolom dapat dilewati dengan syarat urutan nilai wajib sama persis dengan urutan kolom dalam skema tabel asli.

```sql
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

Contoh Kasus:

```sql
INSERT INTO persons
VALUES (2, 'Zidane', 'Zinedine', 'Jln. Anggret', 'DKI');
```

> [!tip] Audio Insight — Semicolon dan penyisipan data ganda
> - **Aturan Penggunaan Titik Koma (Semicolon):** Dalam perangkat lunak DBMS seperti DBeaver atau MySQL Workbench, penggunaan titik koma di akhir baris query bersifat opsional jika Anda mengeksekusi query satu per satu. Namun, jika Anda menjalankan beberapa perintah sekaligus (multiple commands) secara berurutan, titik koma wajib diletakkan di akhir setiap query sebagai pemisah agar tidak memicu error sistem.
> - **Penyisipan Data Ganda (Multiple Rows Insert):** DBMS mendukung penyisipan banyak baris data sekaligus dalam satu kali eksekusi perintah `INSERT INTO` untuk meningkatkan efisiensi operasional. Caranya adalah dengan memisahkan setiap kelompok nilai menggunakan tanda koma di dalam klausa `VALUES`.

Contoh Sintaksis Penyisipan Ganda:

```sql
INSERT INTO persons (PersonID, LastName, FirstName, Address, City)
VALUES
(3, 'Gandi', 'G', 'Jalan Caka', 'Jakarta'),
(4, 'Arif', 'A', 'Jalan Caka', 'Jakarta');
```

---

### 3.2 Pemilihan dan Menampilkan Data Tabel (SELECT)

#### A. Kegunaan Perintah SELECT

- Perintah `SELECT` digunakan untuk mengekstrak dan menampilkan data dari tabel database.
- Hasil pencarian data tersebut disimpan dalam tabel hasil sementara yang disebut sebagai result-set.

|Jenis Perintah SELECT|Bentuk Sintaksis|Efek Terhadap Kolom Hasil|
|:--|:--|:--|
|SELECT Bintang (`*`)|`SELECT * FROM table_name;`|Menampilkan seluruh kolom yang terdaftar di tabel secara lengkap.|
|SELECT Kolom Spesifik|`SELECT col1, col2 FROM table_name;`|Hanya menampilkan kolom-kolom yang didefinisikan secara eksplisit.|

#### B. Menampilkan Seluruh Kolom (*)

```sql
SELECT * FROM table_name;
```

Contoh Kasus (Menampilkan seluruh data kota dari tabel `City` yang memiliki kolom ID, Name, CountryCode, District, dan Population):

```sql
SELECT * FROM CITY;
```

#### C. Menampilkan Kolom Tertentu

```sql
SELECT column1, column2, ...
FROM table_name;
```

Contoh Kasus (Mengambil kolom nama kota, distrik, dan populasi dari tabel `City`):

```sql
SELECT Name, District, Population
FROM City;
```

> [!tip] Audio Insight — SELECT * vs kolom spesifik
> - Penggunaan `SELECT *` sangat praktis saat melakukan eksplorasi data awal guna memahami skema dan isi tabel. Namun, pada database produksi skala besar, menyeleksi kolom spesifik jauh lebih direkomendasikan untuk menghindari overhead transfer data yang tidak diperlukan.

---

### 3.3 Menampilkan Nilai Unik (SELECT DISTINCT)

#### A. Konsep Penghapusan Duplikasi

- Di dalam tabel database, sebuah kolom sering kali berisi nilai-nilai yang sama (duplikat).
- Klausa `DISTINCT` digunakan di dalam pernyataan `SELECT` untuk menyaring hasil query sehingga hanya menampilkan nilai-nilai yang unik dan berbeda saja.

|Sintaksis DISTINCT|Target Pengolahan|Output Hasil Query|
|:--|:--|:--|
|`SELECT DISTINCT column_name`|Mengidentifikasi nilai-nilai unik dalam kolom terpilih.|Menghilangkan seluruh nilai duplikat yang redundan dari result-set.|

#### B. Sintaksis SELECT DISTINCT

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

Contoh Kasus 1 (Mendapatkan daftar nama kota unik dari tabel `City` tanpa pengulangan nama yang sama):

```sql
SELECT DISTINCT Name
FROM City;
```

Contoh Kasus 2 (Mendapatkan daftar distrik unik dari tabel `City`):

```sql
SELECT DISTINCT District
FROM City;
```

> [!tip] Audio Insight — Kegunaan bisnis DISTINCT
> - Penggunaan `SELECT DISTINCT` sangat penting dalam analisis data bisnis, misalnya untuk mengetahui sebaran kota asal pelanggan atau daftar wilayah pengiriman yang aktif tanpa perlu dibingungkan oleh ribuan baris transaksi duplikat yang berulang.

---

### 3.4 Membatasi Jumlah Baris Query (LIMIT)

#### A. Pengendalian Volume Output Query

- Klausa `LIMIT` digunakan untuk menentukan jumlah baris data maksimal yang ingin ditampilkan oleh result-set.
- Aturan ini sangat berguna untuk membatasi tampilan record sehingga pengolahan data menjadi lebih cepat dan efisien.

|Kata Kunci|Kegunaan Utama|Implikasi Kinerja DBMS|
|:--|:--|:--|
|`LIMIT n`|Membatasi baris yang ditampilkan maksimal sebanyak n baris teratas.|Menghemat memori dan mempercepat waktu tunggu retrieval data skala besar.|

#### B. Sintaksis Klausa LIMIT

```sql
SELECT column1, column2, ...
FROM table_name
LIMIT number;
```

Contoh Kasus 1 (Menampilkan 3 baris data teratas dari tabel `City`):

```sql
SELECT * FROM City
LIMIT 3;
```

Contoh Kasus 2 (Menampilkan 5 baris data teratas dari tabel `City`):

```sql
SELECT * FROM City
LIMIT 5;
```

> [!warning] Audio Insight — LIMIT untuk optimasi, dan bahayanya jika dilupakan
> - **Kombinasi Strategis:** Klausa `LIMIT` akan bekerja secara maksimal ketika dikombinasikan dengan perintah pengurutan data (`ORDER BY`). Sebagai contoh, kombinasi ini dapat mempermudah pencarian record ekstrem seperti "3 kota dengan populasi tertinggi" atau "5 pelanggan dengan transaksi paling sedikit" (_Top-N_ dan _Bottom-N_ analysis).
> - **Optimasi Kueri:** Menjalankan kueri `SELECT * FROM table_name` pada tabel berisi jutaan baris tanpa menyertakan klausa `LIMIT` dapat membebani server database secara signifikan karena sistem dipaksa memproses dan mencetak seluruh data sekaligus. Membiasakan diri menggunakan `LIMIT` saat eksplorasi data adalah praktik terbaik dalam pengembangan aplikasi database.

---

## Bab 4 Penyaringan Data Tingkat Lanjut (Filtering Data)

### 4.1 Klausa Penyaringan WHERE

- Klausa `WHERE` adalah perintah dasar yang digunakan untuk menyaring baris data (_records_) dari tabel.
- Fungsi utama klausa ini adalah mengekstrak hanya baris data yang memenuhi kriteria atau kondisi spesifik yang ditentukan.
- Klausa `WHERE` diletakkan setelah klausa `FROM` dalam struktur query SQL.

#### A. Sintaksis Dasar dan Penyaringan Nilai Numerik

- SQL menggunakan operator perbandingan standar seperti `=`, `>`, `<`, `>=`, `<=`, dan `<>` (tidak sama dengan) dalam kondisi `WHERE`.
- Kriteria penyaringan numerik tidak membutuhkan tanda kutip di sekitar nilai angka yang dicari.

```sql
SELECT column1, column2, ... FROM table_name WHERE condition;
```

Contoh query untuk menyaring seluruh kolom dari tabel `City` yang memiliki jumlah populasi lebih dari satu juta jiwa (1.000.000):

```sql
SELECT * FROM City WHERE Population > 1000000;
```

#### B. Penyaringan Data Teks dan String

- Penyaringan data teks atau string membutuhkan penggunaan tanda kutip tunggal (`'`) di sekitar nilai teks yang menjadi kriteria penyaringan.

Contoh query untuk menyaring seluruh kolom dari tabel `City` yang berada di negara Indonesia (menggunakan kode negara `'IDN'`):

```sql
SELECT * FROM City WHERE CountryCode = 'IDN';
```

#### C. Penggabungan Beberapa Kondisi (AND dan OR Operator)

- Beberapa kriteria penyaringan dapat digabungkan secara logis menggunakan operator `AND` atau `OR`.
- Operator `AND` mengharuskan seluruh kondisi penyaringan terpenuhi agar baris data ditampilkan.
- Operator `OR` mengizinkan baris data ditampilkan apabila salah satu kondisi penyaringan terpenuhi.

Contoh query menggunakan operator `AND` untuk menampilkan kota di Indonesia yang memiliki populasi di atas 500.000 jiwa:

```sql
SELECT * FROM City WHERE CountryCode = 'IDN' AND Population > 500000;
```

Contoh query menggunakan operator `OR` untuk menampilkan kota yang berada di Indonesia (`'IDN'`) atau Malaysia (`'MYS'`):

```sql
SELECT * FROM City WHERE CountryCode = 'IDN' OR CountryCode = 'MYS';
```

> [!tip] Audio Insight — Kekakuan AND vs kelonggaran OR
> - Klausa `WHERE` bertindak sebagai penyaring pertama sebelum data diolah lebih lanjut oleh sistem.
> - Di dalam diskusi kuliah dicontohkan bahwa operator `AND` memaksa pemenuhan kondisi secara kaku (misalnya, kota tersebut harus berada di negara Indonesia sekaligus memiliki populasi padat). Sebaliknya, operator `OR` memberikan kelonggaran di mana baris data akan lolos penyaringan apabila salah satu dari kondisi terpenuhi.

---

### 4.2 Pencocokan Pola Teks (String Patterns menggunakan LIKE Operator)

- Operator `LIKE` digunakan bersama klausa `WHERE` untuk mencari pola teks tertentu (_specified pattern_) pada kolom string.
- Pencocokan pola ini sangat berguna ketika pengguna tidak mengetahui nilai teks secara persis tetapi mengetahui sebagian polanya.

#### A. Penggunaan Wildcard dalam SQL

- SQL menyediakan dua karakter khusus (_wildcards_) yang digunakan bersama operator `LIKE`:
    - `%` (Tanda Persen): Merepresentasikan nol, satu, atau beberapa karakter (_zero, one, or multiple characters_).
    - `_` (Tanda Garis Bawah / Underscore): Merepresentasikan satu karakter tunggal saja secara eksis (_exactly a single character_).
- Kedua wildcard ini dapat digunakan secara terpisah maupun digabungkan dalam satu pola pencarian teks.

|Pola Operator LIKE|Deskripsi Pola Pencarian|Contoh Query yang Berjalan (database `world`)|
|:--|:--|:--|
|`WHERE SellerName LIKE 'a%'`|Menemukan nilai teks yang diawali dengan huruf "a".|`SELECT Name FROM Country WHERE Name LIKE 'A%';`|
|`WHERE SellerName LIKE '%a'`|Menemukan nilai teks yang diakhiri dengan huruf "a".|`SELECT Name FROM Country WHERE Name LIKE '%a';`|
|`WHERE SellerName LIKE '%or%'`|Menemukan nilai teks yang mengandung suku kata "or" di posisi mana pun.|`SELECT Name FROM Country WHERE Name LIKE '%or%';`|
|`WHERE SellerName LIKE '_r%'`|Menemukan nilai teks yang memiliki huruf "r" di posisi kedua.|`SELECT Name FROM City WHERE Name LIKE '_r%';`|
|`WHERE SellerName LIKE 'a_%'`|Menemukan nilai teks yang diawali dengan huruf "a" dengan panjang minimal 2 karakter.|`SELECT Name FROM Country WHERE Name LIKE 'A_%';`|
|`WHERE SellerName LIKE 'a__%'`|Menemukan nilai teks yang diawali dengan huruf "a" dengan panjang minimal 3 karakter.|`SELECT Name FROM Country WHERE Name LIKE 'A__%';`|
|`WHERE SellerName LIKE 'a%o'`|Menemukan nilai teks yang diawali dengan huruf "a" dan diakhiri dengan huruf "o".|`SELECT Name FROM Country WHERE Name LIKE 'A%o';`|

#### B. Implementasi Query dengan Wildcard Persen (%)

Contoh query menampilkan seluruh kolom dari tabel `City` yang nama distriknya diawali dengan huruf 'Y':

```sql
SELECT * FROM CITY WHERE DISTRICT LIKE 'Y%';
```

Contoh query menampilkan seluruh kolom dari tabel `City` yang nama distriknya diakhiri dengan huruf 'x':

```sql
SELECT * FROM CITY WHERE DISTRICT LIKE '%x';
```

Contoh query menampilkan seluruh kolom dari tabel `City` yang nama kotanya diawali dengan huruf 'Y' dan diakhiri dengan huruf 'a':

```sql
SELECT * FROM CITY WHERE NAME LIKE 'Y%a';
```

> [!tip] Audio Insight — Contoh kota berawalan 'X', dan sifat dinamis wildcard %
> - Dalam rekaman audio kuliah, dosen memberikan contoh praktis pencarian kota yang diawali dengan huruf tertentu, seperti kota yang diawali dengan huruf 'X'. Saat kueri dijalankan, database langsung mengekstrak kota-kota seperti Xushan, Xinghua, Xiangcheng, dan sejenisnya dari tabel.
> - Karakter persen (`%`) bekerja secara dinamis karena mampu menampung karakter apa pun dengan panjang berapa pun setelah huruf awal ditentukan.

---

### 4.3 Penyaringan Rentang Nilai (BETWEEN & NOT BETWEEN)

- Operator `BETWEEN` digunakan untuk menyaring baris data yang nilainya berada dalam batas rentang tertentu.
- Jenis data yang dapat difilter menggunakan operator ini meliputi tipe data numerik (_numbers_), teks (_text_), maupun tanggal (_dates_).

#### A. Sifat Inklusif Operator BETWEEN

- Operator `BETWEEN` bersifat **inklusif** (_inclusive_), yang berarti nilai batas awal (_begin value_) dan nilai batas akhir (_end value_) dimasukkan sebagai bagian dari hasil penyaringan.

```sql
SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2;
```

Contoh query untuk menampilkan nama kota beserta populasi dari tabel `City` yang memiliki rentang populasi antara satu juta (1.000.000) sampai dua juta (2.000.000) jiwa:

```sql
SELECT Name, Population FROM City WHERE Population BETWEEN 1000000 AND 2000000;
```

Contoh query untuk menampilkan nama negara, wilayah (_region_), dan angka harapan hidup (_life expectancy_) dari tabel `Country` yang memiliki angka harapan hidup antara 80 sampai 90 tahun:

```sql
SELECT Name, Region, LifeExpectancy FROM Country WHERE LifeExpectancy BETWEEN 80 AND 90;
```

#### B. Operator NOT BETWEEN

- Operator `NOT BETWEEN` bekerja sebaliknya, yaitu mengecualikan rentang nilai yang ditentukan dan hanya menampilkan data yang berada di luar rentang tersebut.

Contoh query menampilkan nama negara, wilayah, dan angka harapan hidup dari tabel `Country` yang angka harapan hidupnya berada di luar rentang 45 sampai 90 tahun:

```sql
SELECT Name, Region, LifeExpectancy FROM Country WHERE LifeExpectancy NOT BETWEEN 45 AND 90;
```

> [!tip] Audio Insight — BETWEEN adalah penyederhanaan dari AND
> - Dosen menekankan bahwa secara konseptual, penulisan operator `BETWEEN` merupakan bentuk penyederhanaan sintaksis yang setara dengan penulisan operator perbandingan matematika manual menggunakan logika `AND`.
> - Sebagai contoh, kondisi `WHERE Population BETWEEN 1000000 AND 2000000` secara fungsional identik dengan penulisan kondisi `WHERE Population >= 1000000 AND Population <= 2000000`. Database akan menghasilkan kumpulan data (_result set_) yang sama persis.

---

### 4.4 Sensitivitas Karakter (Case Sensitivity) pada Penyaringan SQL

- Penanganan sensitivitas huruf dalam eksekusi query dipengaruhi oleh letak komponen dan sistem operasi yang digunakan.

#### A. Aturan Standar Case Sensitivity dalam Database

- Kata kunci dasar atau perintah utama SQL (_SQL keywords_) seperti `SELECT`, `WHERE`, `LIKE`, `AND`, dan `OR` bersifat **case-insensitive** (tidak sensitif huruf). Perintah dapat ditulis dalam huruf besar maupun huruf kecil tanpa memengaruhi fungsionalitas.
- Nama kolom (_column names_) secara umum bersifat **case-insensitive**.
- Nama database dan nama tabel (_database and table names_) sangat bergantung pada sistem operasi yang menjalankan database server:
    - Pada sistem operasi **Linux**, nama database dan tabel bersifat **case-sensitive** (sensitif huruf).
    - Pada sistem operasi **Windows** dan **macOS**, nama database dan tabel bersifat **case-insensitive** (tidak sensitif huruf).

Contoh: kedua query berikut menghasilkan output yang identik persis pada Windows/macOS (kolom & keyword tidak sensitif huruf):

```sql
SELECT * FROM CITY WHERE COUNTRYCODE = 'IDN';
SELECT * FROM City WHERE CountryCode = 'IDN';
```

#### B. Sensitivitas Perbandingan String

- Perbandingan string (_text data and string comparison_) yang dieksekusi di dalam klausa `WHERE` (termasuk operator `LIKE`) sangat bergantung pada kolasi dari kolom tabel (_columns collation_).

> [!warning] Audio Insight — Nama kolom huruf kecil aman, tapi kolasi teks tetap perlu hati-hati
> - Mahasiswa mengonfirmasi bahwa ketika mereka menuliskan nama kolom seperti `district`, `city`, atau `countrycode` menggunakan huruf kecil semua (tanpa kapital), database tetap berhasil mengekstrak data tanpa memicu pesan kesalahan (_error_).
> - Namun, dosen mengingatkan bahwa sensitivitas huruf menjadi sangat krusial saat melakukan pencarian teks spesifik. Misalnya, mencari data teks tertentu di dalam kolom harus ditulis secara hati-hati karena dapat dipengaruhi oleh konfigurasi kolasi bawaan dari kolom bersangkutan di database server.

---

## Bab 5 Pembaruan dan Penghapusan Data (Updating & Deleting)

### 5.1 Perintah Pembaruan Data (UPDATE)

#### A. Konseptual dan Sintaksis Dasar UPDATE

- Perintah `UPDATE` digunakan untuk memodifikasi atau mengubah baris data yang sudah ada (existing records) di dalam suatu tabel database.

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- Klausa `SET` digunakan untuk menentukan kolom yang akan diubah beserta nilai barunya, sedangkan klausa `WHERE` berfungsi menentukan kondisi atau kriteria baris data mana saja yang akan diperbarui nilainya.

#### B. Demonstrasi Kasus dan Penerapan Praktis

- Pembaruan data dapat disimulasikan menggunakan tabel `person` yang telah dibuat pada bab sebelumnya.
- **Kasus 1 (Pembaruan ID Tunggal):** Mengubah data alamat (`Address`) menjadi `'Jln. Melati'` dan kota (`City`) menjadi `'DKI'` untuk record dengan `PersonID` bernilai 1 (Andrew).

```sql
UPDATE person
SET Address = 'Jln. Melati', City = 'DKI'
WHERE PersonID = 1;
```

- Sebelum query dijalankan, alamat Andrew adalah `'Jln. Mawar'` dengan kota `'BSD'`. Setelah query dieksekusi, kolom alamat berubah menjadi `'Jln. Melati'` dan kota menjadi `'DKI'`.
- **Kasus 2 (Pembaruan Multi-Kolom):** Mengubah nama belakang (`LastName`) menjadi `'Andrea'` dan nama depan (`FirstName`) menjadi `'Robert'` untuk baris dengan `PersonID` bernilai 2.

```sql
UPDATE person
SET LastName = 'Andrea', FirstName = 'Robert'
WHERE PersonID = 2;
```

> [!tip] Audio Insight — Verifikasi UPDATE dengan SELECT
> - Melalui alat antarmuka seperti DBeaver atau MySQL Workbench, setelah melakukan perubahan data (`UPDATE`), pengguna dapat menjalankan kueri seleksi untuk memverifikasi perubahan secara instan.
> - Data yang telah diperbarui akan langsung tercermin secara real-time pada tabel hasil kueri seleksi.

```sql
SELECT * FROM person;
```

---

### 5.2 Perintah Penghapusan Data (DELETE)

#### A. Konseptual dan Sintaksis Dasar DELETE

- Perintah `DELETE` digunakan untuk menghapus baris data yang sudah ada (existing records) dari suatu tabel di database.

```sql
DELETE FROM table_name
WHERE condition;
```

- Klausa `WHERE` pada kueri `DELETE` sangat vital karena menentukan kriteria spesifik baris mana yang akan dihapus secara permanen dari tabel.

#### B. Demonstrasi Kasus dan Penerapan Praktis

- **Kasus 1 (Penghapusan Berdasarkan ID):** Menghapus record tertentu di dalam tabel `person` yang memiliki `PersonID` bernilai 4.

```sql
DELETE FROM person
WHERE PersonID = 4;
```

- Setelah kueri dieksekusi, baris data dengan ID bernilai 4 akan terhapus sepenuhnya dari tabel `person`.
- **Kasus 2 (Penghapusan Berdasarkan Usia):** Penghapusan record pada tabel `pelanggan` untuk pelanggan yang memiliki kriteria usia (`Usia`) bernilai 28 tahun.

```sql
DELETE FROM pelanggan
WHERE Usia = 28;
```

- Sebelum kueri dieksekusi, terdapat record pelanggan bernama Joni Saputra dengan usia 28 tahun. Setelah kueri dijalankan, record tersebut terhapus secara permanen.

> [!warning] Audio Insight — DELETE bersifat permanen
> - Setiap operasi `DELETE` yang berhasil dieksekusi di DBMS local host akan langsung menghapus data dari penyimpanan fisik.
> - Pengguna disarankan untuk selalu menjalankan perintah kueri seleksi `SELECT * FROM table_name;` pasca eksekusi `DELETE` untuk mengonfirmasi bahwa baris data yang terhapus sudah tepat dan tidak ada kesalahan penghapusan.

---

### 5.3 Bahaya Operasi Tanpa Klausa WHERE

#### A. Konsekuensi Kelalaian Klausa WHERE

- Mengabaikan penggunaan klausa `WHERE` pada perintah `UPDATE` atau `DELETE` merupakan kesalahan fatal yang dapat merusak integritas data tabel.
- Jika klausa `WHERE` tidak disertakan pada perintah `UPDATE`, maka **seluruh baris** data yang ada di tabel tersebut akan diperbarui secara massal menggunakan nilai baru yang didefinisikan pada klausa `SET`.
- Jika klausa `WHERE` tidak disertakan pada perintah `DELETE`, maka **seluruh baris data** yang ada di dalam tabel tersebut akan dihapus sekaligus, menyisakan tabel dalam keadaan kosong tanpa isi.

|Perintah|Dampak Tanpa Klausa WHERE|Konsekuensi Operasional|
|:--|:--|:--|
|UPDATE|Mengubah nilai kolom yang ditentukan untuk seluruh baris data di tabel.|Kehilangan data historis atau data asli secara permanen pada baris yang seharusnya tidak diubah.|
|DELETE|Menghapus seluruh baris data yang tersimpan di dalam tabel sekaligus.|Mengosongkan isi tabel secara total, meskipun struktur kolom tabel tetap utuh.|

Contoh nyata bahaya yang dimaksud (**JANGAN dijalankan di database berisi data penting**):

```sql
-- BAHAYA: tidak ada klausa WHERE -> SELURUH baris di tabel person ikut ter-update!
UPDATE person
SET City = 'DKI';

-- BAHAYA: tidak ada klausa WHERE -> SELURUH baris di tabel person terhapus!
DELETE FROM person;
```

#### B. Mitigasi dan Best Practice Keamanan Data

- Sebagai praktik terbaik (_best practice_), pengguna disarankan untuk selalu menuliskan klausa `WHERE` terlebih dahulu sebelum mengeksekusi perintah manipulasi data (`UPDATE` dan `DELETE`).
- Melakukan verifikasi data dengan menjalankan kueri `SELECT` menggunakan klausa `WHERE` yang sama sebelum mengubahnya menjadi kueri `UPDATE` atau `DELETE` sangat disarankan guna menghindari kesalahan target data.

> [!warning] Audio Insight — Safe Updates Mode sebagai jaring pengaman
> - Dosen memberikan peringatan keras (_what not to do_) dengan sengaja memberikan tanda komentar (_commented out_) pada klausa `WHERE` di skrip demonstrasi, sebagai peringatan visual bagi mahasiswa mengenai bahaya kelalaian kueri tanpa `WHERE`.
> - Beberapa DBMS modern (seperti MySQL Workbench) secara default mengaktifkan fitur pengaman bernama _Safe Updates Mode_. Fitur ini secara otomatis memblokir eksekusi perintah `UPDATE` atau `DELETE` jika tidak menyertakan klausa `WHERE` yang merujuk pada kolom indeks atau kolom kunci (_Key_), untuk mencegah ketidaksengajaan modifikasi data berskala massal.

---

## Bab 6 Pengurutan Hasil Query (Sorting Result Sets)

### 6.1 Konsep Dasar Pengurutan Data dengan `ORDER BY`

#### A. Pengenalan Klausa `ORDER BY`

- Klausa `ORDER BY` digunakan untuk mengurutkan kumpulan hasil (_result-set_) dari kueri data berdasarkan satu atau lebih kolom.
- Secara default, klausa `ORDER BY` akan mengurutkan data dari nilai terkecil ke terbesar (_ascending_).
- Untuk mengubah urutan dari terbesar ke terkecil (_descending_), kata kunci `DESC` ditambahkan secara eksplisit setelah nama kolom yang bersangkutan.

|Kata Kunci|Arah Pengurutan|Karakteristik Default|
|:--|:--|:--|
|`ASC`|Terkecil ke terbesar (_ascending_)|Merupakan arah pengurutan bawaan (_default_) jika tidak ditentukan secara eksplisit.|
|`DESC`|Terbesar ke terkecil (_descending_)|Harus dituliskan secara eksplisit setelah nama kolom.|

#### B. Sintaksis Dasar `ORDER BY`

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

Contoh konkret (urut abjad A-Z, default ASC):

```sql
SELECT Name FROM City ORDER BY Name;
```

Contoh konkret (urut dari populasi terbesar):

```sql
SELECT Name, Population FROM City ORDER BY Population DESC;
```

> [!warning] Audio Insight — Jangan pernah membungkus nama kolom ORDER BY dengan tanda petik
> - Secara lisan dijelaskan bahwa pengurutan data berbasis teks (string atau karakter) akan diurutkan secara alfabetis dari huruf A hingga Z secara otomatis.
> - Penggunaan tanda petik (quotes) pada nama kolom dalam klausa `ORDER BY` sangat dilarang karena dapat mengacaukan logika pengurutan database (sistem memperlakukannya sebagai literal string biasa, bukan nama kolom fisik). Pastikan menulis nama kolom secara langsung tanpa tanda petik seperti `ORDER BY gnp DESC` agar query berjalan dengan benar.

---

### 6.2 Teknik Pengurutan Tingkat Lanjut (Multiple Columns)

#### A. Pengurutan Berdasarkan Lebih dari Satu Kolom

- Database mendukung pengurutan baris data menggunakan kombinasi beberapa kolom sekaligus.
- Kolom pertama yang didefinisikan akan menjadi prioritas utama pengurutan. Kolom kedua dan berikutnya hanya akan dievaluasi jika terdapat nilai yang sama (_duplicate values_) pada kolom prioritas sebelumnya.

#### B. Implementasi Query Multiple Columns

Contoh kueri berikut mengurutkan baris data berdasarkan kode negara (`CountryCode`) secara _ascending_, dan jika terdapat kode negara yang sama, baris akan diurutkan kembali berdasarkan jumlah populasi (`Population`) dari yang terbesar ke terkecil (_descending_):

```sql
SELECT ID, Name, CountryCode, District, Population
FROM City
ORDER BY CountryCode ASC, Population DESC;
```

> [!tip] Audio Insight — Contoh kasus Afghanistan
> - Dosen mengilustrasikan kasus pengurutan multi-kolom ini pada data kota dengan kode negara Afghanistan (`AFG`). Karena beberapa kota memiliki kode negara `AFG` yang identik, kolom populasi kemudian digunakan sebagai penentu urutan sekunder agar data populasi kota-kota di Afghanistan tersebut tersusun rapi dari populasi terbesar ke terkecil.

---

### 6.3 Kombinasi `ORDER BY` dan `LIMIT` (Analisis Top-N dan Bottom-N)

#### A. Pengambilan Data Teratas (_Top-N_)

- Analisis _Top-N_ digunakan untuk menyaring sejumlah baris tertentu yang memiliki nilai tertinggi di dalam database.
- Hal ini dicapai dengan mengurutkan kolom target secara menurun (`DESC`), kemudian membatasi jumlah baris yang ditampilkan menggunakan klausa `LIMIT`.

```sql
SELECT Name, Population AS populasi
FROM country
ORDER BY Population DESC
LIMIT 5;
```

#### B. Pengambilan Data Terbawah (_Bottom-N_)

- Sebaliknya, analisis _Bottom-N_ ditujukan untuk menyaring sejumlah baris dengan nilai terendah.
- Pengambilan data dilakukan dengan mengurutkan kolom secara menaik (`ASC` atau default), lalu memotong baris keluaran menggunakan klausa `LIMIT`.

```sql
SELECT Name, Population
FROM country
ORDER BY Population ASC
LIMIT 5;
```

> [!tip] Audio Insight — Latihan Top-5 negara berpopulasi terbesar
> - Di dalam sesi tanya jawab latihan praktis, mahasiswa mendemonstrasikan penyelesaian kueri untuk menampilkan 5 negara dengan populasi terbesar di dunia menggunakan database latihan `world`.
> - Kueri tersebut disusun secara efisien dalam satu baris maupun terpisah demi keterbacaan: mengurutkan kolom `Population` secara descending, lalu menempatkan klausa `LIMIT 5` di baris paling akhir dari kueri. Hasil eksekusi kueri ini menampilkan lima negara teratas secara berurutan: Cina, India, Amerika Serikat, Indonesia, dan Brasil.

---

## Bab 7 Fungsi Bawaan Database (Built-in Database Functions)

### 7.1 Klasifikasi Fungsi Bawaan Database

#### A. Definisi dan Peran Fungsi Bawaan

- Database secara umum dilengkapi dengan built-in function (fungsi bawaan) yang dapat dimasukkan secara langsung ke dalam pernyataan SQL.
- Penggunaan fungsi ini secara signifikan mengurangi jumlah data yang perlu diekstraksi dari server, sehingga mempercepat proses pengolahan data.
- Fungsi bawaan SQL dikelompokkan menjadi dua kategori utama berdasarkan cakupan kerjanya:
    - **Aggregate Functions (Fungsi Agregat):** Beroperasi pada sekumpulan nilai (_collection of values_) atau satu kolom secara keseluruhan untuk menghasilkan nilai tunggal (_single value_).
    - **Scalar Functions (Fungsi Skalar):** Beroperasi pada setiap nilai individual (_every individual value_) di baris data secara mandiri.

|Jenis Fungsi|Karakteristik Utama|Contoh Fungsi|
|:--|:--|:--|
|Aggregate Function|Beroperasi pada sekumpulan nilai/kolom, menghasilkan satu nilai tunggal.|SUM, COUNT, AVG, MIN, MAX|
|Scalar Function|Beroperasi secara independen pada setiap nilai baris data individual.|ROUND, LENGTH, UCASE, LCASE|

> [!tip] Audio Insight — Kalkulasi di sisi server, bukan sisi klien
> - Penggunaan fungsi agregat sangat krusial dalam analisis data bisnis skala besar karena kalkulasi dilakukan langsung di sisi server database, bukan di sisi aplikasi klien, sehingga menghemat konsumsi memori dan bandwidth jaringan.

---

### 7.2 Fungsi Agregat Utama (Aggregate Functions)

#### A. Fungsi SUM() dan COUNT()

- **SUM():** Menghitung total jumlah nilai numerik pada suatu kolom spesifik.

```sql
SELECT SUM(column_name) FROM table_name WHERE condition;
```

Contoh praktis (menghitung total populasi di India):

```sql
SELECT SUM(Population) AS Total_Population FROM City WHERE CountryCode = 'IND';
```

- **COUNT():** Mengembalikan jumlah baris data yang cocok dengan kriteria filter yang ditentukan.

```sql
SELECT COUNT(column_name) FROM table_name WHERE condition;
```

Contoh praktis (menghitung jumlah kota di Indonesia):

```sql
SELECT COUNT(Name) AS Total_City FROM City WHERE CountryCode = 'IDN';
```

#### B. Fungsi AVG(), MIN(), dan MAX()

- **AVG():** Menghitung nilai rata-rata dari kolom bertipe numerik.

```sql
SELECT AVG(column_name) FROM table_name WHERE condition;
```

Contoh praktis (menghitung rata-rata populasi kota di Indonesia):

```sql
SELECT AVG(Population) AS Avg_Population FROM City WHERE CountryCode = 'IDN';
```

- **MIN():** Mengambil nilai terkecil/minimum dari kolom yang dipilih.

```sql
SELECT MIN(column_name) FROM table_name WHERE condition;
```

Contoh praktis (mencari populasi kota terkecil di Indonesia):

```sql
SELECT MIN(Population) AS Min_Population FROM City WHERE CountryCode = 'IDN';
```

- **MAX():** Mengambil nilai terbesar/maksimum dari kolom yang dipilih.

```sql
SELECT MAX(column_name) FROM table_name WHERE condition;
```

Contoh praktis (mencari populasi kota terbesar di Indonesia):

```sql
SELECT MAX(Population) AS Max_Population FROM City WHERE CountryCode = 'IDN';
```

|Fungsi Agregat|Deskripsi Teknis|Output|
|:--|:--|:--|
|SUM()|Menghitung akumulasi total nilai numerik dalam satu kolom.|Angka total|
|COUNT()|Menghitung jumlah baris yang memenuhi kondisi spesifik.|Angka bulat (jumlah baris)|
|AVG()|Menghitung rata-rata aritmatika dari nilai numerik kolom.|Angka desimal (rata-rata)|
|MIN()|Menemukan nilai paling rendah/kecil dalam kolom.|Nilai minimum|
|MAX()|Menemukan nilai paling tinggi/besar dalam kolom.|Nilai maksimum|

> [!tip] Audio Insight — NULL diabaikan fungsi agregat, dan statistik populasi kota Indonesia
> - Fungsi agregat mengabaikan nilai NULL dalam kalkulasinya (kecuali COUNT(*) yang menghitung seluruh baris termasuk baris kosong).
> - Sesuai data lisan pada rekaman kuliah, rata-rata populasi kota di wilayah Indonesia (dengan filter CountryCode = 'IDN') adalah sekitar 441.008, dengan populasi kota terkecil bernilai 89.900 dan kota terbesar mencapai 9.604.900.

Fungsi agregat SQL ini punya rekan dekat di dunia Python: lihat `.sum()`, `.mean()`, `.min()`, `.max()` pada Pandas Series/DataFrame di [[Sesi 12 - Python Data Manipulation With Pandas and Numpy]].

---

### 7.3 Fungsi Skalar Utama (Scalar Functions)

#### A. Fungsi ROUND() dan LENGTH()

- **ROUND():** Membulatkan nilai numerik ke jumlah desimal tertentu.

```sql
ROUND(number, decimals)
```

- Parameter `number` wajib diisi (angka yang ingin dibulatkan), sedangkan parameter `decimals` bersifat opsional (jumlah angka di belakang koma. Jika diabaikan, maka nilai akan dibulatkan ke bilangan bulat terdekat tanpa desimal).

Contoh praktis (menghitung kepadatan populasi di Asia Tenggara dengan pembulatan 2 desimal):

```sql
SELECT Name, Region, ROUND(Population/SurfaceArea, 2) AS Population_Density FROM Country WHERE Region = 'Southeast Asia';
```

- **LENGTH():** Mengembalikan panjang karakter dari suatu string/teks (dihitung dalam satuan bytes).

```sql
LENGTH(string)
```

Contoh praktis (menghitung jumlah panjang karakter nama negara di Asia Tenggara dan diurutkan menurun):

```sql
SELECT Name, LENGTH(Name) AS Length_Name FROM Country WHERE Region = 'Southeast Asia' ORDER BY Length_Name DESC;
```

#### B. Fungsi Manipulasi Huruf (UCASE/UPPER dan LCASE/LOWER)

- **UCASE() / UPPER():** Mengonversi seluruh string teks menjadi huruf besar/kapital secara penuh.

```sql
UCASE(text)
```

Contoh praktis:

```sql
SELECT UCASE(Name), Population FROM Country WHERE Region = 'Southeast Asia';
```

- **LCASE() / LOWER():** Mengonversi seluruh string teks menjadi huruf kecil secara penuh.

```sql
LCASE(text)
```

Contoh praktis:

```sql
SELECT LCASE(Name), Population FROM Country WHERE Region = 'Southeast Asia';
```

|Fungsi Skalar|Parameter Wajib|Hasil Operasi|
|:--|:--|:--|
|ROUND()|Angka, [Jumlah Desimal]|Nilai angka yang sudah dibulatkan.|
|LENGTH()|Teks/String|Panjang string dalam satuan byte.|
|UCASE() / UPPER()|Teks/String|Teks dalam bentuk huruf kapital penuh.|
|LCASE() / LOWER()|Teks/String|Teks dalam bentuk huruf kecil penuh.|

> [!warning] Audio Insight — LENGTH() itu fungsi skalar, bukan agregat (dipakai di WHERE, bukan HAVING)
> - Fungsi skalar dapat dijalankan langsung di klausa `SELECT` untuk memformat tampilan data, atau di dalam klausa `WHERE` untuk melakukan penyaringan dinamis.
> - Dari sesi tanya jawab kuliah, mahasiswa sempat mencoba menggunakan fungsi `LENGTH` dikombinasikan dengan `GROUP BY` dan `HAVING` secara keliru. Dosen menegaskan bahwa fungsi `LENGTH` adalah fungsi skalar, bukan fungsi agregat, sehingga penyaringan berdasarkan panjang karakter nama (contoh: mencari negara yang panjang namanya sama dengan 6) harus ditulis menggunakan klausa `WHERE` secara langsung, bukan klausa `HAVING`.
> - Contoh penulisan penyaringan yang benar untuk mencari nama negara dengan panjang 6 karakter dan berakhiran 'o':
>
> ```sql
> SELECT Name FROM Country WHERE LENGTH(Name) = 6 AND Name LIKE '%o';
> ```
>
> Ini adalah petunjuk penting yang akan sangat relevan pada pembahasan `GROUP BY` vs `HAVING` di bab berikutnya: **`WHERE` untuk baris individual (termasuk hasil fungsi skalar), `HAVING` untuk grup hasil fungsi agregat.**

---

## Bab 8 Pengelompokan Data (GROUP BY)

### A. Konsep dan Mekanisme GROUP BY

- Klausa `GROUP BY` digunakan untuk mengelompokkan baris data yang memiliki nilai yang sama ke dalam baris rangkuman (_summary rows_), seperti "menghitung jumlah kota di setiap negara".
- Klausa ini sering kali digunakan bersama dengan fungsi agregat (`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`) untuk mengagregasi hasil set berdasarkan satu atau beberapa kolom.
- Urutan sintaksis standar SQL:

```sql
SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) ORDER BY column_name(s);
```

### B. Demonstrasi Kasus GROUP BY

- **Kasus 1 (Menghitung jumlah kota untuk setiap kode negara):**

```sql
SELECT COUNT(ID), CountryCode FROM City GROUP BY CountryCode;
```

- **Kasus 2 (Menghitung rata-rata populasi kota di setiap distrik di Indonesia):**

```sql
SELECT AVG(Population), District FROM City WHERE CountryCode = 'IDN' GROUP BY District;
```

- **Kasus 3 (Menggabungkan GROUP BY dengan Alias `AS`):** Menggunakan `AS` untuk memberikan nama kolom baru yang lebih representatif pada hasil query agregasi.

```sql
SELECT AVG(Population) AS Rata_rata, District AS Provinsi FROM City WHERE CountryCode = 'IDN' GROUP BY District;
```

> [!warning] Audio Insight — Kolom non-agregat di SELECT wajib ada di GROUP BY
> - Klausa `GROUP BY` memecah data menjadi kelompok-kelompok kecil secara logis sebelum fungsi agregat dijalankan. Kolom yang ditulis di dalam klausa `SELECT` (non-agregat) harus dicantumkan pula secara konsisten pada klausa `GROUP BY` untuk mencegah terjadinya galat pembacaan skema data pada sistem DBMS.

**Penting: `GROUP BY`-lah yang benar-benar mengelompokkan baris menjadi grup.** Klausa `HAVING` di bab berikutnya **tidak** melakukan pengelompokan apa pun — ia hanya menyaring grup-grup yang *sudah* dibentuk oleh `GROUP BY`. Lihat penjelasan urutan eksekusi lengkap di [[#Bab 9 Penyaringan Grup Data (HAVING)]] di bawah.

Konsep pengelompokan ini identik dengan method `.groupby()` pada Pandas DataFrame — lihat [[Sesi 12 - Python Data Manipulation With Pandas and Numpy]] untuk perbandingan langsungnya (`GROUP BY District` di SQL ≈ `df.groupby('District')` di Pandas).

---

## Bab 9 Penyaringan Grup Data (HAVING)

### A. Definisi dan Sintaksis Klausa HAVING

- Klausa `HAVING` memiliki fungsi yang serupa dengan klausa `WHERE`, yaitu menyaring hasil set data. Namun, perbedaan mendasarnya adalah **`HAVING` digunakan khusus untuk menyaring hasil setelah proses pengelompokan (`GROUP BY`) dilakukan**.
- Urutan sintaksis lengkap yang menggabungkan seluruh klausa utama:

```sql
SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) HAVING group_condition ORDER BY column_name(s);
```

### B. Contoh Implementasi HAVING

- **Kasus 1 (Menampilkan rata-rata populasi distrik di Indonesia yang nilainya di atas 500.000):** Kueri ini tidak dapat menggunakan `WHERE` untuk memfilter rata-rata karena nilai rata-rata baru dihitung setelah baris data dikelompokkan per distrik.

```sql
SELECT AVG(Population) AS Rata_rata, District AS Provinsi
FROM CITY
WHERE CountryCode = 'IDN'
GROUP BY District
HAVING Rata_rata > 500000;
```

- **Kasus 2 (Menyaring kolom grup itu sendiri menggunakan HAVING):** Meskipun penyaringan nama provinsi sebaiknya diletakkan di `WHERE` demi efisiensi, `HAVING` juga mampu melakukan filter langsung pada kolom grup, misalnya mencari provinsi yang diawali dengan huruf 'K'.

```sql
SELECT AVG(Population) AS Rata_rata, District AS Provinsi
FROM CITY
WHERE CountryCode = 'IDN'
GROUP BY District
HAVING Provinsi LIKE 'K%';
```

### C. Tabel Perbedaan Antara WHERE dan HAVING

|Karakteristik|Klausa WHERE|Klausa HAVING|
|:--|:--|:--|
|**Tahap Eksekusi**|Dieksekusi sebelum baris data dikelompokkan (_before grouping_).|Dieksekusi setelah baris data dikelompokkan (_after grouping_).|
|**Fungsi Agregat**|Tidak dapat digunakan bersama fungsi agregat (misal: dilarang menulis `WHERE AVG(Population) > 100`).|Sangat kompatibel dan digunakan untuk menyaring fungsi agregat (misal: `HAVING Rata_rata > 500000`).|
|**Objek Penyaringan**|Menyaring baris data individual secara langsung dari tabel fisik.|Menyaring kelompok/grup data hasil ringkasan agregasi.|

> [!warning] Audio Insight — Perbedaan mendasar WHERE vs HAVING (poin krusial)
> - Dari tanya jawab kuliah, ketika mahasiswa menanyakan perbedaan mendasar antara `HAVING` dan `WHERE`, dosen memberikan penjelasan sebagai berikut:
>   - `WHERE` diletakkan **sebelum** `GROUP BY` untuk menyaring baris-baris data dari tabel asal terlebih dahulu. Hanya baris yang lolos penyaringan `WHERE` yang akan masuk ke tahap pengelompokan.
>   - `HAVING` diletakkan **setelah** `GROUP BY` untuk menyaring kelompok-kelompok data yang sudah terbentuk berdasarkan hasil perhitungan agregasi.
>   - Penggunaan `WHERE` jauh lebih efisien untuk kolom non-agregat karena membatasi jumlah data yang diproses sejak awal, sementara `HAVING` ideal digunakan ketika kriteria filter melibatkan hasil perhitungan fungsi agregat seperti `SUM()`, `AVG()`, atau `COUNT()`.

### D. Penelusuran Langkah-demi-Langkah: Urutan Eksekusi Sesungguhnya

Ini adalah titik yang paling sering membingungkan: **`HAVING` tidak melakukan pengelompokan — `GROUP BY` yang melakukannya.** `HAVING` hanya seorang "penjaga pintu" yang menyaring grup-grup yang sudah jadi.

SQL ditulis dalam urutan `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY`, tetapi **dieksekusi** oleh mesin database dalam urutan logis yang berbeda:

| Urutan Eksekusi | Klausa | Apa yang Terjadi |
|:--:|:--|:--|
| 1 | `FROM` | Ambil seluruh baris dari tabel `CITY`. |
| 2 | `WHERE` | Saring baris — hanya sisakan baris dengan `CountryCode = 'IDN'`. (Baris individual, belum ada grup.) |
| 3 | `GROUP BY` | Kelompokkan baris-baris yang lolos `WHERE` tadi ke dalam grup berdasarkan `District` — **inilah langkah yang benar-benar membentuk grup.** |
| 4 | *(agregasi)* | Hitung `AVG(Population)` untuk **masing-masing grup** District. |
| 5 | `HAVING` | Saring **grup** (bukan baris) — buang grup District mana pun yang nilai `AVG(Population)`-nya ≤ 500000. `HAVING` tidak pernah menyentuh baris individual, ia hanya melihat hasil agregat per grup. |
| 6 | `SELECT` | Pilih kolom apa yang akan ditampilkan dari grup-grup yang lolos. |
| 7 | `ORDER BY` | Urutkan hasil akhir. |

Contoh konkret ditelusuri langkah demi langkah, menggunakan kueri Kasus 1 di atas:

```sql
SELECT AVG(Population) AS Rata_rata, District AS Provinsi
FROM CITY
WHERE CountryCode = 'IDN'
GROUP BY District
HAVING Rata_rata > 500000;
```

1. `FROM CITY` — mulai dari seluruh baris tabel `CITY` (kota di seluruh dunia).
2. `WHERE CountryCode = 'IDN'` — buang semua baris kota yang bukan Indonesia. Sisa: hanya baris-baris kota Indonesia.
3. `GROUP BY District` — baris-baris kota Indonesia yang tersisa dikelompokkan per provinsi (misal semua kota di "Jawa Barat" jadi satu grup, semua kota di "Jawa Timur" jadi grup lain, dst).
4. Untuk **setiap grup provinsi**, database menghitung `AVG(Population)` — jadi setiap grup kini punya satu angka rata-rata.
5. `HAVING Rata_rata > 500000` — grup provinsi mana pun yang rata-ratanya ≤ 500.000 dibuang dari hasil. Grup yang di atas 500.000 tetap ada.
6. `SELECT AVG(Population) AS Rata_rata, District AS Provinsi` — tampilkan hanya dua kolom ini dari grup-grup yang lolos filter `HAVING`.

**Kesimpulan kunci:** jika Anda ingin menyaring baris mentah sebelum dikelompokkan → pakai `WHERE`. Jika Anda ingin menyaring berdasarkan hasil hitungan agregat (`AVG`, `SUM`, `COUNT`, dst) dari grup yang sudah terbentuk → pakai `HAVING`. `GROUP BY` sendiri tidak pernah menyaring apa pun — tugasnya murni mengelompokkan.

---

## Bab 10 Fungsi Terkait Tanggal dan Waktu (Date and Time Functions)

### 10.1 Format Penyimpanan Tanggal dan Waktu Standar

#### A. Tipe Data dan Format Standar

- Sistem database memiliki tipe data khusus yang dirancang untuk menyimpan informasi tanggal (date) dan waktu (time) secara presisi.
- Format standar penyimpanan data tanggal dan waktu meliputi:
    - **DATE**: Disimpan menggunakan format `YYYYMMDD` (Tahun-Bulan-Hari).
    - **TIME**: Disimpan menggunakan format `HHMMSS` (Jam-Menit-Detik).
    - **TIMESTAMP**: Disimpan menggunakan format `YYYYXXDDHHMMSSZZZZZZ` yang mencakup komponen tanggal, waktu, hingga mikrodetik atau zona waktu.

|Tipe Data|Format Standar|Deskripsi|
|:--|:--|:--|
|DATE|YYYYMMDD|Menyimpan data tanggal tanpa komponen waktu.|
|TIME|HHMMSS|Menyimpan data waktu (jam, menit, detik) secara mandiri.|
|TIMESTAMP|YYYYXXDDHHMMSSZZZZZZ|Menyimpan data kombinasi tanggal dan waktu yang sangat detail.|

> [!tip] Audio Insight — Kenapa perlu tipe data tanggal/waktu khusus
> - Database menggunakan tipe data khusus ini agar operasi penyaringan, pengurutan, dan manipulasi waktu dapat dilakukan secara efisien.
> - Representasi data waktu dalam format standar memudahkan integrasi data lintas platform tanpa risiko salah interpretasi zona waktu atau penulisan tanggal.

---

### 10.2 Fungsi Ekstraksi Komponen Tanggal dan Waktu

#### A. Ekstraksi Nilai Numerik

- Fungsi bawaan ekstraksi digunakan untuk mengambil satu komponen numerik spesifik dari suatu kolom tanggal atau waktu.
- Daftar fungsi ekstraksi numerik yang didukung:
    - `YEAR()`: Mengekstrak komponen tahun dalam bentuk angka integer.
    - `MONTH()`: Mengekstrak komponen bulan (1 hingga 12).
    - `DAY()` atau `DAYOFMONTH()`: Mengekstrak komponen hari dalam bulan (1 hingga 31).
    - `DAYOFWEEK()`: Mengekstrak indeks hari dalam seminggu.
    - `DAYOFYEAR()`: Mengekstrak urutan hari dalam setahun (1 hingga 366).
    - `WEEK()`: Mengekstrak urutan minggu dalam setahun.
    - `HOUR()`: Mengekstrak komponen jam (0 hingga 23).
    - `MINUTE()`: Mengekstrak komponen menit (0 hingga 59).
    - `SECOND()`: Mengekstrak komponen detik (0 hingga 59).

Contoh Kasus Penggunaan `YEAR()`: Menghitung rata-rata nilai transaksi harian per tahun dari tabel pembayaran (`payment`):

```sql
SELECT YEAR(payment_date) AS Year_Sales, AVG(amount) AS Total_Amount_Yearly
FROM PAYMENT
GROUP BY Year_Sales;
```

Contoh Kasus Penggunaan `DAY()`: Menampilkan ID pelanggan dan komponen hari pembayaran dari tabel `payment` untuk transaksi dengan nilai di atas US$ 11:

```sql
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

Contoh gabungan yang menunjukkan **seluruh** fungsi ekstraksi lain dalam satu query (agar setiap fungsi punya contoh nyata yang benar-benar berjalan):

```sql
SELECT
    payment_date,
    YEAR(payment_date)       AS Tahun,
    MONTH(payment_date)      AS Bulan,
    DAY(payment_date)        AS Hari,          -- setara DAYOFMONTH(payment_date)
    DAYOFMONTH(payment_date) AS Hari_Dalam_Bulan,
    DAYOFWEEK(payment_date)  AS Indeks_Hari_Minggu,
    DAYOFYEAR(payment_date)  AS Urutan_Hari_Setahun,
    WEEK(payment_date)       AS Minggu_Ke,
    HOUR(payment_date)       AS Jam,
    MINUTE(payment_date)     AS Menit,
    SECOND(payment_date)     AS Detik
FROM PAYMENT
LIMIT 5;
```

> [!tip] Audio Insight — Output integer memudahkan GROUP BY
> - Komponen tanggal yang diekstrak menggunakan fungsi seperti `YEAR()` akan menghasilkan nilai bertipe integer (angka bulat). Hal ini memungkinkan data hasil ekstraksi langsung dikelompokkan menggunakan klausa `GROUP BY` untuk kepentingan analisis tren tahunan atau bulanan.
> - Indentasi dalam kueri SQL bersifat opsional (tidak wajib seperti Python), namun sangat dianjurkan untuk mempermudah pembacaan baris instruksi `SELECT`, `FROM`, `WHERE`, dan `GROUP BY`.

---

### 10.3 Fungsi Representasi Teks (Nama Hari dan Bulan)

#### A. Konversi Tanggal ke Nama

- Database menyediakan fungsi khusus untuk memformat komponen tanggal menjadi nama tekstual dalam bahasa Inggris:
    - `DAYNAME()`: Mengonversi nilai tanggal menjadi nama hari dalam seminggu (seperti _Monday_, _Tuesday_, _Wednesday_, _Thursday_, _Friday_, _Saturday_, _Sunday_).
    - `MONTHNAME()`: Mengonversi nilai tanggal menjadi nama bulan dalam setahun (seperti _January_, _February_, _March_, _April_, _May_, _June_, _July_, _August_, _September_, _October_, _November_, _December_).

Contoh Kasus Penggunaan `DAYNAME()`: Menghitung rata-rata nilai transaksi berdasarkan nama hari pembayaran dan mengurutkannya dari yang terkecil:

```sql
SELECT AVG(amount) AS Average_Amount, DAYNAME(payment_date) AS Day
FROM PAYMENT
GROUP BY DAYNAME(payment_date)
ORDER BY Average_Amount;
```

Contoh Kasus Penggunaan `MONTHNAME()`: Menghitung rata-rata nilai transaksi berdasarkan nama bulan pembayaran dari tabel `payment`:

```sql
SELECT AVG(amount) AS Average_Amount, MONTHNAME(payment_date) AS Month_Name
FROM PAYMENT
GROUP BY Month_Name
ORDER BY Average_Amount;
```

|Fungsi|Contoh Output|Deskripsi Kegunaan|
|:--|:--|:--|
|DAYNAME(date)|'Saturday', 'Monday'|Mengonversi tanggal ke representasi teks nama hari.|
|MONTHNAME(date)|'August', 'February'|Mengonversi tanggal ke representasi teks nama bulan.|

> [!tip] Audio Insight — Representasi teks untuk kebutuhan laporan manajerial
> - Fungsi representasi teks sangat bermanfaat ketika menyajikan data kepada pihak manajerial atau direktur, karena format nama hari (seperti _Saturday_) jauh lebih mudah dipahami secara visual dibandingkan representasi angka indeks hari.

---

### 10.4 Aritmatika Tanggal (Date Arithmetic)

#### A. Operasi Penjumlahan dan Pengurangan Tanggal

- Aritmatika tanggal (_Date Arithmetic_) merupakan proses melakukan operasi matematika langsung (penambahan atau pengurangan) terhadap nilai tanggal untuk menghasilkan tanggal baru.
- Penambahan nilai integer pada objek tanggal secara otomatis akan menggeser tanggal tersebut ke beberapa hari ke depan.

Contoh Kasus Penjumlahan Tanggal: Menampilkan nama hari satu hari setelah tanggal pembayaran asli (`One_Day_After_Payment`) pada tabel `payment` untuk transaksi yang diproses oleh staf dengan ID 1 dan nilai transaksi di atas US$ 11:

```sql
SELECT Customer_id, Amount, DAYNAME(DATE(payment_date) + 1) AS One_Day_After_Payment
FROM PAYMENT
WHERE staff_id = 1 AND amount > 11;
```

Sebaliknya, pengurangan bekerja dengan logika yang sama untuk menggeser tanggal ke belakang. Contoh menampilkan nama hari satu hari **sebelum** tanggal pembayaran:

```sql
SELECT Customer_id, Amount, DAYNAME(DATE(payment_date) - 1) AS One_Day_Before_Payment
FROM PAYMENT
WHERE staff_id = 1 AND amount > 11;
```

|Operasi|Contoh Sintaksis|Hasil Fungsional|
|:--|:--|:--|
|Penambahan Tanggal|`DATE(payment_date) + 1`|Menghasilkan tanggal baru yang bergeser 1 hari ke depan.|
|Pengurangan Tanggal|`DATE(payment_date) - 1`|Menghasilkan tanggal baru yang bergeser 1 hari ke belakang.|

> [!tip] Audio Insight — Konversi ke DATE() dulu sebelum aritmatika, waspada overflow
> - Operasi aritmatika tanggal dapat dilakukan dengan mengonversi kolom waktu/timestamp ke tipe data tanggal murni terlebih dahulu menggunakan fungsi `DATE(payment_date)`, baru kemudian ditambahkan nilai numerik integer (misalnya `+ 1` untuk bergeser ke hari berikutnya).
> - Perlu diperhatikan batasan dalam operasi aritmatika sederhana ini agar tidak terjadi _overflow_ jika nilai penambah hari terlalu besar di luar batasan penanganan memori tipe datanya.

---

## Bab 11 Subquery dan Kueri Bersarang (Sub Queries and Nested SELECT)

### 11.1 Definisi dan Penempatan Subquery

#### A. Konsep Dasar Subquery

- Subquery atau kueri bersarang didefinisikan sebagai sebuah kueri SQL yang berada di dalam kueri SQL lainnya.
- Kueri yang berada di bagian dalam (inner query) dieksekusi terlebih dahulu, kemudian hasilnya digunakan oleh kueri yang berada di bagian luar (outer query) untuk menyelesaikan operasi utamanya.
- Subquery dapat disisipkan atau bersarang di dalam berbagai jenis pernyataan SQL utama, termasuk SELECT, INSERT, UPDATE, atau DELETE, serta dapat disisipkan di dalam subquery lainnya.

|Konsep|Deskripsi Fungsional|
|:--|:--|
|Subquery|SQL query yang ditulis di dalam kueri SQL lain yang lebih besar.|
|Outer Query|Kueri utama di tingkat luar yang memanfaatkan hasil dari subquery.|
|Inner Query|Sebutan lain dari subquery yang dieksekusi terlebih dahulu oleh mesin database.|

#### B. Aturan Penulisan dan Sintaksis Umum

- Subquery umumnya diletakkan di dalam tanda kurung `()` untuk memisahkannya secara jelas dari kueri luar.
- Hasil dari subquery dapat berupa nilai tunggal (skalar), satu kolom dengan beberapa baris (list), atau sebuah tabel virtual (dataset).

> [!tip] Audio Insight — Kapan subquery dibutuhkan, dan indentasi opsional
> - Subquery digunakan ketika data kueri luar bergantung pada hasil perhitungan dinamis yang tidak dapat diperoleh secara langsung dengan kueri satu tingkat biasa.
> - Penggunaan indentasi saat menulis subquery sangat disarankan untuk memudahkan pembacaan struktur logika kueri bersarang, meskipun secara teknis penulisan indentasi ini tidak wajib bagi mesin MySQL (berbeda dengan bahasa pemrograman Python yang mewajibkan indentasi).

---

### 11.2 Subquery dalam Klausa WHERE

#### A. Evaluasi Kondisi Menggunakan Fungsi Agregasi

- Salah satu batasan utama SQL adalah ketidakmampuan untuk mengevaluasi atau menaruh fungsi agregat seperti `AVG()`, `MIN()`, atau `MAX()` secara langsung di dalam klausa penyaringan `WHERE` biasa.
- Sebagai solusinya, subquery digunakan di dalam klausa `WHERE` untuk menghitung nilai agregat tersebut terlebih dahulu, sebelum hasilnya dievaluasi oleh klausa `WHERE` pada kueri utama.

|Jenis Operasi|Sintaksis Standar yang Salah|Solusi Sintaksis Menggunakan Subquery|
|:--|:--|:--|
|Filter Rata-rata|`WHERE Salary < AVG(Salary)`|`WHERE Salary < (SELECT AVG(Salary) FROM Employees)`|

#### B. Studi Kasus dan Penerapan Praktis

- **Kasus 1 (Data Gaji Karyawan):** Untuk menampilkan data karyawan yang gajinya di bawah rata-rata gaji seluruh karyawan:

```sql
SELECT ID, NAME, SALARY
FROM EMPLOYEE
WHERE SALARY < (SELECT AVG(SALARY) FROM employees);
```

- **Kasus 2 (Data Usia Karyawan):** Menampilkan nama depan, nama belakang, dan usia karyawan dari tabel `new_employees` yang memiliki usia di atas rata-rata usia seluruh karyawan:

```sql
SELECT First_Name, Last_Name, Age
FROM new_employees
WHERE Age > (SELECT AVG(Age) FROM new_employees);
```

> [!tip] Audio Insight — Subquery WHERE mengembalikan satu nilai skalar
> - Pada Kasus 2, subquery `(SELECT AVG(Age) FROM new_employees)` akan mengembalikan satu nilai numerik tunggal (yaitu nilai rata-rata usia). Nilai tersebut kemudian bertindak sebagai parameter pembanding dinamis untuk klausa `WHERE Age >` pada kueri utama.

---

### 11.3 Subquery dalam Daftar Kolom (Scalar Subquery)

#### A. Substitusi Nama Kolom dengan Nilai Tunggal

- Subquery dapat digunakan di dalam daftar pilihan kolom pada klausa `SELECT` untuk mensubstitusi atau menambahkan kolom ekspresi baru (_column expressions_).
- Setiap subquery yang ditempatkan pada daftar kolom harus mengembalikan satu nilai tunggal (_scalar_) per baris kueri utama.

|Istilah|Karakteristik Utama|
|:--|:--|
|Column Expressions|Penggantian atau penambahan nama kolom dengan subquery untuk menghasilkan kolom dinamis baru.|
|Scalar Output|Syarat wajib subquery di klausa `SELECT` yang hanya boleh menghasilkan satu sel data (satu kolom dan satu baris) untuk setiap baris kueri utama.|

#### B. Contoh Kasus Kolom Dinamis

**Kasus Analisis Rentang Usia:** Menampilkan nama depan karyawan, nama belakang, usia saat ini, serta kolom tambahan berisi usia termuda dan usia tertua dari seluruh data di tabel `new_employees`:

```sql
SELECT First_Name, Last_Name, Age,
       (SELECT MIN(Age) FROM new_employees) AS Youngest,
       (SELECT MAX(Age) FROM new_employees) AS Oldest
FROM new_employees;
```

> [!tip] Audio Insight — Membandingkan nilai baris dengan nilai ekstrem tabel tanpa GROUP BY
> - Subquery yang digunakan pada daftar kolom ini sangat membantu saat pengguna ingin membandingkan nilai individual setiap baris dengan nilai ekstrem (seperti nilai minimum atau maksimum) dari keseluruhan tabel secara berdampingan tanpa perlu melakukan operasi pengelompokan `GROUP BY` yang mereduksi baris data asli.

---

### 11.4 Subquery dalam Klausa FROM (Derived Tables)

#### A. Pembuatan Tabel Virtual Sementara

- Subquery yang diletakkan di dalam klausa `FROM` berfungsi menggantikan posisi nama tabel fisik. Konsep ini dikenal sebagai _Derived Tables_ atau _Table Expressions_.
- Subquery ini menghasilkan sekumpulan baris dan kolom yang bertindak sebagai tabel virtual sementara untuk diproses lebih lanjut oleh kueri utama.

|Terminologi|Karakteristik Utama|
|:--|:--|
|Derived Tables|Tabel sementara yang dihasilkan dari eksekusi subquery di dalam klausa `FROM`.|
|Table Expressions|Istilah lain untuk kueri bersarang yang menghasilkan struktur dataset tabular sementara di dalam klausa kueri utama.|

#### B. Aturan Wajib Alias (AS) di MySQL

- Dalam sistem DBMS MySQL, setiap _Derived Table_ yang dihasilkan dari subquery pada klausa `FROM` **wajib** diberikan nama alias menggunakan kata kunci `AS` (atau ditulis langsung setelah tanda kurung tutup subquery).
- Jika alias ini dilewatkan, mesin MySQL akan memunculkan pesan error teknis dan kueri gagal dieksekusi.

**Sintaksis Standar dengan Alias:**

```sql
SELECT * FROM
(SELECT ID, NAME, DEPARTMENT_ID FROM employees) AS ALL_EMPLOYEES;
```

**Contoh Studi Kasus Biodata:** Menampilkan seluruh data dari tabel sementara biodata karyawan yang disaring dari tabel asli `employees`:

```sql
SELECT * FROM
(SELECT First_name, Last_name, Gender, Birth_date FROM employees) AS Employee_Biodata;
```

> [!warning] Audio Insight — Alias wajib pada Derived Table, meski boleh singkat
> - Penamaan alias pada _Derived Table_ sangat penting bagi manajemen memori database MySQL agar kueri utama dapat merujuk kembali ke tabel hasil filter sementara tersebut dengan nama yang jelas.
> - Meskipun penulisan alias ini diwajibkan oleh sintaksis MySQL, alias tersebut tidak harus selalu dipanggil secara aktif di bagian kueri utama jika memang tidak diperlukan. Pengguna dapat menuliskan alias yang singkat dan cepat (misalnya `AS SA` atau `AS ST` seperti dicontohkan dosen) agar kueri dapat dieksekusi tanpa error.

Aturan "alias wajib" ini juga muncul kembali dalam bentuk yang lebih ketat pada Self JOIN di [[Sesi 10 - SQL Working With Multiple Tables]] — di sana, melewatkan alias benar-benar menyebabkan error sintaksis, bukan sekadar rekomendasi.

---

## Bab 12 Interface dan Koneksi Database

### 12.1 Parameter Koneksi Database

#### A. Parameter Utama Koneksi

- Untuk menghubungkan (_connect_) sistem antarmuka ke database server, diperlukan beberapa parameter utama yang harus didefinisikan secara tepat.
- Kegagalan pengisian atau ketidakcocokan salah satu parameter akan menyebabkan koneksi ditolak oleh database server.

| Parameter | Deskripsi Teknis                                                        | Nilai Standar / Default                           |
| :-------- | :---------------------------------------------------------------------- | :------------------------------------------------ |
| DBMS      | Tipe Database Management System yang ditargetkan untuk koneksi.         | MySQL, PostgreSQL, SQLite                         |
| Host      | Alamat jaringan server tempat database fisik dideploy dan dijalankan.   | `localhost` atau `127.0.0.1` (untuk server lokal) |
| Port      | Pintu masuk komunikasi data digital spesifik untuk layanan DBMS.        | `3306` (MySQL), `5432` (PostgreSQL)               |
| Username  | Nama identitas akun pengguna yang memiliki hak akses di database.       | `root` (Super Admin bawaan MySQL)                 |
| Password  | Kunci keamanan autentikasi untuk memverifikasi akses dari user terkait. | Ditentukan saat instalasi awal                    |

#### B. Mekanisme Keamanan Koneksi

- Database server mengamankan data dengan membatasi koneksi hanya dari pengguna terverifikasi melalui pencocokan kombinasi Host, Username, dan Password.
- Hak akses (privilege) dapat diatur per user untuk membatasi query yang diizinkan pada objek database tertentu.

> [!tip] Audio Insight — Parameter wajib diminta ke administrator database
> - Ketika ingin terhubung ke database dalam lingkungan kerja profesional, Anda wajib meminta informasi lengkap mengenai tipe DBMS yang digunakan, alamat Host, nomor Port yang terbuka, serta kredensial Username dan Password kepada tim administrator database. Tanpa parameter ini, koneksi tidak akan pernah bisa terjalin.

---

### 12.2 Perkakas (Tools) Mengakses Database

#### A. Perbandingan GUI (Graphical User Interface) vs CLI (Command Line Interface)

- Akses ke database dapat dilakukan menggunakan dua pendekatan utama berdasarkan jenis antarmukanya.

|Jenis Perkakas|Nama Perkakas|Karakteristik Utama|
|:--|:--|:--|
|GUI (Graphical User Interface)|MySQL Workbench|Perkakas visual resmi (_official_) yang dikembangkan khusus untuk mengelola database MySQL secara eksklusif.|
|GUI (Graphical User Interface)|DBeaver|Perkakas visual multi-database yang mendukung banyak tipe DBMS seperti MySQL, PostgreSQL, SQLite, DB2, Greenplum, dan MariaDB.|
|CLI (Command Line Interface)|MySQL 8.0 Command Line Client|Antarmuka berbasis teks murni (terminal/command prompt) untuk mengeksekusi perintah database dengan mengetik baris perintah langsung.|

#### B. Konfigurasi Koneksi pada GUI (DBeaver & MySQL Workbench)

- Langkah praktis pembuatan koneksi baru pada perkakas GUI:
    - **MySQL Workbench:**
        1. Klik ikon tambah (`+`) pada halaman utama (_Add Connection_).
        2. Tentukan _Connection Name_ (misalnya: "Purwadika MySQL").
        3. Masukkan parameter koneksi (Host: `127.0.0.1` atau `localhost`, Port: `3306`, Username: `root`).
        4. Saat membuka koneksi (_Open Connection_), masukkan password MySQL Anda ketika diminta.
    - **DBeaver:**
        1. Klik kanan pada panel _Database Navigator_, pilih **Create** -> **Connection**.
        2. Pilih ikon **MySQL**, lalu klik _Next_.
        3. Isi parameter koneksi (Server Host: `localhost`, Port: `3306`, Username: `root`, Password sesuai konfigurasi lokal Anda).
        4. Klik **Test Connection** untuk memverifikasi fungsionalitas koneksi sebelum menyimpannya dengan menekan tombol _Finish_.

> [!tip] Audio Insight — GUI sebagai lapisan antarmuka, dan sifat SQL yang indentation-insensitive
> - **Kelebihan GUI dibanding CLI:** Penggunaan CLI/terminal untuk melihat database dan tabel yang jumlahnya banyak dinilai sangat menyulitkan bagi pemula karena output ditampilkan dalam format teks murni yang padat dan kaku. Perkakas GUI menawarkan visualisasi yang jauh lebih terstruktur dan mudah dinavigasi.
> - **Konsep Arsitektur Interface:** Perkakas GUI (DBeaver/MySQL Workbench) pada dasarnya hanyalah lapisan antarmuka (_interface/client_) yang bertindak sebagai jembatan untuk menulis (_write_) dan membaca (_retrieve_) data dari database server fisik. Jika Anda mengedit data menggunakan MySQL Workbench, data di server fisik akan langsung berubah. Sehingga ketika keesokan harinya Anda membuka DBeaver untuk membaca database yang sama, data hasil pembaruan tersebut akan langsung terbaca secara konsisten.
> - **Tujuan Penggunaan Perkakas:** Perkakas database GUI dirancang untuk kebutuhan pengerjaan teknis pengembang (_developer_) atau analis data (_data analyst_) untuk mempermudah eksekusi query. Di dunia kerja nyata, tabel tabular mentah dari database GUI ini tidak disajikan langsung ke level eksekutif/direktur karena sulit dipahami secara instan. Data tersebut harus diekstraksi terlebih dahulu lalu divisualisasikan menggunakan alat visualisasi data eksternal (lihat [[Sesi 13 - Data Visualization]]).
> - **Karakteristik Aturan Penulisan Sintaks SQL:** Penulisan query SQL bersifat fleksibel terhadap spasi, baris baru, dan indentasi (_indentation insensitive_). Hal ini berbeda dengan bahasa pemrograman Python yang mewajibkan indentasi (_indentation sensitive_). Pengaturan spasi dan baris baru pada SQL semata-mata dilakukan untuk mempermudah pemeliharaan kode dan keterbacaan (_readability_) oleh manusia.

---

### 12.3 Otentikasi dan Navigasi Dasar Melalui CLI

#### A. Alur Kerja Otentikasi CLI

- CLI menggunakan utilitas baris perintah sistem operasi untuk masuk dan memverifikasi identitas pengguna langsung ke mesin server database.

#### B. Perintah Navigasi Awal Database

- Setelah otentikasi berhasil, terminal akan menampilkan prompt `mysql>` yang menandakan sistem siap menerima query.
- Eksekusi query navigasi awal wajib diakhiri dengan tanda titik koma (semicolon `;`):

Menampilkan seluruh database pada server:

```sql
SHOW DATABASES;
```

Mengaktifkan dan menggunakan database target (contoh: database `world`):

```sql
USE world;
```

Menampilkan seluruh tabel yang berada di dalam database aktif:

```sql
SHOW TABLES;
```

> [!warning] Audio Insight — Troubleshooting koneksi CLI (Windows)
> - **Pendaftaran Environment Path (Windows):** Jika saat mengetikkan perintah `mysql` pada Command Prompt (CMD) Windows muncul pesan error _'mysql' is not recognized_, hal tersebut menandakan lokasi folder instalasi biner MySQL belum terdaftar pada sistem. Langkah penyelesaiannya adalah:
>     1. Cari dan buka pengaturan **Edit the system environment variables** melalui Windows Search.
>     2. Buka variabel bernama **Path** pada bagian variabel lingkungan, lalu klik _Edit_ atau klik dua kali.
>     3. Klik **New** dan masukkan alamat absolut folder instalasi `bin` MySQL Anda (contoh: `C:\Program Files\MySQL\MySQL Server 8.0\bin`).
>     4. Klik **OK** untuk menyimpan seluruh konfigurasi.
>     5. **Sangat Penting:** Tutup terminal/Command Prompt yang sedang aktif, lalu buka kembali agar perubahan variabel lingkungan tersebut dapat dimuat ulang (_reload_) oleh sistem operasi. Perintah `mysql` kini siap digunakan.
> - **Penanganan Error Koneksi DBeaver (allowPublicKeyRetrieval):** Jika saat melakukan pengujian koneksi di DBeaver muncul error terkait autentikasi publik, arahkan kursor ke tab **Driver Properties** di pengaturan koneksi DBeaver Anda. Cari properti bernama `allowPublicKeyRetrieval`, lalu ubah nilainya dari `false` menjadi `true`. Simpan konfigurasi dan lakukan tes koneksi ulang.
> - **Penanganan Lupa Password Database Server:** Lupa kata sandi MySQL server lokal tidak dapat diatasi dengan fitur pemulihan sederhana seperti "forgot password". Prosedur reset manualnya sangat kompleks dan memakan waktu. Metode pemecahan masalah tercepat untuk lingkungan belajar lokal adalah melakukan _uninstall_ aplikasi MySQL Server secara total, lalu menginstal ulang server database tersebut untuk mengonfigurasi kata sandi administratif yang baru. Proses instalasi ulang ini tidak perlu dilakukan pada aplikasi antarmuka seperti DBeaver.
> - **Unduh Driver Database Otomatis:** Saat pertama kali mengonfigurasi koneksi database jenis baru pada DBeaver, aplikasi akan mendeteksi kebutuhan berkas driver pendukung dan memicu unduhan otomatis dari repositori online. Pengguna cukup mengonfirmasi persetujuan unduhan (_download_) agar koneksi dapat diaktifkan.

Bab konektivitas ini menjadi jembatan langsung ke [[Sesi 10 - SQL Working With Multiple Tables]] bagian Python MySQL Connector, di mana parameter koneksi yang sama (host, user, password, database) dipakai lagi — kali ini dari dalam skrip Python, bukan dari GUI.

---

## Bab 13 Latihan Praktis (Exercise) — Database `world`

### 13.1 Pengenalan Database Latihan "world"

#### A. Deskripsi Skema dan Struktur Tabel

- Database latihan yang digunakan adalah database bawaan MySQL yang bernama **"world"**.
- Database ini terdiri dari tiga tabel utama yang saling berelasi:
    - **`city`**: Menyimpan informasi data kota-kota di dunia (memiliki kolom `ID`, `Name`, `CountryCode`, `District`, dan `Population`).
    - **`country`**: Menyimpan informasi data negara-world (memiliki kolom `Code`, `Name`, `Continent`, `Region`, `SurfaceArea`, `IndepYear`, `Population`, `LifeExpectancy`, `GNP`, `GNPOld`, dll).
    - **`countrylanguage`**: Menyimpan informasi bahasa yang digunakan di setiap negara.

|Nama Tabel|Kolom Kunci (Key Columns)|Deskripsi Singkat|
|:--|:--|:--|
|`city`|`ID` (Primary Key), `CountryCode` (Foreign Key)|Informasi data administrasi kota tingkat dunia.|
|`country`|`Code` (Primary Key)|Data demografi, ekonomi, dan geografis negara.|
|`countrylanguage`|`CountryCode` (Primary Key), `Language`|Distribusi bahasa resmi dan non-resmi negara.|

Perhatikan bahwa ketiga tabel ini sudah saling terhubung lewat Primary Key/Foreign Key — konsep relasi antar-tabel ini dibahas secara formal di [[Sesi 10 - SQL Working With Multiple Tables]].

#### B. Prosedur Penyusunan Lingkungan Kerja (Injest Database)

- Proses import database dapat dilakukan melalui Command Line Interface (CLI) menggunakan utilitas `mysql` bawaan sistem operasi.
- Sebelum melakukan injest, pengguna harus mengunduh file biner beralamat `world.sql` dari laman resmi dokumentasi MySQL, kemudian mengekstraknya jika dalam format terkompresi (`.zip`).
- Perintah eksekusi impor biner database pada terminal adalah sebagai berikut:

```
mysql -u root -p world < "C:\path\to\world.sql"
```

> [!warning] Audio Insight — Kendala ingest database di Windows
> - Dalam praktek instalasi langsung saat kuliah luring, beberapa mahasiswa Windows mengalami kendala perintah `mysql` tidak dikenali (_not recognized_). Solusinya adalah mendaftarkan alamat biner MySQL (contoh: `C:\Program Files\MySQL\MySQL Server 8.0\bin`) ke dalam variabel lingkungan sistem (**Environment Path**) terlebih dahulu.
> - Pada terminal PowerShell Windows, simbol pengarah input `<` dicadangkan (_reserved_) untuk penggunaan masa depan sehingga akan menghasilkan error. Solusinya adalah menjalankan proses impor melalui **Command Prompt (CMD)** standar Windows agar berjalan mulus.
> - Jika koneksi sukses dibuat pada perkakas antarmuka seperti **DBeaver** tetapi database `world` yang baru di-injest belum muncul pada panel navigasi, lakukan operasi **Refresh (F5)** pada folder lokal agar struktur tabel ter-render secara real-time.

---

### 13.2 Bedah Soal dan Solusi Query SQL (Database world)

#### A. Soal 1: Aktivasi Database world

- **Pertanyaan:** Aktifkan database `world` agar seluruh query berikutnya mengeksekusi tabel di dalam database tersebut.

```sql
USE world;
```

#### B. Soal 2: Menghitung Jumlah Region Unik

- **Pertanyaan:** Ada berapa banyak region yang tercatat di dalam database `world`? Ubah nama header kolom output-nya menjadi `Jumlah_Region`.

```sql
SELECT COUNT(DISTINCT region) AS Jumlah_Region
FROM country;
```

- **Hasil Eksekusi:** Teridentifikasi sebanyak **25** region unik di dunia.

#### C. Soal 3: Menghitung Jumlah Negara di Benua Afrika

- **Pertanyaan:** Berapakah jumlah negara yang berada di benua Afrika (`Africa`)? Ubah nama header kolom output-nya menjadi `Jumlah_Negara`.

```sql
SELECT COUNT(Name) AS Jumlah_Negara
FROM country
WHERE Continent = 'Africa';
```

- **Hasil Eksekusi:** Teridentifikasi sebanyak **58** negara di benua Afrika.

#### D. Soal 4: Menampilkan 5 Negara dengan Populasi Terbesar

- **Pertanyaan:** Tampilkan 5 negara dengan jumlah populasi terbesar di dunia. Ubah nama header kolom output-nya masing-masing menjadi `Nama_Negara` dan `Populasi`.

```sql
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

#### E. Soal 5: Menampilkan Rata-Rata Harapan Hidup tiap Benua

- **Pertanyaan:** Tampilkan rata-rata angka harapan hidup (`LifeExpectancy`) untuk setiap benua, diurutkan dari nilai rata-rata yang paling rendah. Ubah nama header kolom output-nya masing-masing menjadi `Nama_Benua` dan `Rata_Rata_Harapan_Hidup`.

```sql
SELECT Continent AS Nama_Benua, AVG(LifeExpectancy) AS Rata_Rata_Harapan_Hidup
FROM country
GROUP BY Continent
ORDER BY Rata_Rata_Harapan_Hidup ASC;
```

> [!tip] Audio Insight — Antarctica menghasilkan NULL
> - Saat query ini dijalankan oleh mahasiswa, benua **Antarctica** menghasilkan nilai rata-rata harapan hidup berupa `NULL` atau tidak memiliki data harapan hidup sama sekali karena tidak memiliki populasi penduduk tetap.

#### F. Soal 6: Menampilkan Benua dengan Jumlah Region Lebih dari 3

- **Pertanyaan:** Tampilkan jumlah region untuk setiap benua yang memiliki jumlah region unik lebih dari 3. Ubah nama header kolom output-nya masing-masing menjadi `Nama_Benua` dan `Jumlah_Region`.

```sql
SELECT Continent AS Nama_Benua, COUNT(DISTINCT Region) AS Jumlah_Region
FROM country
GROUP BY Continent
HAVING Jumlah_Region > 3;
```

- **Hasil Eksekusi:** Menampilkan daftar benua seperti Asia, Europe, dan Africa yang memenuhi kriteria penyaringan agregat. (Perhatikan: filter `Jumlah_Region > 3` di sini adalah contoh nyata `HAVING` menyaring hasil `COUNT(DISTINCT ...)` per grup — lihat penelusuran langkah-demi-langkah di [[#Bab 9 Penyaringan Grup Data (HAVING)]].)

#### G. Soal 7: Menampilkan Rata-Rata GNP di Afrika Berdasarkan Region

- **Pertanyaan:** Tampilkan nilai rata-rata GNP di benua Afrika berdasarkan pembagian regionnya, lalu urutkan dari nilai rata-rata GNP yang paling besar ke yang paling kecil. Ubah nama header kolom output-nya masing-masing menjadi `Nama_Region` dan `Rata_Rata_GNP`.

```sql
SELECT Region AS Nama_Region, AVG(GNP) AS Rata_Rata_GNP
FROM country
WHERE Continent = 'Africa'
GROUP BY Region
ORDER BY Rata_Rata_GNP DESC;
```

- **Hasil Eksekusi:** Peringkat rata-rata GNP terbesar dipimpin oleh Northern Africa, diikuti Southern Africa, Western Africa, Central Africa, dan Eastern Africa.

#### H. Soal 8: Menampilkan Negara Berisi Tepat 6 Huruf dan Berakhiran 'O'

- **Pertanyaan:** Tampilkan nama negara yang memiliki panjang karakter nama tepat 6 huruf dan diakhiri dengan huruf 'O'.

```sql
SELECT Name
FROM country
WHERE LENGTH(Name) = 6 AND Name LIKE '%o';
```

- **Hasil Eksekusi:** Menghasilkan negara-negara spesifik yang memenuhi kondisi string matching tersebut, contohnya **Monaco** dan **Mexico**.

> [!warning] Audio Insight — LENGTH() bukan fungsi agregat, jadi pakai WHERE bukan GROUP BY/HAVING
> - Pada diskusi luring kelas, mahasiswa sempat mencoba menyelesaikan kasus ini menggunakan manipulasi klausa `GROUP BY Name HAVING` panjang karakter tertentu. Dosen memberikan koreksi penting bahwa fungsi `LENGTH()` bukanlah fungsi agregat (melainkan fungsi skalar), sehingga penyaringan karakter string individu wajib diletakkan langsung di dalam klausa filter utama **`WHERE`** dan tidak memerlukan pengelompokan grup.

#### I. Soal 9: Menampilkan Region dengan Kenaikan Rata-Rata GNP Terbesar

- **Pertanyaan:** Region mana saja yang nilai rata-rata GNP terbarunya mengalami kenaikan dibandingkan rata-rata GNP masa lalu (`GNPOld`)? Urutkan hasilnya dari nilai selisih kenaikan yang paling tinggi ke yang paling rendah.

```sql
SELECT Region,
       AVG(GNP) AS Avg_GNP,
       AVG(GNPOld) AS Avg_GNPOld,
       (AVG(GNP) - AVG(GNPOld)) AS Selisih
FROM country
GROUP BY Region
HAVING AVG(GNP) > AVG(GNPOld)
ORDER BY Selisih DESC;
```

> [!warning] Audio Insight — Jangan bungkus alias ORDER BY dengan tanda petik
> - Di akhir diskusi luring, terjadi perbandingan output kueri antara mahasiswa di mana region **British Islands** seharusnya berada di peringkat teratas sebagai region dengan selisih kenaikan rata-rata GNP terbesar. Perbedaan urutan sempat terjadi karena kesalahan sepele penulisan tanda petik pada klausa pengurutan `ORDER BY`.
> - Dosen mengingatkan aturan mutlak penulisan SQL bahwa nama kolom alias pada klausa `ORDER BY` **dilarang keras dibungkus dengan tanda petik tunggal (`'Selisih'`)**. Pembungkusan dengan tanda petik tunggal akan dibaca oleh sistem komputer sebagai string statis konstan dan bukan representasi nilai kolom dinamis, yang mengakibatkan logika pengurutan database menjadi kacau atau tidak berjalan semestinya.

---

### 13.3 Catatan Praktik Langsung di Kelas (Raw Lecture Notes)

Bagian ini adalah catatan mentah langsung dari sesi kuliah (belum diolah ulang), dipertahankan apa adanya sebagai referensi tambahan.

**1. Create Database** (langkah-langkah praktik di DBeaver):
1. Pertama, buka klik kanan di localhost pada panel kiri layar, kemudian SQL Editor, New SQL Script.
2. Rename script menjadi `Database_and_SQL_intro.sql`.
3. Paste `SHOW DATABASES;` kemudian play untuk melihat database apa saja yang sudah ada.
4. Timpa dengan `CREATE DATABASE demo_scratch;` untuk buat database baru.
5. Kemudian refresh, localhost di panel kiri layar, nanti akan muncul `demo_scratch`.
6. Kemudian belajar untuk menghapus database dengan `DROP DATABASE demo_scratch;` kemudian, play dan refresh panel localhost. Database tersebut akan hilang.
7. Sekarang bikin lagi database baru, namanya `CREATE DATABASE seller;`

**Ringkasan cepat tiga klausa inti** (dari catatan kelas, sudah dibahas lengkap di bab-bab sebelumnya):
- **HAVING**: Mengolah data agregat atau hasil olahan (menyaring grup — lihat [[#Bab 9 Penyaringan Grup Data (HAVING)]]).
- **WHERE**: Menyaring data (baris individual — lihat [[#Bab 4 Penyaringan Data Tingkat Lanjut (Filtering Data)]]).
- **LIKE**: Mencocokkan pola teks (lihat Bab 4.2 — Pencocokan Pola Teks di atas).
