from javax.servlet.http import HttpServlet

class servlet1 (HttpServlet):
    def doGet(self,request,response):
        self.doPost (request,response)

    def doPost(self,request,response):
        toClient = response.getWriter()
        response.setContentType ("text/html")
        toClient.println ("<html><head><title>Jython Servlet Test</title>"
        +
        "<body><h1>YES YES YES IT WORKSServlet Jython Servlet at" +
        request.getContextPath() + "</h1></body></html>")

    def getServletInfo(self):
        return "Short Description"