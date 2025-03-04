# Initiation Option 1
my_set: set[str] = set()
# Option 2
my_second_set: set[str] = {"apple"}

# Adding
my_set.add("bananas")
print(my_set)  # output: {"bananas"}

# Removing
my_second_set.remove("apple")
print(my_second_set)  # output: empty set
my_second_set.discard("kiwi")  # Does nothing if "kiwi" is absent

# Clearing the set
my_set.clear()
print(my_set)  # Output: set()

# updating
my_set.update(["date", "elderberry"])
print(my_set)

# Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Output: {1, 2, 3, 4, 5}
print(a.union(b))  # Same result

# Overlaps
print(a & b)  # Output: {3}
print(a.intersection(b))  # Same result

# Difference
print(a - b)  # Output: {1, 2}
print(a.difference(b))  # Same result
