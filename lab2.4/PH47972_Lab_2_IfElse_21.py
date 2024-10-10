# 21. Nhập một số thực và kiểm tra xem phần thập phân có lớn hơn hay bằng 0.5 để làm tròn lên hay không.
number = float(input("Nhập một số thực: "))
if number - int(number) >= 0.5:
    round = int(number) + 1
else: 
    round = int(number)

print(f"{number} được làm tròn thành: {round}")