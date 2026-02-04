#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 1 : Membuat fungsi load/mengambil data
#====================================================

nama_file = "mahasiswa.txt"

# Membuat fungsi membaca data mahasiswa
def read_data_mahasiswa(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
            # Simpan data mahasiswa ke dictionary dengan key NIM
            data_dict[nim] = {  #Key
                "nama" : nama,          #Values
                "nilai" : int(nilai)    #Values
            }
    return data_dict

    # Memanggil fungsi read_data_mahasiswa
    # open_data = read_data_mahasiswa(nama_file)
    # print (open_data) #Menampilkan semua data dari mahasiswa.txt
    # print("Jumlah data terbaca", len(open_data)) #Menampilkan jumlah data dari mahasiswa.txt

#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 2 : Membuat fungsi menampilkan data
#====================================================

def show_data(data_dict):
    if len(data_dict) == 0:
        print("Data Kosong")
        return
    
    # Membuat Header Tabel
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM': <10} | {'Nama' : <12} | {'Nilai': >5}")
    print("-" * 32) #Menampilkan garis untuk header sebanyak 32 strip
    
    '''
    Untuk Tampilan yang rapi, atur f-string formating
        {'NIM': <10} artinya:
        tampikan nim <= rata kiri dengan lebar 10 karakter
        {'Nama': <12}
        tampilkan nama rata kiri, dengan lebar kolom 12 karakter
        {'Nilai':>5}
        tampilkan nilai >= rata kanan, lebar kolom 5 karakter   
    '''


    for nim in sorted(data_dict.keys()):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {nilai: >5}")

    # # Memanggil fungsi show_data
    # show_data(open_data)

#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 3 : Membuat fungsi mencari data
#====================================================

def search_data(data_dict):
    # Mencari data mahasiswa berdasarkan NIM
    nim_cari = input("Masukan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n==== Data Mahasiswa Ditemukan ====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")

    else:
        print("\nData tidak ditemukan")

    # # Menjalankan function search data
    # search_data(open_data)

#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 4 : Membuat fungsi update "nilai"
#====================================================

def update_nilai(data_dict):

    # Cari nim mahasiswa yang akan diupdate nilainya
    nim = input("Masukan NIM mahasiswa yang akan diupdate nilainya ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. update dibatalkan")
    else:
        nilai_lama = data_dict[nim]["nilai"]
        # Memasukan nilai update baru ke dictionary
        data_dict[nim]["nilai"] = nilai_baru

        print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

    # # Menjalankan function update_nilai
    # update_nilai(open_data)

#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 5 : Membuat fungsi menyimpan perubahan data ke file
#====================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai}\n")

    # simpan_data(nama_file, open_data)
    # print("Data berhasil disimpan")

#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 6 : Membuat Menu Program
#====================================================

def main():
    # Menjalankan 
    open_data = read_data_mahasiswa(nama_file)
    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan NIM")
        print("3. Update nilai mahasiswa")
        print("4. Simpan daya ke file")
        print("0. Keluar")

        pilihan = input("Piliha menu: ").strip()

        if pilihan == "1":
            show_data(open_data)
        elif pilihan == "2":
            search_data(open_data) 
        elif pilihan == "3":
            update_nilai(open_data) 
        elif pilihan == "4":
            simpan_data(nama_file, open_data)
            print("Data berhasil disimpan") 
        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()