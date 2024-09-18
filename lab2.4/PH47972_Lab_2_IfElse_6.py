# 6. Nhập hai số và kiểm tra xem chúng bằng nhau, số này lớn hơn số kia, hoặc số này nhỏ hơn số kia.
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

if a == b:
    print("Hai số bằng nhau.")
elif a > b:
    print(f"{a} lớn hơn {b}.")
else:
    print(f"{a} nhỏ hơn {b}.")
