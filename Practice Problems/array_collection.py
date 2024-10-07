'''
python does not have built-in support for arrays
phthon collection(arrays): 1.list, 2.Tuple, 3.Set, 4.Dictionary
'''
# list : Lists are used to store multiple items in a single variable.Lists are created using square brackets.
fruits = ["mango","banana","orange","kiwi"]
print(fruits)
print(type(fruits))

fruits[1] = "Apple"
print(fruits)
print(len(fruits))

if "Apple" in fruits:
    print("yes")
if "licchi" not in fruits:
    print("not present")
else:
    print("no")
    
print(fruits)

# indexing of a list
print(fruits[1])
print(fruits[-3])

# sublist
print(fruits[1:3])

# add items in list at last using append function 
fruits.append("grapes")
print(fruits)

# insert items in list
fruits.insert(4,"guava")
print(fruits)

# list extend 
place = ["Bihar","punjab"]
print(fruits.extend(place))

# remove items from a list
print()
print("after removing the kiwi remaining fruits are : ")

fruits.remove("kiwi")
print(fruits)

fruits.pop(2)
print(fruits)

# update a sublist in list
fruits[1:3] = ["papaya","kiwi"]
print(fruits)

# sorting a list
fruits.sort()  #ascending order
print(fruits)
fruits.sort(reverse=True)   #descending order
print(fruits)

# list comprehension
marks = [90,79,89,95,67,88]
marks2 = [i for i in marks if i > 170]
print(marks2)

