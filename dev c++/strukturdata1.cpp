#include <iostream>
using namespace std;
struct mahasiswa
{
char nim [9];
char nama [25];
char alamat [40];
short umur;
};main()
{
mahasiswa mhs;
cout<<"Nim :";
cin.getline(mhs.nim,9);
cout<<"Nama :";
cin.getline(mhs.nama,25);
cout<<"Alamat :";
cin.getline(mhs.alamat,40);
cout<<"umur :";
cin>>mhs.umur;
cout<<"\n\n\nnim :"<<mhs.nim;
cout<<"\nnama :"<<mhs.nama;
cout<<"\nalamat :"<<mhs.alamat;
cout<<"\numur :"<<mhs.umur;
cin.get();
}
