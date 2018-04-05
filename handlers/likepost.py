from google.appengine.ext import db
from models.User import User
from models.Post import Post
from models.Like import Like
from models.Comment import Comment
from handlers.handler import Handler
from helper import *
import time


class LikePost(Handler):

    def post(self, post_id):
        # check post state (liked or unliked)
        like = Like.getByPostAndAuthor(post_id, self.user.name)

        # You must be authenticated in order to Like or Unlike the post
        if not self.user:
            return self.redirect('/login')

        if like:
            # Unlike the post
            Like.unlike(like.key.id())
        else:
            # Like the post
            Like.like(post_id, self.user.name)
        time.sleep(0.1)
        self.redirect('/post/%s' % post_id)
