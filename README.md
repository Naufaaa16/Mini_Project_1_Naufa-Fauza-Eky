# Mini_Project_1_Naufa-Fauza-Eky

Nama: naufa fauza eky
nim: 2609116060
kelas: B
SISTEM PENILAIAN TINGKAT KEBUGARAN JASMANI
1. Inisialisasi data & variabel
   membuat batas skor untuk membatasi skor minimal dan skor maksimal yang valid,
   Nama_Peserta, Skor_Push_Up, Skor_Sit_Up, Skor_Lari bertipe list kosong agar bisa menyimpan data peserta
2. Perulangan
   menggunakan while True agar program terus berjalan menampilkan menu, menerima input no menu dari pengguna untuk menentukan
   proses selanjutnya
3. Menu 1: Tambah data
   setiap input skor, ditambah while true untuk memastikan skor yang dimasukkan dari rentang 0, 100 jika lebih atau
   kurang dari rentang maka program akan meminta input ulang. Menggunakan append untuk menambahkan data nama dan masing      masing    skor ke dalam list
4. Menu 2: Hapus data
   len(Nama_Peserta) == 0 digunakan untuk memastikan "hapus data" tidak akan berjalan jika belum ada data yang dimasukkan,
   menampilkan dan mengatur nomor urut peserta agar bisa dimulai dari 1, lalu menggunakan pop indeks agar bisa menghapus data     berdasarkan nomor urut peserta
5. Menu 3: Tampilkan data
   menghitung rata-rata skor peserta lalu hasil rata-rata dikategorikan menggunakan conditional (if, elif, elif, else)
    * rata_rata <= 59 -> "kurang"
    * rata_rata <= 75 -> "cukup"
    * rata_rata <= 85 -> "baik"
    * rata_rata > 85 -> "sangat baik
   lalu menampilkan data peserta (nama peserta, skor per jenis tes, rata-rata, kategori)
6. Menu 4: Keluar
   menggunakan break untuk menghentikan perulangan while True agar program bisa diakhiri
