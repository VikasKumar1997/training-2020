#include<bits/stdc++.h>
using namespace std;
const int row=3,column=2;
int matrix[row][column];
void printAntiClockwise(int row,int column)
{
     int startrow=0; // start of row
	int startcolumn=0; // start of column
	while(startrow<row && startcolumn<column)
	{
		for(int index=startcolumn;index<column;index++)
			cout<<matrix[startcolumn][index]<<" ";
		startrow++;
		for(int index=startrow;index<row;index++)
			cout<<matrix[index][column-1]<<" ";
	   column--;
	   if(startrow<row)
	   {
	   	for(int inn=column-1;inn>=startcolumn;inn--)
	   		cout<<matrix[row-1][inn]<<" ";
		row--;
	   }
	   if(startcolumn<column)
	   {
	   	for(int inn=row-1;inn>=startrow;inn--)
	   		cout<<matrix[inn][startcolumn]<<" ";
		   startcolumn++;
	   }
}
}
void printBackward(int row,int column)
{
	   int startrow=0; // start of row
	int startcolumn=0; // start of column
	while(startrow<row && startcolumn<column)
	{
		for(int index=column-1;index>=0;index--)
			cout<<matrix[startcolumn][index]<<" ";
		startrow++;
		for(int index=startrow;index<row;index++)
			cout<<matrix[index][startrow-1]<<" ";
	   column--;
	   if(startrow<row)
	   {
	   	for(int inn=startcolumn+1;inn<=column;inn++)
	   		cout<<matrix[row-1][inn]<<" ";
		row--;
	   }
	   if(startcolumn<column)
	   {
	   	for(int inn=row-1;inn>=startrow;inn--)
	   		cout<<matrix[inn][column]<<" ";
		   startcolumn++;
	   }
}
}
int main()
{
	cout<<"\n\nEnter the element of matrix:-\n";
	for(int outter=0;outter<row;outter++)
	for(int inner=0;inner<column;inner++)
		cin>>matrix[outter][inner];
	for(int outter=0;outter<row;outter++){
	for(int inner=0;inner<column;inner++)
		cout<<matrix[outter][inner]<<" ";
	cout<<"\n";
	}
	printAntiClockwise(row,column);
	cout<<"\n\n";
	printBackward(row,column);
    return 0;	
}
