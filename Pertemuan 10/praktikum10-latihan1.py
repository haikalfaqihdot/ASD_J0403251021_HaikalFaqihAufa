#====================================================
# PRAKTIK PERTEMUAN KE-10
# Topik: Materi 1 " Binary Search Tree"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 1: BST Insert, Inorder Traversal, dan Search
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

# Mengisi data BST
root  = None
data_list = [50, 30, 70, 20, 40, 60, 80]

for data in data_list:
    root = insert(root, data)
    
print("Data BST telah dimasukkan.")

# ==========================================================
# Latihan 2: Tranversal Inorder BST
# ==========================================================

# Alur Fungsi Inorder pada BST: Pada fungsi ini program memeriksa apakah node saat ini tidak kosong. Jika tidak, fungsi inorder dipanggil secara rekursif pada subtree kiri terlebih dahulu, kemudian data pada node saat ini ditampilkan, dan akhirnya fungsi dipanggil pada subtree kanan. Dengan cara ini, semua node dalam BST akan dikunjungi dalam urutan yang terurut (dari nilai terkecil ke terbesar) sesuai dengan sifat BST.
def inorder(node):
    if node is not None:
        inorder(node.left) # Kunjungi subtree kiri
        print(node.data, end= " ") # Tampilkan data node
        inorder(node.right) # Kunjungi subtree kanan

print("Hasil Inorder:")
inorder(root)

# ==========================================================
# Latihan 3: Search BST
# ==========================================================

# Alur Fungsi Search pada BST: Pada fungsi ini program memulai dengan memeriksa apakah root kosong. Jika ya, maka key tidak ditemukan dan fungsi mengembalikan False. Jika data pada node saat ini sama dengan key yang dicari, maka key ditemukan dan fungsi mengembalikan True. Jika key lebih kecil dari data pada node saat ini, fungsi search dipanggil secara rekursif pada subtree kiri, jika lebih besar, fungsi dipanggil pada subtree kanan. Dengan cara ini, pencarian dilakukan secara efisien sesuai dengan struktur BST.
def search(root, key):
    if root is None: # Jika root kosong, berarti key tidak ditemukan
        return False # Key tidak ditemukan
    
    if root.data == key: # Jika data pada node sama dengan key
        return True # Key ditemukan
    
    if key < root.data: # Jika key lebih kecil dari root
        return search(root.left, key) # Cari di subtree kiri
    else: # Jika key lebih besar dari root
        return search(root.right, key) # Cari di subtree kanan
    
    
# Uji pencarian
key = 400

if search(root, key): # Jika key ditemukan dalam BST
    print(f"Data {key} ditemukan dalam BST.") # Menampilkan pesan bahwa data ditemukan
else: # Jika key tidak ditemukan dalam BST
    print(f"Data {key} tidak ditemukan dalam BST.") # Menampilkan pesan bahwa data tidak ditemukan