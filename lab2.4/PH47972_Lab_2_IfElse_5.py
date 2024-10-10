# 5. Nhập điểm số và kiểm tra xếp loại: A (90-100), B (80-89), C (70-79), D (60-69), và F (dưới 60).
diem_so = float(input("Nhập điểm số: "))

if 90 <= diem_so <= 100:
    print("Xếp loại: A")
elif 80 <= diem_so < 90:
    print("Xếp loại: B")
elif 70 <= diem_so < 80:
    print("Xếp loại: C")
elif 60 <= diem_so < 70:
    print("Xếp loại: D")
elif diem_so < 60:
    print("Xếp loại: F")
else:
    print("Điểm số không hợp lệ.")
