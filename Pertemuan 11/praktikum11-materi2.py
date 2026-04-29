#====================================================
# PRAKTIK PERTEMUAN KE-11
# Topik: Materi 1 " Graph"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 2: Implementasi Graph - konsep queue
# ==========================================================

# Struktur data untuk membuat antrian, kita gunakan dari library collections bawaan Python
from collections import deque

# Representasi graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran graph dengan BFS (Brute Force Search)
    # Graph: dictionary yang menyimpan stryktur dari graph
    # Start: Node awal penelusuran
    
    # Queue digunakan untuk menyimpan node yang akan diproses atau dibaca
    queue = deque()
    
    # Variabel yang digunakan untuk menyimpan node yang sudah diproses atau sudah dikunjungi
    visited = set() 
    
    # Masukan node awala ke queue untuk memulai penelusuran
    queue.append(start) # Memulai penelusuran dengan menambahkan node awal ke dalam queue
    
    # Tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start) # Menandai node awal sebagai sudah dikunjungi
    
    while queue: # Selama masih ada node yang akan diproses dalam queue
        
        # Mengambil node paling depan dari queue
        node = queue.popleft() 
        
        # Tampilkan node yang sedang dikunjungi atau diproses
        print(node, end=" ")
        
        # Periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]: 
            # Jika tetangga belum dikunjungi, tambahkan ke queue dan tandai sebagai sudah dikunjungi
            if neighbor not in visited:
                # Menandai tetangga sebagai sudah dikunjungi 
                visited.add(neighbor) 
                # Menambahkan tetangga ke dalam queue untuk diproses
                queue.append(neighbor) 
                
# Menjalankan BFS dari node 'A'
bfs(graph, 'A')