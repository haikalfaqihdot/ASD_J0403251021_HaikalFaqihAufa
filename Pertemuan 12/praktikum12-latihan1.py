#====================================================
# PRAKTIK PERTEMUAN KE-12
# Topik: Materi 1 " Graph II: Shortest Path (Dijkstra & Bellman-Ford) "
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ========================================================== 

# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 

# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D'] # Jalur A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # Jalur A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1) # Output: Jalur 1: A -> B -> D = 9
print("Jalur 2: A -> C -> D =", jalur_2) # Output: Jalur 2: A -> C -> D = 3

# Menentukan jalur terpendek berdasarkan total bobot
if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D") 
    
'''
Jawaban Analisis: 
1. Berapa total bobot jalur A -> B -> D? 
Total bobot jalur A -> B -> D adalah 4 (A ke B) + 5 (B ke D) = 9.
2. Berapa total bobot jalur A -> C -> D? 
Total bobot jalur A -> C -> D adalah 2 (A ke C) + 1 (C ke D) = 3.
3. Jalur mana yang dipilih sebagai jalur terpendek? 
Jalur terpendek adalah A -> C -> D.
4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang 
paling sedikit? 
Jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit karena bobot atau nilai pada setiap edge dapat berbeda. Sebuah jalur dengan lebih banyak edge bisa memiliki total bobot yang lebih kecil dibandingkan dengan jalur yang memiliki lebih sedikit edge, tergantung pada nilai bobot yang diberikan pada setiap edge. Oleh karena itu, untuk menentukan jalur terpendek, kita harus mempertimbangkan total bobot dari jalur tersebut, bukan hanya jumlah edge yang ada. 
'''