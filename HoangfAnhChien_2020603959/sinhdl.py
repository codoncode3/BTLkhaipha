import csv
import json
import random
from faker import Faker

# Hàm chuyển đổi dữ liệu thành định dạng CSV
def convert_to_csv(csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Ghi tiêu đề của bảng
        header = ['User ID', 'Name', 'Interests', 'Location']
        csv_writer.writerow(header)

        # Sinh dữ liệu người dùng giả định
        fake = Faker()
        num_users = 100

        for user_id in range(1, num_users + 1):
            user_data = {
                'name': fake.name(),
                'interests': random.sample(['music', 'movies', 'sports', 'reading', 'travel'], k=random.randint(1, 3)),
                'location': fake.city(),
            }

            # Chuyển danh sách quyền lợi thành chuỗi ngăn cách bởi dấu phẩy
            interests = ', '.join(user_data['interests'])
            row = [user_id, user_data['name'], interests, user_data['location']]
            csv_writer.writerow(row)

# Chuyển đổi và ghi dữ liệu vào file CSV
convert_to_csv('random_users_data.csv')
