# 2. Viết một chương trình yêu cầu người dùng nhập hai số thực và tính hiệu của chúng. Xuất kết quả hiệu ra màn hình.
from decimal import Decimal
num1 = Decimal(input("Nhập vào số thực thứ nhất: "))
num2 = Decimal(input("Nhập vào số thực thứ hai: "))
difference = num1 - num2
print(f"Hiệu hai số thực là: {difference}")
