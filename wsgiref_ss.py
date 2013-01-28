from wsgiref.simple_server import make_server
import sys, json

def app(environ, start_response):
	result = {'success':'true','message':'The Command Completed Successfully'};

	myjson = json.load(sys.stdin)
	# Do something with 'myjson' object

	print 'Content-Type: application/json\n\n'
	print json.dump(result, sys.stdout)

httpd = make_server('', 8000, app)
print "Serving HTTP on port 8000..."

# Respond to requests until process is killed
httpd.serve_forever()

# Alternative: serve one request, then exit
##httpd.handle_request()
