import logging
import ProductInfo
import GCMHandler
from google.appengine.ext import db

class CartHandler():

    def handleCartUpdates(self, cartid, productid):
        print cartid + productid
        pInfo = ProductInfo()
        productInfo =  pInfo.getProductInfo(productid)

        gcmIdCartId = db.GqlQuery("SELECT * from cartGcmMapping where cartId = :1", cartid)

        if gcmIdCartId.gcmdId :
            gcmId = gcmIdCartId.gcmId
            logging.info('GCMId' + gcmId)
            logging.info('productInfo' + productInfo)
            gcm = GCMHandler()
            gcm.GCMSend(gcmId, productInfo)
        #create logs
        logging.info("cart is " + cartid)
        logging.info("product is " + productid)



    def removeProductFromCart(self, cartId, productId):
        print "this functions will remove the product from cart"


   # def createProductLogs(self, cartID, productID) :


