import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "<html><h1>Wow, such web!</h1> Very HTTP</html>"

#main method
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
