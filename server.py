import tornado.ioloop,tornado.web,os
from cadmv import Result,cacheFile,allIdByName,cacheInit

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cache = cacheInit(cacheFile)
        results = []
        for oId in allIdByName:
            result = cache.get(oId,None)
            if not result: continue
            results.append((result.officeId, result.officeName, result.firstDate))
        self.render('index.html', results=results)
        
SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)
application = tornado.web.Application([
    (r"/", MainHandler),
], **SETTINGS)

if __name__ == "__main__":
    application.listen(8888)
    print 'Start server'
    tornado.ioloop.IOLoop.instance().start()
    
