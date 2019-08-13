#ACCESS VIA HTML::LOCALHOST.8080/...
import jinja2
import webapp2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class EnterInfoHandler(webapp2.RequestHandler):

    def get(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())

    def post(self):
        first_line = self.request.get("user-first-ln")
        second_line = self.request.get("user-second-ln")
        result_template = the_jinja_env.get_template('templates/result.html')
        result_template_dictionary = {
            'title': first_line,
            'caption': second_line,
            'image_url': 'https://meme.xyz/uploads/posts/t/l-15786-always-wash-your-grapes.jpg'
        }

        self.response.write(result_template.render(result_template_dictionary))

 class ShowMemeHandler(webapp2.RequestHandler):
     def post(self):
         results_template = the_jinja_env.get_template('templates/result.html')

        # meme_firs

# result_template_dictionary = {
#     'title': 'Grapes',
#     'caption': 'Mo Grapes!',
#     'image_url': 'https://meme.xyz/uploads/posts/t/l-15786-always-wash-your-grapes.jpg'
#
# }
#
# class ResultHandler(webapp2.RequestHandler):
#
#     def get(self):
#         welcome_template = the_jinja_env.get_template('templates/result.html')
#         self.response.write(welcome_template.render(result_template_dictionary))
#         self.response.write('<h1>Result Meme Handler</h1>')
#


app = webapp2.WSGIApplication([
    ("/", EnterInfoHandler)    #This is the Main page
    #("/memeresult", ResultHandler)
], debug=True)
