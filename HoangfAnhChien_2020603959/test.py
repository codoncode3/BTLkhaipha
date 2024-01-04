from sklearn.neighbors import NearestNeighbors
import numpy as np
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
            data[int(user_id)] = {'name': name, 'interests': interests_list, 'location': location}

    return data

# Đường dẫn đến file CSV vừa sinh ra
csv_file_path = 'random_users_data.csv'

# Đọc dữ liệu từ file CSV
users = read_csv_file(csv_file_path)

# Sample friendships
friendships = [
    (1, 2),
    (1, 3),
    (2, 4),
    # Add more friendships...
]

# Feature extraction
user_features = np.array([[len(user['interests']), len(user['location'])] for user_id, user in users.items()])

# KNN model training
knn_model = NearestNeighbors(n_neighbors=3, metric='euclidean')
knn_model.fit(user_features)


# Function to recommend friends
def recommend_friends(user_id):
    user_index = list(users.keys()).index(user_id)
    _, indices = knn_model.kneighbors([user_features[user_index]])

    recommended_friends = [list(users.keys())[i] for i in indices[0] if i != user_index]
    return recommended_friends


# Example usage
user_id_to_recommend = 1
recommended_friends = recommend_friends(user_id_to_recommend)
print(f"Recommended friends for User{user_id_to_recommend}: {recommended_friends}")
