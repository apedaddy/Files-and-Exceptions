my_file = ('pi_million_digits.txt')

with open(my_file) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

''' CHECK IF BIRTHDAY APPEAR IN PI_DIGITS OR NOT'''
birthday = input("Please enter your birthday in (MMDDYY) format: ")

if birthday in pi_string:
    print ("Your birthday appear in pi decimal digits")
else:
    print("Your birthday didn't appear in pi decimal digits")

''' CHECK WHICH NUMBER APPEAR MOST IN THE PI_MILLION DIGITS'''
print()
for checker in range (0,10):
    count_digits = pi_string.count(str(checker))
    if checker !=3:
        print(f"{checker} : Appear {count_digits} times in PI Million Decimal points")
    else:
        print(f"{checker} : Appear {(count_digits - 1)} times in PI Million Decimal points")


