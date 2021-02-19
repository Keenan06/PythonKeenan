#5.1
game = 'asc'
print("Is game == 'asc'? I predict true.")
print(game == 'asc')
game = 'cod'
print("Is game == 'cod'? I predict true.")
print(game == 'cod')
game = 'fifa'
print("Is game == 'fifa'? I predict true.")
print(game == 'fifa')
game = 'killzone'
print("Is game == 'killzone'? I predict true.")
print(game == 'killzone')
game = 'pop'
print("Is game == 'pop'? I predict true.")
print(game == 'pop')
game = 'asc'
print("Is game == 'killzone'? I predict false.")
print(game == 'killzone')
game = 'killzone'
print("Is game == 'asc'? I predict false.")
print(game == 'asc')
game = 'fifa'
print("Is game == 'asc'? I predict false.")
print(game == 'asc')
game = 'cod'
print("Is game == 'asc'? I predict false.")
print(game == 'asc')
game = 'Pop'
print("Is game == 'pop'? I predict false.")
print(game == 'pop')
#5.2
foods = ['Steak', 'mash', 'peas', 'pizza', 'burgers']
print('steak'in foods)
for food in foods:
    if food.lower() == 'steak':
        print('true')
    else:
        print('false')

for food in foods:
    if 'anchovies' in foods:
        print('true')
    else:
        print('false')

num = 8
print(num == 8)
print(num > 6)
print(num < 9)
print(num => 10)
