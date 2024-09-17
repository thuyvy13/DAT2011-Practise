# 15. Viết một chương trình yêu cầu người dùng nhập bán kính của một hình cầu và tính thể tích của hình cầu đó. Xuất kết quả thể tích ra màn 
r = float(input("Nhập vào bán kính hình cầu: "))
pi = 3.14
V = (4/3) * pi * r**3
print(f"Thể tích hình cầu là : {V}")