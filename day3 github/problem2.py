
def check(words, middle_letter):
    return middle_letter in words

def targetedWord():
    try:
        with open('input.txt', 'r') as file:
            sentence = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    words = sentence.lower().split()
    target_word = "the"
    check_sentence = []
    count = 0
    
    i = 0
    while i < len(words):
        if words[i] == target_word:
            check_sentence.append(words[i])
            
            for j in range(i + 1, len(words)):
                check_sentence.append(words[j])
                
                if words[j] == target_word:
                    if not check(check_sentence, "a"):
                        count += 1
                    
                    check_sentence.clear()
                    i = j - 1
                    break
        i += 1
    
    print("Count:", count)
targetedWord()