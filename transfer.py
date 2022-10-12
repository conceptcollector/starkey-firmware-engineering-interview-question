import json

output = {}

with open('input.json', 'r') as original:
    data = json.load(original)

for userDictionary in data:
    if userDictionary["user"] in output.keys():
        for color in userDictionary:
            if color["command"] in userDictionary.keys():
                if userDictionary["command"] == "red":
                    # print(output)
                    output[userDictionary["red"]].append(userDictionary["timestamp"])
                elif userDictionary["command"] == "yellow":
                    # print(output)
                    output[userDictionary["yellow"]].append(userDictionary["timestamp"])
                elif userDictionary["command"] == "blue":
                    # print(output)
                    output[userDictionary["blue"]].append(userDictionary["timestamp"])
                elif userDictionary["command"] == "green":
                    # print(output)
                    output[userDictionary["green"]].append(userDictionary["timestamp"])
                else:
                    pass
    else:
        output.update(user = userDictionary["user"], red = [], yellow = [], blue = [], green = [])
        for color in userDictionary:
            if color in userDictionary.keys():
                if userDictionary["command"] == "red":
                # print(output)
                    output[userDictionary["red"]].append(userDictionary["timestamp"])
                elif userDictionary["command"] == "yellow":
                # print(output)
                    output[userDictionary["yellow"]].append(userDictionary["timestamp"])
                elif userDictionary["command"] == "blue":
                # print(output)
                    output[userDictionary["blue"]].append(userDictionary["timestamp"])
                elif userDictionary["command"] == "green":
                # print(output)
                    output[userDictionary["green"]].append(userDictionary["timestamp"])
                else:
                    pass
    # output.setdefault(userDictionary["user"], {})[userDictionary["command"]]

# class corrected:
#     def __setitem__(self, key, value):
#         try:
#             self[key]
#         except KeyError:
#             super(corrected, self).__setitem__(key, [])

print(output)

# input.json
# Collecting user names
# Aggregating the command into a list of timestamps
# output.json