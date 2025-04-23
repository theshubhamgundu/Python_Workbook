#wap to find given string is heterogram or not op with true or false
s = input().lower().replace(" ", "").replace("-", "")
u= set(s)

if len(s) == len(u): 
    print("True")
else:
    print("False")
