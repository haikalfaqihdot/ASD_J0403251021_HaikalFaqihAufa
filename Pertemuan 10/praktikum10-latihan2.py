#====================================================
# PRAKTIK PERTEMUAN KE-10
# Topik: Materi 1 " Binary Search Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 2: BST Insert, Preorder Traversal, dan Search
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child Kiri atau Referensi ke anak kiri
        self.right = None # Child Kanan atau Referensi ke anak kanan
        
# Alur Fungsi Insert pada BST: Pada fungsi ini program memulai dengan memeriksa apakah root kosong. Jika ya, maka node baru dibuat dengan data yang diberikan. Jika tidak, program membandingkan data dengan nilai pada node saat ini. Jika data lebih kecil, fungsi insert dipanggil secara rekursif pada subtree kiri; jika lebih besar, fungsi dipanggil pada subtree kanan. Setelah penempatan yang benar ditemukan, node baru disisipkan dan root dikembalikan untuk menjaga struktur BST tetap utuh.
def insert(root, data):
    if root is None: # Mulai dari root kosong atau awal
        return Node(data) # Jika root kosong, buat node baru dengan data
    if data < root.data: # Jika data lebih kecil dari root
        root.left = insert(root.left, data) # Sisipkan ke subtree kiri
    elif data > root.data: # Jika data lebih besar dari root
        root.right = insert(root.right, data) # Sisipkan ke subtree kanan
        
    return root

# Alur fungsi preorder: Pada fungsi ini program memeriksa apakah node saat ini kosong atau tidak. Jika tidak, data pada node saat ini ditampilkan terlebih dahulu, kemudian fungsi preorder dipanggil secara rekursif pada subtree kiri, dan akhirnya fungsi dipanggil pada subtree kanan. Dengan cara ini, semua node dalam BST akan dikunjungi dalam urutan Root → Left → Right sesuai dengan metode preorder.
# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None: # Jika node saat ini tidak kosong
        print(root.data, end=" ") # Tampilkan data pada node saat ini
        preorder(root.left) # Kunjungi subtree kiri
        preorder(root.right) # Kunjungi subtree kanan
        
# Alur fungsi tampil_struktur: Pada fungsi ini program memeriksa apakah node saat ini tidak kosong. Jika tidak, data pada node saat ini ditampilkan dengan indentasi yang sesuai untuk menunjukkan level dalam tree, kemudian fungsi tampil_struktur dipanggil secara rekursif pada subtree kiri dengan level yang ditingkatkan, dan akhirnya fungsi dipanggil pada subtree kanan dengan level yang sama. Dengan cara ini, struktur tree dapat divisualisasikan dengan jelas.
# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None: # Jika node saat ini tidak kosong
        print(" " * level + f"{posisi}: {root.data}") # Tampilkan data dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L") # Kunjungi subtree kiri dengan level yang ditingkatkan
        tampil_struktur(root.right, level + 1, "R") # Kunjungi subtree kanan dengan level yang sama
        
# -----------------------------
# Program utama
# -----------------------------
root = None # Inisialisasi root sebagai None (kosong)

# Data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list: 
    root = insert(root, data) # Memasukkan data ke dalam BST
    
print("Preorder BST:")
preorder(root) # Menampilkan data dalam urutan preorder

print("\n\nStruktur BST:")
tampil_struktur(root) # Menampilkan struktur tree untuk melihat bentuknya
