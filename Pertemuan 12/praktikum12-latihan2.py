#====================================================
# PRAKTIK PERTEMUAN KE-12
# Topik: Materi 1 " Graph II: Shortest Path (Dijkstra & Bellman-Ford) "
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ========================================================== 

# Import library heapq untuk priority queue
import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Fungsi untuk mencari jarak terpendek menggunakan Dijkstra's Algorithm
def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    # Selama masih ada node yang akan diproses dalam priority queue
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Menjalankan Dijkstra's Algorithm dari node 'A'
hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)
    
'''
Jawaban Analisis: 
1. Berapa jarak terpendek dari A ke B? 
Jarak terpendek dari A ke B adalah 4, karena ada edge langsung dari A ke B dengan bobot 4.
2. Berapa jarak terpendek dari A ke C? 
Jarak terpendek dari A ke C adalah 2, karena ada edge langsung dari A ke C dengan bobot 2.
3. Berapa jarak terpendek dari A ke D? 
Jarak terpendek dari A ke D adalah 3, karena jalur A -> C -> D memiliki total bobot 2 (A ke C) + 1 (C ke D) = 3, yang lebih kecil dibandingkan dengan jalur A -> B -> D yang memiliki total bobot 4 (A ke B) + 5 (B ke D) = 9.
4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
Jarak A ke D lebih kecil melalui C dibandingkan melalui B karena bobot pada edge A ke C (2) dan C ke D (1) lebih kecil dibandingkan dengan bobot pada edge A ke B (4) dan B ke D (5). Oleh karena itu, jalur A -> C -> D memiliki total bobot yang lebih kecil (3) dibandingkan dengan jalur A -> B -> D (9).
5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
Fungsi priority_queue dalam algoritma Dijkstra adalah untuk menyimpan node-node yang akan diproses berdasarkan jarak terpendek yang telah ditemukan sejauh ini. Priority queue memastikan bahwa node dengan jarak terpendek akan diproses terlebih dahulu.
6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif? 
Dijkstra tidak cocok untuk graph dengan bobot negatif karena algoritma ini mengandalkan prinsip greedy, yaitu memilih jalur dengan jarak terpendek pada setiap langkah. Jika ada edge dengan bobot negatif, Dijkstra mungkin akan melewati jalur yang sebenarnya lebih pendek setelah melewati edge tersebut, sehingga menghasilkan hasil yang salah.
'''