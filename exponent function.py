def raise_to_power(base_num, pow_num): #creating the function raise_to_pow that will accept 2 inputs (base and pow)
    result = 1 #creating the variable result to store number as math is executed
    for index in range(pow_num): #creating a loop so that each index(number) in the range of pow_num is taken through the function (ex: pow = 3 then the function is carried out 3 times)
        result = result * base_num #this is creating a loop that will change each time through
    return result #this prints out the final result once the loop is completed

print(raise_to_power(3, 5)) #this print establishes the numbers in our defined function