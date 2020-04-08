from random import choice
a=['黑桃','紅心','方塊','梅花']
b=['1','2','3','4','5','6','7','8','9','10','J','Q','K']
def poker():
    return choice(a)+choice(b)
