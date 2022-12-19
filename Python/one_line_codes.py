# 1. swap variables
a, b = 1, 2
b, a = a, b
print(a, b) # 2 1


# 2. list comprehension
c = [i*i for i in range(10) if i % 2 == 0]
print(c) # [0, 4, 16, 36, 64]


# 3. if else (ternary operator)
d = 1 if False else 100
print(d) # 100


# 4. print without new lines
e = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*e) # 0 1 2 3 4 5 6 7 8 9 10


# 5. days left in year
import datetime
print(
    (datetime.date(2022,12,31) - datetime.date.today()).days
)
"""
python3 -c "import datetime; print((datetime.date(2022,12,31) - datetime.date.today()).days)"
"""


# 6. reversing a list
f = [1,2,3,4,5,6,7,8,9,10]
f = f[::-1]
print(f) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# 7. multiple variable assignments
g, h, i = "apple", 11, True
print(g, h, i) # apple 11 True


# 8. space separated numbers to integer list
j = "1 2 3 4 5 6 7 8 9 10"
k = list(map(int, j.split()))
print(k) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 9. reading file into list
"""
[test.txt]
a
  b
   c
 d
  e
f
"""
l = [line.strip() for line in open("test.txt", "r")]
print(l) # ['a', 'b', 'c', 'd', 'e', 'f']


# 10. http server
"""
in the folder which has index.html
"""
# python3 -m http.server