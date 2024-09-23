# 16. In bảng nhân
# Sử dụng vòng lặp để in bảng nhân cho một số nguyên nhập từ bàn phím.
so = int(input("Nhập một số nguyên: "))
for i in range(1, 11):
    print(f"{so} x {i} = {so * i}")