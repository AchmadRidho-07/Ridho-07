import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

        TERIMA KASIH 2024

    Terima kasih untuk baik dan buruknya
    Terima kasih untuk senang dan sedihnya
    Terima kasih untuk sakit dan kecewanya
    Terima kasih untuk pelajaran dan pengalamannya

    Yang telah memberi warna dalam perjalanan
    hidupku, kini saatnya kututup bab itu
    dan membuka lembaran baru
    di tahun 2025
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
        tampilkan_kalimat_kata_per_huruf()
        time.sleep(1) # Penundaan sebelum pengulangan
        print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()