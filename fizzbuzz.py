# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz

# for num in range(1,100):
#     if (num % 3 == 0) and (num % 5 == 0):
#         print(num, "FizzBuzz")
#     elif num % 3 == 0:
#         print(num, "Fizz")
#     elif num % 5 == 0:
#         print(num, "Buzz")
#     else:
#         print(num)


def fizz_buzz(n):
    for i in range(1, n + 1):
        result = ''
        if i % 3 == 0:
            result += 'Fizz'
        if i % 5 == 0:
            result += 'Buzz'
        print(result or i)

fizz_buzz(100)