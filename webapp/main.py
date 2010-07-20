from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('This app is for test only, access /test-1k/, /test-10k/, /test-1m/ for tests')

class Test1k(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        output = 'a'*1024
        self.response.out.write(output)

class Test10k(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        output = 'a'*10240
        self.response.out.write(output)

class Test1m(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        output = 'a'*1024*1024
        self.response.out.write(output)

application = webapp.WSGIApplication(
                                     [('/', MainPage),
				      ('/test-1k/', Test1k),
				      ('/test-10k/', Test10k),
				      ('/test-1m/', Test1m)],
                                     debug=False)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
