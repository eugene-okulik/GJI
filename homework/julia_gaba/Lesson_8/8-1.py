import random


salary = input("Type your salary: ")
bonus = random.randint(0, 1)

print(bonus)

if bonus is True:
    salary = int(salary) + random.randint(1, 200)

print(salary)
