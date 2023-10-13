# 6. Question: How do you handle exceptions in Python?

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")