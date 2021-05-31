def fizz():
    nums = []
    for x in range(100):
        number = x+1
        if(number % 3 == 0):
            nums.append("Fizz")
        else:
            nums.append(number)
    return nums
