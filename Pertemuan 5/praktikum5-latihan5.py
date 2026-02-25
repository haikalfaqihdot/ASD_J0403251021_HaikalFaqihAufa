#====================================================
# LATIHAN PERTEMUAN KE-5
# Topik: Latihan 5.5  "Rekursi Generator PIN"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
#  Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    # Fungsi ini membuat semua kemungkinan PIN dengan panjang tertentu
    # menggunakan angka 0, 1, dan 2 secara rekursif

    # Base case: jika panjang 'hasil' sudah sesuai,
    # maka PIN lengkap dan langsung ditampilkan
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Recursive case: coba tambahkan setiap angka (0,1,2)
    # lalu lanjutkan pembentukan PIN sampai panjang terpenuhi
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)

# Untuk mencegah agar angka tidak digunakan berulang, dapat menggunakan:
#  if angka not in hasil:
# Sebelum rekursi