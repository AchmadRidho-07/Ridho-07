#include <cassert>
#include <iostream>

int main() {
    int x = 10;
    assert(x == 10); // Program tidak berhenti
    assert(x == 10); // Program berhenti jika x != 6
    std::cout << "Pernyataan benar" << std::endl;
    return 0;
}

