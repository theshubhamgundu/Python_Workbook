num = int(input("Enter a number: "))
sum_of_factorials = 0

for digit in str(num):
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i  
    sum_of_factorials += fact   

if sum_of_factorials == num:
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is not a Strong Number")
