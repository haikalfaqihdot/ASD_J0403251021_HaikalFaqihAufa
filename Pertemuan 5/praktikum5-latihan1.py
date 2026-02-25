#====================================================
# LATIHAN PERTEMUAN KE-5
# Topik: Latihan 5.1  "Rekursi Pangkat"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    
    # Fungsi ini menghitung a pangkat n dengan cara mengalikan a
    # secara berulang menggunakan konsep rekursi
    
    # Base case: kalau n sudah 0, hasilnya 1
    # karena bilangan apa pun pangkat 0 nilainya 1
    if n == 0:
        return 1
    
    # Recursive case: a akan dikali dengan hasil pemanggilan
    # fungsi pangkat yang pangkatnya dikurangi 1
    # proses ini terus berulang sampai n menjadi 0
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16