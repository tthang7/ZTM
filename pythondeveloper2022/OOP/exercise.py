# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # 1 Instantiate the Cat object with 3 cats
# cat1 = Cat('Cindy', 15)
# cat2 = Cat('Lucy', 8)
# cat3 = Cat('Tom', 3)



# # 2 Create a function that finds the oldest cat
# cat_ages = [cat1.age,cat2.age,cat3.age]
# def maxage():
#     return max(cat_ages)


# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f'Oldest cat is {maxage()} years old')




# #Given the below class:
# # 1 Instantiate the Cat object with 3 cats
# # 2 Create a function that finds the oldest cat
# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

class Cat:
    species = 'buou'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('yuanyuan', 16)
cat2 = Cat('Lucy', 15)
cat3 = Cat('Tom', 88)

cat_ages = [cat1.age,cat2.age,cat3.age]
def Maxage():
    return max(cat_ages)

print(f'the oldest cat age is {Maxage()}')