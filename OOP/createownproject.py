class PlayerCharacter:    # Object is class, class is blueprint
    def __init__(self, name, age):   # class is blueprint and need to be instantiated by using function like _init_
        self.name = name    # attribute that running as instantiation that customise object
        self.age = age
    
    def run(self):  # add method to our class, so each object we creat have access to this method
        print ('run')

    @classmethod # method can be called on the class without instancitating it into an object
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod # method can be called on the class without instancitating it into an object
    def adding_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Cindy', 44)
player2  = PlayerCharacter('Tom', 33)

print(player1.age)
print(player2.name)
