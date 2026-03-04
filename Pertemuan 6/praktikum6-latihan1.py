#====================================================
# PRAKTIK PERTEMUAN KE-6
# Topik: Latihan 1 " Insertion Sort"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Memahami Kode Program (Insertion Sort)
# ==========================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
    return data

nilai = [7,8,5,2,4,6]
print("Hasil Sorting", insertion_sort(nilai))


# ==========================================================
# Jawaban Latihan 1
# ==========================================================
'''
SOAL:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?
'''

'''
JAWABAN:
1. Pada indeks 0 pada insertion sort, tidak ada elemen yang dibandingkan karena itu adalah elemen pertama dan sudah dianggap bagian terurut. Perulangan dimulai dari indeks 1 karena pada saat tersebut indeks satu akan dibandingkan dengan indeks 0 untuk menentukan apakah perlu disisipkan atau tidak. Jadi, indeks 0 dianggap sebagai bagian terurut awal, dan perbandingan dimulai dari indeks 1 ke atas. 
2. Variabel key berfungsi sebagai tempat penyimpanan sementara untuk nilai yang disisipkan ke dalam bagian terurut. dengan contoh: saya mengambil satu angka, lalu menyimpan di variabel key, lalu geser angka-angka yang lebih besar dari key ke kanan, dan akhirnya sisipkan key ke posisi yang benar. 
3. Saya menggunakan while daripada for karena untuk perulangan for harus diketahui jumlah iterasi sebelumnya, sedangkan pada insertion sort saya tidak tahu berapa banyak elemen yang perlu digeser ke kanan untuk menemukan posisi. Dengan menggunakan while, saya bisa terus menggeser elemen ke kanan sampai kita menemukan posisi yang benar untuk key, tanpa harus menentukan jumlah iterasi sebelumnya.
4. Pada dalam while ada operasi yang terjadi yaitu membandingkan elemen pada indeks j dengan key, jika elemen pada indeks j lebih besar dari key, maka elemen tersebut akan digeser ke kanan dengan kode ini:(data[j + 1] = data[j]) dan indeks j akan berkurang (j -= 1) untuk melanjutkan perbandingan dengan elemen sebelumnya.
'''