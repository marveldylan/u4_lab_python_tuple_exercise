# Exercise 1
students = ['Billy', 'Joe Bob', 'Nancy']
print(students[1])

# Exercise 2
foods = ('pizza', 'hot dogs', 'ramen')

for food in foods:
    print(food + ' is good food')

# Exercise 3
for food in foods[1:3]:
    print(food)

# Exercise 4
home_town = {
    "city": "Duluth",
    "state": "Minnesota",
    "population": "87000"
}

print("I was born in " + home_town["city"] + ", " + home_town["state"] + " - population of " + str(home_town["population"]))

# Exercise 5
for key in home_town:
    print(key + "=" + home_town[key])

# Exercise 6
cohort = []
for num in range(0, len(students)):
    pair = {}
    pair[students[num]] = foods[num]
    cohort.append(pair)
print(cohort)

# Exercise 7
awesome_students = []
for student in students:
    awesome_students.append(student + ' is awesome!')
print(awesome_students)

# Exercise 8
for food in foods:
    print_food = False
    for char in food:
        if char == 'a':
            print_food = True
    if print_food == True:
        print(food)