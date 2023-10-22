# 12. Question: What is the difference between == and is?

""" == compares the value whereas is operator compares the memory location
 == checks for value equality, while is checks for identity (whether two references point to the same object in memory).
"""

x=2
y=2.0
if (x == y):
    print("True")
else:
    print("false")

if (x is y):
    print("true")
else:
    print("false")
