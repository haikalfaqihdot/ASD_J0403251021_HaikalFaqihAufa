#====================================================
# TUGAS LINKED LIST LATIHAN 3
# Studi Kasus: Implementasikan	Pencarian	pada	node	tertentu	Double	Linked	List.	
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

#====================================================
# Class untuk menyimpan data(isi nilai) dan next(Pentunjuk untuk node selanjutnya)
#====================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#====================================================
# Class untuk menyimpan fungsi aksi yang akan dilakukan pada linkedList
#====================================================
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #====================================================
    # Fungsi untuk menambah data ke belakang (akhir list)
    #====================================================
    def append(self, data):
        new_node = Node(data)

        #====================================================
        # Kalau list masih kosong
        #====================================================
        if self.head is None:
            self.head = new_node
            return

        #====================================================
        # Kalau sudah ada isinya, cari node terakhir dulu
        #====================================================
        temp = self.head
        while temp.next:
            temp = temp.next

        #====================================================
        # Sambungkan node terakhir ke node baru
        #====================================================
        temp.next = new_node
        new_node.prev = temp
    
    #====================================================
    # Fungsi untuk mencari data tertentu
    #====================================================
    def search(self, key):
        temp = self.head

        #====================================================
        # Cek satu-satu sampai habis
        #====================================================
        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    #====================================================
    # Fungsi untuk menampilkan semua isi list
    #====================================================
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

#====================================================
# Membuat object dari DoublyLinkedList
#====================================================
dll = DoublyLinkedList()

#====================================================
# Input data dari user (dipisahkan pakai koma)
#====================================================
data_input = input("Masukkan elemen ke dalam Doubly Linked List (pisahkan dengan koma): ")
data_list = data_input.split(",")

#====================================================
# Memecah input menjadi list
#====================================================
for item in data_list:
    dll.append(int(item.strip()))

#====================================================
# Input data yang ingin dicari
#====================================================
cari = int(input("Masukkan elemen yang ingin dicari: "))

#====================================================
# Cek apakah datanya ada atau tidak
#====================================================
if dll.search(cari):
    print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {cari} tidak ditemukan dalam Doubly Linked List.")
