n = int(input("Nhập số nguyên dương n: "))

if n < 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    i = 1
    giai_thua = 1
    
    while i <= n:
        giai_thua *= i
        i += 1
    
    print(f"{n}! = {giai_thua}")