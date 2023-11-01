import random

letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

selected_letter = random.choice(letters)
print("Selected Letter ->", selected_letter)

operations = 0
for letter in letters:
    if letter == selected_letter:
        break

    if letter > selected_letter:
        print("The found letter is lower than the selected:", letter)

    if letter < selected_letter:
        print("The found letter is higher than the selected:", letter)

    operations += 1
    

print("total operations carried out ->", operations)