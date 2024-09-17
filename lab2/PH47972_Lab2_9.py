# 9. Viết một chương trình yêu cầu người dùng nhập một số thực và tính bình phương của số đó. Xuất kết quả bình phương ra màn hình.
from decimal import Decimal
num = Decimal(input("Nhập vào một số thực: "))
binh_phuong = num**2
print(f"Bình phương của {num} là {binh_phuong}")