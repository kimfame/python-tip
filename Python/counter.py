from collections import Counter

numbers = [33, 33, 5, 6, 22, 22, 22]
counter = Counter(numbers)

print(counter)
print(counter[33])
print(counter.most_common(1))