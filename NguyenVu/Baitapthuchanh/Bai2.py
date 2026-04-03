
noi_dung = """Thuc hanh voi file IO
Day la bai tap ve doc va ghi file trong Python."""

with open("demo_file1.txt", "w", encoding="utf-8") as f:
    f.write(noi_dung)

print("✅ Đã ghi file thành công!\n")


with open("demo_file1.txt", "r", encoding="utf-8") as f:
    print(f.read())