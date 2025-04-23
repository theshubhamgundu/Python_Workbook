#wap to find longest common prefix from the given strings
#s.t ip = flower,flows,flight

#op:- fl
s = list(map(str, input().split(',')))

if len(s) == 0:
    print()
else:
    s.sort()
    f = s[0]
    l = s[-1]

    i = 0
    while i < len(f) and i < len(l) and f[i] == l[i]:
        i += 1

    prefix = f[:i]
    print("LCF", prefix)
