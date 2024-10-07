# 1.Print the given pattern
'''
n = int(input("enter the number : "))
for i in range(n):
    print("****")

'''
# 2.fibbonacchi number
'''
n = int(input("enter the nth term : "))
a = 0
b = 1
print(a,end=" ")
print(b,end=" ")
for i in range(1,n-1):
    c = a+b  
    print(c,end=" ")
    a = b
    b = c
'''

# 3.
'''
n = int(input("enter the number : "))
i = 1
while i<=n :
    j = 1
    while j<=n:
        print(j,end=" ")
        j = j + 1
    print(end="\n")
    i = i + 1
'''
    
# 4.
'''
n = int(input("enter the number : "))
i = 0
while i < n:
    j = 0
    while j <= i:
        print("*",end=" ")
        j = j + 1
    print(end="\n")
    i = i + 1
'''
# 5.
'''
n = int(input("enter the number : "))
i = 0
while i < n:
    j = 1
    while j <= i:
        print(j,end=" ")
        j = j + 1
    print(end="\n")
    i = i + 1
'''
# 6.

    
    

