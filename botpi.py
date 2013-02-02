#Server and AJAX includes
import cherrypy
import os
import simplejson
import sys

#Servo and PWM driver includes
#from Adafruit_PWM_Servo_Driver import PWM
#import time

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print '%d us per period' % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print '%d us per bit' % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

ASSETS_DIR = os.path.join(os.path.abspath('.'), u'assets')

class AjaxApp(object):
    def index(self):
        return open(os.path.join(ASSETS_DIR, u'botpi.html'))
    index.exposed = True

    def command(self, command):
        if command == 'fwd'
            pwm.setPWM(,,)

        else if command == 'lft'
            pwm.setPWM(,,)     

        else if command == 'stp'
            pwm.setPWM(,,)  

        else if command == 'rgt'
            pwm.setPWM(,,)  

        else if command == 'rev'
            pwm.setPWM(,,)                                         

        cherrypy.response.headers['Content-Type'] = 'application/json'
        return simplejson.dumps(dict(command="%s" % command))
    command.exposed = True             

config = {'/assets':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir': ASSETS_DIR,
                }
        }

cherrypy.tree.mount(AjaxApp(), '/', config=config)
cherrypy.engine.start()
