input="abcdefg"
output=""
for i in range(len(input)):
    if i%2==0 and i!=0:
        output+=f" {input[i]}"
    else:
        output+=input[i]
print(output)