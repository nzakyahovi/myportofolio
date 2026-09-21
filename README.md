Nama : Ovi 
NPM :  2506617582
Kelas : PBP C


### Tugas 1

1. Struktur HTML5 & Penggunaan Elemen SemantikDalam membangun portofolio ini, saya memanfaatkan elemen semantik seperti <header>, <nav>, <main>, <section>, dan <footer>. Elemen <article> dan <aside> sengaja tidak saya gunakan karena seluruh isi halaman berfokus pada satu alur profil pribadi, bukan kumpulan artikel lepas atau kolom samping (sidebar).Penggunaan elemen semantik ini sangat membantu saya dalam:Merapikan Struktur Halaman: Mengelompokkan area dengan jelas memakai <section class="hero" id="profile">, <section class="page-section" id="experience">, dan <section class="page-section" id="education">.Mempermudah Navigasi: ID di tiap <section> memutar peran penting agar menu di <nav> (seperti #profile, #experience, dan #education) bisa langsung mengarah ke bagian yang pas saat diklik.Kerapian Data Profil: Saya memakai Semantic Description List (<dl>, <dt>, <dd>) untuk menampilkan NPM (2506617582) dan Program Studi (S1 Sistem Informasi) karena elemen ini paling pas untuk menyajikan pasangan data label-nilai.

2. Tantangan CSS Responsif & Penyesuaian Tampilan MobileBagian paling menantang saat mengatur responsivitas adalah komponen .hero-grid. Pada layar desktop, saya membuat layout dua kolom pakai CSS Grid (grid-template-areas: "identity photo" "details photo") dengan posisi foto di sebelah kanan. Namun saat dibuka di HP, layout dua kolom ini bikin tampilan sangat sempit dan berantakan.Langkah penyesuaian yang saya lakukan untuk layar mobile 600 :Ubah Layout Jadi 1 Kolom: Di @media (max-width: 600px), tata letak diubah seratus persen menjadi satu kolom lurus ke bawah ("identity" "photo" "details"). Nama dan identitas dipasang paling atas supaya pengunjung langsung tahu ini web siapa, baru diikuti foto dan detail lainnya.Kecilkan Ukuran Foto: Foto profil (.hero-photo) saya batasi maksimal lebarnya 220px agar tidak menghabiskan ruang layar ponsel.Font Teks Fleksibel: Pada elemen <h1>, saya memakai clamp(3rem, 7vw, 5rem) supaya ukuran judul bisa mengecil otomatis mengikuti lebar layar tanpa bikin halaman bergeser ke kanan (horizontal scroll).

3. Batasan Static Web & Rencana Pengembangan SelanjutnyaKarena web ini masih static murni, ada beberapa keterbatasan yang cukup terasa:Konten Masih Kaku (Hardcoded): Setiap kali ada pembaruan riwayat organisasi (seperti BEM Fasilkom atau OSIS SMA N 2 Sumbar) atau data pendidikan, saya harus mengubah file HTML secara manual.Interaksi Terbatas: Tombol kontak seperti email (mailto:nzakyahovi@gmail.com) dan sosmed (GitHub nzakyahovi, LinkedIn) masih lempar ke aplikasi luar, belum ada fitur kirim pesan langsung di web.Rencana fungsionalitas yang ingin saya tambahkan di iterasi berikutnya:Integrasi GitHub API: Mengambil data repositori dan proyek terbaru dari akun GitHub saya (nzakyahovi) secara otomatis.Form Kontak Interaktif: Memakai layanan serverless (seperti Formspree atau EmailJS) supaya pengunjung bisa ngirim pesan langsung dari form tanpa buka aplikasi email.Pemisahan Data JSON: Memindahkan isi riwayat pengalaman dan pendidikan ke file .json, lalu di-render dinamis pakai JavaScript.

Dalam pengerjaan tugas ini, saya menggunakan bantuan alat AI (ChatGPT & Gemini) untuk membantu proses eksplorasi kodingan.

    1. AI membantu saya dalam memberikan variasi background bintang berkelip.

    2. membantu menemukan bug pada </nav> yang terpasang lebih awal dibagian porofil sehingga memberikan warna yang tidak sesuai(seperti tautan) ketika dilihat pada localhost

    3. membantu menemukan kodingan redundan dan mengoptimalkannya


### Tugas 2

1. alur pemrosesan halaman portofolio baru
    a. pengguna mengetik atau membuka link URL di browser
    b. urls.py (Proyek): Menjadi pintu masuk utama. Berkas ini membaca rute URL dan  meneruskannya ke berkas urls.py milik aplikasi menggunakan include()
    c.urls.py (Aplikasi): Mencocokkan rute spesifik yang diminta dengan fungsi view yang bertanggung jawab (misalnya views.show_education).
    d.View (views.py): Berperan sebagai pengatur logika (controller). View memanggil Model untuk meminta data yang dibutuhkan.
    e.Model (models.py): Berkomunikasi dengan database menggunakan Django ORM untuk mengambil data portofolio, lalu mengembalikannya ke View dalam bentuk QuerySet.
    f.Template (.html): View menyuntikkan data tersebut ke dalam dictionary context dan merender file template HTML. Sintaks Django (seperti {% for %}) memproses data dinamis menjadi elemen HTML utuh.
    g.Browser Response: Django mengembalikan hasil render tersebut sebagai HttpResponse ke browser untuk ditampilkan kepada pengguna.

2. . Mengapa Data Wajib Disimpan di Model (Bukan Hardcode di Template)

    a.Pemisahan Tanggung Jawab (Separation of Concerns): Template berfokus pada struktur tampilan (UI/UX), sedangkan Model berfokus pada penyimpanan dan struktur data. Campur aduk keduanya membuat kode berantakan.
    b. Kemudahan Pemeliharaan (Maintainability): Jika data di-hardcode di template, setiap ada penambahan atau perubahan karya, kamu harus membuka dan mengubah file HTML secara manual. Menggunakan Model memungkinkan pengubahan data dengan mudah via Django Admin atau Shell tanpa menyentuh kode aplikasi.
    c. Skalabilitas & Efisiensi Kode: Model memungkinkan pemrosesan data seperti pencarian, filter, dan pengurutan (sorting). Di sisi template, kamu cukup menulis satu struktur looping ({% for item in list %}), dan tampilannya akan otomatis menyesuaikan sebanyak apa pun data di database.

3.  Perbedaan makemigrations vs migrate & Contoh Kasus
    makemigrations: Memindai perubahan pada file models.py dan membuat berkas migrasi baru (berupa blueprint / instruksi perubahan) di dalam folder migrations/. Perintah ini belum mengubah struktur database.

    migrate: Mengeksekusi berkas migrasi yang sudah dibuat untuk benar-benar memperbarui struktur tabel pada database sungguhan.
    # main/models.py
    class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=50)
    # Menambahkan field baru:
    gpa = models.FloatField(null=True, blank=True) 
    Langkah yang harus dilakukan:

    Jalankan python manage.py makemigrations  untuk Django mendeteksi penambahan gpa dan membuat file instruksi (misal: 0002_education_gpa.py).
    Jalankan python manage.py migrate  untuk Django mengeksekusi file 0002 tersebut sehingga kolom gpa benar-benar dibuat di dalam tabel database.

    dalam penyelesaian tugas ini saya menggunakan gemini untuk eksplorasi dan membahas lebih dalam memahami lebih lanjut tentang pertanyaan tugas 2.

