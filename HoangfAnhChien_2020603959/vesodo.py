import unittest
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import numpy as np
import csv

def read_csv_file(csv_file_path):
    data = {}
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        for row in csv_reader:
            user_id, name, interests, location = row
            interests_list = interests.split(', ')
            data[int(user_id)] = {'name': name, 'interests': interests_list, 'location': location}

    return data

class TestFriendRecommendationSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.users = read_csv_file('random_users_data.csv')
        cls.user_features = np.array([[len(user['interests']), len(user['location'])] for user_id, user in cls.users.items()])
        cls.knn_model = NearestNeighbors(n_neighbors=3, metric='euclidean')
        cls.knn_model.fit(cls.user_features)

    def test_recommend_friends(self):
        user_id_to_recommend = 5
        recommended_friends = self.recommend_friends(user_id_to_recommend)

        self.assertIsInstance(recommended_friends, list)
        self.assertTrue(all(isinstance(user_id, int) for user_id in recommended_friends))
        self.assertTrue(all(user_id in self.users for user_id in recommended_friends))
        self.assertNotIn(user_id_to_recommend, recommended_friends)

        # Vẽ biểu đồ
        labels = ['Is List', 'Int User IDs', 'User IDs in Data', 'Excluded User ID']
        friends_ = [
            isinstance(recommended_friends, list),
            all(isinstance(user_id, int) for user_id in recommended_friends),
            all(user_id in self.users for user_id in recommended_friends),
            user_id_to_recommend not in recommended_friends
        ]
        results = friends_

        # Tạo khoảng trống giữa các cột
        bar_width = 0.4

        # Bar chart
        plt.bar(labels, results, width=bar_width, color=['green' if result else 'red' for result in results], align='center')
        plt.title('Test Results')
        plt.show()

    def recommend_friends(self, user_id):
        user_index = list(self.users.keys()).index(user_id)
        _, indices = self.knn_model.kneighbors([self.user_features[user_index]])
        recommended_friends = [list(self.users.keys())[i] for i in indices[0] if i != user_index]
        return recommended_friends

if __name__ == '__main__':
    unittest.main()
