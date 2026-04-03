
n = int(input("Nhập số dòng muốn đọc: "))

try:
    with open("demo_file1.txt", "r", encoding="utf-8") as f:
        for i in range(n):
            line = f.readline()
            if line == "":          
                break
            print(line.strip())
except FileNotFoundError:
    print("❌ File không tồn tại!")