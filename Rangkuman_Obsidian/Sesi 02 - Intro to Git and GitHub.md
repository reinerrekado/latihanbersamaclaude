---
tags: [module1, sesi-02, git, github, version-control, workflow]
aliases: ["Sesi 2", "Intro to Git and GitHub", "Tutorial Git & Github", "Latihan Github Bersama Nadir"]
---

# Session 2 — Intro to Git & GitHub

Catatan sesi kedua ini mencakup pengenalan Git dan GitHub, empat istilah kunci (repository, commit, branch, merge), alur kerja commit lokal secara mendalam, tutorial anatomi perintah Git, latihan praktik langkah-demi-langkah membuat repo hingga push & merge, serta rincian tugas besar (PR Session 2).

---

## Bab 1 — Pengenalan Git dan GitHub

### 1.1 Definisi Git

Git adalah sebuah _distributed version control system_ (VCS) yang memungkinkan pengembang untuk melacak perubahan pada kode mereka dari waktu ke waktu. Sistem ini dirancang untuk menangani segala jenis proyek, dari kecil hingga sangat besar, dengan kecepatan dan efisiensi tinggi.

Salah satu fungsi utama Git adalah memfasilitasi kolaborasi. Dengan Git, beberapa orang dapat bekerja pada proyek yang sama secara bersamaan tanpa risiko saling menimpa (_overwriting_) perubahan yang dilakukan oleh pengembang lain.

### 1.2 Sejarah Singkat dan Tokoh Kunci

Git diciptakan oleh **Linus Torvalds**, yang juga dikenal sebagai pencipta sistem operasi Linux. Pengembangan Git didorong oleh kebutuhan akan sistem kontrol versi yang handal dan terdistribusi untuk mengelola pengembangan _kernel_ Linux yang sangat kompleks dan masif.

### 1.3 Karakteristik Utama Git

| Karakteristik | Deskripsi |
| --- | --- |
| **Tipe Sistem** | _Distributed version control system_ (VCS). |
| **Fungsi Utama** | Melacak setiap perubahan pada kode sumber secara kronologis. |
| **Keamanan Kolaborasi** | Memungkinkan banyak pengembang bekerja bersama tanpa risiko _overwriting_. |
| **Efisiensi Proyek** | Mampu menangani proyek berskala kecil hingga sangat besar dengan cepat. |
| **Arsitektur Terdistribusi** | Setiap pengembang memiliki salinan lengkap dari riwayat proyek di mesin lokal mereka. |

### 1.4 Definisi GitHub

Berbeda dengan Git yang merupakan alat (_tool_) teknis, GitHub adalah sebuah platform layanan _hosting_ berbasis web untuk repositori Git. GitHub menyediakan tempat bagi pengembang untuk menyimpan proyek mereka secara daring (_online_), sehingga memudahkan proses kolaborasi dengan pihak luar atau anggota tim lainnya.

GitHub bukan sekadar tempat penyimpanan, melainkan berfungsi sebagai jejaring sosial bagi para pengembang — tempat berbagi kode, berkontribusi pada proyek sumber terbuka (_open-source_), dan mengelola proyek secara profesional.

**Fitur Kerja Tim di GitHub:**

- **Pull Request:** mekanisme untuk mengajukan perubahan kode ke proyek utama.
- **Issue Tracking:** fitur untuk mencatat dan melacak bug, tugas, atau permintaan fitur baru.
- **Project Management:** perangkat lunak terintegrasi untuk mengelola alur kerja dan progres proyek.

### 1.5 Perbedaan Peran Git vs GitHub

| Aspek Perbedaan | Git | GitHub |
| --- | --- | --- |
| **Sifat Dasar** | Perangkat lunak _version control_ (lokal). | Layanan _hosting_ berbasis web (cloud). |
| **Instalasi** | Diinstal dan dijalankan secara lokal pada komputer. | Diakses melalui peramban web atau aplikasi pihak ketiga. |
| **Fokus Utama** | Pelacakan perubahan kode dan manajemen revisi. | Penyimpanan daring, kolaborasi tim, dan jejaring sosial pengembang. |
| **Ketergantungan** | Dapat berjalan sendiri tanpa internet. | Memerlukan koneksi internet untuk sinkronisasi dan fitur kolaboratif. |

### 1.6 Signifikansi Penggunaan Git & GitHub

