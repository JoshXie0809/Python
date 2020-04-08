n=eval(input('從1到n的整數：'))
for i in range(2,n+1,1):
    for j in range(2,i+1,1):
        if i//j==1:
            print(i,"is a prime number")
            break
        if i%j==0:
            print(i,'equal',j,'*',i//j)
            break
