# Longest word in a sentence
#Input: Python is a powerful programming language
#Output: programming
sentence="Python is a power progr langu"
words=sentence.split(' ')

max=len(words[0])
theword=words[0]
for i in range(len(words)-1):
    
    lengthofeachword=len(words[i+1])
    if(max<=lengthofeachword):
        max=lengthofeachword
        theword=words[i+1]
    
print(max)
print(theword)   
    
