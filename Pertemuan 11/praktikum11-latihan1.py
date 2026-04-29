#====================================================
# PRAKTIK PERTEMUAN KE-11
# Topik: Latihan 1 " Graph"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 1: Studi Kasus BFS (Jalur Terdekat Lokasi)
# ==========================================================

# Struktur data untuk membuat antrian, kita gunakan dari library collections bawaan Python
from collections import deque

# Representasi graph
graph = { 
         'Rumah': ['Sekolah', 'Toko'],
         'Sekolah': ['Perpustakaan'], 
         'Toko': ['Pasar'], 
         'Perpustakaan': [],
         'Pasar': [] 
         } 

# Fungsi untuk melakukan penelusuran graph dengan BFS (Brute Force Search)
def bfs(graph, start):
    visited = set() # Variabel yang digunakan untuk menyimpan node yang sudah diproses atau sudah dikunjungi
    queue = deque([start]) # Queue digunakan untuk menyimpan node yang akan diproses atau dibaca, dimulai dengan node awal
    
    visited.add(start) # Menandai node awal sebagai sudah dikunjungi
    
    # Selama masih ada node yang akan diproses dalam queue
    while queue:
        node = queue.popleft() # Mengambil node paling depan dari queue
        print(node, end=" ") # Tampilkan node yang sedang dikunjungi atau diproses
        
        # Periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            if neighbor not in visited: # Jika tetangga belum dikunjungi, tambahkan ke queue dan tandai sebagai sudah dikunjungi
                visited.add(neighbor) # Menandai tetangga sebagai sudah dikunjungi
                queue.append(neighbor) # Menambahkan tetangga ke dalam queue untuk diproses

print("BFS dari Rumah:")
bfs(graph, 'Rumah')


'''
Pertanyaan Analisis:
1. Node mana yang dikunjungi pertama?  
Karena BFS menggunakan konsep queue, node yang dikunjungi pertama adalah node 'Rumah', karena itu adalah node awal yang dimasukkan ke dalam queue.  
2. Mengapa BFS cocok untuk mencari jalur terdekat? 
BFS menggunakan level untuk memproses atau menelusuri graph, dengan itu ia akan mengunjungi node yang berjarak satu langkah terlebih dahulu sebelum melanjutkan ke node yang lebih jauh. Oleh karena itu, BFS akan menemukan jalur terdekat dari node awal ke node tujuan, karena ia akan menelusuri semua kemungkinan jalur pada level yang sama sebelum melanjutkan ke level berikutnya.
3. Apa perbedaan urutan BFS jika struktur graph diubah?
Jika urutan BFS berubah, akan menyebabkan hubungan jalur atau edge juga ikut berubah, sehingga urutan node yang dikunjungi juga akan berbeda dan Urutan tetangga yang ada pada struktur graph awala juga harus diubah, karena BFS akan mengikuti urutan tersebut saat menelusuri graph.
'''