1. **Peningkatan Produktivitas:** memudahkan pengelolaan versi kode sehingga pengembang dapat fokus pada penulisan fitur.
2. **Kolaborasi yang Lebih Baik:** menyediakan infrastruktur yang rapi agar tim dapat bekerja secara simultan tanpa konflik yang merusak.
3. **Code Management:** memberikan kontrol penuh terhadap riwayat kode, memudahkan pelacakan bug, dan memastikan keamanan integritas kode sumber.

> [!tip] Audio Insight — Kontribusi Masif Linus Torvalds
> Dalam sesi interaktif, ditekankan betapa masifnya kontribusi Linus Torvalds terhadap dunia teknologi informasi. Torvalds tidak hanya menciptakan sistem operasi Linux — yang kini bersifat gratis dan menjadi tulang punggung bagi mayoritas server di seluruh dunia — tetapi ia juga menciptakan Git sebagai solusi atas kebutuhan manajemen kode yang kompleks. Tanpa inovasi Torvalds dalam menciptakan Git, kolaborasi pengembang skala global seperti yang terlihat di GitHub saat ini tidak akan mungkin terjadi secara efisien.

---

## Bab 2 — Konsep Dasar Sistem Git

### 2.1 Metode Analogi Struktur Git

Untuk memahami cara kerja Git, struktur sistem ini dapat divisualisasikan menggunakan analogi sebuah pohon:

- **Pohon (Tree):** merepresentasikan keseluruhan proyek atau aplikasi yang sedang dikembangkan.
- **Cabang (Branch):** merepresentasikan jalur pengembangan yang independen. Dalam satu pohon (proyek), bisa terdapat banyak cabang yang tumbuh secara bersamaan.
- **Daun (Leaves):** merepresentasikan **commit**. Setiap daun adalah titik penanda perubahan yang spesifik pada jalur pengembangan tersebut.

### 2.2 Empat Istilah Kunci Utama Git

**Repository (Repo)** — tempat penyimpanan utama di mana sebuah proyek disimpan. Secara teknis, ini berfungsi seperti folder besar di komputer yang memiliki kemampuan khusus untuk melacak semua file dan setiap perubahan yang terjadi pada file-file tersebut sepanjang waktu.

**Commit** — sebuah _snapshot_ atau potret dari proyek pada titik waktu tertentu. Ketika pengembang melakukan perubahan dan menyimpannya sebagai _commit_, Git mencatat keadaan persis dari seluruh proyek saat itu.

- Setiap _commit_ diidentifikasi secara unik menggunakan **SHA-1 hash** (untaian 40 karakter heksadesimal).
- Hash ini memungkinkan pengembang untuk merujuk kembali ke versi lama dan melihat sejarah perubahan dengan presisi tinggi.

**Branch** — salinan jalur pengembangan proyek yang memungkinkan pengembang bekerja tanpa memengaruhi jalur utama (_main project_). Fitur ini penting untuk eksperimen atau pengembangan fitur baru secara terisolasi.

**Merge** — proses pengambilan perubahan dari sebuah _branch_ dan menggabungkannya kembali ke proyek utama.

- Git akan mencoba menggabungkan perubahan secara otomatis.
- Jika terdapat perubahan pada baris kode yang sama di dua jalur berbeda, akan terjadi **_conflict_**. Dalam situasi ini, pengembang harus melakukan **conflict resolution** secara manual untuk menentukan kode mana yang akan digunakan.

> [!tip] Audio Insight — Repository vs. Cloud Storage
> _Repository_ dapat dibayangkan seperti layanan drive bersama (seperti Google Drive atau OneDrive), namun dengan kecerdasan tambahan untuk melacak riwayat perubahan secara mendalam, bukan sekadar menyimpan file versi terbaru.

> [!warning] Audio Insight — Kolaborasi Git vs. Google Docs (Bukan Live-Update)
> Berbeda dengan Google Docs yang menggunakan _live update_ (perubahan tersimpan otomatis secara _real-time_), Git menggunakan mekanisme _merge_ dan _conflict resolution_ manual. Hal ini memberikan kendali penuh kepada pengembang untuk meninjau kode sebelum digabungkan ke sistem utama.

### 2.3 Tabel Rangkuman 4 Istilah Kunci

