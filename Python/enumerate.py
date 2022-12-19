numbers = [11, 22, 33, 44, 55]

# for idx in range(len(numbers)):
#     print(idx, numbers[idx])

for idx, val in enumerate(numbers):
    print(idx, val)
'''
[Result]
0 11
1 22
2 33
3 44
4 55
'''


for idx, val in enumerate(numbers, start=5):
    print(idx, val)
'''
[Result]
5 11
6 22
7 33
8 44
9 55
'''