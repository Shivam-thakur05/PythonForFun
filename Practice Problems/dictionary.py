# make a dictionary of name of phone

phones = {
    "ram" : 1234,
    "shyam" : 1245,
    "keshav" : 2381,
    "john" : 2126
}

# print the dictionary
print(phones)

# checking type of phones
print(type(phones))

# checking the length of the dictionary
print(len(phones))

# access items of dictionary
print(phones["john"])
print(phones.get("john"))

# print all keys of the dictionary
print(phones.keys())

# update the value in dict
phones["john"] = 7612

# add element in dictionary
phones["kia"] = 2342

# print the dictionary
print(phones)

# add more dict from another dictionary
more_phones = {
    "raj" : 2864,
    "abhi" : 2345,
    "sumit" : 2965
}
phones.update(more_phones)
print(phones)

# remove elements from a dictionary
phones.pop("ram")
phones.popitem()   # this will remove the last item
print(phones)

phones.clear()  # this will empty the dictionary
print(phones)

# printing values of a dict
for x,y in phones.items():
    print(x,y)
    
# nested dictionary
area = {
    "area1" : {
        "a" : 12,
        "b" : 14,
        "c" : 28
    },
    "area2" : {
        "d" : 23,
        "e" : 24,
        "f" : 46
    }
}
print(area["area1"]["b"])
print(area["area2"]["f"])
