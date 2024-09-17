# 24. Viết một chương trình yêu cầu người dùng nhập diện tích theo đơn vị feet vuông (ft²) và chuyển đổi diện tích đó thành mét vuông (m²). Xuất kết quả ra màn hình.
dien_tich = float(input("Nhập diện tích theo đơn vị feet vuông (ft²): "))
met_vuong = dien_tich * 0.092903
print(f"Diện tích {dien_tich} ft² tương đương với {met_vuong:.2f} m²")
