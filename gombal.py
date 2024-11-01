import time

# Fungsi untuk menampilkan lirik lagu berdasarkan waktu
def tampilkan_lirik(lirik_dengan_waktu):
    for baris, waktu in lirik_dengan_waktu:
        print(baris)
        time.sleep(waktu)  # Menunggu sesuai detik tertentu

# Daftar lirik lagu dengan waktu per baris (dalam detik)
lirik_dengan_waktu = [

    ("apa sudah ada kabar lain yang kau tunggu", 5),
    ("sudah adakah yang gantikan ku", 5),
    ("yang khawatirkan mu setiap waktu", 5),
    ("yang cerita tentang apapun sampai hal-hal  tak perlu", 6),
    ("kalau bisa, jangan buru buru", 5),
    ("kalau bisa, jangan ada dulu", 5),
]

# Menjalankan fungsi untuk menampilkan lirik
tampilkan_lirik(lirik_dengan_waktu)

