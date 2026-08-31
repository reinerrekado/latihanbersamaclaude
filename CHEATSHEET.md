# Cheat Sheet Exam 1 — Module 1 (13 Sesi)

*Dibuat 2026-08-30. Sumber: `RANGKUMAN_MODULE_1.md` (rangkuman notes + Audio Insight tutor). Fokus: breadth-first buat Exam 1 (MCQ, Bahasa Inggris, 2026-09-01 19:30 WIB). Tiap sesi ada bagian "⚠️ Trap/Insight" — itu prioritas utama karena sumbernya klarifikasi LISAN dosen yang nggak ada di PDF modul resmi, kandidat kuat soal jebakan.*

*Status belajar per sesi & progress kode praktik yang selalu up-to-date ada di [PANDUAN_LANJUT_BELAJAR.md](PANDUAN_LANJUT_BELAJAR.md) — file ini murni referensi konsep, bukan tracker.*

---

## Daftar Isi & Status Sesi (per 2026-08-30)

| Sesi | Topik | Status Konsep |
|---|---|---|
| 1 | Intro DS/Python/Stats/SQL/Git | ✅ Solid (self-test web 90%) |
| 2 | Intro Git & GitHub | ✅ Solid (quiz+retest) |
| 3 | Conditional & Loop | ✅ Solid |
| 4 | Data Types Collection | ✅ Solid |
| 5 | Python Function & File Handling | ✅ Solid (quiz+retest, 2026-08-31) |
| 6 | Hackerrank Exercise | ✅ Solid (quiz+retest, 2026-08-31) |
| 7 | Object Oriented Programming | ✅ Solid (quiz+retest, 2026-08-31) |
| 8 | Python & Modular Programming | ✅ Solid (quiz+retest, 2026-09-01) |
| 9 | Intro to Database & SQL | ✅ Solid (quiz+retest, 2026-08-31) |
| 10 | SQL Working With Multiple Tables | ✅ Solid (quiz+retest, 2026-08-31) |
| 11 | Statistics Fundamental | ✅ Solid (quiz+retest) |
| 12 | Pandas & NumPy | ✅ Solid (quiz+retest, 2026-09-01 — SEMUA 13 SESI TUNTAS!) |
| 13 | Data Visualization | ✅ Solid (quiz+retest) |

**Cara pakai cheat sheet ini:** untuk sesi yang masih 🆕, ini bacaan PERTAMA kamu — jangan cuma diskim sekali, lebih baik dibaca 2x lalu coba tutup dan recall poin-poin `⚠️ Trap` dari ingatan. Untuk sesi ✅, cukup skim cepat buat refresh sebelum exam.

---

## Sesi 1 — Intro to DS, Python, Statistics, SQL, Git & GitHub

### AI vs Software Tradisional
- AI = cabang Computer Science, meniru: learning from data, recognizing patterns, understanding language, making predictions, solving problems.
- Software tradisional: rules ditulis manual programmer, kaku. AI: belajar pola dari data, adaptif ke input baru.
- Andrew Ng: "AI is the new electricity".
- AI Model Lifecycle (urutan!): **Problem Understanding → Data Preparation → Training → Evaluation → Deployment → Monitoring** (iteratif, bisa balik ke Training/Data Prep kalau hasil jelek).
- Mitos: AI Engineer TIDAK butuh jenius matematika (cuma logika+statistik dasar; calculus itu buat AI Researcher). Tidak wajib compute power tinggi (bisa pakai pre-trained model/API). AI adalah tool, bukan pengganti manusia (yang gantiin adalah orang lain yang jago pakai AI).
- NLP = bahasa (teks/suara). Computer Vision = visual (gambar/video). Compound AI/Agentic AI = gabungan NLP+CV+reasoning+external tools.

### Algoritma & Flowchart
- Algoritma = instruksi step-by-step untuk selesaikan masalah. 4 ciri: **Clear & Unambiguous, Step-by-step, Definite Start & End, Effective**.
- Flowchart shapes: **Oval**=Terminator(Start/End), **Rectangle**=Process, **Kertas robek**=Document, **Belah ketupat (diamond)**=Decision, **Jajar genjang (parallelogram)**=Data (input/output).
- Representasi algoritma: Plain Language (step list) atau Flowchart.

> ⚠️ **Trap/Insight:** Meskipun flowchart terlihat bercabang/paralel, Python (bahasa interpreted) tetap eksekusi baris-per-baris secara SERIAL/sekuensial dari atas ke bawah — percabangan cuma "pengalihan urutan", bukan eksekusi bersamaan.

### Tower of Hanoi (logika rekursif)
- 3 komponen: **Source, Target, Auxiliary/Helper**. 3 aturan mutlak: 1 disk per pindah; hanya disk teratas yang boleh diambil; disk besar tidak boleh di atas disk kecil.
- Base case: N=1 (langsung pindah Source→Target). Recursive case (N>1): pindah N-1 dari Source→Helper, pindah disk ke-N Source→Target, pindah N-1 dari Helper→Target.
- Rumus jumlah langkah minimum: **2^N − 1** (N=1→1, N=2→3, N=3→7, N=4→15).

> ⚠️ **Trap/Insight:** `N-1` pada parameter rekursif bukan sekadar pengurangan — itu strategi wajib mencapai base case. Tanpa pengurangan ini, fungsi akan memanggil dirinya sendiri selamanya (infinite recursion/infinite loop).

### Python Dasar — Environment
- Python = **High-Level Language** (dekat bahasa manusia) vs Low-Level (bahasa mesin).
- Python = **Interpreted** (eksekusi line-by-line saat runtime, development cepat, debug mudah, runtime lebih lambat) vs C/C++ = **Compiled** (kompilasi dulu ke binary, development lambat, runtime sangat cepat).
- VS Code extensions penting: Python, Jupyter, Pylance (auto-complete), Gitlens (opsional).
- Venv (bawaan Python) vs Conda/Miniconda (package+env manager lebih luas).

> ⚠️ **Trap/Insight:** Kalau sudah install Anaconda/Conda, TIDAK perlu install venv terpisah — Conda sudah include Python + environment manager sendiri.

### Variabel & Tipe Data Dasar
- Variabel = "kotak berlabel" di memori RAM; `=` adalah assignment operator.
- Aturan penamaan variabel: hanya huruf/angka/underscore, **tidak boleh diawali angka**, **case-sensitive** (`Nama` ≠ `nama`), tidak boleh pakai reserved keyword (`if`, `class`, dll), tidak boleh ada spasi/minus. Best practice: `snake_case` (PEP 8).
- Tipe data dasar: `int`, `float`, `bool` (True/False), `str`, `NoneType` (None).

> ⚠️ **Trap/Insight:** `0` (integer, ada nilainya) ≠ `None` (NoneType, benar-benar kosong/tanpa nilai). Analogi: 0 = laci berisi angka nol, None = laci benar-benar kosong.

- Truthy vs Falsy: **Falsy** = `0`, `""`, `[]`, `()`, `{}`, `None`. **Truthy** = angka selain 0 (termasuk negatif), string berisi (termasuk `"False"` sebagai teks!), koleksi berisi ≥1 elemen.
- `int(3.99)` = `3` (truncation/dipotong, BUKAN dibulatkan/rounded).

### String Methods & f-String
| Method | Fungsi |
|---|---|
| `.upper()` / `.lower()` | ubah besar/kecil huruf |
| `.strip()` | hapus spasi awal-akhir |
| `.replace(lama, baru)` | ganti substring |
| `.split()` / `.join()` | pecah jadi list / gabung list jadi string |
| `.find()` | cari index kemunculan |
| `.startswith()` / `.endswith()` | cek awalan/akhiran (True/False) |
| `.count()` | hitung kemunculan |
| `.isalpha()` / `.isdigit()` / `.isalnum()` | cek huruf/angka/alfanumerik saja |

- f-String (`f"{var}"`) lebih ringkas & cepat daripada concatenation manual (`+`) yang wajib `str()` untuk non-string. f-String bisa evaluasi ekspresi langsung: `f"{age+1}"`.
- `input()` SELALU return **string**, walau user ketik angka — wajib `int()`/`float()` untuk operasi matematika.

### Operator & Math Module
- Aritmatika: `+ - * /`, `%` (modulo/sisa bagi), `**` (pangkat), `//` (floor division/pembagian bulat).
- Augmented assignment: `n += 5` sama dengan `n = n + 5`.
- Perbandingan (`== != > < >= <=`) selalu return Boolean. Logika: `and` (keduanya True), `or` (salah satu True), `not` (kebalikan).
- `math.sqrt()`, `math.ceil()` (bulat ke atas), `math.floor()` (bulat ke bawah), `math.factorial()`, `math.pi`, `math.e`, `math.inf`, `math.nan`.

