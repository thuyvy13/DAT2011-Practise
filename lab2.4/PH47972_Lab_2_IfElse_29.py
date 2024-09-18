# 29. Nhập ba điểm và kiểm tra điểm trung bình thuộc loại nào: xuất sắc (trên 85), tốt (70-85), trung bình (50-70), yếu (dưới 50).
score1 = float(input("Nhập điểm thứ nhất: "))
score2 = float(input("Nhập điểm thứ hai: "))
score3 = float(input("Nhập điểm thứ ba: "))

avg_score = (score1 + score2 + score3) / 3

if avg_score > 85:
    print("Điểm trung bình: Xuất sắc.")
elif 70 <= avg_score <= 85:
    print("Điểm trung bình: Tốt.")
elif 50 <= avg_score < 70:
    print("Điểm trung bình: Trung bình.")
else:
    print("Điểm trung bình: Yếu.")
