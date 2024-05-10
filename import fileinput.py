import fileinput
meals = ['', '', '']
x = 0
class newMeal():
    def __init__(self, name, date):
        
with fileinput.input(files='thing.txt') as file:
    for data in file:
        data = data.split(' - ')
        meals[x] = [data[0], data[1]]
        x = x + 1
print(meals)