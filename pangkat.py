def pangkat(num, exp):
    temp = num
    if num < 0 or exp < 0:
        return "only accept positive number"
    if exp == 0:
        return 1
    counter = 0
    while counter < exp - 1:
        num = num * temp
        counter += 1
    return num

print(pangkat(3, 2))
