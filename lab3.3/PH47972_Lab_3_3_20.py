# 20. Tính tổng số nguyên tố
# Sử dụng vòng lặp để tính tổng các số nguyên tố từ 1 đến n.
n = int(input("Nhập một số nguyên dương n: "))
tong_nguyen_to = 0
for so in range(2, n+1):
    is_prime = True
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            is_prime = False
            break
    if is_prime:
        tong_nguyen_to += so
print(f"Tổng các số nguyên tố từ 1 đến {n} là: {tong_nguyen_to}")
