def pan_gram(a):
    b=set()
    for i in a:
        if(i.isalpha()):
            b.add(i)
    if len(b)==26:
        return "pangram"
    else:
        return "not pangram"
    
Sent=input()
print(pan_gram(Sent))
