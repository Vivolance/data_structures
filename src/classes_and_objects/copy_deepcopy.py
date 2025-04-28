import copy

"""
Difference between shallow copy and deep copy.

Concepts:
1. The effects of copy / deepcopy only works on mutable objects, such as lists, dicts, sets. If we do copy on [1,2,3,4],
we do not see the effects
2. Shallow copy copies the outer list containing mutable objects ( such as list[list[int]] ). When we change a variable
of the inner list, on the shallow copy, the original copy stays the same
3. Deep copy clones the entire list, changing elements in the inner list of the deep copy affects the original copy.
4. Pass by reference, all variables are pointers to an object on the heap. When we do x = 5, 5 is created on the heap.
x is stored on the stack frame. 
"""


x = [[1, 2], [3, 4, 5]]

x_shallow = copy.copy(x)

x_shallow[0][0] = 2

x_deep = copy.deepcopy(x)

x_deep[0][0] = 10

print(x)  # output = [[2, 2], [3, 4, 5]]
print(x_shallow)  # output = [[2, 2], [3, 4, 5]]
print(x_deep)  # output = [[10, 2], [3, 4, 5]]
