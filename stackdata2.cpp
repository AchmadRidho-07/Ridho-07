#include <iostream>
#include <string> // Include untuk menggunakan tipe data string
using namespace std;

#define MAX 1000

class Stack {
    int top; // Indeks elemen teratas dalam stack
public:
    string a[MAX]; // Ukuran maksimum stack (menggunakan tipe data string)
    
    Stack() { top = -1; } // Konstruktor, inisialisasi top ke -1
    
    bool push(string x); // Menambahkan elemen ke stack
    string pop(); // Menghapus elemen teratas
    string peek(); // Mengakses elemen teratas
    bool isEmpty(); // Mengecek apakah stack kosong
    void display(); // Menampilkan semua elemen stack
};

// Implementasi fungsi `push` untuk string
bool Stack::push(string x) {
    if (top >= (MAX - 1)) {
        cout << "Stack Overflow" << endl;
        return false;
    } else {
        a[++top] = x; // Increment top, lalu simpan elemen
        cout << x << " didorong ke dalam tumpukan\n";
        return true;
    }
}

// Implementasi fungsi `pop` untuk string
string Stack::pop() {
    if (top < 0) {
        cout << "Stack Underflow" << endl;
        return ""; // Mengembalikan string kosong jika stack kosong
    } else {
        string x = a[top--]; // Ambil elemen teratas, lalu decrement top
        return x;
    }
}

// Implementasi fungsi `peek` untuk string
string Stack::peek() {
    if (top < 0) {
        cout << "Tumpukan Kosong" << endl;
        return ""; // Mengembalikan string kosong jika stack kosong
    } else {
        return a[top];
    }
}

// Implementasi fungsi `isEmpty`
bool Stack::isEmpty() {
    return (top < 0); // Mengembalikan true jika top < 0
}

// Implementasi fungsi `display` untuk menampilkan semua elemen stack
void Stack::display() {
    if (top < 0) {
        cout << "Stack Kosong" << endl;
        return;
    }
    cout << "Elemen-elemen dalam stack:" << endl;
    for (int i = 0; i <= top; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}

// Fungsi utama untuk menguji implementasi
int main() {
    Stack s;
    
    // Menambahkan elemen string ke dalam stack
    s.push("Achmad");
    s.push("Ridho");
    s.push("Al Bantanie");
    
    // Menghapus elemen teratas
    cout << s.pop() << " dikeluarkan dari tumpukan\n";
    
    // Menampilkan elemen setelah pop
    s.display();
    
    return 0;
}

