import logging
import re
from google.appengine.ext import db
from DbModel import productInfo
from random import randint
import json

class ProductInfo():

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
