#include <bitset>
#include <iostream>

int main() {
    // Membuat bitset berukuran 8 bit dengan nilai awal 25
    std::bitset<8> bits(25); 

    // Menampilkan representasi biner awal
    std::cout << "Bilangan binner : " << bits << std::endl;

    return 0;
}

