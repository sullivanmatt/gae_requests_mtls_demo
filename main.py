import os
import sys
sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))

import webapp2
import logging
import requests

class MainPage(webapp2.RequestHandler):
    def dispatch(self, *args, **kwargs):
        client = ('./client.crt', './client.key')
        result = requests.get("https://54.197.93.2/", verify=False, cert=client)
        self.response.write(result.text)

application = webapp2.WSGIApplication([
    (r'/.*', MainPage),
], debug=True)
