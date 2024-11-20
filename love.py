import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Kemanapun alur cerita hidupmu, tetaplah bahagia
    menjadi manusia, tetaplah hidup sebagaimana mestinya
    tetaplah tertawa disela gaduhnya isi kepala,
    tetaplah menjadi diri sendiri disaat banyaknya
    pilihan yang membuatmu harus menjadi orang lain.
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