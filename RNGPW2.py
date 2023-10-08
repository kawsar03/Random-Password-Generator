import random
import string

Capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LowerCase_Letters = Capital_letters.lower()
Numbers = "0123456789"
Special_Char = "!£$%^&*()"

include_capital_letters = False
include_lower_case_letters = False
include_numbers = False
include_special_chars = False

Default = ""

print("Random Password Generator" + '\n')

Q2 = input("How secure do you want your password to be? Easy, Medium, or Advanced." + '\n')

if Q2 == "Easy":
    include_capital_letters = True
    include_lower_case_letters = True
elif Q2 == "Medium":
    include_capital_letters = True
    include_lower_case_letters = True
    include_numbers = True
elif Q2 == "Advanced":
    include_capital_letters = True
    include_lower_case_letters = True
    include_numbers = True
    include_special_chars = True

if include_capital_letters:
    Default += Capital_letters
if include_lower_case_letters:
    Default += LowerCase_Letters
if include_numbers:
    Default += Numbers
if include_special_chars:
    Default += Special_Char

amount = 1
length = 10

for x in range(amount):
    password = "".join(random.sample(Default, length))
    print(password)
