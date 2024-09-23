# 27. In danh sách số lẻ
# Tạo một danh sách số và sử dụng vòng lặp để in ra các số lẻ trong danh sách.
danh_sach = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))
for so in danh_sach:
    if so % 2 != 0:
        print(so, end=" ")
