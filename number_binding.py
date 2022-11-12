# '==' value comparison
# 'is' address comparison

# Number 1 ~ 256
num_1 = 256
num_2 = 256

num_1 == num_2 # True
num_1 is num_2 # True

id(num_1), id(num_2)
(4374241488, 4374241488)

# Number 257
num_3 = 257
num_4 = 257
 
num_3 == num_4 # True
num_3 is num_4 # False
 
id(num_3), id(num_4)
(4377003184, 4377003568)