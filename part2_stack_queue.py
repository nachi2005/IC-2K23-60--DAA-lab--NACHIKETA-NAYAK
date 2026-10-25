# DAA Lab Task 1 - Part 2
# Stack and Queue operations

tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]

# Stack follows LIFO (Last In, First Out)
stack = []

for task in tasks:
    stack.append(task)

print("Stack Completion Order:")

while stack:
    print(stack.pop())

# Queue follows FIFO (First In, First Out)
queue = []

for task in tasks:
    queue.append(task)

print("\nQueue Completion Order:")

while queue:
    print(queue.pop(0))

print("\nPrinter should use: Queue")
print("Reason: A printer processes tasks in the order they arrive.")