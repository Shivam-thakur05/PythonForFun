'''
write a program in python taking list of strings and gives back count of target string within list
'''

fruits = ["apple", "banana", "apple", "banana", "apple"]
target1 = "apple"
target2 = "banana"

count = 0
count2 = 0

for i in fruits:
    if i == target1:
        count = count+1
    if i == target2:
        count2 = count2+1

print(count)
print(count2)