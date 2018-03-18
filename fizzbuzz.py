print ("Welcome to the FizzBuzz Game")
number_int=raw_input("Please enter a number between 1 and 100: ")
number_int=int(number_int)

for number_int in range(1, number_int+1):
    if number_int % 3 == 0 and number_int % 5 == 0:
        print("fizzbuzz")
    elif number_int % 3 == 0:
        print("fizz")
    elif  number_int % 5 == 0:
        print("buzz")
    else:
        print number_int
except Exception as e: 
    print "Please enter a whole number."