import os
import sys
use=[]
messag=[]
dedicated=[]
brickList=[]
countryList=[]
cityList=[]
count=1
admin="vikas kumar"
wall=[]
list=[]
class brick:
    global count
    def __init__(s,name,message,dedicate):
        s.message=message
        s.dedicate=dedicate
        s.name=name
        dedicated.append(s.dedicate)
        s.com=[]
        s.report=0
        s.city='agra'
        s.country='india'
class wall:
    global count
    def wallIsFill(s):
        lenght=len(brickList)
        if lenght==90:
           wall[count].append('full')
           count=count+1
class city:
    def __init__(s,name):
        s.city=name
    def wallCheck(s):
        for index in wall:
            if index=='full':
                print()
class country:
    def __init__(s,name):
        s.country=name
#class world:
          
class user:
    def __init__(s,name):
        s.name=name
        use.append(s.name)
        message=input("enter your message:-")
        dedicate=input("enter the dedicated person:-")
        brickList.append(brick(s.name,message,dedicate))
    def comment(s):
        value=input("enter your comment:-")
        s.comment.append(value)
    def edit(s):
        change=input("enter a new message:-")
        s.dedicate=change
    def report(s):
        s.report=s.report+1
class admin(user):
    def adminEdit(s):
        value=input("enter the new message:-")
        s.dedicate=value
def show():
    '''country=input("enter country name:-")
    city=input("enter a city name:-")
    wallId=input("enter wall no.:-")'''
    for index in brickList:
         print("from=",index.name)
         print("           ",index.message)
         print("                     to:=",index.dedicate)
         print("comment=",index.com,"        report=",index.report)
         print("city=",index.city,"          country=",index.country)
def main():
   y=0
   x=0
   result=True
   countryList.append(country('america'))
   countryList.append(country('pakistan'))
   countryList.append(country('india'))
   cityList.append(city('newyork'))
   cityList.append(country('karachi'))
   cityList.append(country('agra'))
   while(result):
       flag=0
       show()
       name=input("\nenter your name:-")
       if name==admin:
               print("welcome admin.\n1. comment on any brick\n2. edit any brick\n3. exit from code")
               choice=int(input("\nenter your choice:-"))
               if choice==1:
                 val=int(input("enter the no. of brick:-"))
                 list[val-1].comment(com) 
               elif choice==2:
                  val=int(input("enter the no. of brick:-"))
                  list[val-1].edit(d)
               else:
                   break
       for index in use:
           if name==index:
               flag=1
               print("welcome again.\n1. wanna dedicate someone\n2. comment on any brick\n3. edit own brick")
               choice=int(input("\nenter your choice:-"))
               if choice==1:
                 list.append(user(name))
               elif choice==2:
                 val=int(input("enter the no. of brick:-"))
                 list[val-1].comment(com) 
               elif choice==3:
                  d=input("enter your new dedicate:-")
                  l=len(use)
                  for inner in range(0,l):
                      if use[inner]==name:
                          list[inner].edit(d)
                          break
               else:
                   c=False
       if flag==0:
           list.append(user(name))
   temp=set(dedicate)
   for index in temp:
       t=dedicate.count(index)
       if y<t:
           y=t
   for index in temp:
       w=dedicate.count(index)
       if w==y:
           print("hottest person is:-",index)
           break
   for i in use:
       for j in temp:
           if i==j:
               x=1
       if x==0:
           print("person's who didn't get any dedication is:-",i)
main()
