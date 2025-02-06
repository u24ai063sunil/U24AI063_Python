def sher_sq(A,B):
    count=0
    for i in range(A,B+1):
        if (i**0.5)%1 == 0.0:
            count+=1
    return count       

T=int(input())
l1,l2=[],[]
for i in range(T):
    l1.append(int(input()))
    l2.append(int(input()))
for j in range(T):
    print(sher_sq(l1[j],l2[j]))  

