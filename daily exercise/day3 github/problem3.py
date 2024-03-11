#From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
#for each word. Write this information at the end of file under the heading "Summary of 4 letter words"

try:
    with open("E:\\sayur python batch-2\\day3\\input.txt", "r") as file:
        sentence = file.read()
        print(sentence)
except IOError:
    print("Error: doesn't have a file" )
words = sentence.lower().split(" ")

occurences={}

incr=0
for j in range(len(words)):
    if len(words[j])==4:
         occurences[words[j]]=0
for i in range(len(words)):
         if words[i] in occurences:
            incr=occurences.get(words[i])
            incr+=1
            occurences[words[i]]=incr
        


print("summary")
for keys,values in occurences.items():
     print(f"{keys} : {values}")
     