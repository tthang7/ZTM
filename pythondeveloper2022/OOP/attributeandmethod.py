class PlayerCharacter:
    # Class Object Attribute, is static and not dynamic
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name # attribute is specific and dynamic to each class obeject, if we want to access we need to use self.name as attribute
            self.age = age
    
    def shout(self):
        print (f'my name is {self.name}')

    def run(self, hello):
        print (f'my name is {self.name}')

player1 = PlayerCharacter('Cindy', 44)
player2  = PlayerCharacter('Tom', 33)
player2.attack = 50

print(player1.age)
print(player2.name)
print(player2.attack)
print(player1.shout())