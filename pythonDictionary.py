dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(dict["brand"])

#update
dict["year"] = 2000
print(dict)

dict.update({"brand":"Suzuki"})
print(dict)

print(len(dict))

print(dict.keys())

print(dict.values())

print(dict.items())

#adding data can be done using update also
dict["color"] = "red"
print(dict)

#remove item
dict.pop("brand")
print(dict)

dict.clear()

del dict
