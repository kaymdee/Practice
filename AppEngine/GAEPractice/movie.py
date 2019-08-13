import webapp2
from google.appengine.ext import ndb

class Movie(ndb.Model):
    title = ndb.StringProperty(required=True)
    media_type = ndb.StringProperty(required=True, default="Movie")
    runtime = ndb.IntegerProperty(required=False)
    rating = ndb.FloatProperty(required=False)

    def autoplay(self):
        if (self.runtime_mins<=120) and (self.rating>=9.0):
            return "Up Next: " + self.title
        else:
            return "Search for More Movies"




class MainPage(webapp2.RequestHandler):
    def get(self): #for a GET request =
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
# movie1 = Movie("Inception", 140, 10.0, 2010)
# movie2 = Movie("Intersteller", 169, 8.7, 2014)
# movie3 = Movie("Avengers: End Game", 182, 7.5, 2019)
#
# print(movie1.description())
# print(movie2.description())
# print(movie3.description())

app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the MainPage Handler
], debug=True)
# 
# from google.appengine.ext import ndb
#
# class Movie(ndb.Model):
#     title = ndb.StringProperty(required=True)
#     media_type = ndb.StringProperty(required=True, default="Movie")
#     runtime = ndb.IntegerProperty(required=False)
#     rating = ndb.FloatProperty(required=False)
#
#     def autoplay(self):
#         if (self.runtime<=120) and (self.rating>=9.0):
#             return "Up Next: " + self.title
#         else:
#             return "Search for More Movies"
#
# movie1 = Movie(title="Maze Runner", runtime=131, rating=8.3)
# movie1.put()
#
# movie1.rating = 9.1
# movie1.put()
#
# movie2 = Movie(title="Nameless Gangster", runtime=112, rating=9.7)
# movie2.put()
#
# movie3 = Movie(title="Iron Man", runtime=119, rating=10.3)
# movie3.put()
#
# movie4 = Movie(title="The Outlaws", runtime=120, rating=17.9)
# movie4.put()
#
# print(movie4.autoplay())
