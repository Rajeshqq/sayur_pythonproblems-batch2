eg=[1,1,1,1,1,2,2,3,3,4,4,5,5,5,5,5,5,8,8,7,7,7,7,7,7,7,7,7,7,7,7]
k=4
dictt={}
li=[]
for x in eg:
    if str(x)  not in dictt:
        dictt[str(x)]=1
    else:
        count=dictt.get(str(x))+1
        dictt[str(x)]=count

sorted_dict = {}
for key in sorted(dictt, key=dictt.get,reverse=True):
    sorted_dict[key] = dictt[key]
 
print(sorted_dict)
   
li = [int(key) for key in sorted_dict.keys()][:k]
print(li)
    
