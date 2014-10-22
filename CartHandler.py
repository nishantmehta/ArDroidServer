
import logging

class CartHandler():

    def handleCartUpdates(self, cartid, productid):
        print cartid + productid
        logging.info( "cart is " + cartid)
        logging.info("product is " + productid)

    def removeProductFromCart(self, cartId, productId):
        print "this functions will remove the product from cart"