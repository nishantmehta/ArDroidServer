import logging
import re
import json
from google.appengine.api import urlfetch
from urllib import urlencode
from google.appengine.ext import db
from DbModel import user

"""
This file is used to get the user authenticated by making a http call in the below format

https://accounts.google.com/o/oauth2/auth?scope=email%20profile&redirect_uri=https://mcprojectserver.appspot.com/auth&response_type=code&client_id=
	    CLIENT_ID&state=REGISTRATION_ID

The user will be authenticated and the username(email_id), registration Id will be saved in the database

"""


class AuthProcessing():

    def extractUserIDAndRegistrationID(self, requestURL):

        #Regex to read string between state= and &
        regex = re.compile('state=(.*?)&')
        m = regex.search(requestURL)
        registrationID = m.group(1)
        logging.info('Registration id is :' + m.group(1))

        #Reading Auth code from the redirected URL
        regexCode =  re.compile('&code=(.*?)$')
        m = regexCode.search(requestURL)
        code = m.group(1)
        logging.info('Authorization code given by google server ' + code)

        #getting Access code using the Authorization code
        accessToken = self.getAccessToken(code)

        #getting email id use the Auth code using the googleplus profile endpoint
        if  accessToken :
            userID = self.getEmailId(accessToken)
        else :
             logging.info('accessToken not got from google server')

        if userID :
            logging.info('userId, registrationId ' + userID +'  '+ registrationID)
            self.saveUserRegistrationId(userID, registrationID)
        else :
            logging.info('emailId not found')



    def saveUserRegistrationId(self, userID, registrationId):

        newUser=user(userID=userID, registrationID=registrationId)
        newUser.put()
        # just for testing purposes, have to removed later.
        users = db.GqlQuery("SELECT * from user")
        #logging.info(str(users.count())
        for data in users :
            logging.info(data.userID + ' ' + data.registrationID)
        logging.info(self.isUserValid('12345'))


    # Checking if user, registrationId exists in the database or not.
    def isUserValid(self, registrationId):

         users = db.GqlQuery("SELECT * from user where registrationID = :1", registrationId)
         logging.info(users.count())
         if(users.count() == 1) :
             return True

         return False


    def getAccessToken(self, code):


        token_url = 'https://accounts.google.com/o/oauth2/token'
        payload = {
            'code': code,
            'client_id': '378239996981-nmpgvld6r8d83k0u6nl1822v3ml6hl4f.apps.googleusercontent.com',
            'client_secret': 'c6mAEjDKBFwjbER8XhPv35Xm',
            'redirect_uri': 'https://mcprojectserver.appspot.com/auth',
            'grant_type': 'authorization_code'
        }

        resp = urlfetch.fetch(
            url=token_url,
            payload=urlencode(payload),
            method=urlfetch.POST,
            headers={'Content-Type': 'application/x-www-form-urlencoded'})

        response = json.loads(resp.content)
        accesstoken = None
        try :
            accesstoken = response['access_token']
        except KeyError:
            logging.info('access_token not supplied by google server')
            return

        logging.info('access_token supplied by google server: ' + accesstoken)

        return accesstoken


    def getEmailId(self, accesstoken) :

        userinfo = urlfetch.fetch('https://www.googleapis.com/plus/v1/people/me?access_token='+accesstoken)
        userProfile = json.loads(userinfo.content)
        emailId = None
        try :
         emailId = userProfile['emails'][0]['value']
        except KeyError:
              logging.info('emailId not got from google server')
              return

        logging.info('emailId supplied by google server: ' + emailId)
        return emailId








