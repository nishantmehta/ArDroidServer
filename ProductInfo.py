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

        prodNames = ['Milk', 'Eggs', 'Rice', 'Chicken Patties', 'Tomato', 'Potato', 'Bread', 'Yogurt', 'Corn Flakes',
                     'Onions', 'Apples']
        for i in range(0, 11):
            prodID = str(i)
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
