---
tags: [exam-prep, cheatsheet, glossary, jcaieh/module1]
bootcamp: JCAIEH
module: 1
aliases: ["Kamus", "Cheat Sheet", "Glosarium"]
---

# 📚 Kamus & Cheat Sheet — Module 1 (13 Sesi)

> [!info] Tentang file ini
> Gabungan dua hal: (1) **Cheat Sheet** — ringkasan konsep + jebakan/trap per sesi (versi Obsidian dari `CHEATSHEET.md`), dan (2) **Kamus A-Z** — ~440 istilah dari seluruh 13 sesi, digabung dan dirapikan dari 4 file glosarium sementara. Dibuat 2026-08-30/2026-09-02. Lihat juga [[MOC - Module 1 (JCAIEH M1)|halaman indeks utama]] untuk catatan lengkap per sesi.

## 🗂️ Daftar Isi

- [[#🧠 Peta Pola Kesalahan Pribadi]]
- [[#⚡ Cheat Sheet per Sesi]]
	- [[#Sesi 1 — Intro to DS Python Statistics SQL Git & GitHub]]
	- [[#Sesi 2 — Intro to Git & GitHub]]
	- [[#Sesi 3 — Conditional & Loop Statement]]
	- [[#Sesi 4 — Data Types Collection]]
	- [[#Sesi 5 — Python Function & File Handling]]
	- [[#Sesi 6 — Hackerrank Exercise]]
	- [[#Sesi 7 — Object Oriented Programming]]
	- [[#Sesi 8 — Python & Modular Programming]]
	- [[#Sesi 9 — Intro to Database & SQL]]
	- [[#Sesi 10 — SQL Working With Multiple Tables]]
	- [[#Sesi 11 — Statistics Fundamental]]
	- [[#Sesi 12 — Python Data Manipulation With Pandas and NumPy]]
	- [[#Sesi 13 — Data Visualization]]
- [[#📖 Kamus Istilah A-Z]]
- [[#🔍 Gap Analysis & Catatan Penting]]

---

## 🧠 Peta Pola Kesalahan Pribadi

> Ditulis 2026-09-01 dari analisis semua sesi belajar — bukan teori umum, tapi pola nyata yang berulang. Baca bagian ini PALING TERAKHIR sebelum exam/quiz apa pun.

### Pola #1 — "Ambil 2 ujung doang, skip yang di tengah"

Muncul di slicing List (`[0:3]` dikira cuma ambil index 0 & 2) dan `.iloc` Pandas (`[0:4]` dikira `0,2,3`). Satu pola pikir yang sama: membayangkan "rentang A ke B" sebagai **2 titik**, padahal harusnya **jalur berkelanjutan**.

> [!tip] Analogi pengunci — Anak Tangga
> "Naik dari anak tangga 2 ke anak tangga 5" — WAJIB injak 3 dan 4 juga, tidak bisa loncat dari 2 langsung ke 5.
>
> **Aturan universal** (sama persis di List, Tuple, String, `range()`, `.iloc`): `[start:stop]` = SEMUA posisi dari `start` sampai TEPAT SEBELUM `stop`. Tidak ada yang boleh dilompatin (kecuali ada `step` > 1 eksplisit).

### Pola #2 — Konsep berpasangan yang MIRIP strukturnya → gampang KEBALIK arahnya

| Pasangan | Yang sering ketuker | Cara benarnya |
|---|---|---|
| `GROUP BY` vs `HAVING` | Dikira `HAVING` yang mengelompokkan | `GROUP BY` = **kelompokkan** dulu. `HAVING` = **saring** hasil kelompok (G duluan abjad = duluan eksekusi) |
| Self JOIN alias | Dikira alias OPSIONAL | Alias (`T1`/`T2`) **WAJIB MUTLAK** di Self JOIN — tanpa itu, SQL ERROR |
| `.max()` vs `.argmax()` | Dikira `argmax()` ngasih NILAI | `.max()` = **nilainya**. `.argmax()` = **posisi/index**-nya ("arg" = "at which position") |
| Arah skewness (Box Plot) | Dikira ikut arah MAYORITAS | Nama skew ikut arah **EKOR/MINORITAS EKSTREM**, bukan kerumunan mayoritas |
| IQR vs batas outlier | Dikira pengali `1.5×` masuk rumus IQR | `IQR` = `Q3-Q1` SAJA. `1.5×` dipakai di LANGKAH BERIKUTNYA (batas outlier) |
| Interval vs Ratio | Label ketuker (mana boleh negatif) | **Interval** = boleh negatif, 0 relatif (Suhu °C). **Ratio** = TIDAK boleh negatif, 0 mutlak (Tinggi badan) |
| Alias `as` — 2 alasan beda | Nyampur "hindari bentrok" vs "konvensi" | `model_modul` = hindari bentrok nama. `pd`/`np` = MURNI konvensi, tidak ada bentrok |

> [!warning] Strategi saat ujian
> Begitu ketemu soal yang "berasa familiar tapi ragu arahnya" — itu sinyal soal jenis Pola #2. STOP, jangan tebak reflex, ingat 1 contoh konkret dari tabel di atas dulu.

### Pola #3 — Jawab pakai istilah sistem yang SALAH (SQL vs Pandas ketuker)

Terjadi karena SQL dan Pandas sering diajarkan berdampingan (konsepnya mirip: `GROUP BY` ↔ `.groupby()`). **Kalau soal menyebut "Pandas"/"DataFrame", jawab pakai method (`.something()`), BUKAN keyword SQL** — dan sebaliknya.

---

## ⚡ Cheat Sheet per Sesi

### Sesi 1 — Intro to DS Python Statistics SQL Git & GitHub

> [[Sesi 01 - Introduction to DS Python Statistics SQL Git and GitHub (JCAIEH M1)|→ Catatan lengkap]]

**AI vs Software Tradisional**
- AI = cabang Computer Science: learning from data, recognizing patterns, understanding language, making predictions, solving problems.
- Software tradisional = rules ditulis manual programmer, kaku. AI = belajar pola dari data, adaptif.
- Andrew Ng: "AI is the new electricity". AI Model Lifecycle: **Problem Understanding → Data Preparation → Training → Evaluation → Deployment → Monitoring** (iteratif).
- NLP = bahasa. Computer Vision = visual. Compound/Agentic AI = gabungan NLP+CV+reasoning+tools.

**Algoritma & Flowchart**
- Algoritma: **Clear & Unambiguous, Step-by-step, Definite Start & End, Effective**.
- Shapes: Oval=Terminator, Rectangle=Process, Kertas robek=Document, Diamond=Decision, Jajar genjang=Data.

> [!warning] Trap — Flowchart bercabang ≠ eksekusi paralel
> Python (interpreted) tetap eksekusi baris-per-baris SERIAL dari atas ke bawah — percabangan cuma "pengalihan urutan", bukan eksekusi bersamaan.

**Tower of Hanoi**
- 3 komponen: Source, Target, Auxiliary. 3 aturan: 1 disk/pindah; hanya disk teratas boleh diambil; disk besar tidak boleh di atas disk kecil.
- Base case N=1. Recursive case (N>1): pindah N-1 Source→Helper, disk ke-N Source→Target, N-1 Helper→Target.
- Rumus langkah minimum: **2^N − 1**.

> [!warning] Trap — `N-1` di parameter rekursif
> Bukan sekadar pengurangan — strategi wajib mencapai base case. Tanpa ini, infinite recursion.

**Python Dasar — Environment**
- Python = **High-Level, Interpreted** (eksekusi line-by-line, debug mudah, runtime lebih lambat) vs C/C++ = Compiled.
- Venv (bawaan) vs Conda/Miniconda (lebih luas, sudah termasuk Python).

> [!warning] Trap — Anaconda sudah include venv
> Kalau sudah install Conda, TIDAK perlu venv terpisah.

**Variabel & Tipe Data**
- `=` assignment operator. Aturan nama: huruf/angka/underscore, tidak diawali angka, case-sensitive, `snake_case`.
- Tipe dasar: `int`, `float`, `bool`, `str`, `NoneType`.

> [!warning] Trap — `0` vs `None`
> `0` = integer, ADA nilainya. `None` = NoneType, benar-benar kosong. Analogi: 0 = laci berisi angka nol, None = laci benar-benar kosong.

- Falsy: `0`, `""`, `[]`, `()`, `{}`, `None`. Truthy: sisanya (termasuk `"False"` sbg teks!).
- `int(3.99)` = `3` (truncation, BUKAN dibulatkan).

**String Methods & f-String**

| Method | Fungsi |
|---|---|
| `.upper()` / `.lower()` | ubah besar/kecil huruf |
| `.strip()` | hapus spasi awal-akhir |
| `.replace(lama, baru)` | ganti substring |
| `.split()` / `.join()` | pecah jadi list / gabung list jadi string |
| `.find()` | cari index kemunculan |
| `.startswith()` / `.endswith()` | cek awalan/akhiran |
| `.count()` | hitung kemunculan |
| `.isalpha()` / `.isdigit()` / `.isalnum()` | cek huruf/angka/alfanumerik |

- f-String lebih ringkas dari concatenation manual (`+`, wajib `str()`). Bisa evaluasi ekspresi: `f"{age+1}"`.
- `input()` SELALU return **string** — wajib `int()`/`float()` untuk operasi matematika.

**Operator & Math Module**
- `+ - * /`, `%` (modulo), `**` (pangkat), `//` (floor division). Augmented: `n += 5`.
- `math.sqrt()`, `math.ceil()`, `math.floor()`, `math.factorial()`, `math.pi`, `math.e`, `math.inf`, `math.nan`.

```python
years = total_days // 365
remaining = total_days % 365
months = remaining // 30
days = remaining % 30
```

> [!warning] Trap — hasil geometri otomatis jadi float
> Circle area pakai `math.pi` → hasil OTOMATIS **float** meski radius integer bulat.

> [!warning] Trap — direktori terminal
> Kalau terminal beda folder dari file `.py`, `python file.py` GAGAL — wajib `cd` dulu.

---

### Sesi 2 — Intro to Git & GitHub

> [[Sesi 02 - Intro to Git and GitHub (JCAIEH M1)|→ Catatan lengkap]]

- Git = **Distributed VCS**, dibuat Linus Torvalds. GitHub = platform **hosting** (bukan VCS itu sendiri) + jejaring sosial developer.

| Aspek | Git | GitHub |
|---|---|---|
| Sifat | Software VCS lokal | Layanan hosting cloud |
| Instalasi | Lokal | Diakses via browser |
| Internet | Tidak wajib | Wajib untuk sync |

**Analogi Pohon**: Tree = proyek, Branch = jalur pengembangan, Leaves = commit.
- **Repository**: folder proyek yang dilacak Git. **Commit**: snapshot, diidentifikasi **SHA-1 hash** (40 karakter). **Branch**: jalur independen dari main. **Merge**: gabungkan branch — konflik → **conflict resolution** manual.

> [!warning] Trap — Git ≠ Google Docs
> Google Docs = live update real-time. Git = merge & conflict resolution MANUAL.

> [!tip] Lelucon "In Case of Fire"
> `git commit` (checkpoint lokal) → `git push` (upload cloud, aman walau laptop hancur) → `git out!` (baru evakuasi fisik). Urutan ini menekankan commit+push SEBELUM evakuasi.

**Status Berkas**

| Status | Arti |
|---|---|
| Untracked | File baru, belum direkam Git |
| Unmodified | Tracked, identik commit terakhir |
| Modified | Tracked, berubah, belum di-add |
| Staged | Sudah `git add`, siap commit |

- Alur: `git init` → `git config --global user.name/user.email` → `git status` → `git add` → `git commit -m "..."` → `git diff`.
- `git remote add origin <url>` → `git push -u origin main`.
- Branch: `git checkout -b <nama>`, `git checkout <nama>`, `git merge --no-ff <branch>`.
- `git log`: riwayat commit. **HEAD** = penanda posisi commit saat ini.

> [!warning] Trap — "no commits yet"
> Biasanya karena lupa `git add` dulu sebelum `git commit`.

> [!warning] Trap — virtual environment harus aktif
> Sebelum jalankan script/perintah Git, pastikan venv (misal `base` di Conda) aktif.

- Anatomi: `git` (program) + `init/status/commit/push` (sub-command) + `-b/-m/--no-ff` (flags) + `"pesan"` (argument).

---

### Sesi 3 — Conditional & Loop Statement

> [[Sesi 03 - Conditional and Loop Statement (JCAIEH M1)|→ Catatan lengkap]]

**Function, Parameter, Return (Review)**

| | `return` | `print()` |
|---|---|---|
| Fungsi utama | Kembalikan nilai ke pemanggil | Tampilkan teks ke layar |
| Nilai | Bisa ditampung ke variabel | Return `None` |
| Alur | Langsung hentikan fungsi | Tidak pengaruhi alur |

> [!warning] Trap — fungsi tanpa `return`
> `result = fungsi_tanpa_return(...)` → `result` = **None**, bukan error, tapi diam-diam salah.

- `"teks" + angka_float` → **TypeError** tanpa `str()`. f-String tidak butuh konversi manual.
- `.replace(search, "", 1)` → parameter ke-3 = batas maksimal penggantian; `1` = hanya first occurrence.

> [!warning] Trap — `.index()` pada nilai tidak ada
> Memicu **ValueError**, bukan return -1/None. Solusi: cek `in` dulu atau `try-except`.

- Boolean wajib kapital: `True`/`False` — huruf kecil = **NameError**.

> [!warning] Trap — Python strongly-typed
> `5 == "5"` → **False**. Python TIDAK PUNYA `===` — cukup `==`.

> [!warning] Trap — Short-circuit evaluation
> `and`: kalau kondisi pertama False, kondisi kedua TIDAK dievaluasi. `or`: kalau pertama True, langsung berhenti.

**Conditional (if/elif/else)**
- Indentation (bukan `{}`) untuk blok. `if-elif-else`: begitu satu True → eksekusi lalu langsung keluar (skip sisanya).

> [!warning] Trap — Dead Code
> `if x>=10: ... elif x>=15: ...` — kondisi `x>=15` TIDAK PERNAH tercapai (x>=10 duluan True). Solusi: urutkan kondisi paling SPESIFIK di atas.

- Nested if: Inner condition hanya dievaluasi kalau Outer True. Butuh double indentation.

> [!warning] Trap — urutan definisi fungsi
> Memanggil fungsi yang belum didefinisikan di atasnya → **NameError**.

**Looping (for vs while)**

| Fitur | for Loop | while Loop |
|---|---|---|
| Kapan pakai | Jumlah iterasi PASTI | Jumlah iterasi TIDAK pasti |
| Cara berhenti | Otomatis saat iterable habis | Saat kondisi False |

> [!warning] Trap — Looping ≠ Recursion
> Recursion = fungsi panggil dirinya sendiri, butuh stack memory baru tiap panggilan. Looping = linear, lebih hemat memori.

- `range(start, stop, step)`: **stop selalu eksklusif**. `range(10)` → 0-9.
- `enumerate(iterable, start=N)` → `(index, element)`. `start` HANYA ubah tampilan angka, TIDAK skip elemen.
- Dict iteration default = keys saja. `pass` = null statement (beda dari `continue`).

> [!warning] Trap — variabel loop tidak dihapus
> `for number in range(10)` → setelah loop, `number` tetap simpan nilai TERAKHIR (9), bisa diakses.

> [!warning] Trap — `else` pada loop
> Blok `else` pada for/while HANYA jalan kalau loop selesai NORMAL. Kalau dihentikan `break`, `else` **TIDAK PERNAH** dieksekusi.

> [!warning] Trap — update variabel sebelum `continue`
> Kalau update variabel kontrol diletakkan SETELAH `continue`, tidak akan pernah tereksekusi → infinite loop.

**Poin tambahan**: cek `number == 0` di paling atas sebelum modulo genap. Hindari `return print(...)`. Cegah ZeroDivisionError: cek `count == 0` dulu.

---

### Sesi 4 — Data Types Collection

> [[Sesi 04 - Data Types Collection Notes (JCAIEH M1)|→ Catatan lengkap]]

| Type | Class | Category | Mutable? |
|---|---|---|---|
| range | `range` | sequence | No |
| tuple | `tuple` | sequence | No |
| list | `list` | sequence | **Yes** |
| dict | `dict` | mapping | **Yes** |
| set | `set` | set | **Yes** |
| frozenset | `frozenset` | set | No |

> [!warning] Trap — mutable = unhashable
> Mutable (list/set/dict) TIDAK BISA jadi dict key/elemen set. Immutable (tuple/frozenset/string/angka) BISA. Set dalam set harus `frozenset()` dulu.

**List**: `[...]`, ordered, mutable. `.append()` (akhir), `.insert(index, item)`, `.extend(iterable)` (unpack). `.pop(index)`, `.remove(value)` (ValueError kalau tidak ada), `.clear()`.

> [!warning] Trap — `.append()` vs `.extend()`
> `.append(list_lain)` → masuk utuh sebagai SATU elemen nested. `.extend(list_lain)` → dibongkar & digabung sejajar.

> [!warning] Trap — `is` vs `==`
> `==` = kesamaan NILAI. `is` = kesamaan ALAMAT MEMORI. `list_a.copy()` → isi sama (`==` True) tapi `is` **False**.

**Tuple**: `(...)`, immutable, no `.append()`. `.index()` (ValueError kalau tidak ketemu), `.count()`.

> [!warning] Trap — Single-item tuple
> WAJIB koma: `(5,)` = tuple. `(5)` tanpa koma = integer biasa!

**Indexing vs Slicing**

| Operasi | Contoh out-of-range | Perilaku |
|---|---|---|
| Indexing | `students[10]` (list isi 4) | **CRASH** `IndexError` |
| Slicing | `students[10:]` | **AMAN**, return `[]` |

> [!warning] Trap PALING PENTING Sesi 4 — Indexing vs Slicing out-of-range
> Index tunggal di luar batas → error. Slice di luar batas → tetap jalan, hasil kosong.

**Set**: `{val1, val2}`, unordered, unindexed (`TypeError` kalau `my_set[0]`), auto-unique.

> [!warning] Trap — `{}` kosong = dictionary, BUKAN set
> Set kosong WAJIB `set()`.

- `.add()` (satu), `.update()` (banyak). `.remove()` → KeyError kalau tidak ada. `.discard()` → aman.
- Union `|`/`.union()`, Intersection `&`/`.intersection()`, Difference `-`/`.difference()`, Symmetric Difference `^`.
- Proper subset `<` (harus beda, tidak boleh identik) vs `<=` (boleh identik).

**Dictionary**: `{key: value}`, key harus unik & hashable.

> [!warning] Trap — duplicate key saat deklarasi
> TIDAK ADA ERROR — nilai TERAKHIR yang menang.

- `dict["key"]` → KeyError kalau tidak ada. `.get(key, default)` → aman.

> [!warning] Trap — `.update()` vs `.setdefault()`
> `.update()` = agresif, selalu timpa. `.setdefault()` = defensif, hanya nambah kalau key belum ada.

> [!warning] Trap — `sorted()` pada dict
> `sorted(my_dict)` HANYA return **KEYS SAJA** sebagai List baru — dict asli tidak berubah.

---

### Sesi 5 — Python Function & File Handling

> [[Sesi 05 - Python Function and File Handling (JCAIEH M1)|→ Catatan lengkap]]

- Function dibuat kalau logika dipakai berulang. Dua cara: `def` atau `lambda`.

> [!warning] Trap — nama fungsi tanpa kurung
> `print(greet)` → menampilkan `<function greet at 0x...>`, BUKAN menjalankan logikanya.

| Istilah | Definisi |
|---|---|
| Parameter | Placeholder di `()` saat definisi |
| Argument | Nilai nyata saat pemanggilan |

> [!warning] Trap — default value `None` falsy
> `if time:` dengan default `time=None` → `None` dievaluasi False, masuk `else`.

```python
lambda_fn = lambda num1, num2: num1 + num2
```

> [!warning] Trap — Type hint BUKAN validasi runtime
> Type hint cuma dokumentasi. Kalau mau validasi beneran, pakai `try`/`except`.

**Namespace & Scope**: Built-in → Global → Local.

> [!warning] Trap — nama sama, scope beda
> Global `message` dan local `message` = 2 variabel berbeda total, tidak error, tidak tumpang tindih.

> [!warning] Trap — UnboundLocalError
> `position = 0` (global). Di dalam fungsi `position += 1` **tanpa** `global position` → Python anggap local variable baru belum ada nilai → `UnboundLocalError`.

- `nonlocal`: khusus nested function, akses enclosing function (1 tingkat di atas), BUKAN global.

| Jenis | Definisi | Ciri Khas |
|---|---|---|
| Nested Function | Fungsi di dalam fungsi | Tidak bisa dipanggil dari luar |
| Callback Function | Dikirim sebagai argumen | Penerima kontrol eksekusi |
| Recursive Function | Panggil dirinya sendiri | Wajib Base Case + Recursive Case |

> [!warning] Trap — callback function tanpa kurung
> Melempar fungsi sebagai argumen callback: nama fungsi TANPA kurung. Kalau pakai kurung, Python eksekusi duluan dan kirim HASILNYA.

> [!warning] Trap bug klasik — `is_prime`
> Kalau `return True` di DALAM loop `for` (bukan setelah loop selesai) → salah deteksi prima di iterasi pertama.

**File Handling**: Open → Read/Write → Close.

| Mode | Nama | Perilaku |
|---|---|---|
| `"r"` | Read | File harus ada, kalau tidak → `FileNotFoundError` |
| `"w"` | Write | Isi lama DIHAPUS TOTAL |
| `"a"` | Append | Ditambah di akhir, data lama aman |

```python
with open("data.txt", "w") as file:
    file.write("Hello, Python!")
```

> [!warning] Trap — `with` menjamin file selalu ditutup
> Bahkan kalau ada exception di tengah jalan — mencegah memory leak/file corrupt.

---

### Sesi 6 — Hackerrank Exercise

> [[Sesi 06 - Hackerrank Exercise (JCAIEH M1)|→ Catatan lengkap]]

```python
# Runner-Up Score
arr = map(int, input().split())
unique_scores = sorted(set(arr))
print(unique_scores[-2])   # index -2 = terbesar kedua
```

```python
# Company Logo — top-3 huruf paling sering
result = sorted(letter_counter.items(), key=lambda x: (-x[1], x[0]))
# -x[1] → count descending; x[0] → huruf ascending sbg tie-breaker
```

> [!warning] Trap paling sering ditanya — `map()` itu lazy
> ```python
> hasil = map(str, [1,2,3])
> print(hasil)          # <map object at 0x...> — BUKAN ['1','2','3']!
> print(list(hasil))    # ['1','2','3'] — baru sekarang diproses
> ```

> [!warning] Trap — `set()` krusial untuk soal runner-up
> Kalau skor tertinggi duplikat, tanpa `set()` juara kedua asli bisa tidak ketemu.

> [!warning] Trap — constraints HackerRank
> Batasan soal adalah jaminan sistem — tidak perlu validasi manual (`if N < 2`) kecuali diminta eksplisit.

---

### Sesi 7 — Object Oriented Programming

> [[Sesi 07 - Object Oriented Programming (JCAIEH M1)|→ Catatan lengkap]]

| | Procedural | OOP |
|---|---|---|
| Fokus | Functions & logic | Objects & data |
| Data + Function | Terpisah | Digabung dalam 1 class |

> [!warning] Trap scope materi — HANYA sampai Basic Inheritance
> Fokus materi: Class, Object, Attributes, Methods, Basic Inheritance. Encapsulation/Abstraction/Polymorphism SENGAJA tidak didalami.

> [!warning] Trap — list/dict itu sendiri adalah Class
> `my_list = []` sama dengan memanggil constructor class `list`.

```python
class Car:
    def move_forward(self):
        self.position += 1
car_john = Car()
car_emily = Car()
```

> [!warning] Trap — `car_john is car_emily` → False
> Tiap object punya alamat memori terpisah & state independen.

```python
class Car:
    def __init__(self, type_name, color):
        self.type_name = type_name
        self.color = color
```

> [!warning] Trap — `__init__` jalan otomatis
> `Car("sedan", "red")` otomatis memicu `__init__` — tidak perlu dipanggil eksplisit.

- `self` = referensi ke current object, parameter pertama WAJIB. `car_john.move_forward(10)` ≡ `Car.move_forward(car_john, 10)`.

> [!warning] Trap — nama parameter ≠ nama attribute
> Nama parameter `__init__` TIDAK HARUS sama dengan nama attribute setelah `self.` — cuma konvensi.

```python
class MachineLearningModel:
    def __init__(self, task): self.task = task

class RegressionModel(MachineLearningModel):
    def __init__(self, train_data):
        super().__init__(task="regression")
        self.error_function = "r2"
```

> [!warning] Trap — inheritance tidak "bocor" ke sibling
> Object child punya akses penuh ke attribute/method parent + miliknya sendiri. Tapi method spesifik 1 child TIDAK ADA di child class lain (sibling).

| Kondisi | Nilai `__name__` | Blok `if` dieksekusi? |
|---|---|---|
| File dijalankan langsung | `"__main__"` | Ya |
| File diimpor sebagai module | Nama modul itu sendiri | Tidak |

---

### Sesi 8 — Python & Modular Programming

> [[Sesi 08 - Python and Modular Programming (JCAIEH M1)|→ Catatan lengkap]]

- Monolitik = 1 file. Modular = dipecah jadi modul kecil reusable. 5 masalah monolitik: sulit dibaca, maintain, debug, reuse, kolaborasi.

> [!warning] Trap evaluasi — modularisasi menambah kompleksitas
> Untuk script kecil sekali-pakai, jangan dipaksakan modular.

| Metode | Sintaks Import | Cara Panggil |
|---|---|---|
| Import seluruh modul | `import calculator` | `calculator.add(2,3)` (wajib prefix) |
| Import spesifik | `from calculator import add` | `add(2,3)` langsung |

> [!warning] Trap — `import calculator` tapi manggil tanpa prefix
> `add(2,3)` tanpa prefix → `NameError`.

| Istilah | Definisi | Representasi Fisik |
|---|---|---|
| Project | Aplikasi/library lengkap | Root folder |
| Package | Kumpulan modul terkait | Folder + wajib `__init__.py` |
| Module | 1 file kode reusable | File `.py` |

> [!warning] Trap — alias `as` untuk hindari bentrok nama
> Variabel lokal (`model = "..."`) nama SAMA dengan module diimpor (`import model`) → Python anggap `model` = string. Solusi: `import model as model_modul`.

> [!warning] Trap KUNCI — Name Guard hanya blokir eksekusi, bukan definisi
> `if __name__ == "__main__"` HANYA memblokir baris eksekusi langsung — TIDAK memblokir definisi function/class. Function tetap bisa diimpor file lain.

- Package = folder + wajib `__init__.py` (boleh kosong).

| | Deep Import | Shallow Import |
|---|---|---|
| Sintaks | `from package.module import function` | `from package import function` |
| Syarat | Jalan meski `__init__.py` kosong | Wajib expose function di `__init__.py` |

> [!warning] Trap — Circular Import
> file_A import file_B DAN file_B import file_A → error. Solusi: modul utilitas ketiga.

---

### Sesi 9 — Intro to Database & SQL

> [[Sesi 09 - Intro to Database and SQL (JCAIEH M1)|→ Catatan lengkap]]

- Database = organized collection of related data. DBMS = software perantara user↔database. Fungsi: correlate, query, report.
- Parameter koneksi wajib: DBMS type, Host (`localhost`), Port (`3306` MySQL), Username (`root`), Password.

> [!warning] Trap — DBeaver perlu Refresh (F5)
> Setelah bikin database baru. PowerShell: simbol `<` untuk import SQL di-reserve → ERROR, pakai CMD.

| Kategori | Perintah | Fungsi |
|---|---|---|
| **DDL** | `CREATE DATABASE/TABLE` | Buat struktur baru |
| DDL | `DROP` | Hapus permanen, tidak bisa undo |
| **DML** | `SELECT` | Ambil/tampilkan data |
| DML | `UPDATE` / `DELETE` | Ubah / hapus baris |

> [!warning] Trap BAHAYA FATAL
> `UPDATE`/`DELETE` **tanpa** `WHERE` = ubah/hapus SELURUH baris tabel!

- `LIKE`: `%` = 0/banyak karakter, `_` = tepat 1 karakter. `BETWEEN a AND b` = **inklusif**.

> [!warning] Trap — case sensitivity
> Keyword & nama kolom = case-insensitive. Nama database/tabel: case-sensitive di **Linux**, tidak di Windows/macOS.

> [!warning] Trap KLASIK — alias di `ORDER BY`
> DILARANG dibungkus kutip satu — kalau dikutip, dibaca sebagai string literal, bukan nama kolom.

| Jenis | Ciri | Contoh |
|---|---|---|
| **Aggregate** | Sekumpulan nilai → 1 hasil | `SUM, COUNT, AVG, MIN, MAX` |
| **Scalar** | Per-baris individual | `ROUND, LENGTH, UCASE, LCASE` |

> [!warning] Trap PALING SERING — agregat abaikan NULL
> Kecuali `COUNT(*)`. `LENGTH()` itu SCALAR — filter pakai `WHERE`, BUKAN `GROUP BY...HAVING`.

| | `WHERE` | `HAVING` |
|---|---|---|
| Kapan | Sebelum grouping | Setelah grouping |
| Fungsi agregat? | TIDAK BISA | BISA |

> [!warning] Trap — subquery untuk agregat di WHERE
> `WHERE Salary < AVG(Salary)` = ERROR. Solusi: `WHERE Salary < (SELECT AVG(Salary) FROM employees)`.

---

### Sesi 10 — SQL Working With Multiple Tables

> [[Sesi 10 - SQL Working With Multiple Tables (JCAIEH M1)|→ Catatan lengkap]]

| | Primary Key (PK) | Foreign Key (FK) |
|---|---|---|
| Keunikan | Wajib unik | Boleh duplikat |
| NULL | TIDAK BOLEH | Boleh |

- Composite PK: gabungan 2+ kolom. Relationship: One-to-One, One-to-Many, Many-to-Many (wajib bridge table).

| | Implicit | Explicit |
|---|---|---|
| Sintaks | Koma di `FROM`, key di `WHERE` | Keyword `JOIN...ON` |
| Rekomendasi | Sulit dibaca | **Direkomendasikan industri** |

> [!warning] Trap BAHAYA CARTESIAN PRODUCT
> Implicit JOIN tanpa kondisi key di `WHERE` → SETIAP baris tabel 1 dikawinkan SETIAP baris tabel 2 (599 × 16.044 = ~9,6 juta baris sampah).

| JOIN | Hasil |
|---|---|
| **INNER** (`JOIN` saja = default) | Hanya baris cocok di KEDUA tabel |
| **LEFT** | SEMUA baris kiri + cocok dari kanan (NULL kalau tidak cocok) |
| **RIGHT** | SEMUA baris kanan + cocok dari kiri |
| **FULL** | Gabungan LEFT+RIGHT |

> [!warning] Trap — RIGHT JOIN selalu bisa ditulis ulang jadi LEFT JOIN
> `A RIGHT JOIN B` = `B LEFT JOIN A` (hasil identik, tukar posisi tabel). Industri lebih suka LEFT JOIN.

```sql
SELECT K1.nama, K2.nama, K1.gaji
FROM karyawan K1
JOIN karyawan K2
  ON K1.karyawan_id <> K2.karyawan_id AND K1.gaji = K2.gaji;
```

> [!warning] Trap — Self JOIN wajib `<>` dan alias
> Kondisi `<>` MUTLAK perlu — tanpa itu, tiap baris berpasangan dengan dirinya sendiri. Alias (`K1`/`K2`) juga MUTLAK — tanpa alias, SQL ERROR ("Not unique table/alias").

| Urutan Penulisan | Urutan Eksekusi Logis |
|---|---|
| SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT | **FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT** |

> [!warning] Trap klasik — urutan eksekusi klausa
> `WHERE` dieksekusi SEBELUM grouping & SEBELUM `SELECT` menghitung nilai — makanya `WHERE` tidak bisa pakai agregat/alias hasil SELECT.

```python
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='pass', database='sakila')
```

> [!warning] Trap keamanan — jangan hardcode password
> Simpan di `.env` (masuk `.gitignore`), load pakai `python-dotenv`.

**Ringkasan trap SQL paling mungkin muncul**: alias jangan pakai kutip satu di `ORDER BY` · agregat tidak bisa langsung di `WHERE` · `LENGTH()` scalar, filter di `WHERE` · agregat abaikan NULL kecuali `COUNT(*)` · implicit JOIN tanpa `WHERE` = Cartesian Product · `RIGHT JOIN A,B` = `LEFT JOIN B,A` · `UPDATE`/`DELETE` tanpa `WHERE` = ubah/hapus semua baris · `BETWEEN` inklusif · nama tabel/db case-sensitive di Linux saja · derived table wajib alias di MySQL · PK unique+NOT NULL, FK boleh duplikat+NULL · Self JOIN wajib 2 alias + `<>`.

---

### Sesi 11 — Statistics Fundamental

> [[Sesi 11 - Statistics Fundamental (JCAIEH M1)|→ Catatan lengkap]]

- Statistics = "belajar dari data": collecting, analyzing, interpreting, drawing conclusion. 3 tahap: Design → Description → Inference.

> [!warning] Trap — Quick Count ≠ Real Count
> Quick count = SAMPEL, real count = POPULASI. Contoh Inferential Statistics.

| Cabang | Fokus |
|---|---|
| **Descriptive** | Merangkum data yang ADA |
| **Inferential** | Pakai SAMPEL simpulkan POPULASI |

```
Qualitative: Nominal (TANPA urutan) | Ordinal (ADA urutan)
Quantitative: Discrete (hasil MENGHITUNG) | Continuous (hasil MENGUKUR)
```

| Scale | Classify | Order | Distance | Zero | Kali/Bagi |
|---|:-:|:-:|:-:|:-:|:-:|
| Nominal | ✓ | ✗ | ✗ | ✗ | ✗ |
| Ordinal | ✓ | ✓ | ✗ | ✗ | ✗ |
| **Interval** | ✓ | ✓ | ✓ | Non-absolute | ✗ |
| **Ratio** | ✓ | ✓ | ✓ | Absolute | ✓ |

> [!warning] Trap paling sering ketuker — Interval vs Ratio
> Suhu Celsius = **Interval** (0°C masih ada suhunya, bisa negatif). Tinggi/berat = **Ratio** (0 = benar-benar tidak eksis).

| Metode | Cara Kerja |
|---|---|
| **Stratified** | Bagi grup HOMOGEN, random dari SEMUA grup |
| **Cluster** | Bagi grup HETEROGEN, pilih BEBERAPA kluster, sensus penuh |

> [!warning] Trap ketuker — Stratified vs Cluster
> Stratified = semua grup dapat sampel. Cluster = cuma beberapa kluster dipilih lalu disensus penuh.

| Ukuran | Sensitif Outlier? |
|---|---|
| **Mean** | SANGAT sensitif |
| **Median** | TIDAK terpengaruh |
| **Mode** | Cocok data kategorikal |

> [!warning] Trap klasik gaji
> 10 orang gaji 7-9jt + 1 orang gaji 100jt → Mean melonjak, Median tetap representatif.

> [!warning] Trap PALING PENTING — IQR
> `IQR = Q3 - Q1` SAJA. Pengali `1.5×` BARU dipakai di batas outlier: Lower = `Q1-1.5×IQR`, Upper = `Q3+1.5×IQR`.

- Empirical Rule (data simetris saja): 68% dalam `mean±1SD`, 95% dalam `±2SD`, 99.7% dalam `±3SD`. QQ Plot paling sensitif deteksi normalitas.

> [!warning] Trap fraud detection
> Outlier TIDAK BOLEH selalu dihapus pakai 1.5×IQR — kalau outlier itu yang mau dideteksi (fraud), menghapusnya = menghilangkan tujuan analisis.

> [!warning] Trap MCQ klasik — Imbalanced Data
> "Akurasi tinggi = model bagus" itu JEBAKAN kalau data imbalanced (99% vs 1%). Solusi metrik: Precision & Recall.

---

### Sesi 12 — Python Data Manipulation With Pandas and NumPy

> [[Sesi 12 - Python Data Manipulation With Pandas and Numpy (JCAIEH M1)|→ Catatan lengkap]]

- NumPy = operasi matematika performa tinggi pada array (vectorization). Pandas = manipulasi data terstruktur, dibangun di atas NumPy. Series (1D), DataFrame (2D).

> [!warning] Trap — arah definisi Series vs DataFrame
> DataFrame = tabel (2D). Series = SATU kolom (1D) — jangan tertukar.

| Fungsi | Kegunaan |
|---|---|
| `np.arange(start,stop,step)` | Isi **step** manual, jumlah elemen otomatis |
| `np.linspace(start,stop,count)` | Isi **jumlah elemen** manual, jarak otomatis (DETERMINISTIK) |

> [!warning] Trap klasik MCQ — arange vs linspace
> `np.arange()` param=step; `np.linspace()` param=jumlah elemen. Jangan tertukar arahnya.

- `.argmax()`/`.argmin()` = INDEKS, bukan nilai.

> [!warning] Trap SANGAT SERING — slice adalah view, bukan copy
> Slice array HANYA referensi. Ubah slice → array asli ikut berubah! Wajib `.copy()` eksplisit untuk salinan independen.

> [!warning] Trap — `np.exp(x)`
> = $e^x$ (e dipangkatkan x), BUKAN x dipangkatkan e.

| Cara | Berdasarkan | Slicing batas akhir |
|---|---|---|
| `.loc[label]` | LABEL nama | **INKLUSIF** |
| `.iloc[posisi]` | posisi INTEGER | **EKSKLUSIF** |

> [!warning] Trap soal favorit MCQ — `.loc` vs `.iloc`
> `.loc` inklusif di ujung, `.iloc` eksklusif — kebalikan intuisi banyak orang.

> [!warning] Trap — method default tidak ubah data asli
> `.drop()`, `.reset_index()` return SALINAN baru. Wajib `inplace=True` untuk permanen.

> [!warning] Trap — `.dropna()` vs `.fillna()`
> `.dropna()` sering BUKAN pilihan terbaik (hilangkan info) → `.fillna()` mean imputation lebih direkomendasikan. `.groupby().mean()` otomatis skip kolom non-numerik.

| Fungsi | Kegunaan |
|---|---|
| `pd.merge()` | Gabung berdasar KOLOM kunci (mirip SQL JOIN) |
| `.join()` | Gabung berdasar INDEX baris |

> [!warning] Trap — Pandas bisa baca html tapi TIDAK BISA export ke html
> Tidak ada `to_html()`.

---

### Sesi 13 — Data Visualization

> [[Sesi 13 - Data Visualization (JCAIEH M1)|→ Catatan lengkap]]

- Otak proses gambar lebih cepat dari tabel. Anscombe's Quartet: mean/SD/korelasi sama, bentuk visual beda total.

> [!warning] Trap — GDP antar negara jangan Line Chart
> Menyiratkan kontinuitas waktu, padahal antar-negara tidak ada dimensi waktu.

| Kategori | Untuk Apa |
|---|---|
| **Comparison** | Bandingkan nilai |
| **Composition** | Bagian dari keseluruhan |
| **Relationship** | Korelasi antar variabel |
| **Distribution** | Sebaran 1 variabel |

> [!warning] Trap paling sering salah — 4 kategori tujuan visualisasi
> BUKAN "Comparison/Composition/Observation/Anomaly Detection" — 4 yang benar di atas.

- Composition seiring waktu: periode SEDIKIT → Stacked Bar. Periode BANYAK → Stacked Area.
- Histogram: batang NEMPEL (numerik). Bar Chart: batang ADA JEDA (kategorikal).

> [!warning] Trap paling gampang kebalik — arah skew
> Median deket Q1 → Right-skewed (ekor kanan). Median deket Q3 → Left-skewed (ekor kiri). Arah skew ikut EKOR/EKSTREM MINORITAS, bukan mayoritas.

- Scatter Plot: `hue`=warna per kategori, `style`=bentuk marker. Pie Chart dilarang kalau: tren waktu, kategori >5, nilai berdekatan. Heatmap: drop kolom ID dulu sebelum correlation matrix.

| Pitfall | Solusi |
|---|---|
| Information Overloading | Decluttering |
| **Inconsistent Scales** | **Secondary Y-axis** (BUKAN pisah 2 grafik) |
| Misleading Colors | Palet konsisten |
| Incomplete Category Pie | Wajib semua kategori (100%) |

> [!warning] Trap paling sering salah paham — Inconsistent Scales
> BUKAN soal "tidak ada korelasi" — murni soal SKALA. Solusi: secondary axis, TETAP 1 grafik.

---

## 📖 Kamus Istilah A-Z

> Gabungan ~440 istilah dari seluruh 13 sesi. Istilah yang sama persis di beberapa sesi digabung jadi satu entri; istilah yang **terlihat mirip tapi beda makna antar-sistem** (mis. Python vs SQL vs Statistics) sengaja dipisah dan diberi label — ini area rawan **Pola #3** (cross-system leakage), jadi perhatikan labelnya.

### A
- **`.add()`** — menambahkan satu elemen tunggal ke Set — `my_set.add("x")`
- **A/B Testing** — pengujian dua desain/versi berbeda untuk melihat efektivitas perubahan terhadap suatu metrik
- **Abstraction** — pilar OOP lanjutan yang menyembunyikan detail implementasi rumit; jarang dipakai intensif di AI Engineering (di luar cakupan Sesi 7)
- **Accuracy (Akurasi)** — proporsi prediksi benar dari total prediksi; MENYESATKAN pada data imbalanced
- **Aggregate Function** — beroperasi pada sekumpulan nilai, hasil 1 nilai tunggal — `SUM()`, `COUNT()`, `AVG()`, `MIN()`, `MAX()`
- **Alias (SQL Table)** — nama panggilan sementara untuk tabel/kolom — `FROM customer C, payment P`
- **Alias (Python Import)** — mempersingkat/menghindari konflik nama modul dengan `as` — `import pandas as pd`, `import model as model_modul` (lihat Pola #2 — dua alasan `as` yang beda)
- **`abs()`** — nilai mutlak — `abs(-7)` → `7`
- **`.append()`** — tambah satu elemen di akhir List — `lst.append(4)`
- **`.apply()`** — terapkan fungsi custom/Lambda ke tiap elemen kolom Pandas — `df['col'].apply(lambda x: x**2)`
- **`.argmax()` / `.argmin()`** — POSISI/indeks nilai terbesar/terkecil (bukan nilainya!) — beda dari `.max()`/`.min()` yang return nilai
- **Argument** — nilai nyata yang dikirim ke fungsi saat dipanggil — `greet("Sari")` → `"Sari"`
- **Artificial Intelligence (AI)** — bidang Computer Science yang membuat sistem mampu melakukan tugas yang biasanya butuh kecerdasan manusia
- **ASC / DESC** — arah `ORDER BY`; `ASC` = kecil→besar (default), `DESC` = besar→kecil
- **Assignment Operator (`=`)** — mengaitkan nilai di kanan ke nama variabel di kiri — `age = 20`
- **Attribute** — variabel yang menempel pada class/object (`self.`) menyimpan state — `self.balance = 0`
- **Augmented Assignment Operator** — menyingkat operasi+penugasan ulang — `n += 5` ≡ `n = n + 5`

### B
- **Bar Chart / Bar Plot** — batang berjeda untuk kategori diskrit — `plt.bar(df['Category'], df['Revenue'])`
- **Base Case** — kondisi paling sederhana rekursi yang menghentikan pemanggilan berulang — `if num <= 1: return 1`
- **Bell-Shaped Curve** — bentuk kurva distribusi normal, simetris terpusat di mean
- **BETWEEN** — filter rentang, **inklusif** (batas awal & akhir ikut) — `WHERE Population BETWEEN 1000000 AND 2000000`
- **Bimodal Distribution** — dua puncak (mode), menandakan dua kelompok tercampur
- **Blinding** — penyamaran informasi perlakuan dari subjek/peneliti untuk hindari bias
- **Bool / Boolean** — dua nilai kebenaran, `True`/`False`; wajib huruf kapital
- **Box Plot (Box-and-Whisker Plot)** — ringkasan lima angka + deteksi outlier/skewness
- **Branch (Git)** — jalur pengembangan independen dari `main` — `git checkout -b fitur-baru`
- **`break`** — hentikan perulangan seketika
- **Bridge Table / Junction Table** — tabel perantara memecah relasi Many-to-Many jadi 2 One-to-Many
- **Broadcasting** — NumPy meregangkan array kecil agar kompatibel dengan array besar; dicek dari sumbu paling KANAN
- **Bubble Plot** — Scatter Plot untuk 3 variabel numerik, variabel ketiga = ukuran bubble
- **Business Intelligence (BI) Tools** — dashboard interaktif skala perusahaan (Power BI, Tableau, Qlik)
- **Built-in Function** — bawaan Python tanpa import — `print()`, `len()`, `input()`, `range()`
- **Built-in Namespace** — namespace tertinggi berisi nama bawaan Python

### C
- **Call Stack** — struktur memori menyimpan "bingkai" tiap pemanggilan fungsi rekursif; bisa penuh → stack overflow
- **Callback Function** — fungsi dilewatkan sebagai argumen ke fungsi lain — `kalkulator(tambah, 1, 3)` (tanpa kurung!)
- **Cartesian Product** — hasil join tanpa filter, tiap baris A dipasangkan tiap baris B (baris_A × baris_B)
- **Case Sensitivity / Collation** — keyword SQL case-insensitive; nama tabel/db case-sensitive di Linux saja
- **Central Tendency (Measures of)** — cara deskripsikan titik tengah: Mean, Median, Mode
- **Child Class (Derived Class)** — class baru mewarisi dari parent — `class RegressionModel(MachineLearningModel):`
- **Circular Import** — dua file saling mengimpor; solusi: pindahkan ke modul netral ketiga
- **Class** — blueprint yang menetapkan attribute & method suatu tipe object
- **Clean Function** — nama deskriptif, parameter bermakna, type hint, docstring
- **.clear()** — kosongkan List/Set/Dict tanpa hapus objeknya
- **Cluster Sample** — populasi dibagi kelompok HETEROGEN (geografis), beberapa klaster dipilih acak, sensus penuh di situ
- **Collection Data Types** — kategori tipe data menampung banyak elemen: List, Tuple, Set, Dict, Range
- **Column Expression** — kolom hasil substitusi dari subquery di daftar SELECT
- **Commit (Git)** — snapshot proyek di satu titik waktu, diidentifikasi SHA-1 hash
- **.concat() (pd.concat)** — menyatukan DataFrame vertikal (axis=0)/horizontal (axis=1)
- **Comparison Operators** — `==`, `!=`, `>`, `<`, `>=`, `<=`, selalu hasil Boolean
- **Compiled Language** — diterjemahkan sekaligus oleh compiler sebelum eksekusi (C/C++)
- **Compiler** — menerjemahkan seluruh kode ke kode mesin sekaligus sebelum eksekusi
- **Composite Primary Key** — PK dari kombinasi 2+ kolom — `PRIMARY KEY (employee_number, from_date)`
- **Conda / Virtual Environment (Venv)** — pengelola lingkungan Python; Venv bawaan (modul standar), Conda/Miniconda lebih luas (sudah termasuk Python sendiri) — kalau sudah install Conda, tidak perlu venv terpisah
- **Constraints (HackerRank)** — batasan resmi soal yang dijamin sistem, tidak perlu divalidasi manual
- **Constructor (`__init__`)** — special method yang otomatis jalan saat object dibuat
- **Continuous Variable** — numerik hasil PENGUKURAN, bisa desimal — tinggi badan
- **Control Group** — kelompok pembanding menerima perlakuan standar/plasebo
- **.copy() (Python collections)** — salinan independen List/Set/Dict di alamat memori berbeda (shallow copy) — `list_b = list_a.copy()`
- **.copy() (NumPy array)** — salinan independen dari array/slice agar perubahan tidak memengaruhi data asli — `arr[0:6].copy()` (lihat trap "slice = view, bukan copy" di Sesi 12)
- **Correlation Heatmap** — Heatmap matriks korelasi antar variabel numerik dengan gradasi warna
- **.count()** — hitung kemunculan nilai di string/tuple/list — `"banana".count("a")` → `3`
- **Covariates (Variabel Pengganggu)** — faktor luar diseimbangkan lewat randomisasi
- **CREATE DATABASE / CREATE TABLE** — perintah DDL membuat database/tabel baru
- **CREATE TABLE ... AS SELECT** — buat tabel baru sekaligus isi dari hasil query tabel lain
- **Cursor (Database)** — objek perantara Python MySQL Connector — `mycursor = mydb.cursor()`

### D
- **D'Agostino and Pearson's Test** — uji normalitas omnibus (skewness + kurtosis)
- **Data (Unit Informasi)** — BARIS = unit observasi, KOLOM = variabel
- **Data Type (SQL)** — jenis nilai kolom, contoh `int`, `varchar(255)`
- **Data Visualization** — penyajian data dalam gambar/grafis agar pola lebih mudah terbaca
- **Data Wrangling** — pembersihan, penataan, transformasi data mentah
- **Database** — koleksi data terorganisasi yang disimpan dan diakses secara elektronik
- **DataFrame** — struktur data Pandas 2 dimensi (tabel), kumpulan Series berbagi index — `pd.DataFrame({'A':[1,2]})`
- **DBMS (Database Management System)** — perangkat lunak perantara user↔database, contoh MySQL, PostgreSQL
- **Dead Code** — blok kode tidak akan pernah tereksekusi karena urutan `if-elif` salah
- **Decision (flowchart)** — simbol belah ketupat, titik percabangan logika
- **Deep Import** — impor merujuk nama modul + jalur lengkap — `from package.module import function`
- **Default Value (parameter)** — nilai bawaan dipakai kalau argumen tidak dikirim — `def greet(name="Bob"):`
- **DELETE** — DML hapus baris — `DELETE FROM person WHERE PersonID = 4;`
- **Dependent Table** — tabel menyimpan FK, bergantung pada tabel induk
- **Derived Table** — tabel virtual sementara dari subquery di `FROM`, wajib alias di MySQL
- **DESCRIBE** — tampilkan struktur kolom tabel
- **Descriptive Statistics** — merangkum data yang ADA, tanpa prediksi
- **Dict / Dictionary** — pasangan key-value, mutable — `{"nama": "andi"}`
- **Dictionary Counter** — pola pakai dict untuk hitung frekuensi — `letter_counter[letter] = letter_counter.get(letter, 0) + 1`
- **Discrete Variable** — numerik hasil MENGHITUNG, hanya bilangan bulat
- **.discard()** — hapus dari Set berdasarkan nilai, aman (tidak error kalau tidak ada) — beda `.remove()`
- **Distributed Version Control System (Git)** — tiap developer punya salinan lengkap riwayat proyek
- **DISTINCT** — hilangkan nilai duplikat dari SELECT
- **DML (Data Manipulation Language)** — `INSERT`, `SELECT`, `UPDATE`, `DELETE`
- **Docstring** — dokumentasi `"""..."""` di dalam fungsi
- **Document (flowchart)** — simbol kertas robek, output dokumen/laporan
- **Double Indentation** — indentasi ganda untuk blok nested if tingkat kedua
- **Down-sampling** — kurangi sampel kelas mayoritas agar seimbang dengan minoritas
- **DROP DATABASE** — hapus database + seluruh isinya permanen
- **.dropna()** — buang seluruh baris/kolom dengan NaN
- **.dtype** — tipe data elemen array/kolom, contoh `int64`

### E
- **elif** — "else if", uji kondisi tambahan jika sebelumnya False
- **else (dalam loop)** — hanya jalan jika loop berakhir NORMAL (bukan karena `break`)
- **Empirical Rule** — 68%-95%-99.7% observasi dalam ±1SD/±2SD/±3SD; HANYA data simetris
- **Encapsulation** — pilar OOP lanjutan menyembunyikan detail internal object (di luar cakupan Sesi 7)
- **Enclosing Function** — fungsi luar pembungkus nested function; diakses `nonlocal`
- **`enumerate()`** — iterasi + lacak indeks, hasil `(index, element)` — `for i, x in enumerate(lst):`
- **`.endswith()`** — cek akhiran string — `"file.py".endswith(".py")` → `True`
- **.env File (Dotenv)** — simpan kredensial rahasia, dibaca `python-dotenv`
- **Escape Character** — karakter berawalan `\`, contoh `\n` = baris baru
- **Experimental Study** — intervensi aktif peneliti (Treatment) untuk uji sebab-akibat
- **Explicit JOIN** — `JOIN...ON` eksplisit — `FROM film F JOIN language L ON F.language_id = L.language_id`
- **Explode Parameter (Pie Chart)** — memisahkan satu irisan Pie Chart — `plt.pie(data, explode=(0,0.1,0,0))`
- **.eye() (np.eye)** — matriks identitas — `np.eye(4)`

### F
- **f-string** — sisip variabel ke string, `f"umur saya {age}"`, bisa evaluasi ekspresi langsung
- **Falsy** — `0`, `""`, `[]`, `()`, `{}`, `None`
- **Fancy Indexing** — akses beberapa elemen non-berurutan sekaligus — `matrix[[0, 2]]`
- **FileNotFoundError** — buka file mode `"r"` tapi belum ada
- **File Object (File Handler)** — objek penunjuk hasil `open()` — `file = open("data.txt", "r")`
- **File I/O (Pandas)** — `pd.read_csv/excel/json/html()` baca; `df.to_csv/excel/json()` simpan — TIDAK ADA `to_html()`
- **.fillna()** — ganti NaN dengan nilai tertentu — `df['Age'].fillna(df['Age'].mean())`
- **`.find()`** — posisi indeks awal substring — `"hello".find("ll")` → `2`
- **Five-Number Summary** — Min, Q1, Median, Q3, Max
- **Float** — angka desimal — `3.14`
- **Floor Division (`//`)** — pembagian bulat, hilangkan sisa desimal — `7 // 2` → `3`
- **`for` loop** — mengiterasi tiap elemen iterable
- **`.format()`** — metode lama sisip variabel ke string — `"Nama {}".format("Andi")`
- **Foreign Key (FK)** — kolom merujuk PK tabel lain, boleh duplikat/NULL
- **FROM Clause** — menentukan tabel sumber data query
- **frozenset** — Set immutable; dipakai saat Set butuh menampung Set lain (hashable requirement)
- **FULL (OUTER) JOIN** — semua baris kedua tabel; tidak native di MySQL, disimulasikan `UNION` LEFT+RIGHT
- **Function** — blok kode reusable, terima input, proses, kembalikan nilai, `def`

### G
- **Gaussian Distribution** — nama lain Normal Distribution
- **Git** — Distributed VCS, diciptakan Linus Torvalds
- **`git add` / `git commit` / `git push` / `git pull` / `git status` / `git log` / `git diff` / `git init` / `git config` / `git checkout` / `git clone` / `git merge` / `git remote add origin`** — lihat tabel perintah di [[#Sesi 2 — Intro to Git & GitHub]]
- **GitHub** — platform hosting berbasis web untuk repo Git + jejaring sosial developer
- **Global Namespace** — nama level modul/file utama
- **Global Variable** — dibuat di luar fungsi, diakses dari mana pun di file sama
- **`global` keyword** — beri tahu Python mengubah variabel global dari dalam fungsi
- **GROUP BY** — kelompokkan baris bernilai sama, biasa dengan fungsi agregat
- **.groupby()** — kelompokkan baris DataFrame berdasar kolom, wajib diikuti agregasi; setara `GROUP BY` SQL — `df.groupby('Company')['Sales'].mean()`

### H
- **HackerRank** — platform evaluasi kode daring untuk latihan logika + seleksi kandidat
- **Hardcoding** — nilai/nama file statis langsung di kode, bukan parameter
- **Hashable** — bisa jadi key dict/elemen Set; biasanya berarti immutable
- **HAVING** — saring hasil SETELAH `GROUP BY`, bisa pakai fungsi agregat
- **HEAD (Git)** — penanda posisi commit aktif — `HEAD -> main`
- **Heatmap** — visualisasi matriks 2D pakai kode warna, umum untuk korelasi
- **High-Level Language** — sintaksis dekat bahasa manusia (Python)
- **Histogram** — distribusi frekuensi numerik tunggal, dibagi bins — batang NEMPEL (beda Bar Chart)
- **Host** — alamat jaringan server DBMS, contoh `localhost`
- **Hypothetical Population** — populasi abstrak dari fenomena berkelanjutan

### I
- **`id()`** — alamat memori unik objek — `id(list_a) == id(list_b)`
- **`if` / `if-elif-else` / `if-else`** — struktur kontrol kondisional
- **Imbalanced Data** — proporsi kelas timpang; akurasi jadi menyesatkan
- **Immutable** — tidak bisa diubah setelah dibuat: `tuple`, `range`, `frozenset`, `str`
- **Implicit JOIN** — koma di `FROM`, kondisi di `WHERE` — bahaya Cartesian Product
- **IndentationError** — blok di bawah `if`/`for`/`while` tidak diindentasi benar
- **Indentation** — spasi/tab penentu blok kode Python
- **IndexError** — akses indeks melebihi kapasitas List/Tuple — `lst[10]` list 4 elemen
- **Indexing** — akses satu elemen berdasar posisi — `lst[0]`
- **Inferential Statistics** — pakai sampel simpulkan populasi
- **Infinite Loop** — kondisi selalu True, variabel kontrol tidak pernah diperbarui
- **Inheritance** — child mewarisi attribute/method parent, hubungan "is-a"
- **INNER JOIN** — hanya baris cocok di kedua tabel
- **Inner Condition** — kondisi bersarang dalam Outer Condition (Nested if)
- **`input()`** — ambil input pengguna, hasil SELALU string
- **INSERT INTO** — tambah baris baru
- **Inplace Parameter (`inplace=True`)** — method Pandas ubah DataFrame asli permanen
- **Instance** — object hasil instansiasi class, state sendiri di memori
- **Instantiation** — proses membuat object baru dari class
- **Int / Integer** — bilangan bulat — `10`, `-5`
- **Interquartile Range (IQR)** — `Q3 - Q1` SAJA, TIDAK melibatkan 1.5 (lihat Pola #2)
- **Intersection (Set)** — irisan dua himpunan — `A & B`
- **Interpreted Language** — eksekusi baris-demi-baris saat runtime (Python)
- **Interpreter** — eksekusi kode langsung tanpa kompilasi awal
- **Interval Scale** — jarak konsisten, TANPA nol absolut — Suhu Celsius
- **`is` (operator identitas)** — bandingkan alamat memori (beda `==` yang bandingkan nilai)
- **is-a relationship** — hubungan konseptual inheritance
- **`.isalnum()` / `.isalpha()` / `.isdigit()`** — cek isi string huruf/angka/alfanumerik
- **.isna()** — deteksi NaN, hasil tabel boolean
- **`.insert()`** — sisip elemen di posisi tertentu List
- **Issue Tracking** — fitur GitHub catat bug/tugas/fitur
- **Iterable** — objek elemen bisa diakses satu per satu (String, List, Tuple, Dict, Set, Range)
- **`.items()`** — pasangan key-value dict sebagai tuple
- **`.join()` (String)** — gabung elemen list jadi string dengan pemisah — `"-".join(["a","b"])` → `"a-b"`
- **`.join()` (DataFrame)** — gabung dua DataFrame berdasar INDEX (beda `pd.merge()` yang berdasar kolom) — `df1.join(df2, how='left')`

### K
- **KDE (Kernel Density Estimation)** — kurva mulus perkiraan kepadatan sebaran, di atas Histogram
- **Key Join (Matching Keys)** — kolom pencocokan baris saat JOIN, biasanya PK-FK
- **KeyError** — akses key tidak ada di dict via `[]`, atau `.remove()` Set dengan nilai tidak ada
- **`.keys()`** — seluruh key dictionary
- **Key (Dictionary)** — pengindeks unik pasangan key-value, harus hashable
- **Kolmogorov-Smirnov Test (KS Test)** — uji normalitas berbasis jarak supremum, kekuatan rendah

### L
- **Lambda (Anonymous Function)** — fungsi tanpa nama, logika 1 baris — `lambda x, y: x + y`
- **Lazy Operation** — tidak langsung dieksekusi sampai hasil dibutuhkan, contoh `map()`
- **Left-Skewed Distribution (Skewness Negatif)** — ekor ke KIRI, mayoritas data di nilai tinggi; median dekat Q3
- **LEFT (OUTER) JOIN** — semua baris kiri + cocok dari kanan
- **`len()`** — jumlah elemen koleksi
- **LENGTH()** — panjang karakter string (SQL, scalar) — beda dari `len()` Python
- **LIKE Operator** — pencocokan pola teks, wildcard `%`/`_`
- **Lilliefors Test** — perbaikan KS Test, masih kalah kuat dari Shapiro-Wilk
- **LIMIT** — batasi jumlah baris maksimum
- **Line Plot** — grafik garis untuk tren data kontinu (time series)
- **.linspace() (np.linspace)** — JUMLAH elemen manual, jarak otomatis (DETERMINISTIK) — beda `np.arange()`
- **List** — koleksi terurut, mutable — `["a","b","c"]`
- **List Comprehension** — sintaksis ringkas bikin list baru — `[x.upper() for x in fruits if "a" in x]`
- **List of Dictionary** — list berisi beberapa dict — `[{"nama":"Apel","harga":5000}]`
- **Local Namespace / Local Variable** — nama/variabel di dalam tubuh fungsi, hilang setelah fungsi selesai
- **.loc[] / .iloc[]** — `.loc` berbasis LABEL (inklusif); `.iloc` berbasis POSISI (eksklusif)
- **Logical Operators** — `and`, `or`, `not`
- **Loop / Looping (Iteration)** — eksekusi berulang hingga kondisi berhenti
- **Low-Level Language** — mendekati bahasa mesin

### M
- **Many-to-Many Relationship** — banyak baris A ↔ banyak baris B, wajib bridge table
- **map()** — terapkan fungsi ke tiap item iterable, **lazy** — `map(int, input().split())`
- **Mappings** — kategori koleksi key-value, contoh `dict`
- **Masking (Boolean Filtering)** — saring elemen array pakai boolean array — `arr[arr > 10]`
- **math module** — fungsi matematika bawaan: `math.sqrt()`, `math.ceil()`, `math.floor()`, `math.factorial()`, `math.pi`, `math.e`, `math.inf`, `math.nan`
- **Mean (Rata-rata)** — jumlah nilai ÷ jumlah observasi; SANGAT sensitif outlier
- **Median (Nilai Tengah)** — nilai tengah data terurut; tahan outlier
- **Memory Address** — lokasi unik di memori tempat object disimpan
- **Merge (Git)** — gabungkan perubahan branch ke branch tempat kita berada
- **Merge Conflict** — Git gagal gabung otomatis, butuh resolusi manual (baris sama diubah 2 jalur)
- **.merge() (pd.merge)** — gabung DataFrame berdasar kolom kunci, setara JOIN SQL — `pd.merge(df1, df2, on='key', how='inner')`
- **Method** — function di dalam class menggambarkan behavior object
- **Missing Values (NaN)** — representasi data kosong Pandas
- **Modular Programming** — pecah program besar jadi modul kecil reusable
- **Mode (Modus)** — nilai frekuensi paling sering; cocok data kategorikal
- **Module** — 1 file `.py` reusable
- **Modulo (`%`)** — sisa hasil bagi — `7 % 2` → `1`
- **Monolithic Code** — seluruh logika dalam satu file tunggal
- **Multi-Index** — indeks bertingkat DataFrame
- **Mutable** — bisa diubah setelah dibuat: `list`, `dict`, `set`
- **MySQL Connector (Python)** — `mysql-connector-python`, hubungkan Python↔MySQL

### N
- **NameError** — panggil variabel/fungsi belum pernah didefinisikan
- **Name Guard (`__name__ == "__main__"`)** — cegah kode eksekusi otomatis saat file diimpor sebagai modul (TIDAK memblokir definisi function/class)
- **Namespace** — area berlabel melacak nama & objek yang dirujuknya
- **Namespace Conflict** — nama variabel lokal sama dengan modul diimpor, diatasi alias `as`
- **Negative Indexing** — dari belakang, mulai `-1`
- **Nested Dictionary** — dict yang salah satu value-nya dict lain
- **Nested Function** — fungsi di dalam fungsi lain, hanya diakses dari dalam pembungkusnya
- **Nested if** — `if` di dalam `if` lain, untuk keputusan dependen
- **Nested List** — list di dalam list — `[['Harry', 37.21]]`
- **`nonlocal` keyword** — ubah variabel enclosing function dari nested function
- **Nominal Scale** — kategorikal tanpa urutan — warna, jenis kelamin
- **None / NoneType** — ketiadaan nilai sama sekali (beda dari `0`)
- **Normal Distribution** — kontinu, lonceng, simetris, mean=median=mode
- **Normality Assessment** — uji apakah data ikut Distribusi Normal (grafis atau formal)
- **`not`** — balik nilai Boolean
- **NumPy Array** — struktur homogen, mutable, zero-indexed, vectorized

### O
- **Object** — instansiasi spesifik dari class, state sendiri
- **Observational Study** — peneliti pasif hanya mengamati (contoh: survei Quick Count)
- **ON Clause** — kondisi pencocokan kolom pada Explicit JOIN
- **One-to-Many / One-to-One Relationship** — jenis relasi antar tabel
- **OOP (Object-Oriented Programming)** — organisasi kode di sekitar object (data) & behavior (method)
- **Open Mode (`"r"`/`"w"`/`"a"`)** — read / write (menimpa) / append
- **Ordinal Scale** — kategorikal DENGAN urutan — tingkat kepuasan
- **Outer Condition** — kondisi tingkat pertama Nested if
- **Outer Query** — kueri utama level luar yang memakai hasil subquery
- **Out-of-range (Slicing)** — melewati batas elemen; TIDAK error, hasil kosong (beda IndexError)
- **Outlier (Pencilan)** — di luar batas `Q1-1.5×IQR` dan `Q3+1.5×IQR`; jangan dihapus sembarangan
- **Overloading (Information Overload)** — terlalu banyak elemen visual dalam 1 grafik

### P
- **Package** — folder modul terkait + wajib `__init__.py`
- **Palindrome** — sama dibaca depan-belakang — `"madam"`
- **Parameter (Programming)** — variabel placeholder di `()` deklarasi fungsi
- **Parameter (Statistics)** — ringkasan numerik karakteristik POPULASI (umumnya tidak diketahui pasti) — **beda dengan Parameter Programming**, hati-hati Pola #3
- **Parent Class (Base Class)** — class umum sumber pewarisan
- **Parent Table (Tabel Induk)** — tabel menyimpan PK yang dirujuk tabel lain
- **`pass`** — placeholder blok kosong, beda `continue`
- **P-Value** — >0.05 asumsikan normal, <0.05 jangan asumsikan normal
- **Percentile** — nilai persentase tertentu observasi di bawahnya
- **Pie Chart** — proporsi bagian dari keseluruhan; hindari kategori >5 atau tren waktu
- **.pivot_table()** — reorganisasi & rangkum data tabular
- **Polymorphism** — pilar OOP lanjutan, method sama nama beda perilaku (di luar cakupan Sesi 7)
- **Population (Populasi)** — keseluruhan target penyelidikan
- **Port** — nomor pintu komunikasi jaringan DBMS, contoh `3306`
- **`.pop()` / `.popitem()`** — hapus & return elemen/pasangan (List: by index; Dict: by key/terakhir; Set: acak)
- **`pow()`** — perpangkatan — `pow(2,3)` → `8`
- **Precision & Recall** — metrik pengganti Accuracy pada imbalanced data
- **Primary Key (PK)** — identifikasi unik baris, wajib unik & NOT NULL
- **`print()`** — tampilkan output ke layar
- **Procedural Programming** — fokus function & logic terpisah dari data
- **Project** — level tertinggi Project → Package → Module
- **Proper Subset / Proper Superset** — subset/superset tidak boleh identik (`<`/`>`)
- **Pseudocode** — versi sederhana bahasa alami sebelum kode nyata
- **Pull Request** — mekanisme GitHub ajukan perubahan kode untuk direview
- **python-dotenv** — load variabel dari `.env` — `load_dotenv()`

### Q
- **QQ Plot (Quantile-Quantile Plot)** — plot kuantil teoretis vs aktual, paling sensitif deteksi non-normal
- **Quartile (Kuartil)** — persentil khusus membagi data jadi 4 (Q1=P25, Q2=median, Q3=P75)
- **Query** — perintah pencarian/permintaan data ke database
- **Quick Count vs Real Count** — hitung cepat sampel vs hitung penuh populasi

### R
- **Randomization** — alokasi acak unit eksperimen agar covariates seimbang
- **`range()` (Python)** — hasilkan urutan angka, `stop` EKSKLUSIF — `range(1,5)` → `1,2,3,4`
- **Range (Rentang, Statistics)** — `Max - Min`, sensitif nilai ekstrem — beda dengan `range()` fungsi Python
- **Ratio Scale** — nol ABSOLUT, boleh kali/bagi — tinggi badan
- **Recursion / Recursive Function** — fungsi memanggil dirinya sendiri, wajib Base Case + Recursive Case
- **Recursive Case** — kondisi (N>1) fungsi rekursif memanggil dirinya dengan parameter lebih kecil
- **Referencing** — entitas tabel merujuk entitas tabel lain
- **Relational Model Constraints** — aturan menjaga integritas data database relasional
- **`.remove()`** — hapus by value; error kalau tidak ada (beda `.discard()` di Set)
- **`.replace(lama, baru, count)`** — ganti substring, parameter ke-3 batasi jumlah — `"aa".replace("a","b",1)` → `"ba"`
- **Repository (Repo)** — folder proyek yang dipantau Git
- **`.reshape()`** — ubah dimensi array, `-1` = flatten otomatis
- **.reset_index() / .set_index()** — kembalikan indeks default / jadikan kolom sebagai indeks
- **Result-set** — tabel hasil sementara output SELECT
- **`return`** — kirim nilai balik ke pemanggil, hentikan eksekusi fungsi (beda `print()`)
- **Right-Skewed Distribution (Skewness Positif)** — ekor ke KANAN, mayoritas di nilai rendah; median dekat Q1
- **RIGHT (OUTER) JOIN** — semua baris kanan + cocok dari kiri; `A RIGHT JOIN B` = `B LEFT JOIN A`
- **`round()` (Python)** — bulatkan angka — `round(3.14159,2)` → `3.14`
- **ROUND() (SQL)** — fungsi scalar SQL, sama konsepnya dengan `round()` Python tapi beda sistem
- **Runner-Up Score** — cari nilai tertinggi kedua via `set()` + `sorted()` lalu `[-2]`

### S
- **Sample (Sampel)** — bagian populasi yang diobservasi langsung
- **Sampling Bias** — sampel tidak representatif terhadap populasi
- **Sampling Frame** — daftar representasi seluruh anggota populasi yang bisa diakses
- **Sankey Diagram** — visualisasi aliran & hubungan kuantitas antar entitas
- **Scalar Function** — beroperasi per-baris individual — `ROUND()`, `LENGTH()`, `UCASE()`, `LCASE()`
- **Scalar Subquery** — subquery wajib return satu nilai tunggal
- **Scale of Measurement** — 4 tingkatan: Nominal, Ordinal, Interval, Ratio
- **Scatter Plot** — titik koordinat 2D untuk korelasi 2 variabel numerik
- **Scope** — aturan di mana variabel bisa diakses
- **Secondary Axis** — sumbu Y kedua untuk dua variabel skala jauh beda — `ax2 = ax1.twinx()`
- **SELECT** — DML ambil/tampilkan data
- **`self`** — referensi ke current object, parameter pertama wajib tiap method
- **Self JOIN** — join tabel dengan dirinya sendiri, wajib 2 alias berbeda + `<>`
- **Sequences** — koleksi terurut: `list`, `tuple`, `range`
- **Series (Pandas)** — struktur 1 dimensi Pandas dengan indeks berlabel
- **`.setdefault()`** — tambah key baru dengan default HANYA jika key belum ada (defensif, beda `.update()` yang agresif)
- **Set** — koleksi unik tak terurut, mutable — `{1,2,3}`
- **SHA-1 Hash** — 40 karakter heksadesimal identitas unik commit Git
- **Shallow Copy** — lihat `.copy() (Python collections)`
- **Shallow Import** — impor ringkas dari tingkat package utama — `from preprocessing import standardize_text`
- **Shapiro-Wilk Test** — uji normalitas paling kuat, eksklusif Distribusi Normal
- **SHOW DATABASES / SHOW TABLES** — tampilkan daftar database/tabel
- **Short-circuit Evaluation** — Python berhenti evaluasi `and`/`or` begitu hasil pasti
- **Simple Random Sample** — semua anggota populasi peluang sama
- **Single Item Tuple** — wajib koma di akhir — `(5,)` bukan `(5)`
- **Single Responsibility Principle** — 1 modul/fungsi = 1 tanggung jawab
- **Skewness (Kemiringan Distribusi)** — ketidaksimetrisan sebaran, dibaca dari posisi median relatif Q1/Q3
- **Slicing (List/String/Tuple)** — `[start:stop:step]`, start inklusif, stop EKSKLUSIF (lihat Pola #1)
- **Slicing (NumPy — View vs Copy)** — hasil slice = VIEW (referensi), bukan salinan independen — wajib `.copy()` eksplisit
- **snake_case** — konvensi penamaan Python (PEP 8) — `total_price`
- **`sorted()`** — urutkan ascending tanpa ubah objek asli; dukung `key=lambda` untuk sorting kompleks; pada dict, HANYA return keys
- **.sort_values() / .sort_index()** — urutkan berdasar NILAI kolom / LABEL indeks
- **Stacked Bar / Stacked Area Chart** — komposisi bertumpuk, periode sedikit (Bar) vs banyak (Area)
- **Stack Overflow** — call stack kehabisan memori akibat rekursi tanpa base case valid
- **Staging Area** — area antre file menunggu di-commit, diisi `git add`
- **Standard Deviation** — akar kuadrat varians; estimasi kasar `Range/4` atau `1.34898×IQR`
- **State** — data keadaan object dalam attribute-nya
- **Statistic (Statistik Sampel)** — ringkasan numerik dari data SAMPEL
- **Statistics (Statistika)** — seni & sains "belajar dari data"
- **`.startswith()`** — cek awalan string
- **Stopping Condition** — syarat batas loop berhenti
- **Str / String** — tipe data teks
- **Stratified Sample** — populasi dibagi grup HOMOGEN, sampel acak dari SEMUA grup
- **`.strip()`** — hapus spasi awal-akhir
- **`.split()`** — pecah string jadi list berdasar pemisah
- **String Concatenation** — gabung string dengan `+`, butuh `str()` manual
- **Subquery (Nested Query)** — query di dalam query, inner dieksekusi duluan
- **Subset** — himpunan A subset B jika seluruh elemen A ada di B
- **`sum()`** — jumlahkan elemen angka koleksi
- **`super()`** — merujuk parent class, `super().__init__()`
- **Superset** — himpunan A superset B jika seluruh elemen B ada di A
- **Symmetric Difference (Set)** — elemen hanya di salah satu himpunan — `A ^ B`
- **Systematic Sample** — interval numerik tetap dari titik awal acak

### T
- **Table Expression** — istilah lain Derived Table
- **Terminator (flowchart)** — simbol oval, titik Start/End
- **Tower of Hanoi** — studi kasus klasik logika rekursif
- **Tracked / Untracked files (Git)** — dikenal vs belum pernah direkam Git
- **Treemap** — visualisasi hierarkis kotak bersarang, luas sebanding kontribusi nilai
- **Truthy** — angka bukan-nol, string berisi, koleksi berisi
- **Tuple** — koleksi terurut, immutable — `(1,2,3)`
- **Tuple Trick (multi-criteria sort)** — `sorted(data, key=lambda x: (-x[1], x[0]))`
- **Type Casting / Type Conversion** — `int("5")`, `str(5)`, `float("3.14")`
- **Type Hint** — anotasi tipe (dokumentasi saja, TIDAK validasi runtime)
- **`type()`** — cek tipe data variabel
- **TypeError** — operasi pada tipe data tidak kompatibel

### U
- **UCASE()/UPPER(), LCASE()/LOWER() (SQL)** — ubah teks jadi huruf besar/kecil
- **UnboundLocalError** — ubah variabel global dalam fungsi tanpa `global` — Python anggap variabel lokal baru
- **Union (Set)** — gabungan elemen unik dua himpunan — `A | B`
- **Universal Functions (NumPy ufunc)** — fungsi matematika element-wise — `np.sqrt()`, `np.exp()`, `np.log()`
- **UPDATE** — ubah baris data yang sudah ada
- **Up-sampling** — tambah sampel minoritas secara sintetik
- **`.update()`** — Dict: timpa banyak pasangan (agresif); Set: tambah banyak elemen
- **`.upper()`** — huruf besar semua
- **USE (database)** — aktifkan database tertentu
- **Username** — identitas akun akses database

### V
- **Value (Dictionary)** — data pada pasangan key-value, boleh duplikat
- **.value_counts()** — hitung frekuensi tiap nilai unik kolom
- **Variable** — wadah bernama menyimpan data di memori
- **Vectorization** — operasi matematika ke seluruh elemen array sekaligus, tanpa loop manual
- **Version Control System (VCS)** — sistem lacak perubahan kode
- **Violin Plot** — kombinasi Box Plot + Kernel Density Plot

### W
- **Whiskers** — perpanjangan Box Plot dari kotak IQR ke nilai ekstrem non-outlier
- **WHERE Clause** — saring baris individual, dieksekusi SEBELUM `GROUP BY`
- **`while` loop** — perulangan selama kondisi True
- **Wildcard (% dan _)** — `%` = 0/banyak karakter, `_` = tepat 1 karakter
- **`with` statement** — buka file, otomatis tertutup setelah blok selesai
- **Word Cloud** — ukuran kata sebanding frekuensi kemunculan
- **Working Directory (Git)** — folder kerja aktif
- **`.where()` (np.where)** — ganti elemen array kondisional — `np.where(data < 0, 0, data)`

### Y
- **YEAR(), MONTH(), DAY(), DAYOFWEEK(), HOUR()**, dll. — ekstraksi komponen tanggal/waktu, hasil integer
- **DAYNAME(), MONTHNAME()** — konversi tanggal ke nama hari/bulan (teks)
- **Date Arithmetic** — tambah/kurang langsung nilai tanggal — `DATE(payment_date) + 1`

### Z
- **Zero-based Indexing** — pengindeksan mulai dari `0`
- **ZeroDivisionError** — membagi dengan angka nol

### Simbol / Dunder
- **`__dict__`** — attribute bawaan object, seluruh attribute-nya dalam bentuk dictionary
- **`__init__.py`** — file penanda folder sebagai package Python resmi, boleh kosong

---

## 🔍 Gap Analysis & Catatan Penting

> Status per 2026-09-02. Exam 1 sudah **LULUS 17/20 (85%)**. Bagian ini relevan untuk CC1 LeetCode & pendalaman kode praktik, bukan lagi syarat exam konsep.

### Kode Python — per modul

| Modul | Sesi terkait | Status |
|---|---|---|
| `collection-data-type/` | Sesi 4 | ✅ 12/12 file selesai |
| `conditional-and-loop-statements/` | Sesi 3 | ⬜ 0/11 file |
| `python-function-and-file-handling/` | Sesi 5 | ⬜ 0/5 file |
| `object-oriented-programming/` | Sesi 7 | ⬜ 0/4 file |
| `python-modular-programming/` | Sesi 8 | sebagian kesentuh (lihat [PANDUAN_LANJUT_BELAJAR.md](../PANDUAN_LANJUT_BELAJAR.md)) |
| `data-manipulation-pandas-numpy/` | Sesi 12 | ⬜ 0/11 file |
| `sql-exercise-materials-/9` | Sesi 9 | ⬜ 0/14 file |
| `sql-exercise-materials-/10` | Sesi 10 | ⬜ 0/6 file |

### Code Challenge 1 (CC1) — LeetCode, deadline 2026-09-03

- Status: **1/4 soal** — Convert the Temperature ✅ Accepted, proof submitted.
- Sedang dikerjakan: **Two Sum** (dict/complement approach).
- Sisa rencana: **Contains Duplicate** (`set`, paling simpel), lalu opsional **Remove Duplicates from Sorted Array**.
- Submit: link profil LeetCode + screenshot "Accepted" per soal → form resmi (lihat [PANDUAN_LANJUT_BELAJAR.md](../PANDUAN_LANJUT_BELAJAR.md)).

### Catatan verifikasi silang (cek ke PDF resmi kalau ragu)

1. **Sesi 3**: dua versi algoritma cek bilangan prima (loop `range(2,n)` vs optimized `range(2,int(n**0.5)+1)`) — cheat sheet ini pakai versi pertama sesuai konteks trace di modul.
2. **Sesi 9-10**: istilah "correlated vs non-correlated subquery" TIDAK muncul eksplisit di materi — semua contoh subquery non-correlated.
3. **Sesi 9-10**: urutan eksekusi SQL (FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY→LIMIT) adalah pengetahuan SQL standar konsisten dengan modul, tapi modul tidak menyebut istilah ini eksplisit.
4. **Sesi 12**: sumber asli menyebut `np.linspace()` hasilkan "angka acak" — kemungkinan salah tulis transkrip, karena `linspace` sebenarnya DETERMINISTIK. Sudah dikoreksi di sini.
