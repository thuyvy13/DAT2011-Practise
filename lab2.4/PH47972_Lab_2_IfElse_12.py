# 12. Nhập thu nhập và kiểm tra xem thuế suất áp dụng (thí dụ: thu nhập > 10000 là 10%, dưới 10000 là 5%).
thu_nhap = int(input("Nhập thu nhập: "))
if thu_nhap > 10000:
    print("Thuế suất áp dụng là 10%")
else:
    print("Thuế suất áp dụng là 5%")