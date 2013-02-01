#Server and AJAX includes
import cherrypy
import os
import simplejson
import sys

#Servo and PWM driver includes
#from Adafruit_PWM_Servo_Driver import PWM
#import time

ASSETS_DIR = os.path.join(os.path.abspath("."), u"assets")

class AjaxApp(object):
    def index(self):
        return open(os.path.join(ASSETS_DIR, u'botpi.html'))
    index.exposed = True

    def command(self, command):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return simplejson.dumps(dict(command="%s" % command))
    command.exposed = True        

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
