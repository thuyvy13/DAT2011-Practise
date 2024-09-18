# 26. Nhập hai số và kiểm tra xem tỷ lệ giữa chúng có phải là phân số đơn giản không (tức là tỷ lệ không thể rút gọn hơn).

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

if a % b == 0 or b % a == 0:
    print("Tỷ lệ giữa hai số không phải là phân số đơn giản.")
else:
    print("Tỷ lệ giữa hai số là phân số đơn giản.")
