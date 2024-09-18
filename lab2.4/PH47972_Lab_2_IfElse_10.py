# 10. Dựa trên số lượng hàng hóa nhập vào, kiểm tra xem phí giao hàng có miễn phí hay không (thí dụ: > 5 sản phẩm thì miễn phí)
san_pham = int(input("Nhập vào số lượng hàng hoá: "))

if san_pham > 5:
    print(f"{san_pham} sản phẩm được miễn phí giao hàng")
else:
    print(f"{san_pham} sản phẩm không được miễn phí giao hàng")
