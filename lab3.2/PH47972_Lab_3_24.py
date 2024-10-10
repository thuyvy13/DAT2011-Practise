# 24. Xóa cặp key-value: Nhập một key và xóa cặp key-value đó nếu có.
my_dict = {
    "name": "Zyy",
    "age": 20,
    "city": "Yên Bái"
}
key_value = input("Nhập key để xoá: ")
if key_value in my_dict:
    del my_dict[key_value]
print("Dictionary sau khi xoá:", my_dict)