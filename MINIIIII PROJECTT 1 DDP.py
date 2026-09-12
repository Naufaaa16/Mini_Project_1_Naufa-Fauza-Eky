Batas_skor = (0, 100)

Nama_Peserta = []
Skor_Push_Up = []
Skor_Sit_Up = []
Skor_Lari= []

print("===== SISTEM PENILAIAN TINGKAT KEBUGARAN JASMANI =====")
print("Pilih keluar untuk mengakhiri penilaian")

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama peserta: ")

        while True:
            Push_Up = int(input("Masukkan skor Push Up: "))
            if Batas_skor[0] <= Push_Up <= Batas_skor[1]:
                break
            else:
                print("nilai harus di antara 0-100")

        while True:
            Sit_Up = int(input("Masukkan nilai Sit Up: "))
            if Batas_skor[0] <= Sit_Up <= Batas_skor[1]:
                break
            else:
                print("nilai harus di antara 0-100")

        while True:
            Lari = int(input("Masukkan nilai lari: "))
            if Batas_skor[0] <= Lari <= Batas_skor[1]:
                break
            else:
                print("nilai harus di antara 0-100")

        Nama_Peserta.append(nama)
        Skor_Push_Up.append(Push_Up)
        Skor_Sit_Up.append(Sit_Up)
        Skor_Lari.append(Lari)
        print("Data berhasil ditambahkan")

    elif pilihan == "2":
        if len(Nama_Peserta) == 0:
            print("Data belum dimasukkan")
        else:
            for i in range(len(Nama_Peserta)):
                print(f"{i + 1}. {Nama_Peserta[i]}")

            nomor = int(input("Masukkan nomor peserta yang ingin dihapus: "))

            if 1 <= nomor <= len(Nama_Peserta):
                indeks = nomor - 1
            
                Nama_Peserta.pop(indeks)
                Skor_Push_Up.pop(indeks)
                Skor_Sit_Up.pop(indeks)
                Skor_Lari.pop(indeks)
                print("Data berhasil dihapus")
            else:
                print("nomor tidak valid")

    elif pilihan == "3":
        if len(Nama_Peserta) == 0:
            print("Data belum dimasukkan")
        else:
            print("\n====== DATA PESERTA =====")

            for i in range(len(Nama_Peserta)):
                rata_rata = (Skor_Push_Up[i] + Skor_Sit_Up[i] + Skor_Lari[i]) / 3

                if rata_rata <= 59:
                    kategori = "kurang"
                elif rata_rata <= 75:
                    kategori = "cukup"
                elif rata_rata <= 85:
                    kategori = "baik"
                else:
                    kategori = "sangat baik"

                print(f"\nPeserta {i + 1}")
                print(f"Nama     : {Nama_Peserta[i]}")
                print(f"Push up    : {Skor_Push_Up[i]}")
                print(f"Sit up    : {Skor_Sit_Up[i]}")
                print(f"Lari    : {Skor_Lari[i]}")
                print(f"Rata-rata    : {rata_rata:.2f}")
                print(f"Kategori   : {kategori}")

    elif pilihan == "4":
        print("program selesai")
        break