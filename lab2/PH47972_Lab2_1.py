# 1. Viết một chương trình yêu cầu người dùng nhập hai số thực và tính tổng của chúng. Xuất kết quả tổng ra màn hình.
from decimal import Decimal
num1 = Decimal(input("Nhập vào số thực thứ nhất: "))
num2 = Decimal(input("Nhập vào số thực thứ hai: "))
sum = num1 + num2
print(f"Tổng hai số thực là: {sum}")

