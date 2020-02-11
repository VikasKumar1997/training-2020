import random
import os
import sys
board=['-','-','-','-','-','-','-','-','-']
def display():
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print("-----------")
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("-----------")
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
def win():
    if (board[0] == 'X'and board[1]=='X' and board[2] == 'X') or (board[3] == 'X'and board[4]=='X' and board[5] == 'X') or (board[6] == 'X'and board[7]=='X' and board[8] == 'X'):
         print("user get wins")
         sys.exit(0)
    elif (board[0] == 'X'and board[3]=='X' and board[5] == 'X') or (board[1] == 'X'and board[4]=='X' and board[7] == 'X') or (board[2] == 'X'and board[5]=='X' and board[8] == 'X'):
         print("user get wins")
         sys.exit(0)
    elif (board[0] == 'X'and board[4]=='X' and board[8] == 'X') or (board[2] == 'X'and board[4]=='X' and board[6] == 'X'):
         print("user get wins")
         sys.exit(0)
    elif (board[0] == 'O'and board[1]=='O' and board[2] == 'O') or (board[3] == 'O'and board[4]=='O' and board[5] == 'O') or (board[6] == 'O'and board[7]=='O' and board[8] == 'O'):
         print("computer get wins")
         sys.exit(0)
    elif (board[0] == 'O'and board[3]=='O' and board[5] == 'O') or (board[1] == 'O'and board[4]=='O' and board[7] == 'O') or (board[2] == 'O'and board[5]=='O' and board[8] == 'O'):
         print("computer get wins")
         sys.exit(0)
    elif (board[0] == 'O'and board[4]=='O' and board[8] == 'O') or (board[2] == 'O'and board[4]=='O' and board[6] == 'O'):
         print("computer get wins")
         sys.exit(0)  
def playerchoice():
    for i in range(1,10):
        choice=int(input("enter your position:-"))
        if board[choice]=='-' and choice<9:
           board[choice]='X'
           break
        else:
            print("enter valid position")
            continue
def rowcheck():
    if (board[0]=='X' and board[2]=='X') or (board[0]=='X' and board[1]=='X') or (board[1]=='X' and board[2]=='X'):
        for index in range(0,3):
            if board[index]=='-':
                board[index]='O'
                return 1
            else:
                continue
    elif (board[3]=='X' and board[4]=='X') or (board[3]=='X' and board[5]=='X') or (board[4]=='X' and board[5]=='X'):
        for index in range(3,6):
            if board[index]=='-':
                board[index]='O'
                return 1
            else:
                continue
    elif (board[6]=='X' and board[7]=='X') or (board[6]=='X' and board[8]=='X') or (board[7]=='X' and board[8]=='X'):
        for index in range(6,9):
            if board[index]=='-':
                board[index]='O'
                return 1
            else:
                continue
    return 0
def coloumncheck():
    if (board[0]=='X' and board[3]=='X') or (board[6]=='X' and board[0]=='X') or (board[3]=='X' and board[6]=='X'):
        for index in range(0,7,3):
            if board[index]=='-':
                print(index)
                board[index]='O'
                return 1 
            else:
                continue
    elif (board[1]=='X' and board[7]=='X') or (board[1]=='X' and board[4]=='X') or (board[7]=='X' and board[4]=='X'):
        for index in range(1,8,3):
            if board[index]=='-':
                board[index]='O'
                return 1 
            else:
                continue
    elif (board[2]=='X' and board[5]=='X') or (board[5]=='X' and board[8]=='X') or (board[2]=='X' and board[8]=='X'):
        for index in range(2,9,3):
            if board[index]=='-':
                board[index]='O'
                return 1
            else:
                continue
    return 0
def diagonalcheck():
    if (board[0]=='X' and board[4]=='X') or (board[4]=='X' and board[8]=='X') or (board[0]=='X' and board[8]=='X'):
        for index in range(0,9,4):
            if board[index]=='-':
                board[index]='O'
                return 1 
            else:
                continue
    elif (board[6]=='X' and board[2]=='X') or (board[6]=='X' and board[4]=='X') or (board[2]=='X' and board[4]=='X'):
        for index in range(2,7,2):
            if board[index]=='-':
                board[index]='O'
                return 1
            else:
                continue
    return 0
def rowwin():
    if (board[0]=='O' and board[2]=='O') or (board[0]=='O' and board[1]=='O') or (board[1]=='O' and board[2]=='O'):
        for index in range(0,3):
            if board[index]=='-':
                board[index]='O'
                return 1
    elif (board[3]=='O' and board[4]=='O') or (board[3]=='O' and board[5]=='O') or (board[4]=='O' and board[5]=='O'):
        for index in range(3,6):
            if board[index]=='-':
                board[index]='O'
                return 1
    elif (board[6]=='O' and board[7]=='O') or (board[6]=='O' and board[8]=='O') or (board[7]=='O' and board[8]=='O'):
        for index in range(6,9):
            if board[index]=='-':
                board[index]='O'
                return 1
    return 0
def coloumnwin():
    if (board[0]=='O' and board[3]=='O') or (board[6]=='O' and board[0]=='O') or (board[3]=='O' and board[6]=='O'):
        for index in range(0,7,3):
            if board[index]=='-':
                board[index]='O'
                return 1
    elif (board[1]=='O' and board[7]=='O') or (board[1]=='O' and board[4]=='O') or (board[7]=='O' and board[4]=='O'):
        for index in range(1,8,3):
            if board[index]=='-':
                board[index]='O'
                return 1
    elif (board[2]=='O' and board[5]=='O') or (board[5]=='O' and board[8]=='O') or (board[2]=='O' and board[8]=='O'):
        for index in range(2,9,3):
            if board[index]=='-':
                board[index]='O'
                return 1
            else:
                continue
    return 0
def diagonalwin():
    if (board[0]=='O' and board[4]=='O') or (board[4]=='O' and board[8]=='O') or (board[0]=='O' and board[8]=='O'):
        for index in range(0,9,4):
            if board[index]=='-':
                board[index]='O'
                return 1
            else:
                continue
    elif (board[6]=='O' and board[2]=='O') or (board[6]=='O' and board[4]=='O') or (board[2]=='O' and board[4]=='O'):
        for index in range(2,7,2):
            if board[index]=='-':
                board[index]='O'
                return 1 
            else:
                continue
    return 0
def selfcheck(tag):
    if tag==0:
        tag=rowwin()
    if tag==0:
        tag=coloumnwin()
    if tag==0:
        tag=diagonalwin()
    if tag==0:
        for inner in [2,4,6,8]:
            if board[inner]=='-':
                board[inner]='O'
                tag=1
                break
    return tag
def computerchoice(flag):
    flag=selfcheck(0)
    if flag==0:
       flag=rowcheck()
    if flag==0:
       flag=coloumncheck()
    if flag==0:
       flag=diagonalcheck()
    win()
def main():
    index=2
    print("welcome in a game of tic tac toe")
    print("user choice is 'X'\ncomputer choice is 'O'")
    choice=int(input("enter your position:-"))
    if board[choice]=='-' and choice < 9:
        board[choice]='X'
    else:
        print("enter valid index")
    display()
    if board[4]=='-':
        board[4]='O'
    else:
        for choice in [2,4,6,8]:
                    if board[choice]=='-' and choice<9:
                       board[choice]='O'
                       flag=1
                       break
                    else:
                        continue
    display()
    while index<9:
        os.system('cls')
        if index%2==0:
            playerchoice()
            display()
            index=index+1
        else:
            computerchoice(0)
            display()
            index=index+1
    print("draw no one wins")
    value=input("you want to play more in (y/n)")
main()        
