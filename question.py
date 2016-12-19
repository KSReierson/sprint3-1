# Library imports
import webapp2
import jinja2
import os
import time
import datetime
import calendar
import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

# Project imports
from message import *
from util import *

# Question
#     student is the name of the student involved in the question
#     topic is a string to be displayed on QL
#     lec is what Lecture the question is to
#     messageList holds message objects. Can be sorted and keeps the order in which they were added.

# Question
#     student is the name of the student involved in the question
#     topic is a string to be displayed on QL
#     lec is what Lecture the question is to
#     messageList holds message objects. Can be sorted and keeps the order in which they were added.

class Question(ndb.Model):
    student = ndb.StringProperty()
    topic = ndb.StringProperty()
    lec = ndb.StringProperty()
    time = ndb.DateTimeProperty()
    answered = ndb.BooleanProperty()

    ML = ndb.StructuredProperty(Message, repeated=True) # ML => Message List

    def toString(self):
        s = (("(")+ self.topic + (",") + self.lec  + (",") + self.time  + (",") + ("{") )
                    # str = str.append(self.content)
                    #        str.append(,)
                    # str.append(self.topic)
                    #str.append(,)
                    # str.append(self.student)
                    #str.append(,)
                    # str.append(self.lec)
                    # str.append(,)
                    # str.append(self.time)
                    #str.append(,)
                    # str.append({)
        for i in self.MessageList.length():
            s.append(i.toString())
            s.append(";")
        s.append("}")
        s.append(")")
        return s
