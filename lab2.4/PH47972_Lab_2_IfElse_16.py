# 16. Nhập số bánh và kiểm tra phương tiện là xe máy, ô tô hay xe đạp.
banh_xe = int(input("Nhập vào số bánh xe: "))
if banh_xe == 2:
    print("Phương tiện là xe đạp hoặc xe máy")
elif banh_xe == 4:
    print("Phương tiện là xe ô tô")
else:
    print("Phương tiện không xác định")