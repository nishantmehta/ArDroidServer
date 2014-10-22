__author__ = 'nisha_000'
import logging

class ComHandler():
    @staticmethod
    def handleCartUpdates(cartid, productid):
        print cartid + productid
        logging.info( "cart is " + cartid)
        
        logging.info("product is " + productid)

