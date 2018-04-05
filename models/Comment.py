from google.appengine.ext import ndb
from models.User import User
from models.Post import Post
from helper import *


class Comment(ndb.Model):
    post_id = ndb.StringProperty(required = True)
    comment = ndb.TextProperty(required = True)
    author =  ndb.StringProperty(required = True)
    created = ndb.DateTimeProperty(auto_now_add = True)

    @classmethod
    def getByPostID(cls, post_id):
        return Comment.query(Comment.post_id==post_id).order(-Comment.created)

    @classmethod
    def getByID(cls, comment_id):
        return Comment.get_by_id(int(comment_id))

    @classmethod
    def create(cls, post_id, text, author):
        c= Comment(post_id = str(post_id),
                   comment = str(text),
                   author = str(author))
        c.put()
        return c.key.id()

    @classmethod
    def delete(cls, comment_id):
        comment = Comment.get_by_id(int(comment_id))
        if comment:
            comment.key.delete()
            return True
        else:
            return False

    @classmethod
    def countByPostID(cls, post_id):
        comments = Comment.query(Comment.post_id == post_id)
        return comments.count()
        

    def humanDate(self):
        return self.created.strftime('%b %d, %Y at %I:%M %p')