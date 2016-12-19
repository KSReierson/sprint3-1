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
from user import *
from util import *
from question import *
from questionanswer import *

class FAQ(webapp2.RequestHandler):
    def get(self):
        CurrentUser = self.request.cookies.get("CurrentUser")
        #fromPage self.request.get("fromPage")
        #if fromPage ==
        template = JINJA_ENVIRONMENT.get_template("/Html/faq.html")
        user = self.request.cookies.get("CurrentUser")
        topics = Topic.query().fetch()
        # faqs = list(Topic.query().order(Topic.heading, -Topic.heading))

        template_values = {
            "CurrentUser": CurrentUser ,
            "topics": topics,
        #    "fromPage": fromPage
        }

        self.response.write(template.render(template_values))

    def post(self):
        # if self.request.get("heading") == "" or self.request.get("question") == "" or self.request.get("answer") == "":
        #     self.redirect("/faq")
        #
        # else:
        heading = self.request.get("heading")
        question = self.request.get("question")
        answer = self.request.get("answer")
        topic = Topic.query(Topic.heading==heading).get()
        if topic == None:
            print("in if statement")
            topic = Topic()
            topic.heading = heading
            topic.QAs = []
            topic.put()
        else:
            print("\t\t\t no Topic initialized **************")
        qa = questionAnswer()
        qa.question = question
        qa.answer = answer
        topic.QAs.append(qa)
        print("\n\n\t")
        print(topic)
        qa.put()
        topic.put()
        self.redirect("/faq")
