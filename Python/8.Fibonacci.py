# 8. Question: Write a function that returns the n-th Fibonacci number using recursion.



def fibonacci(n):    
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(5))

