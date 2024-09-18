# 8. Nhập tháng và kiểm tra số ngày trong tháng đó (cần xem xét năm nhuận cho tháng 2).
year = int(input("Nhập vào năm (>=2024): "))
month = int(input("Nhập vào tháng (1 - 12): "))

nam_nhuan = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if month == 2:
    if nam_nhuan:
        print("Tháng 2 có 29 ngày")
    else:
        print("Tháng 2 có 28 ngày")
elif month in [4, 6, 9, 11]:
    print(f"Tháng {month} có 30 ngày")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {month} có 31 ngày")
else:
    print("Tháng không hợp lệ")
