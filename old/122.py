import lotto
a=eval(input('請輸入需要幾個中獎號碼： '))
b=eval(input('最大中獎號碼： '))
nums=lotto.lotto(n=a,m=b)
for i in range(a):
    for j in range(i,a,1):
        if nums[i]>nums[j]:
            box=nums[i]
            nums[i]=nums[j]
            nums[j]=box
print(nums)
