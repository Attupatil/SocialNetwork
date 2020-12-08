import pymongo
from pymongo import MongoClient


class Posts:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.CodersArena
        self.Users = self.db.users
        self.Posts = self.db.posts

    # This will take data from the text box and put it in mongodb using insert method
    # Made this method private
    def _insert_post(self, data):
        # print('Posting into database!') (For testing)
        inserted = self.Posts.insert_one({'username': data.username, 'content': data.content})
        # print('Posted!') (For testing)
        return True

    def get_all_posts(self):
        all_posts =  self.Posts.find()
        new_posts = []

        for post in all_posts:
            post["user"] = self.Users.find_one({"username":post["username"]})
            new_posts.append(post)

        return new_posts
