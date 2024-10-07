# loops in python basics loops
'''
# 1.
for i in [1,2,3,4]:
    print(i)
    
# 2.
for i in range(1,9):
    print(i,end="\n")
    
'''

# 1.print hello world 'n' times . Taken 'n' from user.

'''
n = int(input("enter the value of n : "))

for i in range(1,n+1):
    print("hello world",end="\t")
    
    # or
    
for i in range(n):
    print("hello world",end="\t")
'''

# 2.print numbers from 1 to 100
'''
for i in range(1,101):
    print(i,end=" ")
    
'''

# 3.print even number from 1 to 100
'''
for i in range(2,101,2):
    print(i,end=" ")
'''

  
# 4.print odd number from 1 to 100
'''
for i in range(1,101,2):
    print(i,end=" ")
'''

# 5. Display this AP - 1,3,5,7,9.. upto ‘n’ terms.
'''
n = int(input("enter the nth number : "))
current_term = 1
common_difference = 2

print("\nAP:", end = " ")
for _ in range(n-1):
    print(current_term, end=", ")
    current_term += common_difference
# this function is outsize the loop for printing the last nth digit of the term
print(current_term)

'''

# 6. break statement :- exit or terminate a loop.
'''
for i in range(1,10):
    print(i,end = " ")
    if i == 7:
        break;
'''

# 7.continue statement :- skip the current iteration of a loop and move to the nwxt iteration
'''
for i in range(1,10):
    if i == 5:
        continue
    print(i,end=" ")
'''

# 8.pass statement :- used as a placeholder to indicate that the code will be added later
'''
for i in range(1,10):
    if i == 5:
        pass
    else:
        print(i,end=" ")
'''

        

# 9.Find the highest factor of given number ‘n’(except n).
'''
n = int(input("Enter a number: "))
highest_factor = -1
 
# Finding the highest factor
for factor in range(n-1, 0, -1):
    if n % factor == 0:
        highest_factor = factor
        break
 
# Printing the highest factor
print("The highest factor of", n, "is", highest_factor)
'''

# 10.print numbers from 1 to 100 while loop
'''
i = 1
while i < 100:
    print(i,end=" ")
    i = i+1;
'''

# 11.print even numbers from 1 to 100
'''
n = int(input("enter the number : "))  
for i in range(n,0,-1):
    print(i,end=" ")
'''

# 12.



n = int(input("enter the nth number : "))
current_term = 1
common_difference = 2

print("\nAP:", end = " ")
for _ in range(n-1):
    print(current_term, end=", ")
    current_term += common_difference
# this function is outsize the loop for printing the last nth digit of the term
print(current_term)




















# right angle triangle of character in increasing order
'''
n = int(input("enter the value of n : "))
for i in range(1,n+1):
    ch = 'A'
    for j in range(1,i+1):
        print(ch,end = " ")
        ch = chr(ord(ch) + 1)
    print()     #for new line 
    
'''


    
