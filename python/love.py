import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Jika hubungan semakin rumit, itu artinya kita
    dijalan  yang tepat, kita hanya perlu bertahan 
    dan tetap berjuang, meski dunia  nunjukkin beberapa
    cara untuk kita berpisah.
    """

    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
            tampilkan_kalimat_kata_per_huruf()
            time.sleep(1) # Penundaan sebelum pengulangan
            print('\n' + '-' * 40) # Pemisah antar kalimat

# Memanggil fungsi main untuk menjalankan program
main()