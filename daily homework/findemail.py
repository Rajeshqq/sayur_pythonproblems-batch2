import re
s=input("enter the sentence")
pattern = r'[a-zA-Z0-9_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3}'
matches = re.findall(pattern, s)
print(matches) 