### Studi Kasus Konversi Hari (Floor Division & Modulo)
```python
years = total_days // 365
remaining = total_days % 365
months = remaining // 30
days = remaining % 30
```

> ⚠️ **Trap/Insight:** Circle area/circumference pakai `math.pi` → hasil OTOMATIS jadi **float** meski input radius-nya integer bulat (karena perkalian dengan angka desimal pi mengubah tipe data). Jangan asumsikan hasil perhitungan geometri selalu integer.

> ⚠️ **Trap/Insight:** Kalau terminal ada di direktori berbeda dari file `.py` (misal di `C:\Users\Nama` padahal file ada di Desktop), perintah `python file.py` akan GAGAL — wajib `cd` dulu ke folder yang tepat (bantu pakai Tab-completion).

---

## Sesi 2 — Intro to Git & GitHub

### Konsep Dasar
- Git = **Distributed Version Control System (VCS)**, dibuat oleh **Linus Torvalds** (juga pencipta Linux) untuk kelola development kernel Linux.
- GitHub = platform **hosting** berbasis web untuk repo Git (bukan alat VCS itu sendiri) — juga jejaring sosial developer (Pull Request, Issue Tracking, Project Management).

| Aspek | Git | GitHub |
|---|---|---|
| Sifat | Software VCS lokal | Layanan hosting cloud |
| Instalasi | Lokal di komputer | Diakses via browser |
| Internet | Tidak wajib | Wajib untuk sync |

### Analogi Pohon & 4 Istilah Kunci
- Tree = keseluruhan proyek, Branch = jalur pengembangan, Leaves = commit.
- **Repository**: folder proyek yang dilacak Git (mirip Google Drive tapi track history mendalam, bukan cuma versi terbaru).
- **Commit**: snapshot proyek di titik waktu tertentu, diidentifikasi **SHA-1 hash** (40 karakter heksadesimal).
- **Branch**: salinan jalur pengembangan independen dari main.
- **Merge**: gabungkan perubahan branch ke proyek utama; kalau ada baris kode sama yang diubah di 2 jalur berbeda → **conflict**, butuh **conflict resolution** manual.

> ⚠️ **Trap/Insight:** Git ≠ Google Docs. Google Docs = live update otomatis real-time. Git = mekanisme merge & conflict resolution MANUAL — developer harus review dulu sebelum digabung.

> ⚠️ **Trap/Insight:** Lelucon "In Case of Fire": `git commit` (amankan checkpoint lokal) → `git push` (upload ke cloud remote, aman walau laptop hancur) → `git out!` (baru menyelamatkan diri). Urutan ini menekankan commit+push dilakukan SEBELUM evakuasi fisik.

### Siklus Status Berkas & Perintah Dasar
- **Tracked** (sudah dikenal Git: unmodified/modified/staged) vs **Untracked** (belum pernah di-add, Git lihat tapi tidak pantau).

| Status | Arti |
|---|---|
| Untracked | File baru, belum direkam Git |
| Unmodified | Tracked, identik dgn commit terakhir |
| Modified | Tracked, sudah berubah, belum di-add |
| Staged | Sudah `git add`, siap commit |

- Alur: `git init` (buat repo, folder `.git` tersembunyi) → `git config --global user.name/user.email` (wajib set identitas) → `git status` → `git add <file>` atau `git add .` → `git commit -m "pesan"` → `git diff` (cek perubahan sebelum commit).
- `git remote add origin <url>` (hubungkan ke GitHub) → `git push -u origin main` (kirim ke server).
- Branch: `git checkout -b <nama>` (buat+pindah branch baru), `git checkout <nama>` (pindah branch saja), `git merge --no-ff <branch>` (paksa buat merge commit khusus agar histori percabangan terlihat jelas).
- `git log` / `git log --oneline`: lihat riwayat commit + hash. **HEAD** = penanda posisi commit saat ini (`HEAD -> main`).

> ⚠️ **Trap/Insight:** Error "no commits yet" meski file sudah ada biasanya karena lupa `git add` dulu sebelum `git commit` — tanpa add, Git tidak punya data untuk disimpan ke staging/history.

> ⚠️ **Trap/Insight:** Sebelum menjalankan script Python/perintah Git, pastikan **virtual environment** (misal `base` di Conda) aktif — ditandai nama env dalam kurung di awal baris terminal. Kalau tidak aktif, dependencies bisa tidak tersedia.

### Anatomi Perintah Git
- Struktur: `git` (program utama) + `init/status/commit/push` (sub-command) + `-b/-m/--no-ff` (flags, pakai minus) + `"pesan"/nama_branch` (arguments/target).

---

## Sesi 3 — Conditional & Loop Statement

### Function, Parameter, Return (Review)
- `def` mendeklarasikan fungsi TAPI tidak langsung jalan — logika di dalamnya baru dieksekusi saat fungsi **dipanggil**.
- `return` vs `print()`:

| | `return` | `print()` |
|---|---|---|
| Fungsi utama | Kembalikan nilai ke pemanggil | Tampilkan teks ke layar |
| Nilai | Bisa ditampung ke variabel | Return `None` (tidak bisa diolah) |
| Alur | Langsung hentikan eksekusi fungsi | Tidak pengaruhi alur |

> ⚠️ **Trap/Insight:** Kalau `result = suatu_fungsi_tanpa_return(...)`, `result` akan bernilai **None** — bukan error, tapi diam-diam salah karena fungsi tsb tidak punya `return`.

### TypeError pada String Concatenation
- `"teks" + angka_float` → **TypeError** kalau tanpa `str()` dulu. f-String tidak butuh konversi manual (otomatis internal).
- `.replace(search, "", 1)` → parameter ke-3 = batas maksimal penggantian; isi `1` = hanya ganti **kemunculan pertama** (first occurrence), sisanya tidak disentuh.

> ⚠️ **Trap/Insight:** `.index()` pada nilai yang tidak ada di tuple/list → **ValueError**, bukan return -1 atau None. Solusi aman: cek `in` dulu atau pakai `try-except`.

### Boolean, Comparison, Logical Operators
- Boolean wajib huruf kapital: `True`/`False` — `true`/`false` huruf kecil = **NameError**.
- Comparison operators (`== != > < >= <=`) selalu hasilkan Boolean.

> ⚠️ **Trap/Insight:** Python **strongly-typed**: `5 == "5"` → **False** (integer vs string dianggap tidak setara meski "nilainya sama"). Python juga **TIDAK PUNYA** operator `===` — cukup `==` karena tipe data sudah diperiksa ketat secara internal.

- `and`: True hanya jika KEDUA True. `or`: True jika SALAH SATU True. `not`: balik nilai.

> ⚠️ **Trap/Insight:** **Short-circuit evaluation**: pada `and`, kalau kondisi pertama sudah False, kondisi kedua TIDAK dievaluasi lagi (hasil pasti False). Pada `or`, kalau kondisi pertama True, langsung berhenti (tidak cek sisanya).

### Conditional Statement (if/elif/else)
- Python pakai **indentation** (bukan `{}`) untuk blok kode — standar 4 spasi/1 tab.
- `if` tunggal: maks 1 blok dieksekusi. `if-else`: pasti 1 dari 2 blok jalan. `if-elif-else`: multi-kondisi, begitu satu True → eksekusi lalu **langsung keluar** (skip elif/else sisanya) — evaluasi serial dari atas ke bawah.

> ⚠️ **Trap/Insight (Dead Code Trap):** Kalau `if x>=10: ... elif x>=15: ...` — kondisi `x>=15` TIDAK PERNAH tercapai walau x=15, karena `x>=10` sudah True duluan dan Python langsung keluar dari rantai. **Solusi**: urutkan kondisi paling SPESIFIK/ketat di atas dulu.

- Tanpa indentasi setelah `:` → **IndentationError**. Campur tab & spasi juga bisa error.

### Nested if
- Inner condition hanya dievaluasi kalau Outer condition True. Butuh **double indentation** (8 spasi/2 tab untuk level kedua).

> ⚠️ **Trap/Insight:** `if is_valid:` secara fungsional SAMA DENGAN `if is_valid == True:` tapi versi pertama lebih "pythonic" — sering muncul sebagai soal gaya/best practice, bukan soal salah-benar logika.

> ⚠️ **Trap/Insight:** Memanggil fungsi yang belum didefinisikan di atasnya → **NameError: name 'x' is not defined**. Urutan definisi fungsi vs pemanggilan itu penting di Python nyata (beda dari pseudocode yang boleh abstrak).

