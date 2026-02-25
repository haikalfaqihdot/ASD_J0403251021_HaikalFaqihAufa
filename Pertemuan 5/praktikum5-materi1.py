#====================================================
# PRAKTIK PERTEMUAN KE-5
# Topik: Materi 1 "Fungsi Rekursif"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#====================================================
#  Materi Rekursif : Faktorial
#  Recursive case => 3! = 3 x 2 x 1
#   Base case => 0! berhenti
#====================================================

def faktorial(n):
    # base case
    if n == 0:
        return 1
    
    # rekursif case
    return n * faktorial(n-1) 

print("========= Program Rekursif Faktorial =========")
print("Hasil faktorial 3! = ",faktorial(3))