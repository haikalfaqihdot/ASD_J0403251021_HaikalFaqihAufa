#====================================================
# PRAKTIK PERTEMUAN KE-6
# Topik: Latihan 4 " Merge Sort"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Memahami Kode Program Merge Sort
# ==========================================================

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted) #bagian merge error karena belum ada fungsi merge


# ==========================================================
# Jawaban Latihan 4
# ==========================================================
'''
SOAL:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?
'''

'''
JAWABAN:
1.Base case pada kode diatas adalah if len(data) <= 1: jadi apabila data yang akan diurutkan hanya memiliki 1 elemen atau tidak ada elemen sama sekali, maka data tersebut sudah dianggap terurut dan tidak perlu dilanjut.
2. Karena pada Merge Sort menggunakan konsep rekursif dan divide dan conquer, data dibagi menjadi dua, masing-masing diurutkan, dan proses tersebut berulang sampai 1 elemen.
3. Tujuan menggunakan fungsi merge() yaitu untuk menggabungkan dua list yang sudah terurut.
'''