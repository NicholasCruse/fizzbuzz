#loops from 1 to 100
for fizzynum in range(1, 101):
    #checks if the number is divisible by 3 and 5
    if fizzynum % 3 == 0 and fizzynum % 5 == 0:
        print("fizzbuzz")
    #checks if the number is divisible by only 3
    elif fizzynum % 3 == 0:
        print("fizz")
    #checks if number is divisible by only 5
    elif fizzynum % 5 == 0:
        print("buzz")
    #it prints the number when its neither divisible by 3 nor 5
    else:
        print(fizzynum)