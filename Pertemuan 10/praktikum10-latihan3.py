#====================================================
# PRAKTIK PERTEMUAN KE-10
# Topik: Materi 2 " AVL Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 3: AVL Tree Insert (Rotasi Kiri pada BST Tidak Seimbang)
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child Kiri atau Referensi ke anak kiri
        self.right = None # Child Kanan atau Referensi ke anak kanan
        
# Alur fungsi preorder: Pada fungsi ini, program pertama-tama memeriksa apakah node saat ini tidak kosong. Jika tidak, data pada node saat ini ditampilkan terlebih dahulu (Root), kemudian fungsi preorder dipanggil secara rekursif pada subtree kiri (Left), dan akhirnya fungsi dipanggil pada subtree kanan (Right). Dengan cara ini, semua node dalam tree akan dikunjungi sesuai dengan urutan preorder.
# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None: # Jika node saat ini tidak kosong
        print(root.data, end=" ") # Tampilkan data pada node saat ini
        preorder(root.left) # Kunjungi subtree kiri
        preorder(root.right) # Kunjungi subtree kanan
        
# Alur fungsi tampil_struktur: Pada fungsi ini program memeriksa apakah node saat ini tidak kosong. Jika tidak, data pada node saat ini ditampilkan dengan indentasi yang sesuai untuk menunjukkan level dalam tree, kemudian fungsi tampil_struktur dipanggil secara rekursif pada subtree kiri dengan level yang ditingkatkan, dan akhirnya fungsi dipanggil pada subtree kanan dengan level yang sama. Dengan cara ini, struktur tree dapat divisualisasikan dengan jelas.
# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None: # Jika node saat ini tidak kosong
        print(" " * level + f"{posisi}: {root.data}") # Tampilkan data dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L") # Kunjungi subtree kiri dengan level yang ditingkatkan
        tampil_struktur(root.right, level + 1, "R") # Kunjungi subtree kanan dengan level yang sama
        
# Alur fungsi rotate_left: Pada fungsi ini, program menerima node x yang akan diputar ke kiri. Pertama, child kanan dari x (y) disimpan, dan subtree kiri dari y (T2) juga disimpan sementara. Kemudian, proses rotasi dilakukan dengan menjadikan x sebagai child kiri dari y, dan mengganti child kanan x dengan T2. Akhirnya, y menjadi root baru dari subtree yang diputar, dan fungsi mengembalikan y untuk memperbarui referensi pada tree utama.
# Fungsi rotasi kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right # y adalah child kanan x
    T2 = y.left # subtree kiri milik y disimpan sementara
    # Proses rotasi
    y.left = x # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2
    # y menjadi root baru
    return y

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)
