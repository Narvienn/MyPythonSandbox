"""Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string
 that reads the same forwards and backwards.)"""

# sample solution 1
word = input((str("Enter any word to see if it's a palindrome. \n").strip("")))
revWord = word[::-1]

if word == revWord:
    print("Your word is a palindrome.")
else:
    print("Your word is not a palindrome.")

# sample solution 2
word = input("Enter any word to see if it's a palindrome. \n")
wordAsList = list(word)
revWord = wordAsList.reverse()

if word == revWord:
    print("Your word is a palindrome.")
else:
    print("Your word is not a palindrome.")