def removeDuplicate():
    input="hellllo"
    output=""
    for i in range(len(input)):
        if input[i] not in output:
            output+=input[i]
    print(output)
removeDuplicate()