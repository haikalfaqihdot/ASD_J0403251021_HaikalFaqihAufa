#====================================================
# PRAKTIK PERTEMUAN KE-6
# Topik: Latihan 2 " Insertion Sort"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Melengkapi Potongan Kode Program (Insertion Sort  'Descending')
# ==========================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] < key: #Jawaban nomer 1 dan 2
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
    return data #Jawaban nomer 1

nilai = [7,8,5,2,4,6]
print("Hasil Sorting ", insertion_sort(nilai)) #Output akan menjadi descending


# ==========================================================
# Jawaban Latihan 2
# ==========================================================
'''
SOAL:
1. Lengkapi kondisi agar menjadi sorting ascending.
2. Ubah agar menjadi descending.
'''

'''
JAWABAN:
1. Jawaban nomer 1 melengkapi ada dalam kode diatas
2. Untuk mengubah menjadi descending, saya mengganti operator pembanding dari ">" menjadi "<" pada bagian while.
'''