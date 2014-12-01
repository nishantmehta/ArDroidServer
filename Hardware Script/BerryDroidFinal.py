import sys
import json
import urllib2
import urllib
from sets import Set

url = 'http://mcprojectserver.appspot.com/sendproduct'
url1 = 'http://mcprojectserver.appspot.com/removeproduct'
productTable = Set([])
cartID = '1042338432'
for productId in sys.stdin:
    productId = productId.strip()
    if productId in productTable:
        print "Removing the product"
        productTable.remove(str(productId))
        productId1 = str(productId)
        i = len(productId1)
        productId = productId1[0: i/2]
        urlGet = url1
        urlGet = urlGet + '?cartid=' + cartID + '&productid=' + productId
        print urlGet
        response = urllib2.urlopen(urlGet)
        html = response.read()
        print html

    else:
        print "Adding the product"
        productTable.add(str(productId))
        productId1 = str(productId)
        i = len(productId1)
        productId = productId1[0: i/2]
        urlGet = url;
        urlGet = urlGet + '?cartid=' + cartID + '&productid=' + productId
        print urlGet
        response = urllib2.urlopen(urlGet)
        html = response.read()
        print html
