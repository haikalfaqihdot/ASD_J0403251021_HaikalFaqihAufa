#====================================================
# PRAKTIK PERTEMUAN KE-6
# Topik: Materi 2 " Materi Insertion Sort"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Insertion Sort dengan tracing
# ==========================================================

def insertion_sort(data):
    
    # Melihat data awal
    print("Data Awal:", data)
    print("-"*50)
         
    # Loop mulai dari data ke-2 (index array ke-1)
    for i in range(1, len(data)):
        
        key = data[i] # Simpan nilai yang disisipkan
        j = i - 1    # Index elemen terakhir di bagian kiri
        
        print("Iterasi ke-", i)
        print("Nilai Key =", key)
        print("Bagian Kiri (terurut)=", data[:i])
        print("Bagian Kanan (belum terurut)=", data[i:])
        
        # Geser elemen ke kanan sampai menemukan posisi yang tepat untuk key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j] # Geser elemen ke kanan jika lebih besar dari key
            j -= 1
        
        # sisipkan key ke posisi yang benar
        data[j + 1] = key # Masukkan key ke posisi yang benar
        
        print("Setelah disisipkan:", data)
        print("-"*50)
        
    return data   
    
angka =[7,8,5,2,4,6]
print("Hasil Sorting", insertion_sort(angka))