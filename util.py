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

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)


# parse Userstring should return the result of each attempt of makeing a new user
# string would look like

def parseUserString(string):
    subStr = string + ";"

    while subStr != "":
        if subStr[0] == ',':
            return
        userName = subStr[:subStr.find(",")].strip() # We assume that the string does not begin with a comma

        if userName == "":
            return
        if len(list(User.query(User.Name == userName))) != 0:
            return 'User name already exists.'

        #print("Loop")

        subStr = subStr[subStr.find(",") + 1:] # Move the sub string forward
        accountName = userPassword = subStr[:subStr.find(",")].strip() # Get data
        if accountName == "":
            print("accountName was bunkus")
            return
        subStr = subStr[subStr.find(",") + 1:] # Move the sub string forward
        userPassword = subStr[:subStr.find(",")].strip() # Get data
        if userPassword == "":
            print("userPassword was bunkus")
            return
        subStr = subStr[subStr.find(",") + 1:] # Move the sub string forward
        account = subStr[:subStr.find(",")].strip() # Get data
        if account == "":
            print("account was bunkus")
            return
        user = User() # Create the user

        user.Name = userName
        user.userName = accountName
        user.password = userPassword
        user.aType = account
        user.lectures = []
        databaseUser = User.query(User.Name==userName).get()
        if databaseUser == None: # have to check if is in data store
            user.put() # Put to the data store
        subStr = subStr[subStr.find("\n") + 1:] # Equivalent to readline, this just moves to the next line of text

def getAccount(userName):
    user = User.query(User.Name == userName).get()
    return user

def getInstrAccount(uList):
    for i in range(len(uList)):
        if uList[i].aType == "i":
            return uList[i]
