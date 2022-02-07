"""EX03 - Structuted Wordle."""

__author__ = "730382185"


def contains_char(x_word: str, x_letter: str) -> bool:
    """Test for letters in words."""
    assert len(x_letter) == 1
    word_index = 0
    num_letters = len(x_word)
    while word_index < num_letters:
        if x_word[word_index] == x_letter:
            return True
        else:
            word_index = word_index + 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Return results as emojis."""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    results = ""
    while index < len(secret_word):
        if guess_word[index] == secret_word[index]:
            results = results + GREEN_BOX
        else:
            bool_char = contains_char(secret_word, guess_word[index])
            if bool_char:
                results = results + YELLOW_BOX
            else:
                results = results + WHITE_BOX
        index = index + 1
    return results


def input_guess(length_word: int) -> str:
    """Check word length."""
    your_word = input(f"Enter a {length_word} character word? ")
    while (len(your_word) < length_word or len(your_word) > length_word):
        your_word = input(f"That wasn't {length_word} chars! Try again: ")
    return your_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    todays_word = "codes"
    won = False
    while turn < 7 and not won:
        print(f"=== Turn {turn}/6 ===")
        guessed_word = input_guess(len(todays_word))
        if guessed_word == todays_word:
            print(emojified(guessed_word, todays_word))
            won = True
        else:
            print(emojified(guessed_word, todays_word))
            turn = turn + 1
    if won:
        print(f"You won in {turn}/6 Turns")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()