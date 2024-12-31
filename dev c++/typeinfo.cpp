#include <typeinfo>
#include <iostream>

int main() {
    int x = 10;
    std::cout << "Tipe data dari x: " << typeid(x).name() << std::endl;
    return 0;
}

