from httplib2 import Http
from urllib import urlencode

def GCMSend(UserGCMID,Message):
    h = Http()
    headers = {'Content-type' : 'application/json' , 'Authorization' : 'key=' + APIKEY} #APIKEY From GCM API
    data = dict(registration_ids = UserGCMID, data=Message) #if didn't work, try registration id to be a list it self
    resp, content = h.request("https://android.googleapis.com/gcm/send", "POST", headers, urlencode(data))
    #return success

