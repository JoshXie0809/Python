def factorial(num=0):

    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

"""
m = int(input('m = '))
n = int(input('n = '))


print(factorial(m) // factorial(n) // factorial(m - n))
"""

""" function can obtain pre-set value"""
def roll_dice(n=2):
    from random import randint
    total=0
    for i in range(n):
        total+=randint(1,6)
    return total

"""
print(roll_dice())   
"""

"""roll_dice() -> pre-set : 2 dice"""

# * in front of the parameter, meaning parameter is changeable

def add(*n):
    total = 0
    for val in n:
        total +=val

    return total

"""

print(add(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
"""
# 最小公倍數&最大公因數
def gcd(x,y):
    
    (x,y) = (y,x) if x>y else (x,y)
    for i in range(x,0,-1):
        if x % i ==0 and y % i ==0:
            return i 

print(gcd(12130,104324))

def lcm(x,y):
    return x * y // gcd(x,y)

print(lcm(12344,65432))

def foo():
    b = 'hello'


    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()


def foo():
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100

def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100

