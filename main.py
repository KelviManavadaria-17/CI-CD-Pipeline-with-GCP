import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("GCCP 2022 - GDSC CHARUSAT")

app = webapp2.WSGIApplication([
    ('/',MainHandler)
], debug = True)
