class PlayerCharacter:
    # Class Object Attribute, is static and not dynamic
    membership = True
    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name # attribute is specific and dynamic to each class obeject, if we want to access we need to use self.name as attribute
            self.age = age
    
    def shout(self):
        print (f'my name is {self.name}')


player1 = PlayerCharacter('Cindy', 19)

print(player1.age)
print(player1.shout())