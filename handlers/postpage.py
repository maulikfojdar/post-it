from handlers.handler import Handler
from models.Post import Post
from models.Comment import Comment
from models.Like import Like

# View a specific post by it's id
class PostPage(Handler):
    def get(self, post_id):
        post = Post.getById(post_id)

        if not post:
            self.error(404)
            self.write("<h1>404 Not Found</h1>The resource could not be found.")
            return

        comments = Comment.getByPostID(post_id)
        comments_count = Comment.countByPostID(post_id)

        likes_num = Like.countByPostID(post_id)
        # Get post status (liked or not) by a specific user
        like_btn_txt = "Like"
        if self.user:
            if Like.getByPostAndAuthor(post_id, self.user.name):
                like_btn_txt = "Unlike"

        self.render("post.html", post = post, comments_count = comments_count, comments = comments, likes_num = likes_num, like_text = like_btn_txt)
