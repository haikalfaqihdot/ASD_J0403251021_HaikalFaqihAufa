#====================================================
# PRAKTIK PERTEMUAN KE-9
# Topik: Materi 1 " Binary Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 1 Membuat Node
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child Kiri atau Referensi ke anak kiri
        self.right = None # Child Kanan atau Referensi ke anak kanan
        
# Membuat root
root = Node("A") # Membuat node root dengan data A
    
# Menampilkan isi node
print("Data pada root: ", root.data)
print("Data kiri pada root: ", root.left)
print("Data kanan pada root: ", root.right)

# Pembahasan: 
'''
Pembahasan: 
Setelah saya pahami dari kode diatas kode tersebut membuat struktur dasar node pada binary tree dengan class Node yang punya atribut data, left, dan right. Program kemudian membuat satu node sebagai root dengan nilai "A" dan menampilkan isinya, di mana anak kiri dan kanan masih None karena belum ada cabang.
'''
