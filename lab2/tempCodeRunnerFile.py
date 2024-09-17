from decimal import Decimal
ban_kinh = Decimal(input("Nhập vào bán kính hình tròn: "))
pi = 3.14
S = pi * ban_kinh**2
print(f"Diện tích hình tròn là: {S}")