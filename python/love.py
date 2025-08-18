import time

def tampilkan_kalinat_kata_per_huruf():
    kalimat = """

    Waktu untuk hidup semakin berkurang,
    jadi jangan sekalipun membiarkan  imanmu
    ikut berkurang. umur boleh semakin tua dan bertambah
    tapi tidak dengan dosa.

    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
        tampilkan_kalinat_kata_per_huruf()
        time.sleep(1) # Penndaan sebelum pengulangan
        print('\n' + '-' * 40) # Pengulangan kalimat

# Memanggil fungsi main untuk menjalankan program
main()