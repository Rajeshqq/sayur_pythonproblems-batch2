def secondSmallestNo(numbers):
    length=len(numbers)
    firstsmall=numbers[0]
    secondSmall=0
    for i in range(1,length):
        if firstsmall>=numbers[i]:
            secondSmall=firstsmall
            firstsmall=numbers[i]
            
        elif secondSmall>=numbers[i]:
             secondSmall=numbers[i]
       
    print(secondSmall)
    print(firstsmall)


secondSmallestNo([8,4,1,5,3,6,2])       