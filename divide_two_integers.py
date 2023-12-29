def divide(dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    times = 0
    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)
    while abs_dividend >= abs_divisor:
        abs_dividend -= abs_divisor
        times += 1
    return min(max(-2147483648, -times), 2147483647) if (dividend < 0 < divisor) or (dividend > 0 > divisor) else min(max(-2147483648, times), 2147483647)


a = -10
b = 3

print(divide(a, b))
