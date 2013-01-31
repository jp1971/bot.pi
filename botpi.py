import cherrypy
import os
import simplejson
import sys

ASSETS_DIR = os.path.join(os.path.abspath("."), u"assets")

class AjaxApp(object):
    def index(self):
        return open(os.path.join(ASSETS_DIR, u'botpi.html'))
    index.exposed = True

    @cherrypy.expose
    def command(self, name):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return simplejson.dumps(dict(title="Command received: %s" % name))
    index.exposed = True        

    @cherrypy.expose
    def exit(self, name):
        cherrypy.engine.exit()
    index.exposed = True        


config = {'/assets':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir': ASSETS_DIR,
                }
        }

cherrypy.tree.mount(AjaxApp(), '/', config=config)
cherrypy.engine.start()
