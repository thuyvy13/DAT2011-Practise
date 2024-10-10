# 7. Tính giai thừa
# Nhập một số nguyên không âm và sử dụng vòng lặp để tính giai thừa của nó.
number = int(input("Nhập một số nguyên để tính giai thừa: "))
giai_thua = 1
for i in range(1, number + 1):
    giai_thua *= i
print(f"Giai thừa của {number} là: {giai_thua}")