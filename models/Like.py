from google.appengine.ext import ndb
from models.User import User
from models.Post import Post
from helper import *


class Like(ndb.Model):
    post_id = ndb.StringProperty(required = True)
    author = ndb.StringProperty(required = True)

    @classmethod
    def like(cls, post_id, author):
        l = Like(post_id = str(post_id), author = str(author))
        l.put()
        return l.key.id()

    @classmethod
    def getByPostAndAuthor(cls, post_id, author):
        likes = Like.query(Like.post_id == post_id and Like.author == author).fetch(1)
        for like in likes:
            if like.post_id == post_id:
                return like
        return None

    @classmethod
    def countByPostID(cls, post_id):
        likes = Like.query(Like.post_id == post_id)
        return likes.count()

    @classmethod
    def unlike(cls, like_id):
        like = Like.get_by_id(int(like_id))
        if like:
            like.key.delete()
            return True
        else:
            return False