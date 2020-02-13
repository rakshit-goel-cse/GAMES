import sys,time,os
l=[['*',1,2,3],[1,' ',' ',' '],[2,' ',' ',' '],[3,' ',' ',' ']]
x,c,r=0,0,0
def start():
     global l
     l=[['*',1,2,3],[1,' ',' ',' '],[2,' ',' ',' '],[3,' ',' ',' ']]
     print('\n    lets play TIC TAC TOW\n\n')
     show()
     p1()
     
def p1():
     print('enter position player 1')
     get()
     #X for p1
     global l,x,c,r
     if(l[x][c]==' '):
          l[x][c]='X'
     else:
          print('try again\n')
          p1()
     os.system('cls')
     show()
     check()
     if(r!=0):
          return
     p2()

def p2():
     print('enter position player 2')
     get()
          #O for p2
     global l,x,c,r
     if(l[x][c]==' '):
          l[x][c]='O'
     else:
          print('try again\n')
          p2()
     os.system('cls')
     show()
     check()
     if(r!=0):
          return
     p1()

def show():
     global l
     print('  -------------------\n',end='   | ')
     for i in range(0,4):
          for j in range(0,4):
               print(l[i][j],end=' | ')
          print()
          print('  -------------------\n',end='   | ')
     print('\b\b \n')
          
def get():
     global x,c
     try:
          x=int(input('ROW '))
          c=int(input('COLLUM '))
     except:
          print('wrong input')
          get()
     if(x<4 and c<4):
          return
     else:
          print('out of range\n')
          get()

def check():
     global l
     q=0
     if(l[1][1]==l[1][2]==l[1][3]=='O'or l[2][1]==l[2][2]==l[2][3]=='O' or l[3][1]==l[3][2]==l[3][3]=='O' or l[1][1]==l[2][1]==l[3][1]=='O' or l[1][2]==l[2][2]==l[3][2]=='O' or l[1][3]==l[2][3]==l[3][3]=='O' or l[1][1]==l[2][2]==l[3][3]=='O' or l[1][3]==l[2][2]==l[3][1]=='O'):
          print('player 2 wins\n')
          play()
     elif(l[1][1]==l[1][2]==l[1][3]=='X' or l[2][1]==l[2][2]==l[2][3]=='X' or l[3][1]==l[3][2]==l[3][3]=='X' or l[1][1]==l[2][1]==l[3][1]=='X' or l[1][2]==l[2][2]==l[3][2]=='X' or l[1][3]==l[2][3]==l[3][3]=='X' or l[1][1]==l[2][2]==l[3][3]=='X' or l[1][3]==l[2][2]==l[3][1]=='X'):
          print('player 1 wins\n')
          play()
     for i in range(1,4):
          for j in range(1,4):
               if(l[i][j]==' '):
                    q=q+1
                    break
     if(q==0):
          print('DRAW\n')
          play()

     
def play():
     global r
     q=input('press y to play more else any key to exit').lower()
     if(q=='y'):
          start()
     else:
          print('\nOK BYE')
          r=r+1
          time.sleep(2)
          
#start()
