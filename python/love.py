import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Gak penting siapa yang mematahkanmu
    atau yang membuatmu terluka

    yang terpenting adalah siapa yang
    membuatmu kembali tersenyum.

    ~ Fokuslah pada mereka
    ~ Bahagiakan mereka
    ~ Hiduplah dengan mereka
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

