# 28. Tính trung bình
# Sử dụng vòng lặp để tính trung bình của một danh sách số đã nhập.
danh_sach = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))
trung_binh = sum(danh_sach) / len(danh_sach)
print(f"Giá trị trung bình của danh sách là: {trung_binh}")
