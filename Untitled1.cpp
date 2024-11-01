#include <iostream>
using namespace std;
main(){
 int n=10;
 int arr1[n];
     cout<<"jumlah elemen array adalah: "<<n<<endl;
for (int i = 0; i < n; i++) {
		cout << "Masukkan elemen ke-" << i + 1 << ": ";
		cin>>arr1[i];
	}

	// Menampilkan elemen array
	cout << "Isi array adalah: ";
	for (int i = 0; i < n; i++) {
		cout << arr1[i] << " ";
	}
}
