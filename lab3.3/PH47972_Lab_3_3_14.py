# 14. In số hoàn hảo
# Sử dụng vòng lặp để tìm và in ra các số hoàn hảo trong khoảng từ 1 đến n.
n = int(input("Nhập một số nguyên dương n: "))
for i in range(1, n + 1):
    tong_uoc = 0
    for j in range(1, i):
        if i % j == 0:
            tong_uoc += j
    if tong_uoc == i:
        print(f"{i} là số hoàn hảo.")

