import web
import os
render = web.template.render('templates/', base ='layout')
db = web.database(dbn = 'sqlite' , db = 'data_base')

urls = (
    '/', 'index',
    '/feed', 'feed',
    '/uploads', 'uploads',
    '/newuser', 'newuser',
    '/login' , 'login',
    '/notloggedin', 'notloggedin'
    )
app = web.application(urls, globals(), True)

class index:
    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        un = form.username
        pw = form.password
        users = db.select('users' , where='name ="' + un + '"')
        if(users[0].password == pw):
            print('login success')
            return render.login(un)
        else:
            print('login failed')
            raise web.seeother('/')
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
class newuser:
    def GET(self):
        return render.newuser()

    def POST(self):
        form = web.input()
        newUsername = form.newUsername
        newPassword = form.newPassword
        db.insert('users' , name = newUsername , password = newPassword)
        raise web.seeother('/feed')
class login:
    def GET(self):
        return render.login()

class notloggedin:
    def GET(self):
        return render.notloggedin()

#main method
if __name__ == '__main__':
    app.run()
