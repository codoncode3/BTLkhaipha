import tkinter as tk
from tkinter import Label, Button, Listbox, Scrollbar, END

from sklearn.neighbors import NearestNeighbors

from BTL import read_csv_file, recommend_friends


class FriendRecommendationDemo:
    def __init__(self, master):
        self.master = master
        master.title("Friend Recommendation Demo")

        # Đọc dữ liệu từ file CSV
        self.users = read_csv_file('random_users_data.csv')

        # Feature extraction
        self.user_features = np.array([[len(user['interests']), len(user['location'])] for user_id, user in self.users.items()])

        # KNN model training
        self.knn_model = NearestNeighbors(n_neighbors=3, metric='euclidean')
        self.knn_model.fit(self.user_features)

        # Giao diện
        self.label = Label(master, text=f"Recommended friends for User5: ")
        self.label.pack()

        self.listbox = Listbox(master, width=40, height=10)
        self.listbox.pack()

        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.update_recommendations()

        self.refresh_button = Button(master, text="Refresh", command=self.update_recommendations)
        self.refresh_button.pack()

    def update_recommendations(self):
        user_id_to_recommend = 5
        recommended_friends = recommend_friends(user_id_to_recommend)

        # Hiển thị kết quả trên giao diện
        self.listbox.delete(0, END)  # Xóa danh sách cũ
        for friend_id in recommended_friends:
            friend_name = self.users[friend_id]['name']
            self.listbox.insert(END, f"User{friend_id}: {friend_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FriendRecommendationDemo(root)
    root.mainloop()
