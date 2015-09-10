import web
render = web.template.render('templates/', base ='layout')

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return render.index()

#main method
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
