#====================================================
# TUGAS LINKED LIST LATIHAN 1
# Studi Kasus: Implementasikan	fungsi	untuk	menghapus	node	dengan	nilai	tertentu.
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

#====================================================
# Class untuk menyimpan fungsi aksi yang akan dilakukan pada linkedList
#====================================================
class LinkedList:
    #====================================================
    # Fungsi untuk menyatakan bahwa bagian head kosong
    #====================================================
    def __init__(self):
        self.head = None

    #====================================================
    # Fungsi untuk menambahkan node baru, dan validasi pada node yang ditambahkan
    #====================================================
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    #====================================================
    # Fungsi untuk menghapus node baru
    #====================================================
    def delete_node(self, key):
        temp = self.head

        #====================================================
        # Memeriksa isi linked list
        #====================================================
        if temp is None:
            print("Linked list kosong.")
            return
        #====================================================
        # Memeriksa jika node yang ingin dihapus adalah head
        #====================================================
        if temp.data == key:
            self.head = temp.next
            temp = None
            print("Data berhasil dihapus.")
            return

        prev = None
        #====================================================
        # Mencari node yang akan dihapus
        #====================================================
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        #====================================================
        # Jika key tidak ditemukan
        #====================================================
        if temp is None:
            print("Data tidak ditemukan.")
            return

        #====================================================
        # Menghapus node
        #====================================================
        prev.next = temp.next
        temp = None
        print("Data berhasil dihapus.")

    #====================================================
    # Menampilkan isi dari linked list
    #====================================================
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

#====================================================
# Penggunaan kode 
#====================================================
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Sebelum dihapus:")
ll.print_list()

ll.delete_node(int(input("Masukan data yang ingin dihapus: ")))

print("Sesudah dihapus:")
ll.print_list()