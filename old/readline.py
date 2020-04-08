import numpy as np

b = ' '
c = []
a = open("/Users/xiezhengqi/Desktop/Josh.txt", "r+")
while b != '':
    b = a.readline()
    c.append(b)
a.close()
d = "一般行政"
e = []
for i in range(8, len(c), 7):
    if i+1 < len(c):
        e.append(str(c[i+1]))
for i in e:
    print(i, end='')