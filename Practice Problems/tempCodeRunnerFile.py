
reverse = 0
while n!=0:
    rem = n%10
    reverse = 10*reverse + rem
    print(rem,end=" ")
    n = n//10

# print("reverse of number : ",reverse)

'''
fruits = ["mango","banana","orange","kiwi"]
print(fruits)
print(type(fruits))

fruits.append(3);
print(fruits)

