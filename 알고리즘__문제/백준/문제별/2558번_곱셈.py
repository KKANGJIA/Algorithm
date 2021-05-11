A = int(input())
B = list(map(int, input()))

# print(A, B) 472 [3, 8, 5]


mul3 = A*B[2]
mul4 = A*B[1]
mul5 = A*B[0]

# print(mul3, mul4, mul5) 2360 3776 1416

mul4_add_zero = str(mul4) + str(0)
mul5_add_zero = str(mul5) + str(0) + str(0)

# print(mul4_add_zero, mul5_add_zero) 37760 141600

mul_result = mul3 + int(mul4_add_zero) + int(mul5_add_zero)

print(mul3)
print(mul4)
print(mul5)
print(mul_result)
