'''def wrap_string(s, w):
    for i in range(0, len(s), w):
        print(s[i:i+w])

# Example usage
S = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
W = 4
wrap_string(S, W)
import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []

    for i in range(size):
        # Create the left part: from current letter to 'a'
        left = alpha[size-1:i:-1]
        # Create the right part: from 'a' to current letter
        right = alpha[i:size]
        # Join both with '-'
        full = '-'.join(left + right)
        # Center align with fill character '-'
        line = full.center(4 * size - 3, '-')
        lines.append(line)

    # Combine top + bottom (reverse of top minus the center line)
    print('\n'.join(lines[::-1] + lines[1:]))

# Example usage
print_rangoli(3)
print()  # Empty line for spacing
print_rangoli(5)

import calendar

def find_day(month, day, year):
    day_index = calendar.weekday(year, month, day)
    return calendar.day_name[day_index].upper()

# Input
month, day, year = map(int, input().split())

# Output
print(find_day(month, day, year))

# Read input
m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

# Compute symmetric difference and sort it
sym_diff = sorted(m_set.symmetric_difference(n_set))

# Print each element in a new line
for num in sym_diff:
    print(num)
b=[]
string=input().split()
for i in string:
    a=i[::-1]
    b.append(a)
print(" ".join(b))


# Accept input from the user
input_string = input()

# Reverse the string
reversed_string = input_string[::-1]

# Print the result
print(reversed_string)

# Total heads and legs
total_heads = 35
total_legs = 94

# Iterate over all possible numbers of chickens (0 to total_heads)
for chickens in range(total_heads + 1):
    rabbits = total_heads - chickens
    legs = chickens * 2 + rabbits * 4
    if legs == total_legs:
        print(f"Chickens: {chickens}, Rabbits: {rabbits}")
        break


a=[1,3,6,78,35,55]
b=[12,24,35,24,88,120,155]
c=set(a).intersection(set(b))
print(c)


class person:
    def getgender(self):
        pass
class male(person):
    def getgender(self):
        return "male"
class female(person):
    def getgender(self):
        return "female"
m=male()
f=female()
print(m.getgender())
print(f.getgender())'''

string=input()
for i in string:
    if string.index(i)%2==0:
        print(i,end="")
        



