# Write a function that uses while,
# if and continue statements to print 
# all the even numbers between 0 and 50.
def even_numbers():
    i = 0
    while i < 50:
        i +=1
        if i % 2 != 0:
            continue
        print(i)
even_numbers()


# Write a function that takes an integer
# argument and prints "Prime" 
# if the number is prime, and "Not prime" 
# if the number is not prime
def prime_numbers(intX):
    if intX % 1 ==0 and intX % intX == 0:
        print("Prime number")
    else:
        print("Not a prime number")

prime_numbers(12)



# Write a function that takes a list
# of integers as input and prints the
#  sum of all the even numbers in the list.

def listx(*listInt):
    x = 0
    for i in listInt:
        if i % 2 == 0:
            x += i
    print(x)
            
listx(1,2,4,6,8,0,9)


# Write a function that takes any two integers as input,
#  and prints the sum of all the numbers between
#  the two integers (inclusive) that are divisible by 3.

def sum(integers,integer):
    add = 0
    for int in range(integers,integer+1):
        if int % 3 == 0:
            add  += int
    print(add)
sum(2,30)


