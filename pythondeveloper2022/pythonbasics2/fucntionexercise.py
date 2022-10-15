def highest_even(li):
    events = []
    for item in li:
            if item % 2 == 0:
                events.append(item)
    return max(events)


print(highest_even([10,2,3,4,8,11]))

