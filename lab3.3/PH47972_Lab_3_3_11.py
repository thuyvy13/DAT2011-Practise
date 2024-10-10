# 11. Tính tổng số lẻ
# Sử dụng vòng lặp để tính tổng tất cả các số lẻ từ 1 đến n.
number = int(input("Nhập vào n: "))
sum = 0
for i in range(1, number + 1):
    if i % 2 != 0:
        sum += i

print(f"Tổng các số từ 1 đến {number} là: {sum}")
        