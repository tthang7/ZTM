is_magician = True
is_expert = True

# check if magician AND experyt: "you are a master magician"
# check if magician BUT not expert: "at least you are getting there"
# if you are not a magician: "you need magic powers"

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician or is_expert:
    print('at least you are getting there')
else:
    print('you need magic powers')