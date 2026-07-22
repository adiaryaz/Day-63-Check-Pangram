# Day-63-Check-Pangram

Day 63/100 - Python Program to Check If a String is Pangram or Not

# Check If a String is a Pangram

A program to determine if a given string qualifies as a "pangram" by verifying that it contains every single letter of the English alphabet at least once.

## 📝 Description

This program efficiently checks for pangrams by leveraging Python's `set` data structure. It imports the `string` module to quickly generate a complete set of all lowercase English letters using `string.ascii_lowercase`.

When the user inputs a sentence, the `is_pangram(sentence)` function processes it by iterating through each character. It isolates only the alphabetic characters using `.isalpha()`, converts them to lowercase with `.lower()`, and stores the unique results in a new set called `letters_in_sentence`. Finally, it mathematically evaluates if the entire alphabet set is a subset of the letters found in the sentence using the `<=` operator (`alphabet <= letters_in_sentence`), returning `True` if it is, and `False` otherwise.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A string of text (a sentence) provided by the user via the terminal prompt.



### Output:

* If the condition is met: "The sentence is a pangram."


* If the condition is not met: "The sentence is not a pangram."



### Rules:

1. The program must accept a string input from the user.


2. The core logic must be encapsulated in a function named `is_pangram(sentence)`.


3. The program must import the `string` module to access the standard English alphabet.


4. The function must filter out spaces, numbers, and punctuation by ensuring `char.isalpha()` is true.


5. The function must be entirely case-insensitive, utilizing `char.lower()` for uniformity.


6. The function must return a boolean value representing the subset evaluation, which the driver code uses to print the final result.



---

## 💡 Examples

### Example 1 (Classic Pangram)

**Input:**

```text
The quick brown fox jumps over the lazy dog.

```

**Output:**

```text
The sentence is a pangram.

```

**Explanation:** The sentence contains all 26 letters of the English alphabet. The punctuation (period) and spaces are safely ignored by the `.isalpha()` check, and uppercase letters like 'T' are safely converted to lowercase.

### Example 2 (Not a Pangram)

**Input:**

```text
Hello World!

```

**Output:**

```text
The sentence is not a pangram.

```

**Explanation:** This sentence only contains a small subset of the alphabet (h, e, l, o, w, r, d). The subset check `alphabet <= letters_in_sentence` evaluates to `False`, so the program rejects it.

### Example 3 (Perfect Pangram without Punctuation)

**Input:**

```text
Pack my box with five dozen liquor jugs

```

**Output:**

```text
The sentence is a pangram.

```

**Explanation:** Every single letter from A to Z is present at least once. The function successfully matches the sets and returns `True`.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script as "Day 63.py").

```bash
git clone https://github.com/adiaryaz/Day-63-Check-Pangram.git
cd check-pangram

```

2. **Run the program**:

```bash
python "Day 63.py"

```

Enter a sentence when prompted to verify if it successfully utilizes every letter of the English alphabet!
