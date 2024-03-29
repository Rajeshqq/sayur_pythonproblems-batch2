input="hello"
stack=list(input)
revword=""
for i in range(len(stack)):
    revword+=stack.pop()
print(revword)