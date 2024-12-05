import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Semua ada waktunya. semua ada masanya.
    yakinlah pada waktunya nanti,
    Allah pasti akan berikan yang terbaik.

    Lakukanlah hal yang baik
    berprasangkalah yang baik,
    yakinlah Allah pasti akan 
    memberikan yang terbaik.
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
        tampilkan_kalimat_kata_per_huruf()
        time.sleep(1) # Penundaan 1 detik sebelum pengulangan
        print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()