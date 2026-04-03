
print("=== NHẬP THÔNG TIN CÁ NHÂN ===")
ten = input("Họ và tên: ")
tuoi = input("Tuổi: ")
email = input("Email: ")
skype = input("Skype: ")
diachi = input("Địa chỉ: ")
noilamviec = input("Nơi làm việc: ")


with open("setinfo.txt", "w", encoding="utf-8") as f:
    f.write(f"Họ và tên: {ten}\n")
    f.write(f"Tuổi: {tuoi}\n")
    f.write(f"Email: {email}\n")
    f.write(f"Skype: {skype}\n")
    f.write(f"Địa chỉ: {diachi}\n")
    f.write(f"Nơi làm việc: {noilamviec}\n")

print("\n✅ Đã lưu thông tin vào file setinfo.txt\n")

print("=== THÔNG TIN ĐÃ LƯU ===")
with open("setinfo.txt", "r", encoding="utf-8") as f:
    print(f.read())