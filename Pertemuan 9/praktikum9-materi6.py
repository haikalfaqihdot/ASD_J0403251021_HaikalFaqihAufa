#====================================================
# PRAKTIK PERTEMUAN KE-9
# Topik: Materi 1 " Binary Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 5 Struktur Organisasi Perusahaan Menggunakan Preorder Traversal
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child Kiri atau Referensi ke anak kiri
        self.right = None # Child Kanan atau Referensi ke anak kanan
        
# Fungsi Preorder : Root -> Left -> Right
def preorder(node):
    if node is not None:
        print(node.data, end= " ")
        preorder(node.left)
        preorder(node.right)
        
# Membuat tree struktur organisasi
root = Node("Direktur") # Membuat node root dengan data Direktur
    
# Membuat child level 1
root.left = Node("Manajer A") # Menambahkan child kiri dengan data Manajer A
root.right = Node("Manajer B") # Menambahkan child kanan dengan data Manajer B

# Membuat child level 2 untuk Manajer A
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

# Membuat child level 2 untuk Manajer B
root.right.right = Node("Staff 3")

# Menampilkan struktur organisasi
print("=" * 60)
print("Struktur Organisasi Perusahaan dengan Preorder Traversal: ")
print("=" * 60)
preorder(root)

# Pembahasan: 
'''
Pembahasan: 
Setelah saya pahami dari kode diatas kode tersebut membuat struktur tree untuk organisasi perusahaan dan menampilkan data menggunakan traversal preorder (Root → Left → Right). Struktur dimulai dari "Direktur" sebagai root, lalu memiliki "Manajer A" dan "Manajer B" beserta staff di bawahnya, kemudian ditampilkan urut sesuai metode preorder.
'''