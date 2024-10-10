# 23. Truy cập giá trị theo key: Nhập một key và in ra giá trị tương ứng trong dictionary.
my_dict = {
    "name": "Zyy",
    "age": 20,
    "city": "Yên Bái"
}
find_key = input("Nhập một key: ")
print(f"Giá trị của {find_key}:", my_dict.get(find_key, "Key không tồn tại"))