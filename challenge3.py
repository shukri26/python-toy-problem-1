def positiveArguments(a, b, c):
    positiveCount = 0
    
    if (a > 0 and b > 0 and c <= 0) or (a > 0 
    and b <= 0 and c > 0) or (a <= 0 and b > 0 and c > 0):
        positiveCount = 2

    return positiveCount == 2

print(positiveArguments(2, -3, 5))
print(positiveArguments(-2, 4, 6))
print(positiveArguments(6, 1, 2))