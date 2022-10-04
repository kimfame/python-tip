def random_algorithm_1(num):
    print(num*num)

def random_algorithm_2(num):
    print(num*2)

def random_algorithm_3(num):
    print(num+num)

def random_algorithm_default(num):
    print(num-num)

choice = 1
num = 10

# if-else
if choice == 1:
    random_algorithm_1(num)
elif choice == 2:
    random_algorithm_2(num)
elif choice == 3:
    random_algorithm_3(num)
else:
    random_algorithm_default(num)

# dictionary
actions = {1: random_algorithm_1, 2:random_algorithm_2, 3:random_algorithm_3}

action = actions.get(choice, random_algorithm_default)
action(num)

