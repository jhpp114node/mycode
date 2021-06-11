#!/usr/bin/env python3
def main():
    # for x in range(1, 101, 1):
    #     if x % 5 == 0 and x % 3 == 0:
    #         print("FizzBuzz")
    #     elif x % 5 == 0:
    #         print("Buzz")
    #     elif x % 3 == 0:
    #         print("Fizz")
    #     else:
    #         print(x)
    for x in range(1, 101):
        print_value = ""
        print_value = "FizzBuzz" if (x % 5 == 0 and x % 3 == 0) else "Buzz" if (x % 5 == 0) else "Fizz" if (x % 3 == 0) else str(x)
        print(print_value)
main()
