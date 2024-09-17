# 23. Viết một chương trình yêu cầu người dùng nhập chiều dài hai đáy và chiều cao của hình thang và tính chu vi cùng diện tích của hình thang đó. Xuất kết quả ra màn hình.
day_lon = float(input("Nhập chiều dài đáy lớn của hình thang: "))
day_nho = float(input("Nhập chiều dài đáy nhỏ của hình thang: "))
h = float(input("Nhập chiều cao của hình thang: "))

chu_vi = day_lon + day_nho + 2 * h  
dien_tich = ((day_lon + day_nho) * h) / 2

print(f"Chu vi của hình thang là {chu_vi:.2f}")
print(f"Diện tích của hình thang là {dien_tich:.2f}")