### Looping (for vs while)
| Fitur | for Loop | while Loop |
|---|---|---|
| Kapan pakai | Jumlah iterasi PASTI diketahui | Jumlah iterasi TIDAK pasti, bergantung kondisi |
| Cara berhenti | Otomatis saat iterable habis | Saat kondisi jadi False |
| Contoh kasus | Iterasi list/string/range | Retry logic, game loop, tunggu input |
| break/continue/else | Didukung | Didukung |

> ⚠️ **Trap/Insight:** Looping ≠ Recursion. Recursion = fungsi panggil dirinya sendiri, butuh stack memory baru tiap panggilan. Looping = linear, satu scope eksekusi, jauh lebih hemat memori.

- `range(start, stop, step)`: **stop selalu eksklusif** (tidak diikutkan). `range(10)` → 0-9 saja. `start` default 0, `step` default 1, hanya `stop` yang wajib diisi.
- Iterable types: string (per karakter), list, tuple, **dict (default iterasi cuma keys!)**, set, range.
- `enumerate(iterable, start=N)` → hasilkan tuple `(index, element)`. Parameter `start` HANYA ubah tampilan angka, TIDAK skip elemen pertama.
- Dict iteration: default = `for key in dict` (keys saja). `.keys()`, `.values()`, `.items()` (pasangan key-value sebagai tuple).
- `pass` = null statement, placeholder biar sintaks valid saat blok kosong (beda dari `continue` yang skip sisa iterasi).

> ⚠️ **Trap/Insight:** Variabel loop (`for number in range(10)`) TIDAK dihapus setelah loop selesai — tetap menyimpan nilai TERAKHIR yang diproses (misal 9) dan bisa diakses setelahnya.

### while, break, continue, else-in-loop
- Infinite loop terjadi kalau lupa update variabel kontrol. Hentikan paksa: `Ctrl+C` di terminal.
- `break`: hentikan SELURUH loop seketika. `continue`: skip sisa iterasi ini, lanjut ke iterasi berikutnya (evaluasi ulang kondisi).

> ⚠️ **Trap/Insight:** Kalau update variabel kontrol diletakkan SETELAH `continue`, kode itu tidak akan pernah tereksekusi → infinite loop. Update wajib diletakkan SEBELUM `continue`.

> ⚠️ **Trap/Insight (paling sering jadi jebakan MCQ):** blok `else` pada loop (for/while) HANYA jalan kalau loop selesai NORMAL (kondisi jadi False / iterable habis). Kalau loop dihentikan pakai `break`, blok `else` **TIDAK PERNAH dieksekusi** — sama sekali beda dari else pada if biasa.

### Poin Tambahan dari Soal Latihan
- Cek `number == 0` harus di paling ATAS sebelum cek modulo genap — kalau tidak, `0 % 2 == 0` bikin 0 salah terdeteksi sebagai "even" padahal harusnya "zero".
- Hindari `return print(...)` — pilih salah satu: `return` (kirim nilai) ATAU `print()` (tampilkan), jangan digabung.
- Rentang inklusif di `range()` wajib `upper + 1` karena stop eksklusif.
- Cegah **ZeroDivisionError**: cek `count == 0` dulu sebelum `total/count`.

---

## Sesi 4 — Data Types Collection (list/tuple/set/dict)

*(Sesi ini sudah dipraktikkan penuh lewat 12 file kode `collection-data-type/` — lihat [PANDUAN_LANJUT_BELAJAR.md](PANDUAN_LANJUT_BELAJAR.md) untuk detail gap yang sudah ditambal.)*

### Kategori & Mutability (Tabel Utama)
| Type | Class | Category | Mutable? |
|---|---|---|---|
| range | `range` | sequence | **No** |
| tuple | `tuple` | sequence | **No** |
| list | `list` | sequence | **Yes** |
| dict | `dict` | mapping | **Yes** |
| set | `set` | set | **Yes** |
| frozenset | `frozenset` | set | **No** |

> ⚠️ **Trap/Insight (mutable = unhashable):** Mutable (list, set, dict) TIDAK BISA jadi dict key atau elemen set (unhashable). Immutable (tuple, frozenset, string, angka) BISA jadi dict key/elemen set (hashable). Contoh: set tidak bisa langsung berisi set lain — set dalam harus dibungkus `frozenset()` dulu.

### List
- `[...]`, ordered, zero-based index, **mutable**, boleh mixed types & nested list.
- Tambah elemen: `.append(item)` (di akhir), `.insert(index, item)` (sisip di posisi), `.extend(iterable)` (unpack & gabung sejajar).
- Hapus elemen: `.pop(index)` (return nilai yg dihapus, default hapus terakhir), `.remove(value)` (**ValueError** kalau value tidak ada), `.clear()` (kosongkan).
- `list_b = list_a` → REFERENSI (id sama, `list_b` berubah → `list_a` ikut berubah). `list_b = list_a.copy()` → **shallow copy** (id beda, independen).

> ⚠️ **Trap/Insight (`.append()` vs `.extend()`):** `.append(list_lain)` → list_lain masuk utuh sebagai SATU elemen nested (`[4,5,6,[1,2,3]]`). `.extend(list_lain)` → elemen list_lain dibongkar & digabung sejajar (`[4,5,6,1,2,3]`). Sering jadi soal trik "apa outputnya?".

> ⚠️ **Trap/Insight (`is` vs `==`):** `==` cek KESAMAAN NILAI. `is` cek KESAMAAN ALAMAT MEMORI (`id()`). Dua list dengan isi sama tapi hasil `.copy()` → `==` True, tapi `is` **False**.

### Tuple
- `(...)`, ordered, zero-based index, **immutable** (read-only), no `.append()/.pop()`.
- Metode terbatas: `.index(value)` (**ValueError** kalau tidak ketemu), `.count(value)`, `len()`.
- Cocok untuk data konstan: geolocation `(-6.2, 106.8)`, RGB `(255,255,255)`.
- Tuple kosong: `tuple()` atau `()`.

> ⚠️ **Trap/Insight (Single-item tuple):** WAJIB pakai koma: `(5,)` = tuple. `(5)` TANPA koma = dianggap Python sebagai integer biasa (parenthesis grouping matematika), BUKAN tuple! Ini salah satu jebakan MCQ paling klasik.

### Indexing vs Slicing (List & Tuple)
- Indexing: `list[i]` — index positif mulai 0 dari kiri, index negatif mulai -1 dari kanan.
- Slicing: `list[start:stop:step]` — start inklusif, **stop eksklusif**, step default 1.

| Operasi | Contoh out-of-range | Perilaku |
|---|---|---|
| **Indexing** | `students[10]` (list isi 4) | **CRASH** → `IndexError: list index out of range` |
| **Slicing** | `students[10:]` | **AMAN**, return koleksi kosong `[]` (atau `()` untuk tuple) — tidak error |

> ⚠️ **Trap/Insight (paling penting Sesi 4):** Indexing dan Slicing beda total soal out-of-range! Index tunggal di luar batas → error. Slice di luar batas → tetap jalan, hasilnya kosong (fail-safe by design). Jangan tertukar.

> ⚠️ **Trap/Insight (step=1, gampang salah kira):** Kalau step default (1), slice mengambil **SEMUA** index dari start sampai TEPAT SEBELUM stop — tidak ada yang dilewatkan. Jangan kira slice cuma ambil "titik awal + titik akhir" doang.

### Set
- `{val1, val2}`, **unordered**, **unindexed** (tidak bisa `my_set[0]` → **TypeError: not subscriptable**), otomatis buang duplikat, **mutable**.

> ⚠️ **Trap/Insight (jebakan klasik):** `{}` KOSONG = **dictionary kosong**, BUKAN set kosong! Untuk set kosong WAJIB pakai `set()`. Ini sering jadi soal trik langsung.

- Tambah: `.add(item)` (satu), `.update(iterable)` (banyak sekaligus).
- Hapus: `.remove(value)` → **KeyError** kalau tidak ada. `.discard(value)` → AMAN, tidak error kalau tidak ada. `.pop()` → hapus elemen ACAK (set unordered, tidak bisa diprediksi). `.clear()`.

> ⚠️ **Trap/Insight (`.remove()` vs `.discard()`):** `.remove()` = berisiko crash (`KeyError`) kalau value tidak ditemukan. `.discard()` = versi aman, diam saja kalau value tidak ada.

- Set operations:

| Operasi | Method | Operator | Arti |
|---|---|---|---|
| Union | `.union()` | `\|` | gabung semua elemen unik |
| Intersection | `.intersection()` | `&` | elemen ada di keduanya |
| Difference | `.difference()` | `-` | elemen A tapi tidak di B |
| Symmetric Difference | `.symmetric_difference()` | `^` | elemen unik masing2 (tidak beririsan) |

