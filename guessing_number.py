# guessing_the_number.py
secret_number = 19
number_too_low = 0
number_too_high = 0
total_numbers = 0
number = 0
while number != secret_number:
    number = int(input ("Try to guess by inserting a number: "))
    total_numbers+=1
    print (f"Total numbers are {total_numbers}")
    if number < secret_number:
    	print ("The number is too low.")
    	number_too_low+=1
    	print (f"Numbers that are too low are: {number_too_low} ")
    elif number > secret_number:
    	print ("The number is too high.")
    	number_too_high+=1
    	print (f"Numbers that are too high are: {number_too_high} ")
    
print("Well done. You guessed the number!")

	   

