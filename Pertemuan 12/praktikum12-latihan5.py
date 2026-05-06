#====================================================
# PRAKTIK PERTEMUAN KE-12
# Topik: Materi 1 " Graph II: Shortest Path (Dijkstra & Bellman-Ford) "
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ========================================================== 
# Latihan 5: Latihan dari Studi Kasus Jalur Terpendek Antar Kota
# Algoritma: Dijkstra 
# ========================================================== 

import heapq

graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    # Inisialisasi semua jarak ke tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue untuk menyimpan (jarak, node)
    priority_queue = [(0, start)]

    # Proses selama queue tidak kosong
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak sekarang lebih besar dari yang tercatat, skip
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

start_node = 'Bogor'

# Menjalankan algoritma
hasil = dijkstra(graph, start_node)

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")
    
'''
Jawaban Analisis: 
1. Node awal yang digunakan apa? 
Node awal yang digunakan adalah Bogor.
2. Node mana yang memiliki jarak paling kecil dari node awal? 
Node yang memiliki jarak paling kecil dari Bogor adalah Depok dengan jarak 2.
3. Node mana yang memiliki jarak paling besar dari node awal? 
Node yang memiliki jarak paling besar dari Bogor adalah Bandung dengan jarak 7.
4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat. 
Algoritma Dijkstra bekerja dengan memulai dari node awal (Bogor) dan menginisialisasi jarak ke semua node lain sebagai tak hingga, kecuali jarak ke dirinya sendiri yang diatur menjadi 0. Algoritma kemudian menggunakan priority queue untuk memproses node dengan jarak terkecil terlebih dahulu. Pada setiap langkah, algoritma memeriksa tetangga dari node yang sedang diproses dan menghitung jarak baru ke tetangga tersebut. Jika jarak baru lebih kecil daripada jarak yang sudah tercatat, maka jarak tersebut diperbarui dan tetangga tersebut dimasukkan kembali ke dalam priority queue untuk diproses lebih lanjut.a.
'''