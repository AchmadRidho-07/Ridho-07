import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Akhir dari sebuah penderitaan menghasilkan
    jiwa yang kuat. tetapi, harus ditandai
    oleh bekas luka yang hebat.
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penunaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
        tampilkan_kalimat_kata_per_huruf()
        time.sleep(1) # Penundaan sebelum pengulangan
        print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()