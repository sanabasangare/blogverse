#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
from main import *

from google.appengine.ext import ndb


#### Blog key
def blog_key(name = 'default'):
    return ndb.Key('blogs', name)

##### Post contents
class bloginfo(ndb.Model):
    time_created = ndb.DateTimeProperty(auto_now_add = True)
    subject = ndb.StringProperty(required = True)
    content = ndb.TextProperty(required = True)
    creator = ndb.StructuredProperty(User)
    likes = ndb.IntegerProperty(default = 0)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("blogpost.html", p =self)

##### Comments
class Comment(ndb.Model):
    post_id = ndb.IntegerProperty(required = True)
    creator = ndb.StructuredProperty(User)
    content = ndb.StringProperty(required = True)
    time_created = ndb.DateTimeProperty(auto_now_add = True)

#### Likes
class Like(ndb.Model):
    post_id = ndb.IntegerProperty(required = True)
    creator = ndb.StructuredProperty(User)
