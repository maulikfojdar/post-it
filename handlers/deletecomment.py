from google.appengine.ext import db
import time
from models.User import User
from models.Post import Post
from models.Like import Like
from models.Comment import Comment
from handlers.handler import Handler
from helper import *


class DeleteComment(Handler):
    def post(self, post_id, comment_id):
        if not self.user:
            self.render("/login")
            return
        
        # get the comment from the comment id
        comment = Comment.get_by_id(int(comment_id))
        # check if there is a comment associated with that id
        if comment:
            # check if this user is the author of this comment
            if comment.author == self.user.name:
                # delete the comment and redirect to the post page
                Comment.delete(comment_id)
                time.sleep(0.1)
                self.redirect('/post/%s' % str(post_id))
            # otherwise if this user is not the author of this comment throw an
            # error
            else:
                self.write("You cannot delete other user's comments")
        # otherwise if there is no comment associated with that id throw an
        # error
        else:
            self.write("This comment no longer exists")
