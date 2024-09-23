# 22. Tính số lượng số âm, dương
# Nhập một danh sách số và sử dụng vòng lặp để đếm số lượng số dương và số âm.
danh_sach = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))
so_duong = 0
so_am = 0
for so in danh_sach:
    if so > 0:
        so_duong += 1
    elif so < 0:
        so_am += 1
print(f"Số lượng số dương: {so_duong}, Số lượng số âm: {so_am}")
