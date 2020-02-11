#include<bits/stdc++.h>
using namespace std;
class StringUtils
{
	public:
	static int countChar(char str[100],char ch){
		int len=strlen(str),count=0;
		for(int index=0;index<len;index++)
		{
			if(str[index]==ch)
			count++;
		}
		return count;
	}
	static bool substring(char str[100],int start,int end){
		int len=strlen(str),count=0;
		char temp[100];
	if(start<0 || end>len)
	  return false;
	else
		for(int index=start;index<=end;index++)
		{
		  temp[count]=str[index];
		  count++;
	}
	puts(temp);
	return true;
	}
	static void split(char str[100],char ch){
		int len=strlen(str),count=0;
		char temp[100];
		for(int index=0;index<len;index++)
		{
			if(str[index]==ch)
			{
				temp[count]=' ';
				count++;
			}
			else
			{
				temp[count]=str[index];
				count++;
			}
		}
		for(int in=0;in<len;in++)
		cout<<temp[in];
		cout<<"\n\n";
	}
	static bool hasPattern(char str[100],string pattern){
		int len=strlen(str),check=0,flag=0,t;;
		int len1=0;
		for(int outter=0;pattern[outter]!='\0';outter++)
		len1++;
		char temp=pattern[0];
		for(int index=0;index<len;index++)
		{
		if(temp==str[index])
		{
			flag=0;
			t=index;
			if((len-index)>=len1)
			{
		      for(int in=0;in<len1;in++)
	            if(pattern[in]==str[t])
	            {
	              flag++;
	              t++;
	        }
	        else
	        break;
	        }
	    }
	}
if(flag==len1)
	return true;
else
  return false;	 
}	 
	static bool allWordsContainChar(char str[100],char ch){
		int len=strlen(str),flag=0;
	string test[10];
	int count=0,i=0;
	for(int index=0;index<len;index++)
	{
		if(str[index]!=' ')
		{
		test[i][count]=str[index];
		count++;
	}
	else
	{
	i++;
	count=0;
}
}
	for(int index=0;index<=i;index++)
	for(int outter=0;outter<10;outter++)
	  if(test[index][outter]==ch)
	  {
	      flag++;
	      break;
	  }
	  if(flag==i+1)
	   return true;
	  else
	    return false;
  }
};
int main()
{
	char str[100],ch;
	bool result1,result2,result3;
	int choice,count,start,end,size;
	StringUtils ob;
	cout<<"Enter a string:-";
	gets(str);
	while(true)
	{
		cout<<"\n\n";
		cout<<"1. count character\n2. sub string\n3. split\n4. pattern match\n5. all word contain character\n\n\nEnter your choice:-";
		cin>>choice;
		switch(choice)
		{
			case 1:
				cout<<"Enter a character:-";
				cin>>ch;
			    count=ob.countChar(str,ch);
			    cout<<"charcatered occur no. of times:-"<<count<<"\n\n";
			    break;
			case 2:
				cout<<"please enter starting point:-";
				cin>>start;
				cout<<"please enter end point:-";
				cin>>end;
				result3=ob.substring(str,start,end);
				if(result3==false)
				cout<<"enter valid cordinates\n\n";
				break;
			case 3:
				cout<<"Entered a character:-";
				cin>>ch;
				ob.split(str,ch);
				break;
			case 4:
				{
				string pattern;
				cout<<"enter a pattern:-";
				cin>>pattern;
				result1=ob.hasPattern(str,pattern);
				if(result1==true)
				cout<<"pattern match\n\n";
				else
				cout<<"pattern didn't match\n\n";
				break;
			}
			case 5:
				cout<<"Entered a character:-";
				cin>>ch;
				result2=ob.allWordsContainChar(str,ch);
				if(result2==true)
				cout<<"all words contain character\n\n";
				else
				cout<<"all words not contain character\n\n";
				break;
			default:
				cout<<"enter valid input";
				exit(0);
		}
	}
}
