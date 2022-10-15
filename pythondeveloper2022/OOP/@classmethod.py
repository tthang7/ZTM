class PlayerCharacter:
    # Class Object Attribute, is static and not dynamic
    membership = True
    def __init__(self, name='anonymous', age=0):
            self.name = name # attribute is specific and dynamic to each class obeject, if we want to access we need to use self.name as attribute
            self.age = age
    
    def shout(self):
        print (f'my name is {self.name}')
    
    @classmethod # using this when we want to modify the attribute, like change self.name = name
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod # using this when don't care about class state, the attribute, like not changing self.name = name 
    def adding_things2(num1, num2):
        return num1 + num2

player2 = PlayerCharacter.adding_things(2,3)
print(player2.name)
print(player2.age)

