#====================================================
# PRAKTIK PERTEMUAN KE-6
# Topik: Materi 3 " Tracing Merge Sort"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Merge Sort (Ascending) dengan tracing
# ==========================================================

def merge_sort(data,depth=0):
    indent =" " * depth #indentasi berdasarkan level rekursi
    print(f"{indent}merge_sort({data})")
    
    if len(data) <= 1: 
        return data
    
    # Divide : membagi data menjadi 2 bagian
    mid = len(data) // 2 # Menentukan titik tengah
    left = data[:mid] # Slicing untuk bagian kiri
    right = data[mid:] # Slicing untuk bagian kanan
    
    print(f"{indent}divide -> left={left}, right={right}")
    
    # 8 ==> left 4 right 4
    # left 4 ==> mergesort
    # dan right 2 ==> mergesort
    
    # Recursive call
    left_sorted = merge_sort(left) # Rekursif untuk bagian kiri
    right_sorted = merge_sort(right) # Rekursif untuk bagian kanan
    
    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge -> {left_sorted} + {right_sorted} = {merged}")
    
    return merged

def merge(left, right):
    
    result = [] # List untuk menyimpan hasil penggabungan
    i = 0
    j = 0
    
    # Membadingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] < right[j]: # Jika elemen kiri lebih kecil
            result.append(left[i]) # Tambahkan ke hasil
            i += 1 # Geser indeks kiri
        else:
            result.append(right[j]) # Tambahkan elemen kanan ke hasil
            j += 1 # Geser indeks kanan
            
    # Menembahkan sisa elemen jika ada
    result.extend(left[i:]) # Tambahkan sisa elemen kiri jika ada
    result.extend(right[j:]) # Tambahkan sisa elemen kanan jika ada
    
    return result 

angka = [13,7,28,5,19,36,4]
print("Data sebelum diurutkan:", angka)
print("-"*50)
print("Data setelah diurutkan:", merge_sort(angka))