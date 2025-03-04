"""
Lesson on integer, float and decimal
1. Integer -> Python's int is arbitrary-precision: -2^31 to 2^31 OR -2^63 to 2^63
2. Float -> 64 bits, 1bit sign, 11 bits exponent, 52 explicit + 1 implicit bits mantissa. 15-17 decimal precision
3. Decimal -> Not stored in a fixed binary format. Up to 28 precision figures
"""
from decimal import Decimal, getcontext


# Integer
big_int = 123456789012345678901234567890
result_int = big_int + 1
print(result_int)

# Float example: potential rounding issues
a = 0.1
result_float = a + a + a  # Expected 0.3
print("Float result:", result_float)
# Output might be: Float result: 0.30000000000000004
# Floats are based on binary (base‑2) arithmetic
# Because 0.1 cannot be represented exactly in binary, adding it three times produces a slight inaccuracy.


# Decimal Precision
# Set precision to 28 decimal places (default is 28)
# Decimal allows you to reflect base‑10 forms exactly
getcontext().prec = 28
a_decimal = Decimal('0.1')
result_decimal = a_decimal + a_decimal + a_decimal  # Expected exactly 0.3
print("Decimal result:", result_decimal)
# Output: Decimal result: 0.3
