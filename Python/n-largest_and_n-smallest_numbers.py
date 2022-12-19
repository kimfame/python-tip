import heapq

numbers = [104, 113, 136, 143, 1, 2, 3, 1000, 300]

print(min(numbers), max(numbers))

print(heapq.nlargest(3, numbers))
print(heapq.nsmallest(2, numbers))