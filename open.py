import rps,tic,double_card_game_X,raja_vajeer,sys,time,os


def start():
     print('1-rock paper scissors\n2-double card game\n3-tic tac toe\n4-raja vajeer')
     i=int(input('enter your choise\n'))
     if(i==1):
          rps.start()
     elif(i==2):
          double_card_game_X.start()
     elif(i==3):
          tic.start()
     elif(i==4):
          raja_vajeer.start()
     else:
          print('wrong choise')
     os.system('cls')
     finish()

def finish():
     q=input('press y to play more else any key to exit').lower()
     if(q=='y'):
          start()
     else:
          print('\nOK BYE')
          time.sleep(2)
          sys.exit()
start()
