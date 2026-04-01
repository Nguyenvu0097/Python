n = int(input("Nhập số nguyên dương n: "))

if n < 2:
    print("Không phải số nguyên tố.")
else:
    i = 2
    la_nguyen_to = True
    
    while i * i <= n:      
        if n % i == 0:
            la_nguyen_to = False
            break
        i += 1
    
    if la_nguyen_to:
        print("Đây là số nguyên tố.")
    else:
        print("Không phải số nguyên tố.")