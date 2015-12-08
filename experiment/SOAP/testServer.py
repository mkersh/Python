import sys
if sys.version.startswith("3."):
    # Python 3.x
    from http.server import HTTPServer
else:
    # Python 2.x
    from BaseHTTPServer import HTTPServer

from pysimplesoap.server import SoapDispatcher, SOAPHandler


def adder(a,b):
    "Add two values"
    return a+b

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# register the user function
dispatcher.register_function('Adder', adder,
    returns={'AddResult': str}, 
    args={'a': str,'b': str})

print("Starting server...")
httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()