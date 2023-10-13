# 5. Question: How can you remove duplicates from a list?

def duplicate():
    lst=[]
    new=[]
    n=int(input("Please enter the number of elements in list:"))

    for i in range(0,n):
        element=input("Enter the number:")
        lst.append(element)
    
    print(f"After removing duplicates is: {set(lst)}")

# By using list Comprehension
[new.append(x) for x in lst if x not in new]
print(f"After removing duplicates:{new}")
