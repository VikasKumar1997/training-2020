#include<bits/stdc++.h>
using namespace std;
bool isKingSafe(int row,int coloumn)
{
 int array[8][8];
 int outter,inner,flag=0,C=10,Q=20,E=30,H=40;
 for(outter=0;outter<8;outter++)
 for(inner=0;inner<8;inner++)
 array[outter][inner]=0;
 array[0][1]=C;   //cammel//
 array[6][4]=Q;  //queen//
 array[5][3]=E;   //elephant//
 array[5][7]=H;   //horse//
 for(outter=0;outter<8;outter++)
 {
 	for(inner=0;inner<8;inner++)
 	{		
		 if(array[outter][inner]==C )
 		{
 			if(((outter+inner) == (row+coloumn)) || ((outter-inner) == (row-coloumn)))
 			return false;
 			else
 		   	flag++;
 		}
		else if(array[outter][inner]==Q)
		{
		    if(((outter+inner) == (row+coloumn)) || ((outter-inner) == (row-coloumn)))
 			return false;
 			else if(outter==row || inner==coloumn)
 			return false;
 			else
 			flag++;
 		}
		else if(array[outter][inner]==E)
		{
			if(outter==row || inner==coloumn)
			return false;
			else
			flag++;
		}
		else if(array[outter][inner]==H)
		{
		if((outter-row==1 && inner-coloumn==2) || (outter-row==2 && inner-coloumn==1))
		return false;
		else
		flag++;
	    }
	    else
	    int c=1;
	 }
  }
 if(flag==4)
	return true;	
}
int main()
{
	int row,coloumn;
	bool result;
	cout<<"Entered the row cordinates of king:-";
	cin>>row;
	cout<<"Entered the coloumn cordinates of king:-";
	cin>>coloumn;
	if(row<=7 && coloumn<=7)
	result=isKingSafe(row,coloumn);
	else
	cout<<"king cordinates is wrong";
	if(result==true)
	cout<<"king is safe";
	else
	cout<<"king is not safe";
	return 0;
}
