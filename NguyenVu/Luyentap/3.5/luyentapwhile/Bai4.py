n = int(input("Nhập số nguyên n: "))

i = 1
tong = 0

while i < n:
    if i % 2 == 0:
        tong += i
    i += 1

print(f"Tổng các số chẵn nhỏ hơn {n} là: {tong}")