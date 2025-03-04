"""
1. String Slicing, taking out a part of a str from a whole str
2. Indexing
3. Strings are immutable, have to create a new string to "change/modify" a string in place
4. Concatenation
5. Combining
6. Lowercase Uppercase
7. Splitting
8. Joining
"""

my_str: str = "clement"
# [start:end:steps]
print(my_str[::-1])

# Syntax: s[start:end:step]
print(my_str[1:4])  # Output: 'lem'
print(my_str[1:4:2])  # Output: 'lm', traverse in steps of 2
print(my_str[5:1:-1])  # Output: 'neme', traverse backwards from position 5 to 2


s = "clement"
print(my_str[0])  # Output: 'c'
print(my_str[-1])  # Output: 't'


b = "hello"
# s[0] = 'H'  # This would raise an error.
# To "change" a string, you must create a new one.
b = "H" + b[1:]
print(b)  # Output: 'Hello'


s1 = "Hello"
s2 = "World"
combined = s1 + " " + s2
print(combined)  # Output: 'Hello World'

my_str = "Hello World"
print(s.lower())  # Output: 'hello world'
print(s.upper())  # Output: 'HELLO WORLD'

s = "apple,banana,cherry"
fruits = s.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

joined = " & ".join(fruits)
print(joined)  # Output: 'apple & banana & cherry'


s = "I love apples"
print(s.find("apples"))  # Output: 7 (index of substring)
print(s.replace("apples", "oranges"))  # Output: 'I love oranges'
