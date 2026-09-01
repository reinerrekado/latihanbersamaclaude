---
tags: [module1, sesi-07, python, oop, class, object, self, inheritance]
aliases: ["Sesi 7"]
---

# Session 7 — Object Oriented Programming

Study guide ini membahas fondasi *Object-Oriented Programming* (OOP) di Python: apa itu *class* dan *object*, konstruktor `__init__`, atribut `self`, *methods*, hingga *basic inheritance* (`super().__init__()`). Materi ditutup dengan latihan praktis membangun `class BankAccount` dan mekanisme `if __name__ == '__main__'`.

> [!tip] Catatan cakupan
> Sesuai penekanan instruktur, sesi ini sengaja membatasi diri pada fondasi OOP (*class*, *object*, *attributes*, *methods*, *basic inheritance*) karena itulah yang paling sering dipakai dalam pekerjaan AI Engineering sehari-hari. Pilar OOP lanjutan (*encapsulation*, *abstraction*, *polymorphism*) disebut tapi tidak didalami — lihat catatan singkat di akhir Bab 1.

---

## Bab 1 — Pendahuluan Object Oriented Programming (OOP)

### 1.1 Definition dan Characteristics dari OOP

#### A. Conceptual Foundation

- Object-Oriented Programming (OOP) merupakan sebuah *software design paradigm* yang mengorganisasi *code* di sekitar *objects* (*data*) dibandingkan di sekitar *functions* dan *logic*.
- *Paradigm* ini memodelkan *real-world entities* dengan mengelompokkan *data* (*attributes*) dan *behaviors* (*methods*) ke dalam satu kesatuan *unit* yang kohesif (*single cohesive unit*).
- Di dunia nyata, segala sesuatu yang ada di sekitar kita dapat diposisikan sebagai kumpulan dari *objects* (seperti *laptop*, *handphone*, *tumblr*, atau *user*).

#### B. Attributes dan Methods dalam OOP

Setiap *object* didefinisikan oleh dua karakteristik utama:
- *Attributes*: *Data* yang merepresentasikan *state* atau identitas dari sebuah *object* (misalnya: *name*, *age*, *email* pada *object* *user*).
- *Methods*: *Function* yang menggambarkan kemampuan atau *behavior* dari *object* tersebut, yang menempel pada *object* yang bersangkutan (misalnya: *update_info*, *get_info*, *greet*).

> [!warning] Audio Insight — Mengapa OOP Penting Meski Sering Dilewati
> Dalam program *AI engineering*, materi terkait OOP sering kali dilewati karena pembelajaran Python dilakukan secara sekilas. Padahal, pemahaman konsep dasar OOP sangat krusial agar tidak membingungkan saat masuk ke dalam implementasi praktis yang banyak menggunakan *paradigm* ini.
>
> Untuk kebutuhan *AI engineering*, fokus utama ditekankan pada penguasaan dasar-dasar OOP seperti *class* (sebagai *blueprint*), *object* (sebagai *instance*), *attributes*, dan *methods*. Konsep tingkat lanjut yang sangat mendalam seperti *encapsulation*, *abstraction*, dan *polymorphism* jarang digunakan secara intensif dalam pekerjaan sehari-hari di bidang ini.

> [!tip] Sekilas tiga pilar lanjutan (ditambahkan sebagai konteks ringan, di luar cakupan wajib sesi ini)
> - **Encapsulation**: menyembunyikan detail internal object, biasanya dengan awalan `_` atau `__` pada atribut (contoh: `self.__balance`) supaya tidak diubah langsung dari luar.
> - **Abstraction**: menyembunyikan kompleksitas implementasi dan hanya menampilkan antarmuka (*interface*) yang sederhana ke pengguna class.
> - **Polymorphism**: kemampuan *method* dengan nama sama berperilaku berbeda tergantung class-nya, contoh singkat:
> ```python
> class Kucing:
>     def suara(self):
>         return "Meong"
>
> class Anjing:
>     def suara(self):
>         return "Guk"
>
> for hewan in [Kucing(), Anjing()]:
>     print(hewan.suara())   # Output: Meong
>                              #         Guk
> ```
> Ketiganya tidak perlu dihafal mendalam untuk kebutuhan AI Engineering — cukup mengenal istilahnya.

---

### 1.2 Perbandingan Procedural Programming dan Object-Oriented Programming (OOP)

#### A. Paradigm Organisasi Code

Perbedaan struktural utama antara *procedural programming* dan *object-oriented programming* terletak pada pemisahan dan pengelompokan *data* serta *functions*:

| Karakteristik | Procedural Programming | Object-Oriented Programming (OOP) |
|:--|:--|:--|
| **Organisasi Utama** | Berfokus pada *functions* dan *logic*. | Berfokus pada *objects* dan *data*. |
| **Relasi Data & Function** | *Function* (*behavior*) dan *data* terkait berada dalam *unit* atau *logic* yang terpisah (*separate unit/logic*). | *Function* (*behavior*) dan *data* terkait disatukan dalam satu grup *code* (*class unit*). |
| **Aksesibilitas Function** | *Function* dibuat secara mandiri dan dapat digunakan oleh *object* atau *data type* apa saja secara bebas. | *Methods* (*functions*) menempel secara eksklusif pada *object* tertentu dan hanya milik *object* tersebut. |

#### B. Perbandingan melalui Implementasi Code Python

##### 1. Procedural Programming Approach

Pada *procedural approach*, *data* didefinisikan secara independen sebagai variabel-variabel terpisah, dan *functions* eksternal menerima *data* tersebut untuk melakukan operasi:

```python
name = "Alex"
email = "alex@ex.com"
age = 20

def update_email(new_email):
    global email
    email = new_email

def get_user_info():
    return {
        "name" : name,
        "email" : email,
        "age" : age,
    }

def send_email():
    return f"email send to {email}"
```

> [!tip] Lihat juga
> Perhatikan `global email` di atas — inilah `global` keyword yang dijelaskan lengkap di [[Sesi 05 - Python Function and File Handling]] Bab 2.3, contoh nyata mengapa OOP dibutuhkan: pendekatan prosedural terpaksa memakai `global` berulang kali untuk mengubah state.

##### 2. Object-Oriented Programming (OOP) Approach

Pada *object-oriented approach*, seluruh *data* (*attributes*) dan *functions* (*methods*) dibungkus bersama di dalam sebuah deklarasi *class*:

```python
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def change_email(self, new_email):
        self.email = new_email

    def get_user_info(self):
        return self.__dict__

    def send_email(self):
        return f"email send to {self.email}"
```

**Contoh penggunaan `self.__dict__` (ditambahkan agar terlihat outputnya):**

```python
user1 = User("Alex", "alex@ex.com", 20)
print(user1.get_user_info())
# Output: {'name': 'Alex', 'email': 'alex@ex.com', 'age': 20}
# self.__dict__ mengembalikan semua attribute milik object dalam bentuk dictionary
```

