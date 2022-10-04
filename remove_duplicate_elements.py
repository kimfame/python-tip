duplicate_list = [11, 22, 3, 4, 5, 11, 22]
print(duplicate_list)

cleaned_list_1 = list(set(duplicate_list))
print(cleaned_list_1) # [3, 4, 5, 11, 22]

cleaned_list_2 = list(dict.fromkeys(duplicate_list))
print(cleaned_list_2) # [11, 22, 3, 4, 5]

