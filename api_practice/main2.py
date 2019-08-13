#main.py
import webapp2
import random
from google.appengine.api import urlfetch
import json


class GiphyPage(webapp2.RequestHandler):
    def get(self):
        giphy_key = "P8hoyqRvEMd3MBzdREzT19RlwyVSieao"
        endpoint_url = "http://api.giphy.com/v1/gifs/search?q=baby+otter&limit=10&api_key="+ giphy_key
        giphy_response = urlfetch.fetch(endpoint_url).content
        response_as_json = json.loads(giphy_response)
        random_index = random.randint(0, 9)
        gif_image = response_as_json['data'][random_index]['images']['original']['url']
        self.response.write(
          "<html><body><img src='{}'/></body></html>".format(gif_image))



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/tester', GiphyPage)
], debug=True)
