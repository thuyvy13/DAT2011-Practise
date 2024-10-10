# 30. Tạo bảng số học
# Sử dụng vòng lặp để tạo bảng số học cho một số nguyên nhập từ bàn phím.
so = int(input("Nhập một số nguyên: "))
for i in range(1, 11):
    print(f"{so} + {i} = {so + i}")
