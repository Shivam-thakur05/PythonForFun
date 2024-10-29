fruits = ["Mango","Apples","Banana","Orange","Kiwi","mango","banana"]
# type of fruits
print(type(fruits))

# insert at position
fruits[1] = "Apple"

# length of the list
print(len(fruits))

# conditional statment
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

fruits.remove("Kiwi")
print(fruits)

fruits.pop(4)
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

# sort the list
fruit = ["Mango","Apples","Banana","Orange","Kiwi","mango","banana","apples"]
# sort with upper case to lower case
fruit.sort()
print(fruit)

# sort the list by a to z no case matter
fruit.sort(key=str.lower)
# print(fruit)

number = [10,12,31,24,15]
# loop using
for i in number:
    print(i,end=" ")
# index as well as element of list
for idx,i in enumerate(number):
    print(idx,i)
    
# if we create a big list then that is not possible to write each thing inside the list agin and again 
zeros = [0] * 1000
# print(zeros)

# concatinate of two list
newlist = fruit+number
print(newlist)