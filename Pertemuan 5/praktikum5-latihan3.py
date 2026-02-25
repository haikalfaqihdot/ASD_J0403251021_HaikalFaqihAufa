#====================================================
# LATIHAN PERTEMUAN KE-5
# Topik: Latihan 5.3  "Rekursi Nilai Maksimum"
#  
# Nama  : Haikal Faqih Aufa
# NIM   : J0403251021
# Kelas : TPL-B1
#====================================================

# ==========================================================
#  Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):
    # Fungsi ini mencari nilai terbesar dalam list
    # dengan membandingkan satu per satu menggunakan rekursi

    # Base case: kalau sudah sampai elemen terakhir,
    # langsung kembalikan nilai tersebut
    if index == len(data) - 1:
        return data[index]

    # Recursive case: cari nilai maksimum dari sisa elemen setelah index sekarang
    maks_sisa = cari_maks(data, index + 1)

    # Bandingkan elemen sekarang dengan maksimum dari sisa list
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))