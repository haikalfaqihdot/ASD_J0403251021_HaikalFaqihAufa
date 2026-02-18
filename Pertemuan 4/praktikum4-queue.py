#====================================================
# PRAKTIK PERTEMUAN KE-4 
# Topik: QUEUE	
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#===============================================================
# IMLEMENTASI DASAR: Node Pada Queue
#===============================================================

# Membuat class Node (Merupakan bagian dasar dari linked list)
class Node: # Class implementasi Stack
    def __init__(self,data):
        self.data = data # Menyimpan nilai / data
        self.next = None # Pointer ke note berikutnya
        
#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None # Pointer ke elemen pertama (depan)
        self.rear = None  # Pointer ke elemen terakhir (belakang)
        
    def is_empty(self):
        return self.front is None # Queue kosong jika front tidak menunjuk ke node manapun (None)
        
    def enqueue(self,data):
        # Menambah data dari belakang (rear)
        nodeBaru = Node(data) # Membuat node baru
        
        #Jika queue kosong, front dan rear menunjuk ke node baru
        if self.is_empty(): # Jika queue kosong, front dan rear menunjuk ke node baru
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #Jika queue tidak kosong:
        #real lama menunjuk ke node baru
        self.rear.next = nodeBaru 
        #Rear pindah ke node baru
        self.rear = nodeBaru 
        
    def dequeue(self):
        # Menghapus data dari depan (front)
        # 1) Lihat data yang paling depan (front) 
        data_terhapus = self.front.next # Front pindah ke node berikutnya (Node pertama dihapus)
        
        # 2) geser front ke node berikutnya
        self.front = self.front.next # Front pindah ke node berikutnya (Node pertama dihapus)
        
        # 3) Jika setelah geser front menjadi none, maka queue kosong
        if self.front is None: # Jika setelah dihapus queue menjadi kosong, rear juga harus di set ke None
            self.rear = None
            
        return data_terhapus # Mengembalikan data yang dihapus untuk ditampilkan
        
    def tampilkan(self):
        #Menampilkan isi queue dari front ke rear
        current = self.front
        print("Front -> ", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Rear di node terakhir")
        
# Instantiasi objek ke class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

# Menampilkan isi queue
q.tampilkan()

q.dequeue() # Output: A
q.tampilkan() # Output: B