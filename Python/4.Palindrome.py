# 4. Question: Write a function that checks if a given word is a palindrome.
def palindrome():
    word = input("Please enter the number: ")

    if word[::] == word[::-1]:
        print("A palindrome")
    else:
        print("Not a palindrome")

palindrome()