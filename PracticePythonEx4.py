"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number. """

usNum = int(input("Gimme a number from 0 to 500. \n"))

potentialDivisors = list(range(0, 501))
usNumDivisors = []

for i in potentialDivisors:
    if usNum % i == 0:
        usNumDivisors.append(i)
print(usNumDivisors)