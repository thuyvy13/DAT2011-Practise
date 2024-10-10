# 14. Kiểm tra xem một số có phải là số chính phương hay không (số nguyên dương có căn bậc hai là số nguyên).
num = int(input("Nhập một số: "))

sqrt_num = num ** 0.5
if sqrt_num == int(sqrt_num):
    print(f"{num} là số chính phương")
else: 
    print(f"{num} không phải là số chính phương")
