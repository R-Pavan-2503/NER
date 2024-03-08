x = ("apple", " banana", "car", "dog", "elephant")

# ACCESSING AN TUPLE

print(x[1])
print(x[-1])
print(x[:3])

# UPDATE AN TUPLE

y = list(x)
y[1] = "frog"
x = tuple(y)
print(x)

# UNPACKING IN TUPLE

a, b, *c = x
print(a, b, c)

# LOOPING IN TUPLE
for i in x:
    print(i, end=" ")
print()
for i in range(len(x)):
    print(x[i], end=" ")
print()

# JOINING IN TUPLE

a = (1, 2, 3, 4, 5)
b = a + x
print(b)

# METHODS IN TUPLE

print(x.count("apple"))
print(b.index("frog"))
