#include <iostream>
using namespace std;
#define max 5
string data[max];
int front = 0;
bool isFull(){
if(front >= max){
return true;
} else{
return false;
}
}
bool isEmpty(){
if(front == 0){
return true;
}else{
return false;
}
}
void view(){
if(!isEmpty()){
cout << "Data Antrian : " <<endl;
for(int a = front-1; a >= 0; a--){
cout << a+1 << ". " << data[a] <<endl;
}
}else {
cout << " Antrian Kosong" <<endl;
}
if(isFull()){
cout << "Antrian Penuh" <<endl;
}
cout << endl;
}
void enqueue(){
if(!isFull()){
cout << "Masukkan Data : ";
cin >> data[front];
front++;
}
}
void dequeue(){
if(!isEmpty()){
	for(int a = 0; a< front-1; a++){
data[a] = data[a+1];
}
front--;
}
}
int main(){
int pilihan;
while (true) {
system("cls");
view();
cout << "Menu Utama\n1. Enqueue\n2. Dequeue\nPilihan : ";
cin >> pilihan;
if (pilihan == 1) {
system("cls");
enqueue();
} else if (pilihan == 2) {
system("cls");
dequeue();
}
}
}
