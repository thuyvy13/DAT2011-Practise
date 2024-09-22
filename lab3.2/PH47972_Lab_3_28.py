# 28. Kiểm tra key trong dictionary: Nhập một key và kiểm tra xem nó có tồn tại trong dictionary hay không.
my_dict = {
    "name": "Zyy",
    "age": 20,
    "city": "Yên Bái"
}
key_check = input("Nhập key để kiểm tra: ")
if key_check in my_dict:
    print(f"Key {key_check} nằm trong dictionary")
else: 
    print(f"Key {key_check} không nằm trong dictionary")