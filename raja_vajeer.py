import random

p=[0,0,0,0]
n=('p1','p2','p3','p4')

def raja(v):
     print('\n\b',n[v],' is Raja\nRaja:where is my vajeer')
     p[v]+=1000
def vajeer(v):
     print(n[v],' is vajeer\nvajeer:here sir\nRaja:chor sipahi ka pata lagao')
     p[v]+=500
     return(input('Enter player who is chor\n').lower())
def chor(v,ans,vj):
     if(ans==n[v]):
          print('Right answer vajeer\n')
     else:
          print('wrong answer vajeer\n')
          p[vj]-=500
          p[v]+=500
     print(n[v],' is chor')
def sipahi(v):
     print(n[v],' is sipahi')
     p[v]+=100


def ran():
     a=random.choice(po)
     po.remove(a)
     return(a)
  
def point():
     for i in range(0,4):
          print(n[i],'has points',p[i])
     if('x'==input('\n\nwant to exit\npress x to exit\n').lower()):
          return
     else:
          start()

def start():
     print('players-p1,p2,p3,p4')
     global po
     po=[0,1,2,3]
     vj,ans='',''
     raja(ran())
     vj=ran()
     ans=vajeer(vj)
     chor(ran(),ans,vj)
     sipahi(ran())
     point()
#start()
