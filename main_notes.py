import random

# For loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension
new_numbers = [n + 1 for n in numbers]

# String as list
name = "Adrian"
letter_list = [letter for letter in name]

# Range as List
range(1,5)
range_list = [num * 2 for num in range(1,5)]

# Conditional List comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# schema # new_names = [new_item for item in items if test]
short_names = [name for name in names if len(name) < 5] # if name is length less than 5 then add to new list
long_names = [name.upper() for name in names if len(name) > 5]

# dictionary comprehension
students_scores = {student:random.randint(1, 100) for student in names}

# passed_students = {new_key:new_value for (key, value) in dictionary.items()}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60} #zdany student

####################################

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
# for word in sentence.split():
#     print(word)

result = {word:len(word) for word in sentence.split()}

print(result)


##############################################################

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# weather_f = {new_key:new_value for (key, value) in dictionary.items()}
weather_f = {day:(temp_c*9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
######################################################################

# write same numbers in 1 and 2
with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

#result = [new_item for item in list if test]
result = [int(num) for num in file1_data if num in file2_data]

# Write your code above 👆

print(result)

#########################################################################

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# for word in sentence.split():
#     print(word)

result = {word:len(word) for word in sentence.split()}

print(result)

#########################################################################
