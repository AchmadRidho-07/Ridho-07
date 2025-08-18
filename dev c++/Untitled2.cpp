#include <iostream>
using namespace std;

int main() {
    int bil1, bil2, bil3, max;

    // Input tiga bilangan
    cout << "Masukkan bilangan pertama: ";
    cin >> bil1;
    cout << "Masukkan bilangan kedua: ";
    cin >> bil2;
    cout << "Masukkan bilangan ketiga: ";
    cin >> bil3;

    // Menentukan bilangan terkecil
    if (bil1 < bil2 & bil1 < bil3) {
        max = bil1;
    } else if (bil2 < bil3) {
        max = bil2;
    } else {
        max = bil3;
    }

    // Output bilangan terkecil
    cout << "Bilangan terkecil adalah: " << max << endl;

    return 0;
}

