import web
render = web.template.render('templates/', base ='layout')

urls = (
    '/', 'index',
    '/feed', 'feed',
    '/uploads', 'uploads'
    )
app = web.application(urls, globals(), True)

class index:
    def GET(self):
        return render.index()
class feed:
    def GET(self):
        return render.feed()
class uploads:
    def GET(self):
        return render.uploads()

#main method
if __name__ == '__main__':
    app.run()
