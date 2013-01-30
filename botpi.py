import cherrypy
import os
import simplejson
import sys

ASSETS_DIR = os.path.join(os.path.abspath("."), u"assets")

class AjaxApp(object):
    @cherrypy.expose
    def index(self):
        return open(os.path.join(ASSETS_DIR, u'index.html'))

    @cherrypy.expose
    def submit(self, name):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return simplejson.dumps(dict(title="Hello, %s" % name))

config = {'/media':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir': ASSETS_DIR,
                }
        }

cherrypy.tree.mount(AjaxApp(), '/', config=config)
cherrypy.engine.start()
