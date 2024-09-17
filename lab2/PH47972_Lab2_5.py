# 5. Viết một chương trình yêu cầu người dùng nhập chiều dài và chiều rộng của hình chữ nhật và tính diện tích của hình chữ nhật đó. Xuất kết quả diện tích ra màn hình.
from decimal import Decimal
chieu_dai = Decimal(input("Nhập vào chiều dài hình chữ nhật: "))
chieu_rong = Decimal(input("Nhập vào chiều rộng hình chữ nhật: "))
S = chieu_dai * chieu_rong
print(f"Diện tích hình chữ nhật là: {S}")