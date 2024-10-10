# 19. Nhập cân nặng và chiều cao, sau đó tính chỉ số BMI và phân loại: thiếu cân, bình thường, thừa cân, béo phì.
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

BMI = can_nang / (chieu_cao ** 2)

print(f"Chỉ số BMI của bạn là: {BMI:.2f}")

if BMI < 18.5:
    print("Bạn đang thiếu cân.")
elif 18.5 <= BMI < 24.9:
    print("Bạn có cân nặng bình thường.")
elif 25 <= BMI < 29.9:
    print("Bạn đang thừa cân.")
else:
    print("Bạn bị béo phì.")
