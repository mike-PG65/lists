#Create an empty list
my_list = []

# Append the elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)


# List to extend with
additional_list = [50, 60, 70]

# Extend my_list with additional_list
my_list.extend(additional_list)

# Remove the last element
last_element = my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find the index of the value 30
index_of_30 = my_list.index(30)

# Print the index
print(index_of_30) 


# Print the list to verify
print(my_list) 
print(last_element)

