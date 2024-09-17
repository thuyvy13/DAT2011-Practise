# 6. Viết một chương trình yêu cầu người dùng nhập chiều dài và chiều rộng của hình chữ nhật và tính chu vi của hình chữ nhật đó. Xuất kết quả chu vi ra màn hình.
from decimal import Decimal
chieu_dai = Decimal(input("Nhập vào chiều dài hình chữ nhật: "))
chieu_rong = Decimal(input("Nhập vào chiều rộng hình chữ nhật: "))
chu_vi = (chieu_dai + chieu_rong) * 2
print(f"Chu vi hình chữ nhật là: {chu_vi}")