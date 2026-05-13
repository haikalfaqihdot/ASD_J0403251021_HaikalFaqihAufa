#====================================================
# PRAKTIK PERTEMUAN KE-13
# Topik: Materi 1 "Graph III: Spanning Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# =========================================================
# Latihan 3:  Implementasi Algoritma Prim   
#==========================================================

import heapq
# Mengimpor library heapq untuk membuat priority queue

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}
# Representasi graph berbobot menggunakan dictionary

def prim(graph, start):

    visited = set([start])
    # Menyimpan node yang sudah dikunjungi

    edges = []
    # Menyimpan edge dalam priority queue

    # Memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    # Menyimpan hasil Minimum Spanning Tree

    total_weight = 0
    # Menyimpan total bobot MST

    # Perulangan selama masih ada edge di priority queue
    while edges:

        weight, u, v = heapq.heappop(edges)
        # Mengambil edge dengan bobot terkecil

        if v not in visited:

            visited.add(v)
            # Menandai node sudah dikunjungi

            mst.append((u, v, weight))
            # Menambahkan edge ke MST

            total_weight += weight
            # Menambahkan bobot edge ke total

            # Mengecek semua tetangga dari node v
            for neighbor, w in graph[v].items():

                if neighbor not in visited:

                    heapq.heappush(edges, (w, v, neighbor))
                    # Menambahkan edge baru ke priority queue

    return mst, total_weight
    # Mengembalikan hasil MST dan total bobot

mst, total = prim(graph, 'A')
# Menjalankan algoritma Prim mulai dari node A

print("Minimum Spanning Tree:")

# Menampilkan setiap edge pada MST
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total)

'''
Jawaban Analisis:
1. Node awal apa yang digunakan?
Node awal yang digunakan adalah node 'A', karena pada pemanggilan fungsi prim, 'A' diberikan sebagai argumen untuk parameter start. 
2. Edge mana yang dipilih pertama kali? 
Edge pertama yang dipilih adalah edge dengan bobot terkecil yang menghubungkan node 'A' dengan salah satu tetangganya. Dalam hal ini, edge (2, 'A', 'C') dipilih pertama kali.
3. Bagaimana Prim menentukan edge berikutnya?
Prim menentukan edge berikutnya dengan memilih edge dengan bobot terkecil dari semua edge yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi.
4. Berapa total bobot MST yang dihasilkan? 
Total bobot MST yang dihasilkan adalah 6.
5. Apa perbedaan pendekatan Prim dan Kruskal? 
Perbedaan utama antara Prim dan Kruskal adalah dalam cara mereka memilih edge untuk membangun MST. Prim dimulai dari satu node dan secara bertahap menambahkan edge yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi, sementara Kruskal memilih edge dengan bobot terkecil secara global tanpa memperhatikan apakah edge tersebut membentuk siklus.
'''