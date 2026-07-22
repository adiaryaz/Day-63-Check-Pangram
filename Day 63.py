import string

def is_pangram(sentence):
    """
    Check if a sentence is a pangram.
    A pangram contains every letter of the English alphabet at least once.

    Args:
    sentence (str): The input string to check.

    Returns:
    bool: True if the sentence is a pangram, False otherwise.
    """
    alphabet = set(string.ascii_lowercase)
    letters_in_sentence = set(char.lower() for char in sentence if char.isalpha())
    return alphabet <= letters_in_sentence

if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    if is_pangram(input_sentence):
        print("The sentence is a pangram.")
    else:
        print("The sentence is not a pangram.")