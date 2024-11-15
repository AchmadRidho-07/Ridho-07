import time

# Fungsi untuk menampilkan lirik lagu berdasarkan waktu
def tampilkan_lirik(lirik_dengan_waktu):
    for baris, waktu in lirik_dengan_waktu:
        print(baris)
        time.sleep(waktu)  # Menunggu sesuai detik tertentu

# Daftar lirik lagu dengan waktu per baris (dalam detik)
lirik_dengan_waktu = [

    ("kiniku sadar", 3),
    ("cintaku ini", 3),
    ("tak berarti untukmu", 7),
    ("kau buat luka isi hatiku", 6),
    ("kau buatku sekecewa itu", 6),
    ("dimana letak hatimu yang dulu", 7),
    ("kau duakanku kau memilih dia", 6), 
]

# Menjalankan fungsi untuk menampilkan lirik
tampilkan_lirik(lirik_dengan_waktu)