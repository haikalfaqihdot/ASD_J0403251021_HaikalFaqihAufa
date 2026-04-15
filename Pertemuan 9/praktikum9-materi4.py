#====================================================
# PRAKTIK PERTEMUAN KE-9
# Topik: Materi 1 " Binary Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 4 Membuat Tranversal Inorder 
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child Kiri atau Referensi ke anak kiri
        self.right = None # Child Kanan atau Referensi ke anak kanan
        
# Fungsi Inorder : Left -> Root -> Right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end= " ")
        inorder(node.right)
        
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

# Menjalankan tranversal inorder
print("Hasil Tranversal Inorder: ")
inorder(root)

# Pembahasan: 
'''
Pembahasan: 
Setelah saya pahami dari kode diatas kode tersebut membuat struktur binary tree dan melakukan traversal inorder (Left → Root → Right) menggunakan fungsi rekursif. Program membuat tree dengan root "A", lalu menampilkan urutan node sesuai metode inorder saat fungsi inorder(root) dijalankan.
'''