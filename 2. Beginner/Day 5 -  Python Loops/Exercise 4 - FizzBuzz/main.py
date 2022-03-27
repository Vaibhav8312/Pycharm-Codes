########################## METHOD 1 ##############################

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} - Fizz Buzz')
    elif num % 3 == 0:
        print(f'{num} - Fizz')
    elif num % 5 == 0:
        print(f'{num} - Buzz')
    else:
        print(num)

############################ METHOD 2 ##################################

for num in range(1, 101):
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    print(output if output != "" else num)
    '''This method inside print statement is called a ternary conditional operator.
    The expression syntax is: "a if condition else b"
    First condition is evaluated, then exactly one of either a or b is evaluated and returned based 
on the Boolean value of condition. If condition evaluates to True, then a is evaluated and returned but b is ignored, 
or else when b is evaluated and returned but a is ignored. 

This allows short-circuiting because when condition is true only a is evaluated and b is not evaluated at all, 
but when condition is false only b is evaluated, and a is not evaluated at all. '''

######################## METHOD 3 ########################

# Without ternary conditional operator

for num in range(1, 101):
    text = ""
    if num % 3 == 0:
        text += 'Fizz'
    if num % 5 == 0:
        text += 'Buzz'
    if text == '':
        text = num
    print(text)

##################### METHOD 4 ########################

for num in range(1, 101):
    fizzbuzz = ""
    if num % 3 == 0:
        fizzbuzz += "Fizz"
    if num % 5 == 0:
        fizzbuzz += "Buzz"
    if len(fizzbuzz) == 0:
        fizzbuzz += str(num)

    print(fizzbuzz)

######################### METHOD 5 ##########################

for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print(f'{i} - Fizz Buzz')
        else:
            print(f'{i} - Fizz')
    elif i % 5 == 0:
        print(f'{i} - Buzz')
    else:
        print(i)
