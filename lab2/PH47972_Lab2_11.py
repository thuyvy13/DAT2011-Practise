# 11. Viết một chương trình yêu cầu người dùng nhập ba số thực và tính tổng của chúng. Xuất kết quả tổng ra màn hình.
from decimal import Decimal
num1 = Decimal(input("Nhập vào số thực thứ nhất: "))
num2 = Decimal(input("Nhập vào số thực thứ hai: "))
num3 = Decimal(input("Nhập vào số thực thứ ba: "))
sum = num1 + num2 + num3
print(f"Tổng ba số thực là {sum}")