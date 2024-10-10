# 1. Viết một chương trình kiểm tra xem một số nguyên nhập vào là số dương, âm hay là 0.
number = int(input("Nhập vào một số nguyên: "))
if number > 0:
    print(f"{number} là một số nguyên dương")
elif number < 0:
    print(f"{number} là một số nguyên âm")
else:
    print(f"{number}")