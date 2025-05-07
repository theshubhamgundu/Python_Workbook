# Program to add the given two no after reversing again rev the sum
def rev(n):
    return int(str(n)[::-1])

def add_rev(a, b):
    rev_a = rev(a)
    rev_b = rev(b)
    total = rev_a + rev_b
    return rev(total)

n1= input()
n2 =input()
r= add_rev(n1, n2)
print("Result:", r)

