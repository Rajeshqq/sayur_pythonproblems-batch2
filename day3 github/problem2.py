try:
    with open("D:\sayur day1\day3 github\input.txt", "r") as file:
        sentence = file.read()
        print(sentence)
except IOError:
    print("Error: doesn't have a file" )

# Split the sentence into words and convert to lowercase
words = sentence.lower().split(" ")

# Target word we want to count
targetWord = "the"

# Initialize count and loop variable
count = 0
i = 0

# Loop through the words
while i < len(words):
    # Initialize a variable to track the word before "the"
    ignored_word = ""
    
    # Check if the current word is "the"
    if words[i] == "the":
        # If "the" is found, start looking for the next occurrence
        for j in range(i + 1, len(words)):
            # If "a" is found, mark it as ignored
            if words[j] == "a":
                ignored_word = "a"

            # If the target word is found
            if targetWord == words[j]:
                # If it's not ignored, increase count and exit the loop
                if ignored_word != "a":
                    count += 1
                    break
                else:
                    break  # If ignored, exit loop without counting

            # Update i to the index of the last occurrence of "the"
            i = j - 1
     
    # Move to the next word
    i += 1

# Print the final count
print(count)