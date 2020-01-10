#Write a program to actually
# play the puzzle, 7 letter input, the first is the key letter, print out all words that can be made with the 7 letters.
#(proper nouns x, less than 4 letters x, no punctuations, marking the key letter-> the first letter)


import re
import os.path
from os import path

print("hello")
if path.exists("cleanDictionary.txt"):
    os.remove("cleanDictionary.txt")

output_file = open("cleanDictionary.txt", "w+")
input_file = open("dictionary.txt", "r+")


for word in input_file:
    #check for proper nouns
    if word[0].isupper():
        continue
    #check for words less than 4 letters
    if len(word) < 5:
        continue
    #check for illegal characters/numbers
    if re.search("[~!#$%^&*()_+{}:.,-;\'1234567890]", word):
        continue
    output_file.write(word)


while True:
    output_file = open("cleanDictionary.txt", "r+")
    print("Input 7 letters (to exit 0): ")
    input_letters = str(input())
    if input_letters == "0":
        break
    for word in output_file:
        if not input_letters[0] in word:
            continue
        if re.match('^['+input_letters+']+$', word):
            print(word)
