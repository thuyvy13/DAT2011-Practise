# 16. Viết một chương trình yêu cầu người dùng nhập bán kính lớn và bán kính nhỏ của một hình elip và tính diện tích cũng như chu vi của hình elip đó. Xuất kết quả ra màn hình.

a = float(input("Nhập vào bán kính lớn hình elip: "))
b = float(input("Nhập vào bán kính lớn nhỏ elip: "))
pi = 3.14159
chu_vi = pi * (3*(a + b) - ((3 * a + b) * (a + 3 * b)) ** 0.5)
dien_tich = pi * a * b
print(f"Diện tích hình elip là: {dien_tich:.2f}")
print(f"Chu vi hình elip là: {chu_vi:.2f}")
