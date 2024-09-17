# 17. Viết một chương trình yêu cầu người dùng nhập ba số thực và tính trung bình cộng của chúng. Xuất kết quả trung bình cộng ra màn hình.

num1 = float(input("Nhập vào số thực thứ nhất: "))
num2 = float(input("Nhập vào số thực thứ hai: "))
num3 = float(input("Nhập vào số thực thứ ba: "))
trung_binh_cong = (num1 + num2 + num3) / 3
print(f"Tổng ba số thực là {trung_binh_cong:.2f}")