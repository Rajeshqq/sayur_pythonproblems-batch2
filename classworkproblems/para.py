#balancing the paranthesis
#input="((q))("


def paracheck(input):
    open=0
    close=0
    #it check the last character of the input if it is close para it return 0
    if(input[len(input)-1]=='(' or input[0]==')'):
           return 0
    for i in range(len(input)):
    
        
        if(input[i]=='('):
            open+=1
        elif(input[i]==')'):
            close+=1

    if(open==close  and open!=0):
                
        return 1
                
    else:
        return 0
input="())(()"
answer=paracheck(input)
if(answer==1):
    print("true")
else:
    print("false")   
                        
