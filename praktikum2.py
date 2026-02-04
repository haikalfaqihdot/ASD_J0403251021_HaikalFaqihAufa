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
open_data = read_data_mahasiswa(nama_file)
print (open_data) #Menampilkan semua data dari mahasiswa.txt
print("Jumlah data terbaca", len(open_data)) #Menampilkan jumlah data dari mahasiswa.txt

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

# Memanggil fungsi show_data
show_data(open_data)