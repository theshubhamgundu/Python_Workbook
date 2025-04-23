#wap to sort the dict accoridng to the values
a = eval(input())

items = list(a.items())

n = len(items)
for i in range(n):
    for j in range(0, n-i-1):
        if items[j][1] > items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]

print()
for key, value in items:
    print(f"({key}:{value})", end=", ")
