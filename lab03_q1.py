def digital_root(n):
    while(n>9):
        num,sum,q=n,0,0
        while num!=0:
            q=num%10
            sum+=q
            num//=10
        n=sum    
    return n
 
num=int(input("enter the number:"))
print("The digital root of the number is:")
print(digital_root(num))
    

