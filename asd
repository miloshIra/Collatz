def collatz(number):
    if number % 2 == 0:
        print(number // 2)
    elif number % 2 != 0:
        print(3 * number + 1)
        return (3 * number + 1)

collatz(52)
