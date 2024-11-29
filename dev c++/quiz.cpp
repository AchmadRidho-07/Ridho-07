#include <iostream>
using namespace std;

int main() {
    int bil1, bil2, bil3;

    // Input tiga bilangan
    cout << "Masukkan bilangan pertama: ";
    cin >> bil1;
    cout << "Masukkan bilangan kedua: ";
    cin >> bil2;
    cout << "Masukkan bilangan ketiga: ";
    cin >> bil3;

    // Menyortir bilangan dari terkecil ke terbesar
    int min, mid, max;
    
    if (bil1 < bil2 & bil1 < bil3) {
        max = bil1;
        if (bil2 < bil3) {
            mid = bil2;
            min = bil3;
        } else {
            mid = bil3;
            min = bil2;
        }
    } else if (bil2 < bil1 & bil2 < bil3) {
        max = bil2;
        if (bil1 < bil3) {
            mid = bil1;
            min = bil3;
        } else {
            mid = bil3;
            min = bil1;
        }
    } else {
        max = bil3;
        if (bil1 < bil2) {
            mid = bil1;
            min = bil2;
        } else {
            mid = bil2;
            min = bil1;
        }
    }

    // Output bilangan dari terkecil ke terbesar
    cout << "Urutan bilangan dari terkecil ke terbesar adalah: " << max << ", " << mid << ", " << min << endl;

    return 0;
}

