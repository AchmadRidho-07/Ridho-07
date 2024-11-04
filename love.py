import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

z    Penyesalan, yaah... kata yang sudah tidak asing lagi.
    penyesalan muncul membuat diri berandai-andai,
    jika saja waktu bisa diputar kembali,
    namun itu hanyalah angan-angan semesta.

    ADA YANG MENYESAL KARENA TAK MAMPU MEMANFAATKAN WAKTU DENGAN BAIK,
    ADA YANG MENYESAL KARENA TIDAK MENGENAL AGAMA SEJAK KECIL.
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.10)  # Penundaan 0.10 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):

            tampilkan_kalimat_kata_per_huruf()
            time.sleep(1)  # Penundaan 1 detik sebelum pengulangan berikutnya
            print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()