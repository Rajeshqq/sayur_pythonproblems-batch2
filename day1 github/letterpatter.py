#previous contain the previous printed letters
previous=""
#assigned the "a" to letter
letter='a'
#print the letter until g
while(letter<='g'):
    #concat the previous front and back of the letter 
    previous=previous+letter+previous
    #increament the letter
    letter=chr(ord(letter)+1)
    print(previous)
    
    
