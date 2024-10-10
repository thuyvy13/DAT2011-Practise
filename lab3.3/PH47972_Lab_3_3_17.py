# 17. Liệt kê các số chia hết cho 3
# Sử dụng vòng lặp để in ra tất cả các số từ 1 đến n chia hết cho 3.
n = int(input("Nhập một số để in các số chia hết cho 3: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)    