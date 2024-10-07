n = int(input("enter the size of a list : "))

list = []

for _ in range(n):
    num = int(input())
    list.append(num)

index1 = int(input("enter index first : "))
index2 = int(input("enter index second : "))
print(list)

# swapping two index
temp = list[index1]
list[index1] = list[index2]
list[index2] = temp

print(list)