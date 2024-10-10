# 20. Gán hai số vào các biến, tính tổng của chúng và so sánh với một ngưỡng cố định (ví dụ: 100), sau đó in ra kết quả so sánh.
num1 = float(input("Nhập vào số thứ nhất: "))
num2 = float(input("Nhập vào số thứ hai: "))
tong = num1 + num2
nguong = 100
if tong > nguong:
    print(f"Tổng {tong} lớn hơn {nguong}")
elif tong < nguong:
    print(f"Tổng {tong} nhỏ hơn {nguong}")
else:
    print(f"Tổng {tong} bằng {nguong}")

