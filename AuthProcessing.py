import logging
import re
from google.appengine.ext import db
from DbModel import user

class AuthProcessing():

    def extractUsernameAndPassword(self, requestURL):

        #Regex to read string between state= and &
        regex = re.compile('state=(.*?)&')
        m = regex.search(requestURL)
        userRegistrationID = m.group(1)
        logging.info(m.group(1))

        userID = userRegistrationID.split('_')[0]
        registrationId = userRegistrationID.split('_')[1]
        logging.info('userId, registrationId ' + userID +'  '+ registrationId)
        self.saveUserRegistrationId(userID, registrationId)



    def saveUserRegistrationId(self, userID, registrationId):
        newUser=user(userID=userID, registrationID=registrationId)
        newUser.put()
        # just for checking purpose, have to removed later.
        users = db.GqlQuery("SELECT * from user")
        #logging.info(str(users.count())
        for data in users :
            logging.info(data.userID + ' ' + data.registrationID)




