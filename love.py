import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Jangan menunggu waktu untuk berubah lebih baik
    tetapi beruahlah menjadi lebih baik
    selagi masih ada waktu.
    """

    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.10) # Penundaan 0.10 detik er huruf

def main():
    jumlah_ulang = 1 # set jumlah penglangan kalimat
    for i in range(jumlah_ulang):

            tampilkan_kalimat_kata_per_huruf()
            time.sleep(1) # Penundaan 1 detik sebelum pengulagan
            print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()