#====================================================
# PRAKTIK PERTEMUAN KE-4 
# Topik: Studi Kasus Queue
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#====================================================
# PROGRAM: Studi Kasus  Antrian Layanan Akademik
# Implementasi Queue =>
# Enqueue : Memindahkan pointer rear (nambah data baru di belakang)
# Dequeue: Memindahkan pointer front (menghapus data di depan)
# Konsep stack = Front -> B -> A
# Konsep Antrian/Queue = Front -> A -> B -> CRear
#====================================================

# 1) Mendefinisikan class Node (Unit dasar Linked List)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim  # Menyimpan NIM mahasiswa
        self.nama = nama # Menyimpan nama mahasiswa
        self.next = None # Pointer ke node berikutnya
    
# 2) Mendefinisikan class Queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None # Pointer ke node pertama (depan)
        self.rear = None # Pointer ke node terakhir (belakang)
        
    def is_Empty(self):
        #Ketika queue kosong, maka front = rear = None
        return self.front is None 
    
    # Menambahkan data baru ke bagian belakang antrian (rear)
    def enqueue(self,nim,nama):
        # Membuat node baru
        nodeBaru = Node(nim,nama)
        # Jika queue kosong, front dan rear menunjuk ke node baru
        if self.is_Empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        # Jika queue tidak kosong, tambahkan di belakang dan update rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru
        
    # Menghapus data palling depan (Memberikan layaanan akademik)
    def dequeue(self):
        # Memeriksa jika ingin melayani tapi antrian kosong
        if self.is_Empty():
            print("Antrian kosong, tidak ada Mahasiswa yang dilayani")
            return None
        # Lihat data bagian front, simpan di variabel data yang akan dihapus(dilayani)
        node_dilayani = self.front
        #geser pointer front ke next front
        self.front = self.front.next
        # Jika front menjadi none (data antrian terakhir yang dilayani), maka rear = front = none
        if self.front is None:
            self.rear = None
                
        return node_dilayani
    
    def tampilkan(self):
        if self.is_Empty():
            print("Antrian kosong, tidak ada Mahasiswa yang dilayani")
            return None
        
        print(" ")
        print("Daftar Antrian Mahasiswa (Front -> Rear):")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. NIM: {current.nim}, Nama: {current.nama}")
            current = current.next
            no += 1
            
            
# Program utama
def main():
    # instantiasi queue
    q = queueAkademik()
    
    while True:
        print("======= Menu Antrian Layanan Akademik ======")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            nim = input("Masukkan NIM Mahasiswa: ").strip()
            nama = input("Masukkan Nama Mahasiswa: ").strip()
            q.enqueue(nim,nama)
            print(f"Mahasiswa {nama} dengan NIM {nim} telah ditambahkan ke antrian.")
            
        elif pilihan == '2':
            mahasiswa_dilayani = q.dequeue()
            if mahasiswa_dilayani is not None:
                print(f"Mahasiswa {mahasiswa_dilayani.nama} dengan NIM {mahasiswa_dilayani.nim} telah dilayani.")
            
        elif pilihan == '3':
            q.tampilkan()
            
        elif pilihan == '4':
            print("Terima kasih telah menggunakan layanan akademik!")
            break
            
        else:
            print("Pilihan tidak valid, silakan pilih menu 1-4.")
            
if __name__ == "__main__":
    main()