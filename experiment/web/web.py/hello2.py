import web
import pdb

urls = (
  '/', 'index',
  '/(.*)', 'index2' # (.*) is a regex match. See index2 below
)

class index:
    def GET(self):
        #pdb.set_trace()
        render = web.template.render('templates/')
        #name = 'Bob'
        # name will match name GET paremeter i.e. http://127.0.0.1?name=Bob
        i = web.input(name=None)
        return render.index(i.name)

class index2:
    def GET(self,name):
        #pdb.set_trace()
        render = web.template.render('templates/')
        return render.index2(name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()