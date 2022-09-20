def sum_squares(*numbers) :
    arr = [*numbers]
    temp = 0
    for num in arr:
        temp += num**2
    return temp

print(sum_squares(1, 2, 3))
