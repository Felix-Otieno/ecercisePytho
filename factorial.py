def iterativeFactorial(n):
    result = 1
    for i in range(n, 0 , -1):
        result = result * i
    return result
print(iterativeFactorial(5))    