| Istilah Kunci | Definisi Teknis | Analogi Dunia Nyata |
| --- | --- | --- |
| **Repository** | Lokasi penyimpanan digital untuk melacak seluruh file dan riwayat perubahan. | Folder besar atau gudang arsip proyek. |
| **Commit** | _Snapshot_ proyek pada titik waktu tertentu dengan identitas SHA-1 hash. | Foto keadaan proyek sebagai titik simpan (_checkpoint_). |
| **Branch** | Jalur pengembangan independen yang terpisah dari kode utama. | Cabang pohon yang tumbuh ke arah berbeda dari batang utama. |
| **Merge** | Proses penggabungan perubahan dari satu jalur ke jalur lainnya. | Menyatukan kembali cabang ke batang pohon utama. |

### 2.4 Signifikansi dan Konsep Branching System

Sistem _branching_ memiliki peran krusial dalam menjaga stabilitas proyek. Tujuan utamanya adalah memisahkan jalur fitur baru atau eksperimen agar tidak merusak kode produksi utama (_main branch_) yang sedang berjalan.

Contoh visualisasi (skema pengembangan aplikasi besar seperti Instagram):

- **Main Branch (Abu-abu):** jalur kode yang stabil dan sedang digunakan oleh pengguna (kode produksi).
- **Feature Branches (Biru/Kuning):** jalur pengembangan untuk fitur baru, misalnya fitur "Explore" atau "Account". Pengembang bekerja di sini untuk memastikan fitur selesai dan bebas _bug_ sebelum akhirnya melakukan _merge_ ke jalur abu-abu.

Dengan sistem ini, jika terjadi kesalahan pada fitur baru yang sedang dikembangkan (jalur biru), aplikasi utama (jalur abu-abu) tetap aman dan tidak mengalami gangguan atau _crash_.

### 2.5 Lelucon Keselamatan Software Engineer

Dalam komunitas _software engineer_, terdapat anekdot mengenai prosedur darurat jika terjadi kebakaran di gedung kantor:

**"In Case of Fire:"**

```bash
git commit
git push
git out!
```

> [!tip] Audio Insight — Logika Protokol Keselamatan Digital di Balik Lelucon
> Dosen menjelaskan logika di balik lelucon ini sebagai protokol keselamatan digital:
> - **git commit:** mengamankan perubahan terakhir di _checkpoint_ lokal laptop.
> - **git push:** mengunggah kode tersebut ke _cloud remote repository_ — agar jika laptop hancur atau meleleh akibat api, hasil kerja keras pengembang tetap selamat di server _cloud_.
> - **git out!:** setelah kode aman di server, barulah pengembang menyelamatkan diri keluar dari gedung. Ini menekankan bahwa bagi seorang pengembang, keselamatan kode (aset digital) sering kali diposisikan sangat penting sebelum mereka benar-benar meninggalkan area berbahaya.

---

## Bab 3 — Bekerja dengan Commits Lokal secara Terstruktur dan Mendalam

### 3.1 Siklus Status Berkas (Status Lifecycle)

Dalam Git, setiap berkas di dalam _working directory_ (direktori kerja) memiliki siklus status yang menentukan bagaimana Git memperlakukan berkas tersebut. Secara garis besar, berkas dikategorikan menjadi dua kelompok utama:

- **Tracked files:** berkas yang sudah dikenal oleh Git. Berkas ini adalah bagian dari _snapshot_ terakhir atau telah masuk ke dalam _staging area_. Statusnya dapat berupa _unmodified_, _modified_, atau _staged_.
- **Untracked files:** berkas apa pun di dalam direktori kerja yang tidak ada dalam _snapshot_ terakhir dan belum dimasukkan ke dalam _staging area_. Git melihat berkas ini tetapi tidak memantau perubahannya secara otomatis.

| Status | Arti | Karakteristik / Indikator |
| --- | --- | --- |
| **Untracked** | Berkas Baru | Berkas yang belum pernah direkam oleh Git. Tidak termasuk dalam riwayat versi. |
| **Unmodified** | Belum Dimodifikasi | Berkas _tracked_ yang isinya identik dengan versi yang ada pada _commit_ terakhir. |
| **Modified** | Telah Dimodifikasi | Berkas _tracked_ yang telah mengalami perubahan pada direktori kerja, namun perubahannya belum ditandai untuk _commit_. |
| **Staged** | Siap di-Commit | Berkas yang telah ditandai (melalui perintah `git add`) untuk disertakan dalam _snapshot_ berikutnya. |

