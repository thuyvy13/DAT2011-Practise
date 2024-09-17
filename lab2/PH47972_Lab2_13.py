# 13. Viết một chương trình yêu cầu người dùng nhập chiều dài, chiều rộng và chiều cao của một hình hộp chữ nhật và tính thể tích của hình hộp đó. Xuất kết quả thể tích ra màn hình.
a = int(input("Nhập vào chiều dài hình hộp chữ nhật: "))
b = int(input("Nhập vào chiều rộng hình hộp chữ nhật: "))
c = int(input("Nhập vào chiều cao hình hộp chữ nhật: "))
V = a * b * c
print(f"Thể tích hình hộp chữ nhật là: {V}")