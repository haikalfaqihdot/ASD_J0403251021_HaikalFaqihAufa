#====================================================
# PRAKTIK PERTEMUAN KE-13
# Topik: Materi 1 "Graph III: Spanning Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# =========================================================
# Latihan 1:  Memahami Konsep Spanning Tree 
#==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'), # Edge antara node A dan B
    ('A', 'C'), # Edge antara node A dan C
    ('A', 'D'), # Edge antara node A dan D
    ('C', 'D'), # Edge antara node C dan D
    ('B', 'D')  # Edge antara node B dan D
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'), # Edge antara node A dan C
    ('C', 'D'), # Edge antara node C dan D
    ('D', 'B') # Edge antara node D dan B
]

print("Edge pada graph:")

# Menampilkan semua edge pada graph
for edge in edges:
    print(edge)

print("\nSpanning Tree:")

# Menampilkan edge yang membentuk spanning tree
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

'''
Pertanyanan Analisis:
1. Apa perbedaan graph awal dan spanning tree? 
Graph awal memiliki 5 edge yang menghubungkan semua node, sedangkan spanning tree hanya memiliki 3 edge yang menghubungkan semua node tanpa membentuk siklus.
2. Mengapa spanning tree tidak boleh memiliki cycle? 
Spanning tree tidak boleh memiliki cycle karena tujuan dari spanning tree adalah untuk menghubungkan semua node dengan jumlah edge yang paling sedikit. Jika ada cycle, maka ada edge yang tidak diperlukan untuk menjaga konektivitas, sehingga tidak efisien.
3. Mengapa jumlah edge spanning tree selalu lebih sedikit? 
Jumlah edge spanning tree selalu lebih sedikit karena spanning tree hanya menggunakan jumlah edge yang diperlukan untuk menghubungkan semua node tanpa membentuk siklus. Dalam sebuah graph dengan n node, spanning tree akan selalu memiliki n-1 edge, sedangkan graph awal bisa memiliki lebih banyak edge tergantung pada bagaimana node-node tersebut terhubung.
'''