- Relasi: `.issubset()`/`<=`, `.issuperset()`/`>=`, **proper subset `<`** (subset TAPI harus beda, tidak boleh identik — beda dari `<=` yang boleh identik), proper superset `>`.
- Konversi: `set(list)` hapus duplikat; `list(set)` balik ke list TAPI urutan asli duplikat sudah hilang permanen (destruktif).

### Dictionary
- `{key: value}`, key harus **unik & hashable** (immutable type), value bebas apa saja & boleh duplikat, **mutable**.
- Dict kosong: `{}` atau `dict()` — KEDUANYA valid untuk dict (beda dari set!).

> ⚠️ **Trap/Insight (duplicate key):** Kalau ada key sama saat deklarasi dict, TIDAK ADA ERROR — nilai TERAKHIR yang menang/overwrite nilai sebelumnya secara diam-diam.

- Akses: `dict["key"]` → **KeyError** kalau key tidak ada. `.get(key, default)` → AMAN, return default (atau `None` kalau default tidak diisi), tanpa error.

| Metode | Fungsi |
|---|---|
| `.update({...})` | tambah/update BANYAK pasangan, AGRESIF (selalu timpa jika key ada) |
| `.setdefault(key, val)` | tambah HANYA JIKA key belum ada, PASIF (tidak timpa jika sudah ada) |
| `.keys()` / `.values()` / `.items()` | ambil keys / values / pasangan (key,value) sebagai tuple |
| `.pop(key)` | hapus by key, return value-nya |
| `.popitem()` | hapus & return pasangan TERAKHIR yang dimasukkan (LIFO) |
| `.clear()` | kosongkan jadi `{}` |
| `.copy()` | shallow copy ke alamat memori baru (independen dari aslinya) |

> ⚠️ **Trap/Insight (`.update()` vs `.setdefault()`):** `.update()` = agresif, selalu timpa. `.setdefault()` = defensif, cuma nambah kalau key belum ada.

> ⚠️ **Trap/Insight (`sorted()` pada dict):** `sorted(my_dict)` HANYA mengurutkan & mengembalikan **KEYS SAJA** sebagai List baru — values TIDAK ikut, dict aslinya TIDAK berubah.

> ⚠️ **Trap/Insight:** Syntax `dict[key] = value` bisa UPDATE (kalau key sudah ada) atau MENAMBAH key baru (kalau belum ada) — sama persis syntax-nya, hasilnya tergantung status key SEBELUM baris itu dijalankan.

### Perbandingan Cepat 4 Koleksi
| | List | Tuple | Set | Dict |
|---|---|---|---|---|
| Simbol | `[]` | `()` | `{}` (isi) | `{k:v}` |
| Kosong | `[]`/`list()` | `()`/`tuple()` | **`set()` wajib** (`{}` = dict!) | `{}`/`dict()` |
| Ordered? | Ya | Ya | **Tidak** | Ya (insertion order, Python 3.7+) |
| Mutable? | Ya | **Tidak** | Ya | Ya |
| Duplikat? | Boleh | Boleh | **Tidak** (auto-unique) | Key tidak boleh, value boleh |
| Index/Key access | `[i]` index | `[i]` index | **Tidak bisa** (unindexed) | `[key]` atau `.get()` |

### HackerRank (Praktik)
- Platform latihan coding + saringan rekrutmen teknis AI Engineer. Daftar via **"For Developers"** (bukan "For Employers"). Filter latihan: Difficulty=Easy, Subdomain=Python Basic. Metrik **Success Rate** tinggi = soal lebih mudah/populer.

---

## Sesi 5 — Python Function & File Handling

### Function dasar (`def` vs `lambda`)
- Function = blok kode reusable untuk 1 tugas spesifik. Dibuat kalau logikanya akan **dipakai berulang**.
- Dua cara bikin function: keyword `def` (standar) atau `lambda` (anonymous, 1 baris expression saja).
- `def nama_fungsi():` → Python bikin **function object** di memori, nama fungsi = pointer ke objek itu.
- Built-in functions (langsung ada tanpa import): `print()`, `len()`, `input()`, `range()`.

> ⚠️ **Trap:** Menulis nama fungsi **tanpa** kurung (`print(greet)`) hanya menampilkan representasi objek (`<function greet at 0x...>`), BUKAN menjalankan logikanya. Harus pakai `greet()` (dengan kurung) untuk eksekusi.

**Parameter vs Argument**
| Istilah | Definisi |
|---|---|
| Parameter | Placeholder di dalam `()` saat definisi fungsi |
| Argument | Nilai nyata yang dikirim saat pemanggilan |

- Default value: `def greet(name="Bob", time=None):` → kalau argumen tidak dikirim, pakai default.

> ⚠️ **Trap:** `if time:` dengan default `time=None` → `None` dievaluasi sebagai **False**, jadi masuk ke `else`.

**return vs print()** — `print()` cuma tampilkan ke layar, nilainya tidak bisa disimpan/dipakai lagi. `return` mengirim nilai balik ke pemanggil.

**lambda**
```python
lambda_fn = lambda num1, num2: num1 + num2
```
Anonymous function, hanya untuk logika 1 baris.

**Clean function rules**: nama fungsi deskriptif, nama parameter bermakna, **type hint** (`data: list -> float`), **docstring** (`"""..."""`).

> ⚠️ **Trap paling penting:** **Type hint TIDAK memicu error saat runtime** kalau tipe datanya beda. Type hint cuma dokumentasi, BUKAN validasi. Kalau mau validasi beneran, pakai `try`/`except`.

### Namespace & Scope
3 tingkat: **Built-in** (otomatis) → **Global** (level modul/file) → **Local** (dalam fungsi, hilang setelah fungsi selesai).

| | Global Variable | Local Variable |
|---|---|---|
| Lokasi | Di luar fungsi | Di dalam fungsi |
| Akses | Dari mana saja di file yang sama | Hanya dari dalam fungsi tsb |
| Lifetime | Selama program berjalan | Hanya selama fungsi dieksekusi |

> ⚠️ **Trap:** Variabel nama sama di scope beda (global `message` dan local `message`) dianggap Python sebagai **2 variabel berbeda total** — tidak error, tidak tumpang tindih.

**`global` keyword**: perlu dideklarasikan eksplisit untuk **mengubah** variabel global dari dalam fungsi.
> ⚠️ **Trap klasik (UnboundLocalError):** `position = 0` (global). Di dalam `move_forward(): position += 1` **tanpa** `global position` → Python anggap `position` local variable baru tapi belum ada nilainya → `UnboundLocalError`.

**`nonlocal` keyword**: khusus **nested function**, mengakses/mengubah variabel di enclosing function (1 tingkat di atas), BUKAN ke global.

### Nested, Callback, Recursive Function
| Jenis | Definisi | Ciri Khas |
|---|---|---|
| **Nested Function** | Fungsi di dalam fungsi (helper) | Hanya ada saat outer function jalan; TIDAK bisa dipanggil dari luar |
| **Callback Function** | Fungsi dikirim sebagai argumen ke fungsi lain | Fungsi penerima yang kontrol kapan callback dieksekusi |
| **Recursive Function** | Fungsi manggil dirinya sendiri | Wajib ada **Base Case** (stop) + **Recursive Case** |

> ⚠️ **Trap:** Manggil nested function langsung dari luar outer function → `NameError`.

> ⚠️ **Trap penting (callback):** Saat melempar fungsi sebagai argumen callback, **nama fungsi TANPA kurung** (`tambah`, bukan `tambah()`). Kalau pakai kurung, Python mengeksekusi duluan dan mengirim HASILNYA, bukan referensi fungsi.

| | Recursive | Iterative (loop) |
|---|---|---|
| Stop | Base Case eksplisit | Kondisi loop `False` |
| Memori | Boros (Call Stack) | Efisien |
| Risiko gagal | **Stack Overflow**/crash | Infinite loop |

> ⚠️ **Trap bug klasik (`is_prime`):** Kalau `return True` diletakkan **di dalam** loop `for` (bukan setelah loop selesai), function langsung return True di iterasi pertama tanpa cek pembagi lain → salah deteksi prima.

### File Handling
Alur: **Open** (`open()`) → **Read/Write** → **Close** (`.close()`).

| Mode | Nama | Perilaku |
|---|---|---|
| `"r"` | Read | File harus sudah ada, kalau tidak → `FileNotFoundError` |
| `"w"` | Write | Isi lama **dihapus total** (truncated); kalau belum ada, dibuat baru |
| `"a"` | Append | Ditambah di akhir, data lama aman; kalau belum ada, dibuat baru |

