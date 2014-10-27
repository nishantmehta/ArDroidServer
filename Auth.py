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
import cgi
import webapp2
import logging
from AuthProcessing import AuthProcessing

class AuthHandler(webapp2.RequestHandler):

    def get(self):
        requestURL=str(self.request.uri)
        logging.info("URl handle : "+requestURL)

        if ('error=access_denied' in requestURL) :
            logging.info('user did not press accept on consent screen')
        else :
            auth = AuthProcessing()
            auth.extractUserIDAndRegistrationID(requestURL)


app = webapp2.WSGIApplication([
    ('/auth', AuthHandler)
], debug=True)
