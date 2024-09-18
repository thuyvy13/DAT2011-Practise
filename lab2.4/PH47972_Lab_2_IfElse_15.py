# 15. Dựa trên số tiền nợ nhập vào, kiểm tra xem khách hàng có cần thanh toán ngay không (thí dụ: nợ > 5000 thì cần thanh toán ngay).
tien_no = int(input("Nhập số tiền nợ: "))
if tien_no > 5000:
    print("Cần thanh toán ngay")
else:
    print("Chưa cần thanh toán ngay")