'''def append_to_list(value, lst=[]):
    lst.append(value)
    return lst
 
print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))


funcs = [lambda x: x+i for i in range(3)]

results = [f(10) for f in funcs]

print(results)




a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True  → same contents
print(a is b)


a=[1,0,5,0,6,2,0,9]
b=[]
for i in a:
    if i==0:
        a.remove(i)
        b.append(i)
d=sorted(a)
print(d+b)'''


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in nums:
    if num % 2 == 0:
        nums.remove(num)
print(nums)
print("abc" * 0)



a = [1, 2, 3]
print(a[3])
            
        
 
