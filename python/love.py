import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

Jangan minta senang, tapi mintalah tenang,
karena banyak yang terlihat senang tapi
tidak meraasakan ketenangan.
"""
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
        tampilkan_kalimat_kata_per_huruf()
        time.sleep(1) # Pengulangan setiap kalimat
        print('\n' + '-' * 40) # Penundaan sebelum pengulangan

# Memanggil fungsi main untuk menjalankan program
main()