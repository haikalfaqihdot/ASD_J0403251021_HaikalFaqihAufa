#====================================================
# PRAKTIK PERTEMUAN KE-13
# Topik: Materi 1 "Graph III: Spanning Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# =========================================================
# Latihan 5:  Latihan Studi Kasus Algoritma Kruskal Jaringan Jalan Antar Kota 
#==========================================================

# Daftar edge: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
# Menyimpan hasil Minimum Spanning Tree

total_weight = 0
# Menyimpan total bobot MST

connected = set()
# Menyimpan node/kota yang sudah terhubung

# Perulangan untuk setiap edge
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        # Menambahkan edge ke MST

        total_weight += weight
        # Menambahkan bobot edge ke total bobot

        connected.add(u)
        connected.add(v)
        # Menandai kota sudah terhubung

print("Minimum Spanning Tree:")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot minimum
print("Total bobot minimum =", total_weight)

'''
Pertanyaan Analisis:
1. Kasus apa yang dipilih?
Kasus yang dipilih adalah jaringan jalan antar kota.
2. Algoritma apa yang digunakan? 
Algoritma yang digunakan adalah Kruskal Algorithm.
3. Edge mana saja yang dipilih dalam MST? 
Edge yang dipilih:
- Bogor → Depok = 2
- Depok → Jakarta = 3
- Depok → Bandung = 4
4. Berapa total bobot MST? 
Total bobot MST = 9
5. Mengapa edge tertentu tidak dipilih? 
Karena edge tersebut memiliki bobot lebih besar dan dapat membentuk cycle, sehingga tidak diperlukan dalam Minimum Spanning Tree.
'''