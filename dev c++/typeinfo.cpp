#include <typeinfo>
#include <iostream>

int main() {
    float x = 10;
    std::cout << "Tipe data dari x: " << typeid(x).name() << std::endl;
    return 0;
}