> [!warning] Audio Insight — Built-in Data Types Sudah Berbasis OOP
> Tanpa disadari, ketika memprogram menggunakan Python, kita sudah sering menggunakan *built-in data types* berbasis *OOP paradigm*. Contohnya adalah *data type* *list* atau *dictionary*, di mana setiap kali kita melakukan *instantiation* (seperti membuat *list* kosong), kita sebenarnya sedang memanggil *constructor* dari *class* *list*.
>
> *Built-in data types* tersebut memiliki *methods* eksklusif yang menempel padanya (seperti `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, dan `.clear()`) yang tidak dapat digunakan oleh *data type* lain yang berbeda *class* *blueprint*-nya.

> [!tip] Lihat juga
> Ini menjelaskan mengapa `list` dan `dict` yang dipakai sejak [[Sesi 04 - Data Types Collection Notes]] terasa punya "kemampuan" (method) sendiri-sendiri — keduanya sebenarnya adalah *class* bawaan Python. Prinsip yang sama juga menjelaskan mengapa objek `DataFrame` di [[Sesi 12 - Python Data Manipulation With Pandas and Numpy]] punya method seperti `.head()`, `.describe()`, `.groupby()` — DataFrame adalah *object* hasil instansiasi dari `class DataFrame` milik library Pandas.

---

### 1.3 Alasan Penggunaan dan Complexity Management

#### A. Mengelola Complexity Perangkat Lunak

Seiring dengan perkembangan skala perangkat lunak, mengorganisasi *code* murni hanya berdasarkan *functions* dan *logic* prosedural akan membuat hubungan (*relationship*) antara *data* dan *behavior* menjadi semakin sulit dikelola (*harder to manage*). OOP menyediakan mekanisme alternatif untuk mengorganisasi *complexity* tersebut agar lebih terstruktur dan rapi.

#### B. Efisiensi Passing Data (Self-Tracking Data)

| Parameter Perbandingan | Tanpa OOP (Procedural) | Dengan OOP |
|:--|:--|:--|
| **Pengelolaan State** | Pengembang harus secara berulang kali mengirimkan (*repeatedly pass*) *data* *state* (seperti *account balance*) ke setiap *function* yang membutuhkannya. | *Object* melacak *data*-nya sendiri secara internal (*keeps track of its own balance*), menghilangkan kebutuhan *passing parameter* berulang kali. |
| **Ketergantungan Function** | *Function* sangat bergantung pada *parameter* luar yang dipasok secara eksplisit pada setiap pemanggilan. | *Methods* dapat mengakses *data* *object* kapan saja melalui referensi internal (`self`). |

##### 1. Non-OOP Approach (Repeatedly passing data)

```python
def deposit(account_balance, amount):
    return account_balance + amount

def withdraw(account_balance, amount):
    if amount <= account_balance:
        return account_balance - amount
    return account_balance

account_balance_1 = 100
account_balance_2 = 200

account_balance_1 = deposit(account_balance_1, 100)
account_balance_2 = deposit(account_balance_2, 200)

account_balance_1 = withdraw(account_balance_1, 10)
account_balance_2 = withdraw(account_balance_2, 30)
```

##### 2. OOP Approach (Object mengelola datanya sendiri)

```python
class Account:
    def __init__(self, amount):
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

account_1 = Account(100)
account_2 = Account(200)

account_1.deposit(100)
account_2.deposit(200)

account_1.withdraw(10)
account_2.withdraw(30)
```

> [!warning] Audio Insight — Independensi Alamat Memori Antar-Object
> Implementasi OOP memisahkan alamat memori (*memory address*) untuk setiap *object* secara terpisah. Ketika kita membuat `account_1` and `account_2` dari *class* `Account` yang sama, kedua *objects* tersebut tetap merupakan entitas yang terpisah secara independen di memori. Segala perubahan keadaan (*state change*) seperti penambahan *balance* pada satu akun tidak akan memengaruhi *balance* akun lainnya.

```python
# Pembuktian independensi memori (ditambahkan)
print(account_1.balance)   # Output: 190  (100 + 100 - 10)
print(account_2.balance)   # Output: 370  (200 + 200 - 30)
print(account_1 is account_2)   # Output: False -> dua object yang benar-benar terpisah
```

---

## Bab 2 — Konsep Dasar Class dan Object

### 2.1 Definition dan Characteristics dari Class

#### A. Conceptual Foundation

- *Class* merupakan sebuah *blueprint* (cetak biru) yang menetapkan *data* (*attributes*) dan *behaviors* (*methods*) yang dapat dimiliki oleh suatu tipe *object*.
- Saat membuat sebuah *class*, kita tidak sedang mendefinisikan suatu entitas secara spesifik, melainkan membuat sebuah representasi umum (*general representation*) mengenai apa saja yang dapat dimiliki dan dilakukan oleh tipe *object* tersebut.

#### B. Analogy dari Class

Analogi nyata dari sebuah *class* adalah ketika kita mengamati mobil (*cars*):
- *Attributes* (Karakteristik/Data): Setiap mobil secara umum memiliki kapasitas bahan bakar (*fuel_capacity*), tipe mobil (*type_of_car*), dan jenis mesin (*engine_type*).
- *Behaviors* (Kemampuan/Perilaku): Setiap mobil secara umum dapat membunyikan klakson (*honk()*), melaju ke depan (*move_forward()*), melakukan akselerasi (*accelerate()*), bergerak mundur (*move_backward()*), dan mengerem (*brake()*).

Representasi umum dari karakteristik dan perilaku mobil inilah yang didefinisikan di dalam sebuah *Class*.

#### C. Python Implementation dari Class

```python
class Car:
    type_name = "suv"
    fuel_capacity = 45
    engine_type = "petrol"

    def honk(self):
        pass

    def move_forward(self):
        pass

    def brake(self):
        pass
```

> [!warning] Audio Insight — Class Ibarat Formulir Kosong
> Dosen menjelaskan bahwa mendefinisikan sebuah *class* mirip seperti membuat sebuah formulir (*form*). Formulir tersebut menetapkan kolom-kolom kosong apa saja yang harus diisi, seperti *fuel_capacity*, *type_of_car*, dan *engine_type*.
>
> Selain atribut standar di atas, mahasiswa mengusulkan beberapa *attributes* tambahan yang dapat mendefinisikan mobil, seperti jumlah ban/roda, warna (*color*), merek (*brand*), dan tahun pembuatan (*year of manufacture*). Untuk bagian *behaviors*, mahasiswa juga mengusulkan perilaku tambahan seperti belok kanan (*turn right*), belok kiri (*turn left*), dan posisi gigi netral (*gear neutral*).
>
> Analogi industri nyata yang diberikan oleh dosen adalah platform *e-commerce* Shopee: *Class* *User* di Shopee didefinisikan dengan *attributes* berupa *name*, *ID*, *password*, tanggal lahir, dan *gender*. *Behaviors* (*methods*) yang melekat pada *Class* *User* tersebut meliputi tindakan seperti tambah ke keranjang (*add to cart*), melakukan *check out*, masuk log (*sign in*), dan keluar log (*sign out*).

---

### 2.2 Definition dan Characteristics dari Object

#### A. Instance dari Class

- *Object* merupakan instansiasi spesifik (*specific instance*) dari sebuah *class*.
- Ketika kita telah memiliki *blueprint* (*class*), kita memerlukan objek nyata yang dibangun berdasarkan cetak biru tersebut untuk dapat digunakan di dalam program.
- *Object* yang dibuat dari *class* yang sama akan berbagi *attributes* dan *behaviors* yang didefinisikan oleh *class* tersebut, namun masing-masing *object* memiliki data keadaan (*state*) sendiri.

#### B. State dan Memory Allocation

Setiap *object* yang dibuat bersifat independen satu sama lain dan disimpan pada alamat memori (*memory address*) yang berbeda. Perubahan keadaan (*state change*) pada satu *object* tidak akan memengaruhi keadaan *object* lainnya.

#### C. Python Implementation dari Object Creation

```python
class Car:
    type_name = "suv"
    fuel_capacity = 45
    engine_type = "petrol"
    color = "red"
    position = 0

    def honk(self):
        print("Tin! Tin!")

    def move_forward(self):
        self.position += 1

    def brake(self):
        print("brake!")

# Instantiation (pembuatan object)
car_john = Car()
car_emily = Car()

# Mengakses attributes
print(car_john.color)      # Output: red
print(car_emily.color)     # Output: red

# Memanggil methods
car_john.honk()             # Output: Tin! Tin!
car_john.move_forward()

# Memeriksa perbedaan state masing-masing object
print(car_john.position)    # Output: 1
print(car_emily.position)   # Output: 0
```

> [!warning] Audio Insight — Identitas Object dan Hubungan dengan Built-in Data Types
> Di dunia nyata, segala sesuatu di sekeliling kita pada dasarnya adalah kumpulan dari *objects*, seperti *laptop*, *handphone*, *tumblr*, atau *user*.
>
> Proses pembuatan *object* dilakukan dengan memanggil *constructor*, yaitu menuliskan nama *class* diikuti dengan tanda kurung buka dan tutup (seperti `Car()`), lalu menyimpannya ke dalam suatu variabel (misalnya `car_john = Car()`).
>
> Pengecekan identitas menggunakan operator `is` (misalnya `car_john is car_emily`) akan mengembalikan nilai `False`. Hal ini membuktikan bahwa meskipun dibuat dari *class* yang sama, keduanya merupakan dua *objects* terpisah dengan alamat memori (*memory address*) yang berbeda secara independen.
>
> Hubungan *Class* dan *Object* dengan *Built-in Data Types* di Python: tanpa disadari, tipe data bawaan Python seperti *list* dan *dictionary* merupakan sebuah *Class* yang dibuat oleh pengembang Python. Saat kita menuliskan kode untuk membuat *list* kosong seperti `my_list = []` atau `my_list = list()`, kita sebenarnya sedang memanggil *constructor* dari *Class* *list* untuk menciptakan sebuah *Object* (*instance*) baru. Setiap *Object* dari kelas *list* tersebut memiliki akses ke *methods* eksklusif yang didefinisikan di dalam cetak birunya, seperti `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, dan `.clear()`. *Methods* tersebut hanya dapat digunakan oleh objek yang bertipe kelas *list* dan tidak dapat dipanggil secara sembarangan oleh tipe objek lain dari kelas yang berbeda.

```python
# Pembuktian operator 'is' (ditambahkan)
print(car_john is car_emily)   # Output: False
print(car_john is car_john)    # Output: True (merujuk objek yang sama persis)
```

---

## Bab 3 — Konstruktor __init__ dan Atribut self

### 3.1 Konstruktor `__init__` dalam Class

#### A. Conceptual Foundation dari `__init__`

- `__init__` merupakan sebuah *special method* di Python yang bertindak sebagai *constructor* untuk membangun *object* dari suatu *class*.
- *Constructor* ini dijalankan secara otomatis (*automatically runs*) pada saat sebuah *object* diinisialisasi atau diciptakan.
- Fungsi utama dari `__init__` adalah untuk memberikan nilai awal (*initial values*) bagi konfigurasi, *attributes*, atau *state* dari *object* tersebut pada saat pertama kali dibuat.

#### B. Perbedaan Pengisian State Tanpa dan Dengan `__init__`

| Pendekatan | Karakteristik Inisialisasi | Dampak pada Object |
|:--|:--|:--|
| **Without `__init__`** | Atribut di-*hardcode* secara langsung di dalam badan *class*. | Semua *objects* yang dibuat memiliki nilai *attributes* yang identik pada awal pembuatan. |
| **With `__init__`** | Atribut diinisialisasi secara dinamis melalui argumen yang dikirim ke *constructor*. | Setiap *object* dapat memiliki *configuration* dan *state* awal yang unik sejak pembuatan. |

#### C. Python Implementation dari `__init__`

##### 1. Class Tanpa `__init__` (Attributes Identik)

```python
class Car:
    type_name = "SUV"
    fuel_capacity = 45
    engine_type = "petrol"
    color = "red"
    position = 0

# Setiap objek akan selalu memiliki state awal yang sama
car_john = Car()
car_emily = Car()
```

##### 2. Class Dengan `__init__` (Attributes Dinamis)

```python
class Car:
    def __init__(self, type_name, fuel_capacity, engine_type, color):
        self.type_name = type_name
        self.fuel_capacity = fuel_capacity
        self.engine_type = engine_type
        self.color = color
        self.position = 0

# Objek dikonstruksi dengan nilai awal berbeda
car_john = Car("sedan", 45, "petrol", "red")
car_emily = Car("SUV", 50, "petrol", "yellow")
```

> [!warning] Audio Insight — Arti Kata "Constructor" dan Magic Method
> Dosen menjelaskan bahwa kata "*construct*" secara harfiah berarti membangun. Jadi, *constructor* adalah metode khusus yang digunakan untuk membangun atau mendirikan sebuah *object* dari cetak birunya (*class*).
>
> Untuk memanggil *constructor* di Python, pengguna cukup menuliskan nama *class* diikuti dengan tanda kurung dan argumen yang diperlukan, misalnya `Car("sedan", 45, "petrol", "red")`. Tindakan ini secara otomatis memicu eksekusi metode `__init__` di latar belakang.
>
> Mahasiswa mengamati bahwa *special method* ini selalu diawali dan diakhiri dengan dua karakter *underscore* (`__init__`), yang menandakan metode tersebut merupakan *magic method* bawaan Python yang memiliki perilaku khusus.

---

### 3.2 Atribut self dan Referensi Current Object

#### A. Conceptual Foundation dari self

- `self` adalah variabel referensi bawaan di Python yang merujuk secara eksklusif kepada *current object* (objek saat ini yang sedang diproses atau diakses oleh program).
- Di dalam definisi *class*, `self` digunakan untuk mengakses *attributes* dan *methods* milik objek tersebut secara internal.
- Setiap kali kita mendefinisikan *method* di dalam *class*, parameter pertama dari *method* tersebut secara mutlak harus diisi oleh `self`.

#### B. Mekanisme Kerja self di Memori

- Ketika sebuah *method* dipanggil melalui objek tertentu, Python secara otomatis melewatkan objek tersebut sebagai argumen pertama untuk parameter `self`.
- Melalui referensi `self`, Python mengetahui objek mana di memori yang data *attributes*-nya harus dibaca atau diubah, sehingga tidak terjadi tumpang tindih data antar-objek.

| Sintaks Pemanggilan | Interpretasi Internal Python | Keterangan |
|:--|:--|:--|
| `car_john.move_forward(10)` | `Car.move_forward(car_john, 10)` | Objek `car_john` dikirim sebagai parameter `self` secara otomatis. |
| `self.color` | Mengakses *attribute* `color` dari objek pemanggil | Merujuk langsung ke alamat memori spesifik objek saat ini. |

> [!tip] Kunci penting soal `self`: bukan soal posisi kode, tapi soal *cara method dipanggil*
> Poin yang sering bikin bingung: `self` **bukan** ditentukan oleh di mana kode method itu berada di dalam file, melainkan ditentukan oleh **objek mana yang ada di sebelah kiri titik (`.`) saat method dipanggil**. Baris kode method-nya sendiri selalu sama persis — yang berubah adalah objek apa yang "mengisi" `self` setiap kali dipanggil.
>
> ```python
> class Car:
>     def __init__(self, color):
>         self.color = color
>
>     def show_color(self):
>         print(f"Warna mobil ini: {self.color}")
>
> mobil_a = Car("merah")
> mobil_b = Car("biru")
>
> mobil_a.show_color()   # Python diam-diam menjalankan: Car.show_color(mobil_a)
>                         # -> di dalam method, self = mobil_a, jadi self.color = "merah"
>                         # Output: Warna mobil ini: merah
>
> mobil_b.show_color()   # Python diam-diam menjalankan: Car.show_color(mobil_b)
>                         # -> di dalam method, self = mobil_b, jadi self.color = "biru"
>                         # Output: Warna mobil ini: biru
>
> # Pembuktian langsung memanggil lewat nama class (jarang dipakai, tapi membuktikan mekanismenya):
> Car.show_color(mobil_a)   # sama persis hasilnya dengan mobil_a.show_color()
>                            # Output: Warna mobil ini: merah
> ```
> Method `show_color` di atas hanya ditulis SATU KALI di dalam class. Yang membuat outputnya berbeda antara `mobil_a` dan `mobil_b` bukan lokasi kodenya (posisinya sama-sama di dalam class Car), melainkan objek mana yang dipakai untuk memanggilnya via titik (`.`).

#### C. Python Implementation dari self

```python
class Car:
    def __init__(self, type_name, color):
        self.type_name = type_name
        self.color = color

    def print_current_object_info(self):
        # Mengakses attributes milik objek saat ini menggunakan self
        print(f"Type: {self.type_name}")
        print(f"Color: {self.color}")

car_john = Car("sedan", "red")

# Pemanggilan method
car_john.print_current_object_info()
```

> [!warning] Audio Insight — self sebagai "Diri Sendiri" Object
> Berdasarkan penjelasan dosen, `self` dapat dibayangkan sebagai cara objek merujuk ke "dirinya sendiri".
>
> Ketika kita membuat `car_john = Car("sedan", "red")`, maka di dalam memori, `self` akan merujuk ke objek `car_john`. Jadi, pernyataan `self.type_name = type_name` diartikan oleh Python sebagai `car_john.type_name = "sedan"`.
>
> Demikian juga jika kita membuat `car_emily = Car("SUV", "yellow")`, maka `self` untuk objek tersebut akan mengarah ke `car_emily`, sehingga `self.color = color` diterjemahkan sebagai `car_emily.color = "yellow"`. Hal inilah yang menjamin bahwa perubahan *state* pada satu objek disimpan secara terisolasi di alamat memori masing-masing dan tidak saling memengaruhi.

---

### 3.3 Attributes vs Parameters dalam Inisialisasi

#### A. Definisi dan Batasan Peran

- *Attributes* adalah variabel yang menempel langsung pada *class* atau objek (ditandai dengan awalan `self.`), dan bertindak sebagai penyimpan data keadaan (*state*) dari objek tersebut.
- *Parameters* adalah variabel lokal yang didefinisikan di dalam tanda kurung metode `__init__` yang bertugas menerima pasokan nilai (*inputs*) dari luar pada saat objek dibuat.

#### B. Aturan Hubungan dan Kustomisasi Atribut

Atribut tidak harus selalu diisi langsung dari nilai parameter. Kita dapat menentukan apakah suatu atribut dapat dikustomisasi oleh pengguna saat pembuatan objek, atau dikunci dengan nilai default tertentu.

| Tipe Data | Deklarasi Sintaks | Sifat Nilai | Kustomisasi Pengguna |
|:--|:--|:--|:--|
| **Attributes** | Diawali dengan `self.` (misal: `self.balance`) | Bertahan selama objek hidup di memori (*state*). | Tergantung pada keberadaan parameter di *constructor*. |
| **Parameters** | Ditulis dalam parameter list `__init__` (misal: `balance`) | Bersifat sementara dan hancur setelah metode selesai dijalankan. | Ditentukan oleh nilai argumen yang dikirim saat instansiasi. |

#### C. Python Implementation dari Attributes dan Parameters

```python
class BankAccount:
    # owner_name dapat dikustomisasi, balance dikunci ke nilai default 0
    def __init__(self, owner_name):
        self.owner_name = owner_name  # Diisi dari parameter
        self.balance = 0              # Nilai default internal, tanpa parameter

# Instansiasi hanya mengirimkan satu argumen untuk owner_name
account_john = BankAccount("John")

print(account_john.owner_name)  # Output: John
print(account_john.balance)     # Output: 0
```

> [!warning] Audio Insight — Nama Parameter dan Attribute Tidak Wajib Sama
> Dosen menegaskan bahwa penamaan parameter di dalam tanda kurung `__init__` dan nama atribut yang diawali `self.` tidak harus sama. Sebagai contoh, kita bisa menulis `def __init__(self, A): self.owner_name = A`. Penamaan yang sama (seperti `self.owner_name = owner_name`) hanyalah sebuah kesepakatan (*convention*) yang umum digunakan oleh para pemrogram untuk mempermudah pembacaan kode.
>
> Untuk mengilustrasikan ini secara praktis, dalam latihan pembuatan *class* `BankAccount`: atribut `owner_name` dan `balance` didefinisikan di bawah referensi `self` di dalam metode `__init__` (menjadi `self.owner_name` dan `self.balance`). Jika pengguna ingin agar nilai awal `balance` dapat disesuaikan pada saat pembuatan akun, maka variabel `balance` harus dimasukkan sebagai parameter dalam `__init__` (misalnya `def __init__(self, owner_name, balance)`). Namun, jika kita ingin saldo awal rekening selalu bernilai `0` tanpa bisa diubah saat inisialisasi, kita dapat menghapus parameter `balance` dari tanda kurung `__init__` dan menetapkan `self.balance = 0` secara langsung di dalam badan metode tersebut.

**Contoh nama parameter yang sengaja berbeda dari nama attribute (ditambahkan, untuk menegaskan poin di atas):**

```python
class BankAccount:
    def __init__(self, A):          # parameter sengaja dinamai 'A', bukan 'owner_name'
        self.owner_name = A          # tapi attribute-nya tetap dinamai owner_name

acc = BankAccount("Rian")
print(acc.owner_name)   # Output: Rian
# print(acc.A)           # -> AttributeError! 'A' hanya ada sebagai parameter sementara,
                          #    bukan attribute, jadi tidak bisa diakses lewat acc.A
```

---

## Bab 4 — Penambahan Behavior melalui Method

### 4.1 Definition dan Characteristics dari Methods

#### A. Conceptual Foundation dari Methods

*Method* merupakan sebuah *function* yang didefinisikan di dalam sebuah *class* yang menggambarkan *behavior* (perilaku atau kemampuan) yang dapat dilakukan oleh sebuah *object*.

| Karakteristik | Attributes | Methods |
|:--|:--|:--|
| **Definisi** | Variabel yang menempel pada *class* untuk menyimpan data atau keadaan (*state*) dari *object*. | *Function* yang didefinisikan di dalam *class* untuk menggambarkan tindakan (*behavior*) yang dapat dilakukan oleh *object*. |
| **Sintaksis** | Dideklarasikan seperti variabel biasa (misalnya: `self.fuel = 40`). | Dideklarasikan menggunakan kata kunci `def` di dalam *class* (misalnya: `def move_forward(self)`). |
| **Penggunaan** | Digunakan untuk merepresentasikan identitas atau kondisi *object*. | Digunakan untuk memproses data, mengubah *state*, atau melakukan aksi tertentu. |

#### B. Perbedaan antara Methods dan Regular Functions

- *Regular Function* (fungsi biasa) didefinisikan secara mandiri di luar *class*. Fungsi ini bersifat global dan dapat menerima parameter berupa data apa saja secara bebas untuk diproses.
- *Method* didefinisikan secara eksklusif di dalam sebuah *class*. *Method* ini menempel pada *object* tertentu hasil instansiasi *class* tersebut dan tidak dapat dipanggil secara independen tanpa adanya *object* penerima.

> [!tip] Lihat juga
> "Regular function" di sini sama persis dengan *function* yang dibahas panjang lebar di [[Sesi 05 - Python Function and File Handling]] Bab 1. Perbedaan utamanya hanya lokasi: method hidup di dalam class dan otomatis menerima `self`, sedangkan regular function hidup bebas di modul/file.

#### C. Python Implementation dari Methods

```python
class Car:
    def __init__(self, type_name, fuel=0):
        self.type_name = type_name
        self.fuel = fuel

    def get_info(self):
        print(self.__dict__)

    def move_forward(self, distance):
        if self.fuel > 0:
            print(f"Move {distance} km")
            self.fuel -= 1
        else:
            print("No fuel!")
```

> [!warning] Audio Insight — Methods Bawaan pada Built-in Data Types
> Dosen menjelaskan bahwa tanpa disadari, kita sudah sangat sering menggunakan *methods* bawaan dari *built-in data types* Python.
>
> Contoh paling nyata adalah pada kelas *list*. Ketika kita memiliki *object* berupa *list* dan memanggil fungsi seperti `.pop()`, `.sort()`, `.append()`, `.extend()`, `.insert()`, `.remove()`, atau `.clear()`, fungsi-fungsi tersebut merupakan *methods* yang menempel secara eksklusif pada cetak biru kelas *list*.
>
> *Methods* ini tidak dapat digunakan secara sembarangan oleh tipe data lain yang tidak memiliki definisi *behavior* tersebut di dalam cetak birunya.

---

### 4.2 Mekanisme Pemanggilan dan Aliran Eksekusi Methods

#### A. Aliran Eksekusi Internal Python

Ketika sebuah program memanggil sebuah *method* pada suatu *object* (misalnya: `car_john.move_forward(10)`), terdapat serangkaian langkah eksekusi internal yang dijalankan oleh interpreter Python:

| Tahap | Aktivitas Eksekusi Internal |
|:--|:--|
| **Langkah 1** | Program memicu pemanggilan *method* pada instansi *object* tertentu: `car_john.move_forward(10)`. |
| **Langkah 2** | Python mencari definisi dari *method* bernama `move_forward` di dalam deklarasi *class* `Car`. |
| **Langkah 3** | Jika *method* ditemukan, Python secara otomatis melewatkan instansi *object* itu sendiri (`car_john`) sebagai argumen pertama untuk parameter `self`, diikuti dengan argumen berikutnya (`10`) untuk parameter `distance`. |
| **Langkah 4** | Di dalam blok kode *method*, referensi `self` merujuk ke variabel keadaan milik `car_john` (`self.fuel` merujuk ke `car_john.fuel`). |
| **Langkah 5** | Blok logika di dalam *method* dieksekusi. Jika `fuel > 0`, teks gerakan dicetak dan nilai `self.fuel` dikurangi. |
| **Langkah 6** | Setelah seluruh instruksi di dalam *method* selesai diproses, kendali program dikembalikan ke baris instruksi berikutnya di luar *class*. |

#### B. Python Implementation dari Method Call

```python
# Instantiation objek dengan data state awal berbeda
car_john = Car("sedan", 40)
car_emily = Car("suv")  # Default fuel = 0

# Objek car_john memanggil move_forward
car_john.move_forward(10)    # Output: Move 10 km

# Objek car_emily memanggil move_forward
car_emily.move_forward(10)   # Output: No fuel!
```

> [!warning] Audio Insight — Kelemahan Logika Fuel dan Perbaikannya
> Dosen dan mahasiswa mendiskusikan kelemahan pada logika pengurangan bahan bakar (*fuel*) di dalam materi dasar. Jika kode hanya ditulis `self.fuel -= 1` setiap kali melaju tanpa memedulikan seberapa jauh jaraknya (*distance*), maka mobil yang melaju sejauh 1 km maupun 100.000 km hanya akan mengurangi kapasitas bahan bakar sebesar 1 unit. Hal ini secara matematis tidak masuk akal (*not making sense*).
>
> Untuk menyelesaikan masalah tersebut, dalam sesi diskusi kelas diusulkan penambahan atribut tingkat konsumsi bahan bakar (*fuel_consumption*) pada objek, misalnya rasio jarak tempuh per liter (seperti 1 liter untuk 7 km pada sedan, atau 1 liter untuk 10 km pada SUV).
>
> Dengan penyesuaian logika tersebut, pengurangan bahan bakar dapat dihitung secara dinamis dan proporsional berdasarkan parameter jarak tempuh yang dimasukkan saat memanggil *method*:

```python
# Ilustrasi logika dinamis yang didiskusikan di kelas lisan
def move_forward_dynamic(self, distance):
    required_fuel = distance / self.fuel_consumption
    if self.fuel >= required_fuel:
        self.fuel -= required_fuel
        print(f"Move {distance} km successfully")
    else:
        print("No fuel!")
```

**Contoh class lengkap dengan `fuel_consumption` (ditambahkan agar bisa langsung dicoba):**

```python
class CarDynamic:
    def __init__(self, type_name, fuel=0, fuel_consumption=7):
        self.type_name = type_name
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption  # km per liter

    def move_forward_dynamic(self, distance):
        required_fuel = distance / self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
            print(f"Move {distance} km successfully")
        else:
            print("No fuel!")

sedan = CarDynamic("sedan", fuel=10, fuel_consumption=7)
sedan.move_forward_dynamic(14)   # butuh 2 liter, tersedia 10 liter
# Output: Move 14 km successfully
print(sedan.fuel)                 # Output: 8.0
```

---

## Bab 5 — Pewarisan Sifat (Basic Inheritance)

### 5.1 Definition dan Konsep Dasar dari Inheritance

#### A. Conceptual Foundation

- *Inheritance* merupakan sebuah mekanisme di mana suatu *class* baru yang lebih spesifik (*child class* atau *derived class*) dibangun berdasarkan *class* umum yang sudah ada (*parent class* atau *base class*).
- *Child class* akan mewarisi semua properti, *attributes*, dan *behaviors* (*methods*) yang didefinisikan oleh *parent class*, sehingga tidak perlu mendefinisikan ulang elemen-elemen dasar tersebut dari awal.
- Konsep ini merepresentasikan hubungan "is-a" (misalnya: *RegressionModel* "is-a" *MachineLearningModel*, atau *Sedan* "is-a" *Car*).

#### B. Alasan Penggunaan dan Reusability

- **Code Organization**: Membantu mengelola struktur kode agar lebih terorganisasi dengan memisahkan fungsi yang bersifat umum (*generic*) ke dalam *parent class*, sementara fitur yang terspesialisasi disimpan di *child class*.
- **Code Reusability**: Menghindari penulisan ulang kode yang sama (*code duplication*) secara berulang pada beberapa *classes* yang memiliki karakteristik dasar serupa.
- **Extensibility**: Mempermudah pengembangan dengan memperluas fungsionalitas (*extending functionality*) *parent class* tanpa mengganggu atau memodifikasi kode dasar yang sudah berjalan stabil.

| Parameter Perbandingan | Tanpa Inheritance | Dengan Inheritance |
|:--|:--|:--|
| **Penulisan Kode** | Setiap tipe *class* harus menuliskan seluruh *attributes* dan *methods* dasar secara berulang dari awal. | *Child class* langsung mewarisi struktur umum dari *parent class* secara otomatis. |
| **Spesialisasi Fitur** | Sulit membedakan fungsionalitas khusus karena semua logika digabung dalam satu atau beberapa berkas terpisah. | Fitur spesifik didefinisikan secara eksklusif hanya di dalam *child class* yang membutuhkannya. |
| **Kemudahan Maintenance** | Perubahan pada logika dasar mengharuskan pembaruan kode di setiap *class* secara individual. | Cukup memperbarui logika dasar di *parent class*, dan seluruh *child classes* akan terupdate. |

> [!warning] Audio Insight — Analogi Otomotif dan Batasan Kedalaman OOP untuk AI Engineering
> Dosen memberikan analogi industri otomotif untuk mempermudah pemahaman konsep *Inheritance*: daripada pengembang harus membuat *class* `Sedan`, `SUV`, dan `PickUp` secara terpisah dari awal (yang akan mengakibatkan penulisan ulang atribut roda, mesin, tangki bahan bakar, serta metode rem dan gas di setiap kelas), pendekatan terbaik adalah membuat sebuah *parent class* bernama `Car`. *Class* `Car` menetapkan seluruh atribut dan perilaku umum yang pasti dimiliki oleh semua jenis mobil. Selanjutnya, *class* `Sedan`, `SUV`, dan `PickUp` dideklarasikan sebagai *child classes* yang mewarisi (*inherit*) fungsionalitas dari kelas `Car`, lalu menambahkan fungsionalitas spesifik mereka sendiri (misalnya, *PickUp* menambahkan atribut kapasitas bak muatan).
>
> Terkait kedalaman pemahaman OOP untuk kebutuhan praktis, mahasiswa (Ibnu) menanyakan apakah kurikulum bootcamp juga akan membahas pilar OOP lanjutan seperti *Encapsulation*, *Abstraction*, atau *Polymorphism*. Dosen menjelaskan bahwa fokus utama dalam program *AI Engineering* sengaja dibatasi pada fondasi utama (seperti *Class*, *Object*, *Attributes*, *Methods*, dan *Basic Inheritance*) tanpa mendalami pilar rekayasa perangkat lunak lanjutan tersebut secara rumit. Berdasarkan pengalaman profesional dosen selama 5 tahun bekerja sebagai *AI Engineer*, pilar-pilar lanjutan seperti *Polymorphism* dan *Abstraction* sangat jarang digunakan secara intensif dalam pekerjaan sehari-hari di bidang kecerdasan buatan. Oleh karena itu, pengembang disarankan untuk memperdalam konsep dasar yang relevan terlebih dahulu daripada kebingungan dengan teori rekayasa perangkat lunak yang terlalu mendalam.

---

### 5.2 Implementasi dan Struktur Sintaksis Inheritance

#### A. Deklarasi Child Class dan Pemanggilan Constructor Parent

- Untuk mendefinisikan *child class* yang mewarisi *parent class*, nama *parent class* dituliskan di dalam tanda kurung langsung setelah penulisan nama *child class*.
- Di dalam *constructor* (`__init__`) milik *child class*, pemanggilan metode `super().__init__()` wajib dilakukan untuk menginisialisasi atribut-atribut dasar yang dikelola oleh *parent class*.

#### B. Sintaksis Dasar super()

- `super()` merujuk secara langsung ke *parent class* (kelas di atasnya).
- Pemanggilan `super().__init__()` bertindak sebagai instruksi untuk menjalankan konstruktor *parent class*, yang memungkinkan *child class* mendapatkan konfigurasi awal atribut dasar secara otomatis.

> [!tip] Cara membaca `super().__init__(...)` supaya tidak tertukar
> Bayangkan `__init__` milik child class sebagai *tambahan* di atas `__init__` milik parent, bukan pengganti. Urutannya:
> 1. Python mulai jalankan `__init__` milik child class.
> 2. Baris `super().__init__(...)` dijalankan LEBIH DULU (biasanya di baris pertama) — ini membangun fondasi attribute dari parent class.
> 3. Baris-baris SETELAH `super().__init__(...)` baru menambahkan attribute/logika KHUSUS milik child class.
>
> Kalau baris `super().__init__(...)` dihapus/lupa ditulis, attribute dari parent class (seperti `self.task`, `self.train_data`) TIDAK akan pernah ter-set pada object child — akan muncul `AttributeError` saat dipanggil nanti.

#### C. Python Implementation dari Basic Inheritance

```python
class MachineLearningModel:
    def __init__(self, task, train_data, test_data):
        self.task = task
        self.train_data = train_data
        self.test_data = test_data

    def train(self):
        pass

    def test(self):
        pass

class RegressionModel(MachineLearningModel):
    def __init__(self, train_data, test_data):
        # Memanggil dan menginisialisasi atribut dasar dari parent class
        super().__init__(task="regression",
                         train_data=train_data,
                         test_data=test_data)

        # Mendefinisikan atribut spesifik milik RegressionModel
        self.error_function = "r2"

    # Mendefinisikan method spesifik milik RegressionModel
    def multicolinearity_test(self):
        pass
```

> [!warning] Audio Insight — Urutan Pemanggilan super() dan Kepemilikan Atribut/Method
> Dosen menekankan urutan pemanggilan di dalam blok kode `RegressionModel`: parameter `train_data` dan `test_data` yang diterima oleh *constructor* `RegressionModel` langsung dioper ke atas (*parent*) menggunakan `super().__init__()` dengan argumen tambahan berupa nilai konstan `task="regression"`. Hal ini menjamin setiap kali sebuah objek `RegressionModel` dibuat, atribut `task` miliknya akan otomatis bernilai "regression" tanpa perlu diinput secara manual oleh pengguna.
>
> Setelah `super().__init__()` selesai dijalankan untuk membuat fondasi dasar dari *parent class*, barulah pengembang menambahkan atribut spesifik di bawahnya seperti `self.error_function = "r2"` (yang merujuk pada metrik evaluasi *R-Squared*).
>
> Ketika sebuah objek dideklarasikan dari *child class*, objek tersebut memegang kendali penuh atas seluruh aset milik *parent class* sekaligus aset spesifik miliknya sendiri: objek tersebut dapat memanggil atribut dan metode dari *parent class* (seperti `.task`, `.train()`, dan `.test()`), sekaligus dapat memanggil atribut dan metode spesifik miliknya sendiri (seperti `.error_function` dan `.multicolinearity_test()`).

**Contoh pembuktian `AttributeError` jika `super().__init__()` lupa dipanggil (ditambahkan):**

```python
class RegressionModelSalah(MachineLearningModel):
    def __init__(self, train_data, test_data):
        # LUPA memanggil super().__init__() !
        self.error_function = "r2"

model_salah = RegressionModelSalah(train_data="d1", test_data="d2")
print(model_salah.error_function)   # Output: r2 (ini attribute miliknya sendiri, aman)
# print(model_salah.task)            # -> AttributeError: 'RegressionModelSalah' object has no attribute 'task'
#                                        karena __init__ milik parent (MachineLearningModel) tidak pernah dijalankan
```

---

### 5.3 Perbandingan Model Spesifik dalam Machine Learning

#### A. Perluasan Fungsionalitas ke Model Klasifikasi

Selain `RegressionModel`, *parent class* `MachineLearningModel` yang sama juga dapat diwariskan ke model spesifik lain seperti `ClassificationModel`. Pendekatan ini menunjukkan bagaimana satu *parent class* dapat memiliki beberapa *child classes* yang berbeda dengan spesialisasi masing-masing, namun tetap berbagi basis fungsionalitas yang identik.

#### B. Perbedaan Spesifikasi RegressionModel dan ClassificationModel

| Karakteristik | RegressionModel | ClassificationModel |
|:--|:--|:--|
| **Parent Class** | `MachineLearningModel` | `MachineLearningModel` |
| **Task Attribute Value** | `"regression"` | `"classification"` |
| **Specific Attribute** | `error_function = "r2"` (R-Squared) | `error_function = "accuracy"` |
| **Specific Method** | `multicolinearity_test()` | `confusion_matrix()` |
| **Shared Methods (Inherited)** | `train()`, `test()` | `train()`, `test()` |

#### C. Python Implementation untuk Multiple Child Classes

```python
# Membuat objek dari RegressionModel
model_reg = RegressionModel(train_data="dataset_latih_reg", test_data="dataset_uji_reg")

# Mengakses inherited attribute dan method
print(model_reg.task)               # Output: regression
model_reg.train()

# Mengakses specific attribute dan method regression
print(model_reg.error_function)     # Output: r2
model_reg.multicolinearity_test()


# Membuat objek dari ClassificationModel (analogi implementasi)
class ClassificationModel(MachineLearningModel):
    def __init__(self, train_data, test_data):
        super().__init__(task="classification",
                         train_data=train_data,
                         test_data=test_data)
        self.error_function = "accuracy"

    def confusion_matrix(self):
        pass

model_clf = ClassificationModel(train_data="dataset_latih_clf", test_data="dataset_uji_clf")

# Mengakses inherited attribute dan method
print(model_clf.task)               # Output: classification
model_clf.train()

# Mengakses specific attribute dan method classification
print(model_clf.error_function)     # Output: accuracy
model_clf.confusion_matrix()
```

> [!warning] Audio Insight — Alasan Pembagian Attribute/Method yang Krusial
> Dosen memberikan penjelasan mengapa pembagian *attributes* dan *methods* spesifik ini sangat krusial: atribut metrik evaluasi seperti `"r2"` (R-Squared) atau metode diagnostik seperti `multicolinearity_test()` hanya relevan dan bekerja pada domain analisis regresi numerik, sehingga tidak boleh ada pada kelas klasifikasi. Sebaliknya, evaluasi menggunakan metrik akurasi (*accuracy*) dan representasi visual *confusion matrix* via metode `confusion_matrix()` hanya relevan untuk domain klasifikasi data kategorikal, sehingga tidak boleh ada pada kelas regresi. Dengan menggunakan paradigma *Inheritance*, pengembang berhasil mencegah terjadinya kesalahan struktural dan menjamin bahwa fungsionalitas yang tidak relevan tidak akan pernah bisa diakses atau dipanggil oleh objek yang salah, sekaligus tetap menjaga efisiensi penulisan kode dasar latihan (`train` dan `test`) yang seragam di memori.

> [!tip] Lihat juga
> Pola `class RegressionModel(MachineLearningModel)` di atas adalah gambaran awal dari cara kerja model *machine learning* di Pandas/Scikit-learn — akan sangat berguna saat sampai ke [[Sesi 12 - Python Data Manipulation With Pandas and Numpy]].

---

## Bab 6 — Latihan Praktis dan Pembahasan Teknis Python

### 6.1 Studi Kasus Class BankAccount

#### A. Persyaratan Fungsionalitas Class BankAccount

*Class* bernama `BankAccount` dirancang untuk merepresentasikan rekening bank secara umum dengan fungsionalitas pengelolaan saldo dasar.

| Elemen Class | Nama Elemen | Deskripsi Fungsional |
|:--|:--|:--|
| **Attributes** | `owner_name` | Menyimpan nama pemilik rekening (*data type*: *string*). |
| | `balance` | Menyimpan nilai saldo saat ini (*data type*: *numeric*). |
| **Methods** | `__init__` | *Constructor* untuk menginisialisasi nama pemilik dan saldo awal saat objek pertama kali dibangun. |
| | `deposit(amount)` | Menambahkan nilai sejumlah `amount` ke dalam atribut saldo (`balance`). |
| | `withdraw(amount)` | Mengurangi saldo sebesar `amount` jika saldo mencukupi. Jika saldo tidak cukup, proses penarikan digagalkan dan menampilkan pesan error. |

#### B. Implementasi Code Python

```python
class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")

# Skenario Pengujian Unit
if __name__ == "__main__":
    # Inisialisasi Objek Rekening John
    john_account = BankAccount("John", 1000000)
    john_account.deposit(500000)
    john_account.withdraw(300000)
    print(f"Account: {john_account.owner_name}")
    print(f"Final balance: {john_account.balance}")

    print("-" * 40)

    # Inisialisasi Objek Rekening Emily
    emily_account = BankAccount("Emily", 200000)
    emily_account.deposit(100000)
    emily_account.withdraw(500000)
    print(f"Account: {emily_account.owner_name}")
    print(f"Final balance: {emily_account.balance}")
```

> [!warning] Audio Insight — Parameter vs Attribute, State Lock, dan Hasil Pengujian
> Diskusi antara dosen dan mahasiswa (Stepen) menyoroti perbedaan mendasar antara *parameter* dan *attribute* di dalam metode *constructor* `__init__`: *Attributes* didefinisikan secara internal dengan awalan kata kunci `self.` (seperti `self.owner_name` dan `self.balance`), yang menandakan bahwa variabel tersebut menempel secara eksklusif pada objek yang bersangkutan. *Parameters* (seperti `owner_name` dan `balance` pada baris deklarasi `def __init__(self, owner_name, balance)`) hanyalah variabel penampung sementara untuk menangkap argumen nilai yang dikirimkan oleh pengguna saat instansiasi dilakukan. Untuk memudahkan penulisan, terdapat konvensi standar (*naming convention*) untuk menyamakan nama variabel *parameter* dengan nama *attribute*, meskipun secara fungsional keduanya sangat berbeda.
>
> Dosen juga memberikan simulasi skenario desain *state lock*: jika suatu nilai *attribute* ingin dikunci sebagai nilai bawaan (*default value*) yang tidak dapat disesuaikan saat pertama kali objek dibuat (misalnya, saldo awal/`balance` selalu bernilai 0), maka parameter `balance` tidak perlu dicantumkan dalam deklarasi *constructor*. Implementasinya dapat ditulis secara langsung di dalam ruang lingkup *constructor*: `self.balance = 0`.
>
> Melalui studi kasus ini, dosen kembali menegaskan definisi formal: variabel yang menempel pada kelas disebut sebagai *attribute*, sementara fungsi yang didefinisikan di dalam kelas disebut sebagai *method*.
>
> Dari sisi pengujian eksekusi: Objek pertama (`john_account`) diinisialisasi dengan saldo awal 1.000.000, ditambah setoran (`deposit`) 500.000 (menjadi 1.500.000), dan dikurangi penarikan (`withdraw`) 300.000, sehingga menghasilkan saldo akhir (*final balance*) sebesar 1.200.000. Objek kedua (`emily_account`) diinisialisasi dengan saldo awal 200.000, ditambah setoran 100.000 (menjadi 300.000), namun gagal melakukan penarikan sebesar 500.000 karena saldo tidak mencukupi. Sistem menampilkan pesan `"Insufficient balance."` dan mempertahankan saldo akhir Emily tetap sebesar 300.000. Mahasiswa lainnya (Rainer) membagikan pengalaman praktis tentang penambahan fungsi cetak (`print`) kustom di dalam logika internal `deposit` dan `withdraw` untuk mempermudah pelacakan kronologis (*state tracking*) aliran dana secara langsung dari dalam objek.

---

### 6.2 Mekanisme `if __name__ == '__main__'`

#### A. Fondasi Konseptual

- Struktur pemeriksaan `if __name__ == '__main__'` merupakan suatu konstruksi kontrol di Python untuk mendeteksi konteks pengeksekusian file *script*.
- Mekanisme ini mengevaluasi apakah file dijalankan secara langsung (*run directly*) oleh pengguna atau diimpor (*imported*) sebagai sebuah *module* ke dalam berkas Python lain.

| Kondisi Eksekusi File | Nilai Variabel `__name__` | Dampak terhadap Blok Kode Utama |
|:--|:--|:--|
| File dijalankan secara langsung (*run directly*) oleh pengguna di terminal. | `"__main__"` | Evaluasi bernilai `True`. Seluruh blok kode di bawah struktur `if` akan dieksekusi. |
| File diimpor (*imported*) sebagai *module* oleh file *script* lain. | Nama dari file *script* itu sendiri (nama modul). | Evaluasi bernilai `False`. Blok kode di bawah struktur `if` akan dilewati (*skipped*). |

#### B. Implementasi Code Python

```python
# Berkas: exercise.py

class BankAccount:
    pass

# Melakukan pengecekan nilai dari variabel internal __name__
print(f"Isi dari variabel internal __name__ adalah: {__name__}")

if __name__ == "__main__":
    print("Kode eksekusi utama berjalan di sini.")
```

> [!warning] Audio Insight — Pembuktian Nilai Variabel dan Independensi dari Nama File
> Dosen menjelaskan cara kerja di balik layar variabel internal `__name__` yang diatur secara otomatis oleh mesin *interpreter* Python.
>
> Ketika pengguna menjalankan program secara langsung dari terminal dengan mengetikkan perintah `python3 exercise.py`, variabel `__name__` akan diisi secara otomatis dengan nilai string `"__main__"`. Kondisi pengecekan menjadi terpenuhi sehingga bagian pengujian program dijalankan.
>
> Apabila kita membuat file *script* baru (misalnya `another_file.py`) dan menuliskan baris kode `import exercise`, proses impor tersebut akan memicu pemuatan isi modul. Namun, karena file `exercise.py` tidak dijalankan secara langsung, nilai variabel `__name__` di dalamnya akan otomatis berubah menjadi string `"exercise"`. Walhasil, seluruh blok kode pengujian di bawah pemeriksaan `if __name__ == '__main__'` tidak akan ikut terpanggil di file baru tersebut.
>
> Melalui teknik ini, *developer* dapat dengan aman menyatukan pendefinisian cetak biru (*blueprint*) kelas, metode, atau fungsi di dalam satu file bersama dengan skenario kode pengujian mandiri (*unit testing*) tanpa khawatir kode pengujian tersebut mengganggu proses pemuatan berkas saat dijadikan modul eksternal.
>
> Dalam diskusi kelas dengan mahasiswa (Stepen), dosen menguji coba mengganti nama berkas utama dari `main.py` menjadi `main_code.py` lalu menjalankannya langsung. Hasilnya menunjukkan bahwa variabel `__name__` pada berkas utama yang dieksekusi tetap bernilai `"__main__"`. Nilai `"__main__"` bersifat konseptual untuk menandai proses utama dan sama sekali tidak bergantung pada nama fisik file script di dalam sistem penyimpanan komputer Anda.

> [!tip] Lihat juga
> Mekanisme `if __name__ == "__main__"` ini dibahas jauh lebih dalam (termasuk *name guard* untuk melindungi modul saat diimpor) di [[Sesi 08 - Python and Modular Programming]] Bab 4 — sesi ini hanya memperkenalkan konsepnya lewat contoh `class BankAccount`.
