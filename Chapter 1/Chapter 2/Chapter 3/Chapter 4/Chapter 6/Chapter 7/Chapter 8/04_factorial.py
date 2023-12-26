# Traditional Method to find factorial
'''
n = 4
product = 1
for i in range(n):
    product = product * (i+1)
print(product)
'''

# Finding factorial via functions and recursion

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(0))