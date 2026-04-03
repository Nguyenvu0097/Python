
noi_dung = "Thuc\nhanh\nvoi\nfile\nIO\n"

with open("demo_file1.txt", "w", encoding="utf-8") as f:
    f.write(noi_dung)

print("File demo_file1.txt đã được tạo.\n")

with open("demo_file1.txt", "r", encoding="utf-8") as f:
    print("a) Nội dung trên một dòng:")
    print(f.read().replace("\n", " ").strip())


print("\nb) Nội dung theo từng dòng:")
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())