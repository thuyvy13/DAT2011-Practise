# 8. Tìm số nguyên tố
# Sử dụng vòng lặp để kiểm tra xem một số đã nhập có phải là số nguyên tố không.
number = int(input("Nhập vào một số để kiểm tra số nguyên tố: "))
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} là số nguyên tố")
else:
    print(f"{number} không phải là số nguyên tố")
