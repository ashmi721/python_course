# Dictionary: Dictionary items are ordered, changeable, and does not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# create a empty dict
dict1 = {}
print(type(dict1))


# create a simple dictionary
simple_dict = {
    "mango" : 4,
    "apple" : 3,
    "orange" : 2
}
print(simple_dict)

# print(len(simple_dict))

# accessing items
print(simple_dict["apple"])

# extract the value of 4
print(simple_dict["mango"])


# create nessted dictinary
nested_dict = {
    "fruits":{"mango":2,"orange":1},
    "vegetable":{"potato":2,"onion":3}
}

# print(len(nested_dict))
# print(type(nested_dict))

# accessing items
print(nested_dict["fruits"])

# extract nested value 1
print(nested_dict["fruits"]["orange"])


# mutable  dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict['year'] = 2023
print(thisdict)


# method of dictinary
# get : Returns the value of the specified key
print(thisdict.get("model"))

# get list  of all the keys present in the dictionary
print(thisdict.keys())

# get list of all the values present in the dictionary
print(thisdict.values())

# get list containing tuples of key-valie pairs
print(thisdict.items())

# add new item key = 'model','manag'
thisdict.update({"model":"manag"})
print(thisdict)
thisdict.update({"foundar": "jyakson"})
print(thisdict)

# remove 2 item of the dict

thisdict.pop("model")
print(thisdict)


# dictionary comprehension

sample_list = [10,30,70,44]

print({idx:item for idx, item in enumerate(sample_list)})