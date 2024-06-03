def print_numbers(number):
    numbers=range(number)
    for num in numbers:
        print (num)
# The if statement checks for comparison to check if true or false.
def print_even_numbers(number):
    numbers=range(number)
    for num in numbers:
        if num%2==0:
            print(num)
# else statement is optional ant a t times it is combined with the if statement.
# a code in the else statement is executed if the preceding if statement returns false 
            
def check_numbers(number):
    number=range(number)
    for num in number:
        if num%2==0:
            print (f"{num} is even")
        else:print(f"{num} is odd")

# elif statement allows us to do more than one comparison.
    
def check_divisibility(number):
    numbers= range(number)
    for num in numbers:
        if num%3==0:
            print(f"{num} is divisible by 3")
        elif num%5==0:
            print(f"{num} is divisible by 5")
        elif num%7==0:
            print(f"{num} is divisible by 7")
        else:
            print(f"{num} in not available")
    
# while loop.Continuue sto iterate a long as the condition is true
def countdown(n):
    x=0
    while n>x:
     print(n)
     n-=1  

# break statement stops the while loop even if the set condition is still true

def count_down(number):
    x=0
    while number>x:
        if number==5:
            break
        print(number)
        number-=1

# continue statement . skips the current iteration loop and jumps to the next iteration of the while loop.

def divisible_by7(number):
    x=1
    while x<=number:
        x+=1
        if x%7!=0:
            continue
        print(f"{x} is divisible by 7")

# using while,continue and if statements, write a function that prints all the odd numbers between 0 and 100.
# create  afunction named fizzbuzz for numbers divisible by 3 it prints fizz, for numbers divisible by 5 it prints buzz
# for the rest it prints fizzbuzz.  
        
def odd_numbers(number):
    numbers=range(number)
    while numbers==number:
        if numbers%2==0:
            continue
        print(f"{numbers} is odd number")


def fizzbuzz(number):
    numbers= range(number)
    for num in numbers:
        if num%3==0:
            print("fizz")
        elif num%5==0:
            print("buzz")
        else:
            print("fizzbuzz")

