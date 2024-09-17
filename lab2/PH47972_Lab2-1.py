num1 = float(input("Nhập vào số thứ nhất: "))
num2 = float(input("Nhập vào số thứ hai: "))

tong = num1 + num2

nguong = 100

(tong > nguong and print(f"Tổng {tong} lớn hơn {nguong}")) or \
(tong < nguong and print(f"Tổng {tong} nhỏ hơn {nguong}")) or \
(tong == nguong and print(f"Tổng {tong} bằng {nguong}"))
