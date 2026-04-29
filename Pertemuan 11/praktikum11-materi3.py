#====================================================
# PRAKTIK PERTEMUAN KE-11
# Topik: Materi 1 " Graph"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 3: Implementasi Graph - konsep stuck
# ==========================================================

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

def dfs(graph, node, visited):
    
    # Fungsi untuk melakukan penelusuran graph dengan DFS (Depth First Search)
    # Graph: dictionary yang menyimpan struktur dari graph
    # Node: Menyimpan node yang sedang dikunjungi atau diproses
    # Visited: Menyimpan node yang sudah dikunjungi
    
    # Tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)
    
    #Tampilkan node yang sedang dikunjungi atau diproses
    print(node, end=" ") 
    
     # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        
        # Jika tetangga belum pernah dikunjungi
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) # Lakukan penelusuran secara rekursif pada tetangga
            
            
# set Visited
visited = set()

# Menjalankan dfs dari node 'A'
dfs(graph, 'A', visited)