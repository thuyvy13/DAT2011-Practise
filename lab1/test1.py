"""Viết chương trình chuyển đổi từ giây sang giờ, phút và giây (không sử dụng vòng lặp hay cấu trúc điều kiện).

Ví dụ: 3672 giây -> 1 giờ 1 phút 12 giây"""

a = 3672
gio = a // 3600
phut = (gio % 3600) /10
giay = a % 60
print(f"{gio} giờ {phut} phút {giay} giay")




