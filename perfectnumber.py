n = int(input("Enter a number: "))

sum_factors = 0  
for i in range(1, n):
    if n % i == 0:
        print(i)  
        sum_factors += i
if sum_factors == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
    print("Sum of proper divisors:", sum_factors)
