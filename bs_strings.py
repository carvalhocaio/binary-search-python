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

begin = 0
end = len(letters) - 1
operations = 0

while begin <= end:
    middle = (end + begin) // 2
    actual_letter = letters[middle]

    if actual_letter == selected_letter:
        print("Find letter ->", actual_letter)
        break

    if actual_letter > selected_letter:
        print("The found letter is lower than the selected:", actual_letter)
        end = middle - 1

    if actual_letter < selected_letter:
        print("The found letter is higher than the selected:", actual_letter)
        begin = middle + 1

    operations += 1

print("total operations carried out ->", operations)