```python
with open("data.txt", "w") as file:
    file.write("Hello, Python!")
# file otomatis tertutup di luar blok with, bahkan kalau ada error
```
> ⚠️ **Trap:** Lupa `\n` → teks berikutnya nempel di baris yang sama.

> ⚠️ **Trap penting `with`:** Best practice dibanding `open()`+`.close()` manual — `with` menjamin file **selalu** ditutup otomatis walau ada exception di tengah jalan (mencegah memory leak/file corrupt).

---

## Sesi 6 — Hackerrank Exercise

Konteks: latihan practical menerapkan konsep list/dict/lambda untuk soal ala technical test.

### Pola-pola penting
**Runner-Up Score** (nilai tertinggi ke-2):
```python
arr = map(int, input().split())
unique_scores = sorted(set(arr))
print(unique_scores[-2])   # index -2 = terbesar kedua
```
**Nested List/second lowest grade**: sama tapi index `[1]` dari `sorted(set(...))`. Pendekatan Dictionary (skor→list nama) direkomendasikan untuk data besar.

**Company Logo** (top-3 huruf paling sering muncul):
```python
result = sorted(letter_counter.items(), key=lambda x: (-x[1], x[0]))
# -x[1] → count descending; x[0] → huruf ascending sbg tie-breaker
```

### Tabel fungsi/method kunci
| Fungsi | Kegunaan |
|---|---|
| `.split()` | Pecah string jadi list (default: whitespace) |
| `map(fn, iterable)` | Terapkan fungsi ke tiap elemen — **lazy** |
| `set()` | Buang duplikat |
| `sorted(x, key=...)` | Urutkan, bisa custom key pakai `lambda` |
| `.items()` | Ambil pasangan key-value dari dict |

> ⚠️ **Trap paling sering ditanya:** `map()` bersifat **lazy** — proses konversi tidak langsung jalan, baru dieksekusi saat hasilnya benar-benar dipakai (dikonversi ke `list`/`set`). Buktinya:
> ```python
> hasil = map(str, [1,2,3])
> print(hasil)          # <map object at 0x...> — BUKAN ['1','2','3']!
> print(list(hasil))    # ['1', '2', '3'] — baru sekarang beneran diproses
> ```

> ⚠️ **Trap:** `set()` **krusial** untuk soal runner-up/nilai-kedua — kalau ada skor tertinggi yang duplikat, tanpa `set()` juara kedua yang asli bisa tidak ketemu.

> ⚠️ **Trap constraints HackerRank:** Batasan soal (constraints) adalah jaminan sistem — tidak perlu validasi manual (`if N < 2`) kecuali diminta eksplisit.

---

## Sesi 7 — Object Oriented Programming (OOP)

### Konsep dasar OOP
- OOP = paradigm mengorganisasi kode di sekitar **objects** (data), bukan di sekitar functions/logic.
- **Attributes** = data/state object. **Methods** = behavior/function yang menempel ke object.

| | Procedural | OOP |
|---|---|---|
| Fokus | Functions & logic | Objects & data |
| Data + Function | Terpisah | Digabung dalam 1 class unit |
| Akses function | Bebas oleh siapa saja | Method eksklusif milik object-nya |

> ⚠️ **Trap scope materi (penting utk exam AI Engineering):** Fokus materi HANYA: **Class, Object, Attributes, Methods, Basic Inheritance**. Konsep lanjutan (**Encapsulation, Abstraction, Polymorphism**) SENGAJA tidak didalami di kelas ini.

> ⚠️ **Trap tersembunyi:** List dan dictionary itu sendiri adalah **Class** — `my_list = []` sama dengan memanggil **constructor** class `list`.

### Class & Object
- **Class** = blueprint. **Object** = instance spesifik hasil instansiasi class.

```python
class Car:
    def move_forward(self):
        self.position += 1
car_john = Car()
car_emily = Car()
```
> ⚠️ **Trap:** `car_john is car_emily` → **False**. Tiap object punya alamat memori terpisah & state independen.

### Constructor `__init__` dan `self`
- `__init__` = special/magic method (constructor), jalan **otomatis** saat object dibuat.
```python
class Car:
    def __init__(self, type_name, color):
        self.type_name = type_name
        self.color = color
```
> ⚠️ **Trap:** Manggil `Car("sedan", "red")` **otomatis memicu** `__init__` — tidak perlu dipanggil eksplisit.

- **self** = referensi ke current object. Parameter pertama tiap method WAJIB `self`.

| Sintaks Panggil | Interpretasi Internal |
|---|---|
| `car_john.move_forward(10)` | `Car.move_forward(car_john, 10)` |

> ⚠️ **Trap sering disalahpahami:** Nama parameter di `__init__` TIDAK HARUS SAMA dengan nama attribute setelah `self.` — cuma konvensi umum.

> ⚠️ **Trap desain:** Kalau attribute dikunci ke default value yang tidak bisa dikustomisasi user (misal `balance` selalu mulai 0), JANGAN masukkan sebagai parameter `__init__` — cukup `self.balance = 0` langsung.

### Methods
- Method: eksklusif milik class, menempel ke object, tidak bisa dipanggil tanpa object.

### Inheritance (Basic)
- Child class dibangun dari parent class → hubungan **"is-a"**. Manfaat: Code Organization, Reusability, Extensibility.
```python
class MachineLearningModel:
    def __init__(self, task): self.task = task

class RegressionModel(MachineLearningModel):
    def __init__(self, train_data):
        super().__init__(task="regression")
        self.error_function = "r2"
```
- `super().__init__()` = panggil constructor parent DULU, baru tambah attribute spesifik child.

> ⚠️ **Trap:** Object child punya akses PENUH ke attribute/method parent SEKALIGUS miliknya sendiri. Tapi method spesifik 1 child class TIDAK ADA di child class lain (sibling) — inheritance mencegah fungsi tidak relevan "bocor" ke class yang salah.

### `if __name__ == '__main__'`
| Kondisi | Nilai `__name__` | Blok `if` dieksekusi? |
|---|---|---|
| File dijalankan langsung | `"__main__"` | Ya |
| File diimpor sebagai module | Nama modul itu sendiri | Tidak |

> ⚠️ **Trap:** Nilai `"__main__"` konseptual, TIDAK bergantung nama fisik file.

---

## Sesi 8 — Python & Modular Programming

### Modular vs Monolithic
- **Monolitik** = semua di 1 file. **Modular** = dipecah jadi modul-modul kecil reusable.
- 5 masalah monolitik: sulit dibaca, maintain, debug, reuse, kolaborasi (merge conflict).

> ⚠️ **Trap evaluasi:** Modularisasi **menambah kompleksitas** (path, import). Untuk script kecil sekali-pakai, jangan dipaksakan modular.

### Module & Cara Import
| Metode | Sintaks Import | Cara Panggil |
|---|---|---|
| Import seluruh modul | `import calculator` | `calculator.add(2,3)` (wajib prefix) |
| Import spesifik | `from calculator import add` | `add(2,3)` langsung |

> ⚠️ **Trap:** Pakai `import calculator` tapi manggil `add(2,3)` tanpa prefix → `NameError`.

### Organisasi Proyek: Project > Package > Module
| Istilah | Definisi | Representasi Fisik |
|---|---|---|
| **Project** | Aplikasi/library lengkap | Root folder |
| **Package** | Kumpulan modul terkait | Folder + wajib `__init__.py` |
| **Module** | 1 file kode reusable | File `.py` |

> ⚠️ **Trap (alias `as`):** Kalau variabel lokal (`model = "..."`) nama SAMA PERSIS dengan module yang diimpor (`import model`), Python anggap `model` = string itu, bukan modul. Solusi: `import model as model_modul`.

### `if __name__ == "__main__"` sebagai Name Guard
> ⚠️ **Trap KUNCI (paling sering disalahpahami):** Name guard HANYA memblokir baris eksekusi langsung (print, test call) — **TIDAK memblokir definisi function/class**. Function tetap terdaftar penuh & tetap bisa diimpor file lain walau ada name guard.

### Package
- Package = folder + wajib `__init__.py` (boleh kosong). Tanpa itu → dianggap folder biasa, import gagal.

| | Deep Import | Shallow Import |
|---|---|---|
| Sintaks | `from package.module import function` | `from package import function` |
| Syarat | Jalan meski `__init__.py` kosong | Wajib expose function di `__init__.py` |

> ⚠️ **Trap:** Kalau baris export di `__init__.py` dihapus, shallow import error `cannot import name 'x'`.

### Tips & Best Practices
| Prinsip | Maksud |
|---|---|
| **Single Responsibility** | 1 modul/fungsi = 1 tanggung jawab |
| **Avoid Circular Imports** | file_A import file_B DAN file_B import file_A → error. Solusi: modul utilitas ketiga |
| **Avoid Hardcoding** | Pakai parameter, jangan kunci nama file/value statis |

