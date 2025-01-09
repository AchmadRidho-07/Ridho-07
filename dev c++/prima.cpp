#include<iostream>
using namespace std;
main()
{
	int bil, I, tanda;
	tanda = 0;
	cin>>bil;
	I = 2;
	while(I<=bil-1)
	{
		if(bil % I == 0)
		tanda = 1;
		I++;
	}
	if(tanda == 1)
	cout<<"bukan bilangan prima";
	else
	cout<<"bilangan prima";
}
