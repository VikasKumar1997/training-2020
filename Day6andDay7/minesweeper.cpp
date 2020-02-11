#include<bits/stdc++.h>
using namespace std;
const int mine=-1;
const int size=8;
int internalboard[size][size];
int showuser[size][size];
bool result=true;
int row=0,column=0;

void createMatrix()
{
  for(int outter=0;outter<size;outter++)
  for(int inner=0;inner<size;inner++)
  {
            if (internalboard[outter][inner]==mine)
            {
                if (outter==0 && inner==0)
                    for(int out=0;out<2;out++)
                        for(int inn=inner;inn<inner+2;inn++)
                            if (internalboard[out][inn]!=mine)
                                internalboard[out][inn]=internalboard[out][inn]+1;
                            else
                                continue;
                    
                else if (outter==0 && inner==size-1)
                      for(int out=outter;out<outter+2;out++)
                        for(int inn=inner-1;inn<inner+1;inn++)
                            if (internalboard[out][inn]!=mine)
                                internalboard[out][inn]=internalboard[out][inn]+1;
                            else
                                continue;
                else if (outter==size-1 && inner==0)
                     for(int out=outter-1;out<outter+1;out++)
                        for(int inn=0;inn<2;inn++)
                            if (internalboard[out][inn]!=mine)
                                internalboard[out][inn]=internalboard[out][inn]+1;
                            else
                                continue;
                else if (outter==size-1 && inner==size-1)
                     for(int out=outter-1;out<outter+1;out++)
                        for(int inn=inner-1;inn<inner+1;inn++)
                            if (internalboard[out][inn]!=mine)
                                internalboard[out][inn]=internalboard[out][inn]+1;
                            else
                                continue;
                else if (outter==0 && inner!=size-1 && outter!=inner)
                     for(int out=0;out<2;out++)
                        for(int inn=inner-1;inn<inner+2;inn++)
                            if (internalboard[out][inn]!=mine)
                                internalboard[out][inn]=internalboard[out][inn]+1;
                            else
                                continue;
                else if (outter==size-1 and inner!=0 and outter!=inner)
                     for(int out=outter-1;out<outter+1;out++)
                         for(int inn=inner-1;inn<inner+2;inn++)
                            if (internalboard[out][inn]!=mine)
                                internalboard[out][inn]=internalboard[out][inn]+1;
                            else
                                continue;
                else if (inner==0 && outter!=size-1 && outter!=inner)
                     for(int out=outter-1;out<outter+2;out++)
                        for(int inn=0;inn<2;inn++)
                            if (internalboard[out][inn]!=mine)
                                internalboard[out][inn]=internalboard[out][inn]+1;
                            else
                                continue;
                else if (inner==size-1 && outter!=0 && outter!=inner)
                     for(int out=outter-1;out<outter+2;out++)
                        for(int inn=inner-1;inn<inner+1;inn++)
                            if (internalboard[out][inn]!=mine)
                                internalboard[out][inn]=internalboard[out][inn]+1;
                            else
                                continue;
                else if (inner!=0 && outter!=0 && inner!=size-1 && outter!=size-1)
                     for(int out=outter-1;out<outter+2;out++)
                        for(int inn=inner-1;inn<inner+2;inn++)
                            if (internalboard[out][inn]!=mine)
                                internalboard[out][inn]=internalboard[out][inn]+1;
                            else
                                continue;
           }
            else
                continue;
}
}
void onClick(int row,int column)
{		
	if(row>=0 && row<size &&  column>=0 && column<size){
		if(showuser[row][column]!=9)
		return;
	 showuser[row][column]=internalboard[row][column];
		if(internalboard[row][column]!=mine && internalboard[row][column]!=0)
		{
			showuser[row][column]=internalboard[row][column];
			return;
		}
		onClick(row-1,column-1);
		onClick(row,column-1);
		onClick(row+1,column-1);
		onClick(row-1,column);
		onClick(row+1,column);
		onClick(row-1,column+1);
		onClick(row,column+1);
		onClick(row+1,column+1);
}
else
return;
}
void checkAvalidity(int row,int column)
{
	if(internalboard[row][column]==mine)
	{
		cout<<"you blast the bomb you lose.";
		exit(0);
	}
	else
	return;
}
void internalDisplay()
{
	for(int outter=0;outter<size;outter++){
  for(int inner=0;inner<size;inner++)
  {
  cout<<internalboard[outter][inner]<<"  ";
}
cout<<"\n";
}
}
void userDisplay()
{
   for(int outter=0;outter<size;outter++){
  for(int inner=0;inner<size;inner++)
  {
  cout<<showuser[outter][inner]<<"  ";
}
cout<<"\n";
}
}
bool checkWin(){
	int count=0;
for(int outter=0;outter<size;outter++)
  for(int inner=0;inner<size;inner++)
  {
  if(showuser[outter][inner]==9)
  count++;	
}
if(count==1)
return false;
else
return true;
}
int main()
{
  for(int outter=0;outter<size;outter++)
  for(int inner=0;inner<size;inner++)
  internalboard[outter][inner]=0;
  for(int outter=0;outter<size;outter++)
  for(int inner=0;inner<size;inner++)
  showuser[outter][inner]=9;
    internalboard[0][0]=mine;
    internalboard[0][7]=mine;
    internalboard[3][3]=mine;
    internalboard[2][6]=mine;
    internalboard[5][1]=mine;
    internalboard[6][3]=mine;
    internalboard[5][3]=mine;
    internalboard[4][7]=mine;
   createMatrix();
   userDisplay();
 while(result)
  {	
  	cout<<"enter your row cordinate:-";
  	cin>>row;
  	cout<<"enter your column cordinate:-";
  	cin>>column;
  	if((row<0 || column<0) && (row>=size || column>=size)){
  		cout<<"please enter valid position";
  		continue;
	  }
  	checkAvalidity(row,column);
  	if(internalboard[row][column]==0)
  	{
  	onClick(row,column);
  	result=checkWin();
  	userDisplay();
  }
  else
  {
  showuser[row][column]=internalboard[row][column];
  result=checkWin();
  userDisplay();
}
}
  if(result==false){
  	showuser[0][0]=mine;
    showuser[0][7]=mine;
    showuser[3][3]=mine;
    showuser[2][6]=mine;
    showuser[5][1]=mine;
    showuser[6][3]=mine;
    showuser[5][3]=mine;
    showuser[4][7]=mine;
userDisplay();
  cout<<"\n\nyou win";	
}
  return 0; 
}

