# Swapping values
print('Swapping values :')
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)

# Create a single string from all the elements in list
a = ['Hello,', 'this', 'is', 'John']
print('create single string from list : ')
print(' '.join(a))

# Find The Most Frequent Value In A List.
a = [1,2,7,6,2,4,2,8,3,4,2,5,4]
print('Most Frequent Value In list : ')
print(max(set(a), key = a.count))