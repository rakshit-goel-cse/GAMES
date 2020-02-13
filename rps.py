import random,time
comp=['r','p','s']
c=0
u=''

def enter():
     global u,c
     c=(random.randint(0,20))%3
     print('enter\n*R for rock\n*P for paper\n*S for scisser')
     u=input('enter your choise\n').lower()
     print('computer move *',comp[c])
#all comparisions from now
def compare():
     
     if(comp[c]==u):
          print('draw')
     elif(comp[c]=='r' and u=='p'):
          print('you won')
     elif(comp[c]=='p' and u=='s'):
          print('you won')
     elif(comp[c]=='s' and u=='r'):
          print('you won')
     elif(comp[c]=='r' and u=='s'):
          print('you loss')
     elif(comp[c]=='p' and u=='r'):
          print('you loss')
     elif(comp[c]=='s' and u=='p'):
          print('you loss')
     else:
          print('wrong entry')
def start():
     print("ROCK PAPER SCISSORS")
     while(1):
          enter()
          compare()
          w=input('want to play again:-\npress x to exit or any key to continue').lower()
          if(w=='x'):
               break
          time.sleep(2)
#start()
