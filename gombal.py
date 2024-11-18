import time

# Fungsi untuk menampilkan lirik lagu berdasarkan waktu
def tampilkan_lirik(lirik_dengan_waktu):
    for baris, waktu in lirik_dengan_waktu:
        print(baris)
        time.sleep(waktu) # Menunggu sesuai detik tertentu

# Daftar lirik lagu dengan waktu per baris (dalam detik)
lirik_dengan_waktu = [

    ("Meski beribu bintang terangi hati", 4),
    ("Hanya kamu yang selalu ku nanti", 4),
    ("Tanpa dirimu tiada berarti", 5),
    ("Kau takkan terganti", 1),
]

# Menjalankan fungsi untuk menampilkan lirik
tampilkan_lirik(lirik_dengan_waktu)