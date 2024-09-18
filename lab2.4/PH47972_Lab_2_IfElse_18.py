# 18. Nhập một số từ 1 đến 7 và in ra tên của ngày trong tuần tương ứng.
day = int(input("Nhập số từ 1 đến 7: "))

if day == 1:
    print("Chủ Nhật")
elif day == 2:
    print("Thứ Hai")
elif day == 3:
    print("Thứ Ba")
elif day == 4:
    print("Thứ Tư")
elif day == 5:
    print("Thứ Năm")
elif day == 6:
    print("Thứ Sáu")
elif day == 7:
    print("Thứ Bảy")
else:
    print("Số không hợp lệ.")
