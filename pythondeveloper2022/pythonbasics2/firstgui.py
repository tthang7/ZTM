picture = [
    [0,0,0,1,0,0,0],
    [0,1,0,1,0,1,1],
    [0,0,0,1,0,0,0]
]

#1 iterate over picture.
    # if 0 -> print ''
    # if 1 -> print *

# for row in picture:
#     for pixel in row:
#         if (pixel == 1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')
def show_cross():
    for row in picture:
        for item in row:
            if (item == 1):
                print('*', end='')
            elif (item == 0):
                print(' ', end='')
        print('') # need a new line after every row

def say_hello():
    print('hellloooo')

show_cross()
say_hello()
show_cross()
show_cross()
say_hello()
show_cross()