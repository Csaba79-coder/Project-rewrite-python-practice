def min(x, y):
    if x > y:
        return y
    else:
        return x


def max(values_list):
    largest = values_list[0]
    for num in values_list:
        if num > largest:
            largest = num
    return largest


def len(values_list):
    result = 0
    for i in values_list:
        result += 1
    return result


def multiply(x, y):
    total = 0
    counter = 0
    while counter < y:
        total += x 
        counter += 1
    return total


def pow(x, y):
    count = 1
    result = x
    while True:
        count += 1
        result *= x
        if count == y:
            return result
 

def divmod(x, y):
    pass