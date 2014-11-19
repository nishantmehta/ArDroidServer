
import logging
import json
class GetProductHandler():


    def getProcuctLocation(self,request, cartid, productid):
        logging.info("cart is " + cartid)
        logging.info("product is " + productid)
        request.response.out.write(json.dumps({"shelf info": "3rd shelf", "aisle": 4}, sort_keys=True))
        request.response.out.write(str(request.request.uri))


    def removeProductFromCart(self, cartId, productId):
        print "this functions will remove the product from cart"
