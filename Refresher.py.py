# Moduls
import random
import math
'''-----------Programming Tasks for refreshing-----------'''

#------------------------------------------
'''Task 1. Get the area of the triangle'''
def area_of_triangle(height, widh, ):
    triangle = height * widh / 2
    print(f"The area of the triangle is: {triangle}")

area_of_triangle(5, 34, )

#------------------------------------------
'''Task 2. Check if a Number is Even or Odd'''
def check(number):
    if (number % 2) == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

check(6)

# --------------------------------------------------
'''Task 3. Reverse a String'''
def reverse(name):
    name = name[::-1]
    print(name)

reverse("mustafa")

# --------------------------------------------------
'''Task 4. Find the Factorial of a Number'''
def factorial(number):
    print(f"The factorial of the number is:", math.factorial(number))

factorial(3)

# --------------------------------------------------
'''Task 5. Check if a String is Palindrome or Not'''
def reverse(name):
    if name[::-1].lower() == name:
        print(f"{name} is polindrome")
    elif name[::-1].lower() != name:
        print(f"{name} is not a polindrome")

reverse("malayalam")

# --------------------------------------------------
'''Task 6. Generate Fibonacci Series up to n terms'''
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

n = 10
fibonacci_numbers = fibonacci(n)
print(fibonacci_numbers)

# --------------------------------------------------
'''Task 7. Find the Largest Among Three Numbers'''
def greater(n1, n2, n3):
    if n1 > n2 and n3:
        print(f"{n1} is greater then {n2} and {n3}")
    elif n2 > n1 and n3:
        print(f"{n2} is greater then {n3} and {n1}")
    elif n3 > n2 and n3:
        print(f"{n1} is greater then {n2} and {n3}")
    elif n1 != n2 and n3:
        print(f"None is greater, all numbers are same")

greater(100, 0, 3,)

# --------------------------------------------------
'''Tast 8. Calculate Simple Interest'''
def intrest(P, R, N):
    print('The principal is', P)
    print('The time period is', R)
    print('The rate of interest is',N)

    display = (P * R * N) / 100

    print('The Simple Interest is', display)
    return display
intrest(8, 6, 8)

# --------------------------------------------------
'''Tast 9. Convert Celsius to Fahrenheit'''
def convert(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius} degree Celsius is equal to\n{fahrenheit} degree fahrenheit")
convert(40)

# --------------------------------------------------
'''Tast 10. Check Leap Year'''
def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} Leap year")
    else:
        print(f"{year} is not a leap year")

leap(1989)

# --------------------------------------------------

'''-----------Programming Challenges-----------'''
# --------------------------------------------------
'''Challenge 1. Find the Median of Three Numbers'''
def median(input1,input2,input3):
    if input2 < input1 and input1 < input3:
        print(f"Median of the above three numbers is: {input1}")
    elif input3 < input1 and input1 < input2:
        print(f"Median of the above three numbers is: {input1}")
    elif input3 < input2 and input2 < input1:
        print(f"Median of the above three numbers is: {input2}")
    elif input1 < input2 and input2 < input3:
        print(f"Median of the above three numbers is: {input2}")
    elif input1 < input3 and input3 < input2:
        print(f"Median of the above three numbers is: {input3}")
    elif input2 < input3 and input3 < input1:
        print(f"Median of the above three numbers is: {input3}")
median(25,15,35)

# --------------------------------------------------
'''Challenge 2. Count the Number of Words in a Sentence'''
def words_count(words):
    count = len(words.split())
    print(f"Number of words are {count}")
words_count("Hello I am a student of BanoQabil 3.0 i am taking advanced python course")

# --------------------------------------------------
'''Challenge 3. Calculate the Sum of Digits in a Number'''
def sum_input(num):

    sum = 0
    for digit in str(num):
     sum += int(digit)

    return f"The total sum of digis is {sum}"

num = 3366
print(sum_input(num))

# --------------------------------------------------
'''Challenge 4. Find the Longest Common Prefix in a List of Strings'''
'''i tried on this one but i cant figure it out'''
def input(word):

    preflix = []
    for char in word:
        if char == word[0]:
            char += preflix
            print(f"longest preflix is {preflix} ")
    return char

# --------------------------------------------------
'''Challenge 5. Check if a Number is a Prime Number'''
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
prime_checker(75)

# --------------------------------------------------
'''i couldnt complete the bonus challenge'''