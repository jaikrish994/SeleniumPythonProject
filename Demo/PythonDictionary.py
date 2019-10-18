my_dict = {
    "class" : "animal",
    "name"  : "girafee",
    "age"   : 10
}
print(my_dict)
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.values())
for x in my_dict:
    print(x)
    print(my_dict[x])
for x,y in my_dict.items():
    print(x, y)
my_dict["name"] = "Elephant"
print(my_dict)
my_dict["color"] = "grey"
print(my_dict)
my_dict.pop("color")
print(my_dict)
my_dict.popitem()
print(my_dict)
del my_dict["class"]
print(my_dict)
my_dict.clear()
print(my_dict)
del my_dict
print(my_dict)