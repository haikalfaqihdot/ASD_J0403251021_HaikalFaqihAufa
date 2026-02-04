#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 1 : Membuat fungsi load/mengambil data
#====================================================

nama_file = "data_barang.txt"

# Membuat fungsi membaca data barang
def read_data_barang(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
            # Simpan data barang ke dictionary dengan key NIM
            data_dict[kode] = {  #Key
                "nama" : nama,          #Values
                "stok" : int(stok)    #Values
            }
    return data_dict

#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 2 : Membuat fungsi menampilkan data
#====================================================

def show_data(data_dict):
    if len(data_dict) == 0:
        print("Data Kosong")
        return
    
    # Membuat Header Tabel
    print("\n============= Daftar Barang =============")
    print(f"{'Kode Barang': <10} | {'Nama Barang' : <15} | {'Stok': >5}")
    print("-" * 40) #Menampilkan garis untuk header sebanyak 32 strip
    
    '''
    Untuk Tampilan yang rapi, atur f-string formating
        {'Kode Barang': <10} artinya:
        tampikan nim <= rata kiri dengan lebar 10 karakter
        {'Nama Barang': <12}
        tampilkan nama rata kiri, dengan lebar kolom 12 karakter
        {'Stok':>5}
        tampilkan nilai >= rata kanan, lebar kolom 5 karakter   
    '''


    for kode in sorted(data_dict.keys()):
        nama=data_dict[kode]["nama"]
        stok=data_dict[kode]["stok"]
        print(f"{kode: <10} | {nama: <15} | {stok: >5}")

#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 3 : Membuat fungsi mencari data
#====================================================

def search_data(data_dict):
    # Mencari data mahasiswa berdasarkan NIM
    kode_cari = input("Masukan kode barang yang ingin dicari: ").strip()

    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["nama"]
        stok = data_dict[kode_cari]["stok"]

        print("\n==== Data Barang Ditemukan ====")
        print(f"kode barang     : {kode_cari}")
        print(f"Nama barang     : {nama}")
        print(f"Stok            : {stok}")

    else:
        print("\nData barang tidak ditemukan")

#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 4 : Membuat fungsi update "nilai"
#====================================================

def update_stok(data_dict):

    # Cari kode barang yang akan diupdate nilainya
    kode = input("Masukan kode barang mahasiswa yang akan diupdate stoknya ").strip()

    if kode not in data_dict:
        print("Kode barang tidak ditemukan, update dibatalkan")
        return
    try:
        stok_baru = int(input("Masukan stok baru (0-1000): ").strip())
    except ValueError:
        print("Stok harus berupa angka. Update dibatalkan")
        return
    
    if stok_baru < 0 or stok_baru > 1000:
        print("Stok harus antara 0 sampai 100. update dibatalkan")
    else:
        stok_lama = data_dict[kode]["stok"]
        # Memasukan stok update baru ke dictionary
        data_dict[kode]["stok"] = stok_baru

        print(f"Update Berhasil. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}")

    # # Menjalankan function update_nilai
    # update_nilai(open_data)

#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 5 : Membuat fungsi menyimpan perubahan data ke file
#====================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["nama"]
            stok = data_dict[kode]["stok"]
            file.write(f"{kode}, {nama}, {stok}\n")

#====================================================
#  Praktikum 2 : Konsep ADT dan File Handling (studi kasus)
# Latihan Dasar 6 : Membuat Menu Program
#====================================================

def main():
    # Menjalankan 
    open_data = read_data_barang(nama_file)
    while True:
        print("\n=== MENU DATA BARANG ===")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan kode barang")
        print("3. Update stok barang")
        print("4. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Piliha menu: ").strip()

        if pilihan == "1":
            show_data(open_data)
        elif pilihan == "2":
            search_data(open_data) 
        elif pilihan == "3":
            update_stok(open_data) 
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