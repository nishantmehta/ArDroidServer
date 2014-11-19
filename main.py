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
from ProductInfo import ProductInfo
from GCM import GCMHandler
import RequestObject
import json
import logging
from google.appengine.ext import db
from DbModel import cartGcmMapping

#$/sendproduct?cartid=1234567&productid=1234234234
class CartHandle(webapp2.RequestHandler):
    def get(self):
        url = self.request.uri
        productData = url.split('?')[1].split('&')
        cartId = productData[0].split('=')[1]
        productId = productData[1].split('=')[1]
        logging.info('cartId ' + cartId + 'productId ' + productId)
        com = CartHandler()
        CartHandler.handleCartUpdates(com, cartId, productId)
        self.response.out.write("{status: OK}")


#$/paircart?cartid=1234567&userid=nishantmehta.n&gcmid=nvkjdsnjnsdvkjngfkbdfg
class PairCart(webapp2.RequestHandler):
     def get(self):
          url = self.request.uri
          requestVar = self.getRequestObject(url)
          logging.info("gcm id " + requestVar.GCMID + " >>>>>>>>>>>>>>. cart id is " + requestVar.cartID)
          gcmMap = cartGcmMapping(gcmId = requestVar.GCMID,  cartId = requestVar.cartID)
          pairingInfo =  db.GqlQuery("SELECT * from cartGcmMapping where cartId = :1", requestVar.cartID)
          if pairingInfo.count() > 0:
            if pairingInfo.get().gcmId != requestVar.GCMID:
                GCMHandler.GCMSend(pairingInfo.get().gcmId,"Your pairing session has expired!")
                for p in pairingInfo:
                    p.delete()
                gcmMap.put()
          else:
            gcmMap.put()

          #call anupam's code to add an entry to the map
          print requestVar.GCMID

          self.response.out.write("{status: OK}")


     def getRequestObject(self, url):
        variables = url.split('?')[-1].split('&')
        return RequestObject.PairCartRequestObject(variables[0].split('=')[-1],variables[1].split('=')[-1],variables[2].split('=')[-1])

#$/unpaircart?cartid=1234567&userid=nishantmehta.n&gcmid=nvkjdsnjnsdvkjngfkbdfg
class UnPairCart(webapp2.RequestHandler):
     def get(self):
          url = self.request.uri
          requestVar = self.getRequestObject(url)
          gcmIdCartId = db.GqlQuery("SELECT * from cartGcmMapping where cartId = :1", requestVar.cartID)
          db.delete(cartGcmMapping, gcmIdCartId)
          self.response.out.write("{status: OK}")


     def getRequestObject(self, url):
        variables = url.split('?')[-1].split('&')
        return RequestObject.PairCartRequestObject(variables[0].split('=')[-1],variables[1].split('=')[-1],variables[2].split('=')[-1])


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

#getProductINfo API
class ProductInfoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(ProductInfo.getProductInfoFromStore("14401160"))
        """requestURL=str(self.request.uri)
        logging.info("URl handle : "+requestURL)
        pdInfo = ProductInfo()
        productID = self.request.get('productID', '')
        logging.info('productID ' + productID)
        pdInfo.inputProduct()
        pdInfo.getProductInfo(productID)"""

#get project info API - vishal


class GCMTester(webapp2.RequestHandler):
    def get(self):
        url = self.request.uri
        data = url.split('?')
        gcmId = data[1]
        message = data[2]
        logging.info('Gcmid ' + gcmId + 'message '  + message)
        res, cont = GCMHandler.GCMSend(gcmId,message)
        self.response.out.write(res)
        self.response.out.write(cont)

app = webapp2.WSGIApplication([
    ('/sendproduct', CartHandle),
    ('/getproductinformation', GetProductLocation),
    ('/getproductinfo', ProductInfoHandler),
    ('/paircart', PairCart),
    ('/gcmtest',GCMTester)
], debug=True)