---

## Sesi 9 — Intro to Database & SQL

### Database & DBMS
- **Database** = organized collection of related data. **DBMS** = software perantara user↔database.
- Fungsi DBMS: **correlate, query, report**. Analogi: DBMS/SQL ≈ Excel Pivot tapi jauh lebih cepat untuk data besar.

> ⚠️ **Trap:** DBMS bantu pahami data rumit, tapi kalau kompleksitas terlalu tinggi tetap butuh alat visualisasi tambahan.

### Tools & Koneksi
- Parameter wajib: **DBMS type, Host** (`localhost`), **Port** (`3306` MySQL, `5432` PostgreSQL), **Username** (`root`), **Password**.
- GUI: MySQL Workbench (khusus MySQL), DBeaver (multi-DBMS). SQL **indentation-insensitive**.

> ⚠️ **Trap:** DBeaver perlu **Refresh (F5)** setelah bikin database baru. PowerShell: simbol `<` untuk import file SQL di-reserve → ERROR, pakai CMD. Ada database sistem bawaan **`sys`** otomatis muncul.

### DDL vs DML
| Kategori | Perintah | Fungsi |
|---|---|---|
| **DDL** | `CREATE DATABASE/TABLE` | Buat struktur baru |
| DDL | `ALTER` | Ubah struktur tabel |
| DDL | `DROP` | Hapus permanen (tabel+isinya), tidak bisa undo |
| DDL | `DESCRIBE table` | Tampilkan struktur kolom |
| **DML** | `SELECT` | Ambil/tampilkan data |
| DML | `INSERT INTO` | Tambah baris baru |
| DML | `UPDATE` | Ubah baris yang ada |
| DML | `DELETE` | Hapus baris |

> ⚠️ **Trap:** Urutan wajib `CREATE DATABASE` → `USE` → `CREATE TABLE`. Kolom baru default **nullable & tanpa PK** kecuali didefinisikan eksplisit. **BAHAYA FATAL: `UPDATE`/`DELETE` tanpa `WHERE`** = ubah/hapus SELURUH baris tabel!

### Filtering (WHERE, LIKE, BETWEEN)
- `WHERE` filter baris. Angka tanpa kutip, string wajib kutip satu.
- `LIKE`: `%` = 0/banyak karakter apa saja, `_` = tepat 1 karakter.
- `BETWEEN a AND b` = **inklusif** (a dan b ikut termasuk).

> ⚠️ **Trap (case sensitivity):** Keyword & nama kolom = case-insensitive. Nama database/tabel: case-sensitive di **Linux**, TIDAK sensitive di **Windows/macOS**.

### Sorting (ORDER BY, LIMIT)
- `ORDER BY` default **ASC**. `LIMIT n` diletakkan paling akhir.

> ⚠️ **Trap KLASIK:** Nama kolom/alias di `ORDER BY` **DILARANG** dibungkus kutip satu — kalau dikutip, dibaca sebagai string literal konstan, bukan nama kolom. `ORDER BY Selisih DESC` (tanpa kutip), bukan `ORDER BY 'Selisih'`.

### Built-in Functions
| Jenis | Ciri | Contoh |
|---|---|---|
| **Aggregate** | Operasi SEKUMPULAN nilai → 1 hasil | `SUM, COUNT, AVG, MIN, MAX` |
| **Scalar** | Operasi per-baris individual | `ROUND, LENGTH, UCASE, LCASE` |

> ⚠️ **Trap PALING SERING:** Fungsi agregat mengabaikan NULL, **kecuali `COUNT(*)`**. `LENGTH()` itu SCALAR bukan aggregate — filter pakai `WHERE LENGTH(Name)=6` langsung, BUKAN `GROUP BY...HAVING LENGTH(...)`.

### GROUP BY & HAVING
| | `WHERE` | `HAVING` |
|---|---|---|
| Kapan | Sebelum grouping | Setelah grouping |
| Fungsi agregat? | TIDAK BISA | BISA |
| Objek | Baris individual | Kelompok hasil agregasi |

> ⚠️ **Trap:** `WHERE AVG(x) > 100` = ERROR (agregat belum ada sebelum grouping). Harus pakai `HAVING`.

### Date & Time Functions
- `YEAR(), MONTH(), DAY(), DAYOFWEEK(), HOUR()` dll → hasil **integer**. `DAYNAME(), MONTHNAME()` → hasil teks.

### Subquery (Nested SELECT)
- Query di dalam query. Inner dieksekusi duluan, hasil dipakai outer.

> ⚠️ **Trap KUNCI kenapa subquery dipakai:** `WHERE Salary < AVG(Salary)` = SALAH (agregat tidak bisa langsung di WHERE). Solusi: `WHERE Salary < (SELECT AVG(Salary) FROM employees)`. *(Catatan: materi tidak eksplisit bahas "correlated vs non-correlated subquery" — semua contoh non-correlated.)*

---

## Sesi 10 — SQL Working With Multiple Tables

### Relational Model Constraints
| | Primary Key (PK) | Foreign Key (FK) |
|---|---|---|
| Keunikan | **Wajib unik** | Boleh duplikat |
| NULL | **TIDAK BOLEH** | Boleh (tergantung aturan) |
| Fungsi | Identifikasi baris | Hubungkan 2 tabel |

- **Composite PK**: gabungan 2+ kolom, dipakai di tabel riwayat/transaksi (contoh: `salaries` PK = `employee_number` + `from_date`).
- Relationship: One-to-One, One-to-Many, Many-to-Many (wajib **bridge/junction table**).

### Implicit vs Explicit JOIN
| | Implicit | Explicit |
|---|---|---|
| Sintaks | Koma di `FROM`, key di `WHERE` | Keyword `JOIN...ON` |
| Rekomendasi | Sulit dibaca | **Direkomendasikan industri** |

> ⚠️ **Trap BAHAYA CARTESIAN PRODUCT:** Implicit JOIN tanpa kondisi key di `WHERE` → SETIAP baris tabel 1 dikawinkan SETIAP baris tabel 2 (contoh: 599 × 16.044 = ~9,6 juta baris sampah).

### INNER / LEFT / RIGHT / FULL JOIN
| JOIN | Hasil |
|---|---|
| **INNER** (`JOIN` saja = INNER default) | Hanya baris cocok di KEDUA tabel |
| **LEFT** | SEMUA baris kiri + cocok dari kanan (NULL kalau tidak cocok) |
| **RIGHT** | SEMUA baris kanan + cocok dari kiri |
| **FULL** | Gabungan LEFT+RIGHT, semua baris kedua tabel |

> ⚠️ **Trap sering ditanya:** `A RIGHT JOIN B` SELALU bisa ditulis ulang `B LEFT JOIN A` (hasil identik, tukar posisi tabel). Industri lebih suka LEFT JOIN.

### Self JOIN
- Join tabel dengan dirinya sendiri, WAJIB 2 alias berbeda (`T1`, `T2`).
```sql
SELECT K1.nama, K2.nama, K1.gaji
FROM karyawan K1
JOIN karyawan K2
  ON K1.karyawan_id <> K2.karyawan_id AND K1.gaji = K2.gaji;
```
> ⚠️ **Trap:** Kondisi `<>` (tidak sama dengan) MUTLAK perlu di Self JOIN — tanpa itu, tiap baris berpasangan dengan dirinya sendiri. Alias (`K1`/`K2`) juga MUTLAK, bukan opsional seperti di JOIN biasa — tanpa alias, `FROM karyawan JOIN karyawan ON ...` langsung **SQL ERROR** ("Not unique table/alias") karena database nggak bisa bedain "karyawan yang mana" dirujuk di tiap kolom.

### Clause Execution Order — JEBAKAN UJIAN KLASIK
| Urutan Penulisan | Urutan Eksekusi Logis |
|---|---|
| SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT | **FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT** |

> ⚠️ **Trap:** `WHERE` dieksekusi SEBELUM grouping & SEBELUM `SELECT` menghitung nilai — makanya `WHERE` tidak bisa pakai agregat/alias hasil SELECT. `HAVING` dieksekusi setelah grouping.

### Python MySQL Connector
```python
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='pass', database='sakila')
```
- Alur: `cursor()` → `execute(query)` → `fetchall()` → `pd.DataFrame(result, columns=mycursor.column_names)`.
> ⚠️ **Trap keamanan:** JANGAN hardcode password — simpan di `.env` (masuk `.gitignore`), load pakai `python-dotenv`.

