#include <iostream>
#include <array>
using namespace std;
int main() {
array <int, 5> data = {10, 20, 30, 40, 50};

cout << "Ukuran array: " << data.size() <<endl;
cout << "Isi array: ";
for (int i = 0; i < data.size(); i++) {
cout << data[i] << " ";
}
cout <<endl;
return 0;
}
