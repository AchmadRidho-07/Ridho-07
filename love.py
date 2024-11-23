import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    For : Rizki Dwi Rahmawati
    Nikmatilah perjalanan hidupmu, meskipun begitu banyak
    cobaan yang menerpa, karena cobaan itu yang akan
    menjadikanmu wanita yang tangguh dikemudian hari.

    Ingatlah setiap langkah yang kamu ambil adalah
    investasi besar untuk masa depanmu, teruslah melangkah maju
    karena itu kamu sedang  mendekatkan diri pada cita-citamu.

    capek, lelah, sakit yang kamu rasakan saat ini
    adalah suatu hal yang wajar, tapi menyerah bukanlah solusinya.

    soo, keep spirit and good luck, wish you all the best
    in your life.
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