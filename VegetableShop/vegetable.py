import random
import os
import sys
vegetableList={1: 'onions',2: 'patato',3: 'tomato',4: 'brinjal',5: 'capsicum',6: 'ladyfinger',7: 'membership'}
normalAmount=[80,60,40,25.25,12.50,10]
discountAmount=[60,40,20,12.5,7.25,5]
employees=["SAHIL","RAMESH","RAJESH","ANKIT"]
preffered=[]
class vegetable:
    def __init__(s,name):
        s.name=name
        s.clerk=random.choice(employees)
        s.itemlist=[]
        s.quantity=[]
        s.rupees=[]
        s.total=0
        s.discount=0
    def additem(s):
        print("1. onion 80rs/kg\n2. patato 60rs/kg\n3. tomato 40rs/kg\n4. brinjal 25.25rs/kg\n5. capsicum 12.50rs/kg\n6. lady finger 10rs/kg\n")
        value=int(input("Enter your choice-: "))
        weight=float(input("Enter your quantity in KG-: "))
        s.quantity.append(weight)
        s.itemlist.append(value)
        s.rupees.append(normalAmount[value-1]*weight)
        s.total=float(s.total+(normalAmount[value-1]*weight))
    def recipt(s):
        print("-----------------------HAVE A GOOD DAY SIR----------------------\nthank for visting:=",s.name,"\n")
        print("S No.   ||    item    ||   quantity   ||   Rs.   ")
        count=0;
        for index in s.itemlist:
            print(count+1 , "          " , vegetableList[index] , "        " , s.quantity[count] , "         " , s.rupees[count] , "   ")
            count=count+1
        print("Total=",s.total, "    Your Helper=",s.clerk, "   discount=",s.discount) 
    def member(s):
        s.itemlist.append(7)
        s.rupees.append(50)
        s.quantity.append(0)
        preffered.append(s.name)
        s.total=s.total+50
        print("\nThankx for taking membership fro now you are our preffered customer you get discount on our shop items\n")
class discount(vegetable):
    def  __init__(s,name):
      super(discount,s).__init__(name)
    def disadd(s):
        print("1. onion 60rs/kg\n2. patoato 40rs/kg\n3. tomato 20rs/kg\n4. brinjal 12.5rs/kg\n5. capsicum 7.25rs/kg\n6. lady finger 5rs/kg\n")
        value=int(input("Enter your choice-: "))
        weight=float(input("Enter your quantity in KG-: "))
        s.quantity.append(weight)
        s.itemlist.append(value)
        s.rupees.append(normalAmount[value-1]*weight)
        s.total=float(s.total+(normalAmount[value-1]*weight))
        s.discount=s.discount+(normalAmount[value-1]-discountAmount[value-1])
def main():
    while True:
       flag=0
       print("Welcome to vegetable shop \n")
       name=input("Enter your name:-")
       if name=="admin":
           sys.exit(0)
       object1=discount(name)
       for index in preffered:
            if index==name:
                flag=1
                print("Welcome again you are our preffered customer you get some benfits on our items")
                while True:
                    print("1. add item\n2. recipt\n3. exit")
                    choice=input("enter your choice-: ")
                    if choice=='1':
                        object1.disadd()
                    elif choice=='2':
                        object1.recipt()
                    else:
                        break
                break
       if flag==0:   
        while True:
            print("1. add item\n2. membership\n3. PrintRecipt\n4. exit")
            choice=input("Enter your choice-: ")
            if choice=='1':
                object1.additem()
            elif choice=='2':
                object1.member()
            elif choice=='3':
                object1.recipt()
            else:
                break
main()

        

     
