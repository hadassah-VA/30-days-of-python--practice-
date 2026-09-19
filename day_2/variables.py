# Day 2: 30 Days of python programming
import math
first_name = "Hadassah"
last_name = "Esther"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Lagos"
age = 27
year = 2026
is_married = False
is_true = True
is_light_on = False
a, b, c = 5, 10, 15
print(type(first_name))
print(type(age))
print(type(is_married))
print(len(first_name))
print(len(first_name) > len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
floor_division = num_one // num_two
print(floor_division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
print(area_of_circle)
print(circum_of_circle)
first_name_input = input("Enter your first name: ")
last_name_input = input("Enter your last name: ")
country_input = input("Enter your country: ")
age_input = input("Enter your age: ")
print(first_name_input, last_name_input, country_input, age_input)
print(help('keywords'))
