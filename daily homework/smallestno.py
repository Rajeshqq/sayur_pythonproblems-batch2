def smallestno():
    numbers=[3,4,53,2,3,5]
    min=numbers[0]
    for i in range(1,len(numbers)):
        if min>=numbers[i]:
            min=numbers[i]
    print(min)

smallestno()