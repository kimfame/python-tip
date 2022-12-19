str = "Hello~!, beginner!?"

print(str.startswith("Hel")) # True
print(str.endswith("ner!?")) # True


filters = ("What's up", "Do", "Hello", "Have")
print(str.startswith(filters)) # True

punctuations = (".", "?", "!")
print(str.endswith(punctuations)) # True
