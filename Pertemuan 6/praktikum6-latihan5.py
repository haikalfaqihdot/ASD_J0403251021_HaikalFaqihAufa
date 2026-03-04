#====================================================
# PRAKTIK PERTEMUAN KE-6
# Topik: Latihan 5 " Merge Sort"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Melengkapi Fungsi Merge 
# ==========================================================

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right): 
        if left[i] < right[j]: #Jawaban nomer 1 untuk melengkapi agar fungsi ascending
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

nilai = [13,7,28,5,19,36,4]
print("Data sebelum diurutkan:", nilai)
print("Data setelah diurutkan:", merge_sort(nilai))


# ==========================================================
# Jawaban Latihan 5
# ==========================================================
'''
SOAL:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend().
'''

'''
JAWABAN:
1. Kode sudah saya lengkapi pada bagian if left[i] < right[j]: untuk membuat fungsi menjadi ascending.
2. Fungsi result.extend() digunakan untuk menyimpan sisa elemen yang belum habis dibandingkan dari list left atau right ke dalam list result.
'''