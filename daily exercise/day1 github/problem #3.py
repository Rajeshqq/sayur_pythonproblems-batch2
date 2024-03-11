def grade():
    name = ["rajesh", "ramesh", "nithish", "siva"]
    maths = [70, 90, 80, 100]
    english = [100, 90, 70, 100]
    cs = [70, 90, 100, 100]
    for i in range(0,len(name)):
        mark = [maths[i], english[i], cs[i]]
        mark.sort()
        if mark[2] == 100 and mark[0] == 100:
            print(f"{name[i]}  grade is A")
        elif mark[2] >= 80:
            print(f"{name[i]} grade is B")


grade()


