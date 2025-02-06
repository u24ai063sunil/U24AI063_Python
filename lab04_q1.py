def palindrome(s):
    if s==s[::-1]:
        return 0
    l2,l,count,i=list(s),len(s),0,0
    while l2!=l2[::-1]:
        if l2[i]!=l2[l-1-i]:        
            if ord(l2[i])>ord(l2[l-i-1]):
                l2[i]=chr(ord(l2[i])-1)
                
            else:
                l2[l-1-i]=chr(ord(l2[l-1-i])-1)
            count+=1
        else:
            i+=1          
    return count






T=int(input())
l1=[]
for i in range(T):
    l1.append(input())
for j in l1:
    print(palindrome(j))    