### Tugas 3

1. Mengapa Menggunakan ModelForm dan Alasan Penggunaan csrf_token

    Alasan Menggunakan ModelForm:
    - Hemat Waktu dan Ringkas (Prinsip DRY):
    Kita tidak perlu menulis tag <input> secara manual satu per satu di HTML. Django secara otomatis membuatkan elemen form berdasarkan struktur field yang sudah kita definisikan di models.py.
    - Validasi Otomatis:
    ModelForm langsung mengambil aturan validasi dari model (misalnya max_length atau field yang wajib diisi). Jadi kalau ada input yang tidak sesuai, pesan error langsung ditangani oleh Django tanpa kita harus membuat logika validasi manual dari awal.
    - Proses Simpan ke Database Lebih Praktis:
    Untuk menyimpan data ke database, kita cukup memanggil form.save(). Beda kalau menggunakan form manual, kita harus mengambil nilainya satu per satu memakai request.POST.get('nama_field') lalu dimasukkan ke instance model secara manual.

    Alasan Wajib Menambahkan {% csrf_token %}:
    - Tag {% csrf_token %} wajib ada pada form bertipe POST, PUT, atau DELETE untuk mengamankan aplikasi dari serangan CSRF (Cross-Site Request Forgery).
    - Cara kerjanya, Django akan menyisipkan token terenkripsi yang unik ke dalam form sebagai hidden input. Saat form dikirimkan, Django bakal mencocokkan token di form dengan token yang ada pada sesi pengguna. Jika token cocok, Django memastikan bahwa request tersebut memang dikirim oleh pengguna dari web kita, bukan dari situs lain yang mencoba memalsukan tindakan atas nama pengguna.


