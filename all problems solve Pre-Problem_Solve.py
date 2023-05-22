#Python program to implement a stack data 
# structure using a list. It includes a push,
#  pop, and display operations:

class Stack:  
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    return self.stack.pop()

  def display(self):
    
    for element in self.stack:
      print(element, end=" ")
    print()


if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.display()
  element = stack.pop()
  print("The popped element is:", element)
  stack.display()



#write a program that takes
#  a list of string as input
#  from user and prints the longest
#  string from the list.
def find_longest_string(list):
    longest_string = ""
    for string in list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


if __name__ == "__main__":
    list = list(map(str, input("Enter a list of strings: ").split()))
    print("The longest string in the list is:", find_longest_string(list))




#write a python program that reads
#  a text file and counts the 
# frequency of each word in the file.
#  Display the top three most
#  frequent words along 
# with their frequencies.
import collections
def count_words(filename):
  
  with open(filename, "r") as f:
    words = f.read().split()
  counts = collections.Counter(words)
  return counts
def main():
  filename = input("Enter the name of the text file: ")
  counts = count_words(filename)
  for word, count in counts.most_common(3):
    print(word, count)
if __name__ == "__main__":
  main()



#write a python program that takes a list of integers as input  from user and prints the sum all of even numbers in the list
def sum_even_numbers(list):
    sum= 0
    for x in list:
        if x % 2 == 0:
            sum += x
    return sum

if __name__== "__main__":
    list = list(map(int, input("Enter a list of integers: ").split()))
print("The sum of all even numbers in the list is:", sum_even_numbers(list))



#write a python program thats take two numbers as input and print their sum
num1 = int(input("enter your number 1: ",))
num2 = int(input("enter your number 2: ",))
sum = num1 + num2
print(sum)
#1. check if a given number is prime ....
number = int(input("enter your number to check prime:",))

def check_prime(number):
    if number > 1 :
        for x in range(2, number):
            if (number % x) ==0 :
                print("not prime")
                break            
        else:
            print("number is prime")
    else:
        print("number is not prime")

check_prime(number
)

3. #reads strings and prints the count of each vowel in the string.abs)......

mystring = input("enter your string", )

def check_vowel(mystring):
    count = 0
    for x in mystring:
        if x in "aeiou":
            count +=1
    print(count)


check_vowel(mystring)
# # 1) Write a Python function 
# to sum all the numbers in a list
# # Sample list: [8, 2, 3, 0, 7]
def  sum_of_numbers(my_list):
    sum = 0
    for x in my_list:
        sum += x
    return sum

print(sum_of_numbers(my_list=[10,20,30,40]))




# 2) Write a Python function that accepts 
# case letters and lower case letters
# Sample list: “The quick Brown Fox”
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def count_upper_lower(string):
    upper_case = 0
    lower_case = 0
    for char in string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
    return f"number of uppercase is  {upper_case}\n and number of lower_case is {lower_case} "
print(count_upper_lower(string = "The quick Brown Fox"))


# 3) Write a Python script to print
#  a dictionary where the keys 
#  are numbers between 1 and 15 (both included) 
# and the values are square of keys
# Expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
result = {}
for num in range(1,16):
    result[num]=num**2
print(result)

# # 4) Write a Python program to 
# sum all the items in a dictionary
# # Sample dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
Sample_dict= {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
sum_of_dict_values = sum(Sample_dict.values())
print(sum_of_dict_values)


# # 5) Write a Python program to 
# create a symmetric difference 
# set of set a and b

# # a = {1, 3, 5, 9, 6}
# # b = {2, 5, 7, 4, 1}
# # Expected output: {3, 2, 7, 9, 6, 4}

a = {1, 3, 5, 9, 6}
b = {2, 5, 7, 4, 1}
symmetric_diff = a.symmetric_difference(b)
print(symmetric_diff)


# # 6) Write a Python program to remove all elements from a given set.
# # Sample input: {3, 2, 7, 9, 6, 4}
# # Expected output: {}
Sample_set= {3, 2, 7, 9, 6, 4}
Sample_set.clear()
print(Sample_set)


#1) If a word remains the same
#  after reversing it then it's a palindrome.
#  Now define a function to detect if a word is palindrome or not

def is_palindrome(word):
    reversed_word = ""

    for char in word:
        reversed_word = char + reversed_word

    return word == reversed_word

print(is_palindrome("eye"))


# 2) 1 kilometer is equal to 0.621371 mile.
#  Now create function that 
# can convert kilometers to mile

def convert_to_miles(kilometers):

    if (type(kilometers) not in [float, int]):
        raise TypeError("Please enter kilometers as a number")

    return kilometers * 0.621371

print(convert_to_miles(5))


# 3) Write a function that can remove punctuation 
# marks from a string
    # punctuations = "!()-[]{};:'"\,<>./?@#$%^&*_~"

def punctuations_remover(string):
    punctuations = "!()-[]{};:\,<>./?@#$%^&*_~"

    fresh_word = ""

    for char in string:
        if char not in punctuations:
            fresh_word += char

    return fresh_word


print(punctuations_remover("He,ll.o>"))


# 4) The Fibonacci sequence is a sequence 
# where the next term is the sum of the 
# previous two terms. 
# The first two terms of the Fibonacci 
# sequence are 0 followed by 1. 
# Now write a program to print fibonacci
#  series up to a certain number

def fibonacci_printer(end_number):
    a, b = 0, 1
    count = 0
    while count < end_number:
        a, b = b, a + b
        print(b)
        count += 1

fibonacci_printer(10)



# 5) Write a function that can take
#  a sentence and print each word of that sentece
#  in alphabetic order

def sort_words_alphabetically(sentence):
    words = sentence.split(" ")
    words.sort()

    for word in words:
        print(word)


sort_words_alphabetically("hi we are learning python and it's awesome")


# 6) Write a function to find even or odd

def number_checker(number):
    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")

number_checker(5)


# 7) Write a program to check 
# if a number is positive, negative or zero

def number_checker(number):
    if number > 0:
        print("Number given by you is positive")
    elif number < 0:
        print("Number given by you is negative")
    else:
        print("Number given by you is zero")

number_checker(-9)


# 8) If any natural number 
# is greater than 1 and having
# no positive divisors other 
# than 1 and the number itself 
# then it's called a prime number.
#  For example: 3, 7, 11 etc are prime numbers.
#  Now write a function that can check
#  if a number is prime number or not

def prime_checker(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(f"{number} is not a prime number")
                break
        else: # NOTICE THIS ELSE BLOCK IS PART OF FOR STATEMENT NOT A PART OF IF STATEMENT
            print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

prime_checker(10)


# 9) Write a function to find the largest number among three given input numbers

def find_largest_number(number1, number2, number3):

    largest = number1

    if (number1 > number2) and (number1 > number3):
        largest = number1
    elif (number2 > number1) and (number2 > number3):
        largest = number2
    else:
        largest = number3

    print(f"The largest number is {largest}")


find_largest_number(15, 23, 8)


# A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,
    # 2017 is not a leap year
    # 1900 is a not leap year
    # 2012 is a leap year
    # 2000 is a leap year

# 10) Now write a function to check if a year is leap year or not

def check_leap_year(year):
    # century year divided by 400 is leap year
    if year % 400 == 0:
        print(f"{year} is a leap year")

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is a leap year")

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        print(f"{year} is not a leap year")


check_leap_year(2009)


# shortcut way
def check_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

check_leap_year(2009)
