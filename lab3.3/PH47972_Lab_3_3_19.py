# 19. Tạo danh sách số tự nhiên
# Sử dụng vòng lặp để tạo một danh sách chứa các số tự nhiên từ 1 đến n.
n = int(input("Nhập một số nguyên dương n: "))
danh_sach = []
for i in range(1, n+1):
    danh_sach.append(i)
print(danh_sach)
