names = {"ram","shyam","mohan"}
print(names)
# check length
print(len(names))

# print all element of names
for x in names:
    print(x)
    
# item present or not
if "ram" in names:
    print("present")
else:
    print("absent")

# add elements in sets
names.add("keshav")
print(names)

# type of names
print(type(names))

# add another sequence in a set
names_list = ["sumit","raghav"]
names.update(names_list)
print(names)
# removing elements from a sets
names.remove("ram")
print(names)

# names.remove("madhav")
# if we want to remove an item which is not present in set then we use discard function which will not give any error
names.discard("madhav")
# we can also remove the element by using discard fucntion
names.discard("raghav")
print(names)


# joining two sets
s1 = {1,2,3,8}
s2 = {4,8,5,6}

print(s1, s2)

# first way
s3 = s1.union(s2)
print(s3)

# second way
s1.update(s2)
print(s1)

# keep only similar items in both sets
s3 = {'a','b','e'}
s4 = {'d','e','a'}
s3.intersection_update(s4)
print(s3)

# keep all values except dublicates
s4 = {6,7,8}
s5 = {5,6,9}
s4.symmetric_difference_update(s5)
print(s4)

