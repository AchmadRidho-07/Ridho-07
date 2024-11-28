#include <iostream>
using namespace std;
#define MAX 1000
class Stack {
int top; // Indeks elemen teratas dalam stack
public:
int a[MAX]; // Ukuran maksimum stack
Stack() { top = -1; } // Konstruktor, inisialisasi top ke -1
bool push(int x); // Menambahkan elemen ke stack
int pop(); // Menghapus elemen teratas
int peek(); // Mengakses elemen teratas
bool isEmpty(); // Mengecek apakah stack kosong
int display(); // Menampilkan semua elemen stack
};
// Implementasi fungsi `push`
bool Stack::push(int x) {
if (top >= (MAX - 1)) {
cout << "Stack Overflow" << endl;
return false;
} else {
a[++top] = x; // Increment top, lalu simpan elemen
cout << x << " didorong ke dalam tumpukan\n";
return true;
}
}
// Implementasi fungsi `pop`
int Stack::pop() {
if (top < 0) {
cout << "Stack Underflow" << endl;
return 0;
} else {
int x = a[top--]; // Ambil elemen teratas, lalu decrement top
return x;
}
}
// Implementasi fungsi `peek`
int Stack::peek() {
if (top < 0) {
cout << "Tumpukan Kosong" << endl;
return 0;
} else {
return a[top];
}
}
// Implementasi fungsi `isEmpty`
bool Stack::isEmpty() {
return (top < 0); // Mengembalikan true jika top < 0
}
// Implementasi fungsi `display`
int Stack::display() {
if (top < 0) {
cout << "Stack Kosong" << endl;
return 0;
}
cout << "Elemen-elemen dalam stack:" << endl;
for (int i = 0; i <= top; i++) {
cout << a[i] << " ";
}
cout << endl;
return top + 1; // Mengembalikan jumlah elemen dalam stack
}
// Fungsi utama untuk menguji implementasi
int main() {
Stack s;
// Menambahkan elemen ke dalam stack
s.push(10);
s.push(20);
s.push(30);
// Menghapus elemen teratas
cout << s.pop() << " dikeluarkan dari tumpukan\n";
// Menampilkan elemen setelah pop
s.display();
return 0;
}
