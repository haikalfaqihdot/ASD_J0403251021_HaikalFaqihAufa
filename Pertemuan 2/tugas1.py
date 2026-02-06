#====================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#====================================================
# Konstanta nama file
#====================================================
nama_file = "data_barang.txt"

#====================================================
#  Fungsi: Mambaca data dari file
#====================================================
def baca_stok(nama_file):
    stok_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        # Mengambil atau membuka data barang per baris
        for baris in file:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
            # Menyimpan data barang ke dictionary dengan key kode
            stok_dict[kode] = {  #Key
                "nama" : nama,          #Values
                "stok" : int(stok)    #Values
            }
    return stok_dict

#=================================
#  Fungsi: Menyimpan data ke file
#==================================
def simpan_stok(nama_file, stok_dict):
    # Membuka file txt dalam mode w atau write yaitu menulis ulang
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

#=================================
#  Fungsi: Menampilkan semua data
#==================================
def tampilkan_semua(stok_dict):
    # Error handler untuk jika data kosong akan mengembalikan nilai "Data Kosong"
    if len(stok_dict) == 0:
        print("Data Kosong")
        return
    
    # Membuat Struktur Header Tabel
    print("\n============= Daftar Barang =============")
    print(f"{'Kode': <10} | {'Nama' : <15} | {'Stok': >5}")
    print("-" * 40) #Menampilkan garis untuk header sebanyak 40 strip
    
    '''
    Untuk Tampilan yang rapi, atur f-string formating
        {'Kode': <10} artinya:
        tampikan kode barang <= rata kiri dengan lebar 10 karakter
        {'Nama': <15}
        tampilkan nama rata kiri, dengan lebar kolom 15 karakter
        {'Stok':>5}
        tampilkan stok >= rata kanan, lebar kolom 5 karakter   
    '''
    # Menampilkan data barang dengan metode perulangan yaitu per baris
    for kode in sorted(stok_dict.keys()):
        nama=stok_dict[kode]["nama"]
        stok=stok_dict[kode]["stok"]
        print(f"{kode: <10} | {nama: <15} | {stok: >5}")

#========================================
#  Fungsi: Cari barang berdasarkan kode
#=======================================
def cari_barang(stok_dict):
    # Mencari data barang berdasarkan kode barang
    kode_cari = input("Masukan kode barang yang ingin dicari: ").strip()

    # Menyatakan kondisi apabila data barang di temukan dan tidak
    if kode_cari in stok_dict:
        nama = stok_dict[kode_cari]["nama"]
        stok = stok_dict[kode_cari]["stok"]

        print("\n==== Data Barang Ditemukan ====")
        print(f"kode barang     : {kode_cari}")
        print(f"Nama barang     : {nama}")
        print(f"Stok            : {stok}")

    else:
        print("\nData barang tidak ditemukan")

#==============================
#  Fungsi: Tambah barang baru
#===============================
def tambah_barang(stok_dict):
    # Input untuk kode barang
    kode = input("Masukan kode barang baru: ").strip()
    # Cek apakah kode barang sudah digunakan atau belum
    if kode in stok_dict:
        print("Kode barang sudah tersedia, tambah data dibatalkan")
        return
    # JIka kondisi di atas terpenuhi dapat mengisi nama barang
    nama = input("Masukan nama barang: ").strip()
    # Mengecek apakah stok yang dimasukan berupa angka atau tidak
    try:
        stok = int(input("Masukan stok awal barang (0-1000): ").strip())
    except ValueError:
        print("Stok harus berupa angka. Tambah data dibatalkan")
        return

    # Apakah range stok berada di dalam angka yang sudah ditentukan
    if stok < 0 or stok > 1000:
        print("Stok harus antara 0 sampai 1000. Tambah data dibatalkan")
        return
    # Menambahkan data ke dictionary
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok
    }

    print(f"Data barang {kode} berhasil ditambahkan")
  
#==============================
#  Fungsi: Update stok barang
#==============================
def update_stok(stok_dict):
    # Cari kode barang yang akan diupdate nilainya
    kode = input("Masukan kode barang yang akan diupdate stoknya: ").strip()

    # Menyatakan kondisi apabila kode barang yang diinput tersedia atau tidak
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan, update dibatalkan")
        return
    
    # Menampilkan suatu pilihan tindakan yang akan di lakukan
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    
    try:
        jumlah = int(input("Masukan jumlah: ").strip())
    except ValueError:
        print("Stok harus berupa angka. Update dibatalkan")
        return
    
    if jumlah < 0:
        print("Jumlah tidak boleh negatif. Update dibatalkan")
        return

    stok_lama = stok_dict[kode]["stok"]

    if pilihan == "1":
        stok_baru = stok_lama + jumlah

    elif pilihan == "2":
        stok_baru = stok_lama - jumlah
        if stok_baru < 0:
            print("Stok tidak boleh 0 atau negatif. Update dibatalkan")
            return
    else:
        print("Pilihan tidak valid. Update dibatalkan")
        return

    # Simpan stok baru ke dalam dictionary
    stok_dict[kode]["stok"] = stok_baru
    print(f"Update berhasil. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}")
  
#====================================================
#  Program Utama
#====================================================
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(nama_file)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Piliha menu: ").strip()

        # Kondisi untuk menentukan pilihan yang di pilih user
        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang) 

        elif pilihan == "3":
            tambah_barang(stok_barang) 

        elif pilihan == "4":
            update_stok(stok_barang) 

        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan") 

        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()