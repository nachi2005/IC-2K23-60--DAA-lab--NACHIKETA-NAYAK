# DAA Lab Task 1 - Part 3
# Build a tree of subjects and perform level-order traversal

tree = {
    "Math": ["Algebra", "Geometry"],
    "Science": ["Physics", "Chemistry"]
}

print("Subject Tree:")
print("Math")
print("  Algebra")
print("  Geometry")
print("Science")
print("  Physics")
print("  Chemistry")

# Level-order traversal
print("\nLevel Order Traversal:")

level_order = ["Math", "Science"]

for subject in level_order:
    print(subject)

    for child in tree[subject]:
        print("  " + child)