2. Keunggulan JSON Dibandingkan XML dalam Pengembangan Web Modern

    JSON lebih banyak digunakan dibanding XML dalam pengembangan web modern karena beberapa alasan:

    - Ukuran Data Lebih Ringan:
    JSON memakai struktur key-value ringkas seperti {"nama": "Ovi"}, beda dengan XML yang harus memakai tag pembuka dan penutup seperti <nama>Ovi</nama>. Hal ini membuat ukuran file JSON jauh lebih kecil dan hemat bandwidth saat dikirim lewat jaringan.
    - Dukungan Bawaan di JavaScript:
    Karena JSON merupakan bagian dari sintaksis JavaScript, browser bisa langsung memproses datanya menggunakan fungsi bawaan JSON.parse(). Sementara untuk XML, browser harus memakai XML DOM Parser yang prosesnya lebih rumit.
    - Struktur Data Sederhana:
    Bentuk JSON secara alami cocok dengan struktur data umum di berbagai bahasa pemrograman, seperti object (dictionary) dan array (list), sehingga jauh lebih gampang dibaca dan diolah.
    - Pemrosesan (Parsing) Lebih Cepat:
    Karena format teksnya sederhana dan tidak berbelit-belit, proses pembacaan data JSON baik di sisi server maupun browser bisa berjalan lebih cepat.


3. Alur View JSON dan Alasan Perlunya Serialization

    Alur Pengembalian Data Portofolio dalam Bentuk JSON:
    1. HTTP Request: Client (browser atau fungsi Fetch/AJAX) mengirim request GET ke URL endpoint JSON (misalnya /json/).
    2. URL Routing: Django mencocokkan path di urls.py lalu meneruskan request ke fungsi view yang sesuai.
    3. Query Database: Di fungsi view, Django ORM mengambil data dari database (seperti Education.objects.all()), yang menghasilkan data berupa QuerySet.
    4. Proses Serialization: Data QuerySet tersebut diubah formatnya dari objek Django/Python menjadi string berformat JSON menggunakan serializers.serialize('json', data) atau JsonResponse.
    5. HTTP Response: Fungsi view mengembalikan objek HttpResponse / JsonResponse berisi data JSON tersebut beserta header Content-Type: application/json ke client.
    6. Rendering di Client: Client menerima data JSON tersebut lalu memakai JavaScript untuk menampilkan datanya di halaman web secara dinamis.

    Mengapa Perlu Melakukan Serialization?
    - Data yang ditarik lewat ORM Django bentuknya adalah objek Python (QuerySet atau instance dari model) yang tersimpan di memori server. Objek ini tidak bisa langsung dikirim melalui protokol HTTP, karena HTTP hanya bisa mentransfer data berbentuk teks/string.
    - Lewat proses serialization, objek kompleks Python tersebut dikonversi dulu menjadi format teks terstruktur (JSON). Selain itu, karena JSON bersifat universal (language-agnostic), data dari backend Django bisa dengan mudah dibaca dan dipakai oleh teknologi apa saja di sisi frontend (JavaScript murni, React, Vue, hingga aplikasi mobile).


    dalam penyelesaian tugas ini saya menggunakan  gen Ai untuk eksplorasi dan membantu dalam mengimplementasi bagian form tanggl dan laiinya yang berbeda pada tutorial 3, serta gen ai juga membantu saya memahami lanjut apa yang baru saya pelajari di json.