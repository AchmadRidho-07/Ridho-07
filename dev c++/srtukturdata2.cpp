#include <iostream>
using namespace std;
struct Tinggal {
char Jaln[40];
char Kota[15];
int Pos;
};
struct Tgl_Lahir {
int Tanggal;
int Bulan;
int Tahun;
};
struct Mahasiswa {
char Nim[9];
char Nama[25];
Tinggal Alamat;
Tgl_Lahir Lahir;
};
main()
{
Mahasiswa Mhs;
cout << "NIM : "; cin.getline(Mhs.Nim, 9);
cout << "Nama : "; cin.getline(Mhs.Nama, 25);
cout << "Alamat : \n";
cout << "\tJalan : "; cin.getline(Mhs.Alamat.Jaln, 40);
cout << "\tKota : "; cin.getline(Mhs.Alamat.Kota, 15);
cout << "\tKode pos : "; cin >> Mhs.Alamat.Pos;
cout << "Tanggal Lahir : \n";
cout << "\tTanggal : "; cin >> Mhs.Lahir.Tanggal;
cout << "\tBulan : "; cin >> Mhs.Lahir.Bulan;
cout << "\tTahun : "; cin >> Mhs.Lahir.Tahun;
cout << "\n\nMencetak Kembali Nilai Anggota\n\n";
cout << "NIM : " << Mhs.Nim;
cout << "\nNama : " << Mhs.Nama;
cout << "\nAlamat : \n";
cout << "\tJalan : " << Mhs.Alamat.Jaln;
cout << "\n\tKota : " << Mhs.Alamat.Kota;
cout << "\n\tKode Pos : " << Mhs.Alamat.Pos;
cout << "\nTanggal Lahir: " << Mhs.Lahir.Tanggal << "-";
cout << Mhs.Lahir.Bulan << "-" << Mhs.Lahir.Tahun;
cin.get();
}
