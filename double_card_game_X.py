import random,time,sys,string
from multiprocessing import Process
alfa=[]
ss=''

def f1():
     global ss
     choice=input('enter answer')
     if(choice==ss):
          print('right answer')
     else:
          print('wrong answer')
     while(1):
          x=input('\npress x to exit else to continue')
          if(x=='x'):
               break
          else:
               start()
     time.sleep(2)
     return

def start():
     global ss,alfa
     print('\n\nSYMBOL MATCH GAME')
     size=int(input('enter size of cards'))
     alfa=list(string.ascii_letters)
     card1=[0]*size
     card2=[0]*size
     pos1=random.randint(0,size-1)
     pos2=random.randint(0,size-1)
     ss=random.choice(alfa)
     alfa.remove(ss)
     card1[pos1]=ss
     card2[pos2]=ss
     i=0
     while(i<size):
          if(i!=pos1):
               card1[i]=random.choice(alfa)
               alfa.remove(card1[i])
          if(i!=pos2):
               card2[i]=random.choice(alfa)
               alfa.remove(card2[i])
          i=i+1
     print(card1)
     print(card2)     
     f1()
     

#start()    
     

