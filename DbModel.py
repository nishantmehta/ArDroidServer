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

class purchaseLogs(db.Model):
        purchaseDate = db.DateProperty(required= True, indexed= True)
        userID = db.StringProperty(required=True, indexed= True)
        productID = db.StringProperty(required=True, indexed = False)
        listID = db.StringProperty(required=True, indexed = True)



