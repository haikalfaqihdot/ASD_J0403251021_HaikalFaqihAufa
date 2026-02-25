#====================================================
# PRAKTIK PERTEMUAN KE-5
# Topik: Materi 4 "Fungsi Rekursif"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#====================================================
#  Contoh Backtracking 1: kombinasi Biner (n)
#====================================================

def biner(n, hasil=""):
    # Fungsi rekursif untuk membentuk semua kombinasi biner sepanjang n digit
    
    # Base case: jika panjang 'hasil' sudah n, cetak dan hentikan rekursi
    if len(hasil) == n:
        print(hasil)
        return
    
    # Recursive call: tambah "0" lalu lanjutkan pembentukan digit berikutnya
    biner(n, hasil + "0")
    
    # Recursive call: tambah "1" untuk kemungkinan yang lain
    biner(n, hasil + "1")
    
biner(3)