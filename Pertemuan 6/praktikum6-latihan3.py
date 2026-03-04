#====================================================
# PRAKTIK PERTEMUAN KE-6
# Topik: Latihan 3 " Insertion Sort"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Membuat Program dengan Menggunakan Algoritma Insertion Sort
# ==========================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        geser = 0

        # Tracing kode untuk melihat proses pergeseran elemen
        print(f"\nIterasi i = {i}")
        print("Key =", key)

        while j >= 0 and data[j] > key:
            print(f"  Geser {data[j]} ke kanan")
            data[j + 1] = data[j]
            j -= 1
            geser += 1

        data[j + 1] = key
        # Tracing kode untuk melihat hasil setelah key disisipkan
        print("  Masukkan key di posisi", j + 1)
        print("  List sekarang:", data)
        print("  Jumlah geser:", geser)

    return data


nilai = [5,2,4,6,1,3]
print("Hasil Sorting:", insertion_sort(nilai))

# ==========================================================
# Jawaban Latihan 3
# ==========================================================
'''
SOAL:
1. Tuliskan isi list setelah iterasi i = 1.
2. Tuliskan isi list setelah iterasi i = 3.
3. Berapa kali pergeseran terjadi pada iterasi i = 4?
'''

'''
JAWABAN:
1. Isi list setelah iterasi tersebut i = 1 sesuai kode tersebut adalah 'List: [2, 5, 4, 6, 1, 3]'
2. Isi list setelah iterasi tersebut i = 3 sesuai kode tersebut adalah 'List: [2, 4, 5, 6, 1, 3]'
3. Pergeseran terjadi sebanyak 4 kali pada iterasi i = 4.
'''