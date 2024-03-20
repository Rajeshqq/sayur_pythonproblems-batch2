list=["good","god","abc","bca","ddd"]
freqoflist={}
count=1
def compareStrings():
    for i in range(len(list)):
        list[i]=removeduplicate(list[i])
        
    print(list)

def removeduplicate(list):
    removeddup=str(set(list))
    print(removeddup)
    res = ''.join(sorted(removeddup))
    return res

compareStrings()
