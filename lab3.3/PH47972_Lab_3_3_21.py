# 21. In tam giác số
# Sử dụng vòng lặp để in ra tam giác số với chiều cao nhập từ bàn phím.
chieu_cao = int(input("Nhập chiều cao của tam giác: "))
for i in range(1, chieu_cao + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
