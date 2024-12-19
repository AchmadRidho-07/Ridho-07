import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Psikologi mengatakan bahwa:

    Orang yang paling tertekan dalam keluarga
    bukanlah ayah ataupun ibu, tapi dia adalah

    Anak perempuan satu-satunya.
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan
    for i in range(jumlah_ulang):
            tampilkan_kalimat_kata_per_huruf()
            time.sleep(1) # Penundaan sebelum pengulangan
            print('\n' + '-' * 40) # Pemisah antar kalimat

# Memanggil fungsi main untuk menjalankan program
main()