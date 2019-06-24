"""Take two lists and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python"""


import random

list1 = random.sample(range(1, 50), k=20)
list2 = random.sample(range(1, 100), k=20)
# random.sample(range, k/population) - return a k length list of unique elements

print(set(list1) & set(list2))
# Python sets are unordered but allow logic operators!











