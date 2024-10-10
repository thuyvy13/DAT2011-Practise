# 2. Tính tổng số từ 1 đến n
# Nhập một số nguyên dương n và tính tổng tất cả các số từ 1 đến n.
number = int(input("Nhập một số nguyên dương: "))
sum_number = sum(range(1, number + 1))
print(f"Tổng các số từ 1 đến {number} là: {sum_number}")