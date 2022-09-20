def triangular(n):
    total = 0
    if n < 0:
       return "only accept positive number" 
    if n == 1:
        return 1
    while n > 0:
        total += n
        n -= 1
    return total
    
print(triangular(5))
