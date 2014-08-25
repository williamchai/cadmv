import tornado.ioloop,tornado.web
from cadmv import Result,cacheFile,allIdByName,cacheInit

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cache = cacheInit(cacheFile)
        self.write("<html><title>cadmv</title>")
        self.write("<body><h3><a href=\"http://williamchai.github.io/cadmv/\">cadmv</a> by williamchai</h3> <table border='1'>")
        for oId in allIdByName:
            result = cache.get(oId,None)
            if not result: continue
            self.write('<tr><td>'+result.officeName+'</td><td>'+result.firstDate+'</td></tr>')
        self.write('</table></body>')
        self.write('</html>')
        
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    print 'Start server'
    tornado.ioloop.IOLoop.instance().start()
    
