# 20. Nhập tên người dùng và mật khẩu và kiểm tra xem thông tin đăng nhập có chính xác không (thí dụ: tên người dùng là "user" và mật khẩu là "pass").
username = input("Nhập tên người dùng: ")
password = input("Nhập mật khẩu: ")

if username == "user" and password == "pass":
    print("Đăng nhập thành công.")
else:
    print("Tên người dùng hoặc mật khẩu không chính xác.")

