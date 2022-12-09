# Tuples

groceries = ('bread', 'milk', 'eggs', 'butter', 'cheese', 'milk')
print(groceries)
print(groceries[0])

# Tuples are immutable
# groceries[0] = 'chocolate'    # TypeError: 'tuple' object does not support item assignment

# Sets

groceries = {'bread', 'milk', 'eggs', 'butter', 'cheese', 'milk'}
print(groceries)

# Sets are mutable
groceries.add('chocolate')
print(groceries)

groceries.remove('milk')
print(groceries)

# groceries.remove('milk')      # KeyError: 'milk'
# print(groceries)

groceries.discard('milk')
print(groceries)

# groceries[2] = 'chocolate'    # TypeError: 'set' object does not support item assignment
# print(groceries)
