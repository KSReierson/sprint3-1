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
from util import *
from instructorcenter import *
from studentcenter import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)

class Login(webapp2.RequestHandler):
    def get(self):
        error = ""
        uNm = self.request.cookies.get("CurrentUser")
        uPwd = self.request.get('uPass')
        print(uNm)

        if self.request.cookies.get("CurrentUser") == None:
            uNm = self.request.get('uName')

        if uNm == "":
            error = "Invalid UserName and Password"
            template = JINJA_ENVIRONMENT.get_template('/Html/login.html')
            template_values = {
                "user": uNm,
                "error": error
            }
            self.response.write(template.render(template_values))
            error
        else:
            if User.query(User.Name == uNm).get().aType == 's':
                self.redirect('/studentcenter')

            elif User.query(User.Name == uNm).get().aType == 'i':
                self.redirect('/instructorcenter')

            elif User.query(User.Name == uNm).get().aType == 'a':
                self.redirect('/instructorcenter')


    def post(self):
        uNm = self.request.get("uName")
        uPwd = self.request.get('uPass')

        query = list(User.query(User.Name == uNm, User.password == uPwd))
        print(query)

        if len(query) != 0:
            if query[0].aType == "i":
                self.response.set_cookie("CurrentUser", uNm, path="/")

                self.redirect("/instructorcenter")

            elif query[0].aType == "a":
                self.response.set_cookie("CurrentUser", uNm, path="/")
                self.redirect("/instructorcenter")
          
            elif query[0].aType == "s":
                self.response.set_cookie("CurrentUser", uNm, path="/")
                self.redirect("/studentcenter")

            else:
                self.redirect("/")

        if len(query) == 0:
            self.redirect("/")

    def checkName(self, name):
        if "?" in name or "&" in name or "+" in name:
            return False

        return True
