# 10. Đảo ngược chuỗi
# Nhập một chuỗi và sử dụng vòng lặp để đảo ngược chuỗi đó.
chuoi = input("Nhập vào một chuỗi để đảo ngược: ")
dao_nguoc = ""
for i in chuoi:
    dao_nguoc = i + dao_nguoc

print(f"Chuỗi đảo ngược là: {dao_nguoc}")