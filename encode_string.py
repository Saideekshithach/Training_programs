'''import re
def parse_encoded(encoded_string):
    parts=re.split('0+',encoded_string)
    return {'first':parts[0],'last':parts[1],'id':parts[2]}
result=parse_encoded('ram000sai000123')
print(result)

from collections import Counter
def extra(original,modified):
    count_org=Counter(original)
    count_mod=Counter(modified)
    for char in count_mod:
        if count_org[char]!=count_mod.get(char,0):
            return char
res=extra("eueiieo","iieoedue")
print(res)

def shadow(sense1,sense2):
    words1=sense1.split()
    words2=sense2.split()
    if len(words1)!=len(words2):
        return False
    for w1,w2 in zip(words1,words2):
        if len(w1)!=len(w2):
            return False
        if set(w1)&set(w2):
            return False
    return True
print(shadow("his friends","our company"))

def duplicate(sense):
    words=sense.split()
    for word in words:
        letters=[char for char in word.lower() if char.isalpha()]
        if len(letters)!=len(set(letters)):
            return True
    return False
print(duplicate("abcdfe"))


def hexa(string):
    hex_values=[format(ord(char),'x') for char in string]
    return ','.join(hex_values)
print(hexa('company'))'''


import datetime
def has_friday13(month,year):
    date=datetime.date(year,month,13)
    if date.weekday()==4:
        return True
    return False
print(has_friday13(4,2023))
    

