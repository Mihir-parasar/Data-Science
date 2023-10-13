#2. Question: How do you reverse a string in Python?
def str_reverse():
    str=input("Please enter the string: ")
    i=len(str)-1
    while i>=0:
        print(str[i],end="")
        i=i-1

    # print(str[::-1])
str_reverse()



