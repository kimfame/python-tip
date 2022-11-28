
fruit_sales = [("apple", 10), ("banana", 5), ("apple", 7)]

only_apples = (fruit_sales[1] for fruit in fruit_sales if fruit[0] == "apple")
apple_sales = sum(only_apples) # error # need to test
print(apple_sales)