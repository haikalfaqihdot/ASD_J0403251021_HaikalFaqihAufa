#====================================================
# LATIHAN PERTEMUAN KE-5
# Topik: Latihan 5.2  "Tracing Rekursi"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
#  Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    # Fungsi ini menampilkan angka saat masuk ke rekursi,
    # lalu menampilkan lagi saat proses rekursinya selesai (kembali)

    # Base case: jika n sudah 0, hentikan dan tampilkan "Selesai"
    if n == 0:
        print("Selesai")
        return

    # Dicetak sebelum masuk lebih dalam (fase turun rekursi)
    print("Masuk:", n)

    # Recursive call: memanggil dirinya sendiri dengan n - 1
    countdown(n - 1)

    # Dicetak setelah proses rekursi selesai (fase naik/kembali)
    print("Keluar:", n)

countdown(3)
# Output "Keluar" muncul terbalik karena dicetak saat proses rekursi kembali (fase naik) seperti tumpukan stack.