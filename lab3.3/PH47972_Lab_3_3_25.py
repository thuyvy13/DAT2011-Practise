# 25. In hình thang bằng dấu sao
# Sử dụng vòng lặp để in ra hình thang bằng dấu sao.
chieu_rong_tren = int(input("Nhập chiều rộng của đáy trên: "))
chieu_rong_duoi = int(input("Nhập chiều rộng của đáy dưới: "))
chieu_cao = int(input("Nhập chiều cao: "))

buoc_giam = (chieu_rong_duoi - chieu_rong_tren) // (chieu_cao - 1)
for i in range(chieu_cao):
    print("*" * (chieu_rong_tren + i * buoc_giam))
