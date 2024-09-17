# 12. Viết một chương trình yêu cầu người dùng nhập chiều cao và đáy của một tam giác và tính diện tích của tam giác đó. Xuất kết quả diện tích ra màn hình.
from decimal import Decimal
h = Decimal(input("Nhập vào chiều cao của tam giác: "))
a = Decimal(input("Nhập vào chiều đáy của tam giác: "))
S = (a * h) / 2
print(f"Diện tích của tam giác là {S}")

