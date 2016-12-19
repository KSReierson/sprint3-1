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

class InstructorCenter(webapp2.RequestHandler):
    def get(self):
        CurrentUser = getAccount(self.request.cookies.get('CurrentUser'))
        # idk if the next line is relevent or not. it seems I'm getting an outdated 'CurrentUser' unless I do this.
        instructor = User.query(User.Name == CurrentUser.Name).get()
        QL = []
        SL = []
        LL = instructor.lectures

        #QL.append(Question.query(Question.lec == 'cs361').fetch()
        for lecName in instructor.lectures: # this is a list of Lecture names
            lec = Lecture.query(Lecture.name==lecName).get()
            if lec == None:
                lec = Lecture()
                lec.QL = []
            for QuestionKey in lec.QL:
                print(QuestionKey)
                key = ndb.Key(urlsafe=QuestionKey)       # construct key
                q = key.get()
                print("\t\tprint q=key.get()\n")
                print(q)
                print("\t\tend current question q")
                QL.append(q)                    #append QL with
            for name in lec.userNames:
                if name not in SL:
                    S = User.query(User.Name==name).get()
                    if S != None:
                        if S.aType == 's':
                            SL.append(name)
            print("\t\t\tend current question q")

        # for lecName in instructor.lectures:
        #     lec = Lecture.query(Lecture.name==lecName).get()                         # get lecture from name
        #     for name in lec.userNames:
        #         if not SL.contains(username):
        #             SL.append(username)

        template = JINJA_ENVIRONMENT.get_template('Html/insc.html')
        template_values = {
            "CurrentUser": instructor, # instructor's info is updated and now you have the User object
            'QL': QL,
            'SL': SL,
            'LL': LL
        }
        self.response.write(template.render(template_values))

    def post(self):

        q = Question()
        m = Message()
        m.name = self.request.cookies.get("CurrentUser")
        m.content = self.request.get('content')
        q.time = datetime.datetime.now()
        q.lec = self.request.get("lecture")
        q.student = self.request.get("student")
        q.topic = self.request.get("topic")
        q.answered = False
        q.ML.append(m)
        lec = Lecture.query(Lecture.name==q.lec).get()
        print(lec)
        print(q)
        key = q.put().urlsafe()
        if lec != None:
            if lec.QL == None:
                lec.QL = []
            lec.QL.append(key)
            m.put()
            q.put()
            lec.put()
        self.redirect('/instructorcenter')

    # wont work because defining own method. make a class
    # def goToChat(self):
    #     print('entering goToChat')
    #     questionKeyString = self.request.get('Quest')
    #     print('printing key string')
    #     print(questionKeyString)
    #     questionKey = ndb.Key(urlsafe=questionKeyString)
    #     question = questionKey.get()
    #     print('printing topic')
    #     print(question.topic)
    #     template_values = {
    #          'user'
    #     }
