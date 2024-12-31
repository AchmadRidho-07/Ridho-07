#include <bitset>
#include <iostream>

int main() {
    // Membuat bitset berukuran 8 bit dengan nilai awal 60
    std::bitset<8> bits(60); 

    // Menampilkan representasi biner awal
    std::cout << "Bilangan binner : " << bits << std::endl;

    return 0;
}