> [!tip] Audio Insight — Indikator Visual 'U' Hijau di VS Code
> Dalam praktik menggunakan VS Code, indikator status berkas dapat dilihat secara visual di samping nama berkas pada panel penjelajah. Berkas yang berstatus **Untracked** sering kali ditandai dengan indikator huruf **'U'** berwarna hijau. Hal ini menandakan bahwa berkas tersebut baru dibuat dan Git memerlukan instruksi eksplisit (seperti `git add`) untuk mulai melacaknya.

### 3.2 Alur Kerja Perintah Dasar Commit Lokal

**3.2.1 Inisialisasi Repository (`git init`)** — langkah pertama untuk mengubah direktori biasa menjadi Git _repository_ lokal. Perintah `git init` akan membuat sub-direktori `.git` tersembunyi yang menyimpan semua metadata dan riwayat versi.

> [!tip] Audio Insight — Navigasi Terminal Sebelum `git init`
> Diskusi teknis menunjukkan adanya kesulitan navigasi terminal sebelum menjalankan `git init`. Pengguna sering kali berada di direktori pengguna default (seperti `C:\Users\NamaUser`) dan harus berpindah ke folder proyek yang tepat.
> - **Navigasi Terminal:** gunakan perintah `cd` (_change directory_) untuk mencapai folder tujuan (misal dari `OneDrive` ke `Desktop`, lalu ke `Python Project`).
> - **Auto-complete:** gunakan tombol **Tab** saat mengetik nama folder untuk menghindari kesalahan penulisan (seperti spasi pada nama folder).
> - **Verifikasi Lokasi:** jalankan `ls` (atau `dir` pada Windows) untuk melihat isi direktori dan memastikan berkas proyek ada di sana sebelum menjalankan perintah Git.

**3.2.2 Mengatur Identitas (`git config`)** — wajib dilakukan sebelum _commit_ karena setiap _commit_ Git menyertakan informasi penulis sebagai bagian dari _snapshot_ yang tidak dapat diubah.

```bash
git config --global user.name "Nama Pengguna"
git config --global user.email "email@contoh.com"
```

**3.2.3 Memeriksa Status Real-Time (`git status`)** — melihat perbedaan antara berkas di direktori kerja, _staging area_ (index), dan _commit_ terakhir (HEAD). Memberikan panduan mengenai langkah apa yang harus diambil selanjutnya (misal: apakah ada berkas yang perlu di-`add`).

**3.2.4 Memindahkan Berkas ke Tahap Staged (`git add`)**

- `git add <nama_berkas>`: menambahkan berkas spesifik.
- `git add .`: menambahkan semua perubahan dan berkas baru di direktori saat ini ke tahap _staged_.

**3.2.5 Membuat Snapshot (`git commit`)** — proses mengambil _snapshot_ dari proyek pada titik waktu tertentu. Setiap _commit_ diidentifikasi oleh _hash_ SHA-1 unik sepanjang 40 karakter.

```bash
git commit -m "feat: pesan commit yang deskriptif"
```

**Kriteria Commit yang Sempurna:** (1) menyertakan perubahan yang tepat (tidak kurang, tidak lebih); (2) memiliki pesan _commit_ yang menjelaskan maksud dari perubahan tersebut secara jelas.

> [!warning] Audio Insight — Urutan Wajib: `git add` Sebelum `git commit`
> Dosen memberikan panduan khusus saat mahasiswa menghadapi kondisi "no commits yet" meskipun berkas sudah ada. Melalui kasus Reainer, dijelaskan bahwa urutan yang benar adalah memastikan berkas dipindahkan ke "changes to be committed" terlebih dahulu menggunakan `git add`, baru kemudian menjalankan `git commit`. Tanpa tahap _add_, Git tidak akan memiliki data untuk disimpan ke dalam riwayat.

**3.2.6 Memeriksa Perubahan (`git diff`)** — sebelum melakukan _commit_, disarankan menjalankan `git diff` untuk memeriksa detail perubahan baris per baris pada berkas, memastikan hanya perubahan yang diinginkan yang masuk ke dalam _snapshot_.

### 3.3 Catatan Tambahan Terkait Lingkungan Kerja

