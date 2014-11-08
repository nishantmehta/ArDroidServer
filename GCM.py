from httplib2 import Http

try:
    # For c speedups
    from simplejson import loads, dumps
except ImportError:
    from json import loads, dumps

class GCMHandler():
    @staticmethod
    def GCMSend(UserGCMID,Message):
        h = Http()
        headers = { 'Content-type' : 'application/json' ,
                    'Authorization' : 'key=' + 'AIzaSyAa5sLIry4DAILEmtESUjw88eh40urZkog'
                  }; #APIKEY From GCM API
        data = dict(registration_ids = [ UserGCMID ], data = {'message': Message} ) #if didn't work, try registration id to be a list it self
        #print data
        resp, content = h.request("https://android.googleapis.com/gcm/send", "POST", headers = headers, body = dumps(data) )
        return resp, content
        #print resp
        #print content

#GCMSend('APA91bF_JjnHkt3pM3mJHLmITlOwNXYLY0gahJkKetcu2HFnqk3erou0i4wltpdQVxsMrYtpnfnvtXl8c1-T7PCwwBWfBzPLEiyFxt2ZEKmk8e70FnoyKPeGX1Edp6lslxk0LkK2bItCs8RlSgTKgmROH5ITBFuvNw','HELLO!')