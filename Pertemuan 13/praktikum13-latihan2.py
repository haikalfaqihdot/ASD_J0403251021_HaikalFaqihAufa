#====================================================
# PRAKTIK PERTEMUAN KE-13
# Topik: Materi 1 "Graph III: Spanning Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# =========================================================
# Latihan 2:  Implementasi Algoritma Kruskal  
#==========================================================

# ========================================================== 
# Implementasi Sederhana Algoritma Kruskal 
# ========================================================== 

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []               # Menyimpan hasil Minimum Spanning Tree
total_weight = 0       # Menyimpan total bobot MST
connected = set()      # Menyimpan node yang sudah terhubung

# Melakukan perulangan pada setiap edge
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        # Menambahkan edge ke MST

        total_weight += weight
        # Menambahkan bobot edge ke total bobot

        connected.add(u)
        connected.add(v)
        # Menandai node sudah terhubung

print("Minimum Spanning Tree:")

# Menampilkan semua edge hasil MST
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total_weight)

'''
Jawaban Analisis:
1. Edge mana yang dipilih pertama kali? 
Edge dengan bobot terkecil, yaitu (1, 'C', 'D'), dipilih pertama kali karena algoritma Kruskal selalu memilih edge dengan bobot paling kecil.
2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
Karena algoritma Kruskal bekerja dengan memilih edge dengan bobot terkecil yang tidak membentuk siklus, sehingga memastikan bahwa MST yang dihasilkan memiliki bobot total yang paling minimum.
3. Berapa total bobot MST yang dihasilkan? 
Total bobot MST yang dihasilkan adalah 6, yang merupakan jumlah dari bobot edge (1, 'C', 'D'), (2, 'A', 'C'), dan (3, 'B', 'D').
4. Mengapa edge tertentu tidak dipilih? 
Karena edge tertentu tidak dipilih karena jika dipilih, edge tersebut akan membentuk siklus dalam MST. Misalnya, edge (4, 'A', 'B') tidak dipilih karena jika dipilih, akan membentuk siklus dengan edge (2, 'A', 'C') dan (3, 'B', 'D').
'''