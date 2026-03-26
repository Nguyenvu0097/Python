a = 16
b = 3
c = 5
# toansohoc
print("toan so hoc")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)

# toantuquanhe
print("toan tu quan he")
print(a > b)
print(a < b)
print(a == c)
print(a != b)
print(a >= b)
print(a <= c)

# toantugan
print("toan tu gan")
x = a
print(f"x = a   -> x = {x}")

x += b
print(f"x =+ b  -> x = {x}")

x -= c
print(f"x -= c  -> x = {x}")

x *= 2
print(f"x *= 2  -> x = {x}")

x /= 2
print(f"x /= 2  -> x = {x}")

x //= 3
print(f"x //= 3 -> x = {x}")

x %= 5
print(f"x %= 5  -> x = {x}")

# toantulogic
print("toan tu logic")
print(f"a > b and b < c = {a > b and b < c}")
print(f"a > b or b > c = {a > b or b > c}")
print(f"not (a == c) = {not (a == c)}")

# toantuthaotacbit
print("toan tu thao tac bit")
print(f"a & b (AND) = {a & b}")
print(f"a | b (OR)  = {a | b}")
print(f"a ^ b (XOR) = {a ^ b}")
print(f"~a (NOT)   = {~a}")
print(f"a << 3 (dich trái 3)    = {a << 3}")
print(f"a >> 2 (dịch phải 2)    = {a >> 2}")