#wap to swap given values in a dictionary
# ip:- {1:20,3:30,4:40}
# op :- {20:1,30:3,40:4}

a = eval(input())
s = {}
for key in a:
    value = a[key]
    if value not in s:
        s[value] = key
    else:
        print()

print(a)
print(s)
