def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()



s1 = "hello, world!"
s2 = "hello, world!"

s3 = """
hello, 
world!
"""
print(s1, s2, s3)

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)





a=10
b=5
print('{0} * {1} = {2}'.format(a,b,a*b))
print('%d * %d = %d' % (a, b, a*b))





list1 = [1,3,5,7,100]
print(list1)
list2 = list1
## change value
list2[2]=300
print(list2)
for index, elem in enumerate(list1):
    print(index, elem)




list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
print(list1)
print(list2)
list3 = sorted(list1,key = len)
print(list3)




f = [x for x in range(1,10)]
print(f)


f = [x + y for x in 'ABCDE' for y in '1234567']
for i in f : print(i)

import sys
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))
print(f)




import time
import os

def main():
    content = 'ZARD!!! ZARD!!! ZARD!!! I love U!!!'
    while True:

        
        #clear_output() # os.system('clear')
        os.system('clear')

        print(content)

        
        content = content[1:] + content[0]
        time.sleep(0.3)

if __name__ == '__main__':
    main()
 