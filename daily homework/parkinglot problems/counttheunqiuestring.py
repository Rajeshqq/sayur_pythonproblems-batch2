lst=["good","god","abc","bca"]
freq={}

def checktrtheunqiue(lst):
    count=0
    for words in lst:
        dupremoved=set(words)
        check_Str="".join(sorted(dupremoved))
        if check_Str not in freq:
            freq[check_Str]=1
        else:
            freq[check_Str]+=1
            if freq[check_Str]==2:
                count+=1
    return count,freq
countoftheunqiue,freqofword=checktrtheunqiue(lst)
print("count of the word",countoftheunqiue)
        