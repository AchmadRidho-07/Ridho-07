import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    setiap langkah kecil yang kamu ambil akan membawamu lebih dekat
    dengan impianmu. jika ada kegagalan, itu adalah kesempatan untuk belajar.
    jangan biarkan apapun menghentikan semangatmu, karena kamu bisa menghadapi apa saja
    percayalah pada dirimu, kamu punya kekuatan besar untuk mencapai hal-hal hebat.
    """
    for huruf in kalimat:
        print(huruf,end='', flush=True)
        time.sleep(0.10)  # Penundaan 0.10 detik per huruf

def main():
    jumlah_ulang = 1 # set jumlah pengulangan kalimat
    for i in range(jumlah_ulang):

            tampilkan_kalimat_kata_per_huruf()
            time.sleep(1)  # Penundaan 1 detik sebelum pengulangan berikutnya
            print('\n' + '-' * 40) # Pemisah antar pengulangan
    
# Memanggil fungsi main untuk menjalankan program
main()