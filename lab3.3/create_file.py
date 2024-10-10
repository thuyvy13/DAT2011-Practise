import os

# MSSV của bạn
mssv = "PH47972"

# Tên thư mục để lưu các file
folder_name = "lab3.3"

# Tạo thư mục nếu chưa tồn tại
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)

# Tạo 30 file với cú pháp [MSSV]_Lab_3_[số bài].py
for i in range(1, 31):
    file_name = f"{mssv}_Lab_3_3_{i}.py"
    file_path = os.path.join(folder_name, file_name)
    
    # Tạo file rỗng
    open(file_path, 'w').close()

