"""
SSL instructions from https://www.piware.de/2011/01/creating-an-https-server-in-python/
"""
import sys
if sys.version.startswith("3."):
    # Python 3.x
    from http.server import HTTPServer
else:
    # Python 2.x
    from BaseHTTPServer import HTTPServer
import ssl

from pysimplesoap.server import SoapDispatcher, SOAPHandler

_FXRATE_TABLE = {
    'USD' : {'GBP': 0.789, 'EUR': 0.888},
    'EUR' : {'GBP': 0.8787}
}

def currencyLookup(cur1,cur2):
    fxtable = _FXRATE_TABLE.get(cur1, None)
    destCurr = cur2
    recipricol = False
    if fxtable == None:
        fxtable = _FXRATE_TABLE.get(cur2, None)
        destCurr = cur1
        recipricol = True
    if fxtable == None:
        raise Exception("No FX Rates for currency") 
    fxRate = fxtable[destCurr]
    if recipricol:
        fxRate = 1 / fxRate
    return {'buy': fxRate,'sell':fxRate}

def getFXRate(cur1,cur2):
    "Get FX from cur1 to cur2"
    #return {'FXResult':{'buy':"0.1324", 'sell':"0.1555"}}
    return {'FXResult':currencyLookup(cur1,cur2)}
    #return "0.2425"

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# register the user function
dispatcher.register_function('GetFXRate', getFXRate,
    returns={'FXResult': {'buy': str, 'sell': str}}, 
    #returns={'FXResult': str}, 
    args={'cur1': str,'cur2': str})

def startServer():
    print("Starting HTTPS server on port 4443...")
    httpd = HTTPServer(("", 4443), SOAPHandler)
    httpd.dispatcher = dispatcher
    httpd.socket = ssl.wrap_socket (httpd.socket, certfile='server.pem', server_side=True)
    httpd.serve_forever()

def printResult(dict):
    for i in dict:
        print("{0}:{1}".format(i,dict[i]))
def test():
    printResult( getFXRate('GBP','EUR') )

if __name__ == '__main__':
    #test()
    startServer()