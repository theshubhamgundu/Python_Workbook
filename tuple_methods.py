# Tuple demonstrations
a = ()
print(a, type(a))

b = (12, 45, 52, 74, 61, 11, 13, 'abcd')
print(b[1], b[-1])

# This is an integer, not a tuple
c = (45)
print(c, type(c))

# Just arithmetic operation
d = (45 + 6) * 2
print(d, type(d))

# Single element tuple
e = (57,)
print(e, type(e))

# Tuple without parentheses
f = 12, 34, 56, 12
print(f, type(f))

# Tuple multiplication
g = e * 3
print(g)

# Tuple concatenation
h = f + g
print(h)

# Tuple methods
print(h.count(57), h.index(12))

# Loop through tuple
for i in f:
    print(i)

# Loop using index
for i in range(len(f)):
    print(i, f[i])

# Tuple functions
print(len(f), max(f), min(f), sum(f))

# Type conversion
k = list(f)
print(k, type(k))
m = tuple(k)
print(m, type(m))

# Swap min and max in a tuple
a = (10, 14, 25, 6, 9, 116, 11)
b = list(a)
c = min(b)
d = max(b)
e = b.index(c)
f = b.index(d)
b[e], b[f] = d, c
print(tuple(b))

# Prefix summation
a = (10, 14, 25, 6, 9, 116, 11)
b = list(a)
for i in range(1, len(b)):
    b[i] += b[i - 1]
print(tuple(b))

# Suffix summation
c = list(a)
for i in range(len(a) - 2, -1, -1):
    c[i] += c[i + 1]
print(tuple(c))
