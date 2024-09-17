# 28. Viết một chương trình yêu cầu người dùng nhập một số và tỷ lệ phần trăm. Tính giá trị tương ứng với tỷ lệ phần trăm đó của số đã nhập. Xuất kết quả ra màn hình.
number = float(input("Nhập số: "))
percen = float(input("Nhập tỷ lệ phần trăm: "))

value = number * (percen / 100)

print(f"{percen}% của {number} là {value}")
