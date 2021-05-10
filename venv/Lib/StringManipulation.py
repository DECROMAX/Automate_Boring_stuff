# chapter 6 "String Manipulation uncomment to run line


# new line escape:  char \n

#print(r"Hello there!\nHow are you?\nI am doing fine.")

# raw string: (use 'r' infront of string to return/print raw string)
# ie if string contains \n, it will ignore and print raw string

#print(r'ryan\n is\n a\n god')

# multi line quote: use three quotes any tabs / new lines are considered part of the string , python indentation does
# not apply to lines inside the string.

#print("""
#Dear Ryan

#Snoot's has been arrested for being the most ugly dog in the world

#yours sincerly
#Ryan Lynch""")

# Example of multiline comments using triple quotes , this is used for comments that span multiple lines

"""
This is a test Python program written by Ryan Lynch

Designed for Python 3.9
"""
# indexing strings: think as strings as lists each charecter as an item with corresponding index , output first 3 char
# of variable on each new line 'H,e,l'

# spam = 'Hello world'
# print(spam[0])
# print(spam[1])
# print(spam[3])

# slicing string using a range: same princible as above , this captures a slice of spam variable and stores in a
# variable called 'fizz'  outputs 'Hello'

# spam = ('Hello world')
# fizz = spam[0:5]
# print(fizz)
#outputs 'Hello'

# in and not operators in strings: an expression with two strings joined using 'in' or 'not in' will output a
# boolean True or False value

# 'Hello' in 'Hello world'
# True
# 'Hello' in 'Hello'
# True
# 'HELLO' in 'Hello world'
# False (due to differing case)
# '' in 'spam'
# True
# 'cats' not in 'cats and dogs'
# False

# putting strings in other strings: use of concatenation to join strings.


# name = 'al'
# age = 4000
# print('Hello, my name is ' + name.title() + '. I am ' + str(age) + ' years old!')
# outputs : Hello, my name is Al. I am 4000 years old!

# upper(), lower() method: used for coverting case in strings.
# This outputs HELLO WORLD
# spam = 'Hello world'
# spam = spam.upper()
# print(spam)

# upper(), lower() method: this can be used for case sensitive input comparison
# print('How are you')
# feeling = input()
# if feeling.lower == 'great':
#     print('I Feel great too!')
#else:
    #print('I hope the rest of the day is good!')

# isupper() and islower : returns a boolean value if the string has a least one letter and all the letters are
# uppercase or lower case.
# spam = 'Hello world'
# spam.islower()
# False , due to uppercase 'H'
# spam.isupper()
# False , lowercase text after 'H'
# 12345yes.islower()
# True , num and lower case
# 12345.isupper()
# False num value



# other string  methods
# isalpha() : returns True if the string consists only of letters and isnt blank.

#'hello'.isalpha()
# True
#print('hello123'.isalpha())
# False

# .isalnum() : returns True if the string consists only of letters and numbers and is not blank.
#print('hello'.isalnum())
# True

# isdecimal() : returns True if the string consists of only numeric characters.
#'123'.isdecimal()
# True



# isspace() : returns True if the string consists of only spaces, tabs and newlines and is not blank.
#'   '.isspace()
# True

# istitle() : returns True if string is string is in title case.
#'This Is Title Case'.istitle()
# True

# is----() methods are useful for validating input (see example below)

# while True:
#     print('Enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number')


# while True:
#     print('Select a new password (letters and numbers only')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers')

# .startswith() , endswith() methods : return true begins or ends with string passed to method.

#print('Hello world'.endswith('world'))
# True

#print('hello world'.endswith('hello'))
# False

#print('Spam and chips'.startswith('Spam'))
# True

#Join() method : joins strings toghether to form one string value.
#print(' for '.join(['cats', 'bats', 'rats']))
#outputs : cats for bats for rats

#print(','.join(['Spam', 'Chips', 'Egg']))
# outputs Spam,Chips,Egg   (inserts colon) 

# .split() method: splits the string to seperate words/values and outputs to list
#print('Snoots is a very ugly dog'.split()) # (defualt split method is space)
# returns : ['Snoots', 'is', 'a', 'very', 'ugly', 'dog']

# .split() method tip you can define split points inside ()  see below for example
#print('Sn#oot#s i#s a ver#y u#gly d#og'.split('#'))
# returns : ['Sn', 'oot', 's i', 's a ver', 'y u', 'gly d', 'og']

# .partition() method splits the the string into text before and after a defined separator string and returns a tuple
# of three substrings for the 'before', 'seperator' and 'after' substrings. 

#print('spam eggs and chips'.partition('eggs'))
# returns ('spam ', 'eggs', ' and chips')

# .rjust() method returns a paddded version of the string that is called
# print('hello, world'.rjust(43))
# returns:                                               hello, world

# You can also use rjust() to specify fill character
# print('hello'.rjust(20, '*'))
# outputs: ***************hello

# .ljust() method works the oppsite of .rjust() and places charactures to the left of the string
# print('hello, world'.ljust(20,'*'))
# hello, world********

# .center() method works like ljust and rjust but centers the text.
#print('hello'.center(20, '-'))
# outputs: -------hello--------

# .strip() removes whitespace or specified charactures that are passed
# spam = 'SpamSpamSpamBaconSpamEggsSpamSpam'
# print(spam.strip('Spam')) # strips 'Spam' from before and after first and last occurance of Bacon , Eggs
# returns BaconSpamEggs

# spam = 'SpamSpamSpamBaconSpamEggsSpamSpam'
# print(spam.rstrip('Spam')) # strips spam from right of eggs
# returns: SpamSpamSpamBaconSpamEggs


# spam = 'SpamSpamSpamBaconSpamEggsSpamSpam'
# print(spam.lstrip('Spam')) # strips spam from left of bacon
#returns: BaconSpamEggsSpamSpam

# the pyperclip module has the abilty to copy and paste text form the computers clipboard, sending the output to the
#clipboard will make easy to paste it in a email, word processor etc.

# import pyperclip
# pyperclip.copy('Hello world')
# print(pyperclip.paste())
# Outputs: 'Hello world'

