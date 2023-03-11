types_of_people = 10 #creates a variable called types_of_people
x = f"There are two {types_of_people} types of people." #creates a new variable "x" formats the variable to call the previous variable created (types_of_people)

binary = "binary" #creates a variable binary with a string of the word binary
do_not = "don't" #creates a variable do_not with the string "don't"
y = f"Those who know {binary} and those who {do_not}." #creates the string "y" formatted to call the two previous variables that place the string inside a string 1/6

print(x) #prints value of varibale "x"
print(y) #prints value of variable "y"

print(f"I said: {x}") #prints variable "x" withing a string 2/6 creatings a string within a string 3/6
print(f"I also said: '{y}'") #prints varible "y" in a string 4/6 in a string 5/6 in a string 6/6

hilarious = False #create a variable with the False boolean
joke_evaluation = "Isn't that joke so funny?! {}" #creates variable joke_evaluation with open brackets to insert varible into when called

print(joke_evaluation.format(hilarious)) #prints joke_evaluation variable and uses format syntax to add hilarious variable into string

w = ("This is the left side of...") #creates variable string "w" with sentence
e = ("a string with a right side") #creates variable string "e" with sentence

print (w + e) #concatinates "w" and "e" strings together


"""
------- Breaking Code -------
* Misspelled/Incorrectly typed variable names :Traceback (most recent call last):
  File "e:\lpthw\ex6.py", line 2, in <module>
    x = f"There are two {types_of_people} types of people." #creates a new variable "x" formats the variable to call the previous variable created (types_of_people)
NameError: name 'types_of_people' is not defined. Did you mean: 'types_o_people'?

* Variable unable to call from variables set lower in code order :Traceback (most recent call last):
  File "e:\lpthw\ex6.py", line 17, in <module>
    print(joke_evaluation.format(hilarious)) #prints joke_evaluation variable and uses format syntax to add hilarious variable into string
NameError: name 'hilarious' is not defined

* Removed one curly brace from varible instered into string :File "e:\lpthw\ex6.py", line 11
    print(f"I said: x}") #prints variable "x" withing a string 2/6 creatings a string within a string 3/6
                       ^
SyntaxError: f-string: single '}' is not allowed

*Removed quotes from string :File "e:\lpthw\ex6.py", line 11
    print(f"I said: {x}) #prints variable "x" withing a string 2/6 creatings a string within a string 3/6
                                            ^
SyntaxError: unterminated string literal (detected at line 11)

*Removed .format from formattted string vaiable call :File "e:\lpthw\ex6.py", line 11
    print(f"I said: {x}) #prints variable "x" withing a string 2/6 creatings a string within a string 3/6
                                            ^
SyntaxError: unterminated string literal (detected at line 11)

*Did not define variable :File "e:\lpthw\ex6.py", line 19
    = ("This is the left side of...") #creates variable string "w" with sentence
IndentationError: unexpected indent
"""