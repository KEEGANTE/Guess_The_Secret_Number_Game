secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
# Read the first number.
number = int(input("Enter a number: "))
 
# 0 terminates execution.
while number != 0:
    if number != 777:
        
       print ("Ha ha! You're stuck in my loop!")
       number = int(input("Enter a number: "))
    else:
        
        number == secret_number
        print ("Well done, muggle! You are free now. ")
