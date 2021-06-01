def fizz():
    nums = []
    for x in range(100):
        number = x+1
        if(number % 3 == 0): 
            if(number % 5 == 0):
                nums.append("FizzBuzz")
            else:
                nums.append("Fizz")
        elif(number % 5 == 0):
            nums.append("Buzz")
        else:
            nums.append(number)
    return nums