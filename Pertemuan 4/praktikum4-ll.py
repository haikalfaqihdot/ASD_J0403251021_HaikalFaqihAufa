#====================================================
# PRAKTIK PERTEMUAN KE-4 
# Topik: LINKED LIST	
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#===============================================================
# IMLEMENTASI DASAR: Node Pada Linked List
#===============================================================

# Membuat class Node (Merupakan bagian dasar dari linked list)
class Node:
    def __init__(self,data):
        self.data = data # Menyimpan nilai / data
        self.next = None # Pointer ke note berikutnya
        
# 1) Membuat node satu per-satu        
nodeA = Node("A") 
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal : Menampilkan data pada linked list dari head sampai akhir (None)
current = head
while current is not None:
    print(current.data) # Menampilkan data pada node saat ini
    current = current.next # Pindah ke node berikutnya
    
#========================================================
#Implementasi Dasar: Linked List + Insert Awal
#========================================================

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_awal(self,data):
        # 1) Membuat node baru
        nodeBaru = Node(data) # Panggil class node
        
        # 2) Node baru menunjukan ke head lama
        nodeBaru.next = self.head
        
        # 3) head lama pindah ke head baru
        self.head = nodeBaru
    
    def hapus_awal(self):
        data_terhapus = self.head.data # Simpan data yang akan dihapus untuk ditampilkan
        self.head = self.head.next # Pindah head ke node berikutnya (Node pertama dihapus)
        print("Node yang dihapus adalah:", data_terhapus) # Menampilkan data yang dihapus
        
    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
print("=== Contoh Insert Awal ===")            
ll = LinkedList() #Instantiasi objek ke class LinkedList
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.hapus_awal()
ll.tampilkan()