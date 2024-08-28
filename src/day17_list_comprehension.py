my_list = [1, 2, 3, 4, 5]

# Add 1 to each element using for loop
new_list = []
for x in my_list:
    new_list.append(x + 1)
    
print(new_list)

# Add 1 to each element using list comprehension

new_list = [x+1 for x in my_list]
print(new_list)