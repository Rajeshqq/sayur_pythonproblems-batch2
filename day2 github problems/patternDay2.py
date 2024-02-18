def pattern():
    center="1"
    num=2
    print("1")
    while(num<=6):
        center=str(num)+str(center)+str(num)
        num+=1
        print(center)
pattern()