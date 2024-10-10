# 22. Nhập một ngày trong tuần và kiểm tra xem đó có phải là cuối tuần không (thí dụ: thứ bảy hoặc chủ nhật).
day = input("Nhập một ngày trong tuần: ").lower()
if day == "thứ bảy" or day == "chủ nhật":
    print(f"{day} là ngày cuối tuần")
else: 
    print(f"{day} không phải là ngày cuối tuần")