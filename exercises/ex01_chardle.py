"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730382185"


xword = input("Enter a 5-character word: ")

if len(xword) < 5 or len(xword) > 5:
    print("Error: Word must contain 5 characters")
    exit()

xletter = input("Enter a single character: ")

if len(xletter) < 1 or len(xletter) > 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + xletter + " in " + xword)

xword_count = 0

if xword[0] == xletter: 
    print(xletter + " found at index 0")
    xword_count = xword_count + 1
if xword[1] == xletter: 
    print(xletter + " found at index 1")
    xword_count = xword_count + 1
if xword[2] == xletter: 
    print(xletter + " found at index 2")
    xword_count = xword_count + 1
if xword[3] == xletter: 
    print(xletter + " found at index 3")
    xword_count = xword_count + 1
if xword[4] == xletter: 
    print(xletter + " found at index 4")
    xword_count = xword_count + 1

if xword_count == 1:
    print(str(xword_count) + " instance of " + xletter + " found in " + xword)
elif xword_count > 1:
    print(str(xword_count) + " instances of " + xletter + " found in " + xword)
else:
    print("No instances of " + xletter + " found in " + xword)
