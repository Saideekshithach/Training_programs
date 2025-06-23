# Step 1: Define the custom exception
'''class NegativeNumberError(Exception):
    """Exception raised when a negative number is provided where not allowed."""
    def __init__(self, number):
        self.number = number
        self.message = f"Negative number error: {number} is not allowed."
        super().__init__(self.message)

# Step 2: Function that uses the custom exception
def square_root(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number ** 0.5

# Step 3: Using the function and handling the exception
try:
    num = float(input("Enter a number to find the square root: "))
    result = square_root(num)
    print(f"The square root of {num} is {result}")
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}")
except ValueError:
    print("Invalid input. Please enter a valid number.")'''


'''class odd(Exception):
    pass
def evenorodd(num):
    try:
        if num%2==0:
            print("even number")
        else:
            raise odd("number is odd")
    except odd as e:
        print(f"prints message like {e}")
num=int(input("enter num:"))
evenorodd(num)'''
        
'''s="hello"
print(s[2])/print(s[-2])
 
 
s="python"
print(s[-7])'''



a=input()
if a in ['a','e','i','o','u']:
    print("vowel")
else:
    print("not a vowel")
    
        
