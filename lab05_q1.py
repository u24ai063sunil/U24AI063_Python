L=int(input())
R=int(input())
max_xor=0
for i in range(L,R+1):
    for j in range(L,R+1):
        if i^j>max_xor:
            max_xor=i^j
print(max_xor) 
