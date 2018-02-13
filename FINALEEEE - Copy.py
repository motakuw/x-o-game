def showboard():

    print(board[0],'|',board[1],'|',board[2])
    print(board[3],'|',board[4],'|',board[5])
    print(board[6],'|',board[7],'|',board[8])

board=[0,1,2,3,4,5,6,7,8]
print("LET'S START!!")

a=input(str("Player 1, what's your name??  "))
b=input(str("Player 2, what's your name??  "))

print(a, 'is X and' ,b, 'is O, Ok?? :D ')

showboard()

def checkboard():
    
             if  (board[0]=='x'and board[1]=='x'and board[2]=='x') or(board[3]=='x'and board[4]=='x'and board[5]=='x')or(board[6]=='x'and board[7]=='x'and board[8]=='x')or(board[0]=='x'and board[3]=='x'and board[6]=='x')or(board[1]=='x'and board[4]=='x'and board[7]=='x')or(board[2]=='x'and board[5]=='x'and board[8]=='x')or(board[0]=='x'and board[4]=='x'and board[8]=='x')or(board[2]=='x'and board[4]=='x'and board[6]=='x'):
               print('WINNER IS ',a, ' \(^O^)/')
                   break
               
             elif(board[0]=='o'and board[1]=='o'and board[2]=='o')or(board[3]=='o'and board[4]=='o'and board[5]=='o')or(board[6]=='o'and board[7]=='o'and board[8]=='o')or(board[0]=='o'and board[3]=='o'and board[6]=='o')or(board[1]=='o'and board[4]=='o'and board[7]=='o')or(board[2]=='o'and board[5]=='o'and board[8]=='o')or(board[0]=='o'and board[4]=='o'and board[8]=='o')or(board[2]=='o'and board[4]=='o'and board[6]=='o'):
                print('WINNER IS ',b, ' \(^O^)/')
                

def repeatP1():
        print(a,(' Please pick a spot(0-8):'))
        P1=int(input())        
        if board[P1]!='x' and board[P1]!='o':
            board[P1]='x'
            showboard()
        else:
            print("oops! it's taken!!")
            repeatP1()

def repeatP2 ():
        print(b,(' Please pick a spot(0-8):'))
        P2=int(input())
        if board[P2]!='x' and board[P2]!='o':
           board[P2]='o'
           showboard()
        else:
            print("oops! it's taken!!")
            repeatP1()

z=0            
while True :
    print(a,(' Please pick a spot(0-8):'))
    P1=int(input())
    if board[P1]!='x' and board[P1]!='o':
        board[P1]='x'
        checkboard()
        showboard()
    else:
        print("oops! it's taken!!")
        repeatP1()
    check = True
    for i in range (9) :
        if board[i] != "x" and board[i] != "o" :
            check = False
            break
    if check == True :
        break
        
    print(b,(' Please pick a spot(0-8):'))
    P2=int(input())
    if board[P2]!='x' and board[P2]!='o':
        board[P2]='o'
        checkboard()
        showboard()
    else:
        print("oops! it's taken!!")
        repeatP2()
      
print("IT'S A DRAW!!!! \\(*____*)//")
