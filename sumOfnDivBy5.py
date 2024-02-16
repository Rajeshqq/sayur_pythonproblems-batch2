def sumofDiv(n):
    sum=0
    for i in range(1,n):
        if(i%5==0):
            sum+=i
            print(i," ",end='')
    print("=",sum)     
sumofDiv(100)