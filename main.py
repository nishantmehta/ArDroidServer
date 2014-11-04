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
import webapp2
from CartHandler import CartHandler
from GetProductHandler import   GetProductHandler
import RequestObject
import json

#convert this to a rest API
class CartHandle(webapp2.RequestHandler):
    def post(self):
        com = CartHandler()
        CartHandler.handleCartUpdates(com, self.request.get('cartID', ''), self.request.get('productID', ''))

#$/paircart?cartid=1234567&userid=nishantmehta.n
class PairCart(webapp2.RequestHandler):
    def get(self):
        url = self.request.uri
        requestVar = self.getRequestObject(url)
        #call anupam's code to add an entry to the map
        self.response.out.write("{status: OK}")

    def getRequestObject(self, url):
        variables = url.split('?')[-1].split('&')
        return RequestObject.PairCartRequestObject(variables[-1].split('=')[-1],variables[-2].split('=')[-1])


#$/getproductinformation?cartid=1234556&productname=peanutbutter
class GetProductLocation(webapp2.RequestHandler):
    def get(self):
        url = self.request.uri
        requestVar = self.getRequestObject(url)
        #get this info from Anupam's code
        self.response.out.write(json.dumps({"shelf info": "3rd shelf", "aisle": 4}, sort_keys=True))

    def getRequestObject(self, url):
        variables = url.split('?')[-1].split('&')
        return RequestObject.GetProductLocation(variables[-1].split('=')[-1],variables[-2].split('=')[-1])

#get project info API - vishal




app = webapp2.WSGIApplication([
    ('/SendProduct', CartHandle),
    ('/getproductinformation', GetProductLocation),
    ('/pairCart', PairCart)
], debug=True)
