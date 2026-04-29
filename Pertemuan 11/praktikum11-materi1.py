#====================================================
# PRAKTIK PERTEMUAN KE-11
# Topik: Materi 1 " Graph"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 1: Inisialisasi Graph
# ==========================================================

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C' : ['A', 'D'],
    'D': ['B', 'C']
}

for node in graph:
    print(node, '->', graph[node])