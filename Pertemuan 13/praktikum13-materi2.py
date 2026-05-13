#====================================================
# PRAKTIK PERTEMUAN KE-13
# Topik: Materi 1 "Graph III: Spanning Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# =========================================================
# Implementasi Algoritma Prims
#==========================================================

# import library heapq untuk priority queue
import heapq   # Digunakan untuk membuat struktur data heap / priority queue

# Representasi graph dengan bobot (weight)
graph = {     
    'A': {'B': 4, 'C': 2, 'D': 5},     # Node A terhubung ke B, C, dan D
    'B': {'A': 4, 'D': 3},             # Node B terhubung ke A dan D
    'C': {'A': 2, 'D': 1},             # Node C terhubung ke A dan D
    'D': {'A': 5, 'B': 3, 'C': 1}      # Node D terhubung ke A, B, dan C
}

# Fungsi untuk melakukan penelusuran graph dengan Prim's Algorithm
def prim(graph, start):      
    visited = set([start])     # Menyimpan node yang sudah dikunjungi
    
    edges = []      # Menyimpan sisi/edge dalam priority queue
    
    # Memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():         
        heapq.heappush(edges, (weight, start, neighbor))      
        
    mst = []     # Menyimpan hasil Minimum Spanning Tree
    total_weight = 0      # Menyimpan total bobot MST
    
    # Perulangan selama masih ada edge di priority queue
    while edges:          
        weight, u, v = heapq.heappop(edges)          
        # Mengambil edge dengan bobot terkecil
        
        if v not in visited:              
            visited.add(v)              
            # Menandai node tujuan sudah dikunjungi
            
            mst.append((u, v, weight))             
            # Menambahkan edge ke MST
            
            total_weight += weight              
            # Menambahkan bobot edge ke total bobot
            
            # Memeriksa semua tetangga dari node v
            for neighbor, w in graph[v].items():                  
                
                if neighbor not in visited:                     
                    heapq.heappush(edges, (w, v, neighbor))      
                    # Menambahkan edge baru ke priority queue
                    
    return mst, total_weight   
    # Mengembalikan MST dan total bobotnya

mst, total = prim(graph, 'A')  
# Menjalankan algoritma Prim mulai dari node A

print("Minimum Spanning Tree:") 

for edge in mst:     
    print(edge)  
    # Menampilkan setiap edge dalam MST
    
print("Total bobot =", total) 
# Menampilkan total bobot Minimum Spanning Tree

'''
Penjelasan Keseluruhan Program:
Program ini mengimplementasikan algoritma Prim untuk menemukan Minimum Spanning Tree (MST) dari sebuah graph berbobot.
Graph disimpan dalam bentuk dictionary, di mana setiap node memiliki dictionary tetangga dan bobot edge.
Fungsi `prim` memulai dari node awal, menambahkan edge yang terhubung ke priority queue, dan iterasi untuk membangun MST dengan memilih edge dengan bobot terkecil yang menghubungkan node yang belum dikunjungi.
Hasil akhir adalah daftar edge yang membentuk MST dan total bobot dari MST tersebut.
'''