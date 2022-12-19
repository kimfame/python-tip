import bisect

a = [4, 10, 11, 13, 17, 20, 30]

new_value = 12

# Insert 1
idx = bisect.bisect(a, new_value)
print(idx)

a.insert(idx, new_value)
print(a)


# Insert 2
bisect.insort(a, 25)
print(a)