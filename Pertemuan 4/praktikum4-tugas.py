#====================================================
# PRAKTIK PERTEMUAN KE-4 
# Topik: Studi Kasus Queue "Sistem Antrian Bengkel"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#====================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor 
#====================================================

# 1) Mendefinisikan class Node (Unit dasar Linked List)
class Node:
    def __init__(self,no,nama,servis):
        self.no = no  # Menyimpan nomer antrian bengkel
        self.nama = nama # Menyimpan nama pelanggan bengkel
        self.servis = servis # Menyimpan informasi servis yang dibutuhkan pelanggan
        self.next = None # Pointer ke node berikutnya
    
# 2) Mendefinisikan class Queue, terdiri dari front dan rear
class QueueBengkel:
    def __init__(self):
        self.front = None # Pointer ke node pertama (depan)
        self.rear = None # Pointer ke node terakhir (belakang)
        
    def is_Empty(self):
        #Ketika queue kosong, maka front = rear = None
        return self.front is None 
    
    # Menambahkan data baru ke bagian belakang antrian (rear)
    def enqueue(self,no,nama,servis):

        # Membuat node baru
        nodeBaru = Node(no,nama,servis)
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
            print("Antrian kosong, tidak ada pelanggan bengkel yang dilayani")
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
            print("Antrian kosong, tidak ada pelanggan bengkel yang dilayani")
            return None
        
        print(" ")
        print("Daftar Antrian Pelanggan Bengkel (Front -> Rear):")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. No Antrian: {current.no}, Nama: {current.nama}, Servis: {current.servis}")
            current = current.next
            no += 1
            
            
# Program utama
def main():
    # instantiasi queue
    q = QueueBengkel()
    
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih menu : ")
        
        if pilihan == '1':
            no = input("Masukkan No Antrian Pelanggan: ").strip()
            nama = input("Masukkan Nama Pelanggan: ").strip()
            servis = input("Masukkan Servis yang dibutuhkan: ").strip()
            q.enqueue(no,nama,servis)
            print(f"Pelanggan {nama} dengan No Antrian {no} dengan servis {servis} telah ditambahkan ke antrian.")
            
        elif pilihan == '2':
            pelanggan_dilayani = q.dequeue()
            if pelanggan_dilayani is not None:
                print(f"Pelanggan {pelanggan_dilayani.nama} dengan No Antrian {pelanggan_dilayani.no} telah dilayani.")
            
        elif pilihan == '3':
            q.tampilkan()
            
        elif pilihan == '4':
            print("Terima kasih telah menggunakan layanan bengkel!")
            break
            
        else:
            print("Pilihan tidak valid, silakan pilih menu 1-4.")
            
if __name__ == "__main__":
    main()