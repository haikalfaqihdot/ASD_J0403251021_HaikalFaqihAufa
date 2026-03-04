#====================================================
# PRAKTIK PERTEMUAN KE-6
# Topik: Materi 1 " Insertion Sort"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Insertion Sort (Ascending)
# ==========================================================

def insertion_sort(data):
    # Loop mulai dari data ke-2 (index array ke-1)
    for i in range(1, len(data)):
        
        key = data[i] # Simpan nilai yang disisipkan
        j = i - 1    # Index elemen terakhir di bagian kiri
        
        # Geser elemen ke kanan sampai menemukan posisi yang tepat untuk key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j] # Geser elemen ke kanan jika lebih besar dari key
            j -= 1
        
        # sisipkan key ke posisi yang benar
        data[j + 1] = key # Masukkan key ke posisi yang benar
    return data   
    
angka =[7,8,5,2,4,6]
print("Hasil Sorting", insertion_sort(angka))