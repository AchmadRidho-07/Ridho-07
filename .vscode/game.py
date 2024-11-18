import random

def tebak_angka():
    print("Selamat datang di game Tebak Angka!")
    print("Saya sudah memilih angka antara 1 dan 100. Coba tebak!")

    # Komputer memilih angka acak antara 1 dan 100
    angka_rahasia = random.randint(1, 100)
    
    # Jumlah tebakan pemain
    tebakan = 0
    
    # Loop hingga pemain menebak angka yang benar
    while True:
        try:
            # Meminta input dari pemain
            tebakan_user = int(input("Masukkan tebakanmu (1-100): "))
            tebakan += 1

            # Cek apakah tebakan benar, lebih kecil, atau lebih besar
            if tebakan_user < angka_rahasia:
                print("Tebakanmu terlalu kecil. Coba lagi!")
            elif tebakan_user > angka_rahasia:
                print("Tebakanmu terlalu besar. Coba lagi!")
            else:
                print(f"Selamat! Kamu berhasil menebak angka {angka_rahasia} dengan {tebakan} tebakan.")
                break
        except ValueError:
            print("Masukkan angka yang valid!")

# Memulai game
tebak_angka()
55