import random

numbers = list(range(1_000_0001))

selected_number = random.choice(numbers)
print("Selected Number ->", selected_number)

begin = 0
end = len(numbers) - 1
operations = 0

while begin <= end:
    middle = (end + begin) // 2
    actual_number = numbers[middle]

    if actual_number == selected_number:
        print("Find number ->", actual_number)
        break

    if actual_number > selected_number:
        print("The found number is lower than the selected:", actual_number)
        end = middle - 1

    if actual_number < selected_number:
        print("The found number is higher than the selected:", actual_number)
        begin = middle + 1

    operations += 1

print("total operations carried out ->", operations)
