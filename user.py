import os
import re
import codecs
import random
import string
import webapp2
import jinja2
import hashlib
import hmac

####hash secret
SECRET = "onecage"
from google.appengine.ext import ndb

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$") # valid user
PWD_RE = re.compile(r"^.{3,20}$") # valid password
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$") # valid email

class User(ndb.Model):
    username = ndb.StringProperty(required = True)
    pwd_hash = ndb.StringProperty(required = True)
    email = ndb.StringProperty()

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PWD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)

def users_key(group = 'default'):
    return ndb.Key('users', group)
