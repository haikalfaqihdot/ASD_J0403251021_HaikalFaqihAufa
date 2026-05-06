#====================================================
# PRAKTIK PERTEMUAN KE-12
# Topik: Materi 1 " Graph II: Shortest Path (Dijkstra & Bellman-Ford) "
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)
    
'''
Jawaban Analisis: 
1. Berapa bobot langsung dari A ke B? 
Bobot langsung dari A ke B adalah 5.
2. Berapa total bobot jalur A -> C -> B?
Total bobot jalur A -> C -> B adalah 4 (A ke C) + (-2) (C ke B) = 2. 
3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? 
Jalur A -> C -> B menghasilkan jarak lebih kecil menuju B dengan total bobot 2, dibandingkan dengan jalur langsung A -> B yang memiliki bobot 5.
4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
 Bellman-Ford melakukan relaksasi pada semua edge sebanyak jumlah node - 1 kali, sehingga dapat menemukan jarak terpendek bahkan jika terdapat edge dengan bobot negatif. 
5. Apa yang dimaksud dengan proses relaksasi edge?
Proses relaksasi edge adalah langkah dalam algoritma Bellman-Ford (dan juga Dijkstra) di mana kita memeriksa setiap edge dalam graph dan mencoba untuk memperbarui jarak terpendek ke node tujuan jika ditemukan jalur yang lebih pendek melalui edge tersebut.
6. Apa perbedaan utama Bellman-Ford dan Dijkstra? 
Perbedaan utama antara Bellman-Ford dan Dijkstra adalah bahwa Bellman-Ford dapat menangani graph dengan bobot negatif, sedangkan Dijkstra tidak dapat. Bellman-Ford melakukan relaksasi pada semua edge sebanyak jumlah node - 1 kali, sehingga dapat menemukan jarak terpendek bahkan jika terdapat edge dengan bobot negatif. 
'''
    