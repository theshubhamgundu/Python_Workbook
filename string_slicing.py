x = 'Vignan college'

# Extracting various slices
b = x[:5]              # First 5 characters
c = x[::]              # Full string
d = x[6:40:2]          # From index 6 to end, step 2
e = x[50:1:3]          # Invalid range, returns empty string
f = x[3:-3]            # From index 3 to 3rd last character
h = x[-6:-2:2]         # Negative index slicing with step
i = x[::-1]            # Reverse the string
j = x[-3:-13:-12]      # Reverse with large step
k = x[-12:-6:-4]       # Negative step, returns empty due to range
l = x[-10:11:-1]       # Returns empty due to range
m = x[11:-10:-1]       # Negative reverse slice
n = x[12:4:-1]         # Reverse slice from 12 to 5

print(b, c, d, e, f, h, i, j, k, l, m, n)
