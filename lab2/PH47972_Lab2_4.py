# 4. Viết một chương trình yêu cầu người dùng nhập hai số thực và tính thương của chúng. Xuất kết quả thương ra màn hình.
from decimal import Decimal
num1 = Decimal(input("Nhập vào số thực thứ nhất: "))
num2 = Decimal(input("Nhập vào số thực thứ hai: "))
quotient = num1 / num2
print(f"Tích hai số thực là: {quotient}")