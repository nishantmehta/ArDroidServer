__author__ = 'nisha_000'

class PairCartRequestObject:
    cartID = 0
    userID = 0

    def __init__(self, cartID, userID):
        self.cartID = cartID
        self.userID = userID

class GetProductLocation:
    cartID = 0
    productName = 0

    def __init__(self, cartID, productName):
        self.cartID = cartID
        self.productName = productName

