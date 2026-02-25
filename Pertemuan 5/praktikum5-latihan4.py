#====================================================
# LATIHAN PERTEMUAN KE-5
# Topik: Latihan 5.4  "Rekursi Kombinasi Huruf"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
#  Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    # Fungsi ini membentuk semua kombinasi huruf A dan B
    # sepanjang n karakter menggunakan rekursi

    # Base case: kalau panjang 'hasil' sudah n,
    # berarti kombinasi sudah lengkap dan langsung dicetak
    if len(hasil) == n:
        print(hasil)
        return

    # Recursive call: tambah "A" lalu lanjutkan pembentukan
    kombinasi(n, hasil + "A")

    # Recursive call: tambah "B" untuk kemungkinan lainnya
    kombinasi(n, hasil + "B")

kombinasi(2)