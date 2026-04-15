#====================================================
# PRAKTIK PERTEMUAN KE-9
# Topik: Materi 1 " Binary Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 2 Membuat Node Tree 
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child Kiri atau Referensi ke anak kiri
        self.right = None # Child Kanan atau Referensi ke anak kanan
        
# Membuat root
root = Node("A") # Membuat node root dengan data A
    
# Membuat child level 1
root.left = Node("B") # Menambahkan child kiri dengan data B
root.right = Node("C") # Menambahkan child kanan dengan data C

# Membuat child level 2
root.left.left = Node("D") # Menambahkan child kiri dengan data D
root.left.right = Node("E") # Menambahkan child kanan dengan data E

# Membuat child level 2 untuk C
root.right.left = Node("F") # Menambahkan child kiri dengan data F
root.right.right = Node("G") # Menambahkan child kanan dengan data G

# Menampilkan isi node
print("Data pada root: ", root.data)
print("Data kiri pada root: ", root.left.data)
print("Data kanan pada root: ", root.right.data)
print("Child kiri dari B: ", root.left.left.data)
print("Child kanan dari B: ", root.left.right.data)
print("Child kiri dari C: ", root.right.left.data)
print("Child kanan dari C: ", root.right.right.data)

# Pembahasan: 
'''
Pembahasan: 
Setelah saya pahami dari kode diatas kode tersebut membuat struktur binary tree sederhana dengan class Node, lalu membangun tree hingga 2 level, yaitu root "A" dengan anak "B" dan "C", serta "B" memiliki anak "D" dan "E", lalu juga "C" memiliki anak "F" dan "G" . Abis itu, program menampilkan data dari setiap node untuk menunjukkan hubungan antar node dalam tree.
'''
