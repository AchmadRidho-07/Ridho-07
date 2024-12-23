import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Hidup laki-laki itu isinya hanya tuntunan
    tanggung jawab dan pertanggung jawaban,
    lalu tentang salah dan menjadi pihak yang disalahkan,
    sisanya hanya lamunan dan harapan.

    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah prngulangan kalimat
    for i in range(jumlah_ulang):
            tampilkan_kalimat_kata_per_huruf()
            time.sleep(1) # Penundaan sebelum pengulangan
            print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()