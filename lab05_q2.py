def choco(k):
    n=k//2
    if k%2:
        return n*(n+1)
    else:
        return n**2    

T=int(input())
list1=[]
for i in range(T):
    list1.append(int(input()))
for i in list1:
    print(choco(i))