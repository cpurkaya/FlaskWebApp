from flask import Flask #from flask module import Flask class

app = Flask(__name__) #create an object of flask class

@app.route("/")  #root dir
@app.route("/home")
def home():
    return "<h1>hello world</h1>"

@app.route("/about") #adding an about route
def about():
    return "<h5>About Page</h5>"

if __name__ == '__main__': #if it is run directly and not if imported onto other py file
    app.run(debug=True) #debug=True because to not restart the web server each time we make a change akshita