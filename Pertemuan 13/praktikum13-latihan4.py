#====================================================
# PRAKTIK PERTEMUAN KE-13
# Topik: Materi 1 "Graph III: Spanning Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# =========================================================
# Latihan 4:  Latihan Studi Kasus Algoritma Prim Jaringan Kabel Antar Gedung Kampus
#==========================================================

# Mengimpor library heapq untuk membuat priority queue
import heapq

# Representasi weighted graph
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan gedung yang sudah dikunjungi
    visited = set([start])

    # Menyimpan edge dalam priority queue
    edges = []

    # Memasukkan semua edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil Minimum Spanning Tree
    mst = []

    # Menyimpan total biaya minimum
    total_weight = 0

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            # Menandai node sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan biaya edge ke total biaya
            total_weight += weight

            # Mengecek semua tetangga dari node v
            for neighbor, w in graph[v].items():

                if neighbor not in visited:

                    # Menambahkan edge baru ke priority queue
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total biaya minimum
    return mst, total_weight

# Menjalankan algoritma Prim mulai dari GedungA
mst, total = prim(graph, 'GedungA')

print("Minimum Spanning Tree:")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total biaya minimum
print("Total biaya minimum =", total)

'''
Jawaban Analisis:
1. Algoritma apa yang digunakan?
Algoritma yang digunakan adalah Prim Algorithm.
2. Edge mana saja yang dipilih? 
Edge yang dipilih:
- GedungA → GedungC = 2
- GedungC → GedungD = 1
- GedungD → GedungB = 3
3. Berapa total biaya minimum? 
Total biaya minimum = 6
4. Mengapa MST cocok digunakan pada kasus ini? 
Karena Minimum Spanning Tree (MST) dapat menghubungkan seluruh gedung dengan biaya pemasangan kabel paling minimum tanpa membentuk cycle, sehingga jaringan menjadi lebih efisien dan hemat biaya.
'''