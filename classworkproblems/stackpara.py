input =")("
stack=[]
for i in input:
    if i=='(':
       stack.append(i)
    elif i==')':
        if(len(stack)!=0):
            stack.pop()
        else:
            stack.append(i) 
        
if len(stack)==0:
    print("true")
else:
    print("false")


