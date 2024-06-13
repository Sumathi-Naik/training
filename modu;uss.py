def modulus(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    # Use absolute values for the operation
    dividend_abs = abs(dividend)
    divisor_abs = abs(divisor)
    while dividend_abs >= divisor_abs:
        dividend_abs -= divisor_abs
    return -dividend_abs if dividend < 0 else dividend_abs
dividend = 10
divisor = 3
result = modulus(dividend, divisor)
print(f"The remainder of {dividend} divided by {divisor} is {result}")
