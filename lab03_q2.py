def fibo(N):
    a,b,sum=0,1,1
    list2=[0,1]
    while sum<N:
        sum=a+b
        list2.append(sum)
        a,b=b,sum
    if N in list2:
        return "IsFibo"
    else:
        return "IsNotFibo"    

T=int(input())
list1=[]
for i in range(T):
    list1.append(int(input()))
for j in list1:
    print(fibo(j))    
