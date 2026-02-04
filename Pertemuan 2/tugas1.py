#====================================================
#  Tugas 1 
# Pembuatan program pengelolaan data barang
#====================================================

# Membuat variabel untuk nama file agar tidak menulis nama file berulang-ulang
nama_file = "data_barang.txt"

#====================================================
#  Inisialisasi pembuatan fungsi read_data_barang
#  Fungsi ini digunakan untuk mengambil data barang yang berada di file data_barang.txt
#====================================================
def read_data_barang(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        # Mengambil atau membuka data barang per baris
        for baris in file:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
            # Menyimpan data barang ke dictionary dengan key kode
            data_dict[kode] = {  #Key
                "nama" : nama,          #Values
                "stok" : int(stok)    #Values
            }
    return data_dict

#====================================================
#  Inisialisasi pembuatan fungsi show_data
#  Fungsi ini digunakan untuk menampilkan data barang yang berada di file data_barang.txt
#====================================================
def show_data(data_dict):
    # Error handler untuk jika data kosong akan mengembalikan nilai "Data Kosong"
    if len(data_dict) == 0:
        print("Data Kosong")
        return
    
    # Membuat Struktur Header Tabel
    print("\n============= Daftar Barang =============")
    print(f"{'Kode Barang': <10} | {'Nama Barang' : <15} | {'Stok': >5}")
    print("-" * 40) #Menampilkan garis untuk header sebanyak 40 strip
    
    '''
    Untuk Tampilan yang rapi, atur f-string formating
        {'Kode Barang': <10} artinya:
        tampikan kode barang <= rata kiri dengan lebar 10 karakter
        {'Nama Barang': <15}
        tampilkan nama rata kiri, dengan lebar kolom 15 karakter
        {'Stok':>5}
        tampilkan stok >= rata kanan, lebar kolom 5 karakter   
    '''
    # Menampilkan data barang dengan metode perulangan yaitu per baris
    for kode in sorted(data_dict.keys()):
        nama=data_dict[kode]["nama"]
        stok=data_dict[kode]["stok"]
        print(f"{kode: <10} | {nama: <15} | {stok: >5}")

#====================================================
#  Inisialisasi pembuatan fungsi search_data
#  Fungsi ini digunakan untuk mencari data barang berdasarkan kode barang
#====================================================
def search_data(data_dict):
    # Mencari data barang berdasarkan kode barang
    kode_cari = input("Masukan kode barang yang ingin dicari: ").strip()

    # Menyatakan kondisi apabila data barang di temukan dan tidak
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
#  Inisialisasi pembuatan fungsi update_stok
#  Fungsi ini digunakan untuk mengubah data stok 
#====================================================
def update_stok(data_dict):
    # Cari kode barang yang akan diupdate nilainya
    kode = input("Masukan kode barang mahasiswa yang akan diupdate stoknya ").strip()

    # Menyatakan kondisi apabila kode barang yang diinput tersedia atau tidak
    if kode not in data_dict:
        print("Kode barang tidak ditemukan, update dibatalkan")
        return
    try:
        stok_baru = int(input("Masukan stok baru (0-1000): ").strip())
    except ValueError:
        print("Stok harus berupa angka. Update dibatalkan")
        return
    
    # Menyatakan kondisi apabila input yang di masukan sesuai dengan yang sudah ditentukan atau tidak
    if stok_baru < 0 or stok_baru > 1000:
        print("Stok harus antara 0 sampai 100. update dibatalkan")
    else:
        stok_lama = data_dict[kode]["stok"]
        # Memasukan stok update baru ke dictionary
        data_dict[kode]["stok"] = stok_baru

        print(f"Update Berhasil. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}")

#====================================================
#  Inisialisasi pembuatan fungsi insert_data
#  Fungsi ini digunakan untuk menambah data baru ke dalam file .txt
#====================================================
def insert_data(data_dict):
    # Input untuk kode barang
    kode = input("Masukan kode barang baru: ").strip()
    # Cek apakah kode barang sudah digunakan atau belum
    if kode in data_dict:
        print("Kode barang sudah tersedia, tambah data dibatalkan")
        return
    # JIka kondisi di atas terpenuhi dapat mengisi nama barang
    nama = input("Masukan nama barang: ").strip()
    # Mengecek apakah stok yang dimasukan berupa angka atau tidak
    try:
        stok = int(input("Masukan stok barang (0-1000): ").strip())
    except ValueError:
        print("Stok harus berupa angka. Tambah data dibatalkan")
        return

    # Apakah range stok berada di dalam angka yang sudah ditentukan
    if stok < 0 or stok > 1000:
        print("Stok harus antara 0 sampai 1000. Tambah data dibatalkan")
        return
    # Menambahkan data ke dictionary
    data_dict[kode] = {
        "nama": nama,
        "stok": stok
    }

    print(f"Data barang {kode} berhasil ditambahkan")

#====================================================
#  Inisialisasi pembuatan fungsi save_data
#  Fungsi ini digunakan untuk menyimpan data yang sudah diubah sebelumnya ke dalam file .txt
#====================================================
def save_data(nama_file, data_dict):
    # Membuka file txt dalam mode w atau write yaitu menulis ulang
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["nama"]
            stok = data_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

#====================================================
#  Inisialisasi pembuatan fungsi maini
#  Fungsi ini digunakan untuk menampilkan menu utama untuk tampilan awal pada saat program dimulai
#====================================================
def main():
    # Menjalankan 
    open_data = read_data_barang(nama_file)
    while True:
        print("\n=== MENU DATA BARANG ===")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan kode barang")
        print("3. Tambah data barang")
        print("4. Update stok barang")
        print("5. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Piliha menu: ").strip()

        if pilihan == "1":
            show_data(open_data)
        elif pilihan == "2":
            search_data(open_data) 
        elif pilihan == "3":
            insert_data(open_data) 
        elif pilihan == "4":
            update_stok(open_data) 
        elif pilihan == "5":
            save_data(nama_file, open_data)
            print("Data berhasil disimpan") 
        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()