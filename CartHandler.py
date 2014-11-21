import logging
import json
from  ProductInfo import ProductInfo
from GCM import GCMHandler
from google.appengine.ext import db
from DbModel import PurchaseLogs


class CartHandler():

    cartGcmMap = {}
    cartUserMap = {}

    def addProductToCart(self, cartid, productid, timeStamp):


        logging.info("cartId is " + cartid + " productId is " + productid)

        productInfo =  ProductInfo.getProductInfoFromStore(productid,"add")#default is walmart
        logging.info('productInfo being added ' + json.dumps(productInfo))

        userId = None
        gcmId = None

        # making a db call for the first call and using cache for the next
        if cartid not in CartHandler.cartGcmMap.keys() :
            gcmIdCartId = db.GqlQuery("SELECT * from CartGcmMapping where cartId = :1", cartid)
            for data in gcmIdCartId :
                    gcmId = data.gcmId
                    CartHandler.cartGcmMap[cartid] = gcmId
                    logging.info('gcmId ' + gcmId)
                    userId = data.userId
                    CartHandler.cartUserMap[cartid] = userId
                    logging.info('userId ' + userId)
        else :
            gcmId = CartHandler.cartGcmMap[cartid]
            userId = CartHandler.cartUserMap[cartid]
            logging.info('gcmId ' + gcmId + ' userId ' + userId)

        if userId :
            self.addPurchaseLogs(userId, productid, timeStamp, "add")

        if gcmId :
            GCMHandler.GCMSend(gcmId, productInfo)




    def removeProductFromCart(self, cartid, productid, timeStamp):

        logging.info("cartId is " + cartid + "productId is " + productid)

        productInfo =  ProductInfo.getProductInfoFromStore(productid,"remove")
        logging.info('productInfo being removed ' + json.dumps(productInfo))

        userId = None
        gcmId = None

        # making a db call for the first call and using cache for the next
        if cartid not in CartHandler.cartGcmMap.keys() :
            gcmIdCartId = db.GqlQuery("SELECT * from CartGcmMapping where cartId = :1", cartid)
            for data in gcmIdCartId :
                    gcmId = data.gcmId
                    CartHandler.cartGcmMap[cartid] = gcmId
                    logging.info('gcmId ' + gcmId)
                    userId = data.userId
                    CartHandler.cartUserMap[cartid] = userId
                    logging.info('userId ' + userId)
        else :
            gcmId = CartHandler.cartGcmMap[cartid]
            userId = CartHandler.cartUserMap[cartid]
            logging.info('gcmId ' + gcmId + ' userId ' + userId)

        if userId :
            self.addPurchaseLogs(userId, productid, timeStamp, "remove")

        if gcmId :
            GCMHandler.GCMSend(gcmId, productInfo)



    def addPurchaseLogs(self, userId, productId, timeStamp, status) :
        purchaseLog = PurchaseLogs(userId = userId, productId = productId, purchaseTimeStamp = timeStamp, eventType = status)
        purchaseLog.put()






