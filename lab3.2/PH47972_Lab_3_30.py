# 30. Lọc dictionary: Tạo một dictionary và lọc các cặp key-value theo một điều kiện cho trước.
my_dict = {
    "name": "Zyy",
    "age": 20,
    "city": "Yên Bái"
}
filter_dict = {k: v for k, v in my_dict.items() if len(str(v)) > 3}
print("Dictionary sau khi lọc (value dài hơn 3 ký tự):", filter_dict)