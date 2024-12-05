#include <iostream>
using namespace std;

int main()
{
    int bilangan, nilai;
    cout << "Masukan suatu bilangan: ";
    cin >> bilangan;
    for(int i = 0; i < 13; i++)
    {
        nilai = i*bilangan;
        cout << i << " * " << bilangan << " = " << nilai << endl;
    }
    return 0;
}
