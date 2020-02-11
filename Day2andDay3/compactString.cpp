#include<bits/stdc++.h>
using namespace std;
bool isCompactString(char value[50],int size)
{
 char set[]={'a','b','c'};
 char checkstring[50];
 int outter=0,count=0,testsize,test,flag=0,tag=0,c=1;
 while(outter<size)
 {
  
  if(value[outter]!=set[0] && value[outter]!=set[1] && value[outter]!=set[2])
  {
  checkstring[count]=value[outter];
  count++;
  outter++;
}
else
{
	for(int inner=0;inner<3;inner++)
	{
		if(value[outter]==set[inner])
		{
			for(int in=0;in<3;in++)
			{
			if(value[outter+1]==set[in])
			{
				tag=1;
			 for(int t=0;t<3;t++)
			 {
			 	if((t!=inner && t!=in) && inner!=in)
			 	{
			 		checkstring[count]=set[t];
			 		count++;
			 		outter=outter+2;
			 		break;
				 }
			 }
				
			}
		}
				checkstring[count]=value[outter];
				count++;
				outter++;
				break;
			}
		}
	}
}
puts(checkstring);
testsize=strlen(checkstring);
for(int index=0;index<testsize;index++)
if(checkstring[index]!=value[index])
{
   flag=1;
   break;
}
if(flag==1)
 return isCompactString(checkstring,testsize);
else
{
	if(testsize<=4)
	return true;
	else
	return false;
}
}
int main()
{
	char value[50];
	bool result;
	int size;
	cout<<"Enter a string:-";
	gets(value);
	size=strlen(value);
	result=isCompactString(value,size);
	if(result==true)
	cout<<"Entered string is get reduced in compact state\n";
	else
	cout<<"Entered string is not in compact state";	
	return 0;
}
