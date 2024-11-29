import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Siapa yang mengenal Allah, maka bergaul
    dengan mahluk sudak tak nikmat lagi.

    Siapa yang sudah mengenal dunia,
    maka dia tidak tertarik lagi mengejarnya.

    Siapa yang sudah mengerti keadilan Allah,
    maka dia akan menghindari perselisihan 
    denga manusia.

    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
        tampilkan_kalimat_kata_per_huruf()
        time.sleep(1) # Penundaan 1 detik sebelum pengulangan
        print('\n' + '-' * 40) # Pemisah antar pengulangam

# Memanggil fungsi main untuk menjalankan program
main()