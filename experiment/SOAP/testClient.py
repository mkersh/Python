from pysimplesoap.client import SoapClient, SoapFault

# create a simple consumer
client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", 
    soap_ns='soap',
    ns = False)

# call the remote method
response = client.Adder(a=1, b=2)

# extract and convert the returned value
result = response.AddResult
print(result)