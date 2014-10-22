__author__ = 'nisha_000'
import webapp2
class MainHandler(webapp2.RequestHandler):

    def get(self):
        print "hi"


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
