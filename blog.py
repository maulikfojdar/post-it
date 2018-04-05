import webapp2
import jinja2
from helper import *

# Models
from models.User import User
from models.Post import Post
from models.Like import Like
from models.Comment import Comment


# Handlers
from handlers.handler import Handler
from handlers.mainpage import MainPage
from handlers.newpost import NewPost
from handlers.signup import Signup
from handlers.login import Login
from handlers.logout import Logout
from handlers.postpage import PostPage
from handlers.likepost import LikePost
from handlers.deletepost import DeletePost
from handlers.editpost import EditPost
from handlers.addcomment import AddComment
from handlers.editcomment import EditComment
from handlers.deletecomment import DeleteComment

app = webapp2.WSGIApplication([
   ('/', MainPage),
   ('/newpost', NewPost),
   ('/signup', Signup),
   ('/login', Login),
   ('/logout', Logout),
   ('/post/([0-9]+)', PostPage),
   ('/post/([0-9]+)/like', LikePost),
   ('/post/([0-9]+)/edit', EditPost),
   ('/post/([0-9]+)/delete', DeletePost),
   ('/post/([0-9]+)/comment', AddComment),
   ('/post/([0-9]+)/comment/([0-9]+)/edit', EditComment),
   ('/post/([0-9]+)/comment/([0-9]+)/delete', DeleteComment)
], debug=True)
