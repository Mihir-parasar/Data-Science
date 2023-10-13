#1. Question: Write a function that takes a list of numbers and returns the sum.
def sum_list():
    lst=[]
    sum=0
    n=int(input("Please enter the number of elements: "))

    for i in range(0,n):
        element=int(input("Enter the elements:"))
        lst.append(element)
        sum = sum + element
    print(f"Entered lst is:{lst}")
    print(f"The sum is:{sum}")

sum_list()