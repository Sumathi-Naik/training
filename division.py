def integer_quotient(numerator, denominator):
    if denominator == 0:
        raise ValueError("Cannot use zero as the denominator")

    # Determine the sign of the result
    negative_result = (numerator < 0) != (denominator < 0)

    # Work with positive values for simplicity
    numerator = abs(numerator)
    denominator = abs(denominator)

    quotient = 0
    while numerator >= denominator:
        numerator -= denominator
        quotient += 1
    return -quotient if negative_result else quotient


# Get input from the user
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

try:
    result = integer_quotient(numerator, denominator)
    print(f"The quotient of {numerator} and {denominator} is {result}")
except ValueError as e:
    print(e)