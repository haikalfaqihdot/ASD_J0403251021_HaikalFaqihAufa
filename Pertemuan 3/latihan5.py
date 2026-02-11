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

#====================================================
# Class untuk menyimpan fungsi aksi yang akan dilakukan pada linkedList
#====================================================
class LinkedList:
    def __init__(self):
        self.head = None

    #====================================================
    # Fungsi untuk menambah data ke belakang (akhir list)
    #====================================================
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    #====================================================
    # Fungsi untuk menampilkan semua isi list
    #====================================================
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    #====================================================
    # Fungsi untuk membalik isi list
    #====================================================
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next   
            current.next = prev       
            prev = current             
            current = next_node       

        self.head = prev              

#====================================================
# Membuat object LinkedList
#====================================================
ll = LinkedList()

#====================================================
# Input dari user (pisahkan pakai koma)
#====================================================
data_input = input("Masukkan elemen untuk Linked List: ")

#====================================================
# Ubah input jadi list
#====================================================
data_list = data_input.split(",")

#====================================================
# Masukkan satu per satu ke linked list
#====================================================
for item in data_list:
    ll.append(int(item.strip()))

print("Linked List sebelum dibalik: ", end="")
ll.display()

ll.reverse()

print("Linked List setelah dibalik: ", end="")
ll.display()
