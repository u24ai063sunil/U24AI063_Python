def height(N):
    H=1
    for i in range(N):
        if i%2:
            H+=1
        else:
            H=2*H    
    return H

T=int(input())
if T>10 or T<0:
    print("**invalid test cases**")
    exit()
else:
    list1=[]
    for i in range(T):
        list1.append(int(input()))
for j in list1:
    print(height(j))
