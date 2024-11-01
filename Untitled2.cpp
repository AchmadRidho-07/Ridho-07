#include <iostream>
using namespace std;
main(){
	int arr2[] = {20, 30, 40, 50}; //Ukuran otomatis menjadi 4
	
// Menampilkan elemen-elemen array
	for (int i = 0; i < 4; i++) {
		cout << "Elemen ke-" << i + 1 << ": " << arr2[i] << endl;
	}
		//cout << "Elemen ke-" << i + 1 << ": " << arr2[i] << endl;
}
