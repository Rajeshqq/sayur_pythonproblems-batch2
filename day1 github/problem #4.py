def check_same(first_word, second_word):
    #find the first letter of first word assigned to begin
    begin = second_word.find(first_word[0])
    #substring the second word start with begin and concat the words
    concat = second_word[begin:] + second_word[:begin]
    #check the firstword and concat are equal if equal print word is same else not same
    if first_word == concat:
        print("word is same")
    else:
        print("word is not same")

# Example usage:
first_word = "12345"
second_word = "23451"
check_same(first_word, second_word)


