# python3


def sum_of_two_digits(first_digit, second_digit):
    int(first_digit) + int(second_digit)
    return first_digit + second_digit

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))



