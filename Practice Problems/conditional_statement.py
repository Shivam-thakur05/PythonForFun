# 1.first 

'''
a = int(input("enter the number"))
if a < 0 :
    print("this number is not positive")
elif  a % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")

'''


# 2. find greatest number in 3 number

'''
a = int(input("enter first number "))
b = int(input("enter second number "))
c = int(input("enter third number "))

if a>b:
    if a>c:
        print(a,"is greater")
    else:
        print(c,"is greater")
elif b>a:
    if b>c:
        print(b,"is greater")   
    else:
        print(c,"is greater")
else:
    print(c,"is greater")
    
'''




# 3.find greatest number in 4 number
'''
a = int(input("enter first number "))
b = int(input("enter second number "))
c = int(input("enter third number "))
d = int(input("enter fourth number "))

if a>=b:
    if a>=c:
        if a>d:
            print(a,"is greater")
        else:
            print(d,"is greater")
    if c>a:
        if c>d:
            print(c,"is greater")
        else:
            print(d,"is greater")
elif b>=a:
    if b>=c:
        if b>d:
            print(b,"is greater")
        else:
            print(d,"is greater")
    if c>b:
        if c>d:
            print(c,"is greater")
        else:
            print(d,"is greater")
elif a == b and b == c and c == d:
    print("all numbers are same")
    
'''

# 4. take positive number input and tell if it is a four digit number or not
'''
n = int(input("enter the number : "))
if n > 999 and n < 10000:
    print(n," is a four digit number")
else:
    print(n," is not a four digit number") 
'''


# 5. take positive number integer input and tell if it is divisible by 5 and 3.
'''
n = int(input("enter the number : "))
if n%5 == 0 or n%3 == 0:
    print("number is either divisible by 5 or 3")
else:
    print("number is not divisible by 5 or 3")

'''


# 5. Determine whether the year is leap year or not

'''
year = int(input("enter the year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
'''

# 6. ternary operator
# 6.1.check if number is even or odd

'''
n = int(input("enter the number"))
ans = "even" if n%2 == 0 else "odd"
print(ans);

'''

# 7.profit or loss

'''
cost_price = int(input("enter the cost price : "))
selling_price = int(input("enter the selling price : "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("seller has made profit of : ",profit," rupees")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("seller has made loss of : ",loss," rupees")
    
'''



a = 10
b = 15
print(f"a + b = {a + b}")
print(a,"+",b,"=",a+b)


