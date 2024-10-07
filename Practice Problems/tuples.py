# creating a tuple 
color = ("red","black","blue","green")

# creating a tuple 1 item
fruit = ("apple")

# check type of tuple
print(type(fruit))

# check length of tuple
print(len(color))

# accesing items in  tuple
print(color[1])     #positive indexing
print(color[-3])    #negative indexing'
print(color[1:3])   #range indexing
print(color[-2:])   #negative range indexing

# check if an item exists in tuple
if "green" in color:
    print("present")
else:
    print("not present")

# traverse the tuple
for i in color:
    print(i,end=" ")

# concatinate two tuple
more_color = ("pink","yellow","orange")
color = color + more_color
print(color)

# unpacking a tuple
