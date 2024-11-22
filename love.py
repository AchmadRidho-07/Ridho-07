import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    "Sebenarnya aku pengen banget bahagiain kamu,
    tapi aku sadar, kelakuanku saja sering bikin kamu kesal."

    "Aku sayang banget sama kamu, tapi maaf yaa
    kalau aku banyak salahnya"
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):
            tampilkan_kalimat_kata_per_huruf()
            time.sleep(1) # PEnundaan 1 detik sebelum pengulangan
            print('\n' + '-' * 40) # PEmisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main()