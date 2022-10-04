class Rocket:
    def __init__(self, name):
        self.name = name
    
    def __format__(self, format_spec):
        if format_spec == "fire":
            return self.name + " Fire!"
        elif format_spec == "repeat":
            return self.name * 5
        return self.name


rocket = Rocket("Falcon")

print(f"{rocket}")
print(f"{rocket:fire}")
print(f"{rocket:repeat}")