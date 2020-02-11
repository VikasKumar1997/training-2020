dict={'a':['V','I','K'],'c':['B','O'],'b':['U','P'],'ab':['L'],'d':['1','3','5']}
lis=[]
combination='ab'
def cartesianProduct(setA, setB): 
    result =[] 
    for i in range(0, len(setA)): 
        for j in range(0, len(setB)): 
            if type(setA[i]) != list:          
                setA[i] = [setA[i]]
            temp = [num for num in setA[i]]
            temp.append(setB[j])              
            result.append(temp)          
    return result   
def Cartesian(tempList, size): 
    temp = tempList[0] 
    for index in range(1, size): 
        temp = cartesianProduct(temp, tempList[index])       
    print(temp)  
def main():
    value=input("enter your input:-")
    for index in value:
        lis.append(dict[index])
    size=len(lis)
    Cartesian(lis,size)
    li=[]
    for index in value:
        if index not in combination:
            li.append(dict[index])
    li.append(dict[combination])
    size=len(li)
    Cartesian(li,size)
main()
