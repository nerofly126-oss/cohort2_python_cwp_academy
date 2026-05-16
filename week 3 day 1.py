# 1. List of 6 random numbers, print with index, then print only numbers greater than 10.
numbers = [4, 17, 8, 23, 11, 6]

for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

print()

for num in numbers:
    if num > 10:
        print(num)

# 2. Numbers from 1 to 50, divisible by 4 but NOT divisible by 8.
for num in range(1, 51):
    if num % 4 == 0 and num % 8 != 0:
        print(num)

# 3. Nested loop to combine colors and objects, skip 'green'.
colors = ['blue', 'green', 'yellow']
objects = ['car', 'house', 'shirt']

for color in colors:
    if color == 'green':
        continue
    for obj in objects:
        print(f"{color} {obj}")

# 4a. 5x5 square of stars.
for i in range(5):
    for j in range(5):
        print('*', end=' ')
    print()

print()

# 4b. Diagonal stars only (where row index equals column index).
for i in range(5):
    for j in range(5):
        if i == j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# 5. Nested loop to print sum of each pair, then only sums greater than 30.
scores1 = [10, 20, 30]
scores2 = [5, 15, 25]

for s1 in scores1:
    for s2 in scores2:
        total = s1 + s2
        print(f"{s1} + {s2} = {total}")

print()

for s1 in scores1:
    for s2 in scores2:
        total = s1 + s2
        if total > 30:
            print(f"{s1} + {s2} = {total}")

#key logic:
#Q2: % checks divisibility. Both conditions must be true at once, hence and.
#Q3: continue skips the inner loop entirely when color is green.
#Q4: end=' ' keeps stars on the same line. Diagonal condition is i == j.
#Q5: Every item in scores1 pairs with every item in scores2, so nested loops give all 9 combinations.                                