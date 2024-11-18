# Practicing Math Functions
import math

x = float(input('Enter first number:'))
y = float(input('Enter second number:'))
z = float(input('Enter third number:'))

num1 = (math.pow(x, z))

print(f'{num1:.2f}', end=' ')

num2 = (math.pow(x, math.pow(y, z)))

print(f'{num2:.2f}', end=' ')

num3 = (math.fabs(x - y))

print(f'{num3:.2f}', end=' ')

num4 = (math.sqrt(math.pow(x, z)))

print(f'{num4:.2f}')

#Using Len to count the characters.
george_v = "His Majesty George V, by the Grace of God, " \
           "of the United Kingdom of Great Britain and " \
           "Ireland and of the British Dominions beyond " \
           "the Seas, King, Defender of the Faith, Emperor of India"
gandhi = 'Mohandas Karamchand Gandhi'
john_f_kennedy = 'JFK'

print(len(george_v), 'characters is much too long of a name!')
print(len(gandhi), 'characters is better...')
print(len(john_f_kennedy), 'characters is short enough.')

#Accessing list elements
lamborghini_veneno = 3900000  # $3.9 million!
bugatti_veyron = 2400000      # $2.4 million!
aston_martin_one77 = 1850000  # $1.85 million!

prices = [lamborghini_veneno, bugatti_veyron, aston_martin_one77]

print('Lamborghini Veneno:', prices[0], 'dollars')
print('Bugatti Veyron Super Sport:', prices[1], 'dollars')
print('Aston Martin One-77:', prices[2], 'dollars')

#Program to calculate statistics from student test scores.
midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]

#Combine the scores into a single list
all_scores = midterm_scores + final_scores

num_midterm_scores = len(midterm_scores)
num_final_scores = len(final_scores)

print(num_midterm_scores, 'students took the midterm.')
print(num_final_scores, 'students took the final.')

#Calculate the number of students that took the midterm but not the final
dropped_students = num_midterm_scores - num_final_scores
print(dropped_students, 'students must have dropped the class.')

lowest_final = min(final_scores)
highest_final = max(final_scores)

print('\nFinal scores ranged from', lowest_final, 'to', highest_final)

# Calculate the average midterm and final scores
# Hint: Sum the midterm scores and divide by number of midterm takers
#       Repeat for the final
average_midterm_scores = sum(midterm_scores)
average_midterm_scores = average_midterm_scores / num_midterm_scores
print('Average midterm score is: ', f'{average_midterm_scores:.2f}')

avg_final_score = sum(final_scores)
avg_final_score = avg_final_score / num_final_scores
print('Average final score is: ', f'{avg_final_score:.2f}')

# importing tuples for lists
from collections import namedtuple

Car = namedtuple('Car', ['make','model','price','horsepower','seats'])  # Create the named tuple

chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)  # Use the named tuple to describe a car
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)  # Use the named tuple to describe a different car

print(chevy_blazer)
print(chevy_impala)

#Adding and removing names from a set
male_names = {'Oliver', 'Declan', 'Henry'}
names_to_remove = input()
names_to_add = input()

male_names.remove(names_to_remove)
male_names.add(names_to_add)

print(male_names)