#include <algorithm>
#include <iostream>
using namespace std;
int main() {
int arr[] = {5, 2, 9, 1};
sort(arr, arr + 4);
cout << "Array terurut: ";
for (int i=0; i< 4; i++) {
cout << arr [i] << " "; }
cout << endl;
return 0;
}
