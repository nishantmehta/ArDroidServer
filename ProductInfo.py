import logging
import re
from google.appengine.ext import db
from DbModel import productInfo
from random import randint
import json
from httplib2 import Http

class ProductInfo():

    Mappings = dict(walmart= {"14401160":"40439294"} )
    WALMART_API = "http://api.walmartlabs.com/v1/items/"
    WALMART_API_KEY = "?apiKey=xnh83gg5vygkn4pfr4nvqmh4&format=json"

    def getProductInfo(self, prodID):
        logging.info("product is " + prodID)
        products = db.GqlQuery("SELECT * FROM productInfo WHERE productID = :1", prodID)
        logging.info(str(products.count()))
        list = {}
        if(products.count() == 0 or products.count() > 1):
            logging.info('No product information found for the product ID')
            return list
        #Create JSON file here and send back
        else:
            for data in products:
                list = {"productID": data.productID, "productName": data.productName , "Price": data.price,
                        "Discount": data.discount, "location": data.location}
                logging.info(json.dumps(list,))
                return (json.dumps(list))

    @staticmethod
    def getProductInfoFromStore(productID,status,store="walmart"):
        storeMap = ProductInfo.Mappings[store]
        storeProductID = storeMap[productID]
        url = ProductInfo.WALMART_API + storeProductID + ProductInfo.WALMART_API_KEY;
        h = Http()
        headers, content = h.request(url,"GET")
        totalProduct = json.loads(content.decode("utf-8"))
        return {"productID":productID, "productName":totalProduct['name'].encode('utf-8'),"Price":totalProduct['salePrice'],"status":status}#"category":totalProduct['categoryPath'].encode('utf-8')}

    def inputProduct(self):

        prodNames = ['milk', 'beans', 'soya', 'jeans']
        prodId = ['%5B-82,-66,81,24,0,0,7,-32%5D ', '%5B-81,-66,81,24,0,0,7,-32%5D' ,'%5B-80,-66,80,24,0,0,7,-32%5D', '%5B-79,-66,80,24,0,0,7,-32%5D'  ]
        for i in range(len(prodNames)):
            prodID = prodId[i]
            prodName = prodNames[i]
            price = str(randint(1,100))
            discount = str(randint(1,99)/100)
            location = str(randint(1,20))
            newProd = productInfo(productID=prodID, productName=prodName, price=price, discount=discount, location=location)
            newProd.put()
        # just for testing purposes, have to remove later.
        products = db.GqlQuery("SELECT * from productInfo")
        #logging.info(str(users.count())
        for data in products:
            logging.info(data.productID + ' ' + data.productName)
