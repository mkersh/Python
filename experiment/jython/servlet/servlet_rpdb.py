"""
This experiment is looking to see how rpdb behaves under a WebApp server like tomcat.
"""
from javax.servlet.http import HttpServlet
import rpdb

class DoWork():
    _Counter = 0 # Class level member. This will be incremented for each call on sayHello across all classes

    @classmethod
    def incClassCounter(cls):
        c = cls._Counter
        c += 1
        cls._Counter = c

    def sayHello(self):
        self.incClassCounter()
        return "<p>Hello I am DoWork {0}</p>".format(self._Counter)


class servlet_rpdb (HttpServlet):
    def doGet(self,request,response):
        self.doPost (request,response)

    def doPost(self,request,response):
        rpdb.set_trace() # The debugger port by default is 4444
        dw = DoWork()
        toClient = response.getWriter()
        response.setContentType ("text/html")
        toClient.println ("<html><head><title>Jython Servlet Test</title>"
        +
        "<body><h1>Servlet Jython Servlet at" +
        request.getContextPath() + "</h1>" + dw.sayHello() + "</body></html>")

    def getServletInfo(self):
        return "Short Description"