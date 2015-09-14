import web
import os
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
        x = os.listdir('static/uploads')
        x.remove('.DS_Store')
        return render.feed(x)
class uploads:
    def GET(self):
        return render.uploads()

    def POST(self):
        x = web.input(myfile={})
        filedir = 'static/uploads' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        raise web.seeother('/feed')

#main method
if __name__ == '__main__':
    app.run()
