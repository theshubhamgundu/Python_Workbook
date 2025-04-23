# wap to sort the elements in the dict using key s
# ip :- { 3:47,-2:36,9:77,4:44}
# op :- (2:36,3:47,4:44,9:77}

a = eval(input())
keys = list(a.keys())
n = len(keys)
for i in range(n):
    for j in range(0, n-i-1):
        if keys[j] > keys[j+1]:
            keys[j], keys[j+1] = keys[j+1], keys[j]
print()
for key in keys:
    print(f"({key}:{a[key]})", end=", ")
