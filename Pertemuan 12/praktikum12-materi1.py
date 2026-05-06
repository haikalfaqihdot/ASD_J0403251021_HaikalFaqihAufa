#====================================================
# PRAKTIK PERTEMUAN KE-12
# Topik: Materi 1 " Graph II: Shortest Path (Dijkstra & Bellman-Ford) "
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Materi 1: Dijkstra's Algorithm
# ==========================================================

# Import library heapq untuk priority queue
import heapq

# Representasi graph dengan bobot (weight)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Fungsi untuk melakukan penelusuran graph dengan Dijkstra's Algorithm
def dijkstra(graph, start):
    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}

    # Jarak node awal = 0
    distances[start] = 0

    # Priority queue
    pq = [(0, start)]

    # Selama masih ada node yang akan diproses dalam priority queue
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Menjalankan Dijkstra's Algorithm dari node 'A'
hasil = dijkstra(graph, 'A')
print(hasil)


'''
Penjelasan Keseluruhan Program:

1. Program ini menerapkan algoritma Dijkstra untuk mencari jalur terpendek dari satu node ke semua node lain dalam graph berbobot.
2. Graph direpresentasikan sebagai dictionary di mana key adalah node dan value adalah dictionary yang berisi tetangga dan bobot edge-nya.
3. Fungsi `dijkstra` menginisialisasi jarak ke semua node sebagai tak hingga, kecuali node awal yang diatur menjadi 0.
4. Priority queue digunakan untuk memproses node dengan jarak terkecil terlebih dahulu.
5. Pada setiap iterasi, program memeriksa tetangga dari node yang sedang diproses dan memperbarui jarak jika ditemukan jarak yang lebih pendek.
6. Hasil akhir adalah dictionary yang berisi jarak terpendek dari node awal ke semua node lain.
'''
