import message
import question
import datetime
import util
import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from user import *
from questionanswer import *
from lecture import *
from message import *
from util import *

class TestPage(webapp2.RequestHandler):
   def get(self):

       test3 = "Passed"
       T = Topic()
       QA = questionAnswer()
       T.heading = "Midterm"
       QA.question = "When is it"
       QA.answer = "NOT TODAY"
       T.QAs.append(QA)
       QA.put()
       T.put()

       Ques = Topic.query(Topic.heading == "Midterm" and questionAnswer.answer == "NOT TODAY")
       test3 = "Passed"



       test2 = "Failed"
       lec = Lecture()
       lec.Name = "CS337"
       lec.userNames = {"arakbar" , "ksr" }
       lec.QL = {QA}
       lec.put()

       lectures = lecture.query(lecture.Name == "CS337")

       test2 = "Passed"



       test1 = "Failed"
       user = User()
       user.Name = "Arham"
       user.userName = "arakbar"
       user.password = "dolphins"
       user.aType = "s"
       user.lectures = {CS337}
       user.put()

       ar = user.query(user.userName == "Arham" and user.password == "dolphins")

       #instead of get, should i be using .fetch and looking for the userName of the object?
       #ar = User.Query(self.Name == "Arham" && self.password == "dolphins")
       assertEqual(user, ar)
       test1 = "Passed"






       test4 = "Passed"
       mess = Message()
       mess.content = "Midterm"
       mess.name = "When is it"
       mess.time= datetime.datetime.now
       mess.put()
       assertNotNull(mess)

       #query stuff hrere
       m= message.query(message.name == "When is it" and message.content == "Midterm")

       assertEqual(m, mess)
       test4 = "Passed"


       template = JINJA_ENVIRONMENT.get_template('test.html')
       template_values = {
           'test1': test1,
           'test2': test2,
           'test3': test3,
           'test4': test4
       }
       self.response.write(template.render(template_values))
