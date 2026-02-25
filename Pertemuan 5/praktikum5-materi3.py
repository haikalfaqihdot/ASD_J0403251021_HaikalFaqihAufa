#====================================================
# PRAKTIK PERTEMUAN KE-5
# Topik: Materi 3 "Fungsi Rekursif"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#====================================================
#  Materi Rekursif : Menjumlahkan elemen list
#====================================================

def jumlah_list(data,index=0):
    # Base case
    if index == len(data):
        return 0
    
    # Rekursif case
    return data[index] + jumlah_list(data,index+1) 

print("========= Program Rekursif Jumlah List =========")
data_list = [2,4,5]
print("Hasil penjumlahan elemen list = ",jumlah_list(data_list))
