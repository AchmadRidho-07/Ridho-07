import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Di antara senyapnya malam
    aku kembali mengingatmu.

    kata-kata yang tak sempat kau ucap,
    rindu yang tak pernah habis,
    meski sudah terpendam.

    seperti hujan yang tak juga berhenti, 
    meski tak ada langit yang menangis.
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
            tampilkan_kalimat_kata_per_huruf()
            time.sleep(1) # penundaan 1 detik sebelum pengulangan k
            print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()
