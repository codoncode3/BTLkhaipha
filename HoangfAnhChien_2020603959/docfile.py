import csv

# Hàm đọc dữ liệu từ file CSV
def read_csv_file(csv_file_path):
    data = {}
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Đọc tiêu đề

        for row in csv_reader:
            user_id, name, interests, location = row
            # Chuyển chuỗi ngăn cách bởi dấu phẩy thành danh sách quyền lợi
            interests_list = interests.split(', ')
            data[user_id] = {'name': name, 'interests': interests_list, 'location': location}

    return data

# Đường dẫn đến file CSV vừa sinh ra
csv_file_path = 'random_users_data.csv'

# Đọc dữ liệu từ file CSV
read_data = read_csv_file(csv_file_path)

# Hiển thị dữ liệu ra màn hình
for user_id, user_data in read_data.items():
    print(f"User ID: {user_id}")
    print(f"Name: {user_data['name']}")
    print(f"Interests: {', '.join(user_data['interests'])}")
    print(f"Location: {user_data['location']}")
    print('-' * 20)
