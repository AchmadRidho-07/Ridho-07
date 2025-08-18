#include <iostream>
#include <iomanip>
using namespace std;

struct Mahasiswa {
    string NIM;
    string nama;
    float ipk;
};

int main() {
    int jumlah;
    cout << "Masukkan jumlah mahasiswa: ";
    cin >> jumlah;

    Mahasiswa mhs[jumlah];

    // Input data mahasiswa
    for (int i = 0; i < jumlah; i++) {
        cout << "\nMahasiswa " << i + 1 << endl;
        cout << "Masukkan NIM: ";
        cin >> mhs[i].NIM;
        cin.ignore(); // Untuk mengabaikan newline setelah input NIM
        cout << "Masukkan Nama: ";
        getline(cin, mhs[i].nama);
        cout << "Masukkan IPK: ";
        cin >> mhs[i].ipk;
    }

    // Menampilkan data mahasiswa
    cout << "\nData Mahasiswa:\n";
    cout << "=============================================\n";
    cout << left << setw(12) << "NIM" 
         << setw(30) << "Nama" 
         << setw(5) << "IPK" << endl;
    cout << "=============================================\n";

    for (int i = 0; i < jumlah; i++) {
        cout << left << setw(12) << mhs[i].NIM
             << setw(30) << mhs[i].nama
             << setw(5) << fixed << setprecision(2) << mhs[i].ipk << endl;
    }

    return 0;
}

