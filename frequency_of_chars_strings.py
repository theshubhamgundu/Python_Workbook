# wap to find the frequency of chars in a string
#ip:- missisipi
#op:- m=1,i=4,s=3,p=1
s = input()
f = {}
for ch in s:
    if ch in f:
        f[ch] += 1
    else:
        f[ch] = 1
for ch in f:
    print(f"{ch}={f[ch]}", end=", ")
