numbers = [1, 2, 3, 4, 5]
strings = ["alfa", "bravo", "charlie", "Delta"]

# numbers size must equal strings size
# for i in range(len(numbers)):
#     print(numbers[i], strings[i])

# use zip
for val1, val2 in zip(numbers, strings):
    print(val1, val2)
