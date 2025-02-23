import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Fase paling menyakitkan adalah ketika
    kamu tidak bisa menjelaskan apa yang kamu rasakan,
    Berbaring ditempat tidur, mulai dengan tatapan kosong,
    tetapi kamu bisa merasakan hatimu semakin berat
    dari detik ke detik.
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
        tampilkan_kalimat_kata_per_huruf()
        print('\n' + '-' * 40) # Penundaan sebelum pengulangan

# Memanggil fungsi main untuk menjalankan program
main()