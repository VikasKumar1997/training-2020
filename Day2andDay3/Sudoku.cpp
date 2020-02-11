#include<bits/stdc++.h>
using namespace std;
bool isValidSudoku(int sudo[50][50],int size)
{
	int temp,f=0;
	for(int outter=0;outter<size;outter++)
	{
		for(int inner=0;inner<size;inner++)
		{
			temp=sudo[outter][inner];
			if(temp>size)
			return false;
			for(int in=0;in<size;in++)
			{
			if(inner!=in)
			{
				if(temp==sudo[outter][in])
				return false;
			}	
		}
	}
}
	for(int outter=0;outter<size;outter++)
	{
		for(int inner=0;inner<size;inner++)
		{
			temp=sudo[inner][outter];
			if(temp>size)
			return false;
			for(int in=0;in<size;in++)
			{
			if(outter!=in)
			{
				if(temp==sudo[inner][in])
				return false;
			}	
		}
	}
}
  return true;	
}
int main()
{
	int sudo[50][50],size,t;
	bool result;
	cout<<"enter the size of sudo please enter in perfect square:-";
	cin>>size;
	for(int i=1;i<size;i++)
	{
	 t=i*i;
	  if(t==size)
	  	break;
	  	else
	  	{
	     if(t>size)
	    {
	    	cout<<"please enter valid input";
	    	exit(0);
		}
	}
}
    cout<<"enter values of sudo";
    for(int outter=0;outter<size;outter++)
     for(int inner=0;inner<size;inner++)
       cin>>sudo[outter][inner];
     for(int outter=0;outter<size;outter++)
     {
     for(int inner=0;inner<size;inner++)
     {
	 cout<<sudo[outter][inner];  
}
cout<<"\n";
}
    result=isValidSudoku(sudo,size);
    if(result==true)
    cout<<"valid sudoku";
    else
    cout<<"invalid sudoku";
    return 0;
}
