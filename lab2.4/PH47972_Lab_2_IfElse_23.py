# 23. Nhập điểm thi của học sinh và kiểm tra xem học sinh có cần thi lại không (thí dụ: điểm < 40 là thi lại).
score = int(input("Nhập điểm thi: "))
if score < 40:
    print("Cần thi lại")
else: 
    print("Không cần thi lại")