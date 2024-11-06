import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Perasaan tersulit adalah ketika hatimu
    terikat pada seseorang.
    
    kamu sadar bahwa kamu tidak dapat memilikinya,
    dan kamu pun tidak kuasa untuk menjauh darinya
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.10) # penundaan 0.10 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan
    for i in range(jumlah_ulang):

            tampilkan_kalimat_kata_per_huruf()
            time.sleep(1) # Penundaan 1 detik sebelum pengulangan
            print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()