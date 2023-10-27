# 23. Question: How do you swap two variables in Python?

var1 = input("Variable1 = ")
var2 = input("Variable2 = ")

temp=var1
var1=var2
var2=temp
print("After swapping")
print(f"Variable1 = {var1}")
print(f"Variable2 = {var2}")