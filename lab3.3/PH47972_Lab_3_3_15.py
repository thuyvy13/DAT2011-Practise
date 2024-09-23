# 15. Tính tổng các chữ số
# Nhập một số nguyên và sử dụng vòng lặp để tính tổng các chữ số của nó.
so = int(input("Nhập một số nguyên: "))
tong_chu_so = 0
while so > 0:
    tong_chu_so += so % 10
    so //= 10
print(f"Tổng các chữ số là: {tong_chu_so}")
