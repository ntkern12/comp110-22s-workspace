"""EX01 - One-Shot Wordle - Loops!"""

__author__ = "730382185"


secret_word = "python"

num_letters = len(secret_word)

your_word = input(f"What is your {num_letters}-letter guess? ")

count = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index = 0

results = ""

letter_at_dif_i = False

secret_index = 0

while (len(your_word) < num_letters or len(your_word) > num_letters) and count < 5:
    your_word = input(f"That was not {num_letters} letters! Try again: ")
    count = count + 1

while index < num_letters:
    if your_word[index] == secret_word[index]:
        results = results + GREEN_BOX
    else:
        results = results + WHITE_BOX
    index = index + 1

print(results)

if your_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")