from httplib2 import Http

try:
    # For c speedups
    from simplejson import loads, dumps
except ImportError:
    from json import loads, dumps

def GCMSend(UserGCMID,Message):
    h = Http()
    headers = { 'Content-type' : 'application/json' ,
                'Authorization' : 'key=' + 'AIzaSyAa5sLIry4DAILEmtESUjw88eh40urZkog'
              }; #APIKEY From GCM API
    data = dict(registration_ids = [ UserGCMID ], data = {'message': Message} ) #if didn't work, try registration id to be a list it self
    print data
    resp, content = h.request("https://android.googleapis.com/gcm/send", "POST", headers = headers, body = dumps(data) )
    print resp
    print content

GCMSend('APA91bE4Kglfn6ntxLdewmSpsAI1rwnrYpffjWR_KpYGfnWhYFgxphZz3_j4-KvW2y6rYTAeqZfgvBmL-rnPIyAXbdbMxsc2y597bDVAM1YF8COBHvMVoJM6P-x2OQLFmlWvIWx24svxDlm6WeIn7ZqsTiSDKi7WhA','HELLO!')