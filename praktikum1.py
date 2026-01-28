#=============================================
#  Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 1A : Membaca seluruh isi file
#=============================================

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
print("=== Membaca File per Baris ===")
jumlah_baris = 0
with open("mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        