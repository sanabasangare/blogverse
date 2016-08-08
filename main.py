import os
import re
import time
import codecs
import jinja2
import hashlib
import hmac
import random
import string
import webapp2

from user import *
from blog import *
from handlers import *

from google.appengine.ext import ndb

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/rot13', Rot13Handler),
    ('/signup', SignupHandler),
    ('/welcome', WelcomeHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/blog', BlogHandler),
    ('/blog/newpost', NewPostHandler),
    ('/blog/([0-9]+)', PostHandler),
    ('/blog/edit', EditPostHandler),
    ('/blog/delete', DeletePostHandler),
    ('/comment/edit', EditCommentHandler),
    ('/comment/delete', DeleteCommentHandler)
], debug=True)