> [!tip] Audio Insight — Pentingnya Aktivasi Virtual Environment
> Sebelum menjalankan script Python atau perintah Git tertentu, dosen menekankan pentingnya aktivasi _virtual environment_. Di terminal VS Code, sering kali pengguna perlu memastikan bahwa environment **base** pada MiniConda atau Anaconda sudah aktif. Hal ini ditandai dengan munculnya nama environment dalam kurung di awal baris perintah terminal. Aktivasi lingkungan yang tepat memastikan semua _dependencies_ tersedia saat script dijalankan. (Lihat juga pengenalan Venv/Conda di [[Sesi 01 - Introduction to DS Python Statistics SQL Git and GitHub]] Bab 4.3.)

---

## Bab 4 — Tutorial Referensi: Anatomi Perintah Git & Siklus Hidup File

> Bagian ini merangkum tutorial referensi cepat ("Tutorial Git & Github") yang aslinya ditulis sebagai catatan Obsidian terpisah, digabungkan di sini agar alurnya menyatu dengan Bab 1–3.

### 4.1 Anatomi Perintah Git (Git Command)

Semua instruksi teks yang Anda ketik di terminal secara umum disebut **Git Commands**. Strukturnya selalu terdiri dari bagian-bagian berikut:

- **`git` (Program Utama):** sama seperti membuka aplikasi — mengetik `git` berarti memanggil program Git untuk bersiap menerima instruksi.
- **`init`, `status`, `commit`, `push` (Sub-command / Kata Kerja):** instruksi utama, memberi tahu Git tugas spesifik apa yang harus dilakukan.
- **`-b`, `-m`, `--no-ff` (Flags / Opsi):** ditandai dengan tanda minus/setrip, memodifikasi cara kerja sub-command. Contoh: `-m` berarti pesan (_message_) diketik langsung di baris tersebut.
- **`"Hello World"`, `main`, `app.py` (Arguments / Target):** objek yang menjadi sasaran perintah, bisa berupa nama file, nama cabang, atau isi pesan.

```bash
# Contoh anatomi lengkap satu perintah git:
git commit -m "feat: initial commit"
# ^git    ^sub-command  ^flag  ^argument (pesan commit)
```

### 4.2 Inisialisasi & Konfigurasi (Membuat "Gudang")

- **Repository (Repo):** folder proyek Anda yang dipantau oleh Git.
- **`git init -b main`:** mengubah folder biasa menjadi _repository_ kosong, dan langsung menamai jalur utamanya dengan nama "main".
- **`git config`:** mengatur identitas (nama dan email) agar Git tahu _siapa_ yang melakukan perubahan pada kode.

### 4.3 Tiga Area Utama Git (Siklus Hidup File)

File Anda selalu berpindah di antara tiga status ini saat Anda bekerja:

1. **Untracked / Modified (_Working Directory_):** Anda mengubah file `app.py`. Saat menjalankan `git status`, Git melihat ada perubahan tapi belum diapa-apakan.
2. **Staged (_Staging Area_):** Anda menjalankan `git add app.py`. Perubahan ini masuk ke dalam "antrean" untuk disiapkan menuju _commit_.
3. **Committed (_Git Directory_):** Anda menjalankan `git commit -m "pesan"`. Git mengambil "foto" dari file di antrean dan menyimpannya ke dalam sejarah permanen.

### 4.4 Membaca Sejarah (Log)

- **`git log`:** mencetak daftar riwayat sejarah _commit_ yang sudah Anda lakukan.
- **Hash Code:** deretan angka dan huruf acak (misal: `e69de29`) di dalam log — ID unik untuk setiap _commit_.
- **HEAD:** kursor/penanda yang menunjukkan di mana posisi Anda saat ini di dalam sejarah Git (contoh: `HEAD -> main` berarti Anda sedang melihat file dari _commit_ terakhir di cabang `main`).

### 4.5 Cabang & Pindah (Branching & Checkout)

- **Branch (Cabang):** salinan paralel dari kode Anda — memungkinkan bereksperimen tanpa merusak kode utama (`main`).
- **`git checkout -b <nama_branch>`:** membuat cabang baru sekaligus langsung memindahkan Anda ke cabang tersebut.
- **`git checkout <nama_branch>`:** hanya berpindah dari satu cabang ke cabang lain (misal kembali ke `main`).

### 4.6 Menggabungkan Kode (Merge)

- **`git merge <nama_branch>`:** menarik kode dari cabang lain dan menggabungkannya ke cabang tempat Anda berada sekarang.
- **`--no-ff` (No Fast-Forward):** opsi ini memaksa Git membuat satu _commit_ baru khusus sebagai "simpul" penggabungan, sehingga grafik sejarahnya terlihat jelas bahwa pernah ada percabangan yang akhirnya disatukan.

