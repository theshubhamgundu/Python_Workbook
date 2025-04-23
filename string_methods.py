# String method demonstrations
a = "vigNan College"

# Convert to upper case
b = a.upper()

# Convert to lower case
c = a.lower()

# Swap the case of each character
d = a.swapcase()

# Capitalize the first character
e = a.capitalize()

# Print transformed strings
print(b, c)
print(d, e)

# Check case conditions
print(a.isupper(), b.isupper())
print(a.islower(), c.islower())

# Check if all characters are alphabets
print(a.isalpha(), 'abc'.isalpha())

# Check numeric conditions
print('123'.isnumeric(), 'a123'.isnumeric())

# Check alphanumeric conditions
print('a123'.isalnum(), 'a123@'.isalnum())

# Loop through characters in a string
for i in 'vignan':
    print(i)

# Loop using index
f = 'vignan'
for i in range(len(f)):
    print(i, f[i])

# Reverse index traversal
for i in range(len(f)-1, -1, -1):
    print(i, f[i])

# Palindrome check
x = 'racecar'
i = x[::-1]
print(x)
if x == i:
    print("Yes")

# Sorting characters in a string
a = input("Enter a string to sort: ")
b = list(a)
print(b)

b.sort()  # Sort list of characters
print(b)

# Join sorted characters into a string
c = ''
for i in b:
    c += i
print(c)
