import jinja2
import webapp2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

story_dict = {
    'name': 'James',
    'adjective': 'hard',
    'noun': 'worker',
    'verb': 'play'
}


class MainPage(webapp2.RequestHandler):
    def get(self):
        story_template = the_jinja_env.get_template('templates/story.html')
        self.response.write(story_template.render(story_dict))
        # self.response.write(story_template.render(story_dict_2))
        # self.response.write(story_template.render(story_dict_3))

class ResultPage(webapp2.RequestHandler):
    def post(self):  # for a post request
        entered_name = self.request.get('entered_name')
        noun = self.request.get('noun')
        verb = self.request.get('verb')

        story_dict['name'] = entered_name
        story_dict['noun'] = noun
        story_dict['verb'] = verb

        story_template = the_jinja_env.get_template('templates/result.html')
        self.response.write(story_template.render(story_dict))  # the response


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/result', ResultPage)

], debug=True)
