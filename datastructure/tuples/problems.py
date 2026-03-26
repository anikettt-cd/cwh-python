


# t = (4, 7, 1, 9, 2)

# max_val = t[0]

# for num in t:
#     if num > max_val:
#         max_val = num

# print(max_val)  

t = (12, 45, 7, 89, 23)

max_val = float('-inf')
second_max = float('-inf')
third_max = float('-inf')

for num in t:
    if num > max_val:
        third_max = second_max
        second_max = max_val
        max_val = num
    elif num > second_max and num != max_val:
        second_max = num
    elif num> third_max and num != max_val and num != second_max:
        third_max = num
       

print(third_max)      
 
