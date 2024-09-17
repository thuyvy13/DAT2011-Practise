# 3. Viết một chương trình yêu cầu người dùng nhập hai số thực và tính tích của chúng. Xuất kết quả tích ra màn hình.
from decimal import Decimal
num1 = Decimal(input("Nhập vào số thực thứ nhất: "))
num2 = Decimal(input("Nhập vào số thực thứ hai: "))
product = num1 * num2
print(f"Tích hai số thực là: {product}")