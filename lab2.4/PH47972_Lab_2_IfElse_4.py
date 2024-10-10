# 4. Nhập một số và kiểm tra xem nó là số lẻ hay số chẵn.
number = int(input("Nhập một số: "))

if number % 2 == 0:
    print(f"{number} là số chẵn.")
else:
    print(f"{number} là số lẻ.")
