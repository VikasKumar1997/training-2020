import os
import sys
#import json
shopList=[]
bookList=[]
class book:
    def __init__(s,name,author):
        s.name=name
        s.author=author
class shop:
    def __init__(s,name,owner):
        s.name=name
        s.owner=owner
    def createBookList(name,author):
        bookList.append(book(name,author))
class response:
    def createBookList(name,owner):
        shopList.append(shop(name,owner))
    def validateJson(value):
        stack=[]
        lenght=len(value)
        for index in range(0,lenght):
            if value[index]=='{':
                stack.append(value[index])
                continue
            elif value[index]=='[':
                stack.append(value[index])
                continue
            elif value[index]=='}':
                if len(stack)==0:
                    return False
                else:
                    ele=stack.pop()
                    if ele!='{':
                     return False
                continue
            elif value[index]==']':
                if len(stack)==0:
                    return False
                else:
                    ele=stack.pop()
                    if ele!='[':
                     return False
                continue
            elif value[index]=='"':
                ele=stack[-1]
                if ele=='"':
                    if value[index+1]!=':' and value[index+1]!=',' and value[index+1]!='}':
                        return False
                    if value[index+1]==':' or value[index+1]==',':
                        if value[index+2]!='"' and value[index+2]!='{' and value[index+2]!='[' and type(value[index+2])!=str:
                            return False
                    stack.pop()
                else:
                    stack.append(value[index])
        if len(stack)==0:
          return True
        else:
          return False
def main():
    result=True
    curly=0
    square=0
    index=0
    temp=''
    value=input("Enter your string:-")
    for outter in value:
        if outter==' ':
            continue
        else:
            temp=temp+outter  #temprary string is gonna stored after removing space
    obj1=response
    print(obj1.validateJson(temp))
    #t=json.loads(temp)
    #print("\n\n",t)      
main()
