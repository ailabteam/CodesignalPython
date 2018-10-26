def numberOfEvenDigits(n):
    e=0 
    while n:
        if n%2==0: e+=1 
        n/=10
    return e 


