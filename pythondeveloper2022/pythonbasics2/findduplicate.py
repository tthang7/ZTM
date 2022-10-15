# exercise: check for duplicates in list:
some_list = ['a', 'b', 'c', 'd', 'e', 'f', 'd', 'n', 'n']

# i = 0
# for item in some_list:
#     if i < len(some_list):
#         print(i)
#         print(some_list[i])
#         i += 1

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         duplicates.append(value)
    
# print(duplicates)
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)