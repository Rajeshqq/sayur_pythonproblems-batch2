#Problem #1
#write a program that reads a passage and reverses the order of 
#letters in each word while keeping the word order intact. Use function.
#Eg- input - I am Sayur
#Output I ma ruyaS

def revTheEachWord(input):

    words=input.split(" ")
    for i in range(0,len(words)):
      
       rev=words[i]
       lenofword=len(rev)-1
       while(lenofword>=0):
              print(rev[lenofword],end="")
              lenofword-=1

       print(" ",end="") 
    
revTheEachWord("I am Sayur")