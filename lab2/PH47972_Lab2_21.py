# 21. Viết một chương trình yêu cầu người dùng nhập bốn số thực và tính trung bình cộng của chúng. Xuất kết quả trung bình cộng ra màn hình.
num1 = float(input("Nhập số thực thứ nhất: "))
num2 = float(input("Nhập số thực thứ hai: "))
num3 = float(input("Nhập số thực thứ ba: "))
num4 = float(input("Nhập số thực thứ tư: "))

avg = (num1 + num2 + num3 + num4) / 4

print(f"Trung bình cộng của bốn số là {avg:.2f}")
