from handlers.handler import Handler
from models.Post import Post


class MainPage(Handler):

    def get(self):
        q = Post.query().order(-Post.created)
        posts = q.fetch(limit = 10)
        if posts:
            self.render("main.html", posts=posts)
