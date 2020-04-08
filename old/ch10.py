n1=eval(input('請輸入sample_1的抽樣數'))
n2=eval(input('請輸入sample_2的抽樣數'))
a1=eval(input('請輸入sample_1的standard deviation'))
a2=eval(input('請輸入sample_2的standard deviation'))
x1=eval(input('請輸入sample_1的mean'))
x2=eval(input('請輸入sample_2的mean'))
D=eval(input('請輸入u1-u2'))
za=eval(input('請輸入1.645or1.96'))

c=D+za*pow(a1*a1/n1+a2*a2/n2,0.5)
if x1-x2>c:
    print('h0 can ce rejected','c=',c)
else:
    print('ho cannot be rejected','c=',c)


