# 1. Create a list of 5 fruits and print it.
fruits = ['Mango', 'Apple', 'Banana', 'Orange', 'Grape']
print(fruits)

# 2. Add a new fruit to the end using append().
fruits.append('Pineapple') 
print(fruits)

# 3. Insert a fruit at position 2.
fruits.insert(2, 'Watermelon')  
print(fruits)

# 4. Remove the last item using pop().
fruits.pop() 
print(fruits)

# 5. Remove a specific fruit using remove().
fruits.remove('Apple') 
print(fruits)

# 6. Create a list of numbers and sort ascending.
numbers = [34, 7, 2, 19, 45, 1]
numbers.sort() 
print(numbers)

# 7. Reverse the order of a list.
numbers.reverse() 
print(numbers)

# 8. Count how many times a number appears.
nums = [3, 7, 3, 9, 3, 1, 7]
print(nums.count(3))  

# 9. Find the index of a specific element.
print(nums.index(9))  

# 10. Combine two lists into one.
list1 = ['cat', 'dog', 'bird']
list2 = ['fish', 'rabbit', 'hamster']
combined = list1 + list2  
print(combined)