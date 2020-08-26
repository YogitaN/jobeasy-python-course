# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = "Python is programming language"
char_1 = 'a'

result_1 = 0
c = 0
while c < len(string_1):
    if string_1[c] == char_1:
        result_1+=1
    c+=1
print(result_1)


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 5234
temp = number_1
result_2 = 1


while( temp > 0):
    result_2 *= temp % 10
    temp //= 10

print(result_2)


# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 236789
temp = number_2
result_3 = 0

while(temp > 0):
    remainder = temp %10
    result_3 = (result_3*10)+remainder
    temp //=10

print(result_3)
