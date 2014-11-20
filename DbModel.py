from google.appengine.ext import db


class user(db.Model):
        userID = db.StringProperty(required=True, indexed=True)
        registrationID = db.StringProperty(required=True, indexed=True)
        
class productInfo(db.Model):
        productID = db.StringProperty(required=True, indexed=True)
        productName = db.StringProperty(required=True, indexed=True)
        price = db.StringProperty(required=True, indexed=False)
        discount = db.StringProperty(required=True, indexed=False)
        location = db.StringProperty(required=True, indexed=False)

class PurchaseLogs(db.Model):
        purchaseTimeStamp = db.DateTimeProperty(required= True, indexed= True)
        userId = db.StringProperty(required=True, indexed= True)
        productId = db.StringProperty(required=True, indexed = False)


class CartGcmMapping(db.Model) :
        gcmId = db.StringProperty(required= True, indexed= False)
        cartId = db.StringProperty(required= True, indexed= True)
        userId = db.StringProperty(required= True, indexed= True)
