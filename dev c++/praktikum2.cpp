#include <iostream>
using namespace std;

int main()
{
    int bilangan[5], value = 0;
    cout << "Masukan 5 angka yang akan dicari angka terbesar" << endl;
    for(int i = 0; i < 5; i++)
    {
        cout << "Masukkan Data-Datanya: ";
        cin >> bilangan[i];
        if(bilangan[i] > value)
            value = bilangan[i];
    }
    cout << "Bilangan terbesar adalah : " << value;
    return 0;
}
