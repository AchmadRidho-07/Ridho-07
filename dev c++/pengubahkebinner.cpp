#include<iostream>
using namespace std;
int main(){
	int bil, I, B, A;
	cin>>bil;
	B = 128;
	for(I=1; I<=8; I++)
	{
		if(bil >= B)
		{
			bil = bil - B;
			A = 1;
		}else{
			A = 0;
		}
		cout<<A;
		B = B/2;
	}
	return 0;
}
