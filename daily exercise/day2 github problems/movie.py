#Problem #4
#You are inviting 3 of your friends over to your house for watching a movie.
#You have a list of 5 movies you like. Ask each of your friends 5 movies they like.

#1. List all the movies everyone likes
#2. List only the movies you like but no one else likes
#3. List the movies you like and at least one friend likes. Find which friend it is.
#4. List the movies all your friends like but you don't like.


frnd1=["god father","matrix","interstellar","inception","dark knight"]
frnd2=["the shawshank redemption","interstellar","dark knight","alien","matrix"]
frnd3=["1917","matrix","mad max","alien","interstellar"]
myself=["interstellar","inception","the prestige","dunkrik","tenet"]
print("List all the movies everyone likes")
for i in range(0,len(frnd1)):
    if frnd1[i] in frnd2:
        if frnd1[i] in frnd3:
            if frnd1[i] in myself:
                print(frnd1[i])
print("List only the movies you like but no one else likes")

for i in range(0,len(myself)):
    if myself[i] not in frnd2:
        if myself[i] not in frnd3:
            if myself[i] not in frnd1:
                print(myself[i])


print("List the movies you like and at least one friend likes. Find which friend it is.")
for i in range(0,len(myself)):
    if myself[i] in frnd1:
        print(f"frnd1 likes {myself[i]} which i likes")
    if myself[i] in frnd2:
         print(f"frnd2 likes {myself[i]} which i likes")
    if myself[i] in frnd3:
         print(f"frnd3 likes {myself[i]} which i likes")
print("List the movies all your friends like but you don't like")
for i in range(0,len(myself)):
     if frnd1[i] in frnd2:
        if frnd1[i] in frnd3:
            if frnd1[i] not in myself:
                print(frnd1[i])
