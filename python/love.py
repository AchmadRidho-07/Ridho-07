import time

def tampilkan_kalinat_kata_per_huruf():
    kalimat = """

    Kebanyakan manusia ketika berdoa begitu yakin
    bahwa tuhan maha mendengar, tetapi ketika bermaksiat
    seakan lupa bahwa tuhan maha melihat.
    """
    for huruf in kalimat:
        print(huruf, end='', flush=True)
        time.sleep(0.05) # Penundaan 0.05 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan
    for i in range(jumlah_ulang):
            tampilkan_kalinat_kata_per_huruf()
            time.sleep(1) # Penundaan sebelum pengulangan
            print('\n' + '-' * 40) # Pemisah antar pengulangan

# Memanggil fungsi main untuk menjalankan program
main() 