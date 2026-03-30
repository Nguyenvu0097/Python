# Bài 4: Kiểm tra số nguyên dương có chia hết cho 2, cho 3 hay cả hai
n = int(input("Nhập một số nguyên dương: "))

if n <= 0:
    print("❌ Vui lòng nhập số nguyên dương (> 0)!")
else:
    chia_2 = (n % 2 == 0)
    chia_3 = (n % 3 == 0)
    
    if chia_2 and chia_3:
        print(f"✅ Số {n} chia hết cho cả 2 và 3")
    elif chia_2:
        print(f"✅ Số {n} chia hết cho 2")
    elif chia_3:
        print(f"✅ Số {n} chia hết cho 3")
    else:
        print(f"❌ Số {n} không chia hết cho 2 hoặc 3")