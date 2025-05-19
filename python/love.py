import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Akan datang masanya dimana kamu 
    dirayakan dan dicintai dengan hebat 
    oleh seseorang yang bersyukur  memilikimu.

    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
        tampilkan_kalimat_kata_per_huruf()
        time.sleep(1) # Penundaan sebelum pengulangan
        print('\n' + '-' * 40) # Pengulangan kalimat

# Memanggil fungsi main untuk menjalankan program
main()
