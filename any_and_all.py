any_true = any([False, True, False])
print(any_true)

all_true = all([True, True, True])
print(all_true)


numbers = [-10, -20, -30, 0, 1, 10, 20, 40]

# manually looping
has_positives_1 = False
for n in numbers:
    if n > 0:
        has_positives_1 = True
        break
print(has_positives_1)


# refactor using any()
has_positives_2 = any(n > 0 for n in numbers)
print(has_positives_2)