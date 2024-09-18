# 27. Nhập số từ 1 đến 5 và in ra tên của món ăn tương ứng từ một menu.)
number = int(input("Nhập số từ 1 đến 5: "))

if number == 1:
    print("Món ăn tương ứng: Phở gà")
elif number == 2:
    print("Món ăn tương ứng: Bún cá")
elif number == 3:
    print("Món ăn tương ứng: Xôi")
elif number == 4:
    print("Món ăn tương ứng: Cơm")
elif number == 5:
    print("Món ăn tương ứng: Bánh mì")
else:
    print("Số không hợp lệ.")
