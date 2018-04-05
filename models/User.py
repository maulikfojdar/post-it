from google.appengine.ext import ndb
from libs.bcrypt import bcrypt
from helper import *


class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(int(uid))

    @classmethod
    def by_name(cls, name):
        user = User.query(User.name==name).fetch(1)
        for u in user:
            return u

    @classmethod
    def register(cls, name, password, email=None):
        pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        return User(name = name, password = pw_hash, email = email)

    @classmethod
    def login(cls, name, password):
        u = cls.by_name(name)
        # if user exists and his unencrypted password
        # matches one that haspreviously been hashed
        if u and bcrypt.hashpw(password, u.password) == u.password:
            return u
