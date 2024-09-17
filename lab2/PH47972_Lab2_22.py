# 22. Viết một chương trình yêu cầu người dùng nhập nhiệt độ theo độ Fahrenheit và chuyển đổi nó thành độ Celsius. Xuất kết quả ra màn hình.
fahrenheit = float(input("Nhập nhiệt độ theo độ Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"Nhiệt độ {fahrenheit} tương đương với {celsius:.2f}")
