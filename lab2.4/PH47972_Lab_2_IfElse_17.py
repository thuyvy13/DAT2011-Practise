# 17. Nhập một ký tự và kiểm tra nếu nó là chữ hoa thì chuyển thành chữ thường, ngược lại không thay đổi.
char = input("Nhập vào một ký tự: ")
if char.isupper():
    print(f"Chữ thường: {char.lower()}")
else:
    print("Ký tự không thay đổi")