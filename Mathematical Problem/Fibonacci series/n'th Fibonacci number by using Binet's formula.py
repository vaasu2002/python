n = int(input("Enter: "))
sqrt_five = 2.23606797749978969
alpha = (1 + sqrt_five) / 2
beta = (1 - sqrt_five) / 2

x = ((alpha ** n) - (beta ** n)) // (sqrt_five)
print(int(x))
