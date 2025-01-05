import time

def tampilkan_kalimat_kata_per_huruf():
    kalimat = """

    Aku bukan laki-laki yang pintar dalam
    memahami cara berfikirmu, bukan juga laki-laki
    yang hebat dalam memberi rasa nyaman, 
    dan juga bukan laki-laki menyenangkan yang bisa
    memberimu berbagai kejutan indah,

    tapi jika kamu mengira selama ini aku tidak pernah
    peduli denganmu, kamu salah, hal kecil yang terjadi
    padamu saja aku selalu berfikir bagaimana cara
    menyikapinya dengan baik.

    aku selalu memperhatikanmu dengan cara yang mungkin
    berbeda dari laki-laki pada umumnya, tapi percayalah
    aku tulus melakukan segalanya untukmu.
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

# Memanggil fungsi mainuntuk menjalankan program
main()