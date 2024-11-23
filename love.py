import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    People come and go, itu nyata.
    hari ini kamu datang, bisa jadi besok 
    kamu sudah menghilang, namun aku percaya bahwa
    setiap orang yang tuhan hadirkan dalam kehidupan
    pasti membawa pelajaran. 
    
    sialnya... kamu datang bukan untuk mengajarkan arti cinta sejati,
    tetapi mengajarkanku arti patah hati.
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