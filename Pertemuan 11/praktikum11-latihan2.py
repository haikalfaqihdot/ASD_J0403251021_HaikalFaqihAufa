#====================================================
# PRAKTIK PERTEMUAN KE-11
# Topik: Latihan 2 " Graph"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 2: Studi Kasus DFS (Eksplorasi Jalur)
# ==========================================================

# Representasi graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Fungsi untuk melakukan penelusuran graph dengan DFS (Depth First Search)
def dfs(graph, node, visited):
    visited.add(node) # Menandai node saat ini sebagai node yang sudah dikunjungi
    print(node, end=" ") # Tampilkan node yang sedang dikunjungi atau diproses
    
    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        if neighbor not in visited: # Jika tetangga belum pernah dikunjungi
            dfs(graph, neighbor, visited) # Lakukan penelusuran secara rekursif pada tetangga

# Set untuk menyimpan node yang sudah dikunjungi
visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited) # Menjalankan dfs dari node 'A'


'''
Pertanyaan Analisis:
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
DFS menggunakan rekursi atau stack, dimana konsep awal stack adalah Last In First Out (LIFO), sehingga ketika DFS menemukan node tetangga, ia akan langsung masuk ke node tersebut sebelum memeriksa tetangga lainnya. Oleh karena itu, DFS akan terus masuk ke node terdalam terlebih dahulu sebelum kembali dan memeriksa tetangga lainnya.
2. Apa yang terjadi jika urutan neighbor diubah?  
DFS mengikuti urutan list tetangga yang ada pada struktur graph. Jika urutan neighbor diubah, maka urutan node yang dikunjungi oleh DFS juga akan berubah, karena DFS akan mengikuti urutan tersebut saat menelusuri graph dan urutan hasil DFS akan berbeda.
3. Bandingkan hasil DFS dengan BFS pada graph yang sama. 
- Pada DFS, urutan node yang dikunjungi adalah A, B, D, E, C, F. -> Masuk sedalam mungkin dulu 
- Pada BFS, urutan node yang dikunjungi adalah A, B, C, D, E, F. -> Masuk secara level
'''
