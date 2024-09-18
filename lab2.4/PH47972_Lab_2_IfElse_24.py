# 24. Nhập số giờ làm việc và mức lương theo giờ, sau đó tính tổng lương với mức làm thêm giờ (thí dụ: trên 40 giờ là tính lương gấp đôi).
hour = int(input("Nhập số giờ làm việc: "))
luong = int(input("Nhập mức lương theo giờ: "))

if hour > 40:
    total_luong = (40 * luong) +((hour - 40) * luong * 2)
else: 
    total_luong = hour * luong

print(f"Tổng lương là {total_luong}")