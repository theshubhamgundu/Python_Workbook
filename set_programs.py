#Wap to find missing number in a given range 1 to n
a = list(map(int, input().split(',')))
n=max(a)
s = int(input())
m = set(range(1, s + 1)) - set(a)
print(m)
c=m.difference(a)
if (len(c)==0):
    print(n+1)
else:
    print(c.pop())
    
