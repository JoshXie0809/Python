def CtoF(degree_c):
    degree_f=1.8*degree_c+32
    return degree_f
temp_c=eval(input('請輸入攝氏溫度： '))
print(CtoF(temp_c))
