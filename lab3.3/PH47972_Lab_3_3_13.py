# 13. Đếm số lần xuất hiện của ký tự
# Nhập một chuỗi và một ký tự, sau đó đếm số lần ký tự đó xuất hiện trong chuỗi.
chuoi = input("Nhập một chuỗi: ")
ky_tu = input("Nhập ký tự cần đếm: ")
dem = 0 
for i in chuoi:
    if i == ky_tu:
        dem += 1
        
print(f"Ký tự '{ky_tu}' xuất hiện {dem} lần trong chuỗi.")