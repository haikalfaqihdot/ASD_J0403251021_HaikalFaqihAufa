# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Haikal Faqih Aufa
# NIM     : J0403251021
# Kelas   : TPL - B1
# ==============================================================================

# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}

    # Membaca file dengan format seusuai yang sudah di berikan dan menyimpan dalam struktur dictionary
    with open(nama_file, "r") as file:
        # Mengambil data buku per-baris dengan pengulangan dan dibuatkan sebuah variabel untuk data tersebut
        for baris in file:
            data = baris.strip().split(",")
            kode = data[0] # Mengambil data pada indeks 0
            judul = data[1] # Mengambil data pada indeks 0
            harga = int(data[2]) # Mengambil data pada indeks 0

            # Menyimban data ke dictionary dengan kode buku sebagai key
            database_buku[kode] = {
                "judul": judul,
                "harga": harga
            }

    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
# Membuat class Node buat menyimpan data judul buku dan pointer ke node selanjutnya
class Node:
    def __init__(self, judul):
        self.judul = judul # Menyimpan judul buku
        self.next = None # Pointer ke node berikutnya


# Class LinkedListPromosi berfungsi untuk mengelola daftar buku promosi menggunakan struktur Linked List
class LinkedListPromosi:
    def __init__(self):
        self.head = None # Node awal pada linked list

    def tambah_buku_promosi(self, judul):
        # Membuat node baru dengan judul buku yang diinputkan
        node_baru = Node(judul)

        # VALIDASI 
        # Jika linked list masih kosong maka node baru menjadi head
        if self.head is None:
            self.head = node_baru
        else:
            # Jika sudah ada data maka mencari node terakhir
            current = self.head
            while current.next:
                current = current.next

            # Menambahkan node baru di akhir linked list
            current.next = node_baru

    def tampilkan_promosi(self):
        # Mengambil node pertama dari linked list
        current = self.head

        # Mengecek apakah daftar promosi masih kosong
        if current is None:
            print("Belum ada buku promosi")
            return

        print("="*40)
        print("Daftar Buku Promosi:")

        # Traversal linked list untuk menampilkan seluruh judul buku
        while current:
            print("-", current.judul)
            current = current.next


# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]

# Class AntreanKasir menggunakan struktur Queue dengan prinsip FIFO
class AntreanKasir:
    def __init__(self):
        self.antrean = [] # List digunakan sebagai penyimpanan antrean pelanggan

    def tambah_antrean(self, nama_pelanggan):
        # Menambahkan pelanggan ke akhir antrean (enqueue)
        self.antrean.append(nama_pelanggan)

        # Menampilkan informasi bahwa pelanggan telah masuk antrean
        print(nama_pelanggan, "masuk ke dalam antrean, silahkan menunggu!")

    def layani_pelanggan(self):
        # Mengecek apakah antrean kosong
        if len(self.antrean) == 0:
            print("Tidak ada pelanggan di dalam antrean!")
        else:
            # Menghapus pelanggan pertama dalam antrean sesuai prinsip FIFO
            pelanggan = self.antrean.pop(0)

            # Menampilkan pelanggan yang sedang dilayani
            print(pelanggan, "sedang dilayani")


# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):

    # Melakukan perulangan mulai dari indeks ke-1
    for i in range(1, len(list_harga)):
        key = list_harga[i] # Menyimpan nilai yang akan dibandingkan
        j = i - 1 # Indeks elemen sebelumnya

        # Membandingkan elemen sebelumnya dengan key
        while j >= 0 and list_harga[j] > key:
            list_harga[j + 1] = list_harga[j] # Menggeser elemen ke kanan
            j -= 1

        # Menempatkan key pada posisi yang sesuai
        list_harga[j + 1] = key

    # Mengembalikan list yang sudah terurut
    return list_harga


# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================

def main():

    # Inialisasi Data yang akan digunakan pada program
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db) # Memuat data buku dari file
    list_promosi = LinkedListPromosi() # Membuat objek linked list promosi
    antrean_toko = AntreanKasir() # Membuat objek antrean kasir
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000] # Data transaksi

    while True:
        # Menampilkan menu utama sistem toko buku
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku")
        print("2. Kelola Daftar Promosi")
        print("3. Kelola Antrean Kasir")
        print("4. Lihat Laporan Penjualan Terurut")
        print("5. Keluar")

        # Mengambil input pilihan dari pengguna
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nKatalog Buku:")

            # Menampilkan seluruh data buku dari dictionary
            for kode, info_buku in data_buku.items():
                print(kode, "-", info_buku["judul"], "- Rp", info_buku["harga"])

        elif pilihan == '2':
            # Meminta input judul buku yang akan dimasukkan ke promosi
            print("")
            judul_baru = input("Masukkan judul buku untuk promosi: ")

            # Menambahkan buku ke linked list promosi
            list_promosi.tambah_buku_promosi(judul_baru)

            # Menampilkan seluruh buku promosi
            list_promosi.tampilkan_promosi()
            print("="*40)

        elif pilihan == '3':

            # Menampilkan submenu antrean kasir
            print("\n--- MENU PELAYANAN ---")
            print("1. Tambah Antrean")
            print("2. Layani Pelanggan")

            aksi = input("Pilih aksi: ")

            if aksi == "1":
                # Menambahkan pelanggan ke antrean
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)

            elif aksi == "2":
                # Melayani pelanggan pertama dalam antrean
                antrean_toko.layani_pelanggan()

        elif pilihan == '4':
            # Menampilkan data transaksi sebelum diurutkan
            print("Harga Sebelum Urut:", riwayat_transaksi)

            # Memanggil fungsi sorting untuk mengurutkan transaksi
            hasil_sort = urutkan_transaksi(riwayat_transaksi)

            # Menampilkan hasil transaksi yang sudah urut
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            # Menyelesaikan Program
            print("Program selesai.")
            break
        # Error Handler
        else:
            # Jika input tidak sesuai menu
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()