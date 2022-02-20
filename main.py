# LISTS
# creating a list
numbers = [10, 12, 34, -21]
print(numbers)
# adding a new element at the end of a list
numbers.append(1)
print(numbers)
# adding an item at a specified location in the list
numbers.insert(0, 45)
# removing last element from list
numbers.pop()
print(numbers)
# retrieve an element from the list
print(numbers[0])
# to modify an item
numbers[0] = 29
print(numbers)
# determine number of items on a list
print(len(numbers))
# looping over lists
for number in numbers:
    print(number)
# to check index of an item
print(numbers.index(29))

# TUPLES
# creating a tuple
coordinates = (12, 5)
print(coordinates)
# accessing tuples using their index
print(coordinates[1])

# SETS
# removing duplicates from a list
numbers = [9, 6, 3, 4, 9, 3]
unique_numbers = set(numbers)
print(unique_numbers)
# union of sets
first_set = {3, 4, 6}
second_set = {4, 5, 9}
print(first_set | second_set)
# intersection of sets
print(first_set & second_set)
# difference between two sets
print(first_set - second_set)
# symmetric difference between sets
print(first_set ^ second_set)
# iterating over elements in a set
numbers = {3, 7}
for x in numbers:
    print(x)

# DICTIONARIES
# creating a dictionary
user = {'name': 'James', 'age': 28, 'hobbies': ['coding', 'jogging']}
print(user)
# accessing a specific key
print(user['name'])
# adding a key to the dictionary
user['email'] = 'male@gmail.com'
print(user.get('email'))
# changing value of a key
user['name'] = 'Peter'
print(user)
# to modify several or all values
user.update({'name': 'Reuben', 'age': 21, 'email': 'kreuben@gmail.com'})
print(user)
# to delete a key
del user['hobbies']
print(user)
#  looping through keys and values
for key, value in user.items():
    print(key, value)
