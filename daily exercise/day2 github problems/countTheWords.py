#Write a program that reads a passage or string and counts the occurrences of two consecutive words 
#that are the same without any other specific word in between.
 #For example, count the occurrences of "apple apple" but not "apple orange apple."
def countwords():
    sentence="apple apple but not apple apple ."
    word=[]
    occurrenceCount=0
    word=sentence.split(" ")
    print(len(word))
    for i in range(0,len(word)-1):
        if word[i]==word[i+1]:
            occurrenceCount+=1
    print(occurrenceCount)    

countwords()