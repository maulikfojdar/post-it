import time
# Models
from models.Post import Post
from handlers.handler import Handler
from helper import *


class EditPost(Handler):

    def get(self, post_id):
        post = Post.getById(post_id)

        if not post:
            self.response.out.write("Not a valid post!")

        if not self.user:
            self.redirect('/login')

        if post.author != self.user.name:
            self.render("post.html", post = post, title = post.subject, error = "You're not allowed to edit this article!")
            return

        self.render('editpost.html', post = post, post_id = post_id)

    def post(self, post_id):
        # get the key for this blog post
        post = Post.getById(post_id)

        if not post:
            self.response.out.write("Not a valid post!")

        if not self.user:
            return self.redirect('/login')

        if post.author != self.user.name:
            self.render("post.html", post = post, title = post.subject, error = "You're not allowed to edit this article!")
            return

        subject = self.request.get('subject')
        content = self.request.get('content')
       
        if subject and content:
            # update the blog post and redirect to the post page
            post.subject = subject
            post.content = content
            post.put()
            time.sleep(0.1)
            self.redirect('/post/%s' % str(post.key.id()))

        else:
            post_error = "Please enter a subject and the blog content"
            self.render(
                        "editpost.html",
                        subject=subject,
                        content=content,
                        post_error=post_error)
