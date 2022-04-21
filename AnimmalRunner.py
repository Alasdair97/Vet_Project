from Animal import Cat,Dog,Pigeon

#obj = Pigeon()
#print(obj.eat())
charlie = Pigeon(2,'Charlie')
#charlie.name = "Charlie"
#charlie.age = int(2)


print(charlie.name)
print('Is Charlie alive ?')
print(charlie.IsAlive)
print('Is Charlie Healthy?')
charlie.healthCheck('Healthy')
print(charlie.health)

charlie.weightCheck()
print (charlie.weight)
print('\n')

print('Charlie is kicked')
charlie.die()
print('Is Charlie alive')
print(charlie.IsAlive)
print('Is Charlie Healthy?')
print(charlie.health)
