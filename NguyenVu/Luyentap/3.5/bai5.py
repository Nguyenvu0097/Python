# Bài 5: Giải phương trình bậc 2: a*x² + b*x + c = 0
import math

print("=== GIẢI PHƯƠNG TRÌNH BẬC 2 ===")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("❌ Đây không phải phương trình bậc 2 vì a = 0")
else:
    delta = b**2 - 4*a*c
    print(f"Delta = {delta:.2f}")
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"✅ Phương trình có 2 nghiệm phân biệt:")
        print(f"   x1 = {x1:.4f}")
        print(f"   x2 = {x2:.4f}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"✅ Phương trình có nghiệm kép:")
        print(f"   x = {x:.4f}")
    else:
        print("❌ Phương trình vô nghiệm (delta < 0)")