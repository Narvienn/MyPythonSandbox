"""Make a list and write a program that prints out all the elements of the list that are less than 5.
Extras:
1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user."""

listA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listB = []

for i in listA:
    if i > 5:
        listB.append(i)
print(listB)

# Extra 2: one-line alternative

print(listB for i in listA if i > 5)

# Extra 3: user number

userNumber = int(input("Please give me a number - we'll see if there are any smaller than that on the list. \n"))
newList = []

for i in listA:
    if i < userNumber:
        newList.append(i)
print(newList)