### Ringkasan Trap SQL Paling Mungkin Muncul
1. `ORDER BY` alias jangan pakai kutip satu.
2. Agregat tidak bisa langsung di `WHERE` → subquery/`HAVING`.
3. `LENGTH()` = scalar, filter di `WHERE` bukan `HAVING`.
4. Agregat abaikan NULL, kecuali `COUNT(*)`.
5. Implicit JOIN tanpa `WHERE` = Cartesian Product.
6. `RIGHT JOIN A,B` = `LEFT JOIN B,A`.
7. `UPDATE`/`DELETE` tanpa `WHERE` = ubah/hapus SEMUA baris.
8. `BETWEEN` inklusif.
9. Nama tabel/db case-sensitive di Linux saja.
10. Derived table (subquery di `FROM`) wajib alias di MySQL.
11. PK: unique+NOT NULL. FK: boleh duplikat+NULL.
12. Self JOIN wajib 2 alias + `<>`.

---

## Sesi 11 — Statistics Fundamental

### Definisi & Alur Kerja
- **Statistics** = seni & sains "belajar dari data": collecting, analyzing, interpreting, drawing conclusion.
- 3 tahap: **Design** → **Description** → **Inference**.
- Aplikasi: Experimental Design (A/B Testing), Survey (Quick Count), Research, Quality Control.

> ⚠️ **Trap:** *Quick Count* ≠ *Real Count* — quick count = SAMPEL, real count = POPULASI. Ini contoh Inferential Statistics.

### 2 Cabang Statistik
| Cabang | Fokus |
|---|---|
| **Descriptive** | Merangkum data yang ADA — tanpa prediksi |
| **Inferential** | Pakai SAMPEL buat menyimpulkan POPULASI |

### Klasifikasi Variabel
```
Qualitative (Categorical): Nominal (TANPA urutan) | Ordinal (ADA urutan, jarak tak terukur)
Quantitative (Numerical): Discrete (hasil MENGHITUNG, integer) | Continuous (hasil MENGUKUR, bisa desimal)
```
> ⚠️ **Trap:** "Nominal" ≠ nominal uang — di statistik = kategori tanpa urutan.

### Skala Pengukuran (hierarki rendah→tinggi)
| Scale | Classify | Order | Distance | Zero | Kali/Bagi |
|---|:-:|:-:|:-:|:-:|:-:|
| Nominal | ✓ | ✗ | ✗ | ✗ | ✗ |
| Ordinal | ✓ | ✓ | ✗ | ✗ | ✗ |
| **Interval** | ✓ | ✓ | ✓ | Non-absolute | ✗ |
| **Ratio** | ✓ | ✓ | ✓ | Absolute | ✓ |

> ⚠️ **Trap paling sering ketuker:** Suhu Celsius = **Interval** (0°C masih ada suhunya, bisa negatif). Tinggi/berat = **Ratio** (0 = benar-benar tidak eksis, tidak bisa negatif).

### Sampling
| Metode | Cara Kerja |
|---|---|
| Simple Random | Semua anggota peluang sama |
| Systematic | Interval tetap dari titik acak awal |
| **Stratified** | Bagi grup HOMOGEN (strata), random dari SEMUA grup |
| **Cluster** | Bagi grup HETEROGEN (geografis), pilih BEBERAPA kluster acak, sensus penuh di situ |

> ⚠️ **Trap ketuker:** Stratified = semua grup dapat sampel. Cluster = cuma beberapa kluster dipilih, lalu disensus penuh.

**Sampling Bias contoh klasik:** proporsi sakit jantung usia MUDA (88.8%) > TUA (57.8%) — bukan fakta medis, tapi BIAS (anak muda ke RS cuma kalau parah, orang tua rutin check-up).

### Measures of Central Tendency
| Ukuran | Sensitif Outlier? |
|---|---|
| **Mean** | SANGAT sensitif |
| **Median** | TIDAK terpengaruh |
| **Mode** | Cocok data kategorikal |

> ⚠️ **Trap klasik (gaji):** 10 orang gaji 7-9jt + 1 orang gaji 100jt → Mean melonjak, Median tetap representatif. Beda jauh mean vs median = sinyal skewed data.

### Measures of Spread
| Ukuran | Formula |
|---|---|
| Range | Max − Min |
| **IQR** | `Q3 − Q1` (TANPA pengali apapun!) |

> ⚠️ **Trap PALING PENTING:** IQR = Q3-Q1 SAJA. Pengali `1.5×` BARU dipakai di batas outlier:
> - Lower Bound = `Q1 - 1.5×IQR`, Upper Bound = `Q3 + 1.5×IQR`.

### Normal Distribution & Empirical Rule
- Normal/Gaussian: simetris, bell-shaped. Kurva sempurna: **Mean = Median**.
- **Empirical Rule** (HANYA data simetris): 68% dalam `mean±1SD`, 95% dalam `mean±2SD`, 99.7% dalam `mean±3SD`.

**Uji Normalitas Grafis:** Histogram (cepat), Box Plot (bagus deteksi outlier, lemah deteksi kelancipan), **QQ Plot** (paling sensitif — garis lurus diagonal = normal).

> ⚠️ **Trap fraud detection:** Outlier TIDAK BOLEH selalu dihapus pakai 1.5×IQR — kalau outlier itu yang mau dideteksi (fraud, 0.5-1% data), menghapusnya = menghilangkan tujuan analisis.

### Graphical Summary
| Tipe Variabel | Chart |
|---|---|
| Numerical (1 var) | Histogram, Boxplot |
| Numerical (2 var) | Scatterplot |
| Categorical | Pie Chart, Bar Plot |

**Bentuk Histogram:** Symmetric/Normal, Right-skewed (ekor kanan, numpuk rendah), Left-skewed (ekor kiri, numpuk tinggi), Bimodal (2 puncak = 2 kelompok tercampur), Uniform (rata).

### Imbalanced Data
- Proporsi kelas timpang (99% normal vs 1% fraud). Model asal-nebak mayoritas → akurasi 99% tapi **0% berguna**.
- Solusi data: Down-sampling / Up-sampling. Solusi metrik: **Precision & Recall**, BUKAN accuracy.

> ⚠️ **Trap MCQ klasik:** "Akurasi tinggi = model bagus" itu JEBAKAN kalau data imbalanced.

---

## Sesi 12 — Python Data Manipulation With Pandas and Numpy

### NumPy vs Pandas
- **NumPy**: operasi matematika performa tinggi pada array (vectorization = operasi massal tanpa loop). **Pandas**: manipulasi data terstruktur, dibangun DI ATAS NumPy. Struktur: **Series** (1D), **DataFrame** (2D).
- Analogi: NumPy 1D array ≈ List (tapi homogen & lebih cepat). DataFrame ≈ "dict of columns", tiap kolom = Series.

> ⚠️ **Trap:** `math` bawaan Python BUKAN pengganti NumPy (tidak untuk array). Install Pandas → NumPy otomatis ikut. DataFrame = tabel (2D). Series = SATU kolom (1D) — jangan tertukar arah definisinya.

### Membuat Array
| Fungsi | Kegunaan |
|---|---|
| `np.array(list)` | Konversi list → array |
| `np.arange(start,stop,step)` | Isi **step** manual, jumlah elemen otomatis |
| `np.linspace(start,stop,count)` | Isi **jumlah elemen** manual, jarak otomatis (DETERMINISTIK, bukan random!) |
| `np.zeros()`/`np.ones()` | Array isi 0/1 semua |
| `np.random.randint(low,high,n)` | Angka acak integer |

> ⚠️ **Trap klasik MCQ:** `np.arange()` param=step; `np.linspace()` param=jumlah elemen. Jangan tertukar arahnya.

### Atribut & Slicing Array
- `.shape`, `.reshape(dims)`, `.reshape(-1)` (flatten otomatis), `.dtype`, `.argmax()`/`.argmin()` (INDEKS, bukan nilai!).

> ⚠️ **Trap SANGAT sering:** "A slice is a view, not a copy" — slice array HANYA referensi, BUKAN salinan. Ubah slice → array asli ikut berubah! Wajib `.copy()` eksplisit untuk salinan independen.

### Broadcasting
- Operasi `+-*/` = element-wise. Broadcasting = NumPy "regangkan" array kecil biar kompatibel dengan array besar (dicek dari sumbu paling KANAN).

> ⚠️ **Trap:** `np.exp(x)` = $e^x$ (e dipangkatkan x), BUKAN x dipangkatkan e.

### Pandas — `.loc` vs `.iloc`
| Cara | Berdasarkan | Slicing batas akhir |
|---|---|---|
| `.loc[label]` | LABEL nama | **INKLUSIF** |
| `.iloc[posisi]` | posisi INTEGER | **EKSKLUSIF** |

