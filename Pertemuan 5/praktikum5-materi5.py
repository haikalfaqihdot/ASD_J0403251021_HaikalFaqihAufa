#====================================================
# PRAKTIK PERTEMUAN KE-5
# Topik: Materi 5 "Fungsi Rekursif"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Fungsi rekursif untuk membentuk biner sepanjang n digit
    # dengan jumlah angka '1' tidak boleh melebihi batas
    
    # Pruning: jika jumlah_1 melebihi batas, hentikan cabang ini
    if jumlah_1 > batas:
        return
    
    # Base case: jika panjang sudah n, cetak hasil dan berhenti
    if len(hasil) == n:
        print(hasil)
        return
    
    # Recursive call: tambah "0" tanpa menambah jumlah_1
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Recursive call: tambah "1" dan jumlah_1 bertambah 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)
    
biner_batas(4, 2)