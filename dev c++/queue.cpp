#include<iostream>
#include<array>
#include<queue>
using namespace std;

int main(){
	array<int,5>data = (10, 20, 30, 40, 50);
	
		cout<<"Ukuran array:"<< data.size()<<endl;
	cout<<"isi array:";
	for (int i = 0; < data.size(); i++){
		cout << data[i]<"";
	}
		cout<<endl;
		
		queque<int>myQueue;
		
	for (int elem : data) {
		myQueue.push(elem);
	}
	
	cout<<"Queue(FIFO):";
	while(!myQueue.empty()) {
		cout<<myQueue.front()<<"";
		myQueue.pop();
	}
	cout<<endl;
	
	return 0;
}
