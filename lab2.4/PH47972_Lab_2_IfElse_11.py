# 11. Nhập một địa chỉ email và kiểm tra xem địa chỉ đó có chứa ký tự @ không.
email = str(input("Nhập vào địa chỉ email: "))
if "@" in email:
    print("Địa chỉ email hợp lệ")
else:
    print("Địa chỉ email không hợp lệ")