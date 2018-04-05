import jinja2

from google.appengine.ext import ndb
# Post Model
class Post(ndb.Model):
    subject = ndb.StringProperty(required = True)
    content = ndb.TextProperty(required = True)
    author  = ndb.StringProperty(required = True)
    created = ndb.DateTimeProperty(auto_now_add = True)
    updated = ndb.DateTimeProperty(auto_now = True)

    # New line to <br> - Render newlines without security issues ;)
    def nl2br(self):
        # Escape, then convert newlines to br tags, then wrap with Markup object
        # so that the <br> tags don't get escaped.
        def escape(s):
            # unicode() forces the conversion to happen immediately,
            # instead of at substitution time (else <br> would get escaped too)
            return unicode(jinja2.escape(s))
        return jinja2.Markup(escape(self.content).replace('\n', '<br>'))

    def humanDate(self):
        return self.created.strftime('%b %d, %Y')

    @classmethod
    def getById(cls, post_id):
        return Post.get_by_id(int(post_id))