# 12. In hình chữ nhật bằng dấu sao
# Sử dụng vòng lặp để in ra hình chữ nhật bằng dấu sao với chiều dài và chiều rộng nhập từ bàn phím.
chieu_dai = int(input("Nhập chiều dài: "))
chieu_rong = int(input("Nhập chiều rộng: "))
for i in range(chieu_rong):
    print("*" * chieu_dai)
