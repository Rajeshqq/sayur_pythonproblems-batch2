#if the previous frogs size is lesser than the current frog it eat whole previous frog
frog = [1,2,5,3,2,1,8,9,10,3,2,5,1]  
#frog=[2,1,5]
#frog=[1,3,4,5,6,7,10,1,2]
#frog=[1,1,1,1]



i = 1 
while True: 
    if i >= len(frog):  
        break 
    
    if frog[i] > frog[i - 1]: 
        
        frog = frog[0:i-1]+frog[i:]   
        i = 1
    else:
        i += 1  

print(frog)

# #it eat  just eat the previous one of the frog if it is lesser in size frog(i) eat frog(i-1)
# #frog= [1,2,5,7,3,2,2]
# #frog= [5,2,5,7,3,2,2]
# frog=[1,1,1,5]
# #frog = [1,2,5,3,2,1,8,9,10,3,2,1]  
# #frog=[1,2,3,4,5]

# alive_frog=[0]
# for i in range(0,len(frog)):
#     if(frog[i]>frog[i-1]):
#         if(frog[i]>alive_frog[len(alive_frog)-1] ):
#             #alive_frog.pop()
#             #alive_frog.append(frog[i])
#             alive_frog[len(alive_frog)-1]=frog[i]
#     else:
#         if(alive_frog[0]==0):
#             alive_frog[0]=frog[i]
#         else:
#              alive_frog.append(frog[i])
# print(alive_frog)


# #bonus problem

# #frog=[1,2,3,4,5]
# alive_frog=[0]
# for i in range(0,len(frog)):
#     if(frog[i]>frog[i-1]):
#         frog[i]+=frog[i-1]
#         if(frog[i]>alive_frog[len(alive_frog)-1]):
#             alive_frog[len(alive_frog)-1]=frog[i]
#     else:
#         if(alive_frog[0]==0):
#             alive_frog[0]=frog[i-1]
#         else:
#             alive_frog.append(frog[i])
# print(alive_frog)

