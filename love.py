import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    kehidupan ini bukan tentang hubungan kamu dan dia,
    tetapi tentang hubungan seorang hamba kepada tuhannya.
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.10) # Penundaan 0.10 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
            tampilkan_kalimat_kata_per_huruf()
            time.sleep(1) # Penundaan 1 detik sebelum pengulangan
            print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()