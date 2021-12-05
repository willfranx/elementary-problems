# 1. Write a program that prints ‘Hello World’ to the screen.

print('Hello World') 

# 2. Write a program that asks the user for their name and greets them with their name.

name = input('What is your name? ')
print('Hello ' + name + '!') 

# 3. Modify the previous program such that only the users Alice and Bob are greeted with their names.

name = input('What is your name? ')
if name.lower() == 'bob':
    print('Hello Bob!')
elif name.lower() == 'alice':
    print('Hello Alice!')
else: print('You are not Bob or Alice. Goodbye!') 

# 4. Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.

num = int(input('Please Enter a number: '))
return_num = 0

for i in range (1, num+1):
    return_num += i
    print (return_num) 

# 5. Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

num = int(input('Please Enter a number: '))
return_num = 0

for i in range (1, num+1):
    return_num += i

if i % 3 == 0 | i % 5 == 0:
    print (return_num)
else:
    print('Sorry! This number is not a multiple of 3 or 5. Try again.') 

# 6. Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.

num = int(input('Please Enter a number: '))
choice = str(input('Do you want to calculate the sum or the product? '))

if choice.lower() == 'sum' :
    total = sum(range(1, num + 1))
    print('The sum is: ' + str(total))
elif choice.lower() == 'product':
    product = 1
    for i in range (1, num +1 ):
        product *= i
    print('The product is: ' + str(product)) 

# 7. Write a program that prints a multiplication table for numbers up to 12.

num = int(input('Please enter a number between 1 and 12: '))

def table(num):
    for i in range(1, 13):
        print('%d * %d = %d' % (num, i, num * i))

table(num) 


# 8. Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)

#This is an arbitrary range that you can change:
lower = 1
upper = 600

print('Prime numbers between', lower, 'and', upper, 'are: ')

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num) 

# 9. Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

import random

upper_limit = random.randint(0, 50)
lower_limit = random.randint(50, 100)

answer = random.randint(upper_limit, lower_limit)
attempts = 0
while True:
    guess = int(input('Please guess the secret number: '))
    if guess > answer:
        print('That number is too high. Aim lower.')
        attempts += 1
    elif guess < answer:
        print('That number is too low. Aim Higher.')
        attempts += 1
    if guess == answer:
        break   
if guess == answer: 
    print('You guessed correctly! That is the secret number.')
    print('It took you ' + str(attempts) + ' tries to find it.') 

# 10. Write a program that prints the next 20 leap years.

def loop_year(year):
    y = 0
    while y < 20:
        if year % 4 != 0 and year % 400 != 0:
            year +=1
        elif year % 100 != 0:
            year +=1
            print('{} is a leap year'.format(year))
            y += 1


loop_year(2021)