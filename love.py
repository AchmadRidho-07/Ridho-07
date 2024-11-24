import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Manusia tabiat dasarnya mencintai dirinya,
    karena itu dia tidak melihat kecuali kebaikan
    demi kebaikan pada dirinya.

    tetapi... tabiat dasar manusia juga membenci
    orang yang tidak menyukainya, karena itu 
    dia tidak melihat kecuali keburukan keburukan
    yang ada pada orang yang tidak menyukainya.
    """

    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
        tampilkan_kalimat_kata_per_huruf()
        time.sleep(1) # Penundaan 1 detik sebelum pengulangan
        print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()