### 4.7 Menghubungkan ke GitHub (Remote & Push)

Git ada di komputer Anda (Lokal), sedangkan GitHub adalah server di internet (Cloud).

- **`git remote add origin <url>`:** menyambungkan gudang lokal Anda ke gudang GitHub. Kata **`origin`** adalah nama alias standar untuk URL GitHub Anda.
- **`git push -u origin main`:** mengirim (_push_) seluruh sejarah yang sudah Anda _commit_ di komputer ke server GitHub (`origin`) pada cabang `main`.

---

## Bab 5 — Latihan Praktik: Membuat Repo hingga Push & Merge (Bersama Nadir)

Berikut adalah rekonstruksi langkah demi langkah dari sesi praktik langsung, dari inisialisasi repo lokal hingga _pull request_ tersimulasikan lewat _merge_ manual dan _push_ ke GitHub — direkonstruksi dari catatan latihan asli agar alurnya mengalir sekali tanpa pengulangan.

### 5.1 Inisialisasi Repository

```bash
# 1. Inisialisasi git. Flag -b main artinya langsung generate branch main.
git init -b main

# 2. Memberikan identitas nama untuk konfigurasi commit.
git config user.name "Your Name"

# 3. Memberikan identitas email untuk konfigurasi commit.
git config user.email "your@email.com"
```

### 5.2 Membuat File Pertama & Commit Pertama

```bash
# 1. Buat file app.py, isi dengan perintah echo
echo "Hello World" > app.py

# 2. Cek status untracked
git status

# 3. Tambahkan file app.py ke Git (masuk ke antrian staging)
git add app.py

# 4. Cek lagi apakah sudah masuk staging
git status
```

Output `git status` akan menunjukkan:

```bash
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   app.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
```

```bash
# 5. Setelah status add ke track, commit dengan pesan deskriptif
git commit -m "feat: nadir suka kopi"

# 6. Lihat aktivitas commit dan kode hash
git log
# HEAD -> main artinya sudah berada di branch main.
```

### 5.3 Modifikasi File, Cek Perbedaan (`git diff`), dan Commit Kedua

```bash
# 7. Modifikasi file app.py
echo "print('Hello')" >> app.py

# 8. Cek status lagi -> modified: app.py
git status

# 9. Cek perbedaan file sebelum dan sesudah diubah
git diff
```

Output `git diff` menunjukkan penambahan dua baris baru:

```bash
diff --git a/app.py b/app.py
index e69de29..d1e154a 100644
--- a/app.py
+++ b/app.py
@@ -0,0 +1,2 @@
+echo "Hello World"
+echo "print('Hello')"
\ No newline at end of file
```

```bash
# 10. Tambahkan perubahan ke staging
git add app.py

# 11. Commit untuk mengunci perubahan
git commit -m "feat: add print statement"
# Output: 1 file changed, 2 insertions(+)

# 12. Lihat aktivitas commit dalam format ringkas
git log --oneline
```

### 5.4 Menghubungkan ke GitHub dan Push Pertama

```bash
# 13. Buat repo baru di GitHub bernama git.demo2, lalu hubungkan remote-nya
git remote add origin https://github.com/reinerrekado/git.demo2.git

# 14. Push commit ke GitHub
git push -u origin main
```

Output sukses akan terlihat seperti:

```bash
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (6/6), 468 bytes | 156.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/reinerrekado/git.demo2.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

### 5.5 Membuat Branch Baru, Berpindah Antar Branch, dan Merge

```bash
# 15. Buat branch baru sekaligus pindah ke sana
git checkout -b feature/greeting

# 16. Modifikasi app.py dengan kode baru
echo "print('Hi everyone')" >> app.py

# 17. Tambahkan ke staging
git add app.py

# 18. Commit perubahan
git commit -m "feat: add greeting message"

# 19. Cek riwayat commit
git log --oneline

# 20. Cek branch aktif saat ini, lalu pindah ke main
git checkout main
# Output: Switched to branch 'main'

# 21. Lihat isi file app.py di branch main
cat app.py

# 22. Pindah lagi ke branch feature/greeting
git checkout feature/greeting

# 23. Bandingkan isi file app.py di branch feature/greeting
cat app.py

