#include <iostream>
using namespace std;

int main() {
    int bilangan, hasil_bagi;

    // Input bilangan 
    cout << "Masukkan bilangan: ";
    cin >> bilangan;

    // Proses menentukan ganjil atau genap
    hasil_bagi = bilangan % 2;

    if (hasil_bagi == 0) {
        cout << "Bilangan Genap" << endl;
    } else {
        cout << "Bilangan Ganjil" << endl;
    }

    return 0;
}

