# DAA Lab Task 1 - Part 4
# Count the steps in single and nested loops

# Single loop from 1 to 5
print("Single Loop (1 to 5):")

count = 0

for i in range(1, 6):
    print(i)
    count += 1

print("Single Loop Runs:", count)

# Single loop from 1 to n, where n = 20
n = 20
count = 0

for i in range(1, n + 1):
    count += 1

print("Single Loop Runs for n = 20:", count)

# Nested loop from 1 to 5
print("\nNested Loop (1 to 5):")

nested_count = 0

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)
        nested_count += 1

print("Nested Loop Total Prints:", nested_count)

# Nested loop from 1 to n, where n = 10
n = 10
nested_count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        nested_count += 1

print("Nested Loop Total Prints for n = 10:", nested_count)
