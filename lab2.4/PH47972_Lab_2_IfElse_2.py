# 2. Nhập tuổi và kiểm tra nhóm tuổi: trẻ em (0-12), thanh thiếu niên (13-19), người trưởng thành (20-59), và người cao tuổi (60+).
age = int(input("Nhập vào tuổi: "))
if 0 <= age <= 12:
    print(f"{age} tuổi là trẻ em ")
elif 13 <= age <= 19:
    print(f"{age} tuổi là thanh thiếu niên")
elif 20 <= age <= 59:
    print(f"{age} tuổi là người trưởng thành")
else:
    print(f"{age} tuổi là người cao tuổi")