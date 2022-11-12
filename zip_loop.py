# Example 1
company = ['Google', 'Amazon']
worker = [1000, 2400]
 
company_worker = dict(zip(company, worker))
print(company_worker)
 
{'google': 1000, 'amazon': 2000}


# Example 2
numbers = [1, 2, 3, 4, 5]
strings = ["alfa", "bravo", "charlie", "Delta"]

# numbers size must equal strings size
# for i in range(len(numbers)):
#     print(numbers[i], strings[i])

# use zip
for val1, val2 in zip(numbers, strings):
    print(val1, val2)
