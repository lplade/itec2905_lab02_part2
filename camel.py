#!/bin/python3

# Write a program that turns a sentence into camel case. The first word is
# lowercase, the rest of the words have their initial letter capitalized, and
# all of the words are joined together. For example, with the input
# "fOnt proCESSOR and ParsER", your program will output
# "fontProcessorAndParser".
#
# Optional extra question: print a warning message if the input will not
# produce a valid Python variable name. You don't need to be exhaustive in
# checking, but test for a few common issues, such as starting with a number,
# or containing invalid characters such as # or + or ".
#
# Test your program, and comment your code.

def display_banner():
    '''Display program name in a banner'''
    msg = "AWESOME camelCaseGenerators PROGRAM"
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')


display_banner()

print("Enter a sentence and I will camelCase it.")
input_sentence = input("> ")

new_word = False
output_sentence = ""
first_is_letter = False

# loop over that string
for char in input_sentence:
    if char == ' ':
        new_word = True
        # just flip flag, ignore for output purposes
    elif not (char.isalpha() or char.isalnum()):
        print("Omitting invalid character \'" + char + "\'")
    else:
        #case for every character after the first
        if first_is_letter:
            if new_word is True:
                output_sentence += char.upper()
            else:
                output_sentence += char.lower()

        #special case that occurs until the first letter in the string
        else:
            if char.isalpha():
                first_is_letter = True
                output_sentence += char.lower()
            else:
                print("Omitting invalid leading character \'" + char + "\'")

        new_word = False


print("Here is your string in camelCase:")
print(output_sentence)
