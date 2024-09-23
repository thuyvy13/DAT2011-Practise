# 5. Tìm giá trị lớn nhất trong danh sách
# Tạo một danh sách số và sử dụng vòng lặp để tìm giá trị lớn nhất.
danh_sach = [3, 5, 7, 2, 8, 6, 4]
max_value = danh_sach[0]
for i in danh_sach:
    if i > max_value:
        max_value = i
        
print(f"Giá trị lớn nhất trong danh sách là: {max_value}")