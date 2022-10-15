# *args

def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,3,4,5,6, num1=4, num2=13))

# Rule: params, *args, default parameters, **kwargs
# def super_func(name, *args, default parameters, **kwargs):
# print(super_func('Andy', 1,3,4,5,6, num1=4, num2=13))