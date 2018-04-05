from models.Post import Post
from handlers.handler import Handler
import time


class DeletePost(Handler):
    def post(self, post_id):
        post = Post.getById(post_id)

        if not post:
            self.response.out.write("Not a valid post!")

        if not self.user:
            self.redirect('/login')
        
        if post.author != self.user.name:
            self.render("post.html", post = post, title = post.subject, error = "You're not allowed to delete this article!")
            return
        # Delete the post
        post.key.delete()
        time.sleep(0.1)
        self.redirect('/')
