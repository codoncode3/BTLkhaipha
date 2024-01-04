import unittest

import numpy as np
from sklearn.neighbors import NearestNeighbors

from BTL import recommend_friends, read_csv_file


class TestFriendRecommendationSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Đọc dữ liệu và chuẩn bị mô hình KNN trước khi chạy tất cả các test case
        cls.users = read_csv_file('testdata.csv')
        cls.user_features = np.array(
            [[len(user['interests']), len(user['location'])] for user_id, user in cls.users.items()])
        cls.knn_model = NearestNeighbors(n_neighbors=3, metric='euclidean')
        cls.knn_model.fit(cls.user_features)

    def test_recommend_friends(self):
        # Test hàm recommend_friends với một người dùng cụ thể
        user_id_to_recommend = 5
        recommended_friends = recommend_friends(user_id_to_recommend)

        # Kiểm tra xem recommended_friends có hợp lý không
        self.assertIsInstance(recommended_friends, list)
        self.assertTrue(all(isinstance(user_id, int) for user_id in recommended_friends))
        self.assertTrue(all(user_id in self.users for user_id in recommended_friends))
        self.assertNotIn(user_id_to_recommend, recommended_friends)

    # Thêm các test case khác nếu cần


if __name__ == '__main__':
    unittest.main()
