Nama : Ovi 
NPM :  2506617582
Kelas : PBP C


### Tugas 1

1. Struktur HTML5 & Penggunaan Elemen SemantikDalam membangun portofolio ini, saya memanfaatkan elemen semantik seperti <header>, <nav>, <main>, <section>, dan <footer>. Elemen <article> dan <aside> sengaja tidak saya gunakan karena seluruh isi halaman berfokus pada satu alur profil pribadi, bukan kumpulan artikel lepas atau kolom samping (sidebar).Penggunaan elemen semantik ini sangat membantu saya dalam:Merapikan Struktur Halaman: Mengelompokkan area dengan jelas memakai <section class="hero" id="profile">, <section class="page-section" id="experience">, dan <section class="page-section" id="education">.Mempermudah Navigasi: ID di tiap <section> memutar peran penting agar menu di <nav> (seperti #profile, #experience, dan #education) bisa langsung mengarah ke bagian yang pas saat diklik.Kerapian Data Profil: Saya memakai Semantic Description List (<dl>, <dt>, <dd>) untuk menampilkan NPM (2506617582) dan Program Studi (S1 Sistem Informasi) karena elemen ini paling pas untuk menyajikan pasangan data label-nilai.

2. Tantangan CSS Responsif & Penyesuaian Tampilan MobileBagian paling menantang saat mengatur responsivitas adalah komponen .hero-grid. Pada layar desktop, saya membuat layout dua kolom pakai CSS Grid (grid-template-areas: "identity photo" "details photo") dengan posisi foto di sebelah kanan. Namun saat dibuka di HP, layout dua kolom ini bikin tampilan sangat sempit dan berantakan.Langkah penyesuaian yang saya lakukan untuk layar mobile 600 :Ubah Layout Jadi 1 Kolom: Di @media (max-width: 600px), tata letak diubah seratus persen menjadi satu kolom lurus ke bawah ("identity" "photo" "details"). Nama dan identitas dipasang paling atas supaya pengunjung langsung tahu ini web siapa, baru diikuti foto dan detail lainnya.Kecilkan Ukuran Foto: Foto profil (.hero-photo) saya batasi maksimal lebarnya 220px agar tidak menghabiskan ruang layar ponsel.Font Teks Fleksibel: Pada elemen <h1>, saya memakai clamp(3rem, 7vw, 5rem) supaya ukuran judul bisa mengecil otomatis mengikuti lebar layar tanpa bikin halaman bergeser ke kanan (horizontal scroll).

3. Batasan Static Web & Rencana Pengembangan SelanjutnyaKarena web ini masih static murni, ada beberapa keterbatasan yang cukup terasa:Konten Masih Kaku (Hardcoded): Setiap kali ada pembaruan riwayat organisasi (seperti BEM Fasilkom atau OSIS SMA N 2 Sumbar) atau data pendidikan, saya harus mengubah file HTML secara manual.Interaksi Terbatas: Tombol kontak seperti email (mailto:nzakyahovi@gmail.com) dan sosmed (GitHub nzakyahovi, LinkedIn) masih lempar ke aplikasi luar, belum ada fitur kirim pesan langsung di web.Rencana fungsionalitas yang ingin saya tambahkan di iterasi berikutnya:Integrasi GitHub API: Mengambil data repositori dan proyek terbaru dari akun GitHub saya (nzakyahovi) secara otomatis.Form Kontak Interaktif: Memakai layanan serverless (seperti Formspree atau EmailJS) supaya pengunjung bisa ngirim pesan langsung dari form tanpa buka aplikasi email.Pemisahan Data JSON: Memindahkan isi riwayat pengalaman dan pendidikan ke file .json, lalu di-render dinamis pakai JavaScript.

Dalam pengerjaan tugas ini, saya menggunakan bantuan alat AI (ChatGPT & Gemini) untuk membantu proses eksplorasi kodingan.

1.AI membantu saya dalam memberikan variasi background bintang berkelip.

2. membantu menemukan bug pada </nav> yang terpasang lebih awal dibagian porofil sehingga memberikan warna yang tidak sesuai(seperti tautan) ketika dilihat pada localhost

3.membantu menemukan kodingan redundan dan mengoptimalkannya

