from google.appengine.ext import db
from models.User import User
from models.Post import Post
from models.Like import Like
from models.Comment import Comment
from handlers.handler import Handler
from helper import *
import time


class AddComment(Handler):
    def get(self, post_id):
        if not self.user:
            self.render('/login')
        else:
            self.render("addcomment.html")

    def post(self, post_id):
        if not self.user:
            self.render('/login')
            return

        comment_text = self.request.get("comment_text")
        # check if there is anything entered in the comment text area
        if comment_text:
            # add comment to the comments database and refresh page
            #key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            Comment.create(post_id, comment_text, self.user.name)
            time.sleep(0.1)
            self.redirect('/post/'+post_id)