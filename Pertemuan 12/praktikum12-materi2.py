#====================================================
# PRAKTIK PERTEMUAN KE-12
# Topik: Materi 1 " Graph II: Shortest Path (Dijkstra & Bellman-Ford) "
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Materi 2: Bellman-Ford Algorithm
# ==========================================================

# fungsi untuk melakukan penelusuran graph dengan Bellman-Ford Algorithm
def bellman_ford(graph, start): 
 
    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph} 
    # Jarak node awal = 0
    distances[start] = 0 
 
    # Relaksasi berulang 
    for _ in range(len(graph) - 1): 
        # Periksa semua node dan tetangganya
        for node in graph: 
            # Periksa semua tetangga
            for neighbor, weight in graph[node].items(): 
                # Jika ditemukan jarak lebih kecil
                if distances[node] + weight < distances[neighbor]: 
                    # Update jarak minimum
                    distances[neighbor] = distances[node] + weight 
 
    return distances