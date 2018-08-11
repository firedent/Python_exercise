import fractions
L=[1,2,2,3,5,9,8,6,]
L1=sorted(L)#排序
L2=list(set(L1))#去重
L3=[]
print(L2)
for i in range(1,len(L2)):
    for n in range(0,i+1):
       L3=fractions.Fraction(L2[i-n],L2[i])


print(L3)