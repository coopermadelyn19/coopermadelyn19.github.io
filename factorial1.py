def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans = ans * i 
        print(f"multiply {i}")
    return ans
# test it
print(factorial(9))