input="hello world"
words=input.split(" ")
for i in range(len(words)):
    length=len(words[i])-1
    rev=""
    while(length>=0):
        rev+=words[i][length]
        length-=1
    words[i]=rev  
print(words)