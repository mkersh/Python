from pysimplesoap.client import SoapClient, SoapFault

# create a simple consumer
client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", 
    soap_ns='soap',
    ns = False)

# call the remote method
response = client.GetFXRate(cur1="USD", cur2="GBP")

# extract and convert the returned value
result = response.FXResult
#print(type(result).__name__)
#print(dir(result))
print(result.sell)