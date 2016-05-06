import os
import sys
import base64
import uuid
import glob
import socket
import platform

if sys.version.startswith("3."):
    # Python 3.x
    from http.server import HTTPServer
else:
    # Python 2.x
    from BaseHTTPServer import HTTPServer

from pysimplesoap.server import SoapDispatcher, SOAPHandler


def getTestImage():
    "Get Test Base64 image"

    with open("TestImage.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return {'base64Image':encoded_string}

def getImagesDir():
    homeDir = os.path.expanduser('~')
    mobileSnapImageDir = homeDir + "/MobileSnaps"
    return mobileSnapImageDir

def getNewImageFileName():
    mobileSnapImageDir = getImagesDir()
    if not os.path.exists(mobileSnapImageDir):
        os.makedirs(mobileSnapImageDir)
    unique_filename = str(uuid.uuid4())
    unique_filename += ".jpg"
    return mobileSnapImageDir + "/" + unique_filename


def saveImage(base64Image):
    "Convert and save Base64 image to a folder"
    imgdata = base64.b64decode(base64Image)
    filename = getNewImageFileName()
    with open(filename, 'wb') as f:
        f.write(imgdata)

def deleteAll():
    "remove all images from the images folder on server"

    imagesPat = getImagesDir() + "/*"
    files = glob.glob(imagesPat)
    for f in files:
        os.remove(f)

def getServerDirectory():
    "return details of machine and folder pictures will be stored on"
    print()
    return platform.system() + "@" + socket.gethostname() + "::" + getImagesDir()

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# register the user function
dispatcher.register_function('getTestImage', getTestImage,
    returns={'base64Image': str},
    args={})
dispatcher.register_function('saveImage', saveImage,
    returns={},
    args={'base64Image':str})
dispatcher.register_function('deleteAll', deleteAll,
    returns={},
    args={})
dispatcher.register_function('getServerDirectory', getServerDirectory,
    returns={'serverfolder':str},
    args={})

def startServer():
    print("Starting server on port 8008...")
    print("Saving images to {0}".format(getImagesDir()))
    httpd = HTTPServer(("", 8008), SOAPHandler)
    httpd.dispatcher = dispatcher
    httpd.serve_forever()

def test():
    deleteAll()
    imgData = getTestImage()
    saveImage(imgData['base64Image'])

if __name__ == '__main__':
    startServer()
    #test()