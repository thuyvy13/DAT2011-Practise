# 7. Viết một chương trình yêu cầu người dùng nhập bán kính của hình tròn và tính diện tích của hình tròn đó. Xuất kết quả diện tích ra màn hình.
ban_kinh = float(input("Nhập vào bán kính hình tròn: "))
pi = 3.14
S = pi * ban_kinh**2
print(f"Diện tích hình tròn là: {S}")