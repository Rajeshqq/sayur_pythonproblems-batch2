# #problem #4
# #write a program to find if two strings are same.
# two string are considered same if both strings have same letters in same order, but from different starting point
# eg abcd is same as bcda (a is moved to the right)
# abcd is same as cdab 
# abcd is  not same as cdba
def check_same(first_word, second_word):
    count=0
    #find the first letter of first word assigned to begin
    for i in range(0,len(second_word)-1):
        if second_word[i]==first_word[0]:
          begin=i
          count+=1
          if(i!=0 and count>=1):
              break
    #substring the second word start with begin and concat the words
    concat = second_word[begin:] + second_word[:begin]
    #check the firstword and concat are equal if equal print word is same else not same
    if first_word == concat:
        print("word is same")
    else:
        print("word is not same")


# Example usage:
first_word = "1111122345"
second_word ="1122345111"
check_same(first_word, second_word)


