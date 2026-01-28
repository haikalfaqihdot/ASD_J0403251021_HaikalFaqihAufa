#====================================================
#  Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 1 : Membaca seluruh isi file
#====================================================

# Membuka file dengan mode read ("r")
with open("mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() # Membaca keseluruhan isi file dalam satu string
print(isi_file)

print(" ")
print("=== Hasil Read ===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("jumlah baris", isi_file.count("\n") + 1)

# Membuka file per baris
print(" ")
print("=== Membaca File per Baris ===")
jumlah_baris = 0
with open("mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() # Untuk menghilangkan baris baru
        print ("Baris ke-", jumlah_baris)
        print ("isinya", baris)

#====================================================
#  Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 2 : Parsing baris menjadi kolom data
#====================================================
print(" ")
print("=== Mengambil baris menjadi kolom data ===")
with open("mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM:", nim, "| Nama:", nama, "| Nilai:", nilai)

#====================================================
#  Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 3 : Membaca File dan Menyimpan ke List
#====================================================

data_list = [] #Untuk menampung data mahasiswa

with open("mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        # Simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim, nama, int(nilai)])

print(" ")
print(" ==== Data Mahasiswa dalam LIST ====")
print(data_list)

print(" ")
print(" ==== Jumlah Record dalam LIST ====")
print("Jumlah Record", len(data_list))

print(" ")
print(" ==== Menampilkan Data Record Tertentu ====")
print("Contoh Record pertama: ", data_list[0])
