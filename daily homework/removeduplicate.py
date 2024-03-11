def removeDuplicate():
    input1=input("enter the string : ")
    for i in range(0,2):
        if(i==0):
             print("with case sensitive :")
             words=input1.lower().split(" ")
        else:
             print("without case sensitive :")
             words=input1.split(" ")
        
        for eachWord in words:
            output=""
            for eachChar in eachWord:
                if eachChar not in output:
                    output+=eachChar
            print(output,end =" ")
        print("\n")
removeDuplicate()






