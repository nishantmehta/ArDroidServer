import logging
import ProductInfo

class CartHandler():

    def handleCartUpdates(self, cartid, productid):
        print cartid + productid
        pInfo = ProductInfo()
        productIfo =  pInfo.getProductInfo(productid)
        #call the get product functions and send the info to Rooz's code
        #create logs
        logging.info("cart is " + cartid)
        logging.info("product is " + productid)



    def removeProductFromCart(self, cartId, productId):
        print "this functions will remove the product from cart"


   # def createProductLogs(self, cartID, productID) :


