# Write a program that reads an integer number and prints its previous and
# next numbers. See the examples below for the exact format your answers
# should take. There shouldn't be a space before the period.
# Remember that you can convert the numbers to strings using the function str.
# The next number for the number 179 is 180. The previous number for the
# number 179 is 178.)

def next_previos_number(number):
    print(f"The next number for the number {number} is {number+1}. The previous number for the number {number} is {number-1}.")

next_previos_number(150)