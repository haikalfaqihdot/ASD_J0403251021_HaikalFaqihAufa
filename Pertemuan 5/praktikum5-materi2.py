#====================================================
# PRAKTIK PERTEMUAN KE-5
# Topik: Materi 2 "Fungsi Rekursif"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#====================================================
#  Materi Rekursif : Call Stack
#  Tracing bilangan (masuk-keluar)
#  Input => 3
#  Masuk 1 - 2 - 3
#  Keluar 3 - 2 - 1
#====================================================

def hitung(n):
    
    # base case
    if n == 0:
        print("selesai")
        return
    
    print("Masuk: ",n)
    hitung(n-1) # rekursif case
    print("Keluar: ",n)
    
print("========= Program Rekursif Call Stack =========")    
