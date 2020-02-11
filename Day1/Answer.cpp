#include<bits/stdc++.h>
using namespace std;
int secondGreatestNumber(int a[],int s) // here we pass array and its size s define its size//
{
	int t,i,j;
	for(i=0;i<s;i++) //here we use i as an index variable//
	{
		for(j=i;j<s;j++) //here we use j as an index variable//
		{
			if(a[i]<a[j])
			{
				t=a[i];          //In this area we do swapping so we can sort array in desending order//
				a[i]=a[j];
				a[j]=t;
			}
		}
	}                        
	for(i=1;i<s-1;i++)   //here i check the repeatance of value//
	if(a[0]!=a[i])
	return a[1];      //returning value//
}
bool isNameValid(char n[100])   //here i get name in variable n//
{
	int c,i,f=0,t=0,x,y;
	c=strlen(n);
	for(i=0;i<c;i++)
	{
		if(n[i]=='A' || n[i]=='E' || n[i]=='I' || n[i]=='O' || n[i]=='U')
		f++;
		else if(n[i]=='T')
		{
			for(x=i-1;x>=0;x--)
			{
				if(n[x]=='S')
				{
				t=1;
				break;
			    }
			}
			for(y=i+1;y<=c;y++)
			{
				if(n[y]=='S')
				{
					t++;
					break;
				}
			}
			if(t==2)
			return false;
		}	
	}
	if(f>1)
	return false;
	else 
	return true;
}
bool isPrimeArray(int a[],int s)
{
	int f=0,i,j;
	for(i=0;i<s;i++)
	{
		for(j=2;j<=a[i]/2;j++)
		if(a[i]%j==0)
		{
		f=1;
		return false;
	    }
    }
	if(f==0)
	return true;
}
int main()
{
	int t,i,c;
	bool f,q,l;
	char o[100],p[100];
	cout<<"enter a name:-";
	gets(o);
	cout<<"enter an url";
	gets(p);
	cout<<"enter the size of array:-";
	cin>>t;
	int a1[t];
	cout<<"enter the elements of array:-\n";
	for(i=0;i<t;i++)
	cin>>a1[i];
	f=isPrimeArray(a1,t);
	if(f==true)
	{
	cout<<"array is of prime numbers";
	cout<<endl;}
	else
	{
	cout<<"array is not of prime numbers";
	cout<<endl;}
	c=secondGreatestNumber(a1,t);
	cout<<"second greatest number is:-"<<c;
	cout<<endl;
	q=isNameValid(o);
	if(q==true){
	cout<<"Name is valid";
	cout<<endl;}
	else{
	cout<<"Name is not valid";
	cout<<endl;}
	return 0;
}

