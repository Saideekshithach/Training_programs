# Step 1: Define the custom exception
class InsufficientFundsError(Exception):
    pass  # No extra code needed for simple custom exceptions

# Step 2: Use the custom exception
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough money to withdraw")
    return balance - amount

# Step 3: Handle the exception
try:
    balance = 1000
    amount = 1500
    new_balance = withdraw(balance, amount)
    print("Withdrawal successful. New balance:", new_balance)

except InsufficientFundsError as e:
    print("Error:", e)