# 24. Kembali ke main karena akan menggabungkan branch
git checkout main

# 25. Gabungkan branch feature/greeting ke main
git merge --no-ff feature/greeting
```

> [!tip] Tips Praktis — Jika Terminal "Stuck" saat Merge
> Perintah `git merge --no-ff` kadang membuka editor teks (Vim) di dalam terminal untuk meminta pesan merge. Jika terminal terlihat "macet"/stuck di layar editor tersebut, tekan `Esc` lalu ketik `:qa` dan Enter untuk keluar tanpa mengubah pesan default.

```bash
# 26. Cek perubahan commit -> akan muncul keterangan merge branch 'feature/greeting'
git log --oneline

# 27. Push hasil merge ke GitHub
git push origin main
```

Output push setelah merge:

```bash
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 400 bytes | 200.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/reinerrekado/git.demo2.git
   e48ad9b..c0ce583  main -> main
```

> [!info] Lihat juga
> Alur `git checkout -b` → edit → `add` → `commit` → `push` → `merge` di atas adalah implementasi konkret dari **GitHub Flow** yang disinggung di Bab 6 (Tugas Besar 1) di bawah, dan dari anatomi perintah di Bab 4.

---

## Bab 6 — Tugas Besar / PR Session 2

### 6.1 Tugas Besar 1: Git & GitHub Workflow (Basic Exercise 1)

Tugas ini berfokus pada penguasaan **alur kerja standar industri (GitHub Flow)** dengan melakukan pembuatan repository baru sampai pull request di GitHub. Ada 5 langkah berurutan:

1. **Inisialisasi Repositori Awal** — buat direktori baru, inisialisasi sebagai repositori Git, tambahkan beberapa file (bisa berupa "Hello World" atau kode lainnya). Ekspektasi: mendemonstrasikan pemahaman proses _setup_ awal repositori Git lokal.
2. **Siklus Commit & Push Pertama** — lakukan perubahan pada file, `stage`, `commit` **dengan pesan yang deskriptif**, lalu `push` ke GitHub. Ekspektasi: mempraktikkan alur kerja dasar dalam membuat perubahan dan menyimpannya ke server.
3. **Membuat Cabang & Navigasi (Branching)** — buat _branch_ baru, lakukan perubahan kode, lalu **berpindah-pindah** (_switch back and forth_) antara _branch_ baru dan _branch_ lama mengikuti strategi **GitHub Flow**. Ekspektasi: memahami fungsi _branch_ tanpa merusak kode di _branch_ utama.
4. **Menyimpan Pekerjaan di Cabang Baru** — pastikan perubahan dilakukan **di dalam branch baru**, lalu _stage_, _commit_ (dengan pesan deskriptif), dan _push_ _branch_ baru tersebut ke GitHub. Ekspektasi: mengerti cara mem-_push_ sebuah _branch_ baru yang sebelumnya belum ada di server.
5. **Integrasi Kode Akhir** — buat _Pull Request_ (PR) di GitHub, _review_ kode tersebut, lalu lakukan penggabungan (_merge the changes_). Ekspektasi: memahami dan mensimulasikan _workflow_ kolaborasi kode yang digunakan secara nyata di industri.

### 6.2 Tugas Besar 2: Python Code / Logic (Basic Exercise 2)

Tugas ini menuntut penulisan 5 kode program (atau fungsi) dengan instruksi dan _output_ yang sangat spesifik.

**1. Program Konversi Suhu** — menerima nilai Fahrenheit sebagai input, mengubahnya menjadi Celcius. Rumus: `(F - 32) * 5/9`.

```python
def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(convert_fahrenheit_to_celsius(212))  # Output: 100.0
```

**2. Program Konversi Jarak** — mengonversi **centimeter** menjadi **kilometer**, dengan format string spesifik. Input `100000` harus menghasilkan output string `"1 km"`.

```python
def cm_to_km(cm):
    km = cm / 100000
    return f"{km:g} km"   # :g menghilangkan angka nol desimal yang tidak perlu

