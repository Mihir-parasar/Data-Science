# 20. Question: How is string interpolation done in Python?

""" 
Using % formatting.
Using .format() method.
Using f-strings (from Python 3.6+)."""

name = 'Alice'
# Using % formatting
print("Hello, %s!" % name)

# Using .format()
print("Hello, {}!".format(name))

# Using f-strings
print(f"Hello, {name}!")