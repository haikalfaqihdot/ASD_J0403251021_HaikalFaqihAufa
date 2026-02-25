#====================================================
# PRAKTIK PERTEMUAN KE-4 
# Topik: STACK	
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#===============================================================
# IMLEMENTASI DASAR: Node Pada Stack
#===============================================================

# Membuat class Node (Merupakan bagian dasar dari linked list)
class Node: # Class implementasi Stack
    def __init__(self,data):
        self.data = data # Menyimpan nilai / data
        self.next = None # Pointer ke node berikutnya
        
#Stack dengan 1 pointer : top
class StackLL:
    def __init__(self):
        self.top = None # Pointer ke elemen paling atas (top)
        
    def is_empty(self):
        return self.top is None # Stack kosong jika top tidak menunjuk ke node manapun (None)
        
    def enqueue(self,data):
        # Menambah data ke atas (top)
        nodeBaru = Node(data) # Membuat node baru
        
        #Jika stack kosong, top menunjuk ke node baru
        if self.is_empty(): 
            self.top = nodeBaru
            return
        
        #Jika stack tidak kosong:
        #Node baru menunjuk ke top lama
        nodeBaru.next = self.top 
        #Top pindah ke node baru
        self.top = nodeBaru 
        
    def dequeue(self):
        # Menghapus data dari atas (top)
        # 1) Lihat data yang paling atas (top) 
        data_terhapus = self.top.data 
        
        # 2) geser top ke node berikutnya
        self.top = self.top.next 
        
        return data_terhapus # Mengembalikan data yang dihapus untuk ditampilkan
        
    def tampilkan(self):
        #Menampilkan isi stack dari top ke bawah
        current = self.top
        print("Top -> ", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Bawah di node terakhir")
        
# Instantiasi objek ke class StackLL
s = StackLL()

s.enqueue("A")
s.enqueue("B")
s.enqueue("C")

# Menampilkan isi stack
s.tampilkan()

s.dequeue() # Output: C
s.tampilkan() # Output: B