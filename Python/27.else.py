# 27. Question: What does the else clause in a loop do?

"""
The else clause in a loop is executed when the loop finishes execution (i.e., when the loop condition becomes False).
It won't execute if the loop was exited using a break statement."""

for i in range(5):
    print(i)
else:
    print("Loop finished")