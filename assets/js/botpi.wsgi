from json import loads, dumps
import sys

def application(environ, response):

	post = json.load(sys.stdin)
	
	status = '200 OK'
	headers = [('Content-type', 'application/json')]

	start_response(status, headers)
	print json.dumps(post) 