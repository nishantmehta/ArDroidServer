import logging
from  ProductInfo import ProductInfo
from GCM import GCMHandler
from google.appengine.ext import db
import json

class CartHandler():

    def handleCartUpdates(self, cartid, productid):
        print cartid + productid
        pInfo = ProductInfo()
        productInfo =  pInfo.getProductInfo(productid)

        gcmIdCartId = db.GqlQuery("SELECT * from cartGcmMapping where cartId = :1", cartid)

        for data in gcmIdCartId :
            if data.gcmId :
                gcmId = data.gcmId
                logging.info('GCMId' + gcmId)
                logging.info('productInfo' + json.dumps(productInfo))
                gcm = GCMHandler()
                gcm.GCMSend(gcmId, productInfo)
        #create logs
        logging.info("cart is " + cartid)
        logging.info("product is " + productid)



    def removeProductFromCart(self, cartId, productId):
        print "this functions will remove the product from cart"


   # def createProductLogs(self, cartID, productID) :