> ⚠️ **Trap soal favorit MCQ:** `.loc` inklusif di ujung, `.iloc` eksklusif — kebalikan dari intuisi banyak orang.

### Manipulasi DataFrame
| Method | Kegunaan |
|---|---|
| `.drop(label, axis=1)` | Hapus KOLOM (axis=1) |
| `.drop(label, axis=0)` | Hapus BARIS (axis=0) |
| `inplace=True` | Ubah DataFrame ASLI permanen |

> ⚠️ **Trap:** Default method (`.drop()`, `.reset_index()`) TIDAK ubah data asli — return SALINAN baru. Wajib `inplace=True` untuk permanen.

### Missing Values & Grouping
- `.isna()`, `.dropna()` (HAPUS baris kosong), `.fillna()` (ISI nilai kosong), `.groupby('kolom')`.

> ⚠️ **Trap:** `.dropna()` sering BUKAN pilihan terbaik (hilangkan info berharga) → `.fillna()` mean imputation lebih direkomendasikan. `.groupby().mean()` otomatis skip kolom non-numerik (bukan error).

### Menggabungkan DataFrame
| Fungsi | Kegunaan |
|---|---|
| `pd.merge()` | Gabung berdasar KOLOM kunci (mirip SQL JOIN) |
| `.join()` | Gabung berdasar INDEX baris |

### File I/O
| Baca | Simpan |
|---|---|
| `pd.read_csv/excel/json/html()` | `df.to_csv/excel/json()` — **TIDAK ADA `to_html()`** |

> ⚠️ **Trap:** Pandas bisa BACA html tapi TIDAK BISA export ke html — pembeda arah baca vs tulis.

---

## Sesi 13 — Data Visualization

*(Sudah solid dari quiz+retest — ringkasan final.)*

### Kenapa Penting & Alur Kerja
- Otak proses gambar lebih cepat dari tabel. Statistik deskriptif bisa SEMBUNYIKAN pola (Anscombe's Quartet: mean/SD/korelasi sama, bentuk visual beda total).
- 6 langkah: pahami konteks → rumuskan pertanyaan → pilih chart tepat → identifikasi pesan → konfigurasi teknis → tarik kesimpulan.

> ⚠️ **Trap:** GDP antar negara TIDAK BOLEH pakai Line Chart (menyiratkan kontinuitas waktu, padahal antar-negara tidak ada dimensi waktu).

### 4 Kategori Tujuan Visualisasi
| Kategori | Untuk Apa |
|---|---|
| **Comparison** | Bandingkan nilai |
| **Composition** | Bagian dari keseluruhan |
| **Relationship** | Korelasi antar variabel |
| **Distribution** | Sebaran 1 variabel |

> ⚠️ **Trap paling sering salah:** BUKAN "Comparison/Composition/Observation/Anomaly Detection" — 4 yang benar di atas.

**Composition seiring waktu:** periode SEDIKIT → Stacked Bar. Periode BANYAK → Stacked Area. *(Bedanya JUMLAH PERIODE, bukan ada/tiadanya time series.)*

### Chart-by-Chart Kunci
- **Histogram**: batang NEMPEL (numerik kontinu). vs **Bar Chart**: batang ADA JEDA (kategorikal diskrit).
- **Box Plot**: median deket **Q1** (bawah) → **Right-skewed** (mayoritas rendah, ekor ekstrem tinggi). Median deket **Q3** (atas) → **Left-skewed** (mayoritas tinggi, ekor ekstrem rendah).

> ⚠️ **Trap paling gampang kebalik:** arah skew ikut arah EKOR/EKSTREM MINORITAS, bukan kerumunan mayoritas. Q1 SELALU nilai lebih kecil (posisi bawah), Q3 SELALU lebih besar (posisi atas) — TETAP, tidak tergantung arah skew.

- **Scatter Plot**: `hue`=warna per kategori, `style`=bentuk marker per kategori lain (bisa 4 dimensi info: x,y,hue,style).
- **Pie Chart** dilarang kalau: (1) tren waktu, (2) kategori **>5**, (3) nilai BERDEKATAN.
- **Heatmap**: drop kolom ID (`PassengerId`) dulu sebelum correlation matrix — meski numerik, tidak bermakna kuantitatif.

### 4 Common Pitfalls
| Pitfall | Solusi |
|---|---|
| Information Overloading | Decluttering |
| **Inconsistent Scales** | **Secondary Y-axis** (BUKAN pisah 2 grafik) |
| Misleading Colors | Palet konsisten lintas grafik |
| Incomplete Category Pie | Wajib semua kategori (100%) |

> ⚠️ **Trap paling sering salah paham:** Inconsistent Scales BUKAN soal "tidak ada korelasi" — murni soal SKALA (variabel kecil keliatan flat karena ketindih variabel besar). Solusi: secondary axis, TETAP 1 grafik.

---

## Gap Analysis (kode praktik & CC1 — status 2026-08-30)

*(Detail lengkap & history koreksi ada di [PANDUAN_LANJUT_BELAJAR.md](PANDUAN_LANJUT_BELAJAR.md); ini cuma ringkasan gap.)*

### Kode Python — per modul
| Modul | Sesi terkait | Status |
|---|---|---|
| `collection-data-type/` | Sesi 4 | ✅ 12/12 file selesai |
| `conditional-and-loop-statements/` | Sesi 3 | ⬜ 0/11 file — belum disentuh |
| `python-function-and-file-handling/` | Sesi 5 | ⬜ 0/5 file |
| `object-oriented-programming/` | Sesi 7 | ⬜ 0/4 file |
| `python-modular-programming/` | Sesi 8 | ⬜ 0/9 bagian |
| `data-manipulation-pandas-numpy/` | Sesi 12 | ⬜ 0/11 file |
| `sql-exercise-materials-/9 - ...` | Sesi 9 | ⬜ 0/14 file demo+exercise |
| `sql-exercise-materials-/10 - ...` | Sesi 10 | ⬜ 0/6 file demo+exercise |

**Catatan penting:** Exam 1 sifatnya MCQ konsep — kode praktik ini "jalur paralel" (bukan syarat exam), tapi relevan buat CC1 LeetCode & pemahaman lebih dalam. Prioritas tetap breadth konsep dulu (cheat sheet ini) sebelum ngoprek semua file kode.

### Session 1 "Tugas Besar 2" — 5 soal, belum pernah dipraktikkan sebagai kode konkret
Rencana sesi berikutnya (lihat panduan): Konversi Suhu, Konversi Jarak (cm→km), Cek Ganjil/Genap, Manipulasi String (hapus first occurrence), Cek Palindrome.

### Code Challenge 1 (CC1) — LeetCode, deadline 2026-09-03, terpisah dari Exam 1
- **Status: 0/4 soal.** Ketentuan: 3 Easy (20 poin) + 1 Medium (40 poin), topik BEBAS (tidak wajib beda-beda).
- **3 Easy direkomendasikan** (reuse skill baru dikuasai): **Two Sum** (dict/complement — sudah mulai dicoba), **Remove Duplicates from Sorted Array** (1 loop + index assignment), **Contains Duplicate** (`set`, paling simpel).
- **Alternatif quick-win**: **Convert the Temperature** (1 baris rumus, hampir pasti Accepted) — isomorfik ke soal resmi Sesi 1 "Program Konversi Suhu".
- Submit: link profil LeetCode + screenshot "Accepted" per soal → https://forms.gle/4ncAW2VPUueAkiJp8

---

## Catatan Penting Lain (dari verifikasi silang agent, cek ke PDF resmi kalau ragu)

1. **Sesi 3**: dua versi algoritma cek bilangan prima muncul di sumber (loop `range(2,n)` vs optimized `range(2,int(n**0.5)+1)`) — cheat sheet ini pakai versi pertama sesuai konteks penjelasan trace di modul.
2. **Sesi 9-10**: istilah "correlated vs non-correlated subquery" TIDAK muncul eksplisit di materi — semua contoh subquery bersifat non-correlated. Kalau exam singgung istilah ini, itu di luar cakupan materi sesi ini.
3. **Sesi 9-10**: tabel "urutan eksekusi SQL" (FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY→LIMIT) adalah pengetahuan SQL standar yang konsisten dengan penjelasan WHERE vs HAVING di modul, tapi modul tidak menyebutnya eksplisit dengan istilah itu.
4. **Sesi 12**: catatan asli sumber menyebut `np.linspace()` hasilkan "angka acak" — ini kemungkinan salah tulis di transkrip asli, karena `linspace` sebenarnya DETERMINISTIK (jarak sama persis), bukan random. Cheat sheet ini sudah dikoreksi.
