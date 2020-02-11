dict={'a':['V','I','K'],'c':['B','O'],'b':['U','P'],'ab':['L']}
x=len(dict)
lis=[] 
def main():
    n=2
    v=input("enter your input:-")
    l=len(v)
    for i in v:
        lis.append(dict[i])
    o=[(v[i:i+n])for i in range(0,len(v),n)]
    for i in o:
        if i=='ab':
           lis.append(dict[i])
    print(lis)
main()
