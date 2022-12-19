class Item:
    def __init__(self, state=None):
        #self.state = state if state else -1 # Wrong! state == 0 -> UNDEFINED
        self.state = state if state is not None else -1
    
    def __str__(self):
        if self.state == -1:
            return "UNDEFINED"
        elif self.state == 0:
            return "UNSET"
        else:
            return "SET"
        

item1 = Item()
print(item1)

item2 = Item(0)
print(item2)

item3 = Item(1)
print(item3)
