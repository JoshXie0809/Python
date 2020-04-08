import random
def lotto(n,m):
    num=[]
    for i in range(m):
        num.append(i+1)
    prize=[]
    for i in range(n):
        a=random.choice(num)
        prize.append(a)
        num.remove(a)
    
        
    return prize

