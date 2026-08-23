user = {
    "age" : 44,
    "name" : 'Kylie',
    "magic" : 'true',
    'array' : [1, 2, 3, 4, 5, 6],
    'tuple' : (1, 2, 3, 4),
    'set' :{1, 2, 3, 4, 5}

}
empty_dict = dict()

    
keys = list(user.keys())
values = list(user.values())
items = list(user.items())

def scream():
    print("ahhhhhh!!")

user["scream"] = scream

user["scream"]()
print(user["array"])
print(user['set'])