print(cm_to_km(100000))  # Output: 1 km
```

**3. Fungsi Cek Angka (Ganjil/Genap) & Format Uang** — menerima integer `n`, mengembalikan `true` jika `n` **ganjil**, `false` jika **genap**.

> [!warning] Audio Insight — Anomali Soal: Boolean vs Format Currency
> Contoh yang diberikan di tabel soal adalah `1000 -> "Rp. 1.000,00"`. Kolom instruksi meminta logika _Boolean_ (True/False untuk ganjil/genap), namun kolom contoh meminta format _Currency_ (Rupiah). Jika ingin memenuhi semua detail secara mutlak, program ini sebaiknya berupa fungsi yang mengecek ganjil-genap TERLEBIH DAHULU, lalu mencetak angka tersebut dengan format rupiah untuk memperlihatkan kemampuan tambahan. Namun biasanya ini adalah _typo_ dari pembuat soal — sebagai _best practice_, ikuti instruksi utama di kolom Task: fokus pada logika Ganjil/Genap.

```python
def is_odd(n):
    return n % 2 != 0

print(is_odd(1000))  # Output: False (genap)
print(is_odd(7))      # Output: True (ganjil)
```

**4. Manipulasi String (Hapus Kemunculan Pertama)** — hapus kemunculan pertama dari kata yang dicari di dalam sebuah teks. Contoh: string `"Hello world"`, cari `"ell"`, hasil: `"Ho world"` (hanya "ell" pertama yang dihapus).

```python
def remove_first_occurrence(text, search):
    return text.replace(search, "", 1)

print(remove_first_occurrence("Hello world", "ell"))  # Output: Ho world
```

**5. Pengecekan Palindrome** — cek apakah sebuah string adalah palindrome. Input `'madam'` harus mengembalikan/mencetak keterangan `palindrome`.

```python
def check_palindrome(word):
    if word.lower() == word[::-1].lower():
        return "palindrome"
    return "bukan palindrome"

print(check_palindrome("madam"))  # Output: palindrome
```

> [!info] Lihat juga
> Kelima soal Python di atas memakai pola if-else, operator modulo, dan slicing string yang dibahas mendalam di [[Sesi 03 - Conditional and Loop Statement]] (khususnya studi kasus konversi suhu, cek ganjil-genap, hapus kemunculan pertama, dan palindrome yang identik di Bab 1).

---

## Bab 7 — Catatan Cepat Tambahan (Quick Notes)

Ringkasan singkat gaya catatan pribadi dari sesi kelas, melengkapi Bab 1–6 di atas dengan detail praktis yang belum disebutkan:

- **GIT** — membuat versi atas kode; bahasa konsepnya adalah _Version Control System_. Agar setiap perubahan tercatat sehingga tidak ada kode yang tertukar.
- **GITHUB** — versi cloud dari Git, sehingga bisa berkolaborasi bersama developer lain.
- **Mengapa Pakai Git?** (1) karena biasanya kita berkolaborasi, (2) untuk membantu enhance produktivitas, (3) membantu kita manage code.
- **Working With Commit:** seluruh file dalam directory bisa berada dalam dua state utama — **Tracked** & **Untracked** (belum di-_save_/dilacak). Sebuah project yang belum di-`git init`, belum masuk repository.

**Verifikasi lokasi kerja di VS Code** — sebelum `git init`, pastikan berada di folder proyek yang benar:

```bash
pwd
# menampilkan path folder aktif saat ini, untuk memastikan lokasi kerja sudah benar
# sebelum menjalankan git init -b main
```

> [!info] Lihat juga
> `pwd` (_print working directory_) melengkapi trio navigasi terminal `cd` dan `ls` yang sudah dibahas di [[Sesi 01 - Introduction to DS Python Statistics SQL Git and GitHub]] Bab 8.3.

---

## Ringkasan Sesi

Sesi 2 memberikan fondasi praktis Git & GitHub: definisi dan perbedaan Git vs GitHub, empat istilah kunci (repository, commit, branch, merge), siklus status file (untracked → modified → staged → committed), alur perintah dasar (`init`, `config`, `status`, `add`, `commit`, `diff`, `log`, `checkout`, `merge`, `remote`, `push`), hingga simulasi lengkap GitHub Flow dari pembuatan repo sampai push & merge branch. Materi Python (Tugas Besar 2) melengkapi konsep if-else dan string yang lebih dalam dibahas di [[Sesi 03 - Conditional and Loop Statement]]. Alur kerja Git ini juga menjadi rutinitas standar yang dipakai berulang sepanjang seluruh materi berikutnya, termasuk saat mengambil materi baru dengan `git pull` (lihat [[Sesi 04 - Data Types Collection Notes]] Bab 2, bagian alur kerja Git dalam pembelajaran praktis).
